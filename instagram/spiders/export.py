# import pymysql
# import pandas as pd
#
# def insta_export():
#     host='localhost'
#     user = 'root'
#     passwd = 'xbyte'
#     db = 'instagram'
#     # table = ' restaurants'
#     # table1="restaurant"
#     table2="insta_new_data_ankur_26_03"
#     # table2="menu_tags"
#
#
#     con = pymysql.connect(host=host, user=user, password=passwd, database=db)
#
#     # qr="""select * from instapost"""
#     qr ="""SELECT
#     `insta_new_data_ankur_26_03`.`Id`,
#     `insta_new_data_ankur_26_03`.`ins_url`,
#     `insta_new_data_ankur_26_03`.`ins_id`,
#     CAST(`insta_new_data_ankur_26_03`.`Insta_ProfileName` AS CHAR) AS `Insta_ProfileName` ,
#     `insta_new_data_ankur_26_03`.`Insta_Type`,
#     `insta_new_data_ankur_26_03`.`Insta_Follower_Count`,
#     `insta_new_data_ankur_26_03`.`Insta_Following_Count`,
#     `insta_new_data_ankur_26_03`.`Insta_Media_Count`,
#     CAST(`insta_new_data_ankur_26_03`.`Insta_Bio` AS CHAR) AS `Insta_Bio`,
#     CAST(`insta_new_data_ankur_26_03`.`Insta_Bio_Link` AS CHAR) AS `Insta_Bio_Link`,
#     CAST(`insta_new_data_ankur_26_03`.`Insta_FullName` AS CHAR) AS `Insta_FullName`,
#     `insta_new_data_ankur_26_03`.`phone`,
#     `insta_new_data_ankur_26_03`.`email`,
#     `insta_new_data_ankur_26_03`.`Insta_Privacy`,
#     `insta_new_data_ankur_26_03`.`Insta_Verified`,
#     `insta_new_data_ankur_26_03`.`Insta_Following_Tag_Count`,
#     `insta_new_data_ankur_26_03`.`Insta_Total_igtv_Videos`,
#     `insta_new_data_ankur_26_03`.`Insta_Usertags_Count`,
#     #`insta_new_data_ankur_26_03`.`Insta_Mutual_Followers_Count`,
#     `insta_new_data_ankur_26_03`.`Insta_Category`,
#     # `insta_new_data_ankur_26_03`.`fbid`,
#     `insta_new_data_ankur_26_03`.`Insta_Profile_Pic_url`,
#     # `insta_new_data_ankur_26_03`.`business_category_name`,
#     `insta_new_data_ankur_26_03`.`Has_igtv_series`,
#     `insta_new_data_ankur_26_03`.`is_business`,
#     #`insta_new_data_ankur_26_03`.`has_highlight_reel`,
#    # `insta_new_data_ankur_26_03`.`total_clip_count`,
#     #`insta_new_data_ankur_26_03`.`public_phone_number`,
#      #`insta_new_data_ankur_26_03`.`ins_url`,
#     `insta_new_data_ankur_26_03`.`latest_post_date`,
#     `insta_new_data_ankur_26_03`.`pagesave_id`
#     FROM insta_new_data_ankur_26_03 ;
#
#      """
#
#     df_final = pd.read_sql(qr, con)
#
#     Writer = pd.ExcelWriter('instagram_ankur_data_27_03_2023.xlsx',engine='xlsxwriter',options={'strings_to_urls': False})
#     df_final.to_excel(Writer, sheet_name='table1', index=False)
#     # df_final.to_excel(Writer, sheet_name='table1', index=False)
#     Writer.save()
# if __name__ == '__main__':
#     insta_export()