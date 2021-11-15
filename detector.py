import os
import os.path
import argparse

PH = 'C:/Sigarette/darknet-master/'

parser = argparse.ArgumentParser()
parser.add_argument("--source")
args = parser.parse_args()
imput_file = args.source
path = f'image/{imput_file}'

def result_out(photo, im_file):
    '''
    Функция принимает фотографию и возвращает фотографию с отрисованными bounding box сигареты
    '''

    if photo[-3:] == 'mp4':
        os.system(f'{PH}darknet.exe detector demo {PH}cfg/coco.data {PH}cfg/custom-yolov4-detector_sig.cfg {PH}custom-yolov4-detector_best_sig.weights {photo}')
    else:
        os.system(f'{PH}darknet.exe detector test  {PH}cfg/coco.data {PH}cfg/custom-yolov4-detector_sig.cfg {PH}custom-yolov4-detector_best_sig.weights {photo} -dont-show')
        if os.path.exists(f'{im_file[:5]}_out.{im_file[6:]}'):
            os.remove('predictions.jpg')
        else:
            os.rename('predictions.jpg', f'{im_file[:5]}_out.{im_file[6:]}')

result_out(path, imput_file)