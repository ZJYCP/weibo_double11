# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    source = scrapy.Field() #来源
    mblogid=scrapy.Field()  #微博id
    created_at=scrapy.Field()  #发布时间
    content=scrapy.Field()  #发布文字内容
    comment_count = scrapy.Field() #评论数量
    attitudes_count = scrapy.Field() #点赞数量
    reposts_count = scrapy.Field() #转发数量
    text_legth = scrapy.Field() # 内容长度

    username=scrapy.Field()  #用户名
    userGender=scrapy.Field()  #用户性别
    user_id = scrapy.Field() #用户id
    followers_count=scrapy.Field()  #粉丝数
    friends_count=scrapy.Field()  #关注数
    statuses_count=scrapy.Field()  #微博数
    verified_type =scrapy.Field() #微博认证类型
