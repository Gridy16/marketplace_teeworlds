import os
import json
from PIL import Image, ImageDraw, ImageFont, ImageColor

# with open(file_name, 'r') as f:
#     data = json.load(f)
#     print(data)

#     # Load the file path from the json
#     imgpath = data['skin']
#     print(imgpath)

#     # Place the image path into the open method
#     img = Image.open(imgpath)


class Skins: 

    def __init__(self, body, marking, decoration, hands, feet, eyes):
        self.body = body
        self.marking = marking
        self.decoration = decoration
        self.hands = hands
        self.feet = feet
        self.eyes = eyes

        self.path_body = os.path.dirname(__file__) + f'\\body\\{self.body}.png'
        self.path_marking = os.path.dirname(__file__) + f'\\marking\\{self.marking}.png'
        self.path_decoration = os.path.dirname(__file__) + f'\\decoration\\{self.decoration}.png'
        self.path_hands = os.path.dirname(__file__) + f'\\hands\\{self.hands}.png'
        self.path_feet = os.path.dirname(__file__) + f'\\feet\\{self.feet}.png'
        self.path_eyes = os.path.dirname(__file__) + f'\\eyes\\{self.eyes}.png'

    def make_body(self):

        self.new_body = Image.open(self.path_body)

        # Split the image into four 128x128 images
        image_1, image_2 = self.new_body.crop((0, 0, 128, 128)), self.new_body.crop((128, 0, 256, 128))
        image_3, image_4 = self.new_body.crop((0, 128, 128, 128)), self.new_body.crop((128, 128, 256, 256))

        # Create a new image that is 256x256
        self.final_body = Image.new("RGBA", (128, 128), (255, 0, 0, 0))

        # Paste the images onto the new image in the correct order
        self.final_body.paste(image_1, (0, 0), image_1)
        self.final_body.paste(image_2, (0, 0), image_2)
        self.final_body.paste(image_3, (0, 0), image_3)
        self.final_body.paste(image_4, (0, 0), image_4)

        # Save the new image
        return self.final_body

    def make_marking(self):

        self.new_marking = Image.open(self.path_marking)
        return self.new_marking
    
    def make_decoration(self):

            self.new_decoration = Image.open(self.path_decoration)

            # Split the image into four 128x128 images
            # image_1, image_2 = image_body.crop((0, 0, 128, 128)), image_body.crop((128, 0, 256, 128))
            # image_3, image_4 = image_body.crop(
            #     (0, 128, 128, 256)), image_body.crop((128, 128, 256, 256))

            # # Create a new image that is 256x256
            # new_image = Image.new("RGBA", (128, 128), (0, 0, 0, 0))

            # # Paste the images onto the new image in the correct order
            # new_image.paste(image_1, (0, 0), image_1)
            # new_image.paste(image_2, (0, 0), image_2)
            # new_image.paste(image_3, (0, 0), image_3)
            # new_image.paste(image_4, (0, 0), image_4)

            # # Save the new image
            # # new_image.save("new_image.png")
            # # new_image.show()
            # return new_image

    

    def make_hands(self):

        self.new_hands = Image.open(self.path_hands)

        # # Split the image into four 128x128 images
        # image_1, image_2 = image_body.crop((0, 0, 128, 128)), image_body.crop((128, 0, 256, 128))
        # image_3, image_4 = image_body.crop(
        #     (0, 128, 128, 256)), image_body.crop((128, 128, 256, 256))

        # # Create a new image that is 256x256
        # new_image = Image.new("RGBA", (128, 128), (0, 0, 0, 0))

        # # Paste the images onto the new image in the correct order
        # new_image.paste(image_1, (0, 0), image_1)
        # new_image.paste(image_2, (0, 0), image_2)
        # new_image.paste(image_3, (0, 0), image_3)
        # new_image.paste(image_4, (0, 0), image_4)

        # # Save the new image
        # # new_image.save("new_image.png")
        # # new_image.show()
        # return new_image

    def make_feet(self):

        self.new_feet = Image.open(self.path_feet).crop((0, 0, 64, 64))
        return self.new_feet

    def make_eyes(self):

        self.new_eyes = Image.open(self.path_eyes).crop((0, 0, 64, 32))
        return self.new_eyes
        
    def make_skin(self): 

        skin_image = Image.new("RGBA", (128, 128), (0, 0, 0, 0))
        # Paste the images onto the new image in the correct order
        skin_image.paste(self.make_feet(), (19, 60), self.make_feet())
        skin_image.paste(self.make_body(), (0, 0), self.make_body())
        skin_image.paste(self.make_marking(), (0, 0), self.make_marking())
        skin_image.paste(self.make_eyes(), (40, 40), self.make_eyes())
        skin_image.paste(self.make_feet(), (45, 60), self.make_feet())

        return skin_image

    def showskin(self, i):
        # image_body = body(Image.open(self.path_body))
        # image_eyes = eyes(Image.open(path_eyes))
        # image_feet = feet(Image.open(path_feet))
        # image_marking = Image.open(path_marking)
        skin = self.make_skin()
        skin.show()
        skin.save(f"{os.path.dirname(__file__)}\skin{i}.png", dpi=(1024, 1024))

    # image_body.show()
    # image_eyes.show()