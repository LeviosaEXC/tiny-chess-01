import json,os
from urllib.request import*
V=(0,20,64,66,100,180,0)
Y=[ord(c)-75 for c in"KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKKACEECGKLELMNEKNOELNOEKMNCGKKACEEGIIIILKKIMMMIKMMILLMIKLMIKKKGIIIKKKLJKKKJKKKJKKKJKKKJKKKLMMMKKKKGIIJIKLKILLLKKLLJKLLIKLLIKKKGIIJOQMKOOKKIGGGGEECECCAECCAECCAECCAAEEEEEKKEIOQEIQSEIQSEIOQEGIKACEG"]
N=(-21,-19,-12,-8,8,12,19,21);D=(-11,-9,9,11);R=(-10,-1,1,10);I=D+R
C=[15]*120;C[25]=12;C[28]=14;C[21]=13;C[95]=3;C[98]=11;C[91]=7
M=20000;L=60000;O=[0];H={};J=[0]*64;U=os.getenv('MAKEFUN_ENV_URL')
X=Exception
def Z():
 O[0]+=1
 if O[0]>L:raise X
def A(b,k,s):
 o=6*s;u=1-2*s
 if b[k-9*u]==1+o or b[k-11*u]==1+o:return 1
 for d in N:
  if b[k+d]==2+o:return 1
 for d in I:
  if b[k+d]==6+o:return 1
 for d in D:
  j=k+d
  while b[j]==0:j+=d
  if b[j]==3+o or b[j]==5+o:return 1
 for d in R:
  j=k+d
  while b[j]==0:j+=d
  if b[j]==4+o or b[j]==5+o:return 1
 return 0
def g(b,s,c,e,k):
 m=[]
 for i,p in enumerate(b):
  if p%13==0 or(p>6)!=s:continue
  t=(p-1)%6+1
  if t==1:
   W=10-20*s;w=9-7*s;j=i+W
   if b[j]==0:
    if j//10==w:m+=[(i,j,q+6*s)for q in(5,4,3,2)]
    else:
     m.append((i,j,0))
     if i//10==3+5*s and b[i+2*W]==0:m.append((i,i+2*W,0))
   for d in(W-1,W+1):
    j=i+d;v=b[j]
    if j==e or v%13 and(v>6)!=s:
     if j//10==w:m+=[(i,j,q+6*s)for q in(5,4,3,2)]
     else:m.append((i,j,0))
  elif t==2 or t==6:
   for d in(I,N)[t==2]:
    j=i+d;v=b[j]
    if v==0 or v<13 and(v>6)!=s:m.append((i,j,0))
   if t==6:
    B0=25+70*s
    for a,f,u,v,w in((3,2,1,1,1),(-4,-2,-1,-3,2)):
     if i==B0 and c&w<<2*s and b[B0+a]==4+6*s and b[B0+u]==b[B0+f]==b[B0+v]==0 and not any(A(b,B0+z,1-s)for z in(0,u,f)):m.append((B0,B0+f,0))
  else:
   for d in(D,R,I)[t-3]:
    j=i+d
    while b[j]==0:m.append((i,j,0));j+=d
    v=b[j]
    if v<13 and(v>6)!=s:m.append((i,j,0))
 o=[]
 for f,t,pr in m:
  if k and not(pr or b[t]or t==e):continue
  nb=b[:];p=nb[f];q=(p-1)%6;nb[f]=0;nb[t]=pr or p
  if q==0 and t==e and b[t]==0:nb[t-10+20*s]=0
  if q==5 and abs(t-f)==2:x,y=(t+1,t-1)if t>f else(t-2,t+1);nb[y]=nb[x];nb[x]=0
  if not A(nb,nb.index(6+6*s),1-s):o.append((f,t,pr,nb,c&C[f]&C[t],(f+t)//2*(q==0 and abs(t-f)==20)))
 return o
def E(b,s):
 c=0;q=0;x=0;y=0
 for i,p in enumerate(b):
  if p%13==0:continue
  t=(p-1)%6+1
  if t>5:x,y=(i,y)if p<7 else(x,i);continue
  q+=t==5
  r=i//10-2;f=i%10-1;h=min(f,7-f)
  v=V[t]+Y[(t-1)*32+(r if p<7 else 7-r)*4+h]
  c+=v if p<7 else-v
 u=(6-(q>0))*32
 for k,z in((x,1),(y,-1)):
  r=k//10-2;f=k%10-1;h=min(f,7-f)
  c+=z*Y[u+(r if z>0 else 7-r)*4+h]
 return c*(1-2*s)
def o(m,b,tt,y,e):
 m.sort(key=lambda n:-(1e6 if n[:3]==tt else(10*V[(b[n[1]]-1)%6+1]-V[(b[n[0]]-1)%6+1]if b[n[1]]else 1000 if n[1]==e else 500 if n[:3]==J[y]else 0)+9000*(n[2]>0)))
def Q(b,s,c,e,a,w,y,q):
 Z()
 if q<=0:return E(b,s)
 h=A(b,b.index(6+6*s),1-s);m=g(b,s,c,e,not h)
 if h:
  if not m:return-M+y
 else:
  a=max(a,E(b,s))
  if a>=w:return w
 o(m,b,None,y,e)
 for f,t,pr,nb,nc,ne in m:
  v=-Q(nb,1-s,nc,ne,-w,-a,y+1,q-1)
  if v>a:a=v
  if a>=w:return w
 return a
def S(b,s,c,e,d,a,w,y):
 Z()
 if d==0:return Q(b,s,c,e,a,w,y,8)
 K=tuple(b),s,c,e;z=H.get(K,(0,0,0,None));tt=z[3]
 if z[0]>=d and(z[2]==0 or z[2]==1 and z[1]>=w or z[2]==2 and z[1]<=a):return z[1]
 m=g(b,s,c,e,0)
 if not m:return(-M+y)*A(b,b.index(6+6*s),1-s)
 o(m,b,tt,y,e)
 j=a;r=-M;n=None
 for f,t,pr,nb,nc,ne in m:
  v=-S(nb,1-s,nc,ne,d-1,-w,-a,y+1)
  if v>r:r,a,n=v,max(a,v),(f,t,pr)
  if a>=w:
   if not(b[t]or pr or t==e):J[y]=n
   break
 H[K]=(d,r,(r>=w)+2*(r<=j),n)
 return r
def v(m):f,t,pr=m;return f'{chr(96+f%10)}{f//10-1}{chr(96+t%10)}{t//10-1}'+('nbrq'[pr%6-2]if pr else'')
def p(x):
 w=x.split()
 b=[13]*120
 for r in range(2,10):b[r*10+1:r*10+9]=[0]*8
 i=91
 for h in w[0]:
  if h=='/':i-=18
  elif h<'9':i+=int(h)
  else:b[i]='PNBRQKpnbrqk'.index(h)+1;i+=1
 s=w[1]=='b'
 c=sum(1<<i for i,h in enumerate('KQkq')if h in w[2])
 e=(int(w[3][1])+1)*10+ord(w[3][0])-96 if w[3]!='-'else 0
 return b,s,c,e
def k(b,s,c,e,l):
 O[0]=0;H.clear();m=g(b,s,c,e,0);z=None
 for d in range(1,40):
  try:
   o(m,b,z,0,e)
   r=a=-M;n=None
   for f,t,pr,nb,nc,ne in m:
    w=-S(nb,1-s,nc,ne,d-1,-M,-a,1)
    if w>r:r=a=w;n=(f,t,pr)
  except X:break
  z=n
  if r>M-200:break
 return v(z)if z and v(z)in l else l[0]
def w(p,o):return json.load(urlopen(Request(U+p,data=json.dumps(o).encode())))
def main():
 while(G:=w('/game',{}))['status']!='done':
  while G['status']=='your_move':
   b,s,c,e=p(G['fen'])
   G=w('/move',{'game':G['game'],'move':k(b,s,c,e,G['legal_moves'])})
if __name__=='__main__':main()
