class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next


  def reverse(self):
      current = self.head
      next_node = current.next
      current.next = None

      while next_node:
          previous_next = next_node.next
          next_node.next = current

          current = next_node
          next_node = previous_next

          if not next_node:
              self.head = current

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(15)
llist.insert_at_beginning(25)
llist.insert_at_beginning(50)
llist.insert_at_beginning(20)
llist.insert_at_beginning(30)
llist.insert_at_beginning(35)
llist.insert_at_beginning(75)
llist.insert_at_beginning(10)
llist.insert_at_beginning(45)
llist.insert_at_beginning(65)
llist.insert_at_beginning(55)
llist.insert_at_beginning(40)
llist.insert_at_beginning(60)
llist.insert_at_beginning(5)
llist.insert_at_beginning(70)

def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next)

    return result

def merge_sort_task(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort_task(head)
    right = merge_sort_task(next_to_middle)

    sorted_list = merge_sorted_lists(left, right)

    return sorted_list


def merge_sort(linked_list: LinkedList):
    ll_sorted = merge_sort_task(linked_list.head)
    new_list = LinkedList()

    new_list.head = ll_sorted

    return new_list



print('Linked list:')
llist.print_list()

llist = merge_sort(llist)
print('Linked list sorted:')
llist.print_list()

llist.reverse()
print("Linked list reversed:")
llist.print_list()
