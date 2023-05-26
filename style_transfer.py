import paddlehub as hub
import cv2
import pymysql
import sys
import paddle
def style_transfer(imagename,choice,account):
    paddle.set_device('gpu')
    picture = 'C:\\style_transfer\\inputs\\'+imagename
    if choice=="0":
        style_image = 'C:\\style_transfer\\style\\fangao.jpg'
    elif choice=="1":
        style_image = 'C:\\style_transfer\\style\\shuimo.jpg'
    elif choice=="2":
        style_image = 'C:\\style_transfer\\style\\donghua2.jpg'
    
    stylepro_artistic = hub.Module(name="stylepro_artistic")
    result = stylepro_artistic.style_transfer(
                    images=[{'content': cv2.imread(picture),
                             'styles': [cv2.imread(style_image)]}],
                    visualization=True,
                    output_dir="C:\\style_transfer\\outputs"
    )
    mypath = result[0]['save_path']
    print(mypath)
    mypath = eval(repr(mypath).replace('\\','/'))
    print(mypath)
    db = pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db='app')
    r= db.cursor()
    sql = "update useroutput set path='"+ mypath +"' where account='"+account+"'"
    r.execute(sql)
    db.commit()
    r.close()
    db.close()
if __name__ == '__main__' :
    name = sys.argv[1]
    choice = sys.argv[2]
    account = sys.argv[3]
    style_transfer(name,choice,account)




    

# # 待转换图片的绝对地址
# picture = 'C:\\style_transfer\\inputs\\pic.jpg'  # 注意代码中此处为双反斜杠
# # 风格图片的绝对地址
# style_image = 'C:\\style_transfer\\style\\fangao.jpg'

# # 创建风格转移网络并加载参数
# stylepro_artistic = hub.Module(name="stylepro_artistic")

# # 读入图片并开始风格转换
# result = stylepro_artistic.style_transfer(
#                     images=[{'content': cv2.imread(picture),
#                              'styles': [cv2.imread(style_image)]}],
#                     visualization=True,
#                     output_dir = "C:\\style_transfer\\outputs")
# print(result[0]['save_path'])