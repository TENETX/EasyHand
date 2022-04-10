from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTimer
import cv2
import torch
import shutil
import os
import mediapipe as mp
from time import sleep
from model import Model
from change import gaoshiqing
import queue
from change import gaoshiqing
nianling = ["变年轻", "无", "变老"]
qingxv = ["悲伤", "无", "喜悦"]
xingbie = ["女性化", "无", "男性化"]
manhua = ["无", "是"]
youhua = ["无", "是"]
global isclose
isclose = False
global lu
lu = True
global ri
ri = True
current_path = os.getcwd()
# Camera number, can be varied if using multiple webcams
cam_number = 0
# Laterally inverting video stream
flip = True
# Minimum confidence score required for detecting and marking hand landmarks
min_conf = 0.75
max_hands = 2
# Path of trained model. Can be changed to point to a custom model
model_path = os.path.join(current_path, './mymodels323/1490.pt')
# 操作序列，对应性别，年龄，情绪，漫画和XX，
caozuo = [0, 0, 0, 0, 0]
# 任务队列
renwu = queue.Queue()
cap = cv2.VideoCapture(cam_number)
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    max_num_hands=max_hands,
    min_detection_confidence=min_conf,
    min_tracking_confidence=min_conf
)
mp_draw = mp.solutions.drawing_utils
_lm_list = [
    mpHands.HandLandmark.WRIST,
    mpHands.HandLandmark.THUMB_CMC,
    mpHands.HandLandmark.THUMB_MCP,
    mpHands.HandLandmark.THUMB_IP,
    mpHands.HandLandmark.THUMB_TIP,
    mpHands.HandLandmark.INDEX_FINGER_MCP,
    mpHands.HandLandmark.INDEX_FINGER_DIP,
    mpHands.HandLandmark.INDEX_FINGER_PIP,
    mpHands.HandLandmark.INDEX_FINGER_TIP,
    mpHands.HandLandmark.MIDDLE_FINGER_MCP,
    mpHands.HandLandmark.MIDDLE_FINGER_DIP,
    mpHands.HandLandmark.MIDDLE_FINGER_PIP,
    mpHands.HandLandmark.MIDDLE_FINGER_TIP,
    mpHands.HandLandmark.RING_FINGER_MCP,
    mpHands.HandLandmark.RING_FINGER_DIP,
    mpHands.HandLandmark.RING_FINGER_PIP,
    mpHands.HandLandmark.RING_FINGER_TIP,
    mpHands.HandLandmark.PINKY_MCP,
    mpHands.HandLandmark.PINKY_DIP,
    mpHands.HandLandmark.PINKY_PIP,
    mpHands.HandLandmark.PINKY_TIP
]


def nothing(x):
    pass

# Extract landmark positions as array


def landmark_extract(hand_lms, mpHands):
    output_lms = []
    for lm in _lm_list:
        lms = hand_lms.landmark[lm]
        output_lms.append(lms.x)
        output_lms.append(lms.y)
        output_lms.append(lms.z)
    return output_lms


def gogogo():
    # Loading torch model
    model = Model()
    model.load_state_dict(torch.load(model_path, map_location='cpu'))
    model.eval()
    # 手势对应的操作
    action_map = {0: 'old', 1: 'young', 2: 'man',
                  3: 'woman', 4: 'smile', 5: 'sad', 6: 'cartoon', 7: 'todo', 8: 'clear', 9: 'selfie'}
    circles = []
    # Video feed loop
    while True:
        shoushi = "None"
        success, frame = cap.read()
        jietu = 0
        if flip:
            frame = cv2.flip(frame, 1)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        # Added 1 to make range of imd_step_gap equal to [1, 30].
        if not results.multi_hand_landmarks:
            go = False
        else:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks,
                                       mpHands.HAND_CONNECTIONS)
                # Mode check
                landmark_list = landmark_extract(hand_landmarks, mpHands)
                model_input = torch.tensor(
                    landmark_list, dtype=torch.float).unsqueeze(0)
                action = action_map[torch.argmax(
                    model.forward(model_input)).item()]
                # 男性化
                if action == 'man':
                    shoushi = "三"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[0] = 1
                # 女性化
                if action == 'woman':
                    shoushi = "四"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[0] = -1
                # 变老
                if action == 'old':
                    shoushi = "一"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[1] = 1
                # 变年轻
                if action == 'young':
                    shoushi = "二"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[1] = -1
                # 微笑
                if action == 'smile':
                    shoushi = "五"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[2] = 1
                # 悲伤
                if action == 'sad':
                    shoushi = "六"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[2] = -1
                # e
                if action == 'cartoon':
                    shoushi = "九"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[3] = 1
                # 漫画
                if action == 'todo':
                    shoushi = "八"
                    for i in range(5):
                        caozuo[i] = 0
                    caozuo[4] = 1
                # 清零
                if action == 'clear':
                    shoushi = "love"
                    for i in range(5):
                        caozuo[i] = 0
                # 自拍
                if action == 'selfie':
                    shoushi = "Selfie!"
                    jietu = 1
        for position, pen_color, pen_size in circles:
            frame = cv2.circle(frame, position, pen_size, pen_color, -1)
        if lu:
            renwu.put(
                [frame, [caozuo[0], caozuo[1], caozuo[2], caozuo[3], caozuo[4]], jietu, shoushi])
        if isclose:
            break


class Ui_jiemian(object):
    def setupUi(self, jiemian):
        jiemian.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        jiemian.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.timerr = QTimer()
        self.timerr.timeout.connect(self.daojishi)
        self._timer = QTimer()
        self._timer.timeout.connect(self.play)
        self._timer.start(1)
        jiemian.setObjectName("jiemian")
        jiemian.resize(920, 560)
        self.frame = QtWidgets.QFrame(jiemian)
        self.frame.setGeometry(QtCore.QRect(10, 10, 901, 541))
        self.frame.setStyleSheet("#frame\n"
                                 "{\n"
                                 "background-color: rgb(255, 255, 255);\n"
                                 "border-radius: 20px;\n"
                                 "border-color: rgb(255, 231, 217);\n"
                                 "border-width: 1px;\n"
                                 "border-style: solid; \n"
                                 "    background-color: qlineargradient(spread:pad, x1:0, y1:0.023, x2:0.875731, y2:0.892, stop:0 #ECAD9E, stop:1 rgba(255, 255, 255, 255));\n"
                                 "} ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.shexiang = QtWidgets.QLabel(self.frame)
        self.shexiang.setGeometry(QtCore.QRect(580, 150, 311, 311))
        self.shexiang.setStyleSheet("border-width: 3px;\n"
                                    "border-style: solid;\n"
                                    "border-color: #ECAD9E;\n"
                                    "border-radius: 0px;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.shexiang.setText("")
        self.shexiang.setObjectName("shexiang_2")
        self.zuixiaohua = QtWidgets.QPushButton(self.frame)
        self.zuixiaohua.setGeometry(QtCore.QRect(790, 10, 35, 35))
        self.zuixiaohua.setMinimumSize(QtCore.QSize(35, 35))
        self.zuixiaohua.setMaximumSize(QtCore.QSize(35, 35))
        self.zuixiaohua.setStyleSheet("QPushButton { \n"
                                      "color: rgb(222, 222, 222);\n"
                                      "border-style: none;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 5px 10px;\n"
                                      "font-size: 13px; }\n"
                                      "\n"
                                      "QPushButton:hover { \n"
                                      "color: #ffffff; \n"
                                      "font-weight: bold; \n"
                                      "background-color: #fd839a; \n"
                                      "}")
        self.zuixiaohua.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/mini.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zuixiaohua.setIcon(icon)
        self.zuixiaohua.setObjectName("zuixiaohua")
        self.guanbi = QtWidgets.QPushButton(self.frame)
        self.guanbi.setGeometry(QtCore.QRect(840, 10, 35, 35))
        self.guanbi.setMinimumSize(QtCore.QSize(35, 35))
        self.guanbi.setMaximumSize(QtCore.QSize(35, 35))
        self.guanbi.setStyleSheet("QPushButton { \n"
                                  "color: rgb(222, 222, 222);\n"
                                  "border-style: none;\n"
                                  "border-radius: 10px;\n"
                                  "padding: 5px 10px;\n"
                                  "font-size: 13px; }\n"
                                  "\n"
                                  "QPushButton:hover { \n"
                                  "color: #ffffff; \n"
                                  "font-weight: bold; \n"
                                  "background-color: #fd839a; \n"
                                  "}")
        self.guanbi.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/logout.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guanbi.setIcon(icon1)
        self.guanbi.setObjectName("guanbi")
        self.m6 = QtWidgets.QLabel(self.frame)
        self.m6.setGeometry(QtCore.QRect(730, 100, 131, 41))
        self.m6.setStyleSheet("font: 15pt \"华文琥珀\";"
                              "color: rgb(255, 170, 0);")
        self.m6.setObjectName("m6_2")
        self.shoushi = QtWidgets.QLabel(self.frame)
        self.shoushi.setGeometry(QtCore.QRect(580, 100, 131, 41))
        self.shoushi.setStyleSheet("font: 15pt \"华文琥珀\";"
                                   "color: rgb(255, 170, 0);")
        self.shoushi.setObjectName("shoushi_3")
        self.huanyin = QtWidgets.QLabel(self.frame)
        self.huanyin.setGeometry(QtCore.QRect(580, 50, 301, 41))
        self.huanyin.setStyleSheet("font: italic 30pt \"Brush Script MT\";\n"
                                   "color: rgb(255, 170, 0);")
        self.huanyin.setObjectName("huanyin")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(20, 480, 861, 51))
        self.widget.setStyleSheet("border-radius: 20px;\n"
                                  "\n")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout_2")
        self.huzi = QtWidgets.QLabel(self.widget)
        self.huzi.setMinimumSize(QtCore.QSize(100, 0))
        self.huzi.setStyleSheet("font: 15pt \"华文琥珀\";"
                                "color: rgb(255, 170, 0);")
        self.huzi.setObjectName("huzi")
        self.horizontalLayout.addWidget(self.huzi)
        self.m1 = QtWidgets.QLabel(self.widget)
        self.m1.setStyleSheet("font: italic 17pt \"Bell MT\";\n"
                              "color:#fd839a;\n")
        self.m1.setObjectName("m1")
        self.horizontalLayout.addWidget(self.m1)
        self.toufa = QtWidgets.QLabel(self.widget)
        self.toufa.setMinimumSize(QtCore.QSize(80, 0))
        self.toufa.setStyleSheet("font: 15pt \"华文琥珀\";"
                                 "color: rgb(255, 170, 0);")
        self.toufa.setObjectName("toufa")
        self.horizontalLayout.addWidget(self.toufa)
        self.m2 = QtWidgets.QLabel(self.widget)
        self.m2.setStyleSheet("font: italic 17pt \"Bell MT\";\n"
                              "color:#fd839a;\n")
        self.m2.setObjectName("m2")
        self.horizontalLayout.addWidget(self.m2)
        self.yanjing = QtWidgets.QLabel(self.widget)
        self.yanjing.setMinimumSize(QtCore.QSize(100, 0))
        self.yanjing.setStyleSheet("font: 15pt \"华文琥珀\";"
                                   "color: rgb(255, 170, 0);")
        self.yanjing.setObjectName("yanjing_2")
        self.horizontalLayout.addWidget(self.yanjing)
        self.m3 = QtWidgets.QLabel(self.widget)
        self.m3.setStyleSheet("font: italic 17pt \"Bell MT\";\n"
                              "color:#fd839a;\n")
        self.m3.setObjectName("m3")
        self.horizontalLayout.addWidget(self.m3)
        self.fuse = QtWidgets.QLabel(self.widget)
        self.fuse.setMinimumSize(QtCore.QSize(150, 0))
        self.fuse.setStyleSheet("font: 15pt \"华文琥珀\";"
                                "color: rgb(255, 170, 0);")
        self.fuse.setObjectName("fuse_2")
        self.horizontalLayout.addWidget(self.fuse)
        self.m4 = QtWidgets.QLabel(self.widget)
        self.m4.setStyleSheet("font: italic 17pt \"Bell MT\";\n"
                              "color:#fd839a;\n")
        self.m4.setObjectName("m4_2")
        self.horizontalLayout.addWidget(self.m4)
        self.lao = QtWidgets.QLabel(self.widget)
        self.lao.setMinimumSize(QtCore.QSize(50, 0))
        self.lao.setStyleSheet("font: 15pt \"华文琥珀\";"
                               "color: rgb(255, 170, 0);")
        self.lao.setObjectName("lao")
        self.horizontalLayout.addWidget(self.lao)
        self.m5 = QtWidgets.QLabel(self.widget)
        self.m5.setMinimumSize(QtCore.QSize(50, 0))
        self.m5.setStyleSheet("font: italic 17pt \"Bell MT\";\n"
                              "color:#fd839a;\n")
        self.m5.setObjectName("m5")
        self.horizontalLayout.addWidget(self.m5)
        self.zhaopian = QtWidgets.QLabel(self.frame)
        self.zhaopian.setGeometry(QtCore.QRect(10, 10, 551, 461))
        self.zhaopian.setStyleSheet("background-color: rgb(238, 238, 238);\n"
                                    "border-radius: 20px;\n"
                                    "font: 63 30pt \"Bahnschrift SemiBold Condensed\";\n"
                                    "color: rgb(163, 163, 163);\n"
                                    "\n"
                                    "")
        self.zhaopian.setObjectName("zhaopian")
        self.biaoji = 3
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/close.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guanbi.setIcon(icon1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icon/mini.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zuixiaohua.setIcon(icon2)
        self.retranslateUi(jiemian)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('./icon/member.png'))
        jiemian.setWindowIcon(icon)
        QtCore.QMetaObject.connectSlotsByName(jiemian)
        self.guanbi.clicked.connect(lambda: self.guan(jiemian))
        self.zuixiaohua.clicked.connect(jiemian.showMinimized)

    def retranslateUi(self, jiemian):
        _translate = QtCore.QCoreApplication.translate
        jiemian.setWindowTitle(_translate("jiemian", "Dialog"))
        self.m6.setText(_translate("jiemian", "无"))
        self.shoushi.setText(_translate("jiemian", "当前手势:"))
        self.huanyin.setText(_translate("jiemian", "Welcome to use!"))
        self.huzi.setText(_translate("jiemian", "性别:"))
        self.m1.setText(_translate("jiemian", "无"))
        self.toufa.setText(_translate("jiemian", "年龄:"))
        self.m2.setText(_translate("jiemian", "无"))
        self.yanjing.setText(_translate("jiemian", "情绪:"))
        self.m3.setText(_translate("jiemian", "无"))
        self.fuse.setText(_translate("jiemian", "漫画化:"))
        self.m4.setText(_translate("jiemian", "无"))
        self.lao.setText(_translate("jiemian", "油画化:"))
        self.m5.setText(_translate("jiemian", "无"))
        self.zhaopian.setText(_translate(
            "jiemian", "              Waiting to take..."))

    def guan(self, jiemian):
        global isclose
        isclose = True
        jiemian.close()

    def play(self):
        if not renwu.empty():
            nn = renwu.get()
            img = nn[0]
            n = nn[1]
            self.m1.setText(xingbie[n[0] + 1])
            self.m1.repaint()
            self.m2.setText(nianling[n[1] + 1])
            self.m2.repaint()
            self.m3.setText(qingxv[n[2] + 1])
            self.m3.repaint()
            self.m4.setText(manhua[n[3]])
            self.m4.repaint()
            self.m5.setText(youhua[n[4]])
            self.m5.repaint()
            self.m6.setText(nn[3])
            self.m6.repaint()
            try:
                temp = QtGui.QImage(
                    img, img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
                temp = temp.rgbSwapped()
                pixmap_temp = QtGui.QPixmap.fromImage(temp)
                self.shexiang.setPixmap(pixmap_temp)
                self.shexiang.setScaledContents(True)
                if nn[2]:
                    self.timerr.start(1000)
            except:
                print('No Frame')

    def daojishi(self):
        if self.biaoji >= 0:
            self.zhaopian.setText("              " + str(self.biaoji) + "...")
            self.zhaopian.repaint()
            self.biaoji -= 1
        else:
            global lu
            global ri
            if ri:
                img = renwu.get()[0]
                cv2.imwrite("./output/result.png", img)
                ri = False
            else:
                nnn = renwu.get()
                self.zhaopian.setText("              In the processing...")
                self.zhaopian.repaint()
                lu = False
                for i in range(5):
                    if nnn[1][i]:
                        gaoshiqing(i, nnn[1][i])
                ri = True
                self.biaoji = 3
                if nnn[1][4] == 1:
                    for i in range(170):
                        if i < 10:
                            p = "./output/result/00" + str(i) + ".png"
                        elif i < 100:
                            p = "./output/result/0" + str(i) + ".png"
                        else:
                            p = "./output/result/" + str(i) + ".png"
                        img2 = cv2.imread(p)
                        cv2.waitKey(0)
                        sleep(0.05)
                        temp2 = QtGui.QImage(
                            img2, img2.shape[1], img2.shape[0], img2.shape[1] * 3, QtGui.QImage.Format_RGB888)
                        temp2 = temp2.rgbSwapped()
                        pixmap_temp2 = QtGui.QPixmap.fromImage(temp2)
                        self.zhaopian.setPixmap(pixmap_temp2)
                        self.zhaopian.setScaledContents(True)
                    os.rename("./output/result/170.png", "./output/result/result.png")
                    shutil.move("./output/result/result.png", "./output/result.png")
            img = cv2.imread("./output/result.png")
            temp = QtGui.QImage(
                img, img.shape[1], img.shape[0], img.shape[1] * 3, QtGui.QImage.Format_RGB888)
            temp = temp.rgbSwapped()
            pixmap_temp = QtGui.QPixmap.fromImage(temp)
            self.zhaopian.setPixmap(pixmap_temp)
            self.zhaopian.setScaledContents(True)
            lu = True
            self.timerr.stop()


def showout():
    formm = QtWidgets.QDialog()
    ui = Ui_jiemian()
    ui.setupUi(formm)
    formm.show()
    formm.exec_()
