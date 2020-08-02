class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0] * 1
        heights.append(0)
        # stack will keep track of height and current_width
        stack = [(heights[0], 1)]
        maxArea = 0

        for i in range(1, len(heights)):
            curr_height = heights[i]
            if (curr_height >= stack[-1][0]):
                stack.append((heights[i], 1))
            else:
                counter = 0
                while len(stack) > 0 and stack[-1][0] > curr_height:
                    prev_height, prev_width = stack.pop()
                    curr_area = prev_height * (prev_width + counter)
                    maxArea = max(maxArea, curr_area)
                    counter += prev_width
                stack.append((curr_height, counter + 1))
        return maxArea
