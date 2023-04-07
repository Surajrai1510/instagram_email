# import  pymysql
# from scrapy.http import HtmlResponse
# import json
# from  datetime import  datetime,date
#
# connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
# mycursor = connection.cursor()
#
#
# sql = (f"SELECT * FROM insta_new_data_21_02_2023  where timesatmp_status='pending'  ")
#
# mycursor.execute(sql)
# result = mycursor.fetchall()
# print(len(result))
# for i in result:
#     # header =i[1]
#     # timestamp =1659000447
#     id = int(i[0])
#     timestamp=i[29]
#     post_published_date = datetime.utcfromtimestamp(int(timestamp))
#     post_published_date = post_published_date.date()
#     post_published_date = datetime.strftime(post_published_date, "%d-%m-%Y")
#     connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#     update = f"UPDATE insta_new_data_21_02_2023 SET `timesatmp_status`='done',`latest_post_date`='{post_published_date}' WHERE   Id = '{id}' "
#     print(update)
#     crsr = connection.cursor()
#
#     crsr.execute(update)
#     connection.commit()
#     # url="https://www.instagram.com/"+header
#     # update = f"UPDATE insta_new_data SET `pagesave_id`='{id}',`ins_url`='{url}' WHERE   Insta_ProfileName = '{header}' "
#     # print(update)
#     # crsr = connection.cursor()
#     # crsr.execute(update)
#     # connection.commit()
#
#     # update = f"UPDATE instapageid SET `url_status`='done' WHERE   id = '{id}' "
#     # print(update)
#     # crsr = connection.cursor()
#     # crsr.execute(update)
#     # connection.commit()
#     # id=1673
#     # request_page = f"\\\\192.168.100.97\\\\21_12_2022\\\\{id}.html"
#     # request_page=request_page.replace("\\\\","\\")
#     # request_page=request_page.replace("\\","\\\\")
#     # if request_page
#     # try:
#     #     with open(request_page, 'r', encoding='utf8') as f:
#     #         data = f.read()
#     #         f.close()
#     #     response = HtmlResponse(url='', body=data.encode('utf8'))
#
#
#
#         # if "Sorry, this page" in response.text:
#         #     connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#         #     update = f"UPDATE instapageid SET `url_status`='not found' WHERE   Id = '{id}' "
#         #     print()
#         #     crsr = connection.cursor()
#         #
#         #     crsr.execute(update)
#         #     connection.commit()
#         # else:
#         #
#         #     data = json.loads(response.text)
#
#             # try:
#             #     ins_following_count = data['data']['user']['edge_follow']['count']  # data.user.edge_follow.count
#             # except Exception as e:
#             #     ins_following_count = ""
#
#             # print(post_published_date)
#
#     # except Exception as e:
#     #     connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#     #     update = f"UPDATE instapageid SET `url_status`='page not found' WHERE   Id = '{id}' "
#     #     print()
#     #     crsr = connection.cursor()
#     #     crsr.execute(update)
#     #     connection.commit()
#
