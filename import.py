#!/usr/bin/env python
#-*- coding:utf-8 -*-

import gdata.spreadsheet.text_db
import config
import sys

MENU_ID = '0AmjmnXFuHdP0dDh0UHE4LU5EYXZtMzBZNUtOZnRnWmc'
MENU_SHEET = 'od6'

def main():
    dic, comments = load_dic(sys.stdin)

    client = gdata.spreadsheet.text_db.DatabaseClient(config.EMAIL, config.PASSWORD)
    db = client.GetDatabases(MENU_ID)[0]
    tbl = db.GetTables(MENU_SHEET)[0]

    for i in tbl.FindRecords(''):
        for key in  i.content.keys():
            if key in [u'date', u'曜日']:
                continue
            item = i.content[key]
            if not item:
                continue

            for j in item.split(u'・'):
                if j in dic:
                    continue
                dic[j] = [[u'*', j, u'名詞']]

    save_dic(sys.stdout, dic, comments)

def load_dic(f):
    dic = {}
    comments = []

    for line in f:
        if line[0] == '#':
            comments.append(line)
            continue
        a  = unicode(line, "utf-8").strip().split("\t")
        kanji = a[1]
        if kanji not in dic:
            dic[kanji] = []
        dic[kanji].append(a)
    return dic, comments

def save_dic(f, dic, comments):
    for line in comments:
        f.write(line)

    items = dic.items();
    items.sort(key=lambda x:x[1])
    for kanji, i in items:
        for j in i:
            line = "\t".join(j[:3])
            f.write(line.encode('utf-8'))
            f.write('\n')

if __name__=="__main__":
    main()
