def chr_before_wrds(chr, list):
    x=[]
    for i in list:
        x.append(chr+i)
    return x

def alph(w):
  m =list(w)
  m.sort()
  return ''.join(m)

def remove_aindexfromb(a,b):
    b = list(b)
    del b[a]
    oy= "".join(b)
    return oy

def degn(a):
    l=[]
    al = alph(a)
    n1=-1
    for i in al:
      n1+=1
      m1 = remove_aindexfromb(n1,al)
      x1 = m1
      x2 = m1[::-1]
      f_ = [i+x1, i+x2]
      l+=f_
    return l

def pr(lis, mark):
  m=0
  for i in lis:
    m+=1
    if i==mark:
      print(m, i,' <----Over here')
    else:
      print(m,i)

def funcher(func):
  def funched(a):
    al2 = alph(a)
    m=-1
    fi = []
    for i in al2:
      m+=1
      x=remove_aindexfromb(m,al2)
      l= func(x)
      li = chr_before_wrds(i,l)
      fi+=li
    return fi
  return funched

def eliminator(lis):
  d= []
  for i in lis:
    if i in d:
      continue
    elif i not in d:
      d.append(i)
  return d

def dis_check(a):
  h =[]
  for i in a:
    if i in h:
      t=False
      break
    else:
      h+=[i]
  else:
    t= True
  return t

wrd = input('Enter the word:')
n =len(wrd)

for i in range(4,n+1):
  degn = funcher(degn)

if dis_check(wrd):
  pr(degn(wrd),wrd)
else:
  pr(eliminator(degn(wrd)),wrd)
