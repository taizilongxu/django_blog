#---------------------------------import---------------------------------------
import sys
import misaka as m
from misaka import HtmlRenderer, Markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
#------------------------------------------------------------------------------

class ColorRenderer(HtmlRenderer):
    def block_code(self, text, lang):
        if not lang:
            return '<pre><code>%s</code></pre>' % text.strip()
        lexer = get_lexer_by_name(lang, stripall = True)
        return highlight(text, lexer, HtmlFormatter())

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as fd:
            text = fd.read()
    else:
        text = sys.stdin.read()
    text = text.decode('utf-8')

    flags = m.HTML_HARD_WRAP
    exts = m.EXT_FENCED_CODE | m.EXT_AUTOLINK | m.EXT_NO_INTRA_EMPHASIS | m.EXT_SUPERSCRIPT | m.EXT_TABLES
    md = Markdown(ColorRenderer(flags), exts)
    print md.render(text).encode('utf-8')
###############################################################################
