import json


def ruleaza_mt(config_mt, sir_intrare, pasi_maxim=100):
    banda = list(sir_intrare)
    simbol_vid_mt = config_mt["simbol_vid"]
    stare_curenta = config_mt["stare_initiala"]
    stari_finale_mt = set(config_mt["stari_finale"])
    reguli_mt = config_mt["reguli"]

    if not banda:
        banda = [simbol_vid_mt]

    pozitie_cap = 0
    numar_pasi = 0

    while numar_pasi < pasi_maxim:
        if pozitie_cap < 0:
            banda.insert(0, simbol_vid_mt)
            pozitie_cap = 0
        elif pozitie_cap >= len(banda):
            banda.append(simbol_vid_mt)

        simbol_citit_actual = banda[pozitie_cap]

        if stare_curenta in stari_finale_mt:
            return True, "".join(banda), f"ACCEPTAT in starea {stare_curenta}"

        tranzitie_aplicata = False
        for regula in reguli_mt:
            if regula["st_actuala"] == stare_curenta and regula["citit"] == simbol_citit_actual:
                stare_curenta = regula["st_urmatoare"]
                banda[pozitie_cap] = regula["scris"]
                if regula["mutare"] == "D":
                    pozitie_cap += 1
                elif regula["mutare"] == "S":
                    pozitie_cap -= 1
                tranzitie_aplicata = True
                break

        if not tranzitie_aplicata:
            return False, "".join(banda), f"BLOCAT: Stare={stare_curenta}, Simbol={simbol_citit_actual}"

        numar_pasi += 1

    if stare_curenta in stari_finale_mt:
        return True, "".join(banda), f"ACCEPTAT la limita de pasi in starea {stare_curenta}"

    return False, "".join(banda), f"MAX_PASI ({pasi_maxim}) atinsi. Stare curenta: {stare_curenta}"


#nume_fisier_config = 'config_bitadder.json'
#nume_fisier_config = 'config_copy.json'
nume_fisier_config = 'config_2noadder.json'
fisier_citit = open(nume_fisier_config)
mt_incarcat = json.load(fisier_citit)
fisier_citit.close()

intrare_user = input("Sir de intrare: ")
acceptat, banda_finala_str, mesaj_final = ruleaza_mt(mt_incarcat, intrare_user, pasi_maxim=300)

print(f"Rezultat: {'ACCEPTAT' if acceptat else 'RESPINS'}")
print(f"Mesaj: {mesaj_final}")
print(f"Banda finala: {banda_finala_str}")