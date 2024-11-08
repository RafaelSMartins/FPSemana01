characters = []
count = 3

for i in range(count):
    name = input("Nome do personagem: ")
    attack = int(input("Ataque do personagem: "))
    defense = int(input("Defesa do personagem: "))
    character = [name, attack, defense]  
    characters.append(character)

print("Lista de personagens:", characters)


max_attack = -1
max_defense = -1
max_attack_character = None
max_defense_character = None


for character in characters:
    if character[1] > max_attack:  
        max_attack = character[1]
        max_attack_character = character
    
    if character[2] > max_defense: 
        max_defense = character[2]
        max_defense_character = character


print("Ataque: " + str(max_attack_character[0]) + " " + str(max_attack_character[1]))
print("Defesa: " + str(max_defense_character[0]) + " " + str(max_defense_character[2]))
