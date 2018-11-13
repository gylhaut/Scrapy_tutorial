from scrapy import cmdline



#cmdline.execute("scrapy crawl quotes".split())
#cmdline.execute("scrapy crawl quotes -o quotes.json".split())

#cmdline.execute("scrapy crawl author -o author.jl".split())


cmdline.execute("scrapy crawl JiangRoomSpider".split())
# scrapy crawl quotes -o quotes.jl