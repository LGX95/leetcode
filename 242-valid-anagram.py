"""Question: https://leetcode.com/problems/valid-anagram/submissions/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if s == t:
            return True
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        if len(s_cnt) != len(t_cnt):
            return False
        for i, j in zip(sorted(s_cnt), sorted(t_cnt)):
            if i != j or s_cnt[i] != t_cnt[j]:
                return False
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    output = Solution().isAnagram(s, t)
    print(f's: {s}, t: {t}, output: {output}')
