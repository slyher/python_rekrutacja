"""
Work interview for python developer
convert: a4g2h6 to: aaaagghhhhhh
"""


class StringDecoder:
    def stage_one(self, st: str):  # brute force
        for i in range(len(st)):
            if i % 2 == 1:
                for j in range(int(st[i])):
                    print(st[i - 1], end='')

    def stage_two(self, st: str):  # lets think about optimisation
        for i in range(int(len(st) / 2)):
            st_temp = st[2 * i: 2 * (i + 1)]
            for j in range(int(st_temp[1])):
                print(st_temp[0], end='')

    def stage_three(self, st: str):  # more optimisation
        for i in range(int(len(st) / 2)):
            for j in range(int(st[2 * i + 1])):
                print(st[2 * i], end='')

    def stage_four(self, st: str):  # let it lok nice too
        for i in range(len(st)):
            if i % 2 == 0:
                print(int(st[i + 1]) * st[i], end='')

    def stage_five(self, st: str):  # final version
        for i in range(int(len(st) / 2)):
            print(int(st[2 * i + 1]) * st[2 * i], end='')

    def stage_six(self, st: str):  # regexp bonus :P
        import re
        for st_temp in re.findall(r"\D+\d+", st):
            print(int(st_temp[1]) * st_temp[0], end='')

s = "a4g2h6"
StringDecoder.stage_one(s)
print()
StringDecoder.stage_two(s)
print()
StringDecoder.stage_three(s)
print()
StringDecoder.stage_four(s)
print()
StringDecoder.stage_five(s)
print()
StringDecoder.stage_six(s)
