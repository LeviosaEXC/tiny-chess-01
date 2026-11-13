import json,os,urllib.request as u
V=(0,20,64,66,100,180,0)
Y=[ord(c)-75 for c in"KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKKACEECGKLELMNEKNOELNOEKMNCGKKACEEGIIIILKKIMMMIKMMILLMIKLMIKKKGIIIOQMKOOKKIGGGGEECECCAECCAECCAECCA"]
N=(-21,-19,-12,-8,8,12,19,21);D=(-11,-9,9,11);R=(-10,-1,1,10);I=D+R;T=((N,2),(I,6));Q=((D,3),(R,4))
C=[15]*120;C[25]=12;C[95]=3;C[28],C[21],C[98],C[91]=14,13,11,7
M=2e4;L=5e4;O=[0];H={};J=[0]*64;U=os.getenv('MAKEFUN_ENV_URL')
X=Exception
def Z():
 O[0]+=1
 if O[0]>L:raise X
def A(b,k,s):
 o=6*s;u=1-2*s
 if b[k-9*u]==1+o or b[k-11*u]==1+o:return 1
 for E,P in T:
  for d in E:
   if b[k+d]==P+o:return 1
 for E,P in Q:
  for d in E:
   j=k+d
   while b[j]==0:j+=d
   if b[j]==P+o or b[j]==5+o:return 1
 return 0
def g(b,s,c,e,k):
 W=10-20*s;w=9-7*s;m=[]
 def P(i,j):m.extend((i,j,q+6*s)for q in(5,4,3,2))if j//10==w else m.append((i,j,0))
 for i,p in enumerate(b):
  if p%13==0 or(p>6)^s:continue
  t=(p-1)%6+1
  if t==1:
   j=i+W
   if b[j]==0:
    P(i,j)
    if i//10==3+5*s and b[i+2*W]==0:m.append((i,i+2*W,0))
   for d in(W-1,W+1):
    j=i+d;v=b[j]
    if j==e or v%13 and(v>6)^s:P(i,j)
  elif t==2 or t==6:
   for d in(I,N)[t==2]:
    j=i+d;v=b[j]
    if v==0 or v<13 and(v>6)^s:m.append((i,j,0))
   if t==6:
    B0=25+70*s
    for a,f,u,v,r in((3,2,1,1,1),(-4,-2,-1,-3,2)):
     if i==B0 and c&r<<2*s and b[B0+a]==4+6*s and b[B0+u]==b[B0+f]==b[B0+v]==0 and not any(A(b,B0+z,1-s)for z in(0,u,f)):m.append((B0,B0+f,0))
  else:
   for d in(D,R,I)[t-3]:
    j=i+d
    while b[j]==0:m.append((i,j,0));j+=d
    v=b[j]
    if v<13 and(v>6)^s:m.append((i,j,0))
 o=[]
 for f,t,pr in m:
  if k and not(pr or b[t]or t==e):continue
  nb=b[:];p=nb[f];q=(p-1)%6;nb[f]=0;nb[t]=pr or p
  if q==0 and t==e and b[t]==0:nb[t-10+20*s]=0
  if q==5 and abs(t-f)==2:x,y=(t+1,t-1)if t>f else(t-2,t+1);nb[y]=nb[x];nb[x]=0
  if not A(nb,nb.index(6+6*s),1-s):o.append((f,t,pr,nb,c&C[f]&C[t],(f+t)//2*(q==0 and abs(t-f)==20)))
 return o
def E(b,s):
 c=0;x=0;y=0
 for i,p in enumerate(b):
  if p%13==0:continue
  t=(p-1)%6+1
  if t>5:x,y=(i,y)if p<7 else(x,i);continue
  r=i//10-2;f=i%10-1;h=min(f,7-f)
  v=V[t]+(Y[t*32-32+(r if p<7 else 7-r)*4+h]if t<4 else 0)
  c+=v if p<7 else-v
 for k,z in((x,1),(y,-1)):
  r=k//10-2;f=k%10-1;h=min(f,7-f)
  c+=z*Y[96+(r if z>0 else 7-r)*4+h]
 return c*(1-2*s)
def o(m,b,tt,y,e):
 m.sort(key=lambda n:-(1e6 if n[:3]==tt else(10*V[(b[n[1]]-1)%6+1]-V[(b[n[0]]-1)%6+1]if b[n[1]]else 1000*(n[1]==e)+500*(n[:3]==J[y]))+9000*(n[2]>0)))
def S(b,s,c,e,d,a,w,y):
 Z()
 if d>0:
  K=tuple(b),s,c,e;z=H.get(K,(0,0,0,None));tt=z[3]
  if z[0]>=d and(z[2]==0 or z[2]==1 and z[1]>=w or z[2]==2 and z[1]<=a):return z[1]
  m=g(b,s,c,e,0)
  if not m:return(-M+y)*A(b,b.index(6+6*s),1-s)
  o(m,b,tt,y,e);j=a;r=-M;n=None
 else:
  if d<-7:return E(b,s)
  h=A(b,b.index(6+6*s),1-s);m=g(b,s,c,e,not h)
  if h and not m:return-M+y
  if not h and(a:=max(a,E(b,s)))>=w:return w
  o(m,b,None,y,e);r=a
 for f,t,pr,nb,nc,ne in m:
  v=-S(nb,1-s,nc,ne,d-1,-w,-a,y+1)
  if v>r:r,a,n=v,max(a,v),(f,t,pr)
  if a>=w:
   if d>0 and not(b[t]or pr or t==e):J[y]=n
   break
 if d>0:H[K]=(d,r,(r>=w)+2*(r<=j),n)
 return r
def v(m):f,t,pr=m;return'%c%d%c%d'%(96+f%10,f//10-1,96+t%10,t//10-1)+'nbrq'[pr%6-2]*(pr>0)
def p(x):
 w=x.split()
 b=[13]*120
 for r in range(8):b[r*10+21:r*10+29]=[0]*8
 i=91
 for h in w[0]:
  if h=='/':i-=18
  elif h<'9':i+=int(h)
  else:b[i]='PNBRQKpnbrqk'.index(h)+1;i+=1
 s=w[1]=='b'
 c=0
 for h in'qkQK':c=2*c+(h in w[2])
 e=(int(w[3][1])+1)*10+ord(w[3][0])-96 if w[3]!='-'else 0
 return b,s,c,e
def k(b,s,c,e,l):
 O[0]=0;H.clear();m=g(b,s,c,e,0);z=None;o(m,b,None,0,e)
 for d in range(39):
  try:
   r=a=-M;n=None
   for f,t,pr,nb,nc,ne in m:
    w=-S(nb,1-s,nc,ne,d,-M,-a,1)
    if w>r:r=a=w;n=(f,t,pr)
  except X:break
  z=n
  if r>M-200:break
 return v(z)if z and v(z)in l else l[0]
def w(p,o):return json.load(u.urlopen(u.Request(U+p,json.dumps(o).encode())))
def main():
 while(G:=w('/game',{}))['status']>'done':
  while G['status']=='your_move':
   b,s,c,e=p(G['fen'])
   G=w('/move',{'game':G['game'],'move':k(b,s,c,e,G['legal_moves'])})
main()
