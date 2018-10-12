from numpy import random
import ROOT
import array
import math
from ROOT import TFile, TTree

#setting parameters
numb = int (input('number of events: '))
rad = float (input('radius: '))
std = float (input('standard deviation: '))
a = float (input('a: '))
b = float (input('b: '))

random.seed(25)
#first random radius
r1 = array.array('d') # set up an empty vector
for i in range(numb): # n numbers
    rr1 = rad + std*random.randn() # normal dist with mean , sd
    r1.append(rr1) # enter xx into vector
r_1 = [float(i) for i in r1]

#first random angle
t1 = array.array('d') # set up an empty vector
for i in range(numb): # n numbers
    tt1 = 2 * math.pi * random.random() # normal dist with mean , sd
    t1.append(tt1) # enter mm into vector
t_1 = [float(i) for i in t1]

#second random radius
r2 = array.array('d') # set up an empty vector
for i in range(numb): # n numbers
    rr2 = rad + std*random.randn() # normal dist with mean , sd
    r2.append(rr2) # enter xx into vector
r_2 = [float(i) for i in r2]

#second random angle
t2 = array.array('d') # set up an empty vector
for i in range(numb): # n numbers
    tt2 = 2 * math.pi * random.random() # normal dist with mean , sd
    t2.append(tt2) # enter mm into vector
t_2 = [float(i) for i in t2]

#defining x for signal
xvec = array.array('d')
for i in range (numb):
    xx = a * r_1[i] * math.cos(t_1[i])*math.cos(math.pi/4)-b * r_1[i] * math.sin(t_1[i])*math.sin(math.pi/4)
    xvec.append(xx)
#x = [float(i) for i in xvec]

#defining y for signal
yvec = array.array('d')
for i in range (numb):
    yy = b * r_1[i] * math.sin(t_1[i])*math.cos(math.pi/4)+a * r_1[i] * math.cos(t_1[i])*math.sin(math.pi/4)
    yvec.append(yy)
#y = [float(i) for i in yvec]

#defining x for background
wvec = array.array('d')
for i in range (numb):
    ww = a * r_2[i] * math.cos(t_2[i])*math.cos(-math.pi/4)-b * r_2[i] * math.sin(t_2[i])*math.sin(-math.pi/4)
    wvec.append(ww)
#w = [float(i) for i in wvec]

#defining y for background
zvec = array.array('d')
for i in range (numb):
    zz = b * r_2[i] * math.sin(t_2[i])*math.cos(-math.pi/4)+a * r_2[i] * math.cos(t_2[i])*math.sin(-math.pi/4)
    zvec.append(zz)
#z = [float(i) for i in zvec]

#array of ones
ones = array.array('d')
for i in range (numb):
    ttt = 1
    ones.append(ttt)

#array of zeros
zeros = array.array('d')
for i in range (numb):
    zzz = 0
    zeros.append(zzz)

f = ROOT.TFile( 'sig_%s_%s_%s.root' %(numb,rad,std), 'recreate' )
tree1 = ROOT.TTree( 't1', 'tree with histos' )


x = array.array ('f', [0.0])
y = array.array ('f', [0.0])
truth = array.array ('f', [0.0])

rsig = array.array ('f', [0.0])
thetasig = array.array ('f', [0.0])


tree1.Branch( 'x', x, 'x_sig/F' )
tree1.Branch( 'y', y, 'y_sig/F' )
tree1.Branch( 'r_sig', rsig, 'r_sig/F' )
tree1.Branch( 'theta_sig', thetasig, 'theta_sig/F' )
tree1.Branch( 'truth', truth, 'truth/F' )

for i in range (len (xvec)):
    x[0]=xvec[i]
    y[0]=yvec[i]
    truth[0] = ones[i]
    rsig[0]=r1[i]
    thetasig[0]=t1[i]
    tree1.Fill()

f.Write()
f.Close()

g = ROOT.TFile( 'bg_%s_%s_%s.root' %(numb,rad,std), 'recreate' )
tree2 = ROOT.TTree( 't2', 'tree with histos' )

x = array.array ('f', [0.0])
y = array.array ('f', [0.0])
truth = array.array ('f', [0.0])

rbg = array.array ('f', [0.0])
thetabg = array.array ('f', [0.0])

tree2.Branch( 'x', x, 'x_bg/F' )
tree2.Branch( 'y', y, 'y_bg/F' )
tree2.Branch( 'r_bg', rbg, 'r_bg/F' )
tree2.Branch( 'theta_bg', thetabg, 'theta_bg/F' )
tree2.Branch( 'truth', truth, 'truth/F' )

for i in range (len (xvec)):
    x[0]=wvec[i]
    y[0]=zvec[i]
    truth[0] = zeros[i]
    rbg[0]=r2[i]
    thetabg[0]=t2[i]
    tree2.Fill()

g.Write()
g.Close()


#plotting with python
'''
plt.plot(xvec, yvec,'g.', label = 'signal')
plt.plot(xvec, zvec,'b.', label = 'background')
#plt.plot(resultx, z,'g^', label = 'background')
#move axis
plt.axes().spines['bottom'].set_position(('data',0))
plt.axes().spines['left'].set_position(('data',0))
plt.grid ()
plt.title('mean_1_std_0.1')
plt.savefig ('mean_1_std_0.1.jpg')
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axis([-5, 5,-5, 5])
plt.show()
'''

#ploting with ROOT
gr = ROOT.TGraph(numb,xvec,yvec)
#gr.GetXaxis().SetRangeUser(-310,310)
#gr.GetYaxis().SetRangeUser(-310,310)
gr.SetTitle("Signal_and_Background_%s_events_rad_%s_std_%s; x; y" %(numb,rad,std))
gr.SetMarkerStyle(6)
gr.SetMarkerColor(2)
bg = ROOT.TGraph(numb,wvec,zvec)
bg.SetMarkerStyle(6)
bg.SetMarkerColor(3)
c = ROOT.TCanvas("test1")
gr.Draw("AP")
bg.Draw("P")
legend = ROOT.TLegend(0.1,0.85,0.3,0.9)
#legend.SetHeader("Signal vs Background","C")
legend.AddEntry(gr,"Signal","p");
legend.AddEntry(bg,"Background","p");
legend.Draw();
c.Print("numb_%s_rad_%s_std_%s.png" %(numb,rad,std))
