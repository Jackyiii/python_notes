import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name,img_url):
	req= urllib.request.urlopen(img_url)
	img_content=req.read()
	with open(img_name,"wb") as f:
		f.write(img_content)

def main():
	g1=gevent.spawn(downloader,"1.jpg","https://douyucdn.cn/appCovers/2017/07/22/2325374_20170722125724_big.jpg")
	g2=gevent.spawn(downloader,"2.jpg","http://www.itcast.cn/")
	gevent.joinall([g1,g2])

if __name__ == '__main__':
	main()