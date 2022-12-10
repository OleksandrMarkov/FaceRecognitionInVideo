DISKS_CAPTIONS = "wmic logicaldisk get  DriveType, caption"
PC_DISKS = ('C', 'D')

VIDEOS_FOLDER = "dataset/videos"
PHOTOS_FOLDER = "dataset/photos"
IMAGES_FOLDER_ON_USB_FLASH_DRIVE = 'photos'
FULL_PATH_TO_PHOTOS_FOLDER = "C:/Users/ALEX/Documents/grokkingDeepLearning/VisitorsFacesDetection/src/VisitorsFacesDetection/dataset/photos"
SNAPSHOTS_FOLDER = "snapshots"
PROCESSED_PHOTOS_FOLDER = "dataset/photos/processed photos"

VIDEOTYPES = (("MP4 files", "*.mp4"),
        ("WMV files", "*.wmv"),
        ("AVI files", "*.avi"))

IMAGE_ENDS_WITH = ('jpg', 'png', 'gif')

MAX_FRAME_WIDTH = 860
MAX_FRAME_HEIGHT = 480
WINDOW_BACKGROUND = "#f2dbff"
BTN_FRAME_COLOR = 'lightgreen'
ICON = "ico/icon.ico"
BTN_W = 20

WINDOW_TITLE = "Розпізнавання облич на відео"
ERROR_TITLE = "Виникла помилка!"

MAY_LAUNCH_MSG = "Відеофайл обрано, можна починати розпізнавання"
VIDEO_NOT_SELECTED_MSG = 'Відеофайл не відтворюється або не обраний!'
CANT_LAUNCH_VIDEO_MSG = "Неможливо відтворити відеофайл!"
CANT_ADD_IMAGES_MSG = "Спочатку вставте накопичувач з папкою \"photos\";"\
+ "\nТакож перевірте розташування цільової директорії для колекції" 
CANT_DISPLAY_VIDEO_MSG = "Розмір відео завеликий!"
NO_CAPTURED_VISITORS_MSG = "Визначених відвідувачів з колекції зображень на відео не зафіксовано."
NO_SNAPSHOTS_MSG = "Окремих скріншотів для відео не створено."

FAQ_STEP1 = "Оновіть колекцію зображень, вставивши накопичувач з колекцією в папці \"photos\""
FAQ_STEP2 = "Оберіть відеозапис для перегляду та дослідження"
FAQ_STEP3 = "Виконайте запуск, ставте відео на паузу, робіть скріншоти"
FAQ_STEP4 = "Здійснюйте розпізнавання; результати будуть надіслані повідомленням в Telegram"

SELECT_VIDEO_LBL = "Обрати відеозапис"
RECOGNIZE_FACES_MSG = "Виконати розпізнавання"
ADD_NEW_IMAGES_LBL = "Додати нові фото"
FAQ_LBL = "Довідка"
LAUNCH_VIDEO_LBL = "Запуск відео"
PAUSE_VIDEO_LBL = "Пауза"
RELAUNCH_LBL = "Продовжити"
TAKE_A_SNAPSHOT_LBL = "Знімок"

FACE_RECOG_MODEL = 'model/faces.xml'