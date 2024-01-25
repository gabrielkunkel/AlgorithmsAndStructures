class LongestRepeatingCharacterReplacement:

    # https://leetcode.com/problems/longest-repeating-character-replacement/
    @staticmethod
    def my_attempt(s: str, k: int) -> int:
        most_freq_char_count = 0
        character_tab = [0] * 26
        result = 0
        left = 0

        for right in range(len(s)):
            character_tab[ord(s[right]) - 65] += 1
            most_freq_char_count = max(most_freq_char_count, character_tab[ord(s[right]) - 65])

            if right - left + 1 - most_freq_char_count > k:
                character_tab[ord(s[left]) - 65] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result

    @staticmethod
    def random_solution_study(s, k):
        countdict = {}
        left = 0
        res = 0

        for right, char in enumerate(s):
            countdict[char] = 1 + countdict.get(char, 0)

            while (right - left + 1) - max(countdict.values()) > k:  # not good checks ALL values every time; should
                # check just last value
                countdict[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

    @staticmethod
    def my_better_solution(s, k):
        char_hash = {}
        most_freq_char_count = 0
        left = 0
        result = 0

        for right, char in enumerate(s):
            char_hash[char] = char_hash.get(char, 0) + 1
            most_freq_char_count = max(char_hash[char], most_freq_char_count)

            if right - left + 1 - most_freq_char_count > k:
                char_hash[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
