#Import Library
import json
import os
from flask import Flask
from flask import request
from flask import make_response
import random

# Flask
app = Flask(__name__)
@app.route('/', methods=['POST']) 

def MainFunction():

    #รับ intent จาก Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)

    #เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    answer_from_bot = generating_answer(question_from_dailogflow_raw)

    #ตอบกลับไปที่ Dailogflow
    ans = make_response(answer_from_bot)
    ans.headers['Content-Type'] = 'application/json' #การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป

    return ans

def generating_answer(question_from_dailogflow_dict):

    #Print intent ที่รับมาจาก Dailogflow
    print(json.dumps(question_from_dailogflow_dict, indent=4 ,ensure_ascii=False))

    #เก็บค่า ชื่อของ intent ที่รับมาจาก Dailogflow
    intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"] 

    #ตัวเลือกของฟังก์ชั่นสำหรับตอบคำถามกลับ
    if intent_group_question_str == 'เมนูข้าว':
        answer_str = menu_recormentation_rice()
    elif intent_group_question_str == 'เมนูเส้น':
        answer_str = menu_recormentation_noodle()
    elif intent_group_question_str == 'ของหวาน':
        answer_str = menu_recormentation_sweet()
    elif intent_group_question_str == 'say yes':
        answer_str = bmi(question_from_dailogflow_dict)
    elif intent_group_question_str == "สวัสดี":
        answer_str = hello()
    else: answer_str = "ขอโทษค่ะ ฉันไม่สามารถเข้าใจคำถามได้ กรุณาปรับเปลี่ยนคำถามเล็กน้อยแล้วลองอีกครั้งได้ไหมคะ"
    #สร้างการแสดงของ dict 
    answer_from_bot = {"fulfillmentText": answer_str}
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    return answer_from_bot

def hello(): #สวัสดี
    answer = "สวัสดีค่ะ ฉันคือ <e> MAE มีอะไรให้ช่วยไหมคะ"
    return answer


def menu_recormentation_rice(): #ฟังก์ชั่นสำหรับเมนูแนะนำข้าว
    menu_name1 = ["ผัดกะเพราหมูสับ", "ข้าวขาหมู", "ข้าวมันไก่", "ข้าวไข่เจียว", "ข้าวพะแนงไก่", "ปลากระพงทอดน้ำปลา", "ข้าวคลุกกะปิ ",\
                 "ข้าวผัดปลากระป๋อง", "กะเพราปลาหมึก", "ผัดกะเพราหมูกรอบ", "ผัดกะเพราไก่", "ผัดคะน้าหมูกรอบ", "ผัดผักบุ้ง", "ผัดผักรวม", "ผัดผงกะหรี่", "หมูกระเทียม",\
                    "ผัดเปรี้ยวหวาน", "ข้าวผัดไข่", "ข้าวผัดหมู", "ข้าวผักทะเล"]
    answer_function1 = ''.join(random.choice(menu_name1)) + ' สิน่ากินนะคะ'
    return answer_function1


def menu_recormentation_noodle(): #ฟังก์ชั่นสำหรับเมนูแนะนำเมนูเส้น
    menu_name2 = ["ขนมจีนน้ำพริก", "ขนมจีนน้ำยากะทิ", "ขนมจีนน้ำยาป่า", "ขนมจีนน้ำยาแกงเขียวหวาน", "ขนมจีนน้ำเงี้ยว", "ก๋วยเตี๋ยวไก่มะระ",\
                "ก๋วยเตี๋ยวหมูน้ำตก", "ก๋วยเตี๋ยวเนื้อ", "ก๋วยเตี๋ยวเรือ", "ผัดไทยกทะเล", "ผัดไทยหมู", "ผัดซีอิ๊วหมู", "ผัดซีอิ๊ว", "สุกี้ทะเล",\
                "สุกี้หมู", "สปาเกตตีคาร์โบนารา", "สปาเกตตีผัดขี้เมาทะเล", "สปาเกตตีราดซอสมะเขือเทศ", "สปาเกตตีเบคอนพริกกระเทียม", "ก๋วยจั๊บญวน",\
                "ก๋วยจั๊บเยาวราช"]
    answer_function2 = ''.join(random.choice(menu_name2)) + ' สิน่ากินนะคะ'
    return answer_function2


def menu_recormentation_sweet(): #ฟังก์ชั่นสำหรับเมนูแนะนำเมนูของหวาน
    menu_name3 = ["ข้าวเหนียวมะม่วง", "ขนมชั้น", "เต้าส่วน", "บัวลอยไข่หวาน", "บัวลอย", "กล้วยบวชชี", "วุ้นกะทิใบเตย", "วุ้นมะพร้าว",\
                "ลูกชุบ", "ลูกตาลลอยแก้ว", "ขนมเบื้อง", "ไอศกรีม", "บิงซู", "แพนเค้ก", "บานอฟฟี่พาย", "ชีสเค้ก", "วาฟเฟิล",\
                "เอแคลร์", "คุกกี้", "มาการอง", "เครป", "เค้ก", "บราวนี่", "ขนมครก" , "คัพเค้ก"]
    answer_function3 = ''.join(random.choice(menu_name3)) + ' สิน่ากินนะคะ'
    return answer_function3


def bmi(respond_dict): #ฟังก์ชั่นสำหรับคำนวนBMI
    #เก็บค่าของ Weight กับ Height
    weight1 = float(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["Weight.original"])
    height1 = float(respond_dict["queryResult"]["outputContexts"][1]["parameters"]["Height.original"])
    #คำนวนBMI
    thebmi = (weight1/(height1/100)**2)
    if thebmi < 18.5 :
        answer_function = ("ค่าดัชนีมวลกายของคุณคือ %.2f ผอมจัง กินเยอะๆหน่อยนะคะ" %thebmi)
    elif 18.5 <= thebmi < 23.0:
        answer_function = ("ค่าดัชนีมวลกายของคุณคือ %.2f สมส่วน สุดยอดเลยค่ะ" %thebmi)
    elif 23.0 <= thebmi < 25.0:
        answer_function = ("ค่าดัชนีมวลกายของคุณคือ %.2f ค่อนข้างอ้วน ลดหน่อยก็ดีค่ะ" %thebmi)
    elif 25.0 <= thebmi < 30:
        answer_function = ("ค่าดัชนีมวลกายของคุณคือ %.2f อ้วนล่ะนะ ลดหน่อยนะคะ" %thebmi)
    else :
        answer_function = ("ค่าดัชนีมวลกายของคุณคือ %.2f อ้วนมากจ้าา ลดด่วนนน!!!" %thebmi)
    return answer_function


#Flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
