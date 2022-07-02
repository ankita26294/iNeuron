import logging as log

log.basicConfig(filename="tasks_log.log", level=log.DEBUG)


class StringOperations():

    def __init__(self, string):
        self.string = string

    def word_extract(self, string, start, end, jump):
        log.info("Try to extract data from index one to index 300 with jump of 3")
        return string[start:end:jump]

    def reverse_string(self,string):
        rs = string[::-1]
        log.info("the given string is reversed as %s:", rs)
        return rs

    def upper_string(self,string):
        u = string.upper()
        log.info("the given string in uppercase as %s", u)
        return u

    def lower_string(self, string):
        l = string.lower()
        log.info("split a string after conversion of entire string in lowercase")
        return l

    def capitalize_string(self,string):
        c = string.capitalize()
        log.info("capitlize string")
        return c

    def re_char(self,string):
        r =string.replace('y','*')
        log.info("y changes to '*' ")
        return r

try:
    test = StringOperations("this is My First python programming class and i am learNING python string and its function")
    print(test.word_extract(test.string, 0, 300, 3))
    print(test.reverse_string(test.string))
    print(test.upper_string(test.string))
    print(test.lower_string(test.string))
    print(test.capitalize_string(test.string))
    print(test.re_char(test.string))

except Exception as e:
    print(e)

