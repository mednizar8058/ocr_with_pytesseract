import pytesseract as tes
import cv2
import string


def check_resize_image(image_path, scale):
    # check image
    try:
        image = cv2.imread(image_path)
    except TypeError as error:
        print(error)

    # resize image
    scale_percent = scale   # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return(resized)


def apply_threshold(image):
    '''if the input image is too bright set the thresh to a lower value like 120
    but if the image is a low light image then set the thresh to 12 for example'''

    retval, threshold = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
    return(threshold)


def pytesseract(image):
    try:
        txt = tes.image_to_string(image)
    except tes.TesseractError as error:
        print(error)

    return(txt)


def clean_text(txt):
    words = txt.split()
    # remove punctuation from each word

    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    return(stripped)


def main():
    image_path = '/home/mnizar/Pictures/test2.png'
    checked_image = check_resize_image(image_path,60)
    threshold_image = apply_threshold(checked_image)
    my_txt = pytesseract(threshold_image)
    cleaned_txt = clean_text(my_txt)
    print(cleaned_txt)


if __name__ == '__main__':
    main()

