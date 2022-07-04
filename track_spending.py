#list中的list__二維清單

track = []
while True:
	product = input('請輸入商品名稱 : ')
	if product == 'q':
		break
	price = input('請輸入商品價格 : ')
	track.append([product, price])
print(track)

#取二維清單中的值
print(track[0][1])
#也可用for將值取出
for p in track:
	print(p[0], '的價格為', p[1])
