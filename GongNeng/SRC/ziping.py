import urllib
import urllib2 
#coding=utf-8
import cookielib
import re

import sys



list = (920 , 923 , 930 , 930 , 935 , 952 , 953 , 944 , 818 , 44 , 49 , 823 , 59 , 64 , 69 , 76 , 828 , 84 , 89 , 94 , 99 , 104 , 109 , 114 , 119 , 124 , 129 , 134 , 139 , 144 , 833 , 158 , 838 , 165 , 173 , 174 , 179 , 184 , 843 , 194 , 199 , 204 , 209 , 214 , 848 , 224 , 853 , 234 , 239 , 244 , 249 , 254 , 259 , 264 , 269 , 274 , 858 , 284 , 289 , 294 , 299 , 304 , 309 , 314 , 319 , 324 , 329 , 334 , 339 , 344 , 354 , 863 , 364 , 868 , 374 , 379 , 873 , 389 , 394 , 399 , 404 , 878 , 414 , 419 , 424 , 429 , 434 , 439 , 444 , 449 , 883 , 888 , 464 , 469 , 474 , 479 , 893 , 489 , 494 , 898 , 504 , 509 , 514 , 519 , 524 , 529 , 903 , 539 , 544 , 549 , 554 , 559 , 564 , 569 , 574 , 579 , 584 , 589 , 594 , 599 , 604 , 908 , 614 , 619 , 624 , 629 , 634 , 639 , 913 , 649 , 659 , 659 , 664 , 669 , 674 , 679 , 684 , 689 , 694 , 699 , 704 , 709 , 714 , 719 , 724 , 729 , 734 , 739 , 744 , 749 , 754 , 760 , 764 , 918 , 774 , 779 , 784 , 789 , 794 , 799 , 804 , 809)



nID = ''
while 1:
    nID = raw_input("Input your id plz    ")
    if len(nID) != 7:
        print 'wring length of id,input again'
    else:
        break
Pass = raw_input("Input your password plz     ")




url = 'http://fuxue.nankai.edu.cn/index.php/assessment/question/mod/show'
urllogin = 'http://fuxue.nankai.edu.cn/index.php/Account/doLogin'

cj = cookielib.CookieJar()
pattern = re.compile(r'<h3>\S*:\S*')
pattern1 = re.compile(r'"[0-9]+" >\S*')
valueslogin ={
'Host':' fuxue.nankai.edu.cn',
'Connection':' keep-alive',
'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'DNT':' 1',
'Accept-Encoding':' gzip,deflate,sdch',
'Accept-Language':' zh-CN,zh;q=0.8'
} 
postdata = urllib.urlencode({'username':nID,'password':Pass})

req3 = urllib2.Request(urllogin,headers=valueslogin) 
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
response = opener.open(req3,postdata)
if response.read() != '<meta http-equiv=refresh content=\'0; url=http://fuxue.nankai.edu.cn/index.php/index/index\' >':
	print 'Password Error'
	sys.exit(0)
for cookie in cj:
	cookie = cookie.value

values = {
'Host':' fuxue.nankai.edu.cn',
'Connection':' keep-alive',
'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'DNT':' 1',
'Referer':'http://fuxue.nankai.edu.cn/index.php/assessment/xnmSelfAssessment',
'Accept-Encoding':' gzip,deflate,sdch',
'Accept-Language':' zh-CN,zh;q=0.8',
'Cookie':' PHPSESSID='+cookie
}

urlS='http://fuxue.nankai.edu.cn/index.php/assessment/question'
req4 = urllib2.Request(urlS,headers=values)
urllib2.urlopen(req4).read()




str2=' http://fuxue.nankai.edu.cn/index.php/assessment/question/fangxiang/xia/pid/'
count = 1
strup = 'http://fuxue.nankai.edu.cn/index.php/assessment/question_ajax'
for i in range(2,164):
	Re=' http://fuxue.nankai.edu.cn/index.php/assessment/question/fangxiang/xia/pid/'+str(count)
	Cook=' PHPSESSID='+cookie
	values2 = {
	'Host':' fuxue.nankai.edu.cn',
	'Connection':' keep-alive',
	'Accept':'  */*',
	'Origin':' http://fuxue.nankai.edu.cn',
	'X-Requested-With':' XMLHttpRequest',
	'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
	'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
	'DNT':' 1',
	'Referer':Re,
	'Accept-Encoding':' gzip,deflate,sdch',
	'Accept-Language':' zh-CN,zh;q=0.8',
	'Cookie':Cook
	}
	
	url2=(strup)
	req = urllib2.Request(url2,headers=values2)
	content = urllib2.urlopen(req,urllib.urlencode([('pid',str(count)),('answer',str(list[count-1]))])).read()

	result=pattern.findall(content)
	count=count + 1
	req4 = urllib2.Request((str2+str(count)),headers=values)
	content2 = urllib2.urlopen(req4).read()
	print count

	
Re=' http://fuxue.nankai.edu.cn/index.php/assessment/question/fangxiang/xia/pid/162'
cook=' PHPSESSID='+cookie
values2 = {
'Host':' fuxue.nankai.edu.cn',
'Connection':' keep-alive',
'Accept':'  */*',
'Origin':' http://fuxue.nankai.edu.cn',
'X-Requested-With':' XMLHttpRequest',
'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
'DNT':' 1',
'Referer':Re,
'Accept-Encoding':' gzip,deflate,sdch',
'Accept-Language':' zh-CN,zh;q=0.8',
'Cookie':cook
}

url3=('http://fuxue.nankai.edu.cn/index.php/assessment/commit_ajax')
req = urllib2.Request(url3,headers=values2)
content = urllib2.urlopen(req,urllib.urlencode([('pid',str(count)),('answer',str(list[161]))])).read()
