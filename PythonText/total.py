#coding= utf-8
#---------------------------------import---------------------------------------
import glob
import markdown2
import re
import csv

import os
import sys
import misaka as m

from misaka import HtmlRenderer, Markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
#-------------------------------------------------------------------------------------
tags = {}
times = {}
for filepath in glob.glob(r'../article/*.md'):
    F = open(filepath,'r')
    txt = F.readlines()
    i = 0
    flag = 1
    si = []
    tmp1 =''
    for data in txt:
        if flag == 0:
            if i == 2:
                si = [markdown2.markdown(i) for i in si]
                si = [re.sub(r'</?\w+[^>]*>','',i) for i in si]
                times[tmp1].append(si) #加入index索引
                break
            else:
                i += 1
                si.append(data)
        if data == '---\n':
            flag = 0
        #tags
        if data.find('tag') != -1 and flag:
            tmp = (data[5:]).strip('\n')
            taginfo = []
            filename = (filepath.split("/")[-1]).split(".")[-2] #文件名
            taginfo.append(filename)
            taginfo.append(filepath)
            if tmp in tags:
                length = len(tags[tmp])
                tags[tmp][length + 1] = taginfo
            else:
                s = {}
                s[1] = taginfo
                tags[tmp] = s
        #times
        if data.find('date') != -1 and flag:
            tmp1 = (data[6:]).strip('\n')
            taginfo = []
            filename = (filepath.split("/")[-1]).split(".")[-2] #文件名
            taginfo.append(filename)
            taginfo.append(filepath)
            times[tmp1] = taginfo
    F.close()
print tags
Ft = open('../source/tags.txt','wa')
Ft.write(str(tags))
Ft.close()

dict1= sorted(times.iteritems(), key=lambda d:d[0])#字典排序
print dict1
Fd = open('../source/times.txt','wa')
Fd.write(str(dict1))
Fd.close()
#csv control
#-------------------------------------------------------------------------------------
csvfile = file('../source/data_20131013_20140503.csv','rb')
reader = csv.reader(csvfile)

#
dic1 = {}
for index,line in enumerate(reader):
    if index < 12:
        continue
    if line[2] in dic1:
        dic1[line[2]] += float(line[0])
    else:
        dic1[line[2]] = float(line[0])
for i in dic1:
    print '%s : %s' % (i,dic1[i])
F = open('../source/timemeter.txt','wa')
F.write(str(dic1))
F.close()

#时间学习

dic2 = {}
for index,line in enumerate(reader):
    if index < 12:
        continue
    if line[1] in dic2:
        dic2[line[1]] += float(line[0])
    else:
        dic2[line[1]] = float(line[0])
for i in dic2:
    print '%s : %s' % (i,dic2[i])
F = open('../source/timemeter2.txt','wa')
F.write(str(dic2))
F.close()

#第2个表数据

dic3= {}
for index,line in enumerate(reader):
    if index < 12:
        continue
    if line[3][0:7] in dic3:
        dic3[line[3][0:7]] += float(line[0])
    else:
        dic3[line[3][0:7]] = float(line[0])
F = open('../source/timemetermouth.txt','wa')
F.write(str(dic3))
F.close()
#-------------------------------------------------------------------------------------
class ColorRenderer(HtmlRenderer):
    def block_code(self, text, lang):
        if not lang:
            return '<pre><code>%s</code></pre>' % text.strip()
        lexer = get_lexer_by_name(lang, stripall = True)
        return highlight(text, lexer, HtmlFormatter())
F = open('../source/times.txt','r')
txt = eval(F.read())
F.close()
#解决输出乱码问题
reload(sys)
sys.setdefaultencoding('utf-8')
#创建文件目录，方便索引
def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        print path + 'success!'
        os.makedirs(path)
        return True
    else:
        print path + 'has been made!'
        return False

#创建文件article目录
F = open("../source/times.txt","wa")

for key in txt:
    x = key[0][0:10].split('-')
    path = '../article/' + '/'.join(x)
    mkdir(path)
    f = open(key[1][1],'r')
    input = f.readlines()
    f.close()

    #去掉---行
    tmp = []
    flag = False
    for line in input:
        if flag:
            tmp.append(line)
        if line == "---\n":
            flag = True
    input = ''.join(tmp)
    print input

    #makrdown html
    #flags = m.HTML_HARD_WRAP
    #exts = m.EXT_FENCED_CODE | m.EXT_AUTOLINK | m.EXT_NO_INTRA_EMPHASIS | m.EXT_SUPERSCRIPT | m.EXT_TABLES
    #md = Markdown(ColorRenderer(flags), exts)
    #html = md.render(input).encode('utf-8')
    abso = path + '/' + key[1][0] + '.html'
    print abso
    f = open(abso,'wa')
    key[1][2] = abso
    print key[1][2]


    f.write(input)
    f.close()

#写入times.txt
F.write(str(txt))
F.close()
print txt
