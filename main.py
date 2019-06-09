import os
from xml.dom.minidom import parse, parseString
from PIL import Image

from image_creator import ImageCreator
from models.combine_image import CombineImage

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = ROOT_DIR + "/input/"

def main():
    img = Image.open("/home/ebubekirtabak/projects/python-projects/image-multiplexer/input/1.jpg")
    img_w, img_h = img.size
    # img.show()
    shapes = get_shapes()
    images = get_images()
    image_combainer(images)
    print(shapes)

def image_combainer(images):
    image_files = filter(lambda image: image.endswith((".jpg", ".png")), images)
    combine_image_list = []

    for image in images:
        name = image[0:image.rindex('.')]
        xml = filter(lambda item: item == name + ".xml", images)
        if len(list(xml)) > 0:
            datasource = open(INPUT_DIR + name + ".xml")
            xml_data = parse(datasource)
            combine_image = CombineImage(path=INPUT_DIR, name=image, xml=xml_data)
            combine_image_list.append(combine_image)
            ImageCreator().create_random_image()
            print(name)

def get_images():
    return os.listdir(INPUT_DIR)


def get_shapes():
    return os.listdir(ROOT_DIR + "/shapes")


if __name__ == "__main__":
    main()