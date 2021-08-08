from flask import Flask, render_template, json

app = Flask(__name__)

# get data lists
with open('assets/common_words.json', 'r') as myfile:
    data=myfile.read()
common_word_list = json.loads(data)
with open('assets/common_tags.json', 'r') as myfile:
    data=myfile.read()
common_tag_list = json.loads(data)
with open('assets/common_genres.json', 'r') as myfile:
    data=myfile.read()
common_genre_list = json.loads(data)
with open('assets/developer_dict.json', 'r') as myfile:
    data=myfile.read()
developer_dict = json.loads(data)
with open('assets/publisher_dict.json', 'r') as myfile:
    data=myfile.read()
publisher_dict = json.loads(data)

# get top 20 appear-the-most dev & pub
cutdevlist = list(developer_dict.keys())
cutdevlist = [a for a in cutdevlist if developer_dict[a] > 50]
cutpublist = list(publisher_dict.keys())
cutpublist = [a for a in cutpublist if publisher_dict[a] > 50]


@app.route('/', methods=['GET'])
def index():
    # get top 20 appear-the-most dev & pub
    developerList = json.dumps( cutdevlist )
    publisherList = json.dumps( cutpublist )
    return render_template('index.html', developerList=developerList, publisherList=publisherList)