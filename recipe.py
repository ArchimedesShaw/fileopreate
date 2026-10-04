#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#RECIPY:"加工点位，X位置，Z位置，X运动速度,Z运动速度"

with open('recipe.txt', 'w', encoding='utf-8') as frecipe:
    frecipe.write('Point1,105,220,800,150\n')
    frecipe.writelines(['Point2,855,238,600,100\n','Point3,1062,266,7500,120\n'])

    
with open('recipe.txt', 'a', encoding='utf-8') as frecipe:
    frecipe.write('Point4,105,220,800,150')

with open('recipe.txt', 'r', encoding='utf-8') as frecipe:
    line = frecipe.readline()
    while line:
        print(line.strip())
        line = frecipe.readline()

with open('recipe.txt', 'r', encoding='utf-8') as frecipe:
    for i,line in enumerate(frecipe,1):
        line = line.strip()
        if not line:
            continue
        print(f'第{i}条:{line}')

with open('recipe.txt', 'r', encoding='utf-8') as frecipe:
    print(frecipe.read())

        
    
