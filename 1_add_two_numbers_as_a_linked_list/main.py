# 18 of October 2020
import math


# definition for a singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def add_two_numbers(self, l1, l2):

        number_l1 = 0
        number_l2 = 0

        # 342 = 3*100 + 4*10 + 2*1
        # as we want inverted, its easier so,
        # 2->4->3 will be 2*1 + 4*10 + 3*100 that equals 342

        # transform the list 1 to the number
        tmp = l1
        i = 0
        while tmp:
            number_l1 += int(tmp.val) * (10 ** i)
            tmp = tmp.next
            i += 1

        # transform the list 2 to the number
        tmp = l2
        i = 0
        while tmp:
            number_l2 += int(tmp.val) * (10 ** i)
            tmp = tmp.next
            i += 1

        # add the two numbers
        total = number_l1 + number_l2

        # lets know how many digits the number has by using the log10
        # the log10 of x, tells which number the 10 must be raised to obtain the value of x
        number_of_digits = int(math.log10(total)) + 1

        result_list = None
        aux = None

        for i in range(number_of_digits):
            # extract the units, tens, hundreds, etc...
            # e.g. the unit of the number 807 = 807 / 10**0 % 10
            # the tens = 807 / 10**1 % 10, and so on
            number = int(total / (10 ** i) % 10)

            if aux is None:
                result_list = ListNode(number)
                aux = result_list
            else:
                aux.next = ListNode(number)
                aux = aux.next

        return result_list


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().add_two_numbers(l1, l2)

while result:
    print(result.val)
    result = result.next
