"""Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999."""


class Solution:

    def romanToInt(self, s: str) -> int:

        roman_mapper = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        res_sum, skip_idx = 0, -1

        for i in range(len(s)):

            if i == skip_idx:
                continue

            if i < len(s) - 1 and s[i:i + 2] in roman_mapper:
                res_sum += roman_mapper[s[i:i + 2]]
                skip_idx = i + 1

                continue

            res_sum += roman_mapper[s[i]]

        return res_sum


sol = Solution()

assert sol.romanToInt('IX') == 9
assert sol.romanToInt('LVIII') == 58
assert sol.romanToInt('MCMXCIV') == 1994
