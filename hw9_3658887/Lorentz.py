import numpy as np


##############################Definitions of four vector object and its methods
class fourvector():
   def __init__(self, v=np.array([0.0,0.0,0.0,0.0])):
        self.v=1.0*np.array(v)
   def __add__(self,other):
        v=self.v+other.v
        return(fourvector(v))
        ############################# Allows multiplication by scalars
   def __rmul__(self,sc: type(0.0)):
       ##assert(type(sc)==type(0.0))
       v1=sc*self.v
       return fourvector(v1)
   def __sub__(self,other):
        v=self.v-other.v
        return(fourvector(v))
      ########################### How do I represent myself on the commands print
   def __repr__(self):
       return("Fourvector = "+ str(self.v))
   def t(self):
       return(self.v[0])
   def x(self):
       return(self.v[1])
   def y(self):
       return(self.v[2])
   def z(self):
       return(self.v[3])
   def lower(self):
       v=1.0*self.v
       v[1:3]=-v[1:3]
       return(fourvector(v))
   def dot(self,other):
       ip = self.v[0]*other.v[0]-np.dot(self.v[1::],other.v[1::])
       return ip
   def boost(self,boos):
        v= np.dot(boos,self.v)
        return fourvector(v)
   ###################### For something ew might want to know: spacelike, timelike, null. Returns nothing
   def typ(self):
        u=self.dot(self)
        if u>0:
           print("Is timelike")
        elif u<0:
           print("Is spacelike")
        else:
           print("Is null")
 ########################################### Here ends the definition of the obhect
           
           
           
################Finds a boost matrix, given a 3-vector direction and a velocity
def boost(uv, beta):
    if np.abs(beta)>=1:
       print("Not  allowed velocity parameter")
       return
    uw= np.array(uv)
    uw=uw/np.sqrt(np.dot(uw,uw))
    a= np.array(4*[4*[0.0]])
    gamma= 1/(np.sqrt(1-beta**2))
   # print(gamma)
    s=  np.array(3*[3*[0.0]])
    for i in range(3):
          s[i,i]=1
    coshs= gamma
    sinhs= beta*gamma
   # print(coshs,sinhs)
    for i in range(3):
       for j in range(3):
           s[i,j]+=-uw[i]*uw[j]+coshs*uw[i]*uw[j]
    #print(s)
    a[0:3,0:3]=s[0:3,0:3]
    a[0:3,3]=sinhs*uw[0:3]
    a[3,0:3]=sinhs*uw[0:3]
    a[3,3]=coshs
    boo_mat=0.0*a
    for i in range(4):
      for j in range(4):
         boo_mat[i,j]= a[(i-1)%4,(j-1)%4]
  #  print(a)
    return boo_mat
    
#################### Shortcut for inverse lorentz transformation
def inv(B):
   return( np.linalg.inv(B))


######################Finds a boost to a "center of mass frame" of a particle
def CM(u):
   s=u.v[1:]
   w=u.t()
   dir= s/w
   bet= - np.sqrt(np.dot(dir,dir))
   return boost(dir,bet)
