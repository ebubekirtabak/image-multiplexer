import random

from PIL import Image, ImageDraw


class ImageCreator:
    def __init__(self, shapes, SHAPES_DIR):
        self.shapes = shapes
        self.SHAPES_DIR = SHAPES_DIR

    def create_random_image(self):
        mode = 'RGB'
        size = (1200, 880)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        im = Image.new(mode, size, color)
        step = 0
        for shape in self.shapes:
            step += 1
            shape_image = Image.open(self.SHAPES_DIR + shape)
            img_w, img_h = shape_image.size
            image_width = int((img_w / 100) * 25)
            image_height = int((img_h / 100) * 25)
            shape_image = shape_image.resize((image_width, image_height))
            im.paste(shape_image, (image_width * step, image_height), shape_image)

            # im.save(image_path_output + image_name_output )

        im.show()
