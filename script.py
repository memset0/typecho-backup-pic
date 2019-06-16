import yaml, requests
import re, os, mimetypes

root_path = os.path.dirname(os.path.abspath(__file__))
result_path = os.path.join(root_path, 'result')
pic_counter = 0

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
}

def make_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)

def info_color(text):
	return '\033[35m' + text + '\033[0m'

def request_get(url):
	return requests.get(url, headers=headers)

def download_pic(url):
	print('download pic', info_color(url), end=" ")
	global pic_counter
	req = request_get(url)
	content_type = req.headers['content-type'].partition(';')[0].strip()
	extension = mimetypes.guess_extension(content_type)
	pic_name = str(pic_counter) + extension
	print('to', info_color(pic_name))
	pic_path = os.path.join(result_path, pic_name)
	pic_file = open(pic_path, 'wb+')
	pic_file.write(req.content)
	pic_file.close()
	pic_counter += 1
	return pic_name

def search(path):
	content = open(path, 'rb+').read()
	text = str(content)
	md_set = re.findall(r'!\[[\S!\[!\]]*?\]\([\S]*?\)', text)
	result = [ it.split('(')[-1].split(')')[0] for it in md_set ]
	return result

if __name__ == '__main__':
	make_dir(result_path)
	for url in search(os.path.join(root_path, 'source.dat')):
		name = download_pic(url)