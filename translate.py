import os
import re
from pathlib import Path

from translate_dict import translate_dict

regexp = re.compile(r'>(.*?)<')


def translate(s):
    s0 = s.strip()
    if s0:
        s1 = translate_dict.get(s0)
        if s1:
            return s.replace(s0, s1)
    matcher = regexp.search(s)
    while matcher:
        g = matcher.group(1)
        s0 = g.strip()
        if s0:
            s1 = translate_dict.get(s0)
            if s1:
                return s[:matcher.start()] + ">" + g.replace(s0, s1) + "<" + s[matcher.end():]
        matcher = regexp.search(s, pos=matcher.end())
    return s


for dirpath, _, filenames in os.walk('brendonmay.github.io'):
    d = Path(dirpath)
    for filename in filenames:
        if filename not in ('index.html', 'main.js', 'outputStats.js'):
            continue
        filepath = d.joinpath(filename)
        lines = []
        with open(filepath, 'r', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if line:
                    lines.append(translate(line))
                else:
                    break
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
