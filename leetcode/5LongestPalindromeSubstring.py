class Solution:
    @classmethod
    def longestPalindrome(self, s: str) -> str:

        map_dic = dict()

        for n, let in enumerate(s):
            if not let in map_dic:
                map_dic[let] =[]
            map_dic[let].append(n)
        
        longest_palindrome = s[0]

        for let, vals in map_dic.items():
            if len(vals)>1:
                combs = self.permutations(vals)
                for b,f in combs:
                    if len(s[b:f+1])>len(longest_palindrome) and s[b:f+1] == s[b:f+1][::-1]:
                        longest_palindrome = s[b:f+1]

            
        return longest_palindrome

    @classmethod
    def permutations(self, l: list) -> list:
        perms = []
        for val1 in l:
            for val2 in l:
                if val2>val1:
                    perms.append((val1,val2))
        return perms


a = Solution.longestPalindrome("1200")
print(a)