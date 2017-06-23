list=[
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "http://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.jpg"
    ]

m = {}
for x in list:
    if x.split("/")[-1] in m:
        m[x.split("/")[-1]] += 1
    else:
        m[x.split("/")[-1]] = 1

for key in sorted(m)[:3]:
	print(key, m[key])