from scrapy import Spider

class QuestionsSpider(Spider):
    name = "qlinks"  # name of spider
    allowed_domains = ["https://leetcode.com"]  # base-URLs for the allowed domains for the spider to crawl
    start_urls = ["https://leetcode.com/problemset/all/?page={}".format(i) for i in range(1, 41)]  # URLs to start crawling from

    def parse(self, response):
        filename = "all_unique_qlinks.txt" # only gets the first 50 questions since the default setting is 50 questions/page
        unique_links = set()  # to remove duplicates
        divs = response.xpath('//div')
        with open(filename, 'a') as f: # append mode 'a' to avoid overwriting
            # for a in divs.xpath('.//a[re:test(@href, "^(?=.*problems)(?!^.*solutions).*")][has-class("h-5", "truncate")]/@href').getall(): # works too; didn't need to exclude solns since it's already excluded
            for a in divs.xpath('.//a[contains(@href, "problems")][has-class("h-5", "truncate")]/@href').getall():
                unique_links.add(a)

            for link in unique_links:
                f.write(link+'\n')



