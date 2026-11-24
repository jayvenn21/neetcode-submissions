class Solution:

    def encode(self, strs: List[str]) -> str:
        li = []
        for word in strs:
            li.append(str(len(word)))
            li.append('#')
            li.append(word)
        return ''.join(li)


    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        res = []
        l, r = 0, 0
        while r < len(s):
            while s[r].isalnum():
                r += 1
            num = int(s[l:r])
            r += 1
            l = r
            for _ in range(num):
                r += 1
            word = s[l:r]
            l = r
            res.append(word)
        return res
            

