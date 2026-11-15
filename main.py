import os,json,urllib.request as u
V=[0,100,320,330,500,900]
Z='k'*32
P=['kkkkuuuummoqllmpkkkoljiklmmgkkkk','aceecgkkekmnelnoeknoelmncgklacee','giiiikkkiklmillmikmmimmmilkkgiii',Z,Z,'eccaeccaeccaeccageecigggookkoqmk']
W=[[(V[t:=p%6]+(ord(P[t-1][(7-(i>>4)if p<7 else i>>4)*4+min(i&7,7-(i&7))])-107)*5)*(1 if p<7 else-1)for i in range(128)]for p in range(13)]
D8=(1,-1,16,-16,15,-15,17,-17)
DR=[(),(),(-33,-31,-18,-14,14,18,31,33),D8[4:],D8[:4],D8,(-17,-16,-15,-1,1,15,16,17)]
Q4=(5,4,3,2)
T={};N=0;L=90000
def A(b,s,w):
 for D,y in(((-15,-17)if w else(15,17),1),(DR[2],2),(DR[6],6)):
  if any(not(s+d)&136 and b[s+d]==(y if w else y+6)for d in D):return 1
 for d in DR[5]:
  q=s+d
  while not q&136 and not b[q]:q+=d
  if not q&136:
   p=b[q];y=p%6
   if(p>6)!=w and(y==5 or y==(4 if abs(d)in(1,16) else 3)):return 1
 return 0
def J(b,w):
 return b.index(6+6*(not w))
def G(b,w,c,e,C):
 m=[]
 for s,p in enumerate(b):
  if not p or s&136 or(p>6)==w:continue
  y=p%6 or 6
  if y==1:
   d=16 if w else-16;r=s>>4;q=s+d;u=r==6 if w else r==1
   if not b[q]:
    if u:m+=[s|q<<7|z<<14 for z in Q4]
    elif not C:
     m.append(s|q<<7)
     if(r==1 if w else r==6) and not b[s+d*2]:m.append(s|(s+d*2)<<7)
   for q in(s+d-1,s+d+1):
    if q&136:continue
    v=b[q]
    if(v and(v>6)==w)or q==e:
     if u:m+=[s|q<<7|z<<14 for z in Q4]
     else:m.append(s|q<<7)
  else:
   for d in DR[y]:
    q=s+d
    while not q&136:
     v=b[q]
     if(not v and not C)or(v and(v>6)==w):m.append(s|q<<7)
     if v or y in(2,6):break
     q+=d
 if not C and not A(b,k:=4 if w else 116,not w):
  for j in(1,-1):
   if c&(1 if w else 4)<<(j<0) and not b[k+j] and not b[k+2*j] and(j>0 or not b[k-3])and all(not A(b,k+x,not w)for x in(j,2*j)):m.append(k|(k+2*j)<<7)
 return m
def M(b,w,c,e,m):
 n=b[:];f=m&127;t=m>>7&127;z=m>>14;p=n[f];y=p%6 or 6;n[f]=0
 if y==1 and t==e:n[t-16+32*(not w)]=0
 if y==6 and abs(t-f)==2:n[(f+t)//2]=n[r:=f+3 if t>f else f-4];n[r]=0
 n[t]=p if not z else z+6-6*w
 if y==6:c&=12 if w else 3
 for q in(f,t):c&=~((1<<(q//56+(not q%8)))if q in(0,7,112,119)else 0)
 return n,not w,c,(f+t)//2 if y==1 and abs(t-f)==32 else-1
def E(b,w):
 return sum(W[p][i]for i,p in enumerate(b)if p and not i&136)*(1 if w else-1)
def S(b,w,c,e,d,a,B,pl):
 global N;N+=1
 if N>L:return 0
 k=tuple(b);t0=T.get(k,0)
 if d<=0:
  s=E(b,w)
  if s>=B or pl>48:return s
  if s>a:a=s
  ms=G(b,w,c,e,0 if A(b,J(b,w),not w) else 1)
  ms.sort(key=lambda m:-V[b[m>>7&127]%6])
  for m in ms:
   if A((nb:=M(b,w,c,e,m))[0],J(nb[0],w),not w):continue
   sc=-S(*nb,0,-B,-a,pl+1)
   if sc>=B:return B
   if sc>a:a=sc
  return a
 ic=A(b,J(b,w),not w)
 if d>=3 and not ic and E(b,w)>=B and-S(b,not w,c,-1,d-3,-B,-B+1,pl+1)>=B:return B
 ms=G(b,w,c,e,0)
 ms.sort(key=lambda m:-(9**7 if m==t0 else V[b[m>>7&127]%6]))
 be=bm=-9**7
 for m in ms:
  if A((nb:=M(b,w,c,e,m))[0],J(nb[0],w),not w):continue
  sc=-S(*nb,d-1,-B,-a,pl+1)
  if sc>be:be=sc;bm=m
  if sc>a:a=sc
  if a>=B:break
 if bm<0:return-99999+pl if ic else 0
 T[k]=bm
 return be
def F(s):
 b=[0]*128;p=s.split();r=7;f=0
 for ch in p[0]:
  if ch=='/':r-=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:b[r*16+f]='PNBRQKpnbrqk'.index(ch)+1;f+=1
 w=p[1]=='w';c=sum(1<<'KQkq'.index(ch)for ch in p[2]if ch in'KQkq')
 e=(int(p[3][1])-1)*16+ord(p[3][0])-97 if p[3][1:]else-1
 return b,w,c,e
def R(b,w,c,e):
 global N
 lm=[m for m in G(b,w,c,e,0)if not A((nb:=M(b,w,c,e,m))[0],J(nb[0],w),not w)]
 be=0;N=0
 for d in range(8):
  a=bs=-9**7;bb=0
  for m in lm:
   sc=-S(*M(b,w,c,e,m),d,-9**7,-a,1)
   if sc>bs:bs=sc;bb=m
   if sc>a:a=sc
  if N>L:break
  be=bb
  lm.remove(bb);lm.insert(0,bb)
 return be or lm[0]
def PO(p,d):
 try:return json.load(u.urlopen(os.getenv('MAKEFUN_ENV_URL')+p,json.dumps(d).encode()))
 except Exception:return{}
while(g:=PO('/game',{}))and g['status']!='done':
 while g['status']=='your_move':
  b,w,c,e=F(g['fen']);mv=R(b,w,c,e)
  s=''.join(chr(97+(x&7))+str((x>>4)+1)for x in(mv&127,mv>>7&127))+('nbrq'[(mv>>14)-2] if mv>>14 else'')
  l=g['legal_moves']
  if s not in l:s=l[0]
  g=PO('/move',{'game':g['game'],'move':s})
  if not g:break
