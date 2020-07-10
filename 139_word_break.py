class SolutionNaive:
  # uses recursion + backtracking
  # O(n ^ n) time complexity

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakHelper(s, set(wordDict), 0)

    def wordBreakHelper(self, s, wordDict, start):
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.wordBreakHelper(s, wordDict, end):
                return True

        return False


class SolutionMemo:
    # uses memoization to illiminate multiple calculations
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wordBreakHelper(s, set(wordDict), 0, [None]*len(s))

    def wordBreakHelper(self, s, wordDict, start, memo):
        if start == len(s):
            return True

        if memo[start] != None:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in wordDict and self.wordBreakHelper(s, wordDict, end, memo):
                memo[start] = True
                return True

        memo[start] = False
        return False




import queue

class SolutionBST:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = queue.Queue()
        visited = [False] * len(s)
        q.put(0)
        while(not q.empty()):
            start = q.get()
            if not visited[start]:
                for end in range(start + 1, len(s) + 1):
                    if (s[start:end] in wordDict):
                        if (end == len(s)):
                            return True
                        q.put(end)
            visited[start] = True
        return False



class SolutionDP1:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        m = [[None for j in range(l)] for i in range(l)]

        for i in range (l):
            if s[i] in wordDict:
                m[i][i] = True
            else:
                m[i][i] = False

        i = 0
        j = counter = 1

        while (j < l):
            if s[i:j+1] in wordDict:
                m[i][j] = True
            else:
                for k in range (i, j):
                    if m[i][k] and m[k + 1][j]:
                        m[i][j] = True
                        break;
                if m[i][j] == None:
                    m[i][j] = False;
            j += 1;
            i += 1;
            if j == l:
                i = 0
                counter += 1
                j = counter
        return m[0][l - 1]


# print('\n'.join([' '.join([str(item) for item in row])
#       for row in m]))


class SolutionDPSimple:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True

        for i in range (1, l + 1):
            for j in range(0, i):
                if (dp[j] and s[j: i] in wordDict):
                    dp[i] = True
                    break;

        return dp[l]
