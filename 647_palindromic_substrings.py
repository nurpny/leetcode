class Solution_Naive:
    ## runs in O(n^2) time
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        i = 0
        while i < len(s):
            if i % 1 == 0:
                count += self.countPalindrome(int(i - 1), int(i + 1), s)
            else:
                count += self.countPalindrome(int(i - 0.5), int(i + 0.5), s)
            i += 0.5
        return count

    def countPalindrome(self, startIdx: int, endIdx: int, s: str) -> int:
        count = 0
        while startIdx >= 0 and endIdx < len(s):
            if s[startIdx] == s[endIdx]:
                count += 1
                startIdx -= 1
                endIdx += 1
            else:
                break
        return count


# https://www.youtube.com/watch?v=EIf9zFqufbU
class SolutionDP:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        count = 0
        # first initiate the dp matrix
        # matrix row represents: starting index
        # matrix column represents: ending index
        # 3 cases:
            # 1) string is of length 1 --> palindrome
            # 2) string is of length 2 --> palindrome if string[start] == string[end]
            # 3) string is of lenggth > 3 --> palindrome if string[start] == string[end] AND string[start + 1 : end - 1] IS a palindrome

        dp = [[None for j in range(l)] for i in range(l)]
        for idx in range(l):
            dp[idx][idx] = True
            count += 1
        for col in range(1, l):
            for row in range(0, col):

                if col - row == 1:
                    if s[col] == s[row]:
                        dp[row][col] = True
                        count += 1
                    else:
                        dp[row][col] = False
                else:
                    if s[col] == s[row] and dp[row + 1][col - 1]:
                        dp[row][col] = True
                        count += 1
                    else:
                        dp[row][col] = False
        return count
