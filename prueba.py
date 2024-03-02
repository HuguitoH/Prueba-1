name = input("Nombre:")
print("Buenas,", name)
print("Diccionario de Palabras Actuales")


meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH":"Ligera desaprobación", 
            "CREEPY":"Aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado",
            }

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("Definición de", word + ":", meme_dict[word])
    else:
        print("La palabra que solicitaste no esta o hay algun error en su escritura")
print("Gracias por tu curiosidad!")
