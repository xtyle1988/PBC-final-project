class Clothes:
    def __init__(self, brand, gender, itemName, hashtag, price, productLink, imgLink):
        self.brand = brand
        self.gender = gender
        self.item_name = itemName
        self.hashtag = hashtag
        self.price = price
        self.pd_link = productLink
        self.img_link = imgLink
#  品牌、性別、款式、風格、價格、連結、圖片

with open(file='C:\\Users\\Sylvia Vanros\\Desktop\\first_version.csv', mode='r', encoding='utf-8') as my_file:
    data = []
    for line in my_file.readlines():
        line = line.strip().split(',')
        data.append(line)
    data.pop(0)  # pop title line
    # print(data)


# create a gender data
def gen_temp_list(g, d):
    lst = []
    for i in d:
        tp = Clothes(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        tp = tp.gender
        if g == '女性':
            if tp == 'women':
                lst.append(i)
        else:
            if tp == 'men':
                lst.append(i)
    return lst


# create a category data
def cat_temp_list(wtb, d):  # 類別(want_to_buy, data)
    lst = []
    set_hashtag = set()
    for i in d:
        tp = Clothes(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        tp = tp.hashtag.split('|')  # 從hashtag找出類別
        if tp[1] == wtb:
            lst.append(i)
            for j in range(len(tp)):  # hashtag的聯集
                if j == 1:
                    continue
                else:
                    set_hashtag = set_hashtag|{tp[j]}
    return lst, set_hashtag  # 回傳datalist和hashtag_set


# create a price data
def price_temp_list(p, cat):
    lst = []
    for i in cat:
        tp = Clothes(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        tp = tp.price
        if p == '價格不拘':
            lst = cat
        elif p == '1000元以下':
            if int(tp) <= 1000:
                lst.append(i)
        elif p == '1000元~1799元':
            if 1000 < int(tp) < 1800:
                lst.append(i)
        elif p == '1800元以上':
            if int(tp) >= 1800:
                lst.append(i)
    return lst


def hashtag_temp_list(h, d):  # 風格(hashtag, data篩到最後一步的)
    lst = d
    for k in h:  # 跑每個選取風格
        key = k  # 此輪篩選風格
        lst2 = []
        print(k)
        for i in lst:  # 跑每個data
            tp = Clothes(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
            tp = tp.hashtag.split('|')
            print(tp)
            for j in range(len(tp)):
                if j == 1:
                    continue
                if tp[j] == key:
                    lst2.append(i)
                    break
        lst = lst2
        print(len(lst2))
    return lst2


# process input
gender = input('1. 請優先勾選您的性別: ')
want_to_buy = input('2. 您想購買什麼(款式): ')
price = input('3. 您偏好的價格區間: ')
hashtag = input('4. 您喜歡的風格: ')

gen_data = gen_temp_list(gender, data)
cat_data, set_hashtag = cat_temp_list(want_to_buy, gen_data)
price_data = price_temp_list(price, cat_data)
hashtag_data = hashtag_temp_list(hashtag, price_data)
# print(price_data)
# print(len(price_data))
