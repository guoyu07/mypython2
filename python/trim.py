 def trim(s):
   print('原来的值:'+s)
   print('原来的长度:'+str(len(s)))
   while len(s)>0 and s[:1].isspace():
     s=s[1:len(s)]
   while len(s)>0 and s[-1].isspace():
     s=s[0:len(s)-2]
     print('截取后面的空格后:'+s) 
   return s
