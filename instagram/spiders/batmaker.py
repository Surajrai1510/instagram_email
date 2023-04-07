total_count = 12000
divi = int(total_count /30)
parts = divi
#E:\instagram\instagram\spiders
with open('E:\\instagram\\instagram\\spiders\\pageupdate.bat', 'w+') as f:
    f.write("")
for i in range(0, total_count, parts):
    with open('E:\\instagram\\instagram\\spiders\\pageupdate.bat', 'a+') as f:
        # f.write(f'start "{i}" scrapy crawl airline_spider_second -a a={i} -a b={parts}')
        f.write(f'start py -m scrapy crawl insta_pagesave -a start={i} -a end={parts}')
        f.write('\n')
        # f.write('timeout 5')
        # f.write('\n')
        f.close()