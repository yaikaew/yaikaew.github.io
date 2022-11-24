---
theme: jekyll-theme-merlot
title: Connect Google Sheet To Line
---
[<< Home](https://yaikaew.github.io/index.html)

## Setting Google Sheet

เปิด Google Sheet ที่เราได้สร้างไว้ จากนั้น Copy ลิ้งค์ไว้

![38](/images/Google Sheet and Line/38.png)


จากนั้นไปที่ส่วนขยาย

![01](/images/Google Sheet and Line/01.png)

![02](/images/Google Sheet and Line/02.png)


URL ที่นำมาให้ Copy จาก Google Sheet ของเรา และลบข้อความหลัง # ออก

![03](/images/Google Sheet and Line/03.png)


ตั้งค่าตัวแปร

![04](/images/Google Sheet and Line/04.png)


กำหนดว่าให้แสดงข้อความแบบใด

![05](/images/Google Sheet and Line/05.png)

![06](/images/Google Sheet and Line/06.png)


เมื่อเขียนเสร็จแล้วให้กดปุ่ม save

![07](/images/Google Sheet and Line/07.png)


ไปที่ปุ่ม การทำให้ใช้งานได้

![08](/images/Google Sheet and Line/08.png)


เลือกประเภทเป็นเว็บแอป แล้วกดอนุญาตสิทธิ์ให้เรียบร้อย

![09](/images/Google Sheet and Line/09.png)


ทำการ Copy URL ของเว็บแอปไว้ เพื่อนำไปใช้ต่อ

![10](/images/Google Sheet and Line/10.png)


ไปที่เว็บ [Dialogflow](https://dialogflow.cloud.google.com)

กดปุ่ม Creat Intent เพื่อสร้าง Intent ใหม่สำหรับเทรนข้อมูลที่รับ

![11](/images/Google Sheet and Line/11.png)

![12](/images/Google Sheet and Line/12.png)



มาที่ Training Phrases เพิ่มคำที่ต้องการให้ค้นหาเพื่อส่งค่ากลับมา

![13](/images/Google Sheet and Line/13.png)



ไปที่หัวข้อ Fulfillment นำ URL ที่เราได้จาก App Script มาวางไว้ จากนั้นกดปุ่ม save

![14](/images/Google Sheet and Line/14.png)


## Setting Line

[LINE Developers](https://developers.line.biz/en/)

![15](/images/Google Sheet and Line/15.png)

![16](/images/Google Sheet and Line/16.png)

![17](/images/Google Sheet and Line/17.png)

![18](/images/Google Sheet and Line/18.png)

![19](/images/Google Sheet and Line/19.png)

![20](/images/Google Sheet and Line/20.png)

![21](/images/Google Sheet and Line/21.png)

![22](/images/Google Sheet and Line/22.png)

![23](/images/Google Sheet and Line/23.png)


## Connect Google Sheet To Line

![24](/images/Google Sheet and Line/24.png)

![25](/images/Google Sheet and Line/25.png)

![26](/images/Google Sheet and Line/26.png)

![27](/images/Google Sheet and Line/27.png)


ไปที่หน้า Integrations แล้วเลื่อนลงมาจนเจอโลโก้ Line 

![28](/images/Google Sheet and Line/28.png)


เมื่อกดเข้าไปจะเจอกับหน้าที่ให้ใส่ข้อมูล ให้กลับไปที่หน้า Line แล้ว Copy ข้อมูลต่าง ๆ มาวาง

![29](/images/Google Sheet and Line/29.png)


จากนั้น Copy Webhook URL แล้วกดปุ่ START

![30](/images/Google Sheet and Line/30.png)


กลับไปที่หน้า Line ไปที่หน้า Massaging API แล้วเลื่อนลงมาด้านล่าง 

![31](/images/Google Sheet and Line/31.png)


นำ Webhook URL มาวางไว้แล้วกด Update

* ถ้าเคยใส่ลิ้งค์ไว้แล้วจะขึ้นให้ Edit แล้วกด Update เพื่อ Update ลิ้งค์ที่ได้มาใหม่

![32](/images/Google Sheet and Line/32.png)

![33](/images/Google Sheet and Line/33.png)


เลื่อนลงมาด้านล่าง แล้ว edit เมนู Auto-reply messages

![34](/images/Google Sheet and Line/34.png)


ตั้งค่าตามนี้

![35](/images/Google Sheet and Line/35.png)


ทดสอบการใช้งาน

![36](/images/Google Sheet and Line/36.png)

![37](/images/Google Sheet and Line/37.png)


[<< Home](https://yaikaew.github.io/index.html)
