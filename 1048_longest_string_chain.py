class Solution:
    def longestStrChain(self, words):
        if not words: return 0
        words = sorted(words, key=len)
        dictionary = {}
        max_count = 1
        for word in words:
            if len(word) == 1:
                dictionary[word] = 1
            else:
                curr_count = 1
                for i in range (0, len(word)):
                    sub_word = word[: i] + word[i + 1:]
                    if (sub_word in dictionary and dictionary[sub_word] + 1 > curr_count):
                        curr_count = dictionary[sub_word] + 1
                dictionary[word] = curr_count
                max_count = max(max_count, curr_count)
        return max_count

solution = Solution()
print(solution.longestStrChain(["a","b","ba","bca","bda","bdca"]))
print(solution.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))
