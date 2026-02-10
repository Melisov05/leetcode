from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            word_len = len(word)
            res += str(word_len) +"#" + word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            j+=1
            start = j
            end = j + length
            res.append(s[start:end])
            i = end

        return res

