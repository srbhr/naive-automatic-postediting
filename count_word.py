# -*- coding: utf-8 -*-

import re
import os
from collections import Counter


class FrequencyDict:
    def __init__(self):

        # Определяем регулярное выражение для поиска английских слов
        self.wordPattern = re.compile("((?:[a-zA-Z]+[-']?)*[a-zA-Z]+)")

        # Частотный словарь(использум класс collections.Counter для поддержки подсчёта уникальных элементов в последовательностях)
        self.frequencyDict = Counter()

    # Метод парсит файл, получает из него слова
    def ParseBook(self, file):
        if file.endswith("training.en"):
            self.__ParseTxtFile(file, self.__FindWordsFromContent)
        else:
            print('Warning: The file format is not supported: "%s"' % file)

    # Метод парсит файл в формате txt
    def __ParseTxtFile(self, txtFile, contentHandler):
        try:
            with open(txtFile, 'rU') as file:
                for line in file:  # Читаем файл построчно
                    # Для каждой строки вызываем обработчик контента
                    contentHandler(line)
        except Exception as e:
            print('Error parsing "%s"' % txtFile, e)

    # Метод находит в строке слова согласно своим правилам и затем добавляет в частотный словарь
    def __FindWordsFromContent(self, content):
        # В строке найдем список английских слов
        result = self.wordPattern.findall(content)
        for word in result:
            word = word.lower()  # Приводим слово к нижнему регистру
            # Добавляем в счетчик частотного словаря не нормализованное слово
            self.frequencyDict[word] += 1

    # Метод отдает первые countWord слов частотного словаря, отсортированные по ключу и значению

    def FindMostCommonElements(self, countWord):
        dict = list(self.frequencyDict.items())
        dict.sort(key=lambda t: t[0])
        dict.sort(key=lambda t: t[1], reverse=True)
        return dict[0: int(countWord)]
