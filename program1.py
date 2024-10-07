class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        
        for char in s: 
            if char in pairs.values():
                stack.append(char)
            elif char in pairs.keys():
                if not stack or stack.pop() != pairs[char]:
                    return False
           
        return not stack
        pass







    



  

