#coding=utf8

#----------------------------------------
#version: 0.2
#usage:myOCR_start(im)
#----------------------------------------
import PIL.ImageEnhance
from timeout import timeout

def remove_isolate(ran_x, ran_y):
	result_x = []
	result_y = []
	for i in range( len(ran_x)/2 ):
		j = i
		if ( (ran_x[2*i+1] - ran_x[2*i]) + (ran_y[2*j+1] - ran_y[2*j]) ) > 5:
			result_x.append(ran_x[2*i])
			result_x.append(ran_x[2*i+1])
			result_y.append(ran_y[2*j])
			result_y.append(ran_y[2*j+1])
	return ( result_x,result_y )

def match_white(color):
	return ( (255-color[0]<10) and (255-color[1]<10) and (255-color[2]<10) )

def im_2bit(im):
	x = im.size[0]
	y = im.size[1]
	bit = [ [0 for col in range(0,y-1)] for row in range(0,x-1) ]
	for i in range(0, x-1):
		for j in range(0, y-1):
			if match_white( list(im.getpixel((i,j))) ):
				bit[i][j] = 0
			else:
				bit[i][j] = 1
	return bit

def getEnd_x(bit,start,ran_x,ran_y):
	for end in range(start,ran_x-1):
		total_white = True
		for j in range(ran_y-1):
			total_white &= (~bit[end][j])
		if total_white:
			return end-1
		else:
			continue
	return

def getEnd_y(bit,start,ran_x,ran_y):
	for end in range(start,ran_y-1):
		total_white = True
		for i in range(ran_x[0],ran_x[1]):
			total_white &= (~bit[i][end])
		if total_white:
			return end-1
		else:
			continue
	return ran_y-2

def bit2str(bit,ran_x,ran_y,count):
	res=''
	for i in range(ran_x[2*count],ran_x[2*count+1]+1):
		for j in range(ran_y[2*count],ran_y[2*count+1]+1):
			if bit[i][j]:
				res += '1'
			else:
				res += '0'
	return res

def initDistance(str1,str2):
	distance=[[0 for col in range(len(str2))] for row in range(len(str1))]
	for i in range(len(str1)):
		for j in range(len(str2)):
			distance[i][j] =- 1
	distance[0][0] = 0
	for i in range(len(str1)):
		distance[i][0] = i
	for j in range(len(str2)):
		distance[0][j] = j
	return distance


def EditDistance(str1,str2,distance,pos_x,pos_y):
	if distance[pos_x][pos_y] != -1:
		return distance[pos_x][pos_y]
	min_dis = min( EditDistance(str1,str2,distance,pos_x,pos_y-1)+1,EditDistance(str1,str2,distance,pos_x-1,pos_y)+1 )
	replace_dis = 0
	if str1[pos_x] != str2[pos_y]:
		replace_dis = 1
	min_dis=min( min_dis,EditDistance(str1,str2,distance,pos_x-1,pos_y-1)+replace_dis )
	distance[pos_x][pos_y] = min_dis
	return min_dis


def getNumber(im):
	enhancer = PIL.ImageEnhance.Contrast(im)
	im=enhancer.enhance(1.5)
	enhancer = PIL.ImageEnhance.Brightness(im)
	im=enhancer.enhance(2)
	#print im.getpixel((130,10))
	bit=im_2bit(im)
	ran_x = []
	ran_y = []
	count = 0
	x_begin = 0
	x_end = 0
	while True:
		STOP = False
		for i in range(x_end+1, im.size[0]-1):
			if i == im.size[0]-2:
				STOP = True
			total_white = True
			for j in range(2, im.size[1]-1):
				total_white &= (~bit[i][j])
			if total_white:
				continue
			else:
				x_begin = i
				x_end = getEnd_x(bit,x_begin, im.size[0], im.size[1])
				ran_x += (x_begin,x_end)
				count += 1
				break
		if STOP:
			break
	count=0
	while count < (len(ran_x)/2):
		for j in range(2, im.size[1]-1):
			total_white=True
			for i in range(ran_x[2*count] ,ran_x[2*count+1]):
				total_white &= (~bit[i][j])
			if total_white:
				continue
			else:
				y_begin = j
				y_end = getEnd_y(bit,y_begin, (ran_x[2*count], ran_x[2*count+1]), im.size[1])
				ran_y += (y_begin ,y_end)
				count += 1
				break
	result = remove_isolate(ran_x, ran_y)
	ran_x = result[0]
	ran_y = result[1]
	count = len(ran_x)/2
	NumberList = [''for i in range(count)]
	for i in range(count):
		NumberList[i] = bit2str(bit, ran_x, ran_y, i)
	#print NumberList
	return NumberList

@timeout(2)
def myOCR_start(im):
	characteristic_value = [''for i in range(10)]
	characteristic_file = open("vcodeData2",'r')
	for i in range(10):
		characteristic_value[i] = characteristic_file.readline()
		characteristic_value[i] = characteristic_value[i][:len(characteristic_value[i])-1]
	characteristic_file.close()
	NumberList = getNumber(im)
	result=''
	min_distance = 99999
	tmp_res = 0
	for i in range(len(NumberList)):
		min_distance = 99999
		tmp_res = 0
		for j in range(len(characteristic_value)):
			str1 = NumberList[i]
			str2 = characteristic_value[j]
			distance = EditDistance(str1, str2, initDistance(str1,str2), len(str1)-1, len(str2)-1)
			if distance < min_distance:
				tmp_res = j
				min_distance = distance
			#print tmp_res,min_distance
		result += str(tmp_res)
	return result

#im=PIL.Image.open("ValidateCode.jpg")
#print myOCR_start(im)
