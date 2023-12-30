class IsPalindrome:
    @staticmethod
    def my_attempt(s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            if not (s[left].isdigit() or s[left].isalpha()):
                left += 1
                continue
            elif not (s[right].isdigit() or s[right].isalpha()):
                right -= 1
                continue
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
