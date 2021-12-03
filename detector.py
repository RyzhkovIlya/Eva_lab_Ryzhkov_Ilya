import os
import os.path
import argparse

PH = 'C:/Sigarette/darknet-master/' # Необходимо указать путь до папки darknet-master

parser = argparse.ArgumentParser()
parser.add_argument("--source") # Добавляем кастомный флаг ввода "--source"
args = parser.parse_args() # ввод в командную строку. Пример - "python3 detector.py --source 00001.png"
imput_file = args.source # Введенное изображение "00001.png"
path = f"image/{imput_file}" # Изображение из папки "image"

def result_out(photo, im_file):
    '''
    Функция принимает фотографию и возвращает фотографию с отрисованными bounding box сигареты
    '''

    format_photo = ["jpg", "jpeg", "png"]
    if photo[-3:] == "mp4": # Если файл - видео
        os.system(f"{PH}darknet.exe detector demo {PH}cfg/coco.data {PH}cfg/custom-yolov4-detector_sig.cfg {PH}custom-yolov4-detector_best_sig.weights {photo}")
    elif photo[-3:] in format_photo: # Если файл - фотография
        os.system(f"{PH}darknet.exe detector test  {PH}cfg/coco.data {PH}cfg/custom-yolov4-detector_sig.cfg {PH}custom-yolov4-detector_best_sig.weights {photo} -dont-show")
        if os.path.exists(f"{im_file[:5]}_out.{im_file[6:]}"): # Если делаем предсказание второй раз на одной и той де фотографии, то перезаписываем ее
            os.remove('predictions.jpg') # Удаляем файл "predictio.jpg"
        else:
            os.rename("predictions.jpg", f"{im_file[:5]}_out.{im_file[6:]}") # Переименовываем файл в формат "00001_out.png"
    else:
        return "Данный форма файла не поддерживается!"

result_out(path, imput_file) # Делаем предсказания всех файлов из папки "image" 

for ph in "image/":
    path_all = f"image/{ph}"
    result_out(path_all, ph)
