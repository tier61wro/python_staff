#!/usr/bin/env python3
import site
data = site.getsitepackages()
for d in data:
    print(d)
