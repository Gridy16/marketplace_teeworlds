import skin
import generation
import os 

skin_number = 2
a = generation.random_skin(skin_number)
a.create_save_json()
for i in range (1, skin_number+1):
    print(i)
    skin_name = f"skin{i}.json"
    json_file = a.getSkin(os.path.join(os.path.dirname(__file__)+f"\\{skin_name}"))
    skin_body = json_file["body"]["filename"]
    skin_marking = json_file["marking"]["filename"]
    skin_decoration = json_file["decoration"]["filename"]
    skin_hands = json_file["hands"]["filename"]
    skin_feet = json_file["feet"]["filename"]
    skin_eyes = json_file["eyes"]["filename"]

    image = skin.Skins(skin_body, skin_marking, skin_decoration, skin_hands, skin_feet, skin_eyes)
    image.showskin(i) 