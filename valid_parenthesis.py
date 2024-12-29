class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lists = []
        for element in s:
            if element in ["[", "{", "("]:
                lists.append(element)
            elif element == "}" and len(lists) > 0:
                if lists[-1] == "{":
                    lists.pop()
                else:
                    return False
            elif element == "]" and len(lists) > 0:
                if lists[-1] == "[":
                    lists.pop()
                else:
                    return False
            elif element == ")" and len(lists) > 0:
                if lists[-1] == "(":
                    lists.pop()
                else:
                    return False
            else:
                return False  # Handles mismatched closing bracket or empty stack
        
        return not lists  # Return True if all brackets matched
