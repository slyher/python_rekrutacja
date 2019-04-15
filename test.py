"""
Work interview for python developer
convert: a4g2h6 to: aaaagghhhhhh
"""
import unittest


class StringDecoder:
    def stage_one(self, st: str):  # brute force
        return_string = ''
        for i in range(len(st)):
            if i % 2 == 1:
                for j in range(int(st[i])):
                    return_string += st[i - 1]
        return return_string

    def stage_two(self, st: str):  # lets think about optimisation
        return_string = ''
        for i in range(int(len(st) / 2)):
            st_temp = st[2 * i: 2 * (i + 1)]
            for j in range(int(st_temp[1])):
                return_string += st_temp[0]
        return return_string

    def stage_three(self, st: str):  # more optimisation
        return_string = ''
        for i in range(int(len(st) / 2)):
            for j in range(int(st[2 * i + 1])):
                return_string += st[2 * i]
        return return_string

    def stage_four(self, st: str):  # let it lok nice too
        return_string = ''
        for i in range(len(st)):
            if i % 2 == 0:
                return_string += str(int(st[i + 1]) * st[i])
        return return_string

    def stage_five(self, st: str):  # final version
        return_string = ''
        for i in range(int(len(st) / 2)):
            return_string += str(int(st[2 * i + 1]) * st[2 * i])
        return return_string

    def stage_six(self, st: str):  # regexp bonus :P
        import re
        return_string = ''
        for st_temp in re.findall(r"\D+\d+", st):
            return_string += str(int(st_temp[1]) * st_temp[0])
        return return_string


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        self.string_decoder = StringDecoder()

    def testForStageOneDecoder(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        s = "a4g2h6"
        assert self.string_decoder.stage_one(s) == "aaaagghhhhhh"

    def testForStageTwoDecoder(self):
        s = "a4g2h6"
        assert self.string_decoder.stage_two(s) == "aaaagghhhhhh"

    def testForStageThreeDecoder(self):
        s = "a4g2h6"
        assert self.string_decoder.stage_three(s) == "aaaagghhhhhh"

    def testForStageFourDecoder(self):
        s = "a4g2h6"
        assert self.string_decoder.stage_four(s) == "aaaagghhhhhh"

    def testForStageFiveDecoder(self):
        s = "a4g2h6"
        assert self.string_decoder.stage_five(s) == "aaaagghhhhhh"

    def testForStageSixDecoder(self):
        s = "a4g2h6"
        assert self.string_decoder.stage_six(s) == "aaaagghhhhhh"


if __name__ == "__main__":
    unittest.main()  # run all tests
