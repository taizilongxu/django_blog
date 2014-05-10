#coding= utf-8
#---------------------------------import---------------------------------------
from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404
#------------------------------------------------------------------------------------
PATH = ' http://127.0.0.1:8000/'

F = open('/home/limbo/code/myblog/source/tags.txt','r')
tags = eval(F.read())
tags1 = [i for i in tags]
tags2 = [len(tags[i]) for i in tags]
lable=["primary","success","info","warning","danger"]
TAGS = zip(tags1,tags2,lable)
F.close()

F = open('/home/limbo/code/myblog/source/times.txt','r')
TIMES = eval(F.read())
F.close()

#------------------------------------------------------------------------------------
def indexinfo(request,template_name):
	tags3 = TAGS
	path = PATH
	txt = TIMES
	title = 'Limbo\'s blog'	

	l = [i[1][0] for i in txt]
	info = [i[1][2] for i in txt]
	h = zip(l,info)
	return render_to_response(template_name,locals())

def about(request):
	tags3 = TAGS
	path = PATH

	return render_to_response('about.html',locals())

def blog_index(request):	
	txt = TIMES
	tags3 = TAGS
	path = PATH
	txt2 = TIMES
	l = [i[1][0] for i in txt]
	info = [i[1][2] for i in txt]
	h = zip(l,info)

	address = []
	for key in txt2:
		x = key[0][0:10].split('-')
		path1 = PATH + 'article/' + '/'.join(x) + '/'
		abso = path1 + key[1][0].strip('.md') + '.html'
		address.append(abso)

	addr = zip(l,address)

	return render_to_response('blog_index.html',locals())

def blog_body(request,year,month,day,blog_title):
	tags3 = TAGS
	path = PATH
	F = open('/home/limbo/code/myblog/article/' + year + '/' + month + '/' + day + '/' +blog_title ,'r' )
	output = F.read()
	F.close()
	blog_title = blog_title.strip('.html')
	return render_to_response('blog_body.html',locals())

def time(request):
	tags3 = TAGS
	path = PATH
	F1 = open('/home/limbo/code/myblog/source/timemeter.txt','r')
	txt = eval(F1.read())
	F1.close()
	sort=sorted(txt.items(),key=lambda e:e[1],reverse=True)
	timemetertag = [ i[0] for i in sort]
	timemetertime = [i[1] for i in sort]

	pieValue = [txt[i] for i in txt]
	color = ["#D9534F","#69D2E7","#F38630","#5CB85C","#999","#46BFBD","#428BCA","#FDB45C","#E0E4CC","#949FB1","#4D5360"]
	pieData = zip(sorted(pieValue,reverse = True),color)
	pieTitle = zip(timemetertag,timemetertime,color)

	F2 = open('/home/limbo/code/myblog/source/timemeter2.txt','r')
	txt2 = eval(F2.read())
	F2.close()
	l2 = [txt2[i] for i in txt2]
	h2 = zip(l2,color)

	F3 = open('/home/limbo/code/myblog/source/timemetermouth.txt','r')
	txt3 = eval(F3.read())
	F3.close()
	sort3=sorted(txt3.items(),key=lambda e:e[0],reverse=False)
	s1 = [i[0] for i in sort3]
	si1 = [i[1] for i in sort3]
	h3 = zip(s1,si1)

	return render_to_response('time.html',locals())
	

def blog(request,year,month,day):
	return render_to_response('blog.html')