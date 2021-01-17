#!/usr/bin/python
# -*- coding: UTF-8 -*
import pymysql
import random
db=pymysql.connect("localhost","root","2325120123","experiment")
def main():
	try:
		cursor=db.cursor()
		cursor.execute("DROP TABLE Item_Record")
		cursor.execute("DROP TABLE Inventory_Record")
		cursor.execute("DROP TABLE Questionnaire_Record")
		cursor.execute("DROP TABLE AD_Record")
		cursor.execute("DROP TABLE User_Record")
		cursor.execute("DROP TABLE Promotions_Record")
		cursor.execute("DROP TABLE Customized_Recommendation")
		cursor.execute("DROP TABLE Order_Record")
		cursor.execute("DROP TABLE Trans_Record")
		cursor.execute("DROP TABLE Consumption_Record")
		cursor.execute("DROP TABLE Reorder_Record")
		cursor.execute("DROP TABLE FirstName_DB")
		cursor.execute("DROP TABLE LastName_DB")
		cursor.execute("DROP TABLE Questionnaire_End")
		print("資料庫已回復預設值")
	except pymysql.err.OperationalError:
		print("尚未有資料表，不須重製，將自動進入創建環節")

	#範例
	#cursor=db.cursor()
	#cursor.execute("CREATE TABLE  ()")
	#sqlStuff = ""
	#records = []
	#cursor.executemany(sqlStuff, records)
	#db.commit()

	#品項資料表	
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Item_Record (Item_ID int(11),Item_Name varchar(255),Category_Name VARCHAR(255),Item_Price int(11),cost_Price int(11))")
	sqlStuff = "INSERT INTO Item_Record (Item_ID, Item_Name ,Category_Name ,Item_Price,cost_Price) VALUES (%s,%s,%s,%s,%s)"
	records = [
	(1,"寬鬆襯衫外套","外套",1000,700),
	(2,"經典款風衣外套","外套",1800,1100),
	(3,"無領外套NT","外套",1800,1200),
	(4,"撞色塊登山外套","外套",1500,1150),
	(5,"棒球外套","外套",1000,700),
	(6,"寬版拼接休閒上衣","上衣",800,500),
	(7,"雙面織紋高領上衣","上衣",600,300),
	(8,"休閒高領針織衫","上衣",600,400),
	(9,"雙面織紋高領上衣","上衣",600,300),
	(10,"中高領休閒上衣","上衣",600,450),
	(11,"刷毛附腰帶寬褲","下身",600,380),
	(12,"主廚褲","下身",600,440),
	(13,"男裝輕便九分褲","下身",800,680),
	(14,"燈芯絨工作九分褲","下身",600,400),
	(15,"男裝工作束口褲","下身",600,520),
	(16,"多色金屬圓圈耳環","配件",200,130),
	(17,"再生皮編織腰帶","配件",400,250),
	(18,"仿鱷魚皮腰帶","配件",400,330),
	(19,"托特包","配件",200,110),
	(20,"輕軟仿皮束口包","配件",800,600),
	(21,"珊瑚絨家居服組","內搭",600,400),
	(22,"保暖V領上衣","內搭",300,200),
	(23,"保暖寬領上衣","內搭",300,230),
	(24,"Extra極暖寬領上衣","內搭",400,310),
	(25,"保暖圓領上衣","內搭",400,200),]
	cursor.executemany(sqlStuff, records)
	db.commit()

	#存貨紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Inventory_Record (Store_ID int(11),Store_Name varchar(255),Item_ID int(11),Item_Quantity int(11))")
	sqlStuff = "INSERT INTO Inventory_Record (Store_ID,Store_Name, Item_ID ,Item_Quantity) VALUES (%s,%s,%s,%s)"
	records = [
	(1,"總倉庫",1,60),
	(1,"總倉庫",2,60),
	(1,"總倉庫",3,60),
	(1,"總倉庫",4,60),
	(1,"總倉庫",5,60),
	(1,"總倉庫",6,60),
	(1,"總倉庫",7,60),
	(1,"總倉庫",8,60),
	(1,"總倉庫",9,60),
	(1,"總倉庫",10,60),
	(1,"總倉庫",11,60),
	(1,"總倉庫",12,60),
	(1,"總倉庫",13,60),
	(1,"總倉庫",14,60),
	(1,"總倉庫",15,60),
	(1,"總倉庫",16,60),
	(1,"總倉庫",17,60),
	(1,"總倉庫",18,60),
	(1,"總倉庫",19,60),
	(1,"總倉庫",20,60),
	(1,"總倉庫",21,60),
	(1,"總倉庫",22,60),
	(1,"總倉庫",23,60),
	(1,"總倉庫",24,60),
	(1,"總倉庫",25,60),
	(2,"台北店",1,20),
	(2,"台北店",2,20),
	(2,"台北店",3,20),
	(2,"台北店",4,20),
	(2,"台北店",5,20),
	(2,"台北店",6,20),
	(2,"台北店",7,20),
	(2,"台北店",8,20),
	(2,"台北店",9,20),
	(2,"台北店",10,20),
	(2,"台北店",11,20),
	(2,"台北店",12,20),
	(2,"台北店",13,20),
	(2,"台北店",14,20),
	(2,"台北店",15,20),
	(2,"台北店",16,20),
	(2,"台北店",17,20),
	(2,"台北店",18,20),
	(2,"台北店",19,20),
	(2,"台北店",20,20),
	(2,"台北店",21,20),
	(2,"台北店",22,20),
	(2,"台北店",23,20),
	(2,"台北店",24,20),
	(2,"台北店",25,20),
	(3,"桃園店",1,20),
	(3,"桃園店",2,20),
	(3,"桃園店",3,20),
	(3,"桃園店",4,20),
	(3,"桃園店",5,20),
	(3,"桃園店",6,20),
	(3,"桃園店",7,20),
	(3,"桃園店",8,20),
	(3,"桃園店",9,20),
	(3,"桃園店",10,20),
	(3,"桃園店",11,20),
	(3,"桃園店",12,20),
	(3,"桃園店",13,20),
	(3,"桃園店",14,20),
	(3,"桃園店",15,20),
	(3,"桃園店",16,20),
	(3,"桃園店",17,20),
	(3,"桃園店",18,20),
	(3,"桃園店",19,20),
	(3,"桃園店",20,20),
	(3,"桃園店",21,20),
	(3,"桃園店",22,20),
	(3,"桃園店",23,20),
	(3,"桃園店",24,20),
	(3,"桃園店",25,20),
	(4,"台中店",1,20),
	(4,"台中店",2,20),
	(4,"台中店",3,20),
	(4,"台中店",4,20),
	(4,"台中店",5,20),
	(4,"台中店",6,20),
	(4,"台中店",7,20),
	(4,"台中店",8,20),
	(4,"台中店",9,20),
	(4,"台中店",10,20),
	(4,"台中店",11,20),
	(4,"台中店",12,20),
	(4,"台中店",13,20),
	(4,"台中店",14,20),
	(4,"台中店",15,20),
	(4,"台中店",16,20),
	(4,"台中店",17,20),
	(4,"台中店",18,20),
	(4,"台中店",19,20),
	(4,"台中店",20,20),
	(4,"台中店",21,20),
	(4,"台中店",22,20),
	(4,"台中店",23,20),
	(4,"台中店",24,20),
	(4,"台中店",25,20),
	(5,"台南店",1,20),
	(5,"台南店",2,20),
	(5,"台南店",3,20),
	(5,"台南店",4,20),
	(5,"台南店",5,20),
	(5,"台南店",6,20),
	(5,"台南店",7,20),
	(5,"台南店",8,20),
	(5,"台南店",9,20),
	(5,"台南店",10,20),
	(5,"台南店",11,20),
	(5,"台南店",12,20),
	(5,"台南店",13,20),
	(5,"台南店",14,20),
	(5,"台南店",15,20),
	(5,"台南店",16,20),
	(5,"台南店",17,20),
	(5,"台南店",18,20),
	(5,"台南店",19,20),
	(5,"台南店",20,20),
	(5,"台南店",21,20),
	(5,"台南店",22,20),
	(5,"台南店",23,20),
	(5,"台南店",24,20),
	(5,"台南店",25,20),
	(6,"高雄店",1,20),
	(6,"高雄店",2,20),
	(6,"高雄店",3,20),
	(6,"高雄店",4,20),
	(6,"高雄店",5,20),
	(6,"高雄店",6,20),
	(6,"高雄店",7,20),
	(6,"高雄店",8,20),
	(6,"高雄店",9,20),
	(6,"高雄店",10,20),
	(6,"高雄店",11,20),
	(6,"高雄店",12,20),
	(6,"高雄店",13,20),
	(6,"高雄店",14,20),
	(6,"高雄店",15,20),
	(6,"高雄店",16,20),
	(6,"高雄店",17,20),
	(6,"高雄店",18,20),
	(6,"高雄店",19,20),
	(6,"高雄店",20,20),
	(6,"高雄店",21,20),
	(6,"高雄店",22,20),
	(6,"高雄店",23,20),
	(6,"高雄店",24,20),
	(6,"高雄店",25,20),]
	cursor.executemany(sqlStuff, records)
	db.commit()

	#問券紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Questionnaire_Record (Q_id int(11), User_id int(11), Q1 int(11), Q2 int(11), Q3 int(11), Q4 int(11) , Q5 int(11), Q6 int(11),statistics_DATE DATE,multiple int(11))")
	db.commit()

	#問券結果
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Questionnaire_End (Q1 int(11), Q2 int(11), Q3 int(11), Q4 int(11) , Q5 int(11), Q6 int(11))")
	db.commit()

	#廣告紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE AD_Record (AD_ID int(11),AD_Start_Date DATE,AD_Finish_Date DATE,AD_Cost int(11),AD_pick_up_rate float(24),AD_AC float(24),AD_ROI float(24))")
	sqlStuff = "INSERT INTO AD_Record (AD_ID,AD_Start_Date,AD_Finish_Date,AD_Cost,AD_pick_up_rate,AD_AC,AD_ROI) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	records = [
	#剩下假設，但為了獲取顧客花得廣告前要算
	(1,'2021-01-02','2021-01-16',5000,0.0,0.0,0.0),
	(2,'2021-01-28','2021-2-28',7900,0.0,0.0,0.0),
	(3,'2021-02-08','2021-02-13',1500,0.0,0.0,0.0),
	(4,'2021-02-18','2021-03-18',9000,0.0,0.0,0.0),
	(5,'2021-04-10','2021-04-30',6000,0.0,0.0,0.0),]
	cursor.executemany(sqlStuff, records)
	db.commit()

	#促銷活動紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Promotions_Record (Recom_text varchar(255), Recom_Date DATE)")
	cursor.executemany(sqlStuff, records)
	db.commit()

	#客製化推薦紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Customized_Recommendation (User_ID int(11) ,User_Name varchar(255),Recommendation_Content varchar(255), Customized_Time DATE)")
	db.commit()

	#訂購紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Order_Record (Order_ID int(11), Item_ID int(11), Order_Quantity int(11),Order_Date DATE,Arrive_Date DATE)")
	db.commit()

	#調貨記錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Trans_Record (Transfer_ID int(11),Transferred_ID int(11),Item_ID int(11),Trans_Quantity int(11),Trans_Date DATE,Arrive_Date DATE)")
	db.commit()

	#消費紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Consumption_Record (Consumption_ID int(11),User_ID int(11),Item_ID int(11),Store_ID int(11),Consumption_Date DATE,earn_money int(11))")
	db.commit()


	#再訂購點紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE Reorder_Record (Seperate_ID int(11) , Item_ID int(11) , Reorder_Quantity float(24), EOQ int(11))")
	sqlStuff = "INSERT INTO Reorder_Record (Seperate_ID,Item_ID,Reorder_Quantity,EOQ) VALUES (%s,%s,%s,%s)"
	records = [
	#到貨天數*過往每天平均
	#EOQ(倉儲成本/成本)
	(1,1,40.0,40),
	(1,2,40.0,40),
	(1,3,40.0,40),
	(1,4,40.0,40),
	(1,5,40.0,40),
	(1,6,40.0,40),
	(1,7,40.0,40),
	(1,8,40.0,40),
	(1,9,40.0,40),
	(1,10,40.0,40),
	(1,11,40.0,40),
	(1,12,40.0,40),
	(1,13,40.0,40),
	(1,14,40.0,40),
	(1,15,40.0,40),
	(1,16,40.0,40),
	(1,17,40.0,40),
	(1,18,40.0,40),
	(1,19,40.0,40),
	(1,20,40.0,40),
	(1,21,40.0,40),
	(1,22,40.0,40),
	(1,23,40.0,40),
	(1,24,40.0,40),
	(1,25,40.0,40),
	(2,1,8.0,8),
	(2,2,8.0,8),
	(2,3,8.0,8),
	(2,4,8.0,8),
	(2,5,8.0,8),
	(2,6,8.0,8),
	(2,7,8.0,8),
	(2,8,8.0,8),
	(2,9,8.0,8),
	(2,10,8.0,8),
	(2,11,8.0,8),
	(2,12,8.0,8),
	(2,13,8.0,8),
	(2,14,8.0,8),
	(2,15,8.0,8),
	(2,16,8.0,8),
	(2,17,8.0,8),
	(2,18,8.0,8),
	(2,19,8.0,8),
	(2,20,8.0,8),
	(2,21,8.0,8),
	(2,22,8.0,8),
	(2,23,8.0,8),
	(2,24,8.0,8),
	(2,25,8.0,8),]
	cursor.executemany(sqlStuff, records)
	db.commit()

	cursor=db.cursor()
	cursor.execute("CREATE TABLE FirstName_DB (FirstName_ID int(11) , FirstName varchar(255))")
	sqlStuff = "INSERT INTO FirstName_DB (FirstName_ID,FirstName) VALUES (%s,%s)"
	records = [
	(1,"Aaron"),
	(2,"Abel"),
	(3,"Ace"),
	(4,"Adam"),
	(5,"Ahern"),
	(6,"Alan"),
	(7,"Albert"),
	(8,"Aldrich"),
	(9,"Alexander"),
	(10,"Alonso"),
	(11,"Alvin"),
	(12,"Amos"),
	(13,"Angelo"),
	(14,"Archibald"),
	(15,"August"),
	(16,"Bard"),
	(17,"Bartholomew"),
	(18,"Ben"),
	(19,"Benjamin"),
	(20,"Benson"),
	(21,"Bernie"),
	(22,"Bill"),
	(23,"Booth"),
	(24,"Borislav"),
	(25,"Brandon"),
	(26,"Bruce"),
	(27,"Byron"),
	(28,"Calvin"),
	(29,"Calvin"),
	(30,"Chad"),
	(31,"Chester"),
	(32,"Christopher"),
	(33,"Clarence"),
	(34,"Claude"),
	(35,"Cleveland"),
	(36,"Clyde"),
	(37,"Conrad"),
	(38,"Cornelius"),
	(39,"Cyril"),
	(40,"Dan"),
	(41,"Dante"),
	(42,"Darren"),
	(43,"Davis"),
	(44,"Delbert"),
	(45,"Derrick"),
	(46,"Deven"),
	(47,"Donald"),
	(48,"Donahue"),
	(49,"Duncan"),
	(50,"Earnest"),
	(51,"Edric"),
	(52,"Edgar"),
	(53,"Elijah"),
	(54,"Elmer"),
	(55,"Emmanuel"),
	(56,"Eugene"),
	(57,"Felix"),
	(58,"Fitzgerald"),
	(59,"Frank"),
	(60,"Franklin"),
	(61,"Gale"),
	(62,"Gary"),
	(63,"Geoff"),
	(64,"Giles"),
	(65,"Griffith"),
	(66,"Haley"),
	(67,"Harold"),
	(68,"Hayden"),
	(69,"Herbert"),
	(70,"Hugh"),
	(71,"Hugo"),
	(72,"Hunter"),
	(73,"Ingemar"),
	(74,"James"),
	(75,"Jason"),
	(76,"Jeffrey"),
	(77,"Jerry"),
	(78,"Jonathan"),
	(79,"Kennedy"),
	(80,"Kerwin"),
	(81,"Leopold"),
	(82,"Llywelyn"),
	(83,"Malcolm"),
	(84,"Marsh"),
	(85,"Maximilian"),
	(86,"Monty"),
	(87,"Owen"),
	(88,"Paddy"),
	(89,"Pete"),
	(90,"Quennel"),
	(91,"Radomil"),
	(92,"Randolph"),
	(93,"Regan"),
	(94,"Richard"),
	(95,"Roderick"),
	(96,"Ron"),
	(97,"Spencer"),
	(98,"Timothy"),
	(99,"Valentine"),
	(100,"Waldo"),
	(101,"Ada"),
	(102,"Afra"),
	(103,"Althea"),
	(104,"Alyssa"),
	(105,"Angela"),
	(106,"Ashley"),
	(107,"Ava"),
	(108,"Barbara"),
	(109,"Belinda"),
	(110,"Bess"),
	(111,"Bonnie"),
	(112,"Brianna"),
	(113,"Carol"),
	(114,"Carlin"),
	(115,"Cathy"),
	(116,"Charlotte"),
	(117,"Cheryl"),
	(118,"Clara"),
	(119,"Cynthia"),
	(120,"Dale"),
	(121,"Daphne"),
	(122,"Deborah"),
	(123,"Destiny"),
	(124,"Dolores"),
	(125,"Dorothy"),
	(126,"Eartha"),
	(127,"Eileen"),
	(128,"Ella"),
	(129,"Elvira"),
	(130,"Enid"),
	(131,"Eunice"),
	(132,"Evelyn"),
	(133,"Faithe"),
	(134,"Florence"),
	(135,"Frederica"),
	(136,"Gabrielle"),
	(137,"Genevieve"),
	(138,"Gloria"),
	(139,"Gustave"),
	(140,"Harriet"),
	(141,"Hedy"),
	(142,"Hulda"),
	(143,"Ingrid"),
	(144,"Ivy"),
	(145,"Jamie"),
	(146,"Janice"),
	(147,"Jenny"),
	(148,"Josephine"),
	(149,"Julia"),
	(150,"Katherine"),
	(151,"Kimberley"),
	(152,"Lara"),
	(153,"Lillian"),
	(154,"Lola"),
	(155,"Lydia"),
	(156,"Madeline"),
	(157,"Marguerite"),
	(158,"Martha"),
	(159,"Maxine"),
	(160,"Merry"),
	(161,"Miriam"),
	(162,"Nelly"),
	(163,"Novia"),
	(164,"Odelette"),
	(165,"Ophelia"),
	(166,"Patricia"),
	(167,"Penelope"),
	(168,"Phoenix"),
	(169,"Prudence"),
	(170,"Quintina"),
	(171,"Regina"),
	(172,"Rita"),
	(173,"Rose"),
	(174,"Roxanne"),
	(175,"Sally"),
	(176,"Sarah"),
	(177,"Tara"),
	(178,"Tina"),
	(179,"Una"),
	(180,"Valerie"),
	(181,"Victoria"),
	(182,"Wendy"),
	(183,"Xanthe"),
	(184,"Yedda"),
	(185,"Yetta"),
	(186,"Yuri"),
	(187,"Yvette"),
	(188,"Yvonne"),
	(189,"Zara"),
	(190,"Zenobia"),
	(191,"Zoe"),
	(192,"Zona"),
	(193,"Zanna"),
	(194,"Zora"),
	(195,"Selena"),
	(196,"Stacey"),
	(197,"Theresa"),
	(198,"Trista"),
	(199,"Penny"),
	(200,"Phyllis"),]
	cursor.executemany(sqlStuff, records)
	db.commit()

	cursor=db.cursor()
	cursor.execute("CREATE TABLE LastName_DB (LastName_ID int(11) , LastName varchar(255))")
	sqlStuff = "INSERT INTO LastName_DB (LastName_ID,LastName) VALUES (%s,%s)"
	records = [
	(1,"Smith"),
	(2,"Jones"),
	(3,"Taylor"),
	(4,"Williams"),
	(5,"Brown"),
	(6,"Davies"),
	(7,"Evans"),
	(8,"Wilson"),
	(9,"Thomas"),
	(10,"Roberts"),
	(11,"Johnson"),
	(12,"Lewis"),
	(13,"Walker"),
	(14,"Robinson"),
	(15,"Wood"),
	(16,"Thompson"),
	(17,"White"),
	(18,"Watson"),
	(19,"Jackson"),
	(20,"Wright"),
	(21,"Green"),
	(22,"Harris"),
	(23,"Cooper"),
	(24,"King"),
	(25,"Lee"),
	(26,"Martin"),
	(27,"Clarke"),
	(28,"James"),
	(29,"Morgan"),
	(30,"Hughes"),
	(31,"Edwards"),
	(32,"Hill"),
	(33,"Moore"),
	(34,"Clark"),
	(35,"Harrison"),
	(36,"Scott"),
	(37,"Young"),
	(38,"Morris"),
	(39,"Hall"),
	(40,"Ward"),
	(41,"Turner"),
	(42,"Carter"),
	(43,"Phillips"),
	(44,"Mitchell"),
	(45,"Patel"),
	(46,"Adams"),
	(47,"Campbellc"),
	(48,"Anderson"),
	(49,"Allen"),
	(50,"Cook"),
	]
	cursor.executemany(sqlStuff, records)
	db.commit()

	#會員紀錄
	cursor=db.cursor()
	cursor.execute("CREATE TABLE User_Record (User_ID int(11), User_Name varchar(255), User_LTV float(24), User_Join DATE)")
	sqlStuff = "INSERT INTO User_Record (User_ID,User_Name,User_LTV,User_Join) VALUES (%s,%s,%s,%s)"
	records = [
	(1,"吳泓澈",1000.0,'2021-01-01'),
	(2,"游勝凱",1000.0,'2021-01-01'),
	(3,"張詠翔",1000.0,'2021-01-01'),]
	cursor.executemany(sqlStuff, records)
	db.commit()

	for i in range (1,498):
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
		cursor=db.cursor()
		sqlStuff = "INSERT INTO User_Record (User_ID,User_Name,User_LTV,User_Join) VALUES (%s,%s,%s,%s)"
		records = [(users_num+1,str(firstname)+" "+str(lastname),1000.0,'2021-01-01'),]
		cursor.executemany(sqlStuff, records)
		db.commit()

def SQL_Query(sql):
	cursor=db.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	return data