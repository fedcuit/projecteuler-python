__author__ = 'edfeng'

single_dict = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight",
               "9": "nine"}
teen_dict = {"10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen",
             "16": "sixteen",
             "17": "seventeen", "18": "eighteen", "19": "nineteen"}
ty_dict = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty",
           "9": "ninety"}
import re

non_letter = re.compile(r'\W')


def read_number(n):
    if n < 10:
        return single_dict[str(n)]

    read = ""
    s = str(n)
    if len(s) == 4 and int(s) >= 1000:
        read += single_dict[s[0]] + ' thousand'
        s = s[1:]
    if len(s) == 3 and int(s) >= 100:
        if read:
            read += ' and '
        read += single_dict[s[0]] + ' hundred'
        s = s[1:]

    if len(s) == 2:
        if read and int(s) != 0:
            read += ' and '
        i = int(s)
        if i >= 20:
            read += ty_dict[s[0]]
            s = s[1:]
            if n % 10 != 0:
                read += '-' + single_dict[s]
        elif 10 <= i < 20:
            read += teen_dict[s]
        elif 0 < i < 10:
            read += single_dict[str(i)]

    return read


def number_of_letters(s):
    return len(re.sub(non_letter, '', s))


def result():
    return sum([number_of_letters(read_number(i)) for i in range(1, 1001)])