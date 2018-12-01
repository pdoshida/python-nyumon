import requests
from bs4 import BeautifulSoup

def main():

    # 江古田おすすめランチ
    url = 'https://retty.me/area/PRE13/ARE26/SUB2602/STAN5343/PUR1/'

    # requests で参加者一覧の情報と取得する
    response = requests.get(url)

    # response から HTML 部分(content) を取得
    content = response.content

    # BeautifulSoup に content を渡して解析の準備をする
    soup = BeautifulSoup(content, 'html.parser')

    # <h3 class="restaurant__name">  に該当するものを取り出す
    # <p class="restaurant__voice">  に該当するものを取り出す
    rest_n = soup.find_all('h3', class_='restaurant__name')
    rest_v = soup.find_all('p', class_='restaurant__voice')
#    print(rest_n)
#    print()
#    print(rest_v)
#    print()

    new_rset_n = []
    for nname in rest_n:
        #print(name.get_text())
        new_rset_n.append(nname.get_text())
    
    new_rset_v = []
    for vname in rest_v:
        #print(vname.get_text())
        new_rset_v.append(vname.get_text())

    for n, v in zip(new_rset_n, new_rset_v):
        print('{}:  {}'.format(n, v))

if __name__ == '__main__':
    main()

