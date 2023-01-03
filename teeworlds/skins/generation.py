import random
import json
import os

class random_skin:

    def __init__(self, number):
        self.number = number
        self.body = ["bat", "bear", "beaver", "dog", "force", "fox", "hippo", "kitty",
                    "koala", "monkey", "mouse", "piglet", "raccoon", "spiky", "standard", "x_ninja"]
        self.decoration = ["hair", "twinbop", "twinmello",
                        "twinpen", "unibop", "unimelo", "unipento"]
        self.eyes = ["colorable", "negative", "standard", "standardreal", "x_ninja"]
        self.marking = ["bear", "belly1", "belly2", "blush", "bug", "cammo1", "cammo2", "cammostripes", "coonfluff", "donny", "downdony", "duodonny", "fox", "hipbel", "lowcross", "lowpaint",
                    "marksman", "mice", "mixture1", "mixture2", "monkey", "panda1", "panda2", "purelove", "saddo", "setisu", "sidemarks", "singu", "stripe", "striped",
                    "stripes", "stripes2", "thunder", "tiger1", "tiger2", "toptri", "triangular", "tricircular", "tripledon", "tritri", "twinbelly", "twincross",
                    "twintri", "uppy", "warpaint", "warstripes", "whisker", "wildpaint", "wildpatch", "yinyang"]

    def create_save_json(self):
        for i in range(1, self.number+1):
            skin = {
                "body": {
                    "filename": random.choice(self.body),
                    "custom_colors": True,
                    "hue": random.randint(0, 255),
                    "sat": random.randint(0, 255),
                    "lgt": random.randint(0, 255)
                },
                "marking": {
                    "filename": random.choice(self.marking),
                    "custom_colors": True,
                    "hue": random.randint(0, 255),
                    "sat": random.randint(0, 255),
                    "lgt": random.randint(0, 255),
                    "alp": random.randint(0, 255)
                },
                "decoration": {
                    "filename": random.choice(self.decoration),
                    "custom_colors": True,
                    "hue": random.randint(0, 255),
                    "sat": random.randint(0, 255),
                    "lgt": random.randint(0, 255)
                },
                "hands": {
                    "filename": "standard",
                    "custom_colors": True,
                    "hue": random.randint(0, 255),
                    "sat": random.randint(0, 255),
                },
                "feet": {
                    "filename": "standard",
                    "custom_colors": True,
                    "hue": random.randint(0, 255),
                    "sat": random.randint(0, 255),
                    "lgt": random.randint(0, 255)
                },
                "eyes": {
                    "filename": random.choice(self.eyes),
                    "custom_colors": True,
                    "hue": random.randint(0, 255),
                    "sat": random.randint(0, 255),
                    "lgt": random.randint(0, 255)
                },
            }

            file_path = os.path.join(os.path.dirname(__file__), f'skin{i}.json')
            print(file_path)
            with open(file_path, 'w') as f:
                json.dump(skin, f)

    def getSkin(self, json_file):

        with open(json_file, "r") as read_content:
            a = json.load(read_content)
            return a




