# 記帳程式

products = []

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)

	products.append([name, price])

print(products)

for p in products:
	print(p[0], '的價格是', p[1])


# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #沒有會創建檔案, 有的話會覆蓋
	f.write('商品,價格\n') # 需指定編碼(encoding)才不會便亂碼 # 用excel要用utf-8打開
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 字串字串才能合併
