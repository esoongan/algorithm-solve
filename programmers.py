# LinkedList 구현 210711

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def listSize(self):
        return self.size

    def is_empty(self):
        if self.size != 0:
            return False
        else:
            return True

    def selectNode(self, idx):
        if idx >= self.size:
            print("Index Error")
            return None
        if idx == 0:
            return self.head
        else:
            target = self.head
            for cnt in range(idx):
                target = target.next
            return target

    # 맨 왼쪽에 추가 head를 변경
    def appendLeft(self, value):
        # 연결리스트의 원소가 하나도없는경우 헤드만 추가되는 노드를 가리키도록
        if self.is_empty():
            self.head = Node(value)
        else:
            # 헤드가 가리키던 화살표를 추가되는 노드가 가지는 화살표로 바꿔준다.
            self.head = Node(value, self.head)
        self.size += 1

    # 맨 오른쪽에 추가
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        else:
            # 현재의 헤드다음 노드 -> 맨마지막 노드를 향해 간다.
            target = self.head
            while target.next != None:
                target = target.next
            # 맨 마지막에 추가될 노드이므로 두번째인자는 주지않는다. -> None으로 초기화
            newTail = Node(value)
            target.next = newTail
            self.size += 1

    #idx에 새로운노드 추가 ->
    # idx이전노드의 next가 가리키던 값을 자신의 next로
    # idx이전노드의 next는 자신으로
    def insert(self, value, idx):
        if self.is_empty():
            self.head = Node(value)
            self.size += 1
        else:
            target = self.selectNode(idx-1)
            newNode = Node(value)
            newNode.next = target.next
            target.next = newNode
            self.size += 1

    def delete(self, idx):
        if self.is_empty():
            print("삭제할 노드가 없다.")
            return
        elif idx>= self.size:
            print("인덱스에러")
            return
        elif idx == 0:
            target = self.head
            self.head = target.next
            del(target)
            self.size -=1
        else:
            target = self.selectNode(idx-1)
            deltarget = target.next
            target.next = deltarget.next
            del(deltarget)
            self.size -=1

    def printlist(self):
        target = self.head
        while target:
            if target.next != None:
                print(target.data, '->', end=" ")
                target = target.next
            else:
                print(target.data)
                target = target.next # None


mylist = SingleList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendLeft('E')
mylist.printlist()
print(mylist.listSize())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendLeft('A')
mylist.printlist()

# A
# A -> B
# A -> B -> C
# A -> D -> B -> C
# E -> A -> D -> B -> C
# 5
# A -> D -> B -> C
# A -> D -> B
# D -> B
# A -> D -> B












