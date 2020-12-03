from gray import gray_pic
from dilatation import dilatation_pic
from blur import blur_pic

dossierE = "imgs"
dossierS = "ImgsModif"
blur_level = -3

blur_pic(dossierE, dossierS, blur_level)
gray_pic(dossierS, dossierS)
dilatation_pic(dossierS, dossierS)