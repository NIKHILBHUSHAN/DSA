"""
LeetCode-style Problem: Sort Characters By Frequency (Manual)

Return characters ordered by descending frequency.
If frequencies tie, either order is accepted.
Build the frequency dictionary and ordering manually.
Forbidden: collections.Counter, sorted(), list.sort(), min(), and imports.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        # Count each character manually.
        frequency = {}
        for ch in s:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        # Collect distinct characters.
        characters = []
        for ch in frequency:
            characters.append(ch)

        # Selection sort by frequency, highest frequency first.
        n = len(characters)
        for i in range(n):
            highest_index = i

            for j in range(i + 1, n):
                if frequency[characters[j]] > frequency[characters[highest_index]]:
                    highest_index = j

            if highest_index != i:
                temp = characters[i]
                characters[i] = characters[highest_index]
                characters[highest_index] = temp

        # Repeat each character according to its frequency.
        answer = ""
        for ch in characters:
            count = frequency[ch]
            for _ in range(count):
                answer += ch

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.frequencySort("tree"))    # "eert" or "eetr"
    print(solution.frequencySort("cccaaa"))  # "cccaaa" or "aaaccc"
    print(solution.frequencySort("Aabb"))    # "bbAa" or "bbaA"
