"""线程安全的LRU cache
"""

import threading
from functools import wraps

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.node_head = None
        self.node_tail = None
        self.map = dict()
        self.lock = threading.Lock()

    def remove_node(self, node):
        #表示是第一个节点
        if node.pre is None:
            self.node_head = node.next
        else:
            node.pre.next = node.next

        #表示是最后一个节点
        if node.next is None:
            self.node_tail = node.pre
        else:
            node.next.pre = node.pre

    def add_head(self, node):
        node.next = self.node_head
        node.pre = None
        if self.node_head:
            self.node_head.pre = node
        self.node_head = node

        if self.node_tail is None:
            self.node_tail = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.lock.acquire()
        try:
            if key not in self.map:
                return -1
            else:
                node = self.map[key]
                # node已经处于头结点
                if node.pre is None:
                    return node.value
                self.remove_node(node)
                self.add_head(node)
                return node.value
        except Exception as e:
            raise e
        finally:
            self.lock.release()

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.lock.acquire()
        try:
            if key in self.map:
                node = self.map[key]
                node.value = value
                # node已经处于头结点
                if node.pre is None:
                    return
                #移动当前节点
                node.pre.next = node.next
                self.remove_node(node)
                self.add_head(node)
                return
            else:
                if self.capacity == 0:
                    return

                if len(self.map) < self.capacity:
                    new_node = Node(key, value)
                    self.map[key] = new_node  # 要记录新节点
                    self.add_head(new_node)
                    return
                else:
                    tail_node = self.node_tail  # 取最后节点
                    old_key, old_value = tail_node.key, tail_node.value
                    tail_node.key = key
                    tail_node.value = value
                    self.map.pop(old_key)
                    self.map[key] = tail_node
                    self.remove_node(tail_node)
                    self.add_head(tail_node)
                    return
        except Exception as e:
            raise e
        finally:
            self.lock.release()