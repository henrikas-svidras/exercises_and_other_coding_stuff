from typing import List
import itertools

class Solution(object):
    @classmethod
    def braceExpansionII(self, expression: str) -> List[str]:
        #print("Input ", expression)

        linearised = [[""]]
        ## Linearise the expression as much as possible

        for symb in expression:
            if symb == '{':
                # Mark the location where bracket opens
                linearised.append(symb)
                linearised.append([""])

            elif symb == ',':
                linearised.append([""])

            elif symb == '}':
                terms_to_be_linearised = []
                while linearised[-1] != '{':
                    terms_to_be_linearised += linearised.pop()
                linearised.pop() # will remove the "{" but not add it

                # Here every term already existing in list will be 
                # added with the terms to be linearised, up to the last bracket
                # This makes sense because if I have a list then the list will simply be extended
                # And if I have 2 terms in a list they will be squashed into one term
                linearised[-1] = [subterm+term for subterm in linearised[-1] for term in terms_to_be_linearised]

            else:
                linearised[-1] = [subterm+symb for subterm in linearised[-1]]
        
        ## Unpack everything and add it to set (will remove doubles automatically)

        res = set()
        while linearised:
            ele = linearised.pop()
            for x in ele:
                res.add(x)
        return sorted(res)


soln = Solution.braceExpansionII("{a,b}{c,{d,e}}")
print(soln)

soln = Solution.braceExpansionII("{{a,z},a{b,c},{ab,z}}")
print(soln)