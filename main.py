from gray import gray_pic
from dilatation import dilatation_pic
from blur import blur_pic
import sys
import logger
import os

args = sys.argv

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

# On boucle dans nos arguments, si l'un d'eux est "--blur", alors on lance la fonction blur_pic
for i in range(0, len(args)):
    arg = args[i]
    if arg == '--blur':
        blur_pic(dossierE, dossierS, 13)

# On boucle dans nos arguments, si l'un d'eux est "--dilate", alors on lance la fonction dilatation_pic
for i in range(0, len(args)):
    arg = args[i]
    if arg == '--dilate':
        dilatation_pic(dossierS,dossierS)

# On boucle dans nos arguments, si l'un d'eux est "--gray", alors on lance la fonction gray_pic
for i in range(0, len(args)):
    arg = args[i]
    if arg == '--gray':
        gray_pic(dossierS,dossierS)


#blur_pic(dossierE,dossierS,13)
#dilatation_pic(dossierS,dossierS)

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


logger.dump_log()