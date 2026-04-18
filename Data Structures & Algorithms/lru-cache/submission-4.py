class LRUCache:

    class Node:
        def __init__(self,key,value,prev=None,next=None):
            self.key=key
            self.value=value
            self.prev=prev
            self.next=next


    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=LRUCache.Node(-1,-1)
        self.tail=LRUCache.Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.hmap={}
        
    def insert_after_head(self,node):
        end=self.head.next
        node.next=end
        end.prev=node
        self.head.next=node
        node.prev=self.head

    def remove_node(self,node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        # get value from the node
        # remove lru node from its position
        # insert after head
        p = self.hmap[key]
        self.remove_node(p)
        self.insert_after_head(p)
        return p.value

    def put(self, key: int, value: int) -> None:
        if key not in self.hmap:
            if len(self.hmap)==self.capacity:
                #remove lru node
                #insert key after head
                p=self.tail.prev
                self.remove_node(p)
                del self.hmap[p.key]
                self.insert_after_head(p)
                self.hmap[key]=p
                p.key=key
                p.value=value
            else:
                # add lru node after head
                p=LRUCache.Node(key,value)
                self.hmap[key]=p
                self.insert_after_head(p)
        else:
            p=self.hmap[key]
            p.value=value
            self.remove_node(p)
            self.insert_after_head(p)
            # remove lru node
            #insert key after head
