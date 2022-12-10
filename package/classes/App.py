from tkinter import *
from tkinter import ttk
from package.classes.Helper import *
from package.classes.Alerts import *
from package.classes.Video import *
import PIL.Image, PIL.ImageTk
import cv2, os, time

class App():
	def __init__(self, window):

		self.helper = Helper()
		self.error = Error()
		self.info = Info()

		self.window = window
		self.window.title(WINDOW_TITLE)
		self.window.iconbitmap(ICON)
		self.window.resizable(False, False)

		self.launch = False 
		self.selected_video, self.tmp = None, None 

		top_frame = Frame(self.window)

		top_frame.pack(side = TOP, pady = 10)

		btn_frame = Frame(self.window, bg = BTN_FRAME_COLOR)
		btn_frame.pack(side = BOTTOM, pady = 5)

		self.pause = False

		self.canvas = Canvas(top_frame)
		self.canvas.pack()

		self.btn_select_video = Button(btn_frame, text = SELECT_VIDEO_LBL, width = BTN_W, command = self.open_video)
		self.btn_select_video.grid(row = 0, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.btn_recognize_faces = Button(btn_frame, text = RECOGNIZE_FACES_MSG, width = BTN_W, command = self.recognize_faces)
		self.btn_recognize_faces.grid(row = 0, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.btn_update_photo_collection = Button(btn_frame, text = ADD_NEW_IMAGES_LBL, width = BTN_W, command = self.update_photo_collection)
		self.btn_update_photo_collection.grid(row = 0, column = 2, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.btn_open_FAQ = Button(btn_frame, text = FAQ_LBL, width = BTN_W, command = self.read_FAQ)
		self.btn_open_FAQ.grid(row = 0, column = 3, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.btn_launch_video = Button(btn_frame, text = LAUNCH_VIDEO_LBL, width = BTN_W, command = self.launch_video)
		self.btn_launch_video.grid(row = 1, column = 0, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.btn_pause_video = Button(btn_frame, text = PAUSE_VIDEO_LBL, width = BTN_W, command = self.pause_video)
		self.btn_pause_video.grid(row = 1, column = 1, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.btn_relaunch_video = Button(btn_frame, text = RELAUNCH_LBL, width = BTN_W, command = self.relaunch_video)
		self.btn_relaunch_video.grid(row = 1, column = 2, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.btn_take_a_snapshot = Button(btn_frame, text = TAKE_A_SNAPSHOT_LBL, width = BTN_W, command = self.take_a_snapshot)
		self.btn_take_a_snapshot.grid(row = 1, column = 3, ipadx = 6, ipady = 6, padx = 5, pady = 5)

		self.delay = 15

		self.window.mainloop()			
		
	def frames_are_of_acceptable_size(self, selected_video):
		self.cap = cv2.VideoCapture(selected_video) 
		canvas_width, canvas_height = self.get_frame_size(selected_video)

		if MAX_FRAME_WIDTH >= canvas_width > 0 and MAX_FRAME_HEIGHT >= canvas_height > 0:
			return True
		return False	
	
	def get_frame_size(self, selected_video):
		cap = cv2.VideoCapture(selected_video)
		canvas_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		canvas_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		return canvas_width, canvas_height

	def configure_the_canvas(self, canvas, selected_video):
		return canvas.config(width = self.get_frame_size(selected_video)[0],
			height = self.get_frame_size(selected_video)[1])

	def read_FAQ(self):
		faq = Toplevel()
		faq.geometry("645x350")
		faq.title("Довідка")
		
		faq_label1 = ttk.Label(faq, text=FAQ_STEP1, background="#FFCDD2", foreground="#B71C1C", font=("Arial", 12), padding=3)
		faq_label2 = ttk.Label(faq, text=FAQ_STEP2, background="#D9FFBA", foreground="#62B71C", font=("Arial", 12), padding=3)
		faq_label3 = ttk.Label(faq, text=FAQ_STEP3, background="#9CBFF7", foreground="#2B1CB7", font=("Arial", 12), padding=3)
		faq_label4 = ttk.Label(faq, text=FAQ_STEP4, background="#C277ED", foreground="#791AB0", font=("Arial", 12), padding=3)
		
		faq_label1.pack(fill=BOTH, expand=True)
		faq_label2.pack(fill=BOTH, expand=True)
		faq_label3.pack(fill=BOTH, expand=True)
		faq_label4.pack(fill=BOTH, expand=True)

	def open_video(self):
		if self.selected_video is not None:
			self.pause = False
			self.tmp = self.selected_video

		self.selected_video = self.helper.get_videofile()

		if self.selected_video:
			self.helper.remove_old_snapshots()
		
			if self.frames_are_of_acceptable_size(self.selected_video):
				self.info.show(message = MAY_LAUNCH_MSG)
				self.configure_the_canvas(self.canvas, self.selected_video)
			else:
				self.error.show(message = CANT_DISPLAY_VIDEO_MSG)
		else:
			if self.tmp is not None:
				self.selected_video = self.tmp	
			else:
				self.selected_video = None

	def update_photo_collection(self):
		path_to_new_collection = self.helper.get_path_to_new_collection()

		if path_to_new_collection is not None:
			try:
				self.helper.move_images(path_to_new_collection)
			except:
				self.error.show(message = CANT_ADD_IMAGES_MSG)
		else:
			self.error.show(message = CANT_ADD_IMAGES_MSG)		
				
	def get_frame(self):
		try:
			if self.cap.isOpened() and self.launch:
				ret, frame = self.cap.read()
				return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
		except:
			self.error.show(message = CANT_LAUNCH_VIDEO_MSG)					

	def launch_video(self):
		try:
			if self.selected_video is None:
				self.error.show(message = VIDEO_NOT_SELECTED_MSG)
				return

			self.tmp = self.selected_video					
			self.launch = True

			ret, frame = self.get_frame()

			if ret:
				self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
				self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

			if not self.pause:
				self.window.after(self.delay, self.launch_video)
		except:
			pass

	def pause_video(self):
		if self.pause == True:
			pass
		if self.selected_video is None:
			self.error.show(message = VIDEO_NOT_SELECTED_MSG)

		self.launch = False	
		self.pause = True

	def relaunch_video(self):
		self.pause = False
		self.launch_video()

	def take_a_snapshot(self):
		if self.selected_video is None or self.launch == False:
			self.error.show(message = VIDEO_NOT_SELECTED_MSG)
			return

		ret, frame = self.get_frame()	
		if ret:
			cv2.imwrite(os.path.join(SNAPSHOTS_FOLDER, "frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg"), cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

	def recognize_faces(self):

		if self.selected_video is None:
			self.error.show(message = VIDEO_NOT_SELECTED_MSG)
		else:
			self.helper.remove_old_processed_photos()
			self.helper.crop_images_from_the_collection()
				
			video = Video(self.selected_video)
					
			visitors = self.helper.iterate_processed_images(video)
			report = Report(visitors)
			report.send()

	def __del__(self):
		if self.cap.isOpened():
			self.cap.release()
			cv2.destroyAllWindows()