import requests
from bs4 import BeautifulSoup

while True:
    url = 'https://algospot.com/judge/problem/read/'
    keyword = input('문제를 입력하세요: (종료는 x)')
    if keyword == 'x':
        break
    keyword = keyword.upper()
    url += keyword
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        resultArr = []
        config = ['statement', 'input', 'output', 'sample_input', 'sample_output']
        for i in config:
            problem = soup.select_one('#main_section > article.full-block.clearfix > div > section.problem_' + i)
            problem = problem.text
            problem = problem.replace('. ', '.\n').replace('\r\n','\n')
            resultArr.append(problem.strip())

        result = ('\n\n').join(resultArr)
        result ='// '+url+ '\n\n/*'+result+'\n*/'

        f = open(keyword+'.cpp','w', encoding='utf8')
        f.write(result)
        f.close()
        print('완료')
    else:
        print(response.status_code)