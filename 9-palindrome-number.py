"""Question: https://leetcode.com/problems/palindrome-number/
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        copy, reverse = x, 0
        while copy:
            reverse *= 10
            reverse += copy % 10
            copy = copy // 10

        return x == reverse

    def isPalindrome_using_str(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    x = 121
    output = Solution().isPalindrome(x)
    print(f'x: {x}\toutput: {output}')

    x = -121
    output = Solution().isPalindrome(x)
    print(f'x: {x}\toutput: {output}')
