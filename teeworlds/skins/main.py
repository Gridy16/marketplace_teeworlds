import skin
import generation
import os 

a = generation.random_skin(2)
a.create_save_json()
skin_name = "skin1.json"
json_file = a.getSkin(os.path.join(os.path.dirname(__file__)+f"\\{skin_name}"))
skin_body = json_file["body"]["filename"]
skin_marking = json_file["marking"]["filename"]
skin_decoration = json_file["decoration"]["filename"]
skin_hands = json_file["hands"]["filename"]
skin_feet = json_file["feet"]["filename"]
skin_eyes = json_file["eyes"]["filename"]

image = skin.Skins(skin_body, skin_marking, skin_decoration, skin_hands, skin_feet, skin_eyes)
image.save()
