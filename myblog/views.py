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

#提取文章在首页展示
blog_title = []
blog_time = []
blog_output = []
blog_path = []

for i in range(len(TIMES)):
	tmp ='/home/limbo/code/myblog/'+ TIMES[i][1][2][3:]
	F = open(tmp,'r')
	blog_title.append(TIMES[i][1][0])
	blog_time.append(TIMES[i][0])
	blog_output.append(F.read())
	blog_path.append(TIMES[i][1][2])
	F.close()
INDEX_BLOG = zip(blog_title,blog_time,blog_output)
INDEX_BLOG_BODY = zip(blog_path,blog_title,blog_time)

#------------------------------------------------------------------------------------
def tags(request,tags_one):
	path = PATH
	tags3 = TAGS
	return render_to_response('tags.html',locals())

def indexinfo(request):
	tags3 = TAGS
	path = PATH
	txt = TIMES
	title = 'Limbo\'s blog'	
       	index_blog = INDEX_BLOG
	return render_to_response('index.html',locals())

def about(request):
	tags3 = TAGS
	path = PATH

	return render_to_response('about.html',locals())

def blog_index(request):
	tags3 = TAGS	
	index_blog = INDEX_BLOG_BODY
	path = PATH
	return render_to_response('blog_index.html',locals())

def blog_body(request,year,month,day,blogTitle):
	tags3 = TAGS
	path = PATH
	F = open('/home/limbo/code/myblog/article/' + year + '/' + month + '/' + day + '/' +blogTitle,'r' )
	output = F.read()
	F.close()
	blog_body_title = blogTitle[:-5]
	return render_to_response('blog_body1.html',locals())

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


	return render_to_response('time.html',locals())
	

def blog(request,year,month,day):
	return render_to_response('blog.html')

def mylove(request):
	path = PATH
	return render_to_response("mylove.html",locals())