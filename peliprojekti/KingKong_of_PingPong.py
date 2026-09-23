# kysytään pelaajan tiedot ja tallennetaan ne muuttujiin

nimi = input("Anna nimesi: ")
ikä = input("Anna ikäsi: ")

# tulostetaan pelaajan tiedot konsoliin

print(f"Pelaajan nimi on {nimi} ja ikä on {ikä} vuotta.")

# pelaajan aloitustiedot, kaikki aloittaa isän autotallista

taito = 0
paikka = "autotalli"
varusteet = []


# päävalikko tulostetaan tällä aina komennon jälkeen

def näytä_valikko():
    print()
    print("Päävalikko:")
    print("harjoittele")
    print("ottelu")
    print("lepää")
    print("osta")
    print("varusteet")
    print("tilanne")
    print("liiku")
    print("kerää")
    print("tallenna")
    print("lopeta")


# lepopäivä, ei tee mitään muuta kuin tulostaa tekstin

def lepää():
    print("Pidit lepopäivän ja katsoit pingisvideoita.")
    print("Taito ei noussut, mutta olo on virkeä.")


# harjoittelu nostaa taitoa yhdellä ja palauttaa uuden taidon

def harjoittele(taito):
    taito = taito + 1
    print("Harjoittelit koko päivän pöydän ääressä.")
    print(f"Taitosi on nyt {taito}")
    return taito


# kysytään pelaajalta varuste ja lisätään se varusteet listaan

def osta(varusteet):
    varuste = input("Mitä haluat ostaa? ")
    if varuste == "":
        print("Et ostanut mitään.")
    else:
        varusteet.append(varuste)
        print(f"Ostit: {varuste}")


# tulostetaan kaikki varusteet listasta yksi kerrallaan

def näytä_varusteet(varusteet):
    if len(varusteet) == 0:
        print("Sinulla ei ole vielä varusteita.")
    else:
        print("Varusteesi:")
        for varuste in varusteet:
            print(f"- {varuste}")


# näyttää pelaajan tiedot ja missä pelaaja on

def tilanne(nimi, ikä, taito, paikka):
    print(f"Nimi: {nimi}")
    print(f"Ikä: {ikä}")
    print(f"Taito: {taito}")
    print(f"Paikka: {paikka}")
    print(f"Varusteita: {len(varusteet)} kpl")


# ottelu jossa vastustaja riippuu paikasta
# jos taito on tarpeeksi iso niin pelaaja voittaa

def ottelu(taito, paikka):
    if paikka == "autotalli":
        vastustaja = "isä"
        vaadittu = 2
    elif paikka == "koulu":
        vastustaja = "opettaja Pekka"
        vaadittu = 5
    elif paikka == "sm-kisat":
        vastustaja = "Suomen mestari"
        vaadittu = 8
    else:
        vastustaja = "maailman ykkönen"
        vaadittu = 12

    print(f"Pelaat ottelun, vastustajana {vastustaja}.")

    if taito >= vaadittu:
        print("Voitit ottelun!")
        return True
    else:
        print(f"Hävisit ottelun. Tarvitset taidon {vaadittu}.")
        return False


# liikkuminen paikasta toiseen, uuteen paikkaan pääsee vain jos taito riittää

def liiku(taito, paikka):
    print("1. autotalli (taito 0)")
    print("2. koulu (taito 5)")
    print("3. sm-kisat (taito 8)")
    print("4. mm-kisat (taito 12)")
    valinta = input("Mihin haluat mennä? ")

    if valinta == "1":
        print("Menit takaisin autotalliin.")
        return "autotalli"
    elif valinta == "2" and taito >= 5:
        print("Menit kouluun.")
        return "koulu"
    elif valinta == "3" and taito >= 8:
        print("Menit SM-kisoihin.")
        return "sm-kisat"
    elif valinta == "4" and taito >= 12:
        print("Menit MM-kisoihin!")
        return "mm-kisat"
    else:
        print("Et päässyt sinne, taito ei riitä tai valinta oli väärä.")
        return paikka


# jokaisesta paikasta löytyy yksi esine jonka voi ottaa mukaan
# esine nostaa taitoa yhdellä

def kerää(paikka, varusteet, taito):
    if paikka == "autotalli":
        esine = "vanha maila"
    elif paikka == "koulu":
        esine = "pingistossut"
    elif paikka == "sm-kisat":
        esine = "hikinauha"
    else:
        esine = "kultainen maila"

    if esine in varusteet:
        print(f"Olet jo ottanut täältä esineen {esine}.")
    else:
        varusteet.append(esine)
        taito = taito + 1
        print(f"Löysit esineen {esine}. Taito nousi yhdellä!")
    return taito


# luetaan tekstitiedosto (intro ja ohjeet) ja palautetaan sen teksti

def lue_tiedosto(tiedoston_nimi):
    tiedosto = open(tiedoston_nimi, "r", encoding="utf-8")
    teksti = tiedosto.read()
    tiedosto.close()
    return teksti


# tallennetaan taito, paikka ja varusteet tiedostoon jonka nimessä on pelaajan nimi

def tallenna(nimi, taito, paikka, varusteet):
    tiedosto = open(f"{nimi}_tallennus.txt", "w", encoding="utf-8")
    tiedosto.write(f"{taito}\n")
    tiedosto.write(f"{paikka}\n")
    for varuste in varusteet:
        tiedosto.write(f"{varuste}\n")
    tiedosto.close()
    print("Peli tallennettiin.")


# luetaan tallennus ja palautetaan sen rivit listana

def lataa(nimi):
    tiedosto = open(f"{nimi}_tallennus.txt", "r", encoding="utf-8")
    rivit = tiedosto.read().split("\n")
    tiedosto.close()
    return rivit


# tarkistetaan, onko pelaaja tarpeeksi vanha

if int(ikä) < 12:
    print("peli vaatii vähintään 12-ikäisyyden, peli sammuu")
else:
    print(lue_tiedosto("intro.txt"))

# kysytään halutaanko jatkaa vanhaa peliä samalla nimellä

    jatka = input("Haluatko jatkaa tallennettua peliä? (k/e) ")

    if jatka == "k":
        rivit = lataa(nimi)
        taito = int(rivit[0])
        paikka = rivit[1]
        for rivi in rivit[2:]:
            if rivi != "":
                varusteet.append(rivi)
        print(f"Tervetuloa takaisin {nimi}!")

    print(lue_tiedosto("ohjeet.txt"))

# päävalikko pyörii kunnes pelaaja kirjoittaa lopeta tai voittaa MM-kisat

    while True:
        näytä_valikko()
        print(f"Olet paikassa: {paikka}")

        komento = input("Valitse toiminto: ")

        if komento == "lopeta":
            tallenna(nimi, taito, paikka, varusteet)
            print("Kiitos pelaamisesta!")
            break

        elif komento == "harjoittele":
            taito = harjoittele(taito)

        elif komento == "ottelu":
            voitto = ottelu(taito, paikka)
            if voitto == True:
                taito = taito + 1

# jos voittaa ottelun MM-kisoissa niin peli on voitettu

                if paikka == "mm-kisat":
                    print(f"ONNEKSI OLKOON {nimi}!")
                    print("Uusi tittelisi on King Kong of Ping Pong!")
                    tallenna(nimi, taito, paikka, varusteet)
                    break

        elif komento == "lepää":
            lepää()

        elif komento == "osta":
            osta(varusteet)

        elif komento == "varusteet":
            näytä_varusteet(varusteet)

        elif komento == "tilanne":
            tilanne(nimi, ikä, taito, paikka)

        elif komento == "liiku":
            paikka = liiku(taito, paikka)

        elif komento == "kerää":
            taito = kerää(paikka, varusteet, taito)

        elif komento == "tallenna":
            tallenna(nimi, taito, paikka, varusteet)

        else:
            print("En ymmärrä komentoa, kokeile uudestaan.")