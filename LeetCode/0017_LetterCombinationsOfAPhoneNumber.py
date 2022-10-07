import itertools
from typing import List


class Solution:
    # Prepare a phone key map
    digit_chars_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # Get charset for the digits
        chars = [self.digit_chars_map[digit] for digit in digits]

        # Create combinations with the cartesian product of charsets
        return ["".join(p) for p in itertools.product(*chars)]
