import requests
import random

tok = input('توكن⚡ :   ')
print('')
ID = input('ايدي⚡ :    ')
a='qwertyuiopasdfghjklzxcvbnm'
b='1234567890'
length = 1
while True:
   u= ''.join(random.sample(b,length))
   r= ''.join(random.sample(a,length))
   b= ''.join(random.sample(a,length))
   o= ''.join(random.sample(a,length))
   i=''.join(random.sample(a,length))
   AA=(i+o+b+u+r)
   A=(i+r+b+o+u)
   AAA=(i+u+o+b+r)
   AAAA=(i+o+r+b+u)
   AAAAA=(r+i+o+u+b)
   AAAAAA=(i+u+r+o+b)
   AAAAAAA=(i+o+b+u+r)
   AAAAAAAAA=(b+o+i+u+r)
   AHMad = AA , A , AAA , AAAA , AAAAA , AAAAAA , AAAAAAA , AAAAAAAAA
   email = str("".join(random.choice(AHMad)))
   
   tiktok = requests.get('https://ibrahemalkabby.ml/api/TikTok/email.php?email='+email+'@yahoo.com').json()['result']
   
   
   yahoo = requests.get('http://xtools.pythonanywhere.com/Yahoo/Ckeck?Email='+email).json()['status']
   if yahoo == 'Not Available' and tiktok == 'UnAvailable' :
    print('\n\n')
    print('yahoo  \n ---- \n'+email+'@yahoo.com : Not Available \n  \ntiktok \n ---- \n'+email+'@yahoo.com : Not Available')
    print('\n\n\n\n')
   
   
   if yahoo == 'Available' and tiktok == 'Available' :
    print('\n\n')
    print('yahoo  \n ---- \n'+email+'@yahoo.com : Available \n  \ntiktok \n ---- \n'+email+'@yahoo.com : Available')
    print('🟢')
    print('\n\n\n\n')
    requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= متاح ياهو تيك توك\n ---- \nEmail :   قناه @jfihcfib '+email+'@yahoo.com ')
    
    
   if yahoo == 'Not Available' and tiktok == 'Available' :
    print('\n\n')
    print('yahoo  \n ---- \n'+email+'@yahoo.com : Not Available \n \ntiktok \n ---- \n'+email+'@yahoo.com : Available')
    print('\n\n\n\n')
   if yahoo == 'Available' and tiktok == 'Email Not Linked TikTok' :
    print('\n\n')
    print('yahoo  \n ---- \n'+email+'@yahoo.com : Not Available \n \ntiktok \n ---- \n'+email+'@yahoo.com : Not Available')
    print('\n\n\n\n')