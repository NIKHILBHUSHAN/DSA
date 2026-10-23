class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_seen = {}
        max_length = 0

        for right in range(len(s)):
            character = s[right]

            if character in last_seen and last_seen[character] >= left:
                left = last_seen[character] + 1

            last_seen[character] = right

            window_length = right - left + 1
            if window_length > max_length:
                max_length = window_length

        return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # 3
