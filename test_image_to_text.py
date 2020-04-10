import unittest
import image_to_text as i
import cv2


image = cv2.imread('/home/mnizar/Pictures/test2.png')


class Testimagetxt(unittest.TestCase):
    def test_check_resize_image(self):
        pass

    def test_threshold(self):
        result = i.apply_threshold(image)
        retval, thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
        self.assertIs(result, thresh)

    def test_pytesseract(self):
        result = i.pytesseract(image)
        self.assertNotIn(result, '')

    def test_clean_txt(self):
        list = []
        result = i.clean_text(i.pytesseract(image))
        self.assertIsNot(result, list)


if __name__ == '__main__':
    unittest.main()