import cv2
import face_recognition
from package.constants import *
from package.classes.Image import *

class ProcessedImage(Image):
	def __init__(self, path):
		self.path = path	
		self.img = cv2.imread(path)

	def get_encodings(self):
		try:
			image_enc = face_recognition.face_encodings(self.img)[0]
			image_encs = [image_enc]
			return image_encs
		except Exception as e:
			return None				