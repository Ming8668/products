# 記帳程式

import os # operating system



# 讀取檔案
def read_file(filename):
	products = []
	if os.path.isfile(filename): # 檢查檔案在不在
		print('找到檔案!')
		with open(filename, 'r', encoding='utf-8') as f:
			for line in f:
				if '商品,價格' in line:
					continue # 繼續 #不執行迴圈跳到下一個迴圈
				name, price = line.strip().split(',') # 先把\n去掉，再遇到逗點切一刀
				products.append([name, price])
		# print(products)

		# 印出歷史紀錄
		print('-' * 40)
		print('目前記帳紀錄:')
		for p in products:
			print(p[0], '的價格是', p[1])
		print('-' * 40)
	else:
		print('找不到檔案!')
		print('-' * 40)


	#提醒
	print('提醒: 輸入結束請輸入 q')
	print('-' * 40)

	return products


# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)

		products.append([name, price])
	print(products)
	return products


# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])


# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f: #沒有會創建檔案, 有的話會覆蓋
		f.write('商品,價格\n') # 需指定編碼(encoding)才不會便亂碼 # 用excel要用utf-8打開
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') # 字串字串才能合併



products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv', products)
