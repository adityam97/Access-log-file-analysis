

import re

def get_status_count(file_name):
    data = open(file_name).read()
    data = re.findall(r' \d\d\d ',data)
    data = dict((i, data.count(i)) for i in data)
    for k, v in data.items():
        print("status code",k,"-> count", v)

file_name = "access_log"
get_status_count(file_name)
