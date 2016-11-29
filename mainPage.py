import sys

from helpers.ImgsVids_provider import *
from PyQt4.QtCore import *
from CNN.helper import *
from CNN.cnn_training import *
from main_gui import Ui_MainWindow
from CNN.CNN import *
import scipy.misc
import Image
from functools import partial


import matplotlib.pyplot as plt

class Online_learning(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Online_learning, self).__init__(parent)
        # QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)


        self.connect(self.btn_view_imgs, SIGNAL("clicked()"), self.nextImage)
        self.connect(self.btn_prev_img, SIGNAL("clicked()"), self.PrevImage)
        self.connect(self.btn_predict, SIGNAL("clicked()"), self.prediction)
        self.connect(self.btn_class_1, SIGNAL("clicked()"), self.learn)
        self.connect(self.btn_clear_points,SIGNAL("clicked()"), self.clear_points)

        self.file_path = "/hdd1T/frames_concert/Tomorrowland Belgium 2016 - Steve Aoki (10-19-2016 11-44-05 AM)"
        self.imgs_list = findImages(self.file_path)
        self.img_idx = 0

        self.current_img = []
        self.current_img_RGB= []
        self.head_locations = []

        self.showImage()


        self.cnn = CNN('weights/weights.pkl')

        self.create_lbl_layers(self.cnn.nkerns)
        self.fill_image_weights()

    def prediction(self):
        sliced_imgs = Image_slicer(self.current_img_RGB, self.head_locations, False)

        # print conv[0][0]
        # w,b =  self.cnn.classifier.layer0.params
        # # print "\n"
        # print b.get_value()
        # print "\n"
        # print conv_b[0][0]
        # print "\n"
        # for idx in xrange(32):
        #     print conv[0][idx][0][0] - conv_b[0][idx][0][0]

        prediction = self.cnn.predict(sliced_imgs)
        img = Image_predicted_labels(self.current_img, prediction)
        self.Impose_image(img, self.lbl_image, scaled=False)

    def preview_layers(self, layer, idx):
        sliced_imgs = Image_slicer(self.current_img_RGB, self.head_locations, False)
        conv, conv_b, conv_relu = self.cnn.tester_only(sliced_imgs,layer)
        tmp_conv = conv.swapaxes(0, 1)
        img = visualize_convoulved_imgs(tmp_conv[idx])
        plt.imshow(img, cmap='Greys_r')
        plt.show()

        # for i in range(tmp_conv.shape[0]):
        #     img = visualize_convoulved_imgs(tmp_conv[i])
        #     filename = "imgs/img_L0/%d_kernel.png" % i
        #     scipy.misc.imsave(filename, img)

        # plt.figure(1)
        # plt.subplot(121)
        # plt.imshow(sliced_imgs[20])
        # plt.subplot(122)
        # plt.imshow(tmp_conv[8][20], cmap = 'Greys_r')
        # plt.show()


    def learn(self):
        sliced_imgs = Image_slicer(self.current_img_RGB, self.head_locations, True)
        train_x, train_y = arrange_training_input(sliced_imgs)
        # fit_predict(self.cnn, train_x, train_y)
        self.cnn.fit(train_x,train_y)
        self.fill_image_weights()


    def addLocation(self,loc_x, loc_y):
        location = np.array([loc_x, loc_y])
        self.head_locations.append(location)

    def clear_points(self):
        self.head_locations = []
        self.Impose_image(self.current_img, self.lbl_image, scaled=False)


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

            self.Impose_image(img, self.lbl_image, scaled=False)
    #//TODO change to clear when new image and apply next and previous btns
    def nextImage(self):
        self.head_locations = []

        if self.imgs_list > 0:
            if self.img_idx <= len(self.imgs_list):
                self.img_idx += 1

        self.showImage()

    def PrevImage(self):
        self.head_locations = []

        if self.imgs_list > 0:
            if self.img_idx > 0:
                self.img_idx -= 1

        self.showImage()


    def showImage(self):
        file_name = join(self.file_path, self.imgs_list[self.img_idx])

        self.current_img = cv2.imread(file_name)
        self.current_img = cv2.resize(self.current_img, (1024, 576))
        self.current_img_RGB = cv2.cvtColor(self.current_img, cv2.COLOR_BGR2RGB)
        self.current_img = draw_boxes(self.current_img)

        self.Impose_image(self.current_img, self.lbl_image, scaled=False)

    def Impose_image(self, img, lbl_img, scaled):
        pixmap = convert_cv2_pixmap(img)
        if scaled:
            lbl_img.setPixmap(pixmap.scaled(30,30,Qt.KeepAspectRatio))
        else:
            lbl_img.setPixmap(pixmap)
        lbl_img.show()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.drawRect(0, 0, 20, 20)
        # self.draw_rectangle(qp)
        # self.update()
        qp.end()

    # //TODO check this implementation is not good the transpose.
    #  is correct but shoind, saving in all the way might be wrong
    def fill_image_weights(self):
        w, b = self.cnn.classifier.layer0.params
        filters_count = w.get_value().shape[0]
        filter = w.get_value()
        for i in xrange(filters_count):
            # filter_img = cv2.resize(filter[i], (100, 100))\
            #tmp=np.array(filter[i]).swapaxes(0,2).swapaxes(0,1)
            rgb = np.transpose(filter[i], axes=(1,2,0)) #np.array(filter[i]).swapaxes(0, 2)
            # rgb *= 255.0/rgb.max()
            # rgb = (rgb - rgb.min()) / (rgb.max() - rgb.min())
            # print rgb
            self.Impose_image(rgb, self.labels[i], scaled=True)
            im = Image.fromarray(rgb.astype(np.uint8))
            # cv2.imshow("img",rgb)
            # cv2.waitKey(500)

        #     # print filter[0]
        #     plt.imshow(rgb)
        #     plt.grid(False)
        #     filename = "imgs/L0/%d_cv2.png" %i
        #     scipy.misc.imsave(filename, rgb)
        #     cv2.imwrite(filename, rgb)
            # plt.savefig(filename)

            # plt.show()
            # plt.hold(0)
        # im.show()
app = QApplication(sys.argv)
form = Online_learning()
form.show()
app.exec_()


