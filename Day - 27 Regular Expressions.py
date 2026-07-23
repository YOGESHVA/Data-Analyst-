#Regular Expression(Regex)
---------------------------
--->regex is an sequence of char that can searching patter
--->to use regex we have import re module....
Functions()
1)findall
----------
--->It will find all the char that are in the string.
Eg:-
import re
txt = 'python is a language and also called dynamically typed'
print(re.findall('[a]',txt))

2)search()
import re
txt = 'python is a language and also called dynamically typed'
print(re.search('[a]',txt))

3)split()
Eg:
import re
txt = 'python is a language and also called dynamically typed'
print(re.split(' ',txt))

4)Sub()
----------
Eg:
import re
txt = 'python is a language and also called dynamically typed'
print(re.sub(' ','&',txt))

5)fullmatch()


 Metchar
----------
 []
-----
-->
txt = 'I have 100 Rupee'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))
--------------------------------
-->^
Eg:
import re
txt = 'I have 100 Rupee'
print(re.findall('^I have',txt))
print(re.search('^I have',txt))
--------------------------------
$
Eg:
import re
txt = 'I am going to school'
print(re.findall('school$',txt))
print(re.search('school$',txt))
-------------------------------
-->.
import re
txt = 'Hello! This is Manoj'
print(re.findall('T...',txt))
print(re.search('T...',txt))
-------------------------------
*
Eg:-
import re
txt = 'python module will going complete this week'
print(re.findall('p.*',txt))
print(re.findall('p.n*',txt))
print(re.findall('p.*ython',txt))
print(re.search('p.*n',txt))
------------------------------
+
Eg:
import re
txt = 'python is a language'
print(re.findall('p.+n',txt))
print(re.search('p.+n',txt))
-----------------------------
{}
Eg:-
import re
txt = 'python is a language'
print(re.findall('p.{10}',txt))
print(re.search('p.{10}',txt))
-------------------------------------









      
