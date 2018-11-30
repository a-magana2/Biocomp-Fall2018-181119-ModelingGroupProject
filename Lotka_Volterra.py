#Lotka-Volterra Model
import pandas
import scipy
import scipy.integrate as spint
from plotnine import *
def lotkaSim(y,t0,b,H,a,P,e,s):
    H=y[0]
    P=y[1]
    dHdt=((b*H)-(a*P*H))
    dPdt=((e*a*P*H)-(s*P))
    return [dHdt,dPdt]
# Model Simulation- Ideal Parameters
times=range(0,100)
y0=[25,5]
params=(0.5,25,0.02,5,0.1,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()

#Increase b parameter by x4
params=(2,25,0.02,5,0.1,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease b parameter by x2
params=(.25,25,0.02,5,0.1,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase a parameter by x2
params=(0.5,25,0.04,5,0.1,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease a parameter by x2 
params=(0.5,25,0.01,5,0.1,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase e parameter by x2
params=(0.5,25,0.02,5,0.2,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease e parameter by x2
params=(0.5,25,0.02,5,0.05,0.2)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Increase s parameter by x2 
params=(0.5,25,0.02,5,0.1,0.4)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")

#Decrease s parameter by x2
params=(0.5,25,0.02,5,0.1,0.1)
sim=spint.odeint(func=lotkaSim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"t":times,"Herbivore":sim[:,0],"Predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="Herbivore"))+geom_line()+geom_line(simDF,aes(x="t",y="Predator"),color='red')+theme_classic()+xlab("Time")+ylab("Population")
