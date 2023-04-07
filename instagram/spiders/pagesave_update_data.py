import os.path

import scrapy
import  pymysql
from scrapy.cmdline import execute
from scrapy.http import HtmlResponse
import json
from instagram.items import InstagramItem
from  datetime import  datetime


class instadata(scrapy.Spider):
    name = "insta_pagesave"
    connection = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
    mycursor = connection.cursor()
    start_urls = ['https://www.instagram.com/']

    def __init__(self, start, end):
        self.start = start
        self.end = end
    def parse(self, response, **kwargs):
        global data1
        item = InstagramItem()
        # sql = (f"SELECT * FROM insta_new_data_ankur_26_03  where status_my='pending'  limit {self.start}, {self.end} ")
        sql = (f"SELECT `pagesave_id`,CAST(`Insta_ProfileName` AS CHAR)AS `Insta_ProfileName` FROM insta_new_data_ankur_26_03  where Insta_Category='None' and status_my='pending' limit {self.start},{self.end} ")
        # sql = (f'SELECT * FROM instapageInsta_ProfileName WHERE url_status_my="page not found" AND status_my="pending"  limit {self.start}, {self.end} ')
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        print(len(result))
        for i in result:
            # Insta_ProfileName = int(i[0])
            # Insta_ProfileName='cucina_71'
            Insta_ProfileName = i[1]
            # Insta_ProfileName ='zivent_stores.ng'
            # Html_path = i[38]
            Html_path = i[0]#.replace('D:','\\\\localhost\\d') #D:\Extract Data\Instagram\Html1\15_03_2023\535.html
            #\\192.168.100.97\d\Extract Data\Instagram\Html1\15_03_2023\26517.html
            # Html_path=f"\\\\192.168.100.97\\d\\Extract Data\\Html1\\15_03_2023\\26517.html"
            # Html_path=f"\\\\localhost\\d\\Extract Data\\Instagram\\Html1\\15_03_2023\\7389.html"
            #file:////localhost//d//Extract Data//Instagram//Html1//15_03_2023//8484.html
            #D:\Extract Data\Instagram\Html1\17_03_2023\8446.html
            # pagesave=f"\\\\localhost\\15_03_2023\\{Insta_ProfileName}.html"
            # pagesave=f"\\\\localhost\\d\\VS Projects\\Levis\Levis\\bin\\Html1\\03_03_2023\\{Insta_ProfileName}.html"
            #request_page = f"\\\\localhost\\d\\VS Projects\\Levis\Levis\\bin\\Html1\\03_03_2023\\{Insta_ProfileName}.html"
            #D:\VS Projects\Levis\Levis\bin\Html1\15_03_2023\3.html

            if os.path.exists(Html_path):
                with open(Html_path,'r',encoding='utf-8') as e:
                    data=e.read()
                    e.close()
                response = HtmlResponse(url='', body=data.encode('utf8'))
                print(response)
                if "Page Not Found" in response.text:
                    con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
                    update = f"UPDATE insta_new_data_ankur_26_03 SET `status_my`='not found' WHERE   Insta_ProfileName = '{Insta_ProfileName}' "
                    print()
                    crsr = con.cursor()
                    crsr.execute(update)
                    con.commit()
                else:
                    try:
                        data = json.loads(response.text)


                        try:
                            message=data['message']#message
                        except Exception as e:
                            message=''
                        if message is None:
                            con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
                            update = f"UPDATE insta_new_data_ankur_26_03 SET `status_my`='not null' WHERE   Insta_ProfileName = '{Insta_ProfileName}' "
                            # print()
                            crsr = con.cursor()
                            crsr.execute(update)
                            con.commit()
                        else:
                            data1 = data['data']['user'] #data.user
                            if data1 is not None:
                                # try:
                                #     phone=data1['public_phone_number'] #user.following_tag_count
                                # except Exception as e:
                                #     print(e)
                                #user.category
                                # try:
                                #     category = data1['category']  # user.category
                                # except Exception as e:
                                #     print(e)
                                # try:
                                #     tag_count = data1['following_tag_count']  # user.following_tag_count
                                # except Exception as e:
                                #     print(e)
                                # con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
                                # update = f'UPDATE insta_new_data_13_03_ankur_new SET Insta_Following_Tag_Count="{tag_count}"  WHERE   Insta_ProfileName = "{Insta_ProfileName}" '
                                # # print()
                                # crsr = con.cursor()
                                # crsr.execute(update)
                                # print("data update ")
                                # con.commit()
                                # con = pymysql.connect(host="localhost", user="root", password="xbyte",
                                #                       database="instagram")
                                # update = f"UPDATE insta_new_data_13_03_ankur_new SET `status_my`='tagdone' WHERE   Insta_ProfileName = '{Insta_ProfileName}' "
                                # # print()
                                # crsr = con.cursor()
                                # crsr.execute(update)
                                # con.commit()
                                # try:
                                #     Insta_ProfileName=data1['Insta_ProfileName'] #data.user.Insta_ProfileName
                                # except Exception as e:
                                #     print(e)
                                # try:
                                #     follower_count=data1['edge_followed_by']['count']
                                # except Exception as e:
                                #     print(e)
                                # try:
                                #     following_count=data1['edge_follow']['count']
                                # except Exception as e:
                                #     print(e)
                                # try:
                                #     media_count=data1['edge_owner_to_timeline_media']['count']
                                # except Exception as e:
                                #     print(e)
                                # try:
                                #     insta_bio=data1['biography_with_entities']['raw_text']
                                #     insta_bio = insta_bio.replace('"','\"').replace("'","")
                                # except Exception as e:
                                #     print(e)
                                # try:
                                #     bio_link=data1['bio_links'][0]['url']
                                # except Exception as e:
                                #     print(e)
                                try:
                                    category_name=data1['category_name'] #user.category
                                except Exception as e:
                                    print(e)
                                # try:
                                #     business=data1['is_business_account']#user.is_business
                                #     # business.strip()
                                # except Exception as e:
                                #     print(e)
                                # try:#data.user.edge_owner_to_timeline_media.edges[0].node.taken_at_timestamp
                                #     timestamp = data['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node'][
                                #         'taken_at_timestamp']  # data.user.edge_felix_vInsta_ProfileNameeo_timeline.edges[0].node.taken_at_timestamp
                                #     # timestamp = data['user']['edge_felix_vInsta_ProfileNameeo_timeline']['edges'][0]['node']['taken_at_timestamp'] #data.user.edge_felix_vInsta_ProfileNameeo_timeline.edges[0].node.taken_at_timestamp
                                #     post_published_date = datetime.utcfromtimestamp(int(timestamp))
                                #     post_published_date = post_published_date.date()
                                #     post_published_date = datetime.strftime(post_published_date, "%d-%m-%Y")
                                #     if timestamp == "":
                                #         timestamp = data['user']['edge_felix_vInsta_ProfileNameeo_timeline']['edges'][0]['node'][
                                #             'taken_at_timestamp']
                                #         post_published_date = datetime.utcfromtimestamp(int(timestamp))
                                #         post_published_date = post_published_date.date()
                                #         post_published_date = datetime.strftime(post_published_date, "%d-%m-%Y")
                                try:
                                    con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
                                    update = f'''UPDATE insta_new_data_ankur_26_03 SET Insta_Category="{category_name}"  WHERE   Insta_ProfileName = "{Insta_ProfileName}" '''

                                    crsr = con.cursor()
                                    crsr.execute(update)
                                    print("data update ")
                                    con.commit()
                                    con = pymysql.connect(host="localhost", user="root", password="xbyte",
                                                          database="instagram")
                                    update = f"UPDATE insta_new_data_ankur_26_03 SET `status_my`='done_ff1' WHERE   Insta_ProfileName = '{Insta_ProfileName}' "
                                    # print()
                                    crsr = con.cursor()
                                    crsr.execute(update)
                                    print("status_my update")
                                    con.commit()
                                except Exception as e:
                                   print(e)
                                #     else:
                                #         try:
                                #             con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
                                #             update = f'''UPDATE insta_new_data_13_03_ankur_new SET Insta_Category='{category_name}',is_business='{business}',latest_post_date="{post_published_date}",Insta_Follower_Count="{follower_count}",Insta_Following_Count="{following_count}",Insta_Media_Count="{media_count}",`Insta_Bio`='{insta_bio}'  WHERE `Insta_ProfileName`="{Insta_ProfileName}"'''
                                #             # print()
                                #             crsr = con.cursor()
                                #             crsr.execute(update)
                                #             print("data update ")
                                #             con.commit()
                                #
                                #         except Exception as e:
                                #             print(e)
                                #         con = pymysql.connect(host="localhost", user="root", password="xbyte",
                                #                               database="instagram")
                                #         update = f"UPDATE insta_new_data_ankur_26_03 SET `status_my`='done_ff1' WHERE   `Insta_ProfileName` = '{Insta_ProfileName}' "
                                #         # print()
                                #         crsr = con.cursor()
                                #         crsr.execute(update)
                                #         print("status_my update")
                                #         con.commit()
                                # except Exception as e:
                                #     con = pymysql.connect(host="localhost", user="root", password="xbyte",
                                #                           database="instagram")
                                #     update = f'''UPDATE insta_new_data_13_03_ankur_new SET Insta_Category="{category_name}",is_business="{business}",latest_post_date="",Insta_Follower_Count="{follower_count}",Insta_Following_Count="{following_count}",Insta_Media_Count="{media_count}",`Insta_Bio`='{insta_bio}'  WHERE   Insta_ProfileName = "{Insta_ProfileName}" '''
                                #
                                #     crsr = con.cursor()
                                #     crsr.execute(update)
                                #     print("data update ")
                                #     con.commit()


                            else:
                                con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
                                update = f"UPDATE insta_new_data_ankur_26_03 SET `status_my`='data null' WHERE   `Insta_ProfileName` = '{Insta_ProfileName}' "
                                # print()
                                crsr = con.cursor()
                                crsr.execute(update)
                                con.commit()
                    except Exception as e:
                        print(e)
            else:
                con = pymysql.connect(host="localhost", user="root", password="xbyte", database="instagram")
                update = f"UPDATE insta_new_data_ankur_26_03 SET `status_my`='not found page' WHERE   `Insta_ProfileName` = '{Insta_ProfileName}' "
                print()
                crsr = con.cursor()
                crsr.execute(update)
                con.commit()





if __name__ == '__main__':
    execute('scrapy crawl insta_pagesave -a start=0 -a end=12000'.split())
