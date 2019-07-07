# -*- coding: utf-8 -*-
s = input()

dm = "dream"
dmr = "dreamer"
er = "erase"
err = "eraser"

s = s.replace(err, "")
s = s.replace(er, "")
s = s.replace(dmr, "")
s = s.replace(dm, "")

if s == "":
    print("YES")
else:
    print("NO")
