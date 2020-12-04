from gray import gray_pic
from dilatation import dilatation_pic
from blur import blur_pic
import sys
import logger
import os

args = sys.argv

# On boucle dans nos arguments, si l'un d'eux est "--dilate",
# notre valeur de dilatation prend celle écrite juste après --dilate
for i in range(0, len(args)):
    arg = args[i]
    if arg == '--dilate':
        dilate_level = int(args[i+1])

# On boucle dans nos arguments, si l'un d'eux est "--blur",
# notre notre valeur de flou prend celle écrite juste après --blur
for i in range(0, len(args)):
    arg = args[i]
    if arg == '--blur':
        blur_level = int(args[i+1])


# On boucle dans nos arguments, si l'un d'eux est "-i", notre dossier d'entrée prend la valeur écrite juste après
for i in range(0, len(args)):
    arg = args[i]
    if arg == '-i':
        dossierE = f'{args[i+1]}'

# On boucle dans nos arguments, si l'un d'eux est "-o", notre dossier de sortie prend la valeur écrite juste après
for i in range(0, len(args)):
        arg = args[i]
        if arg == '-o':
            dossierS = f'{args[i+1]}'
            if not os.path.exists(args[i+1]):
                os.mkdir(args[i + 1])

first_arg = args [1]

#Si mon premier argument est '-h' alors je fais tous ces prints
if first_arg == '-h':
    print(args)
    print('usage: imagefilter')
    print("-h, ---help")
    print("-i, --input-dir <imgs>")
    print("-o, --output-dir <>")
    print("--blur --dilate -- gray")

#Sinon si mon premier argument est '---help' alors je fais tous ces prints
elif first_arg == '---help':
    print('write "-i" for choose an input dir')
    print('write "-o" for choose an output dir')
    print('write "--blur" to blur the images')
    print('write "--dilate" to dilate the images')
    print('write "--gray" to put the images in black and white')

if args[1] == '--gray':
    gray_pic(dossierE, dossierS)
    for i in range(2, len(args)):
        arg = args[i]
        if arg == '--blur':
            blur_pic(dossierS, dossierS, blur_level)
        elif arg == '--dilate':
            dilatation_pic(dossierS, dossierS, dilate_level)

elif args[1] == '--blur':
    blur_pic(dossierE, dossierS, blur_level)
    for i in range(2, len(args)):
        arg = args[i]
        if arg == '--gray':
            gray_pic(dossierS, dossierS)
        elif arg == '--dilate':
            dilatation_pic(dossierS,dossierS,dilate_level)

elif args[1] == '--dilate':
    dilatation_pic(dossierE, dossierS, dilate_level)
    for i in range(2, len(args)):
        arg = args[i]
        if arg == '--blur':
            blur_pic(dossierS, dossierS, blur_level)
        elif arg == '--gray':
            gray_pic(dossierS,dossierS)

logger.dump_log()
















