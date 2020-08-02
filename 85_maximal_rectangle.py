class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        row = [0] * len(matrix[0])
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row[j] = row[j] + 1 if matrix[i][j] == "1" else 0
            max_area = max(max_area, self.maxLengthHistogram(row))
        return max_area

    def maxLengthHistogram(self, heights: List[str]) -> int:
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:

                prev_idx = stack.pop()
                curr_area = heights[prev_idx] * (i - stack[-1] - 1)
                max_area = max(max_area, curr_area)
            stack.append(i)
        while stack[-1] != -1:
            prev_idx = stack.pop()
            curr_area = heights[prev_idx] * (len(heights) - stack[-1] - 1)
            max_area = max(max_area, curr_area)
        return max_area
