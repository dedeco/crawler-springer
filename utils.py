

def limpa_unicode(astr, force_encoding=False, encoding='latin-1', encoding_method='replace'):
    if not astr:
        return None

    s = astr
    s = s.replace(u'\u200b', u'')
    s = s.replace(u'\u2010', u'-')
    s = s.replace(u'\u2011', u'-')
    s = s.replace(u'\u2012', u'-')
    s = s.replace(u'\u2013', u'-')
    s = s.replace(u'\u2014', u'-')
    s = s.replace(u'\u2015', u'-')
    s = s.replace(u'\u2022', u'*')
    s = s.replace(u'\u2021', u'|')
    s = s.replace(u'\u2030', u'%0')
    s = s.replace(u'\u2122', u'TM')
    s = s.replace(u'\u2018', u"'")
    s = s.replace(u'\u2019', u"'")
    s = s.replace(u'\u201a', u"'")
    s = s.replace(u'\u201b', u"'")
    s = s.replace(u'\u201c', u'"')
    s = s.replace(u'\u201d', u'"')
    s = s.replace(u'\u201e', u'"')
    s = s.replace(u'\u201f', u'"')
    s = s.replace(u'\u255a', u'"')
    s = s.replace(u'\u20ac', u'Euro')
    s = s.replace(u'\uf066', u'')
    
    if force_encoding:
        ts = s.encode(encoding, encoding_method)
        s = unicode(ts, encoding)

    return s