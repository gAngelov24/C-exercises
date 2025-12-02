# Reverse Even-Indexed Nodes and Append : HackerRank

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')



#
# Complete the 'extractAndAppendSponsoredNodes' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def extractAndAppendSponsoredNodes(head):
    # head = [10, 20, 30, 40, 50, 60] -> extract -> evenIdx = [10, 30, 50], oddIdx = [20, 40, 60]
    # reverse evenIdx = [50, 30, 10] -> append to oddIdx -> output = [20, 40, 60, 50, 30, 10]
    # all these operations must happen in one traversal of head / O(n) runtime
    if head is None or head.next is None:
        return head
    evenIdx = []
    oddIdx = []
    i = 0
    prev = head
    curr = head
    reachedEnd = 0
    while curr is not None:
        #print("curr =", curr.data, "- i =", i)
        if i % 2 == 0 and curr.next is not None:
            evenIdx.append(curr.data)
            if i == 0:
                head = curr.next
            else:
                prev.next = curr.next
        else:
            oddIdx.append(curr.data)
        #print("1: evenIdx =", evenIdx)
        i+=1
        prev = curr
        if curr.next is None and reachedEnd == 0:
            reachedEnd = 1
            while len(evenIdx) > 0:
                data = evenIdx[-1]
                node = SinglyLinkedListNode(data)
                curr.next = node
                #print("data =", data, "- curr =", curr.data, "curr.next =", curr.next.data)
                curr = curr.next
                evenIdx.remove(data)
                #print_singly_linked_list(head, " -> ")
                # print("\\n")
                # print("2: evenIdx =", evenIdx)
            return head
        else:
            curr = curr.next
    # while len(evenIdx) != 0:
    #     oddIdx
    # print_singly_linked_list(head, " -> ")
    # print('\\n')
    # print(" - evenIdx =", evenIdx)
    return head
    

if __name__ == '__main__':
    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    result = extractAndAppendSponsoredNodes(head.head)

    print_singly_linked_list(result, '\n')
    print()
