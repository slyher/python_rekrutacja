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


stage_one(s)
print()
