#coding= utf-8
#---------------------------------import---------------------------------------
import glob
import markdown2
import re
#------------------------------------------------------------------------------
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
###############################################################################
