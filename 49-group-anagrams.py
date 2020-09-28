"""Question: https://leetcode.com/problems/group-anagrams/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for word in strs:
            letter_cnt = defaultdict(int)
            for w in word:
                letter_cnt[w] += 1
            anagrams['-'.join(
                '{}:{}'.format(k, v)
                for k, v in sorted(letter_cnt.items()))].append(word)
        return list(anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = Solution().groupAnagrams(strs)
    print(f'strs: {strs}, output: {output}')
