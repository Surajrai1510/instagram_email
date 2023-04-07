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
#     name = "insert_spider"
#     connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
#     mycursor = connection.cursor()
#     start_urls = ['https://www.instagram.com/']
#
#     def parse(self, response, **kwargs):
#         item = InstagramItem()
#         # sql = (f"SELECT * FROM firstlevelcategory  where status='pending'  limit {self.start}, {self.end} ")
#         sql = (f"SELECT * FROM firstlevelcategory  where status='Not Found' ")
#         # sql = (f'SELECT * FROM instapageid WHERE url_status="page not found" AND STATUS="pending"  limit {self.start}, {self.end} ')
#         self.mycursor.execute(sql)
#         result = self.mycursor.fetchall()
#         print(len(result))
#         for i in result:
#             id=int(i[0])
#             handles=i[1]
#             # id="199"
#             # request_page=f"\\192.168.100.97\17_01_2023\\{id}.html"
#             request_page=f"\\\\192.168.100.97\\21_02_2023\\{id}.html"
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
#                 if "Sorry, this page" in response.text:
#                     item['latest_post_date'] = ""
#                     item['ins_id'] = ""
#                     item['Insta_Follower_Count'] = ""
#                     item['Insta_Following_Count'] = ""
#                     item['Insta_Media_Count'] = ""
#                     item['Insta_Bio'] = ""
#                     item['Insta_ProfileName'] = "not found data on this page "
#                     item['Insta_Bio_Link'] = ""
#                     item['Insta_FullName'] = ""
#                     item['Insta_Privacy'] = ""
#                     item['Insta_Verified'] = ""
#                     item['timestamp'] = ""
#                     item['Insta_Mutual_Followers_Count'] = ""
#                     item['Insta_Category'] = ""
#                     item['is_business'] = ""
#                     item['Insta_Profile_Pic_url'] = ""
#                     item['should_show_public_contacts'] = ""
#                     item['pagesave_id'] = request_page.replace("\\", "\\\\")
#                     yield item
#             except:
#                 print()
#
# if __name__ == '__main__':
#     execute('scrapy crawl insert_spider '.split())