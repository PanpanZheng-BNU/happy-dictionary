__author__ = 'Katie Lee'


def iciba(list_dict):
    # import zone
    import os
    import urllib.request
    from xml.dom.minidom import parse
    import xml.dom.minidom

    # get the current working path
    CurrentWorkingPath = os.getcwd()

    # prepare the url_pre and post Strings
    url_preString = "http://dict-co.iciba.com/api/dictionary.php?w="
    url_postString = "&key=BACC496E7F9A1E527D004E6D4F563417"

    # prepare the txtFileName and Folders
    # txtFileName = "Dictionary_Revised.txt"
    # txtFileName = "singleWord.txt"
    # txtPathName = CurrentWorkingPath + '\\' + txtFileName
    FolderName_Dict = "ALLDictionaryWords_ICIBA_singleWord"
    FolderName_Others = "OtherWordsCannotFind_ICIBA"

    if not os.path.exists(FolderName_Dict):
        os.mkdir(FolderName_Dict)

    if not os.path.exists(FolderName_Others):
        os.mkdir(FolderName_Others)
        # f_dict = open(txtPathName)
        # list_dict = f_dict.read().split('\n')
        # n = 0
        # for iWord in list_dict:
        #
        #     word_url = url_preString + iWord + url_postString
        #     n += 1
        #     xml_codes = urllib.request.urlopen(word_url).read()
        #     dom1 = xml.dom.minidom.parseString(xml_codes)
        #     results = dom1.getElementsByTagName("pos")
        #     if len(results) > 0:
        #         xmlPath = CurrentWorkingPath + os.sep + FolderName_Dict
        #         xmlFileName = xmlPath + os.sep + iWord + ".xml"
        #         # print xmlFileName
        #         urllib.request.urlretrieve(word_url, xmlFileName)
        #     else:
        #         # print "else"
        #         xmlPath = CurrentWorkingPath + os.sep + FolderName_Others
        #         xmlFileName = xmlPath + os.sep + iWord + ".xml"
        #         # print xmlFileName
        #         # xmlFileName = CurrentWorkingPath + "\\" + FolderName_Others + "\\" + iWord
        #         urllib.request.urlretrieve(word_url, xmlFileName)
    iWord = list_dict

    word_url = url_preString + iWord + url_postString
    # n += 1
    xml_codes = urllib.request.urlopen(word_url).read()
    dom1 = xml.dom.minidom.parseString(xml_codes)
    results = dom1.getElementsByTagName("pos")
    if len(results) > 0:
        xmlPath = CurrentWorkingPath + os.sep + FolderName_Dict
        xmlFileName = xmlPath + os.sep + iWord + ".xml"
        # print xmlFileName
        urllib.request.urlretrieve(word_url, xmlFileName)
    else:
        # print "else"
        xmlPath = CurrentWorkingPath + os.sep + FolderName_Others
        xmlFileName = xmlPath + os.sep + iWord + ".xml"
        # print xmlFileName
        # xmlFileName = CurrentWorkingPath + "\\" + FolderName_Others + "\\" + iWord
        urllib.request.urlretrieve(word_url, xmlFileName)
