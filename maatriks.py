import random
import numpy as np

def teeme_maatriksi():
    tahed = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V', 'Ü', 'Õ', 'Ö', 'Ä']
    maatriks = []
    for i in range(100):
        uus_list = []
        for n in range(100):
            juhu_taht = random.choice(tahed)
            uus_list.append(juhu_taht)
        maatriks.append(uus_list)
    return maatriks


def kirjutame_maatriksi_faili():
    with open('maatriks.txt', 'w') as f:
        for rida in teeme_maatriksi():
            loendur = 0
            for element in rida:
                f.write(element)
                f.write(', ')
                loendur += 1
                if loendur == 100:
                    f.write('\n')

def teeme_listi_eesti_sonadest():
    eesti_keele_sonad = []
    with open("eesti_keele_sonavormid.txt", "r", encoding="utf-8") as fail:
        for rida in fail:
            rida = rida.split()
            eesti_keele_sonad.append(rida[1])
    return eesti_keele_sonad

massiiv = np.array(teeme_maatriksi())
read_stringiks = [''.join(rida) for rida in massiiv]
transp_maatriks = np.transpose(massiiv)
veerud_stringiks = [''.join(rida) for rida in transp_maatriks]
veerud_read_kokku = read_stringiks + veerud_stringiks
leiduvad_sonad = []
for sona in teeme_listi_eesti_sonadest():
    for string in veerud_read_kokku:
        if sona in string.lower() and len(sona) > 4:
            leiduvad_sonad.append(sona)

kirjutame_maatriksi_faili()
print(leiduvad_sonad)
