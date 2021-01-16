#!/usr/bin/python
# -*- coding: UTF-8 -*
import pymysql
import random
import math
import time
import datetime as go
from datetime import datetime
db=pymysql.connect("localhost","root","2325120123","experiment")
T_time=0
New_time=0
date=''
last_list=[0,0,0,0,0]
this_list=[0,0,0,0,0]
def main():
	print("已連上資料庫，模擬交易開始")

	#迴圈設定為2021.1.1~2021.4.30(共計120天)
	#每天預設有100筆交易行為(共計11999筆交易紀錄)
	for i in range (1,1200):
		#訂出本日的日期 120.9
		global date
		today=math.floor(i/10)+1
		if(today>=1 and today<=31):
			date='2021-01-'+str(today)
		elif(today>=32 and today<=59):
			date='2021-02-'+str(today-31)
		elif(today>=60 and today<=90):
			date='2021-03-'+str(today-59)
		else:
			date='2021-04-'+str(today-90)

		#每月的1/7/14/28進行Promotions_Record推薦
		if((date=='2021-01-01' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-01-07' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-01-14' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-01-21' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-01-28' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-02-07' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-02-14' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-02-21' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-02-28' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-03-07' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-03-14' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-03-21' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-03-28' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-04-07' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-04-14' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1))  or (date=='2021-04-21' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)) or (date=='2021-04-28' and (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1))):
			global this_list
			global last_list
			if(date=='2021-01-01'):
				for dr in range (2,7):
					sql_IQ="select sum(Item_Quantity*cost_Price) from Inventory_Record JOIN Item_Record ON Item_Record.Item_ID=Inventory_Record.Item_ID where Store_ID="+str(dr)
					IQ=SQL_Query(sql_IQ)[0][0]
					this_list.append(IQ)
			else:
				last_list[0]=this_list[0]
				last_list[1]=this_list[1]
				last_list[2]=this_list[2]
				last_list[3]=this_list[3]
				last_list[4]=this_list[4]
				this_list=[]
				for dr in range (2,7):
					sql_IQ="select sum(Item_Quantity*cost_Price) from Inventory_Record JOIN Item_Record ON Item_Record.Item_ID=Inventory_Record.Item_ID where Store_ID="+str(dr)
					IQ=SQL_Query(sql_IQ)[0][0]
					this_list.append(IQ)

				for ooo in range(1,6):
					av_Item_Quantity=(last_list[ooo-1]+this_list[ooo-1])/2
					turnover=(70000/av_Item_Quantity)
					#找0.3到0.35
					if(turnover<0.35):
						sql_StoreName="select Store_Name from Inventory_Record where Store_ID="+str(ooo+1)
						StoreName=SQL_Query(sql_StoreName)[0][0]
						text=str(StoreName)+"的周轉率不理想，需要規劃促銷活動"

						cursor=db.cursor()
						sqlStuff = "INSERT INTO Promotions_Record (Recom_text,Recom_Date) VALUES (%s,%s)"
						records = [(text,date),]
						cursor.executemany(sqlStuff, records)
						db.commit()

			
		#隨機選出使用者
		#新使用者的id與名稱
		sql_users_num="""
			select count(User_ID) from user_record;
		"""	
		users_num=SQL_Query(sql_users_num)[0][0]
		Random_users_num=random.randint(1,users_num)

		sql_firstname_num="""
			select count(FirstName_ID) from FirstName_DB;
		"""	
		firstnam_num=SQL_Query(sql_firstname_num)[0][0]
		Random_firstnam_num=random.randint(1,firstnam_num)

		sql_firstname="select FirstName from FirstName_DB where FirstName_ID="+str(Random_firstnam_num)+";"
		firstname=SQL_Query(sql_firstname)[0][0]

		sql_lastname_num="""
			select count(LastName_ID) from LastName_DB;
		"""	
		lastname_num=SQL_Query(sql_lastname_num)[0][0]
		Random_lastname_num=random.randint(1,lastname_num)

		sql_lastname="select LastName from LastName_DB where LastName_ID="+str(Random_lastname_num)+";"
		lastname=SQL_Query(sql_lastname)[0][0]

		#隨機事件發生
		event1_happen_num=random.randint(1,11)
		#至少一個新會員
		if(event1_happen_num%10==1 or (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1)):
			#計算創辦會員次數
			global New_time
			New_time=New_time+1
			#開始創辦新會員
			cursor=db.cursor()
			sqlStuff = "INSERT INTO User_Record (User_ID,User_Name,User_LTV,User_Join) VALUES (%s,%s,%s,%s)"
			records = [(users_num+1,str(firstname)+" "+str(lastname),500.0,date),]
			cursor.executemany(sqlStuff, records)
			db.commit()
		else:
			event2_happen_num=random.randint(1,6)
			Random_store=random.randint(2,6)
			for n in range (1,event2_happen_num):
				#產生購買行為
				sql_Consumption_num="""
					select count(Consumption_ID) from Consumption_Record;
				"""	
				Consumption_num=SQL_Query(sql_Consumption_num)[0][0]
				global T_time
				T_time=T_time+1
				#SQL建立虛擬交易紀錄
				cursor=db.cursor()
				sqlStuff = "INSERT INTO Consumption_Record (Consumption_ID,User_ID,Item_ID,Store_ID,Consumption_Date,earn_money) VALUES (%s,%s,%s,%s,%s,%s)"
				Random_item=random.randint(1,25)
				sql_Item_Price="select Item_Price from item_record where Item_ID="+str(Random_item)+";"
				Item_Price=SQL_Query(sql_Item_Price)[0][0]
				records = [(Consumption_num+1,Random_users_num,Random_item,Random_store,date,Item_Price),]
				cursor.executemany(sqlStuff, records)
				db.commit()
				#SQL交易紀錄引響貨品數量
				cursor=db.cursor()
				cursor.execute("UPDATE Inventory_Record SET Item_Quantity=Item_Quantity-1 where Store_ID="+str(Random_store)+" AND Item_ID="+str(Random_item)+";")
				db.commit()

			#交易結束後填寫問券
			sql_Questionnaire_num="""
				select count(Q_id) from Questionnaire_Record;
			"""	
			Questionnaire_num=SQL_Query(sql_Questionnaire_num)[0][0]

			event3_happen_num=random.randint(1,6)
			if(event3_happen_num==1 or event3_happen_num==2 or event3_happen_num==3):
				Random_Q1=random.randint(1,7)
				Random_Q2=random.randint(1,7)
				Random_Q3=random.randint(1,7)
				Random_Q4=random.randint(1,7)
				Random_Q5=random.randint(1,7)
				Random_Q6=random.randint(1,7)
			else:
				Random_Q1=7
				Random_Q2=7
				Random_Q3=7
				Random_Q4=7
				Random_Q5=7
				Random_Q6=7				
			cursor=db.cursor()
			sqlStuff = "INSERT INTO Questionnaire_Record (Q_id,User_id,Q1,Q2,Q3,Q4,Q5,Q6,statistics_DATE,multiple) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			records = [(Questionnaire_num+1,Random_users_num,Random_Q1,Random_Q2,Random_Q3,Random_Q4,Random_Q5,Random_Q6,date,0),]
			cursor.executemany(sqlStuff, records)
			db.commit()

		#進行每日結算
		
		if (math.floor(i/10)+1)!=(math.floor((i+1)/10)+1):
			for r in range (1,7):
				for z in range(1,25):
					
					sql_Inventory_num="select Item_Quantity from Inventory_Record where Store_ID="+str(r)+" and Item_ID="+str(z)+";"
					Inventory_num=SQL_Query(sql_Inventory_num)[0][0]

					if(r==1):
						#判斷今日到貨的商品
						sql_book_or_not="select count(*) from Order_Record where Arrive_Date='"+str(date)+"' and Item_ID="+str(z)+" and Order_ID=1"
						book_or_not=SQL_Query(sql_book_or_not)[0][0]

						if(book_or_not==1):
							sql_Order_Quantity="select Order_Quantity from Order_Record where Arrive_Date='"+str(date)+"' and Item_ID="+str(z)+" and Order_ID=1;"
							Order_Quantity=SQL_Query(sql_Order_Quantity)[0][0]

							cursor=db.cursor()
							cursor.execute("UPDATE Inventory_Record SET Item_Quantity=Item_Quantity+"+str(Order_Quantity)+" WHERE Store_ID=1 and Item_ID="+str(z)+";")
							db.commit()
						
						#3天內調過的貨不會再調
						yesterday1=datetime.strptime(date, "%Y-%m-%d")-go.timedelta(days=1)
						yesterday1=str(yesterday1).split(' ')[0]
						yesterday2=datetime.strptime(date, "%Y-%m-%d")-go.timedelta(days=2)
						yesterday2=str(yesterday2).split(' ')[0]
						yesterday3=datetime.strptime(date, "%Y-%m-%d")-go.timedelta(days=3)
						yesterday3=str(yesterday3).split(' ')[0]
						sql_TF123_num="select count(*) from Order_Record where Item_ID="+str(z)+" and Order_ID="+str(r)+" and (Order_Date='"+str(yesterday1)+"' or Order_Date='"+str(yesterday2)+"' or Order_Date='"+str(yesterday3)+"')"
						TF123_num=SQL_Query(sql_TF123_num)[0][0]

						#判斷要不要從海外訂貨
						sql_reorder_point="select Reorder_Quantity from Reorder_Record where Seperate_ID=1 and Item_ID="+str(z)+";"
						reorder_point=SQL_Query(sql_reorder_point)[0][0]
						sql_EOQ="select EOQ from Reorder_Record where Seperate_ID=1 and Item_ID="+str(z)+";"
						EOQ=SQL_Query(sql_EOQ)[0][0]

						if(Inventory_num<=reorder_point  and TF123_num==0):
						#寫下訂購紀錄
							sqlStuff = "INSERT INTO Order_Record(Order_ID,Item_ID,Order_Quantity,Order_Date,Arrive_Date) VALUES (%s,%s,%s,%s,%s)"
							if(reorder_point-Inventory_num<EOQ):
								Order_Quantity=EOQ
							else:
								Order_Quantity=reorder_point-Inventory_num
							Arrive_Date=datetime.strptime(date, "%Y-%m-%d")+go.timedelta(days = 3)
							Arrive_Date=str(Arrive_Date).split(' ')[0]
							records = [(1,z,Order_Quantity,date,Arrive_Date),]
							cursor.executemany(sqlStuff, records)
							db.commit()
					else:
						#判斷今日到貨的商品
						sql_book_or_not="select count(*) from Trans_Record where Arrive_Date='"+str(date)+"' and Item_ID='"+str(z)+"' and Transfer_ID="+str(r)+";"
						book_or_not=SQL_Query(sql_book_or_not)[0][0]

						if(book_or_not==1):
							sql_Trans_Quantity="select Trans_Quantity from Trans_Record where Arrive_Date='"+str(date)+"' and Item_ID="+str(z)+" and Transfer_ID="+str(r)+";"
							Trans_Quantity=SQL_Query(sql_Trans_Quantity)[0][0]

							sql_Transferred_ID="select Transferred_ID from Trans_Record where Arrive_Date='"+str(date)+"' and Item_ID="+str(z)+" and Transfer_ID="+str(r)+";"
							Transferred_ID=SQL_Query(sql_Transferred_ID)[0][0]


							cursor=db.cursor()
							cursor.execute("UPDATE Inventory_Record SET Item_Quantity=Item_Quantity+"+str(Trans_Quantity)+" WHERE Store_ID="+str(r)+" and Item_ID="+str(z)+";")
							db.commit()

							cursor=db.cursor()
							cursor.execute("UPDATE Inventory_Record SET Item_Quantity=Item_Quantity-"+str(Trans_Quantity)+" WHERE Store_ID="+str(Transferred_ID)+" and Item_ID="+str(z)+";")
							db.commit()

						

						#昨天調過的貨不會再調
						yesterday1=datetime.strptime(date, "%Y-%m-%d")-go.timedelta(days=1)
						yesterday1=str(yesterday1).split(' ')[0]
						sql_TF1_num="select count(*) from Trans_Record where Trans_Date='"+str(yesterday1)+"' and Item_ID="+str(z)+" and Transfer_ID="+str(r)
						TF1_num=SQL_Query(sql_TF1_num)[0][0]
						

						#判斷要不要在國內調貨
						sql_reorder_point="select Reorder_Quantity from Reorder_Record where Seperate_ID=2 and Item_ID="+str(z)+";"
						reorder_point=SQL_Query(sql_reorder_point)[0][0]
						sql_EOQ="select EOQ from Reorder_Record where Seperate_ID=2 and Item_ID="+str(z)+";"
						EOQ=SQL_Query(sql_EOQ)[0][0]

						if(Inventory_num<=reorder_point and TF1_num==0):
						#寫下調貨紀錄
							#判斷最充裕的店
							sql_Inventory_judgment="select Item_Quantity from Inventory_Record where Store_ID=1 and Item_ID="+str(z)+";"
							Inventory_judgment=SQL_Query(sql_Inventory_judgment)[0][0]
							sql_reorder_judgment="select Reorder_Quantity from Reorder_Record where Seperate_ID=1 and Item_ID="+str(z)+";"
							reorder_judgment=SQL_Query(sql_reorder_judgment)[0][0]
							if(Inventory_judgment>60):
								chosen_Store=1
							else:
								chosen_Store=random.randint(1,7)

							if(chosen_Store==r):
								chosen_Store=1

							if(reorder_point-Inventory_num<EOQ):
								Trans_Quantity=EOQ
							else:
								Trans_Quantity=reorder_point-Inventory_num

							Arrive_Date=datetime.strptime(date, "%Y-%m-%d")+go.timedelta(days =1)
							Arrive_Date=str(Arrive_Date).split(' ')[0]
							cursor=db.cursor()
							sqlStuff = "INSERT INTO Trans_Record(Transfer_ID,Transferred_ID,Item_ID,Trans_Quantity,Trans_Date,Arrive_Date) VALUES (%s,%s,%s,%s,%s,%s)"
							records = [(r,chosen_Store,z,Trans_Quantity,date,Arrive_Date),]
							cursor.executemany(sqlStuff, records)
							db.commit()

		#進行每月結算
		if(i==309 or i==589 or i==899 or i==1199):
			print("現在開始"+str(i)+"結算")
			#推薦顧客偏好商品
			for m in range (1,users_num):
				sql_Numberof_Maxconsumption="select Item_ID from Consumption_Record join User_Record ON User_Record.User_ID=Consumption_Record.User_ID WHERE User_Record.User_ID="+str(m)+" GROUP BY Item_ID ORDER BY count(*) DESC LIMIT 1;"
				Recommendation_Text=""
				try:
					Numberof_Maxconsumption=SQL_Query(sql_Numberof_Maxconsumption)[0][0]
					if(Numberof_Maxconsumption>=1 and Numberof_Maxconsumption<=5):
						Recommendation_Text="外套7折優惠券"
					elif(Numberof_Maxconsumption>=6 and Numberof_Maxconsumption<=10):
						Recommendation_Text="上衣7折優惠券"
					elif(Numberof_Maxconsumption>=11 and Numberof_Maxconsumption<=15):
						Recommendation_Text="褲子&裙子7折優惠券"
					elif(Numberof_Maxconsumption>=16 and Numberof_Maxconsumption<=20):
						Recommendation_Text="配件7折優惠券"
					else:
						Recommendation_Text="內衣7折優惠券"
				except IndexError:
					Recommendation_Text="全館9折優惠券"
				
				sql_username="select User_Name from User_Record WHERE User_ID="+str(m)+";"
				username=SQL_Query(sql_username)[0][0]

				sqlStuff = "INSERT INTO Customized_Recommendation (User_ID,User_Name,Recommendation_Content,Customized_Time) VALUES (%s,%s,%s,%s)"
				records = [(str(m),username,Recommendation_Text,date),]
				cursor.executemany(sqlStuff, records)
				db.commit()
			
			#按月更新再訂購點
			for xx in range (1,26):
				if(i==309):
					sql_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210101' and Consumption_Date<='20210131' group by Consumption_Date"
					consumption_num=SQL_Query(sql_consumption_num)[0][0]
					sql_max_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210101' and Consumption_Date<='20210131' group by Consumption_Date order by count(*) DESC limit 1"
					max_consumption_num=SQL_Query(sql_max_consumption_num)[0][0]
					New_ReOrder=(consumption_num/31)*1+(max_consumption_num-consumption_num)+2
					New_ReOrder=round(New_ReOrder)
				elif(i==589):
					sql_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210201' and Consumption_Date<='20210228' group by Consumption_Date"
					consumption_num=SQL_Query(sql_consumption_num)[0][0]
					sql_max_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210201' and Consumption_Date<='20210228' group by Consumption_Date order by count(*) DESC limit 1"
					max_consumption_num=SQL_Query(sql_max_consumption_num)[0][0]
					New_ReOrder=(consumption_num/28)*1+(max_consumption_num-consumption_num)+2
					New_ReOrder=round(New_ReOrder)
				elif(i==899):
					sql_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210301' and Consumption_Date<='20210331' group by Consumption_Date"
					consumption_num=SQL_Query(sql_consumption_num)[0][0]
					sql_max_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210301' and Consumption_Date<='20210331' group by Consumption_Date order by count(*) DESC limit 1"
					max_consumption_num=SQL_Query(sql_max_consumption_num)[0][0]
					New_ReOrder=(consumption_num/31)*1+(max_consumption_num-consumption_num)+2
					New_ReOrder=round(New_ReOrder)
				else:
					sql_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210401' and Consumption_Date<='20210430' group by Consumption_Date"
					consumption_num=SQL_Query(sql_consumption_num)[0][0]
					sql_max_consumption_num="select count(*) from consumption_record where Item_ID="+str(xx)+" and Consumption_Date>='20210401' and Consumption_Date<='20210430' group by Consumption_Date order by count(*) DESC limit 1"
					max_consumption_num=SQL_Query(sql_max_consumption_num)[0][0]
					New_ReOrder=(consumption_num/30)*1+(max_consumption_num-consumption_num)+2
					New_ReOrder=round(New_ReOrder)

				cursor=db.cursor()
				cursor.execute("UPDATE Reorder_Record SET Reorder_Quantity="+str(New_ReOrder)+" where Item_ID="+str(xx)+" and Seperate_ID=2")
				db.commit()


			#按月更新LTV
			"""
			sql_users_num="select count(User_ID) from user_record;"
			users_num=SQL_Query(sql_users_num)[0][0]

			for cc in range (1,users_num+1):
				if(i==309):
					sql_tfcc="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210101' and Consumption_Date<='20210131'"
					tfcc=SQL_Query(sql_tfcc)[0][0]
					if(tfcc>0):
						sql_money_sum="select sum(earn_money) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210101' and Consumption_Date<='20210131'"
						money_sum=SQL_Query(sql_money_sum)[0][0]
						sql_customer_buy_num="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210101' and Consumption_Date<='20210131'"
						customer_buy_num=SQL_Query(sql_customer_buy_num)[0][0]
						CV=money_sum/customer_buy_num
						LTV=4*CV
					else:
						LTV=500
				elif(i==589):
					sql_tfcc="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210201' and Consumption_Date<='20210228'"
					tfcc=SQL_Query(sql_tfcc)[0][0]
					if(tfcc>0):
						sql_money_sum="select sum(earn_money) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210201' and Consumption_Date<='20210228'"
						money_sum=SQL_Query(sql_money_sum)[0][0]
						sql_customer_buy_num="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210201' and Consumption_Date<='20210228'"
						customer_buy_num=SQL_Query(sql_customer_buy_num)[0][0]
						CV=money_sum/customer_buy_num
						LTV=4*CV
					else:
						LTV=500
				elif(i==899):
					sql_tfcc="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210301' and Consumption_Date<='20210331'"
					tfcc=SQL_Query(sql_tfcc)[0][0]
					if(tfcc>0):
						sql_money_sum="select sum(earn_money) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210301' and Consumption_Date<='20210331'"
						money_sum=SQL_Query(sql_money_sum)[0][0]
						sql_customer_buy_num="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210301' and Consumption_Date<='20210331'"
						customer_buy_num=SQL_Query(sql_customer_buy_num)[0][0]
						CV=money_sum/customer_buy_num
						LTV=4*CV
					else:
						LTV=500
				"""


		print("成功執行第"+str(i)+"次")		
			


	#正在進行最終決算
	print("正在進行最終決算")
	sql_users_num="""
		select count(User_ID) from user_record;
	"""	
	users_num=SQL_Query(sql_users_num)[0][0]
	for cc in range (1,users_num+1):
		sql_tfcc="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210101' and Consumption_Date<='20210430'"
		tfcc=SQL_Query(sql_tfcc)[0][0]
		if(tfcc>0):
			sql_money_sum="select sum(earn_money) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210101' and Consumption_Date<='20210430'"
			money_sum=SQL_Query(sql_money_sum)[0][0]
			sql_customer_buy_num="select count(*) from consumption_record where User_ID="+str(cc)+" and Consumption_Date>='20210101' and Consumption_Date<='20210430'"
			customer_buy_num=SQL_Query(sql_customer_buy_num)[0][0]
			CV=money_sum/customer_buy_num
			LTV=4*CV
		else:
			LTV=1000
		
		cursor=db.cursor()
		cursor.execute("UPDATE User_Record SET User_LTV="+str(LTV)+" where User_ID="+str(cc))
		db.commit()

	#問券加權判斷
	sql_Questionnaire_num="""
		select count(User_ID) from Questionnaire_Record;
	"""
	Questionnaire_num=SQL_Query(sql_Questionnaire_num)[0][0]
	for ee in range (1,Questionnaire_num+1):
		sql_QUser_id="select User_id from Questionnaire_Record where Q_id="+str(ee)
		QUser_id=SQL_Query(sql_QUser_id)[0][0]
		sql_QLTV="select User_LTV from User_Record where User_ID="+str(QUser_id)
		QLTV=SQL_Query(sql_QLTV)[0][0]
		QLTV=round(QLTV/1000)
		
		cursor=db.cursor()
		cursor.execute("UPDATE Questionnaire_Record SET multiple="+str(QLTV)+" where Q_id="+str(ee))
		db.commit()

	#問券決算
	sql_Q1_sum="""
		select sum(Q1*multiple) from Questionnaire_Record;
	"""
	Q1_sum=SQL_Query(sql_Q1_sum)[0][0]

	sql_Q2_sum="""
		select sum(Q2*multiple) from Questionnaire_Record;
	"""
	Q2_sum=SQL_Query(sql_Q2_sum)[0][0]

	sql_Q3_sum="""
		select sum(Q3*multiple) from Questionnaire_Record;
	"""
	Q3_sum=SQL_Query(sql_Q3_sum)[0][0]

	sql_Q4_sum="""
		select sum(Q4*multiple) from Questionnaire_Record;
	"""
	Q4_sum=SQL_Query(sql_Q4_sum)[0][0]

	sql_Q5_sum="""
		select sum(Q5*multiple) from Questionnaire_Record;
	"""
	Q5_sum=SQL_Query(sql_Q4_sum)[0][0]

	sql_Q6_sum="""
		select sum(Q6*multiple) from Questionnaire_Record;
	"""
	Q6_sum=SQL_Query(sql_Q6_sum)[0][0]

	sql_multiple_sum="""
		select sum(multiple) from Questionnaire_Record;
	"""
	multiple_sum=SQL_Query(sql_multiple_sum)[0][0]

	
	cursor=db.cursor()
	sqlStuff = "INSERT INTO Questionnaire_End (Q1,Q2,Q3,Q4,Q5,Q6) VALUES (%s,%s,%s,%s,%s,%s)"
	records = [(Q1_sum/multiple_sum,Q2_sum/multiple_sum,Q3_sum/multiple_sum,Q4_sum/multiple_sum,Q5_sum/multiple_sum,Q6_sum/multiple_sum),]
	cursor.executemany(sqlStuff, records)
	db.commit()
	
	#廣告判定
	for aa in range (1,6):
		sql_AD_Start_Date="select AD_Start_Date from AD_Record where AD_ID="+str(aa)
		AD_Start_Date=SQL_Query(sql_AD_Start_Date)[0][0]

		sql_AD_Finish_Date="select AD_Finish_Date from AD_Record where AD_ID="+str(aa)
		AD_Finish_Date=SQL_Query(sql_AD_Finish_Date)[0][0]

		sql_User_ID_join="select User_ID from User_Record where User_Join='"+str(AD_Start_Date)+"' limit 1"
		User_ID_join=SQL_Query(sql_User_ID_join)[0][0]

		sql_User_ID_finish="select User_ID from User_Record where User_Join='"+str(AD_Finish_Date)+"' limit 1"
		User_ID_finish=SQL_Query(sql_User_ID_finish)[0][0]

		intervalDay=AD_Finish_Date-AD_Start_Date
		intervalDay=intervalDay.days
		AD_pick_up_rate=(User_ID_finish-User_ID_join)/(intervalDay*5)

		cursor=db.cursor()
		cursor.execute("UPDATE AD_Record SET AD_pick_up_rate="+str(AD_pick_up_rate)+" where AD_ID="+str(aa))
		db.commit()

		sql_AD_Cost="select AD_Cost from AD_Record where AD_ID="+str(aa)
		AD_Cost=SQL_Query(sql_AD_Cost)[0][0]

		AD_AC=AD_Cost/(User_ID_finish-User_ID_join)
		cursor=db.cursor()
		cursor.execute("UPDATE AD_Record SET AD_AC="+str(AD_AC)+" where AD_ID="+str(aa))
		db.commit()

		AD_ROI=random.randint(30,60)
		AD_ROI=AD_ROI/10
		cursor=db.cursor()
		cursor.execute("UPDATE AD_Record SET AD_ROI="+str(AD_ROI)+" where AD_ID="+str(aa))
		db.commit()



#擷取SQL查詢結果
def SQL_Query(sql):
	cursor=db.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	return data