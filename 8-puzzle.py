class Node:
    def __init__(self,value,label):
        self.value=value
        self.label=label
        self.up=None
        self.down=None
        self.right=None
        self.left=None
node0=Node(int(input('value suare 0 : ')),'node0')
node1=Node(int(input('value suare 1 : ')),'node1')
node2=Node(int(input('value suare 2 : ')),'node2')
node3=Node(int(input('value suare 3 : ')),'node3')
node4=Node(int(input('value suare 4 : ')),'node4')
node5=Node(int(input('value suare 5 : ')),'node5')
node6=Node(int(input('value suare 6 : ')),'node6')
node7=Node(int(input('value suare 7 : ')),'node7')
node8=Node(int(input('value suare 8 : ')),'node8')
node0.up,node0.down,node0.right,node0.left=None,node3,node1,None
node1.up,node1.down,node1.right,node1.left=None,node4,node2,node0
node2.up,node2.down,node2.right,node2.left=None,node5,None,node1
node3.up,node3.down,node3.right,node3.left=node0,node6,node4,None
node4.up,node4.down,node4.right,node4.left=node1,node7,node5,node3
node5.up,node5.down,node5.right,node5.left=node2,node8,None,node4
node6.up,node6.down,node6.right,node6.left=node3,None,node7,None
node7.up,node7.down,node7.right,node7.left=node4,None,node8,node6
node8.up,node8.down,node8.right,node8.left=node5,None,None,node7
nodes=[node0,node1,node2,node3,node4,node5,node6,node7,node8]
s=[]
found=False
def show():
    v=0
    for i in nodes:
        v+=1
        print(i.value,end=' ')
        if v==3:
            v=0
            print('\n')
def find():
    for i in nodes:
        if i.value==0:
            return i
def change(node,op):
    if op=='up' and node.up is not None:
        node.up.value,node.value=node.value,node.up.value
    if op=='down' and node.down is not None:
        node.down.value,node.value=node.value,node.down.value
    if op=='right' and node.right is not None:
        node.right.value,node.value=node.value,node.right.value
    if op=='left' and node.left is not None:
        node.left.value,node.value=node.value,node.left.value
def movement(max_move):
    global s
    global found
    if node0.value==1 \
    and node1.value==2 \
    and node2.value==3 \
    and node3.value==4 \
    and node4.value==5 \
    and node5.value==6 \
    and node6.value==7 \
    and node7.value==8 \
    and node8.value==0 :
        found=True
        return
    if max_move==0 or found:
        return
    if find().up is not None and not found:
        change(find(),'up')
        s.append('up')
        movement(max_move-1)
        if not found:
            change(find(),'down')
            s.pop()
    if find().down is not None and not found:
        change(find(),'down')
        s.append('down')
        movement(max_move-1)
        if not found:
            change(find(),'up')
            s.pop()
    if find().right is not None and not found:
        change(find(),'right')
        s.append('right')
        movement(max_move-1)
        if not found:
            change(find(),'left')
            s.pop()        
    if find().left is not None and not found:
        change(find(),'left')
        s.append('left')
        movement(max_move-1)
        if not found:
            change(find(),'right')
            s.pop()
show()
while 1:
    movement(int(input('what are the minimum moves ? ')))
    if len(s)!=0:
        print(s)
        break
    print('increas your minimum moves ! ')
print()
show()