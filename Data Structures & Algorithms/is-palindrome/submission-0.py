class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(filter(str.isalnum, s))
        cleaned_text = cleaned_text.lower()
        for i in range(len(cleaned_text)):
            if cleaned_text[i] == cleaned_text[-i-1]:
                continue
            if cleaned_text[i] != cleaned_text[-i-1]:
                return False
        return True