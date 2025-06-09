from collections import deque, defaultdict

class Environment:
    def __init__(self, world):
        self.world = world
        self.width = len(world[0])
        self.height = len(world)

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(x + dx, y + dy) for dx, dy in directions if self.in_bounds(x + dx, y + dy)]

    def get_percepts(self, x, y):
        return self.world[y][x]  # assumes top-left origin

class InferenceAgent:
    def __init__(self, env):
        self.env = env
        self.knowledge = dict()
        self.visited = set()
        self.safe_to_visit = set()
        self.unsafe = set()
        self.pit_candidates = defaultdict(set)
        self.wumpus_candidates = defaultdict(set)
        self.pit_confirmed = None
        self.wumpus_confirmed = None
        self.current = (0, 3)  # bottom-left
        self.found_gold = False
        self.path = [self.current]

    def infer(self):
        # استنتاج کلاسیک اولیه
        for cell, sources in list(self.pit_candidates.items()):
            if len(sources) >= 2:
                self.pit_confirmed = cell
                self.unsafe.add(cell)

        for cell, sources in list(self.wumpus_candidates.items()):
            if len(sources) >= 2:
                self.wumpus_confirmed = cell
                self.unsafe.add(cell)

        # استنتاج پیشرفته: ومپوس کجاست؟
        stench_sources = [cell for cell in self.visited if 'S' in self.env.get_percepts(*cell)]
        if stench_sources:
            possible_wumpus = set(self.env.neighbors(*stench_sources[0]))
            for src in stench_sources[1:]:
                possible_wumpus &= set(self.env.neighbors(*src))
            if len(possible_wumpus) == 1:
                self.wumpus_confirmed = list(possible_wumpus)[0]
                self.unsafe.add(self.wumpus_confirmed)
                # همسایه‌های سایر خانه‌ها امن هستند اگر ومپوس قطعی شد
                for src in stench_sources:
                    for n in self.env.neighbors(*src):
                        if n != self.wumpus_confirmed and n not in self.visited:
                            self.knowledge[n] = 'Safe'
                            self.safe_to_visit.add(n)

        # استنتاج پیشرفته: گودال کجاست؟
        breeze_sources = [cell for cell in self.visited if 'B' in self.env.get_percepts(*cell)]
        if breeze_sources:
            possible_pit = set(self.env.neighbors(*breeze_sources[0]))
            for src in breeze_sources[1:]:
                possible_pit &= set(self.env.neighbors(*src))
            if len(possible_pit) == 1:
                self.pit_confirmed = list(possible_pit)[0]
                self.unsafe.add(self.pit_confirmed)
                for src in breeze_sources:
                    for n in self.env.neighbors(*src):
                        if n != self.pit_confirmed and n not in self.visited:
                            self.knowledge[n] = 'Safe'
                            self.safe_to_visit.add(n)

        # خانه‌هایی که امن هستند
        for (x, y), status in list(self.knowledge.items()):
            if status == 'Safe':
                for nx, ny in self.env.neighbors(x, y):
                    if (nx, ny) not in self.visited and (nx, ny) not in self.safe_to_visit:
                        percepts = self.env.get_percepts(x, y)
                        if 'B' not in percepts and 'S' not in percepts:
                            self.knowledge[(nx, ny)] = 'Safe'
                            self.safe_to_visit.add((nx, ny))

    def get_path_to(self, target):
        queue = deque([(self.current, [self.current])])
        visited = set()
        while queue:
            (cx, cy), path = queue.popleft()
            if (cx, cy) == target:
                return path
            for nx, ny in self.env.neighbors(cx, cy):
                if (nx, ny) not in visited and self.knowledge.get((nx, ny)) == 'Safe' and (nx, ny) not in self.unsafe:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
        return []

    def explore(self):
        while not self.found_gold:
            x, y = self.current
            self.visited.add((x, y))
            percepts = self.env.get_percepts(x, y)
            if 'G' in percepts:
                print(f"🎉 Tala dar khane {x},{3 - y} peida shod!")
                self.found_gold = True
                return
            if 'P' in percepts or 'W' in percepts:
                print(f"💀 Agent dar khane {x},{3 - y} mord be dalil {percepts}!")
                return
            if 'B' in percepts:
                for nx, ny in self.env.neighbors(x, y):
                    self.pit_candidates[(nx, ny)].add((x, y))
            if 'S' in percepts:
                for nx, ny in self.env.neighbors(x, y):
                    self.wumpus_candidates[(nx, ny)].add((x, y))
            if 'B' not in percepts and 'S' not in percepts:
                for nx, ny in self.env.neighbors(x, y):
                    if (nx, ny) not in self.knowledge:
                        self.knowledge[(nx, ny)] = 'Safe'
                        self.safe_to_visit.add((nx, ny))

            self.knowledge[(x, y)] = 'Safe'
            self.infer()

            # فقط خانه‌هایی که ۱۰۰٪ امن هستند
            next_cell = None
            for cell in sorted(self.safe_to_visit):
                if cell not in self.visited and cell not in self.unsafe and self.knowledge.get(cell) == 'Safe':
                    path = self.get_path_to(cell)
                    if path:
                        next_cell = cell
                        break

            if next_cell:
                path = self.get_path_to(next_cell)
                self.path.extend(path[1:])
                self.current = next_cell
            else:
                print("🚫 Hich masir amni baraye edame vojud nadarad.")
                return

# نمونه محیط ارتقایافته
world = [
    ['B', 'B', '', 'G'],
    ['P', 'B', 'S', ''],
    ['B', 'SB', 'S', 'S'],
    ['', 'S', 'W', 'S']
]

env = Environment(world)
agent = InferenceAgent(env)
agent.explore()
print("\n🧭 Masir tay shode:", [(x, 3 - y) for (x, y) in agent.path])
