# import  pymysql
# from googletrans import Translator, constants
# import  re
# from scrapy.http import HtmlResponse
# import json
# from  datetime import  datetime,date
# import emoji
# translator = Translator()
#
# connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
# mycursor = connection.cursor()
#
#
# sql = (f"SELECT * FROM insta_new_data_09_02 WHERE   email IS null ")
# # sql = (f"SELECT * FROM insta_new_data_18_01 WHERE Insta_Bio LIKE '%@gmail%' AND email='' ")
#
# mycursor.execute(sql)
# result = mycursor.fetchall()
# print(len(result))
# for i in result:
#     bio =i[9]
#     if type(bio) is bytes:
#         bio = bio.decode()
#     # timestamp =1659000447
#     id = int(i[0])
#     # bio = translator.translate(bio,src="en")
#     # print(bio)
#
#     # list1=[]
#     # list1.append(bio)
#     # phone=re.findall("\d{9}\d",str(bio))
#     # phone="".join(phone)
#     # print(phone)
#     #
#     if '@gmail' in bio:
#         bio=bio.split("@gmail")[0].replace("\n"," ")
#         bio=bio.split(" ")[-1]
#         email=bio+"@gmail"+".com"
#         email = ''.join(c for c in email if c not in emoji.UNICODE_EMOJI['en'])
#         print(email)
#
#     # update = f"UPDATE insta_new_data_09_02 SET `phone`='{str(phone)}' WHERE   Id = '{id}' "
#         update = f"UPDATE insta_new_data_09_02 SET `email`='{email}' WHERE   Id = '{id}' "
#         print(update)
#         crsr = connection.cursor()
#         crsr.execute(update)
#         connection.commit()
#
#
