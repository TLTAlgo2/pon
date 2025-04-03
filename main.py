from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from os import listdir
from os.path import join
from PIL import Image, ImageOps


def get_image_name_from_working_directory():
    files = listdir(working_directory)
    list_images = []
    for file_name in files:
        if file_name.endswith((".png", ".jpg", ".jpeg")):
            list_images.append(file_name)

    list_widget_images.addItems(list_images)


def get_directory():
    global working_directory
    working_directory = QFileDialog().getExistingDirectory()
    get_image_name_from_working_directory()


def open_image_by_click(name_image):
    global image
    with Image.open(join(working_directory, name_image.text())) as opened_image:
        image = opened_image
    label.setPixmap(QPixmap(join(working_directory, name_image.text())))

# def left():

working_directory = ""
image = None

app = QApplication([])
main_widget = QWidget()
main_hbox = QHBoxLayout()

left_vbox = QVBoxLayout()
right_vbox = QVBoxLayout()
buttons_hbox = QHBoxLayout()

label = QLabel("Картинка")
button_select_dir = QPushButton("Папка")
button_go_left = QPushButton("Лево")
button_go_right = QPushButton("Право")
button_mirror = QPushButton("Зеркало")
button_rezkost = QPushButton("Резкость")
button_bw = QPushButton("Ч/Б")
button_save = QPushButton("Сохранить")
button_reset = QPushButton("Сбросить фильтры")

button_select_dir.clicked.connect(get_directory)


buttons_hbox.addWidget(button_go_left)
buttons_hbox.addWidget(button_go_right)
buttons_hbox.addWidget(button_mirror)
buttons_hbox.addWidget(button_rezkost)
buttons_hbox.addWidget(button_bw)
buttons_hbox.addWidget(button_save)
buttons_hbox.addWidget(button_reset)
left_vbox.addWidget(button_select_dir)
right_vbox.addWidget(label)
right_vbox.addLayout(buttons_hbox)

main_hbox.addLayout(left_vbox)
main_hbox.addLayout(right_vbox)

main_widget.setLayout(main_hbox)
main_widget.show()
app.exec_()





# from PIL import Image
# from PIL import ImageOps
# from PIL import ImageEnhance
# with Image.open('original.jpg') as r :
#     print('Размер:', r.size)
#     print('цветовой тип::', r.mode)
#     print('формат:', r.format)
#     gr = ImageOps.grayscale(r)
#     print('Размер:', gr.size)
#     print('цветовой тип::', gr.mode)
#     print('формат:', gr.format)
#     gr.save('original1.jpg')
#     grr = gr.rotate(90)
#     grr.save("original2.jpg")
#     rr = r.rotate(180)
#     rr.save('original3.jpg')
#     rrr = ImageOps.mirror(r)
#     rrr.save('original5.jpg')
#     gg= ImageEnhance.Contrast(r)
#     gg =  gg.enhance(1.5)
#     gg.save('contr.jpg')

  
#     r.show()
#     gr.show()
#     grr.show()
#     rr.show()
#     rrr.show()
#     gg.show()