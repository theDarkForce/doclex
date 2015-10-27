# -*- coding: UTF-8 -*-
# doclex
# create at 2015/10/27
# autor: qianqians

def docsplit(doc):
    doclist = doc.split('.')

    def sub(doc_list, ch):
        _list = []
        for str in doc_list:
            _list.extend(str.split(ch))
        return _list

    for ch in [',', ';', '，', '。']:
        doclist = sub(doclist, ch)

    return doclist

def lex(doc):
    doclist = docsplit(doc)

