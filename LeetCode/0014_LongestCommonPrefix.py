class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new_str = strs[0]
        for _str in strs[1:]:
            len_str = len(new_str)
            _len_str = len(_str)
            for i in range(len_str):
                if i >= _len_str or new_str[i] != _str[i]:
                    new_str = new_str[:i]
                    break
        return new_str