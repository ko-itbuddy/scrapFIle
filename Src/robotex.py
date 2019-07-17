import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.wikipedia.org/robots.txt")
rp.read()

print(rp)

