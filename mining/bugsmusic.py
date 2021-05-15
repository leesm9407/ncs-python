from bs4 import BeautifulSoup
from urllib.request import urlopen


class Bugsmusic:  # class는 대문자로 시작
    url = ''

    def scrap(self):
        url = urlopen(self.url)
        soup = BeautifulSoup(url, 'lxml')       # lxml : 파사?(인간이 인지할 수 있는 언어로 번역하는 번역기)
        cnt_artist = 0
        cnt_title = 0

        for link1 in soup.find_all(name="p", attrs=({"class": "artist"})):
            cnt_artist += 1
            print(str(cnt_artist) + "위")
            print("아티스트 : " + link1.find('a').text)

        print("---------------------------------------")

        for link2 in soup.find_all(name="p", attrs=({"class": "title"})):
            cnt_title += 1
            print(str(cnt_title) + "위")
            print("노래제목" + link2.text)

    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210508&charthour=12'
        bugs.scrap()


if __name__ == '__main__':
    Bugsmusic.main()
