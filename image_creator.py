from PIL import Image, ImageDraw


class ImageCreator:
    def __init__(self):
        pass

    def create_random_image(self):
        mode = 'RGB'
        size = (640, 480)
        color = (73, 109, 137)

        im = Image.new(mode, size, color)

        # im.save(image_path_output + image_name_output )

        im.show()
