# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import  pymysql
from instagram.items import InstagramItem


class InstagramPipeline:
    host = "localhost"
    passwd = "xbyte"
    uname = "root"
    con1 = pymysql.connect(host=host, user=uname, password=passwd)
    db_name = "instagram"  # databse name
    data = "insta_new_data_ankur_26_03"




    def process_item(self, item, spider):
        if isinstance(item,InstagramItem):
            try:
                    con = pymysql.connect(host=self.host, user=self.uname, password=self.passwd,
                                          database=f'{self.db_name}')
                    crsr = con.cursor()
                    field_list = []
                    value_list = []
                    for field in item:
                        field_list.append(f'`{str(field)}`')
                        value_list.append(str(item[field]).replace("'", "’"))
                    fields = ','.join(field_list)
                    values = "','".join(value_list)
                    insert_db = f"insert into {self.data}" + "( " + fields + " ) values ( '" + values + "' )"
                    print(insert_db)
                    crsr.execute(insert_db)
                    con.commit()
                    print(insert_db)


            except Exception as e:
                    print(str(e))
        return item
