class Clothes:
    def __init__(self, brand, gender, itemName, hashtag, imgLink, price, productLink):
        self.brand = brand
        self.gender = gender
        self.item_name = itemName
        self.hashtag = hashtag
        self.img_link = imgLink
        self.price = price
        self.pd_link = productLink


with open(file='C:\\Users\\Sylvia Vanros\\Desktop\\first_version.csv', mode='r', encoding='utf-8') as my_file:
    data = []
    for line in my_file.readlines():
        line = line.strip().split(',')
        data.append(line)
    print(data)

gender = input('1. 請優先勾選您的性別: ')
want_to_buy = input('2. 您想購買什麼(類別): '), input('您想購買什麼(款式): ')
price = input('3. 您偏好的價格區間: ')
hashtag = input('4. 您喜歡的風格: ')


def cat_temp_list(wtb, fd):
    lst = []
    for i in fd:
        tp = Clothes(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        tp = tp.hashtag.split(',')
        if tp[1] == wtb:
            lst.append(i)
    return lst


def price_temp_list(p, cat):
    lst = []
    for i in cat:
        tp = Clothes(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        if p == '價格不拘':
            return cat
        elif p:
            pass
        elif p:
            pass


if gender == '女性':
    female_data = []
    for item in data:
        temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        if temp.gender == 'women':
            female_data.append(item)

    cat_temp_list(want_to_buy, female_data)

    if price:
        pass

if gender == '男性':
    male_data = []
    for item in data:
        temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
        if temp.gender == 'men':
            male_data.append(item)

    cat_temp_list(want_to_buy, male_data)

    if price:
        pass


# if gender == '女性':
#     female_data = []
#     for item in data:
#         temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#         if temp.gender == 'women':
#             female_data.append(item)
#
#     if want_to_buy == '休閒外套':
#         casual_coat = []
#         for item in female_data:
#             temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#             temp = temp.hashtag.split(',')
#             if temp[1] == '休閒外套':
#                 casual_coat.append(item)
#
#     elif want_to_buy == '短褲':
#         short_pants = []
#         for item in female_data:
#             temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#             temp = temp.hashtag.split(',')
#             if temp[1] == '短褲':
#                 short_pants.append(item)
#
#     elif want_to_buy == '針織衫/毛衣':
#         hosiery_sweater = []
#         for item in female_data:
#             temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#             temp = temp.hashtag.split(',')
#             if temp[1] == '針織衫/毛衣':
#                 hosiery_sweater.append(item)
#
# if gender == '男性':
#     male_data = []
#     for item in data:
#         temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#         if temp.gender == 'men':
#             male_data.append(item)
#
#     if want_to_buy == '休閒外套':
#         casual_coat = []
#         for item in male_data:
#             temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#             temp = temp.hashtag.split(',')
#             if temp[1] == '休閒外套':
#                 casual_coat.append(item)
#
#     elif want_to_buy == '短褲':
#         short_pants = []
#         for item in male_data:
#             temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#             temp = temp.hashtag.split(',')
#             if temp[1] == '短褲':
#                 short_pants.append(item)
#
#     elif want_to_buy == '針織衫/毛衣':
#         hosiery_sweater = []
#         for item in male_data:
#             temp = Clothes(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
#             temp = temp.hashtag.split(',')
#             if temp[1] == '針織衫/毛衣':
#                 hosiery_sweater.append(item)