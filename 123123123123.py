studs = [{'sid': '103', 'Chinese': 90, 'Math': 95, 'English': 92}, 
         {'sid': '101', 'Chinese': 80, 'Math': 85, 'English': 82}, 
         {'sid': '102', 'Chinese': 70, 'Math': 75, 'English': 72}]
scores = {}
for stud in studs:
    v = []
    for key, value in stud.items():
        if key =='sid':
            k = value
        else:
            v.append(value)
    scores[k] = v
so = list(scores.items())
so.sort(key = lambda x: x[0], reverse = False)
for i in so:
    print('{}:{}'.format(i[0], i[1]))