__author__ = 'Katie Lee'


def iciba(input_text):
    import urllib.request
    import xml.dom.minidom

    # prepare the url_pre and post Strings
    url_preString = "http://dict-co.iciba.com/api/dictionary.php?w="
    url_postString = "&key=BACC496E7F9A1E527D004E6D4F563417"
    word_url = url_preString + input_text + url_postString

    xml_codes = urllib.request.urlopen(word_url).read()
    translate_result = xml.dom.minidom.parseString(xml_codes)


    if translate_result.getElementsByTagName('acceptation').length > 0:
        return translate_result
    else:
        return '啥也没找到'

# def xmltojson():
#     import json
#     import xmltodict



