import sys

from Online_GUI_Learning.helpers.ImgsVids_provider import *
from PyQt4.QtCore import *

from main_gui import Ui_MainWindow


class Online_learning(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Online_learning, self).__init__(parent)
        # QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)


        self.connect(self.btn_view_imgs, SIGNAL("clicked()"), self.showImage)
        self.connect(self.btn_predict, SIGNAL("clicked()"), self.prediction)
        self.connect(self.btn_class_1, SIGNAL("clicked()"), self.learn)
        # self.connect(self.btn_class_2, SIGNAL("clicked()"), self.learn())

        self.file_path = "/hdd1T/frames_concert/Tomorrowland Belgium 2016 - Steve Aoki (10-19-2016 11-44-05 AM)"
        self.img_idx = -1
        self.imgs_list = []
        self.current_img = []
        self.head_locations = []

        self.showImage()

    def prediction(self):
        sliced_imgs = Image_slicer(self.current_img)
        # CNN_fit(sliced_imgs)

    def learn(self):
        sliced_imgs = Image_slicer(self.current_img, self.head_locations)
        train_x, train_y = arrange_training_input(sliced_imgs)
        # train_x = CNN_fit(train_x)
        fit(train_x,train_y)


    def addLocation(self,loc_x, loc_y):
        location = np.array([loc_x, loc_y])
        self.head_locations.append(location)

    def mousePressEvent(self, QMouseEvent):
        locations = QMouseEvent.pos()
        loc_x = locations.x() - 50
        loc_y = locations.y() - 30
        # print('mouse x: %d, y: %d' %(loc_x, loc_y))
        self.addLocation(loc_x, loc_y)
        self.draw_point()

    def draw_point(self):
        img = copy.copy(self.current_img)
        if self.img_idx > -1:
            for idx in xrange(len(self.head_locations)):
                locx = self.head_locations[idx][0]
                locy = self.head_locations[idx][1]
                cv2.circle(img, (locx, locy), 3, (0, 0, 255), -1)

            pixmap = convert_cv2_pixmap(img)
            self.Impose_image(pixmap)
        # qp.drawRect(0,0, 20, 20)

    def showImage(self):
        self.head_locations = []
        self.imgs_list = findImages(self.file_path)
        if self.imgs_list > 0:
            if self.img_idx <= len(self.imgs_list):
                self.img_idx += 1
            else:
                self.img_idx = 0
            self.current_img = cv2.imread(join(self.file_path, self.imgs_list[self.img_idx]))
            self.current_img = cv2.resize(self.current_img, (1024,576))
            pixmap = convert_cv2_pixmap(self.current_img)
        self.Impose_image(pixmap)

    def Impose_image(self, pixmap):
        self.lbl_image.setPixmap(pixmap)
        self.lbl_image.show()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.drawRect(0, 0, 20, 20)
        # self.draw_rectangle(qp)
        # self.update()
        qp.end()


app = QApplication(sys.argv)
form = Online_learning()
form.show()
app.exec_()


