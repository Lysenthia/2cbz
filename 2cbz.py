# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:10:22 2017

@author: Lysenthia
"""

def main():
    import os, zipfile
    cwd = os.getcwd()
    subdirs= []
    [subdirs.append(x[0]) for x in os.walk(cwd)]
    subdirs.pop(0)
    for dir_path in subdirs:
        print(dir_path)
        dirname = dir_path.split(os.path.sep)[-1]
        zipf = zipfile.ZipFile('{}.cbz'.format(dirname), 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                zipf.write(os.path.join(root, file))
        zipf.close()

main()