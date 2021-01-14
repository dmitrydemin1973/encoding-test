#-*- coding:utf-8 -*-
import sys
a = 'This is a bit русские буквы.'
print ("sys.stdout.encoding",sys.stdout.encoding)
print('Original string:', a)
# Encoding in utf-8
encoded_bytes = a.encode('utf-8', 'replace')
print('Encoded string:', encoded_bytes)


decoded_cp1251 = encoded_bytes.decode('cp1251', 'replace')
decoded_cp866 = encoded_bytes.decode('cp866', 'replace')
decoded_utf8 = encoded_bytes.decode('utf-8', 'replace')

sys.stdout.reconfigure(encoding='cp1251')
print ("sys.stdout.encoding",sys.stdout.encoding)
print('Decoded string: 1251', decoded_cp1251)
sys.stdout.reconfigure(encoding='cp866')
print ("sys.stdout.encoding",sys.stdout.encoding)
print('Decoded string: 866', decoded_cp866)
sys.stdout.reconfigure(encoding='utf-8')
print ("sys.stdout.encoding",sys.stdout.encoding)
print('Decoded string: utf-8', decoded_utf8)


