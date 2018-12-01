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
    participation_tables_n = soup.find_all('h3', class_='restaurant__name')
    participation_tables_v = soup.find_all('p', class_='restaurant__voice')
    print(participation_tables_n)
    print(participation_tables_v)
    print()

    # participation_tables を順番に見て、"講師・メンター枠"の情報を取り出す
#    for participation_table in participation_tables:
        # <table><thead><tr><th> に該当するタグの要素を取り出す (参加者枠の種類が記載されているので)
#        print(participation_table)

#        # 参加者枠を示す文字に "講師・メンター枠" が含まれるものを取り出す
#        if '講師・メンター枠' in participant_type:
#            mentors_table = participation_table
#            break
#
#    # 講師・メンター枠の HTML の中で class=display_name に該当するものを取り出す
#    # mentor_names は List
#    mentor_names = mentors_table.find_all(class_='display_name')
#
#    # 取り出した 講師・メンター枠の要素から純粋な名前だけを取り出す(前後の無駄な空行や改行などを取り除く)
#    for mentor_name in mentor_names:
#        print(mentor_name.get_text().strip())


if __name__ == '__main__':
    main()

