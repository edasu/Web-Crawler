import scrapy

class PostsSpider(scrapy.Spider):
    name = 'blog'

    start_urls = [
    "web side url"
    ]

    # def parse(self, response):
    #     page = response.url
    #     filename = 'blog.html'
    #     with open(filename, 'wb') as f:
    #         f.write(reponse.body)

    def parse(self, response):
        for post in response.css('div.posts'): #loop trough all the posts
            yield {
                'title': post.css('.posts h2 a::text')[0].get(),
                'date': post.css('.posts a::text')[1].get(),
                'author': post.css('.posts a::text')[2].get()
            } #dictionarie
        next_page = response.css('a.next-posts-link::attr(href)').get() #will give actual link to next page
        if next_page is not None: #is there a next page?
            next_page = response.urljoin(next_page) #scriping next page
            yield scrapy.Request(next_page, callback=self.parse)
