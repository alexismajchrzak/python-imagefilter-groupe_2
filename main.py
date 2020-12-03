from gray import gray_pic
from dilatation import dilatation_pic
from blur import blur_pic
import sys
import logger
import os

args = sys.argv

for i in range(0, len(args)):
    arg = args[i]
    if arg == '-i':
        dossierE = f'{args[i+1]}'


for i in range(0, len(args)):
        arg = args[i]
        if arg == '-o':
            dossierS = f'{args[i+1]}'
            if not os.path.exists(args[i+1]):
                os.mkdir(args[i + 1])

blur_pic(dossierE, dossierS)
dilatation_pic(dossierE,dossierS)
gray_pic(dossierS, dossierS)



first_arg = args [1]

if first_arg == '-h':
    print(args)
    print('usage: imagefilter')
    print("-h, ---help")
    print("-i, --input-dir <imgs>")
    print("-o, --output-dir <>")
    print("--blur --dilate -- gray")
elif first_arg == '---help':
    print('write "-i" for choose an input dir')
    print('write "-o" for choose an output dir')
    print('write "--blur" to blur the images')
    print('write "--dilate" to dilate the images')
    print('write "--gray" to put the images in black and white')





logger.dump_log()