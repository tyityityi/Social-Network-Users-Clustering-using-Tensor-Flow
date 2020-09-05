import csv
import requests
from PIL import Image


def getImage(path, min=0, max=0):
    with open(path + '/wuser.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        if min > 0:
            for _ in range(min):
                next(f_csv)
        i = min
        # x = sum(1 for row in f_csv)
        # print(x)
        id = []
        imgUrl = {}
        if min < 0:
            return
        for row in f_csv:
            if i > max:
                return id, imgUrl
            id.append(row[0])
            imgUrl[i] = row[2]
            ir = requests.get(row[2])
            url = ir.url
            lex = url.split('/')[-1].find('.')
            s = url.split('/')[-1][lex:]

            if ir.status_code == 200:
                open(path + '/img/' + str(i) + s, 'wb').write(ir.content)
            x = Image.open(path + '/img/' + str(i) + s)
            x.convert('RGB').save(path + '/img/' + str(i) + '.jpg', 'JPEG')
            i += 1
            # f = open('C:\\Users\\LAI\\PycharmProjects\\Data mining\\wuser.csv', encoding='utf-8')
            #
            # f_csv = csv.reader(f)
            # print(next(f_csv))
