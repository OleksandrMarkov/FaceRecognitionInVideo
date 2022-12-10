import cv2
import face_recognition
from package.constants import *

class Image:
	def __init__(self, path):
		self.path = path.split(f"{PHOTOS_FOLDER}/")[1]
		self.img = cv2.imread(path) 	
		self.face_cascade = cv2.CascadeClassifier(FACE_RECOG_MODEL)

	def crop_face(self):
		faces = self.get_faces()
		for (x, y, w, h) in faces:
			self.img = self.img[y:y + h, x:x + w]
			path_to_cropped_img = f"{PROCESSED_PHOTOS_FOLDER}/{self.path}"
			cv2.imwrite(path_to_cropped_img, self.img)

	def get_faces(self):
		gray = self.convert2Gray()
		faces = self.face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
		return faces

	def convert2Gray(self):					
		self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
		return self.img