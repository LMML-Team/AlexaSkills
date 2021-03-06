from camera import take_picture
import skimage.io as io
from time import sleep

from .config import *
from .detection import face_detection


def add_picture(filepath=None, alexa=False) :
    """


    Parameters
    -----------
    filepath: r"PATH" (optional)
        analyzes a picture at the given filepath. if no file path is given, a picture is taken
    alexa: boolean
        whether to prompt user and show picture (false) or simply return string (true)
    """
    if filepath is not None :
        img_array = io.imread(filepath)
    else :
        print("Please prepare to have your picture taken")
        sleep(1)
        img_array = take_picture()

    face_descriptors, face_borders = face_detection(img_array)
    names = get_names(face_descriptors)
    name_str, first_saved = format_names(names, face_descriptors, alexa)
    if first_saved :
        names = get_names(face_descriptors)
    if not alexa :
        show_image(img_array, face_borders, names)

    return name_str
