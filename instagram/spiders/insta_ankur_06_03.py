# import hashlib
# import json
#
# import scrapy
# import  pymysql
# from scrapy.cmdline import execute
# from scrapy.http import HtmlResponse
# import json
# from instagram.items import InstagramItem
# from  datetime import  datetime
#
#
# class instadata(scrapy.Spider):
#     name = "ankur_spider"
#     connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#     mycursor = connection.cursor()
#     start_urls = ['https://www.instagram.com/']
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#
#     def parse(self, response, **kwargs):
#         item = InstagramItem()
#         # sql = (f"SELECT * FROM firstlevelcategory_march  where status='pending'  limit {self.start}, {self.end} ")
#         sql = (f"SELECT * FROM firstlevelcategory_march  where status='done'  and id between {self.start} and {self.end} ")
#         # sql = (f'SELECT * FROM instapageid WHERE url_status="page not found" AND STATUS="pending"  limit {self.start}, {self.end} ')
#         self.mycursor.execute(sql)
#         result = self.mycursor.fetchall()
#         print(len(result))
#         for i in result:
#             id=int(i[0])
#             # id=658
#             handles=i[1]
#             # handles='avocadogreenbrands'
#             ins_url=i[2]
#             # ins_url='https://www.instagram.com/avocadogreenbrands'
#             # id="199"
#             # request_page=f"\\192.168.100.97\17_01_2023\\{id}.html"
#             request_page=f"\\\\192.168.100.97\\d\\VS Projects\\Levis\Levis\\bin\\Html1\\03_03_2023\\{id}.html"
#
#             #file://192.168.100.97/d/VS%20Projects/Levis/Levis/bin/Html1/03_03_2023/4.html
#             #\\192.168.100.97\d\VS Projects\Levis\Levis\bin\Html1\03_03_2023
#             #\\192.168.100.97\d\VS Projects\Levis\Levis\bin\Html1\03_03_2023
#             #D:\VS Projects\Levis\Levis\bin\Html1
#             #\\192.168.100.97\21_02_2023
#             # request_page=request_page.replace("\\\\","\\")
#             # request_page=request_page.replace("\\","\\\\")
#
#
#             try:
#                 with open(request_page, 'r',encoding='utf8') as f:
#                     data = f.read()
#                     f.close()
#                 response = HtmlResponse(url='', body=data.encode('utf8'))
#
#                 # ins_url="https://www.instagram.com/" +str(handles)
#                 # hash_id=str(int(hashlib.md5(bytes(ins_url, "utf8")).hexdigest(), 32) % (10 ** 32))
#                 # print(response.text)
#                 if "Page Not Found" in response.text:
#                     item['latest_post_date'] = ""
#                     item['ins_id'] = ""
#                     item['ins_url'] = ins_url
#                     item['Insta_Follower_Count'] = ""
#                     item['Insta_Following_Count'] = ""
#                     item['Insta_Media_Count'] = ""
#                     item['Insta_Bio'] = "not found data on this page "
#                     item['Insta_ProfileName'] = handles
#                     item['Insta_Bio_Link'] = ""
#                     item['Insta_FullName'] = ""
#                     item['Insta_Privacy'] = ""
#                     item['Insta_Verified'] = ""
#                     item['timestamp'] = ""
#                     item['Insta_Mutual_Followers_Count'] = ""
#                     item['fbid'] = ""
#                     item['Insta_Category'] = ""
#                     item['is_business'] = ""
#                     item['Insta_Profile_Pic_url'] = ""
#                     item['should_show_public_contacts'] = ""
#                     item['business_category_name'] = ""
#                     # item['hashid'] = hash_id
#                     item['pagesave_id'] = request_page.replace("\\", "\\\\")
#                     yield item
#                     con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#                     update = f"UPDATE firstlevelcategory_march SET `status`='not found' WHERE   Id = '{id}' "
#                     print()
#                     crsr = con.cursor()
#                     crsr.execute(update)
#                     con.commit()
#                 else:
#
#                     data=json.loads(response.text)
#
#                     try:
#                         user=data['user'] #data.user
#                         # print(user)
#                         if not user:
#                             item['latest_post_date'] = ""
#                             item['ins_id'] = ""
#                             item['ins_url'] = ins_url
#                             item['Insta_Follower_Count'] = ""
#                             item['Insta_Following_Count'] = ""
#                             item['Insta_Media_Count'] = ""
#                             item['Insta_Bio'] = "user data null "
#                             item['Insta_ProfileName'] = handles
#                             item['Insta_Bio_Link'] = ""
#                             item['Insta_FullName'] = ""
#                             item['Insta_Privacy'] = ""
#                             item['Insta_Verified'] = ""
#                             item['timestamp'] = ""
#                             item['Insta_Mutual_Followers_Count'] = ""
#                             item['fbid'] = ""
#                             item['Insta_Category'] = ""
#                             item['is_business'] = ""
#                             item['Insta_Profile_Pic_url'] = ""
#                             item['should_show_public_contacts'] = ""
#                             item['business_category_name'] = ""
#                             # item['hashid'] = hash_id
#                             item['pagesave_id'] = request_page.replace("\\", "\\\\")
#                             yield item
#
#                             con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#                             update = f"UPDATE firstlevelcategory_march SET `status`='null data' WHERE   Id = '{id}' "
#                             print()
#                             crsr = con.cursor()
#                             crsr.execute(update)
#                             con.commit()
#                         else:
#
#
#
#
#                             try:
#                                 ins_id=data['user']['pk_id'] #user.pk_id
#                             except Exception as e:
#                                 ins_id=""
#
#                             try:
#                                 ins_follower_count=data['data']['user']['edge_followed_by']['count'] #data.user.edge_followed_by.count
#                             except Exception as e:
#                                 ins_follower_count=""
#                             try:
#                                 ins_following_count=data['data']['user']['edge_follow']['count']#data.user.edge_follow.count
#                             except Exception as e:
#                                 ins_following_count=""
#                             try:
#                                 Insta_Media_Count=data['data']['user']['edge_owner_to_timeline_media']['count'] #data.user.edge_owner_to_timeline_media.count
#                             except Exception as e:
#                                 Insta_Media_Count=""
#                             try:
#                                 insta_bio=data['user']['biography_with_entities']['raw_text']#data.user.biography_with_entities.raw_text
#                             except Exception as e:
#                                 insta_bio=""
#                             # try:
#                             #     fbid=data['data']['user']['fbid']#data.user.fbid
#                             # except Exception as e:
#                             #     fbid=''
#                             # try:
#                             #     busines_category_name=data['data']['user']['business_category_name'] #data.user.business_category_name
#                             # except Exception as e:
#                             #     busines_category_name=''
#                             try:
#                                 ins_profile=data['user']['username']#user.username
#                             except Exception as e:
#                                 ins_profile=""
#                             try:
#                                 ins_bio_link=data['user']['external_url'] #data.user.external_url
#                             except Exception as e:
#                                 ins_bio_link=""
#                             try:
#                                 Insta_FullName=data['user']['full_name'] #data.user.full_name
#                             except Exception as e:
#                                 Insta_FullName=""
#                             try:
#                                 Insta_Privacy=data['user']['is_private']#data.user.is_private
#                             except Exception as e:
#                                 Insta_Privacy=""
#                             try:
#                                 Insta_Verified=data['user']['is_verified']#data.user.is_verified
#                             except Exception as e:
#                                 Insta_Verified=""
#                             try:
#                                 Insta_Mutual_Followers_Count=data['data']['user']['edge_mutual_followed_by'] #data.user.edge_mutual_followed_by.count
#                             except Exception as e:
#                                 Insta_Mutual_Followers_Count=""
#                             try:
#                                 Insta_Category=data['user']['category'] #user.category
#                             except Exception as e:
#                                 Insta_Category=""
#                             # try:
#                             #     is_business=data['data']['user']['is_business_account']
#                             # except Exception as e:
#                             #     is_business=''
#                             try:
#                                 Insta_Profile_Pic_url=data['user']['profile_pic_url']  #data.user.profile_pic_url
#                             except Exception as e:
#                                 Insta_Profile_Pic_url=""
#                             try:
#                                 public_contact=data['user']['public_phone_number'] #user.public_phone_number
#                             except Exception as e:
#                                 public_contact=""
#                             try:
#                                 email=data['user']['public_email'] #user.public_email
#                             except Exception as e:
#                                 email=""
#
#
#
#                             # try:
#                             #     timestamp=data['data']['user']['edge_felix_video_timeline']['edges'][0]['node']['taken_at_timestamp'] #data.user.edge_felix_video_timeline.edges[0].node.taken_at_timestamp
#                             #
#                             # except Exception as e:
#                             #     timestamp=""
#                             if "taken_at_timestamp" not in response.text:
#                                 item['timestamp'] = " "
#                                 # item['latest_post_date'] = timestamp
#                                 item['ins_id'] = ins_id
#                                 item['ins_url'] = ins_url
#                                 # item['Insta_Follower_Count'] = ins_follower_count
#                                 # item['Insta_Following_Count'] = ins_following_count
#                                 # item['Insta_Media_Count'] = Insta_Media_Count
#                                 item['Insta_Bio'] = insta_bio
#                                 item['Insta_ProfileName'] = ins_profile
#                                 item['Insta_Bio_Link'] = ins_bio_link
#                                 item['Insta_FullName'] = Insta_FullName
#                                 item['Insta_Privacy'] = Insta_Privacy
#                                 item['Insta_Verified'] = Insta_Verified
#                                 # item['timestamp'] = timestamp
#                                 # item['Insta_Mutual_Followers_Count'] = Insta_Mutual_Followers_Count
#                                 # item['fbid'] = fbid
#                                 item['Insta_Category'] = Insta_Category
#                                 # item['is_business'] = is_business
#                                 item['Insta_Profile_Pic_url'] = Insta_Profile_Pic_url
#                                 item['should_show_public_contacts'] = public_contact
#                                 item['email'] = email
#                                 # item['hashid'] = hash_id
#                                 item['pagesave_id'] = request_page.replace("\\", "\\\\")
#                                 yield item
#                                 con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#                                 update = f"UPDATE firstlevelcategory_march SET `status`='done_ff' WHERE   Id = '{id}' "
#                                 print()
#                                 crsr = con.cursor()
#                                 crsr.execute(update)
#                                 con.commit()
#                             elif "taken_at_timestamp" in response.text:
#                                 #data.user.edge_felix_video_timeline.edges[0].node.taken_at_timestamp
#                                 # timestamp = data['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['taken_at_timestamp'] #data.user.edge_felix_video_timeline.edges[0].node.taken_at_timestamp
#                                 timestamp = data['data']['user']['edge_felix_video_timeline']['edges'][0]['node']['taken_at_timestamp'] #data.user.edge_felix_video_timeline.edges[0].node.taken_at_timestamp
#                                 post_published_date = datetime.utcfromtimestamp(int(timestamp))
#                                 post_published_date = post_published_date.date()
#                                 post_published_date = datetime.strftime(post_published_date, "%d-%m-%Y")
#                                 if timestamp=="":
#                                     timestamp=data['data']['user']['edge_felix_video_timeline']['edges'][0]['node']['taken_at_timestamp']
#                                     post_published_date = datetime.utcfromtimestamp(int(timestamp))
#                                     post_published_date = post_published_date.date()
#                                     post_published_date = datetime.strftime(post_published_date, "%d-%m-%Y")
#
#                                     item['latest_post_date'] = post_published_date
#                                     item['ins_id']=ins_id
#                                     item['ins_url']=ins_url
#                                     item['Insta_Follower_Count']=ins_follower_count
#                                     item['Insta_Following_Count']=ins_following_count
#                                     item['Insta_Media_Count']=Insta_Media_Count
#                                     item['Insta_Bio']=insta_bio
#                                     item['Insta_ProfileName']=ins_profile
#                                     item['Insta_Bio_Link']=ins_bio_link
#                                     item['Insta_FullName']=Insta_FullName
#                                     item['Insta_Privacy']=Insta_Privacy
#                                     item['Insta_Verified']=Insta_Verified
#                                     item['timestamp']=post_published_date
#                                     item['Insta_Mutual_Followers_Count']=Insta_Mutual_Followers_Count
#                                     # item['fbid']=fbid
#                                     item['Insta_Category']=Insta_Category
#                                     # item['is_business']=is_business
#                                     item['Insta_Profile_Pic_url']=Insta_Profile_Pic_url
#                                     item['should_show_public_contacts'] = public_contact
#                                     item['email'] = email
#                                     # item['business_category_name'] = busines_category_name
#                                     # item['hashid'] = hash_id
#                                     item['pagesave_id'] = request_page.replace("\\","\\\\")
#                                     yield item
#
#                                     con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#                                     update = f"UPDATE firstlevelcategory_march SET `status`='done_ff' WHERE   Id = '{id}' "
#                                     print()
#                                     crsr = con.cursor()
#                                     crsr.execute(update)
#                                     con.commit()
#                                 else:
#                                     item['latest_post_date'] = post_published_date
#                                     item['ins_id'] = ins_id
#                                     item['ins_url'] = ins_url
#                                     item['Insta_Follower_Count'] = ins_follower_count
#                                     item['Insta_Following_Count'] = ins_following_count
#                                     item['Insta_Media_Count'] = Insta_Media_Count
#                                     item['Insta_Bio'] = insta_bio
#                                     item['Insta_ProfileName'] = ins_profile
#                                     item['Insta_Bio_Link'] = ins_bio_link
#                                     item['Insta_FullName'] = Insta_FullName
#                                     item['Insta_Privacy'] = Insta_Privacy
#                                     item['Insta_Verified'] = Insta_Verified
#                                     item['timestamp']=post_published_date
#                                     item['Insta_Mutual_Followers_Count'] = Insta_Mutual_Followers_Count
#                                     # item['fbid'] = fbid
#                                     item['Insta_Category'] = Insta_Category
#                                     # item['is_business'] = is_business
#                                     item['Insta_Profile_Pic_url'] = Insta_Profile_Pic_url
#                                     item['should_show_public_contacts'] = public_contact
#                                     # item['business_category_name'] = busines_category_name
#                                     item['email'] = email
#                                     # item['hashid'] = hash_id
#                                     item['pagesave_id'] = request_page.replace("\\", "\\\\")
#                                     yield item
#
#                                     con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#                                     update = f"UPDATE firstlevelcategory_march SET `status`='done_ff' WHERE   Id = '{id}' "
#                                     print()
#                                     crsr = con.cursor()
#                                     crsr.execute(update)
#                                     con.commit()
#
#
#
#                     except Exception as e:
#                         print(e)
#             except Exception as e:
#                 print(e)
#
#
#
# if __name__ == '__main__':
#     execute('scrapy crawl ankur_spider -a start=0 -a end=35000'.split())
#
#
#
#
#
#
#
#
