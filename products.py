# 記帳程式

products = []

# 讀取檔案
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line: 
			continue # 繼續 #不執行迴圈跳到下一個迴圈
		name, price = line.strip().split(',') # 先把\n去掉，再遇到逗點切一刀
		products.append([name, price])
# print(products)


# 印出歷史紀錄
print('目前記帳紀錄:')
for p in products:
	print(p[0], '的價格是', p[1])
print('-' * 40)


#提醒
print('提醒: 輸入結束請輸入 q')
print('-' * 40)


# 讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)

	products.append([name, price])
print(products)


# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])


# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #沒有會創建檔案, 有的話會覆蓋
	f.write('商品,價格\n') # 需指定編碼(encoding)才不會便亂碼 # 用excel要用utf-8打開
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 字串字串才能合併
