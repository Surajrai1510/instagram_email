# import json
#
# import scrapy
# import  pymysql
# from scrapy.cmdline import execute
# from scrapy.http import HtmlResponse
# import json
# import time
# from instagram.items import InstagramItem
#
#
# class instadata(scrapy.Spider):
#     name = "insta_update"
#     connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#     mycursor = connection.cursor()
#     start_urls = ['https://www.instagram.com/']
#
#
#     def parse(self, response, **kwargs):
#         sql = (f"SELECT * FROM insta_new_data_09_02  where mail_update='pending'  and email IS null ")
#         self.mycursor.execute(sql)
#         result = self.mycursor.fetchall()
#         print(len(result))
#         for i in result:
#         #     # id=int(i[1])
#             id=i[2]
#             name = i[4]
#             name ='byvedha'
#             url = "https://www.instagram.com/" + name
#
#             # id="16239584327"
#
#             import requests
#             # Product_link = "https://m.instagram.com/api/v1/users/web_profile_info/?username=" + name+";"
#             # url = "https://instagram-scraper-2022.p.rapidapi.com/ig/business/"
#             #
#             # querystring = {"id_user": f"{id}"}
#             #
#             # headers = {
#             #     "X-RapidAPI-Key": "42bca6a056msh2bc743bc2347f00p13b91fjsn138a74255788",
#             #     "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
#             # }
#             proxy_dict = {
#                 # "http": f"http://brd-customer-hl_4fc8c816-zone-zone4_insta_test:i4v8bustsvah@zproxy.lum-superproxy.io:22225/",
#                 # "https": f"https://brd-customer-hl_4fc8c816-zone-zone4_insta_test:i4v8bustsvah@zproxy.lum-superproxy.io:22225/"
#                 "https": f"https://brd-customer-hl_4fc8c816-zone-zone_batch4_us:i4v8bustsvah@zproxy.lum-superproxy.io:22225/",
#                 "http": f"https://brd-customer-hl_4fc8c816-zone-zone_batch4_us:i4v8bustsvah@zproxy.lum-superproxy.io:22225/",
#
#             }
#
#             # response = requests.request("GET", url, headers=headers,proxies=proxy_dict, params=querystring,verify=False,timeout=1000)
#             response = requests.request("GET", url, proxies=proxy_dict,verify=False,timeout=1000)
#                 # time.sleep(40)
#                 #
#             print(response.text)
#
#             # import http.client
#             #
#             # conn = http.client.HTTPSConnection("instagram-data1.p.rapidapi.com")
#             #
#             # headers = {
#             #     'X-RapidAPI-Key': "42bca6a056msh2bc743bc2347f00p13b91fjsn138a74255788",
#             #     'X-RapidAPI-Host': "instagram-data1.p.rapidapi.com"
#             # }
#             #
#             # conn.request("GET", f"/user/contacts?user_id={id}", headers=headers)
#
#             # res = conn.getresponse()
#             # data = res.read()
#             data=response.text
#             jdata=json.loads(data)
#
#             try:
#                 mail=jdata['user']['public_email']#user.public_email
#             except Exception as e:
#                 mail=""
#             try:
#                 phone=jdata['user']['contact_phone_number'] #user.contact_phone_number
#             except Exception as e:
#                 phone=""
#
#             # print(data.decode("utf-8"))
#
#
#
#             con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#             update = f"UPDATE insta_new_data_09_02 SET `mail_update`='done_s',`phone`='{phone}' ,`email`='{mail}' WHERE   ins_id = '{id}' "
#             print(update)
#             print()
#             crsr = con.cursor()
#             crsr.execute(update)
#             con.commit()
#
#
#
#
# if __name__ == '__main__':
#     execute('scrapy crawl insta_update'.split())
#
#
#
#
#
#
#
#
