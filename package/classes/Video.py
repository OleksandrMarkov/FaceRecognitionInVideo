import cv2
import face_recognition
from package.constants import *

class Video:
	def __init__(self, path):
		self.cap = cv2.VideoCapture(path)
		self.path = path[path.find(VIDEOS_FOLDER + "/"):]
		self.face_cascade = cv2.CascadeClassifier(FACE_RECOG_MODEL)

	def get_face_locations(self, frame):
		return face_recognition.face_locations(frame)

	def get_face_encodings(self, frame, locations):
		return face_recognition.face_encodings(frame, locations)	

	def get_capture_matches(self, images_dict):		
		captured_visitors = []
		while self.cap.read():
			try:
				success, img = self.cap.read()
				if not success:
					break
				frame = img[:, :, ::-1]
				face_locations = self.get_face_locations(frame)
				face_encodings = self.get_face_encodings(frame, face_locations)	
				for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
					for image in images_dict.keys():
						matches = face_recognition.compare_faces(images_dict[image], face_encoding)
						if True in matches:
							if image not in captured_visitors:
								captured_visitors.append(image)
			except Exception as e:
				pass
		return captured_visitors