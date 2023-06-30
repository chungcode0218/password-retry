#密碼重試程式
#先在程式碼中 設定好密碼為a123456 
#讓使用者最多輸入3次密碼
#錯誤時要印出還有幾次機會
password = 'a123456'   #先將密碼存著比較好(方便之後改動)
times = 1
while times <= 3:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('密碼正確 ! 登入成功 !')
		break
	else:
		chance = 3 - times
		print('密碼錯誤! 您還剩下',chance ,'次機會' )
	times = times + 1
if pwd != password:
	print('錯誤次數過多，已封鎖帳密')