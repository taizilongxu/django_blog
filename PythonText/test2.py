#coding= utf-8
#---------------------------------import---------------------------------------
import markdown2
import os
import codecs
#------------------------------------------------------------------------------
F = open('../source/times.txt','r')
txt = eval(F.read())
F.close()
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
for key in txt:
    x = key[0][0:10].split('-')
    path = '../article/' + '/'.join(x)
    mkdir(path)
    f = open(key[1][1],'r')
    input = f.read()
    f.close()
    html = markdown2.markdown(input)
    abso = path + '/' + key[1][0].strip('.md') + '.html'
    f = open(abso,'aw')
    key[1][1] = abso
    print key[1][1]
    print html
    f.write(html)
    f.close()

###############################################################################
