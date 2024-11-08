characters = []
max_ataque = -1
max_defesa = -1
character_max_ataque = ""
character_max_defesa = ""

for i in range(3):
    nome = str(input(""))
    ataque = (int(input("")))
    defesa = (int(input("")))
    characters.append([nome,(ataque,defesa)])
    
    if ataque > max_ataque:
        max_ataque = ataque
        character_max_ataque = nome
    if defesa > max_defesa:
        max_defesa = defesa
        character_max_defesa = nome
    
    print(characters)
    print("Ataque: ", max_ataque, ataque)
    print("Defesa: ", max_defesa, defesa)