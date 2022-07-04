#list中的list__二維清單

#確認檔案是否在資料夾內
import os #匯入作業系統模組

track = []
if os.path.isfile('track_spending.csv'): #檢查檔案是否存在,是的話就執行if的內容,開始讀取檔案
	print('yes, file is there')
	#讀取檔案 : 叫系統去讀取track_spending.csv檔案,然後把它寫入到track的列表中
	with open('track_spending.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line: 
			continue  #當遇到資料為'商品,價格'時,跳到下一回,不繼續執行。continue可避免抓到不要的資料
		name, price = line.strip().split(',') #刪除前後多於空格及換行後,用逗號將資料分開,已知資料會分為2塊,則直接定義給name及price
		track.append([name, price])
	print(track)
else:
	print('找不到檔案')

#讓使用者輸入
while True:
	product = input('請輸入商品名稱 : ')
	if product == 'q':
		break
	price = int(input('請輸入商品價格 : '))
	track.append([product, price])
print(track)

#取二維清單中的值
print(track[0][1])
#也可用for將值取出,印出所有購買紀錄
for p in track:
	print(p[0], '的價格為', p[1])

#寫入檔案
with open('track_spending.csv', 'w', encoding='utf-8') as t:
	t.write('商品,價格\n')
	for p in track:
		t.write(p[0] + ',' + str(p[1]) + '\n')