import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        result = emotion_detector("I am glad this is working")

        self.assertIn("anger", result)
        self.assertIn("disgust", result)
        self.assertIn("fear", result)
        self.assertIn("joy", result)
        self.assertIn("sadness", result)

        self.assertIn("dominant_emotion", result)

    def test_anger(self):
        result = emotion_detector("I am very angry")
        self.assertIn("anger", result)

    def test_disgust(self):
        result = emotion_detector("I am disgusted")
        self.assertIn("disgust", result)

    def test_fear(self):
        result = emotion_detector("I am afraid")
        self.assertIn("fear", result)

    def test_joy(self):
        result = emotion_detector("I am very happy")
        self.assertIn("joy", result)

    def test_sadness(self):
        result = emotion_detector("I am very sad")
        self.assertIn("sadness", result)


if __name__ == "__main__":
    unittest.main()
