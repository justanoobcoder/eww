#!/usr/bin/env python

import subprocess

ws = {
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
    }

aw = subprocess.check_output("hyprctl monitors | grep active | sed 's/()/(1)/g' | sort | awk 'NR>1{print $1}' RS='(' FS=')'", shell=True).decode('utf-8').rstrip('\n')

ew = subprocess.check_output("hyprctl workspaces | grep ID | sed 's/()/(1)/g' | sort | awk 'NR>1{print $1}' RS='(' FS=')'", shell=True).decode('utf-8').replace('\n', '')
ew = list(ew)

box = '(box :class "workspace_class" :orientation "h" :spacing 5 :space-evenly "true" '

for i in ew:
    if i == aw:
        btn = '(button :class "active" :onclick "hyprctl dispatch workspace ' + i + '" "' + ws[int(i)] + '")'
    else:
        btn = '(button :class "inactive" :onclick "hyprctl dispatch workspace ' + i + '" "' + ws[int(i)] + '")'
    box += btn

box += ')'

print(box)
