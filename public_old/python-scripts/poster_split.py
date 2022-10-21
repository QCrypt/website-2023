import copy

import simplejson as json
from collections import OrderedDict
import csv


#create Ordered Dictionary using keyword
# 'object_pairs_hook=OrderDict'

with open('2021_posters.json', encoding='utf8') as fh:
    data = json.load(fh, object_pairs_hook=OrderedDict)

    with open('poster_schedule.csv', encoding='utf8') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        tuesday = {}
        thursday = {}
        for row in reader:
            print(reader.line_num, row)
            if row[1] and reader.line_num > 3:
                if len(row[4].split(':')) > 1:
                    arxivid = row[4].split(':')[1]
                else:
                    arxivid = row[4]

                if reader.line_num < 34:
                    tuesday[int(row[1])] = [row[2], arxivid]
                else:
                    thursday[int(row[1])] = [row[2], arxivid]

        tue_data = []
        for poster in data:
            print(poster)
            if poster['pid'] in tuesday:
                presenter_arxiv = tuesday[poster['pid']]
                poster['options'] = {}
                if presenter_arxiv[0]:
                    poster['options']['name-main-presenter'] = presenter_arxiv[0]
                if presenter_arxiv[1]:
                    poster['options']['arxiv-id'] = presenter_arxiv[1]
                tue_data.append(poster)

        with open('poster_tue_afternoon.json', 'w', encoding='utf8') as tue_fh:
            json.dump(tue_data, tue_fh, indent=4, ensure_ascii=False)


        thu_data = []
        for poster in data:
            print(poster)
            if poster['pid'] in thursday:
                presenter_arxiv = thursday[poster['pid']]
                poster['options'] = {}
                if presenter_arxiv[0]:
                    poster['options']['name-main-presenter'] = presenter_arxiv[0]
                if presenter_arxiv[1]:
                    poster['options']['arxiv-id'] = presenter_arxiv[1]
                thu_data.append(poster)

        with open('poster_thu_morning.json', 'w', encoding='utf8') as thu_fh:
            json.dump(thu_data, thu_fh, indent=4, ensure_ascii=False)

