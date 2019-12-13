"""Given a List of words, return the words that can be typed using letters of alphabet
on only one row's of American keyboard like the image below."""


class Solution(object):

    def __init__(self):
        self.lines = [{'e', 'u', 'y', 'o', 'r', 't', 'w', 'q', 'p', 'i'},
                      {'g', 'd', 's', 'k', 'f', 'l', 'a', 'j', 'h'},
                      {'z', 'm', 'c', 'b', 'x', 'n', 'v'}]

    def findWords(self, words):
        res = []
        for word in words:
            is_valid = True
            this_line = None
            for ch in word:

                for i in range(3):
                    if ch in self.lines[i]:
                        if this_line is not None:
                            if this_line != i:
                                is_valid = False
                                break
                        this_line = i
                        continue
            if is_valid:
                res.append(word)
        return res


assert not Solution().findWords(["qwwewm"])
assert Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
