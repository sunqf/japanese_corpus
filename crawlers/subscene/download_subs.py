


from webbrowser import open_new_tab 
import sys
import re
from collections import defaultdict
import os
import time
from tqdm import tqdm
import subprocess, shlex

url_base = lambda url: re.findall("https://subscene.com/subtitles/(.*)/[japanese|english]", url)[0]


jp_urls = [x.strip() for x in open(sys.argv[1]).readlines()]
jp_dict = defaultdict(list)
for url in jp_urls:
    jp_dict[url_base(url)].append(url)


en_urls = [x.strip() for x in open(sys.argv[2]).readlines()]
en_dict = defaultdict(list)
for url in en_urls:
    en_dict[url_base(url)].append(url)



os.system('mkdir ~/Desktop/subs')
try: 
    for item in tqdm(list(set(jp_dict.keys()) & set(en_dict.keys()))):
        os.system('mkdir ~/Desktop/subs/%s' % item)
        os.system('mkdir ~/Desktop/subs/%s/jp' % item)
        os.system('mkdir ~/Desktop/subs/%s/en' % item)

        for jp_sub in set(jp_dict[item]):   # set to rm dups
            os.system('wget %s -O tmp' % jp_sub)
            os.system('grep "/subtitle/download?" tmp > tmp2')
            url = open('tmp2').read().strip()
            url = re.findall('"(.*?)"', url)[0]
            url = 'https://subscene.com' + url
            open_new_tab(url)
        time.sleep(4)
        os.system('find ~/Downloads/ -name "*.zip" -exec unzip -o -d ~/Desktop/subs/%s/jp {} \;' % item)
        os.system('find ~/Downloads/ -name "*.rar" -exec unrar x {} ~/Desktop/subs/%s/jp \;' % item)
        time.sleep(2)
        os.system('rm ~/Downloads/*.zip ~/Downloads/*.rar ~/Downloads/*.txt')

        for en_sub in set(en_dict[item]):   # set to rm dups
            os.system('wget %s -O tmp' % en_sub)
            os.system('grep "/subtitle/download?" tmp > tmp2')
            url = open('tmp2').read().strip()
            url = re.findall('"(.*?)"', url)[0]
            url = 'https://subscene.com' + url
            open_new_tab(url)
        time.sleep(4)
        os.system('find ~/Downloads/ -name "*.zip" -exec unzip -o -d ~/Desktop/subs/%s/en {} \;' % item)
        os.system('find ~/Downloads/ -name "*.rar" -exec unrar x {} ~/Desktop/subs/%s/en \;' % item)
        time.sleep(2)
        os.system('rm ~/Downloads/*.zip ~/Downloads/*.rar ~/Downloads/*.txt')
        


except KeyboardInterrupt:
    print 'stopped'

finally:
    # cleanup 
    os.system('rm tmp tmp2 wget-log')
