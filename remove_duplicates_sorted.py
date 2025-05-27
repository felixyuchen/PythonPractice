from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def main():
    head = [1, 1, 2, 3, 3]
    sol = Solution()
    print(sol.delete_duplicates(head))


if __name__ == "__main__":
    main()