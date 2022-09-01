#!/usr/bin/env python

import subprocess

ws = {
        1: "一",
        2: "二",
        4: "三",
        8: "四",
        16: "五",
        32: "六",
        64: "七",
        128: "八",
        256: "九",
    }

et = [1, 2, 4, 8, 16, 32, 64, 128, 256]
ct = int(subprocess.check_output("./scripts/dwm-dump-all | grep current | head -n 1 | awk -F' ' '{print $2}'", 
                                shell=True).decode('utf-8').rstrip('\n'))

box = '(box :class "workspace_class" :orientation "h" :spacing 5 :space-evenly "true" '

for i in et:
    if i == ct:
        btn = '(button :class "active" :onclick "dwm-msg run_command view ' + str(i) + '" "' + ws[i] + '")'
    else:
        btn = '(button :class "inactive" :onclick "dwm-msg run_command view ' + str(i) + '" "' + ws[i] + '")'
    box += btn

box += ')'

print(box)
