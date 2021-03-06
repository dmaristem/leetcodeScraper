from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request

class QuestionsSpider(Spider):
    name = "scraper"  # name of spider
    allowed_domains = ["https://leetcode.com/problems/"]  # base-URLs for the allowed domains for the spider to crawl
    start_urls = ["https://leetcode.com/problemset/all/?page=1"]  # URLs to start crawling from

    def parse(self, response):
        questions = Selector(response).xpath('//*[@id="__next"]/div/div/div[1]/'
                                             'div[1]/div[5]/div[2]/div/div/div[2]/div[2]/'
                                             'div[2]/div/div/div/a/@href').extract()
        # <a href= "/problems/two-sum" //*[@id="__next"]/div/div/div[1]/div[1]/div[5]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div
        # return questions
        # for q in questions:
            # print(q)
        yield Request(questions)
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





if __name__ == "main":
    s = QuestionsSpider()
    response = HtmlResponse(url="https://leetcode.com/problemset/all/?page=1", encoding='utf8')
    print(response)
    s.parse(response)

