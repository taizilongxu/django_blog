#coding= u8
#---------------------------------import---------------------------------------
import os
import sys
import misaka as m

from misaka import HtmlRenderer, Markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
#------------------------------------------------------------------------------------
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
for key in txt:
    x = key[0][0:10].split('-')
    path = '../article/' + '/'.join(x)
    mkdir(path)
    f = open(key[1][1],'r')
    input = f.read()
    f.close()

    flags = m.HTML_HARD_WRAP
    exts = m.EXT_FENCED_CODE | m.EXT_AUTOLINK | m.EXT_NO_INTRA_EMPHASIS | m.EXT_SUPERSCRIPT | m.EXT_TABLES
    md = Markdown(ColorRenderer(flags), exts)
    html = md.render(input).encode('utf-8')
    abso = path + '/' + key[1][0].strip('.md') + '.html'
    f = open(abso,'aw')
    key[1][1] = abso
    print key[1][1]
    f.write(html)
    f.close()
###############################################################################
