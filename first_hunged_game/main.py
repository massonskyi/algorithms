import re
from collections import Counter


class StringWorked:
    def __init__(self, text: str) -> None:
        self.__text = text

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text

    @property
    def most_long(self) -> str:
        return sorted(self.__text.split(' '), key=lambda x: len(x), reverse=True)[0]

    @property
    def most_popular_word(self) -> str:
        return Counter(self.text.split(' ')).most_common(1)[0][0]

    @property
    def count_special_chars(self):
        return len(re.findall(r'[^\w\s]', self.text))

    def find_palindromes(self):
        words_list = self.text.split(' ')
        palindromes = []
        for word in words_list:
            if word == word[::-1]:
                palindromes.append(word)
        return ', '.join(palindromes)


string = StringWorked(
    "T in L .T T T !in in i@n in in43 in ,,,,,L L L L L L L L L L L L ")
print(string.count_special_chars)
