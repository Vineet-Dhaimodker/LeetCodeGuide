class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=dummy = ListNode()
        while list1 and list2:
            if list1.val<=list2.val:
                curr.next =list1
                list1,curr = list1.next,list1
                
            else:
                curr.next = list2
                list2,curr = list2.next,list2
            
        
        if list1 or list2:
            curr.next = list1 if list1 else list2
        return dummy.next