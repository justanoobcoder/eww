#!/usr/bin/env python

import subprocess
import bisect

tags = {
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

existed_tags = [1, 2, 4, 8, 16, 32, 64, 128, 256]
selected_tag = int(subprocess.check_output("~/.config/eww/scripts/dwm-dump-all | grep current | head -n 1 | awk -F' ' '{print $2}'", 
                                shell=True).decode('utf-8').rstrip('\n'))
occupied_num = int(subprocess.check_output("~/.config/eww/scripts/dwm-dump-all | grep occupied | head -n 1 | awk -F' ' '{print $2}'", shell=True).decode('utf-8').rstrip('\n'))
occupied_tags = []

index = len(existed_tags) - 1
while occupied_num > 0:
    if occupied_num - existed_tags[index] >= 0:
        occupied_tags.append(existed_tags[index])
        occupied_num -= existed_tags[index]
    index -= 1
occupied_tags = occupied_tags[::-1]

if selected_tag not in occupied_tags:
    bisect.insort(occupied_tags, selected_tag)

box = '(box :class "tag_class" :orientation "h" :spacing 5 :space-evenly "true" '

for i in occupied_tags:
    if i == selected_tag:
        btn = '(button :class "selected_tag" :onclick "dwm-msg run_command view ' + str(i) + '" "' + tags[i] + '")'
    else:
        btn = '(button :class "occupied_tag" :onclick "dwm-msg run_command view ' + str(i) + '" "' + tags[i] + '")'
    box += btn

box += ')'

print(box)
