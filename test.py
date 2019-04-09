"""
Work interview for python developer
convert: a4g2h6 to: aaaagghhhhhh
"""
s = "a4g2h6"


def stage_one(st: str):  # brute force
    for i in range(len(st)):
        if i % 2 == 1:
            for j in range(int(st[i])):
                print(st[i - 1], end='')


def stage_two(st: str):  # lets think about optimisation
    for i in range(int(len(st) / 2)):
        st_temp = st[2 * i: 2 * (i + 1)]
        for j in range(int(st_temp[1])):
            print(st_temp[0], end='')


stage_one(s)
print()
stage_two(s)
print()
