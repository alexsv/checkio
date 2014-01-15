import re
import time
from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%d-%H-%M-%S"
HOSTNAME_PATTERN = "\w+://([^/]+).*"
SESSION_TIME = 30 * 60 + 1

def checkio(data):
    sessions = {}
    for dt, name, url in [line.split(";;") for line in data.split("\n")]:
        dtint = int(time.mktime(datetime.strptime(dt, DATETIME_FORMAT).timetuple()))
        name = name.lower()
        hostname = re.findall(HOSTNAME_PATTERN, url)[0]
        hostname = '.'.join(hostname.split('.')[-2:])
        key = "%s/%s" % (name, hostname)
        if key not in sessions:
            sessions[key] = [[dtint, dtint, 1, name, hostname]]
        else:
            if dtint - sessions[key][-1][1] <= SESSION_TIME:
                sessions[key][-1][1] = dtint
                sessions[key][-1][2] += 1
            else:
                sessions[key].append([dtint, dtint, 1, name, hostname])
    result = []
    for record in sessions.values():
        result.extend(record)
    result = sorted([(rec[3], rec[4], rec[1] - rec[0] + 1, rec[2]) for rec in result])
    return "\n".join(map(lambda x: ";;".join(map(str, x)), result))

if __name__ == "__main__":
    print checkio("""2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-01-01-03-11-00;;Name;;http://checkio.org/task
2013-02-03-04-00-00;;user2;;http://checkio.org/task""")
