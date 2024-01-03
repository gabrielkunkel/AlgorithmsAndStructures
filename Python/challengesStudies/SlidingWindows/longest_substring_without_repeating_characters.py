class LongestSubstringWithoutRepeatingCharacters:

    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    @staticmethod
    def my_attempt(s: str) -> int:
        longest_count = 0
        tracker = set()
        left = right = 0
        str_length = len(s)

        while right < str_length:
            right_value = s[right]
            while right_value in tracker:
                tracker.remove(s[left])
                left += 1
            tracker.add(right_value)
            longest_count = max(longest_count, right - left + 1)
            right += 1

        return longest_count
