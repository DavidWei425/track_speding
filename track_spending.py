import os #匯入作業系統模組

def read_file(filename):#讀取檔案
	track = []
	with open(filename, 'r', encoding='utf-8') as f:#叫系統去讀取track_spending.csv檔案,然後把它寫入到track的列表中
		for line in f:
			if '商品,價格' in line: 
				continue  #當遇到資料為'商品,價格'時,跳到下一回,不繼續執行。continue可避免抓到不要的資料
			name, price = line.strip().split(',') #刪除前後多於空格及換行後,用逗號將資料分開,已知資料會分為2塊,則直接定義給name及price
			track.append([name, price])
	return track

def user_input(track):#讓使用者輸入
	while True:
		product = input('請輸入商品名稱 : ')
		if product == 'q':
			break
		price = int(input('請輸入商品價格 : '))
		track.append([product, price])
	return track

def print_file(track):
	print(track[0][1])
	#也可用for將值取出,印出所有購買紀錄
	for p in track:
		print(p[0], '的價格為', p[1])#取二維清單中的值

def write_file(filename, track):#寫入檔案
	with open(filename, 'w', encoding='utf-8') as t:
		t.write('商品,價格\n')
		for p in track:
			t.write(p[0] + ',' + str(p[1]) + '\n')
	return track

def main(filename):
	if os.path.isfile(filename): #檢查檔案是否存在,是的話就執行if的內容,開始讀取檔案
		print('yes, file is there')
		track = read_file(filename)
		print(track)
	else:
		print('找不到檔案')#讀取檔案#讀取檔案
	track = user_input(track)
	track = write_file(filename, track)
	print(track)

main('track_spending.csv')