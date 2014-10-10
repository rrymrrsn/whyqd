from bs4 import BeautifulSoup
from pydocx import Docx2Html
import re

def cleanhtml(html, **kwargs):
    '''
    The HTML generated by both the docx converter and the diff needs serious cleansing.
    '''
    valid_keep = kwargs.get('valid_keep', ['b', 'i', 'u', 'strong', 'em', 'blockquote', 'div', 'ins'])
    valid_del = kwargs.get('valid_del', ['del', 'hr'])
    # https://medium.com/p/f2fa442daf99
    soup = BeautifulSoup(html, 'html.parser')
    if soup.body:
        soup = soup.body
    # http://tezro.livejournal.com/219164.html
    empty_tags = soup.find_all(lambda tag: tag.name in valid_keep and not tag.contents and (tag.string is None or not tag.string.strip()))
    [empty_tag.unwrap() for empty_tag in empty_tags]
    # clear up the mess
    # http://stackoverflow.com/q/1765848
    for v in valid_keep:
        for match in soup.find_all(v):
            match.unwrap()
    for v in valid_del:
        for match in soup.find_all(v):
            match.decompose()
    return soup    
    
def mergediff(html, **kwargs):
    # Changes related to b, i, u, strong, em, blockquote are allowed...
    kwargs['valid_keep'] = ['div', 'ins']
    soup = cleanhtml(html, **kwargs)
    return unicode(soup)

def docxtract(docxfile, **kwargs):
    '''
    Get a docx file and extract chapters. Return an array for further processing by the user.
    '''
    header = [u'h1', u'h2', u'h3', u'h4']
    html = Docx2Html(docxfile).parsed
    html = cleanhtml(html, **kwargs)
    # Get the tree
    p = False
    tree = []
    for child in html.find_all(True):
        if child.name in header:
            if p:
                tree.append([ptext, p])
                p = False
            tree.append(["<b>%s</b>" % child.get_text(), unicode(child)])
        else:
            if child.get_text().strip():
                if p:
                        p = ''.join([p, unicode(child)])
                else:
                    p = unicode(child)
                    ptext = "%s..." % child.get_text()[:80]
    if p:
        tree.append([ptext, p])
    return tree

def xtractemail(emails):
    """
    Receive a list of emails as a comma-separated value;
    Test against a regex http://www.w3.org/TR/html5/forms.html#valid-e-mail-address and return only the valid ones;
    """
    regex = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    emails = emails.split(",")
    reg_test = re.compile(regex)
    emails = [e for e in emails if reg_test.match(e)]
    return emails