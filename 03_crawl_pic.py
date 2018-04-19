import urllib
import re
import time

#main function
def main():
    start_time = time.time()
    try:
        html = get_html('http://tieba.baidu.com/p/2460150866')
        imglist = get_pic(html)
        save_pic(imglist)
    except:
         print('something wrong')
    finally:
         print('finally')
    end_time = time.time()
    print('time for running this script is %f s' %(end_time - start_time))


#get html
def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#get pic via re
def get_pic(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

#save pic to local pc
def save_pic(imglist):
    for imgurl in imglist:
        i = imgurl.split('/')[-1] #get the name of pic
        urllib.urlretrieve(imgurl, 'c:/downloads/%s' %i)

#main function
if __name__ == '__main__':
    main()    


        
