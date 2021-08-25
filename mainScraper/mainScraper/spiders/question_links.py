from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request
# import csv

class QuestionsSpider(Spider):
    name = "qlinks"  # name of spider
    allowed_domains = ["https://leetcode.com"]  # base-URLs for the allowed domains for the spider to crawl
    start_urls = ["https://leetcode.com/problemset/all/?page=1"]  # URLs to start crawling from

    def parse(self, response):
        # Get the page
        filename = "questionLinks_noDup.txt" # only gets the first 50 questions since the default setting is 50 questions/page
        # filename = "question_links.csv"
        unique_links = set()
        divs = response.xpath('//div')
        with open(filename, 'w') as f:
            # csvwriter = csv.writer(f)
            for a in divs.xpath('.//a[re:test(@href, "^(?=.*problems)(?!^.*solutions).*")][has-class("h-5", "truncate")]/@href').getall():
            # for a in divs.xpath('.//a[contains(@href, "problems")][has-class("h-5", "truncate")]/@href').getall():
                # print(a) # <Selector xpath='.//a[contains(@href, "problems")]' data='<a href="/problems/reverse-integer" ...'>
                # f.write(a + '\n')
                unique_links.add(a)
                # csvwriter.writerows([[a]])

            for link in unique_links:
                f.write(link+'\n')
            # f.write(response.body)
            # f.write(response.body.xpath('//a[contains(@href, "problems")]'))
            # f.write(response.xpath('//*/div/a[contains(@href, "problems")]/@href').getall())
        # self.log(f'Saved file {filename}')
        # questions = Selector(response).xpath('//*[@id="__next"]/div/div/div[1]/'
        #                                      'div[1]/div[5]/div[2]/div/div/div[2]/div[2]/'
        #                                      'div[2]/div/div/div/a/@href').extract()
        # <a href= "/problems/two-sum" //*[@id="__next"]/div/div/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div
        # return questions
        # yield Request(questions)
        # print(questions)

    # def is_good_response(resp) -> bool:
    #     """
    #      Return True if the response seems to be HTML, otherwise return False.
    #     """
    #     content_type = resp.headers['Content-Type'].lower()
    #     print("HTTP Status Code: {0}".format(resp.status_code))
    #     return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)
    #
    # def log_error(e):
    #     """
    #     This function prints the errors.
    #     """
    #     print(e)
    #
    # def simple_get(url: str):
    #     """
    #     Attempts to get the content at 'url' by making an HTTP GET request.
    #     If the content-type of response is some kind of HTML/XML, return the text content, otherwise return None.
    #     """
    #     try:
    #         with closing(url, stream=True) as resp:
    #         if  is_good_response(resp):
    #             print("HTTP Error: {0}".format(resp.raise_for_status()))
    #             print(resp.headers)
    #             # the content is the HTML document
    #             return resp.content
    #         else:
    #             return None
    #
    #     except RequestException as e:
    #         log_error('Error during requests to {0} : {1}'.format(url, str(e)))
    #         return None





# if __name__ == "main":
#     s = QuestionsSpider()
#     response = HtmlResponse(url="https://leetcode.com/problemset/all/?page=1", encoding='utf8')
#     print(response)
#     s.parse(response)

