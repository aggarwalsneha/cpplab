'''A  python module to implement Singly Linked List'''

class Node:
    '''A Node class'''
    def __init__(self, data):
        self.data = data
        self.next = None


def create_node(data):
    '''Creates a node'''
    return Node(data)


def input_list():
    '''Inputs the list'''
    head = None
    values_list = list(map(int, input().split()))
    for value in values_list:
        if head is None:
            head = create_node(value)
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = create_node(value)
    return head


def print_list(head):
    '''Prints the list'''
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def middle_element(head):
    '''Impement this method that returns the middle element of 
    the linked list and comment the next line'''
    len=0
    temp=head
    while(temp!=None):
        len=len+1;
        temp=temp.next
    temp=head
    if head!=None:
        mid=len//2
        while mid!=0:
            temp=temp.next
            mid=mid-1
    return temp.data


def main():
    '''Main function'''
    head = input_list()
   # print_list(head)
   # Uncomment the next line
    print(middle_element(head))


if __name__ == '__main__':
    main()
