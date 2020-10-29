
''' 实现了一个带头结点（头结点未存放数据）的单向链表，没有涉及到python的高级语法 其中包含了以下功能：

    add_first(self,new_node) 在链表头部插入元素
    add_last(self,new_node)  在链表尾部插入元素
    find_node_by_value(self,value) 通过value值获取节点
    find_node_by_index(self,value) 通过索引获取节点
    insert_after(self,node,value) 在node节点之后插入一个节点值为value的节点
    insert_before(self,node,value)在node节点之前插入一个节点值为value的节点
    delete_by_node(self,node) 删除指定的node
    delete_by_value(self,value) 根据值删除指定的node
    delete_last_N(self,n) 删除倒数第N个节点
    get_middle_node(self) 获取链表的中间节点
    reversed(self) 链表就地反转
    has_ring(self) 检测是否有环
    merge_sorted_list(self,h1,h2) 两个有序链表合并
    __iter__(self) 支持迭代器迭代

    Author:littleloulou

    
'''


''' 链表的节点 '''
class Node:
    def __init__(self,data,next_node=None):
        # 数据字段
        self.__data = data
        # 下一个节点
        self.__next = next_node

        
    @property
    def data(self):
        return self.__data
        
    
    @data.setter
    def data(self,data):
        self.__data = data

        
    @property
    def next_node(self):
        return self.__next


    @next_node.setter
    def next_node(self,next_node):
        self.__next = next_node
            

''' 单链表实现 '''
class SingleLinkedList:
    def __init__(self):
       # 创建一个空的头节点,哨兵节点 
       self.__head = Node(None)

    @property   
    def head(self):
        return self.__head
       
    ''' 在链表头部添加 '''    
    def add_first(self,new_node):
        if new_node:
            new_node.next_node = self.__head.next_node
            self.__head.next_node = new_node

    ''' 在链表尾部添加 '''        
    def add_last(self,new_node):
        if new_node:
            p = self.__head
            # 寻找最后一个节点
            while p.next_node:
                p = p.next_node
            # 当前节点的下一个节点为空时，说明是尾部节点，将新的节点挂载到尾部节点
            p.next_node = new_node
    
    ''' 根据value值获取相应节点 '''        
    def find_node_by_value(self,value):
        p = self.__head
        while p.next_node:
            p = p.next_node
            if p.data == value:
                return p
        return None


    ''' 根据索引获取节点'''
    def find_node_by_index(self,index):
        p = self.__head
        pos = 0
        while p.next_node:
            p = p.next_node
            if pos == index:
                return p
            else:
                pos+=1
        return None    


    ''' 在node节点之后插入一个节点值为value的节点'''
    def insert_after(self,node,value):
        p = self.head
        found = False
        # 先寻找被插入后面的节点
        while p.next_node:
            p = p.next_node
            if p == node:
                found = True
                break
        # 如果找到，p就是被插入的节点
        if found:
            # 新创建一个节点
            new_node = Node(value)
             # p后面的节点挂载到插入节点的后面
            new_node.next_node = p.next_node
             # 插入节点挂载到p节点后面
            p.next_node = new_node

    ''' 节点之前插入 '''
    def insert_before(self,node,value):
        # 从第一个头节点开始
        p = self.head
        while p.next_node:
            # 记录当前节点
            q = p
            # 移动当前节点到后一个节点
            p = p.next_node
            if p == node:
                q.next_node = Node(value)
                q.next_node.next_node = node
                break
                
    ''' 删除指定的node '''
    def delete_by_node(self,node):
        p = self.head
        while p.next_node:
            q = p
            p = p.next_node
            if p == node:
                # 把待删除节点的后序节点挂载到待删除节点的前序节点
                q.next_node = p.next_node
                p = None
                return True
        return False
                
    ''' 根据值删除指定的node '''
    def delete_by_value(self,value):
        p = self.head
        while p.next_node:
            q = p
            p = p.next_node
            if p.data == value:
                 # 把待删除节点的后序节点挂载到待删除节点的前序节点
                q.next_node = p.next_node
                return True
        return False

    ''' 删除倒数第n个元素 '''
    def delete_last_N(self,n):
        fast = self.head
        slow = self.head
        step = 0
        # 快指针移动n步,快指针就比慢指针多n个元素
        while step < n and fast:
            fast = fast.next_node
            step += 1
        # 快慢指针同时移动，直到快指针到链表尾部
        # 移动过程中，快指针始终比慢指针多移动N个元素，当快指针移动到最后一个节点时，
        # 那么慢指针距离最后一个节点还有N个节点，倒数第N个元素也就很好确定
        # 则慢指针slow就是倒数第N个节点的前一个节点,已知要删除节点的前一个节点删除已知节点就很简单了
        if fast:
            while fast.next_node:
                slow = slow.next_node
                fast = fast.next_node
            # 删除倒数第N个节点
            slow.next_node = slow.next_node.next_node
            return True
        else:
            return False
            
    ''' 获取链表中间节点 '''        
    def get_middle_node(self):
        fast = self.head
        slow = self.head
        # fast 每次移动两次
        # slow 每次移动一次
        # 
        while fast and fast.next_node:
            fast = fast.next_node
            if fast:
                fast = fast.next_node
                slow = slow.next_node
            else:
                return slow    
        return slow

    ''' 链表翻转 '''    
    def reversed(self):
            # 基本思想,要想翻转整个链表，则可以从1开始相邻的两个元素以次交换，左边元素用left表示，右边元素用right表示
            # 原始链表 head -->1-->2-->3-->4-->5---> NULL 
            # 第一趟，翻转 1 和 2    2-->1-->2  并且通过 tmp 保存 2的下一个节点 3       tmp(3) --> 4 --> 5 --> None
            # 第二趟，翻转 2 和 3    3-->2-->1-->2  并且通过 tmp 保存 3 的下一个节点 4          tmp(4) --> 5 --> None
            # 第三趟，翻转 3 和 4    4-->3-->2-->1-->2  并且通过 tmp 保存 4 的下一个节点 5             tmp(5) --> None
            # 第四趟，翻转 4 和 5    5-->4-->3-->2-->1-->2  并且通过 tmp 保存 5 的下一个节点 NULL                 tmp(None)
            # 走完四趟，再次判断时right已经为NULL，说明已经翻转完成
            # 此时 head.next_node指向当前的最后一个节点 1,而1还指向2的节点，实际应该是None ，所以需要设置为空 ：self.head.next_node.next_node = None
            # 5-->4-->3-->2-->1-->None
            # 此时的left则为第一个节点，所以让头结点指针指向left :self.head.next_node = left
            # head --> 5-->4-->3-->2-->1-->None 至此翻转完成
        left = self.head.next_node
        # 不是空链表
        if left: 
            right = left.next_node
            while right:
                # 保存right的下一个节点到tmp
                tmp = right.next_node
                # 调换right 和 left 相邻元素
                right.next_node = left
                # 更新相邻元素
                left = right
                right = tmp

            # 更新最后一个元素指向
            self.head.next_node.next_node = None
            # 更新头节点指向
            self.head.next_node = left
        
    ''' 判断是否有环 '''    
    def has_ring(self):
        fast = self.head
        slow = self.head
        # 快慢指针的方式，快指针每次移动两步，慢指针每次移动一步，如果在移动过程中慢指针和快指针相遇，则说明存在环，而且最早
        # 的相遇应该是发生在慢指针移动了1圈，而快指针移动了2圈
        # 还记的大学时候的400米环形跑到吗，小红和小绿从起点同时出发，小绿的速度是小红的2倍，当小红跑完400米时，即是一圈，首次回到起点
        # 而此时的小绿已经跑了小红里程的2倍800米，同样位于起点处，只不过小绿是第二次到达起点，所以由于是环形跑道，小红和小绿相遇。
        while fast and fast.next_node:
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                return True
        return False       


    ''' 支持 for in 遍历 '''
    def __iter__(self):
        node = self.head.next_node
        while node:
            yield node.data
            node = node.next_node
        


    ''' 打印链表中的所有元素 '''
    def print_element(self):
        p = self.head.next_node
        res = []
        while p :
            res.append(p.data)
            p = p.next_node
        print(res)

    ''' 合并两个有序链表 '''                    
    def merge_sorted_list(self,h1,h2):
        if not h1 or not h2:
            return Node
        # 如果是两个非空链表，则进行合并
        if h1.next_node and h2.next_node:
            # 记录两个链表
            p1 = h1.next_node
            p2 = h2.next_node
            merged_head = Node(Node)
            current = merged_head
            while p1 and p2:
                # 如果链表1的数值小于等于链表2，则把当前链表1的节点放到新的链表当前节点后面
                if p1.data <= p2.data:
                    current.next_node = p1
                    p1 = p1.next_node
                else:
                    current.next_node = p2
                    p2 = p2.next_node
                    
                # 移动当前新的链表到下一个位置    
                current = current.next_node
            # 凡是两个列表进行了比较，都会出现首先有一个链表指向空，所以非空的直接挂载到合并链表的结尾
            current.next_node = p1 if p1 else p2
            # 返回新的头节点 
            return merged_head         
        else:
            return h1 or h2            
            
         
        
# 创建一个单向链表
l = SingleLinkedList()      
#for el in range(1,6):
#      l.add_first(Node(el))

for el in range(1,6):
      l.add_last(Node(el))

#l.print_element()
''' 测试通过value获取node
n1 = l.find_node_by_value(-1) 
n2 = l.find_node_by_value(1)  
n3 = l.find_node_by_value(5)        
n4 = l.find_node_by_value(6)  

print("Get," if n1 else "Not Found,","Get," if n2 else "Not Found,","Get," if n3 else "Not Found,","Get it," if n4 else "Not Found,")
'''

''' 测试通过index获取Node
n1 = l.find_node_by_index(-1) 
n2 = l.find_node_by_index(0)  
n3 = l.find_node_by_index(4)        
n4 = l.find_node_by_index(5)  

print(n1.data if n1 else "Not Found,",n2.data if n2 else "Not Found,",n3.data if n3 else "Not Found,",n4.data if n4 else "Not Found,")
'''

''' 测试后向插入
l.print_element()

e0 = l.find_node_by_index(0)
l.insert_after(e0,101)
l.print_element()

e2 = l.find_node_by_index(2)
l.insert_after(e2,102)
l.print_element()

e6 = l.find_node_by_index(6)
l.insert_after(e6,105)
l.print_element()

l.insert_after(Node(100),10)
l.print_element()

'''

''' 测试前向插入
l.print_element()

e0 = l.find_node_by_index(0)
l.insert_before(e0,101)
l.print_element()

e2 = l.find_node_by_index(2)
l.insert_before(e2,102)
l.print_element()

e6 = l.find_node_by_index(6)
l.insert_before(e6,105)
l.print_element()

l.insert_before(Node(100),10)
l.print_element()
'''

'''
l.print_element()

for e in range(1,6):
    node = l.find_node_by_value(e)
    l.delete_by_node(node)
l.print_element()


e1 = l.find_node_by_value(1)
l.delete_by_node(e1)
l.print_element()

e2 = l.find_node_by_value(2)
l.delete_by_node(e2)
l.print_element()

e5 = l.find_node_by_value(5)
l.delete_by_node(e5)
l.print_element()

l.delete_by_node(Node(1))
l.print_element()

'''

'''
l.print_element()
l.delete_by_value(1)
l.print_element()

l.print_element()
l.delete_by_value(3)
l.print_element()


l.print_element()
l.delete_by_value(5)
l.print_element()

l.print_element()
l.delete_by_value(0)
l.print_element()
'''

'''
# 验证获取倒数第N个元素
l.print_element()
if l.delete_last_N(10):
    l.print_element()

l.print_element()
l.delete_last_N(2)
l.print_element()

l.print_element()
l.delete_last_N(3)
l.print_element()
'''

'''
# 验证获取中间节点
l.print_element()

middle = l.get_middle_node()

print('middle:',middle.data)

'''

'''
# 验证列表反转
l.print_element()
l.reversed()
l.print_element()
'''

'''
# 验证环
l.print_element()
print(l.has_ring())
'''

'''
# head 节点挂载到最后一个节点，构造环
l.find_node_by_value(5).next_node = l.head
print(l.has_ring())
'''



# 验证两个有序列表合并
l1 = SingleLinkedList()
l2 = SingleLinkedList()

for x in range(1,6):
    l1.add_last(Node(x))
    l2.add_last(Node(x+3))

l1.print_element()
l2.print_element()

node = l.merge_sorted_list(l1.head,l2.head)
merged = list()
while node.next_node:
    merged.append(node.next_node.data)
    node = node.next_node
print(merged)




