from bs4 import BeautifulSoup
import requests
import pandas as pd 
import sqlite3

# for month in range(1,13):
#     if month in [1,3,5,7,8,10,12]:
#         days = 31
#     elif month in [4, 6, 9, 11]:
#         days = 30 
#     else:
#         days = 28

#         for day in range(1, days + 1):

#             month, day = str(month), str(day)

#             if len(month) == 1:
#                 month = f'0{month}'
#             if len(days) == 1:
#                 days = f'0{days}'

conn = sqlite3.connect('articles.db')
c = conn.cursor()

# c.execute('''CREATE TABLE hackernoon(date TEXT, authorLink TEXT, authorName TEXT, articleTitle TEXT, articleLink TEXT, articleLikes TEXT)''')
# c.execute('''DROP TABLE hackernoon''')

def hackernoon_articles():
    articles_data = []

    for year in range(2014,2015):
        for month in range(1,13):
            month = str(month)

            if len(month) == 1:
                month = f'0{month}'
        
            date = (f'{year} {month}')
            url = f'https://medium.com/hackernoon/archive/{year}/{month}'
            html_text = requests.get(url).text

            soup = BeautifulSoup(html_text, 'lxml')

            articles = soup.find_all('div', class_='streamItem streamItem--postPreview js-streamItem')

            for article in articles:

                every_article = []

                author_box = article.find('div', class_='postMetaInline u-floatLeft u-sm-maxWidthFullWidth')
                author_link = author_box.find('a')['href']
                author_name = author_box.find('a', class_='ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken').text

                article_title = article.find('h3').text if article.find('h3') else article.find('h2').text
                article_link = article.find('a', class_='button button--smaller button--chromeless u-baseColor--buttonNormal')['href']
                article_likes_exist = article.find('button', class_='button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton u-disablePointerEvents')
                if article_likes_exist:
                    article_likes = article_likes_exist.text
                else:
                   article_likes = '0'
            
                c.execute('''INSERT INTO hackernoon VALUES(?,?,?,?,?,?)''', (date, author_link, author_name, article_title, article_link, article_likes))



    

if __name__=="__main__":
    hackernoon_articles()
    conn.commit()
    print('complete')

    c.execute('''SELECT * FROM hackernoon''')
    results = c.fetchall()
    print(results)




# def find_articles(articles):
#     for article in articles:
#         article_date = article.find('time').text
#         # if 'May 14' in article_date:
#         article_title = article.find('h3').text
#         article_likes = article.find('button', class_='button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton u-disablePointerEvents').text
#         link_header = article.find('div', class_='postArticle-content')
#         article_link = link_header.a['href']
#         # with open(f'article.txt', 'w') as f:
#         print(article_title)
#         # print(article_date)
#         # print(article_likes)
#         # print(article_link)



# print('Enter the keywoards related to the articles you want to search for')
# keyword = input ('>')
# print(f'Searching for articles related to {keyword}')

# max_articles_searched = 100


# first_page = requests.get(f'https://medium.com/search?q={keyword}').text
# other_pages = requests.get(f'https://medium.com/search/posts?q={keyword}&count={max_articles_searched}&ignore=120ea540b567&ignore=68998a08e4f6&ignore=518db9a68a78&ignore=b467524ee747&ignore=30ddc5339b66&ignore=dd6e99039d5e&ignore=9230bff0df62&ignore=c62152f39420&ignore=7c8c8215ac6e&ignore=ddba3357eace').text

# soup = BeautifulSoup(first_page, 'lxml')
# soup2 = BeautifulSoup(other_pages, 'lxml')
# articles_main = soup.find_all('div', class_='u-paddingTop20 u-paddingBottom25 u-borderBottomLight js-block')
# articles_more = soup2.find_all('div', class_='u-paddingTop20 u-paddingBottom25 u-borderBottomLight js-block')

# if __name__=="__main__":
#     find_articles(articles_main)
#     find_articles(articles_more)


# for article in articles:
#     print(article.text)

# job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# print(job.find('h3', class_= 'joblist-comp-name').text.replace(' ',''))
# print(job)

# for job in jobs:
#     title = job.h3.text.replace(' ', '')
#     print(title)
# with open('home.html', 'r') as html_file:
#     content = html_file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     course_cards = soup.find_all('div', class_='card')
#     for course in course_cards:
#         name = course.h5.text
#         price = course.a.text.split()[-1]

#         print(name)
#         print(price)

