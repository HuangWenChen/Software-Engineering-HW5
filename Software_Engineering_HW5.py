# -*- coding: utf-8 -*-

all_time ={1:"平日中午",2:"平日晚上",3:"假日中午",4:"假日晚上"}
cost = ((268, 120),(368, 150))


def set_mealtime_people():
	mealtime = input("請輸入進餐時間(1 平日中午, 2 平日晚上, 3 假日中午,4 假日晚上) :")
	while (not mealtime.isdigit() or int(mealtime) not in all_time.keys()):
		mealtime = input("輸入錯誤,請在輸入一次:")
	adult = input("請輸入大人人數：") 
	while (not adult.isdigit()):
		adult = input("輸入錯誤,請在輸入一次:")
	child = input("請輸入小孩人數：") 
	while (not child.isdigit()):
		child = input("輸入錯誤,請在輸入一次:")
	return int(mealtime),int(adult),int(child)


def promotions(adult ,child):
	if adult + child >= 3:
		for i in range((adult + child)//3):
			if child > 0:
				child = child - 1
			else:
				adult = adult - 1
	return adult ,child


def bill(adult,child,mealtime):
	count = adult + child
	pro_adults ,pro_childs = promotions(adult ,child)
	price = 0 if mealtime==1 else 1
	price_fountion = lambda x: x[0] * x[1]
	total = sum(map(price_fountion, zip(cost[price], [pro_adults, pro_childs])))
	total = total * 1.1
	total = total * 0.95 if count >= 10 else total
	print("="*20)
	print("進餐時間：%s \n大人 %d - %d 位 * %d \n小孩 %d - %d 位 * %d\n\t*10%%服務費\n總金額：%d"
		%(all_time[mealtime],adult,adult-pro_adults,cost[price][0],child,child-pro_childs,cost[price][1],total))
	if count >= 3:
		print("\t*促銷(三人同行一人免費)")
	if count >= 10:
		print("\t*促銷(10人以上同行 95折)")


def main():
	mealtime,adult,child = set_mealtime_people()
	bill(adult,child,mealtime)


if __name__ == "__main__":
	main()
