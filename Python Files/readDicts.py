import json, ast, csv, cPickle

def load_json(name):
    with open(name, 'r') as f:
        temp = []
        for l in f:
            l = l.strip()
            temp.append(l)
        json_data = json.loads(json.dumps(temp))
##        return_dict = [ast.literal_eval(i) for i in json_data]
    return json_data

def read_csv(filename):
    with open(filename, 'rb') as f:
        content = csv.reader(f)
        content_list = []
        for row in content:
            content_list.append(row)
    return content_list

def insertIntoDat(liszt ,filename):
    with open(filename, 'wb') as f:
        for l in liszt:
            f.write(str(l) + '\n')
    print "written to file ..."

if __name__ == "__main__":

##    score_data = read_csv('yelp_reviews_scores.csv')
##    scores = [data[1] for data in score_data[1:]]
##    with open('score_list.dat', 'wb') as f:
##        for score in scores:
##            f.write(score + '\n')
    data = load_json('business.json')
    bool_atts = []
    for d in data:
        d = json.loads(str(d))
        for a,b in d['attributes'].iteritems():
            if (isinstance(b, dict)):
                bool_atts.append(str(a))

    bool_attset = list(set(bool_atts))
    print bool_attset
##    insertIntoDat(bool_attset, 'dict_atts.dat')

##    ridToStars = dict()
##    for d in data:
##        ridToStars.update({d['review_id'] : d['stars']})
##
##    cPickle.dump(ridToStars, open('ridToStars.pkl', 'wb'))
