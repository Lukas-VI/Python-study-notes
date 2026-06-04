studs = [{'sid': '103', 'Chinese': 90, 'Math': 95, 'English': 92}, {'sid': '101', 'Chinese': 80, 'Math': 85, 'English': 82}, {'sid': '102', 'Chinese': 70, 'Math': 75, 'English': 72}]
sorted_studs = sorted(studs, key = lambda x:x['sid'])
for student in sorted_studs:
    print(f"学号：{student['sid']}，语文：{student['Chinese']}，数学：{student['Math']}，英语：{student['English']}")