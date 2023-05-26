import cv2
import paddlehub as hub
import pymysql
import os
import random
import sys

def myocr(imageName,account):
    print(imageName)
    ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")
    np_images = [cv2.imread("C:\inputs\\"+imageName)]

    results = ocr.recognize_text(
        images=np_images,  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
        use_gpu=False,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
        output_dir="C:\outputs\\img",  # 图片的保存路径，默认设为 ocr_result；
        visualization=True,  # 是否将识别结果保存为图片文件；
        box_thresh=0.5,  # 检测文本框置信度的阈值；
        text_thresh=0.5)  # 识别中文文本置信度的阈值；
    save_path = results[0]['save_path']
    temp = save_path[:15]
    print(temp)
    newName = temp + str(random.randint(0,100))+ ".jpg"
    print(newName)
    os.rename(save_path,newName)
    db = pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db='app')
    r= db.cursor()
    sql = "update userimage set imgname='"+ newName[14:] +"' where account="+"'"+account+"'"
    print(sql)
    print(newName[15:])
    r.execute(sql)
    db.commit()
    r.close()
    db.close()
    data = results[0]['data']
    end = ""
    for information in data:
        end = end + information['text']
    
    with open("C:\outputs\\text\\"+ newName[15:-4] +".txt" ,'w',encoding='utf-8') as f:
        f.write(str(end))
        f.close
    print(str(end))
    #     for infomation in data:
    #         print('text: ', infomation['text'], '\nconfidence: ', infomation['confidence'], '\ntext_box_position: ',
    #               infomation['text_box_position'])
if __name__ == '__main__' :
    
    imgname = sys.argv[1]
    account = sys.argv[2]
    myocr(imgname,account)