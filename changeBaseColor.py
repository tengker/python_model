import cv2
import numpy as np
import random
import pymysql
import sys
def baseColor(account,choice,path):
    print(account)
    print('/n')
    print(choice)
    print('/n')
    print(path)
    print('/n')
    inputpath = "C:/baseColor/input/"+account
    temp_account = account
    img = cv2.imread(inputpath, 1)
    new_img = cv2.resize(img, None, fx=0.5, fy=0.5)

    rows, cols, channels = new_img.shape
    print(rows, cols, channels)
    gray_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
    low_value = np.array([90, 70, 70])
    high_value = np.array([110, 255, 255])
    binary_img = cv2.inRange(gray_img, low_value, high_value)
    erode = cv2.erode(binary_img, None, iterations=1)
    dilate = cv2.dilate(erode, None, iterations=1)
    print(temp_account)
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:
                if(choice=="0"):
                    new_img[i, j] = (255, 0, 0)
                elif(choice=="1"):
                    new_img[i , j] = (0,0,255)
                elif(choice=="2"):
                    new_img[i,j] = (255,255,255)
    outpath = "C:/baseColor/output/"+str(random.randint(1,100))+".png"
    print(outpath)
    cv2.imwrite(outpath,new_img)
    db = pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db='app')
    r= db.cursor()
    sql = "update basecolor set path='"+ outpath +"' where account='"+path+"'"
    print(sql)
    r.execute(sql)
    db.commit()
    r.close()
    db.close()

if __name__ == '__main__' :
    path = sys.argv[1]
    choice = sys.argv[2]
    account = sys.argv[3]
    baseColor(account,choice,path)
   # baseColor("admin","2","color.png")