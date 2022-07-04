#list中的list__二維清單

track = []
while True:
	product = input('請輸入商品名稱 : ')
	if product == 'q':
		break
	price = int(input('請輸入商品價格 : '))
	track.append([product, price])
print(track)

#取二維清單中的值
print(track[0][1])
#也可用for將值取出
for p in track:
	print(p[0], '的價格為', p[1])

#寫入檔案
with open('track_spending.csv', 'w', encoding='utf-8') as t:
	t.write('商品,價格\n')
	for p in track:
		t.write(p[0] + ',' + str(p[1]) + '\n')