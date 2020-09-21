from itertools import product
class Node:
    def __init__(self, data, next_val=None):
        self.data = data
        self.next_val = next_val
    def get_next(self):
        return self.next_val
    def get_data(self):
        return self.data
    def set_next(self, node):
        self.next_val = node


class LinkedList:
    def __init__(self):
        self.head = None
        self.index = 0
    def insert(self, data):
        new_node = Node(data)
        new_node.next_val = self.head
        self.head = new_node
        self.index += 1        
        # print(f'Current _ indexof linked list is {self.index} --- {data}')
    #return kth item q no 1
    def get_kth_to_last(self, idx):
        assert (idx < self.index), f"Length of ll is less than the idx"
        current_node = self.head        
        for _ in range(0, self.index - idx):
            current_node = current_node.get_next()
        return current_node.get_data()

    def sum(self):        
        curr_node = self.head
        sum_val = curr_node.get_data()
        while curr_node is not None:
            curr_node = curr_node.get_node()
            sum += curr_node.get_data()
        return sum_val

    def print_list(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.get_data(), end=" -> ")
            curr_node = curr_node.get_next()
        print()

    def get_end(self):
        end = self.head
        while end.next_val != None:
            end = end.get_next()
        return end

    #no 4 partition
    def partition(self, threshold):
        small_ll = LinkedList()
        larger_ll = LinkedList()        
        curr_head = self.head
        while curr_head is not None:
            if curr_head.get_data() <= threshold:
                small_ll.insert(curr_head.get_data())
                curr_head = curr_head.get_next()
            else:
                larger_ll.insert(curr_head.get_data())
                curr_head = curr_head.get_next()
        small_ll.print_list()
        larger_ll.print_list()
        small_end = small_ll.get_end()
        small_end.set_next(larger_ll.head)        
        return small_ll

    #no 6
    def palindrome(self):        
        if self.head.get_next() is None:
            return True
        elem_list = []
        curr_node = self.head
        while curr_node is not None:
            elem_list.append(curr_node.get_data())
            curr_node = curr_node.get_next()
        string_val = "".join(elem_list)
        if string_val.lower() == string_val[::-1].lower():
            return True
        else:
            return False

    def loop_detection(self):
        one = self.head
        two = self.head
        while one is not None and one.get_next() is not None:
            two = two.get_next()
            if (one == two):                
                break
        if (one is None or one.get_next() is None):
            return None
        two = self.head
        while (two != one):
            two = two.get_next()
            one = one.get_next()
        return one.get_data()

if __name__ == "__main__":
    # val = [''.join(str(i)) for i in list(product(['a','b','c','d'],[1,2,5,4]))]
    val = [1,2,4,6,586,34,2,34,37,37,345]
    ll = LinkedList()
    for i in val:
        ll.insert(i)
    # print(ll.get_kth_to_last(14))
    ll.print_list()
    new_l = ll.partition(34)
    new_l.print_list()
    news = LinkedList()
    for i in list('cba987654321'):
        news.insert(i)
    end = news.get_end()
    end.set_next(news.head)
    # print(news.palindrome())
    print(news.loop_detection())
             
            




