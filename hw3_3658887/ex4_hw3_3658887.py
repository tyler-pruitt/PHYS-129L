import random
import matplotlib.pyplot as plt


################# Here is a function that uses random number to make a radioactive particle decay
def decay(p):
    u=random.random()
    if u< p:
       return -1
    else:
       return 0


###### This is a set of variables that is useful later on when we plot. It is initialized before anything is
#####computed.
styles=('ro','b^', 'gs', 'bo','go','r^',)

An_tot= int (input("Input the total number of A particles  "))
Bn_tot= int (input("Input the total number of B particles  "))
Cn_tot= int (input("Input the total number of C particles  "))
Dn_tot= int (input("Input the total number of D particles  "))


##### We will repeat the experiment to see how random numbers produce statistcail outcomes
n_runs= int (input("Input the total number of runs"))

####### This is the main parameter we tweak. It describes the chance of an individul particle decays.
##########    Large probabilities, fast decay.

probA2B = float(input("input a probability of decay for process A -> B in 1 unit of time (needs to be less than 1)  "))
probB2C = float(input("input a probability of decay for process B -> C in 1 unit of time (needs to be less than 1)  "))
probC2D = float(input("input a probability of decay for process C -> D in 1 unit of time (needs to be less than 1)  "))


##### here we have a loop to repeat our experiment
for runs in range(n_runs):
    ######### For each run, we initialize
    particles = An_tot*[3] + Bn_tot*[2] + Cn_tot*[1] + Dn_tot*[0]
    u3 = [An_tot]
    u2 = [Bn_tot]
    u1 = [Cn_tot]
    u0 = [Dn_tot]
    
    ########### The while condition checks if any particle is still not decayed
    
    while any(particles):
    
     for i in range(len(particles)):
         ####### Here we check if the i-th particle particle is not decayed yet
         if particles[i]==3:
             ####### Here we are chaning particle one to 0 if particle decays (final end product)
            particles[i]= particles[i]+decay(probA2B)
         elif particles[i]==2:
             ####### Here we are chaning particle one to 0 if particle decays (final end product)
            particles[i]= particles[i]+decay(probB2C)
         elif particles[i]==1:
             ####### Here we are chaning particle one to 0 if particle decays (final end product)
            particles[i]= particles[i]+decay(probC2D)
     u3+=[ particles.count(3)]
     u2+=[ particles.count(2)]
     u1+=[ particles.count(1)]
     u0+=[ particles.count(0)]

############### This shows the raw data for an individual run. The numbers don't help too much
    print('')
    print('A data:', u3)
    print('')
    print('B data:', u2)
    print('')
    print('C data:', u1)
    print('')
    print('D data:', u0)
################## this makes a list of times
    timetot= list(range(len(u3)))
################### We are adding points to the plot
    plt.plot(timetot,u3, styles[runs], color='red')
    plt.plot(timetot,u2, styles[runs], color='blue')
    plt.plot(timetot,u1, styles[runs], color='orange')
    plt.plot(timetot,u0, styles[runs], color='yellow')
#################### This adds lines connecting points to the plot
    plt.plot(u3)
    plt.plot(u2)
    plt.plot(u1)
    plt.plot(u0)

############# Before displaying everything, label the x axis and the y axis.
plt.ylabel("Number of particles")
plt.xlabel("time")
plt.legend(labels=('A','B','C','D'))
plt.title(label=('p =', probA2B, probB2C, probC2D))

############## We finally show the plot.

input("When ready to see plot press enter")
plt.show()


