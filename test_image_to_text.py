import unittest
import image_to_text as i
import cv2
import numpy as np


image = cv2.imread('/home/mnizar/Pictures/coloredimage.jpg')
image_path = '/home/mnizar/Pictures/coloredimage.jpg'


class Testimagetxt(unittest.TestCase):
    def test_check_image(self):
        result = i.check_image(image_path)
        self.assertIsInstance(result, np.ndarray)

    def test_resize_image(self):
        result = i.resize_image(image, 60)
        self.assertNotAlmostEqual(result.shape[0], image.shape[0])
        self.assertNotAlmostEqual(result.shape[1], image.shape[1])

    def test_threshold(self):
        result = i.apply_threshold(image, True, 90)
        retval, thresh = cv2.threshold(image, 90, 255, cv2.THRESH_BINARY)
        self.assertTrue(np.array_equal(result, thresh))

    def test_pytesseract(self):
        result = i.pytesseract(image)
        self.assertNotIn(result, '')

    def test_clean_txt(self):
        result = i.clean_text(i.pytesseract(image))
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()