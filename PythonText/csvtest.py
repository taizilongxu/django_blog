#coding= utf-8
#---------------------------------import---------------------------------------
import csv
#------------------------------------------------------------------------------
csvfile = file('../source/data_20131013_20140503.csv','rb')
reader = csv.reader(csvfile)

dic = {}
# for index,line in enumerate(reader):
#     if index < 12:
#         continue
#     if line[2] in dic:
#         dic[line[2]] += float(line[0])
#     else:
#         dic[line[2]] = float(line[0])
# for i in dic:
#     print '%s : %s' % (i,dic[i])

#时间学习
# for index,line in enumerate(reader):
#     if index < 12:
#         continue
#     if line[1] in dic:
#         dic[line[1]] += float(line[0])
#     else:
#         dic[line[1]] = float(line[0])
# for i in dic:
#     print '%s : %s' % (i,dic[i])
# F = open('../source/timemeter2.txt','aw')
# F.write(str(dic))
# F.close()

#第2个表数据
# for index,line in enumerate(reader):
#     if index < 12:
#         continue
#     if line[3][0:7] in dic:
#     	dic[line[3][0:7]] += float(line[0])
#     else:
#     	dic[line[3][0:7]] = float(line[0])
# F = open('../source/timemetermouth.txt','wa')
# F.write(str(dic))
# F.close()

# for i in dic:
#     print '%s : %s' % (i,dic[i])


###############################################################################
