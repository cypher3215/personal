import requests
import re
while True:
    web = "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://es.pornhub.com/video/search%3Fsearch%3Dcomo%2Bchupar%2Bpija&ved=2ahUKEwj1lof3vPyGAxXvVTABHd0oCy8QFnoECBAQAQ&usg=AOvVaw0B-pIwoPYJySB3f_HlI4O1"
    data = requests.get(web)
    content = data.text

    print(content)
    patron = r"id=[\w-]*"
    maquinas_repetidas = re.findall(patron, str(content))
    print(maquinas_repetidas)
    sin_duplicados = list(set(maquinas_repetidas))

    print(sin_duplicados)

    maquinas_final = []

    for i in sin_duplicados:
        nombre_maquinas = i.replace("id=", "")
        maquinas_final.append(nombre_maquinas)
    
    print(maquinas_final)
