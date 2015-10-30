# -*- coding: UTF-8 -*-
# doclex
# create at 2015/10/27
# autor: qianqians
import chardet

def docsplit(doc):
    doclist = doc.split('.')

    def sub(doc_list, ch):
        _list = []
        for str in doc_list:
            _list.extend(str.split(ch))
        return _list

    for ch in [u',', u';', u'，', u'。']:
        doclist = sub(doclist, ch)

    return doclist

keykorks = [u"大灰狼",u"小白兔"]

def splitbykeyworks(str):
    strlist = [str]
    for word in keykorks:
        words = []
        for str in strlist:
            r = str.split(word)
            for s in r:
                if s != "":
                    words.append(s)
                else:
                    words.append(word)
        strlist = words

    return strlist

dec1 = [u'是',u'乃']
dec2 = [u'不是']
dec1filte = [u'不是',u'是的']

def splitbydec(str):
    words = []

    strdoc = str.split(dec2[0]);

    for str in strdoc:
        tmp = ""
        index = 0
        for i in range(len(str)):
            ch = str[i]
            tmp += ch
            if ch == u'是':
                if str[i-1:i+1] == dec1filte[0]:
                    continue
                if str[i:i+2] == dec1filte[1]:
                    continue

            if ch in dec1:
                words.append(str[index:i+1])
                index = i+1
                tmp = ""
        if tmp != "":
            words.append(tmp)
    return words

classifier = [u'匹',u'张',u'座',u'回',u'场',u'尾',u'条',u'个',u'首',u'阙',u'阵',u'网',u'炮',u'顶',u'丘',u'棵',
              u'只',u'支',u'袭',u'辆',u'挑',u'担',u'颗',u'壳',u'窠',u'曲',u'墙',u'群',u'腔',u'砣',u'座',u'客',
              u'贯',u'扎',u'捆',u'刀',u'令',u'打',u'手',u'罗',u'坡',u'山',u'岭',u'江',u'溪',u'钟',u'队',u'单',
              u'双',u'对',u'口',u'头',u'枝',u'件',u'贴',u'针',u'线',u'管',u'名',u'位',u'身',u'堂',u'课',u'本',
              u'页',u'丝',u'毫',u'厘',u'分',u'钱',u'两',u'斤',u'担',u'铢',u'石',u'钧',u'锱',u'忽',u'脚',u'板',
              u'跳',u'寸',u'尺',u'丈',u'里',u'寻',u'常',u'铺',u'程',u'撮',u'勺',u'合',u'升',u'斗',u'石',u'盘',
              u'碗',u'碟',u'叠',u'桶',u'笼',u'盆',u'盒',u'杯',u'钟',u'斛',u'锅',u'簋',u'篮',u'盘',u'桶',u'罐',
              u'瓶',u'壶',u'卮',u'盏',u'箩',u'箱',u'煲',u'啖',u'袋',u'钵',u'年',u'月',u'日',u'季',u'刻',u'时',
              u'周',u'天',u'秒',u'分',u'旬',u'纪',u'岁',u'世',u'更',u'夜',u'春',u'夏',u'秋',u'冬',u'代',u'伏',
              u'辈',u'丸',u'泡',u'粒',u'颗',u'幢',u'堆']

numlist = [u'一',u'二',u'三',u'四',u'五',u'六',u'七',u'八',u'九',u'十',u'百',u'千',u'万',u'亿',u'兆','1',u'2'
           u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'0',u'壹',u'壹',u'贰',u'贰',u'叁',u'肆',u'肆',u'伍',u'伍',u'陆',u'柒',u'捌',u'玖',u'拾',u'佰',u'仟']

def splitbyclassifier(str):
    words = []

    tmp = ""
    old = ""
    for ch in str:
        tmp += ch
        if ch in classifier:
            if old in numlist:
                for i in range(len(tmp)-2, 0, -1):
                    if tmp[i] not in numlist:
                        words.append(tmp[0:i+1])
                        words.append(tmp[i+1:])
                        tmp = ""
                        break
        old = ch
    if tmp != "":
        words.append(tmp)
    return words

punctuations = [u'.',u',',u'[',u']',u'{',u'}',u'"',u'\'',u';',u':',u'<',u'>',u'?',u'?',u'(',u')',u'*',u'&',u'^',u'%',u'$',u'#',u'@',u'!',u'~',u'`',
                u'，',u'》',u'。',u'《',u'？',u'/',u'：',u'；',u'“',u'‘',u'{',u'}',u'、',u'|']

def specialword(str):
    if len(str) < 32:
        for ch in str:
            if ch in punctuations:
                return False
    return True

adjective = [u'的',u'地',u'得']
adjectivefilte = [u'大地',u'地面',u'地表',u'地底',u'地暖',u'地光',u'地气',u'地平线',u'地藏王',u'地广人稀',u'地大物博']

def splitbyadjective(str):
    words = []

    tmp = ""
    index = 0
    for i in range(len(str)):
        ch = str[i]
        tmp += ch
        if ch == u'地':
            if str[i-1:i+1] == adjectivefilte[0]:
                continue
            if str[i:i+2] in adjectivefilte[1:7]:
                continue
            if str[i:i+3] in adjectivefilte[7:9]:
                continue
            if str[i:i+4] in adjectivefilte[9:]:
                continue

        if ch in adjective:
            words.append(str[index:i+1])
            index = i+1
            tmp = ""
    if tmp != "":
        words.append(tmp)
    return words

def lex(doc):
    encoding = chardet.detect(doc)
    doc = unicode(doc, encoding['encoding'])

    keywords = []

    if specialword(doc):
        keywords.append(doc)

    doclist = docsplit(doc)

    def splitlistbylambda(strlist, fn):
        ret = []
        for str in strlist:
            ret.extend(fn(str))
        return ret

    doclist = splitlistbylambda(doclist, splitbykeyworks)
    doclist = splitlistbylambda(doclist, splitbydec)
    doclist = splitlistbylambda(doclist, splitbyclassifier)
    doclist = splitlistbylambda(doclist, splitbyadjective)

    keywords.extend(doclist)

    return keywords

for str in lex("中国是一个伟大的古老的地大物博的国家"):
    print str