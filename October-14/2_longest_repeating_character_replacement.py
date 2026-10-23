class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequencies = {}
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            character = s[right]
            frequencies[character] = frequencies.get(character, 0) + 1

            if frequencies[character] > max_frequency:
                max_frequency = frequencies[character]

            window_length = right - left + 1

            # Characters to replace = window size - count of most frequent char.
            if window_length - max_frequency > k:
                left_character = s[left]
                frequencies[left_character] -= 1
                left += 1
                window_length -= 1

            if window_length > max_length:
                max_length = window_length

        return max_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement("ABAB", 2))       # 4
    print(solution.characterReplacement("AABABBA", 1))    # 4
