import re
def create_html(content, title):
    content = re.sub(r'<ul class="pre-numbering" style=".*?">[\s\S]*?</ul>','',content)
    content = re.sub(r'<div id="article_content" class="article_content clearfix" style="height: 1166px; overflow: hidden;">','<div id="article_content" class="article_content clearfix">',content)
    html_content = '<div class="blog-content-box">' + content + '</div>'
    html_title = '<h1>' + title + '</h1>\n'
    body = '<div style="margin:40px 40px 40px 40px">' + html_title + html_content +'</div>'
    # head = create_Head(title)
    # html = '<!DOCTYPE html>\n<html>' + head + body + '</html>'
    return body

def create_Head(title):
    """
    页面头部生成
    """
    try:
        head_title = '<title>' + title + '</title>\n'
        charset = '<meta charset="utf-8" />\n'
        head = '<head>\n' + head_title + charset +'</head>\n'
        return head
    except Exception as e:
        print("头部："+ str(e))