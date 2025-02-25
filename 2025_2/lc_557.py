class Solution:
    def reverseWords(self, s: str) -> str:

        c = s.split()

        # for word in c:
        #     c = word[::-1]
        #     print(c)
        reverse = [ word[::-1] for word in c]
        
        return " ".join(reverse)
  