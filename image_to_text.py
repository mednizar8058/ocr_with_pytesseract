import pytesseract as tes
import cv2
import string


def check_image(image_path):
    # check image
    try:
        image = cv2.imread(image_path)
    except TypeError as error:
        print(error)
    return(image)


def resize_image(image, scale):
    # resize image
    scale_percent = scale   # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return(resized)


def apply_threshold(image, state, val):
    '''if the input image is too bright set the thresh to a lower value like 120
    but if the image is a low light image then set the thresh to 12 for example'''
    if state:
        retval, threshold = cv2.threshold(image, val, 255, cv2.THRESH_BINARY)
        cv2.imshow('threshold', threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return(threshold)
    else:
        cv2.imshow('original', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return(image)


def pytesseract(image):
    try:
        txt = tes.image_to_string(image)
    except tes.TesseractError as error:
        print(error)

    return(txt)


def clean_text(txt):
    words = txt.split()  # split our txt into strings and make them in a list
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation) # the first arg in maketrans will be replaced with the second arg
                                                      # but the third arg will be removed
    stripped = [w.translate(table) for w in words]
    return(stripped)


def main():
    image_path = '/home/user/Desktop/ocr_with_pytesseract/test2.png'
    checked_image = check_image(image_path)
    resized_image = resize_image(checked_image, 90)
    threshold_image = apply_threshold(resized_image, False, 90)
    my_txt = pytesseract(threshold_image)
    cleaned_txt = clean_text(my_txt)
    print(cleaned_txt)


if __name__ == '__main__':
    main()

