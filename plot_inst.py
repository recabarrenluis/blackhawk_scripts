import matplotlib.pyplot as plt
import numpy as np
import sys

############ Folder path #################

# Here put the BlackHawk path
BH_path = "/home/lumarev/Downloads/version_finale"
result_folder = BH_path + "/results/"


# List of the 'destination_folder'
data_folders = ['100s_hadrochoice2'] #['10yr_hadrochoice2','5yr_hadrochoice2','1yr_hadrochoice2','3mth_hadrochoice2','1wk_hadrochoice2','1day_hadrochoice2','12h_hadrochoice2','6h_hadrochoice2','3h_hadrochoice2','1h_hadrochoice2','30min_hadrochoice2','10min_hadrochoice2','300s_hadrochoice2','100s_hadrochoice2','50s_hadrochoice2','10s_hadrochoice2','1s_hadrochoice2','0.1s_hadrochoice2','0.01s_hadrochoice2'] # add lifetime name that you are interested
P=[] #path of lifetimes data
for i in range(len(data_folders)):
    f=str(result_folder + data_folders[i] + "/")
    P.append(f)

# Data loading from python program prediction
data_prediction_path= "/media/sf_share/"

############ spectrum data #########################

#data_spectrum = np.genfromtxt(folder+"BH_spectrum.txt", skip_header=2)
#data_primary = np.genfromtxt(folder+"instantaneous_primary_spectra.txt", skip_header=2)
 
#data_secondary = np.genfromtxt( folder+"instantaneous_secondary_spectra.txt", skip_header=2)
#data_prediction = np.loadtxt(data_prediction_path+"data_prediction_file.txt", dtype=int) #datos de prediccion con gas de bosones from Jupyter notebook!

#print(data_spectrum[1,0], np.size(data_spectrum),data_spectrum.shape)

#dim_primary=data_primary.shape
# dim_secondary=np.size(data_secondary)
# print(data_primary,"data_primary.size=",dim_primary)
# print(data_secondary,"data_secondary.size=",dim_secondary)


######################### Put 1 to plot the particle spectrum##################

photon_primary = 1 
gluons_primary = 0 
higgs_primary = 0 
W_primary = 0 
Z_primary = 0 
neutrinos_primary = 1 
electron_primary = 1 
muon_primary = 0 
tau_primary = 0
up_primary = 1 
down_primary = 0 
charm_primary = 0 
strange_primary = 0 
top_primary = 0 
bottom_primary = 0 
graviton_primary = 0 

part_show_primary = np.zeros(16)
part_show_primary = np.array(part_show_primary, int)
part_show_primary[0] = photon_primary
part_show_primary[1] = gluons_primary
part_show_primary[2] = higgs_primary
part_show_primary[3] = W_primary
part_show_primary[4] = Z_primary
part_show_primary[5] = neutrinos_primary
part_show_primary[6] = electron_primary
part_show_primary[7] = muon_primary
part_show_primary[8] = tau_primary
part_show_primary[9] = up_primary
part_show_primary[10] = down_primary
part_show_primary[11] = charm_primary
part_show_primary[12] = strange_primary
part_show_primary[13] = top_primary
part_show_primary[14] = bottom_primary
part_show_primary[15] = graviton_primary

labels_primary = np.array(np.zeros(16), str)
labels_primary[0] = "$\gamma$"
labels_primary[1] = "$g$"
labels_primary[2] = "$h$"
labels_primary[3] = "$W^\pm$"
labels_primary[4] = "$Z^0$"
labels_primary[5] = "$\\nu,\overline{\\nu}$"
labels_primary[6] = "$e^\pm$"
labels_primary[7] = "$\mu^\pm$"
labels_primary[8] = "$\\tau^\pm$"
labels_primary[9] = "$q,\overline{q}$"
labels_primary[10] = "$d,\overline{d}$"
labels_primary[11] = "$c,\overline{c}$"
labels_primary[12] = "$s,\overline{s}$"
labels_primary[13] = "$t,\overline{t}$"
labels_primary[14] = "$b,\overline{b}$"
labels_primary[15] = "${\\rm G}$"

# print(np.size(data_prediction),'DATA size')

# r=float(input('PBH distance from Earth in [pc]= ')) EARTH

#### peak value ####
dataX=[]
dataY=[]
dataYearth=[]
fig=plt.figure(figsize=(7.,4.3), dpi=200)
ax=fig.add_subplot(111)
for j in range(len(data_folders)):
    data_spectrum = np.genfromtxt(P[j]+"BH_spectrum.txt", skip_header=2)
    print(data_spectrum[1],data_folders[j])
    data_primary = np.genfromtxt(
    P[j]+"instantaneous_primary_spectra.txt", skip_header=2)
    M=data_spectrum[1,0]
    flux_max = 0.
    for i in range(16):
        if part_show_primary[i]:
            flux_max = max(flux_max, max(data_primary[:, i+1]))
    #plt.ylim(flux_max/1e+10, flux_max*10.)
    for i in range(16):
        if part_show_primary[i]:
            peak=max(data_primary[:,i+1])
            x=data_primary[:,i+1].argmax()
            E_max=data_primary[x,0]
            #print('peak= ',peak,' E_peak= ',E_max,'GeV ', 'M_BH= ',str(M),'g')
            #np.savetxt(str(data_folders[j])+'X.txt',data_primary[:,0],delimiter=',')
            #np.savetxt(str(data_folders[j])+'Y.txt',data_primary[:,i+1],delimiter=',')
            dataX.append(data_primary[:,0])
            dataY.append(data_primary[:,i+1])
            ############## PLOT ###############
            ax.scatter(data_primary[:, 0],data_primary[:,i+1],s=2,label=labels_primary[i]+'  100 sec. / 1.7 TeV')#+', peak= '+str( peak)+', E_peak= '+str(E_max)+'GeV'+' M_BH= '+str(M)+'g', linewidth=2)
#            ax.text(0.15,0.7,'100 sec. / 1704 [GeV]',horizontalalignment='center',transform=ax.transAxes,fontsize=12) ## by hand
            plt.xscale('log')
            plt.xlim(1e1,1e5)
            ax.set_xlabel('$E{\\rm \,\, [GeV]}$')
            ax.set_ylabel(r'$d\dot{N}\,/\,dE$ [GeV$^{-1}$ s$^{-1}]$')
            plt.title(r'Primary spectrum of photons, electrons, neutrinos and one quark flavor', fontsize=10,y=1.05) #by hand
            print(peak,E_max,labels_primary[i]) 
            ############ PLOT EARTH ##############
            #Y=[]
            #for u in data_primary[:,i+1]:
            #    y=((1.05*10**-27)/(4*np.pi*r**2))*(3.153*10**7)*u # solid angle factor, seconds to yr
            #    Y.append(y)
            ##np.savetxt(str(data_folders[j])+'Yearth.txt',Y,delimiter=',') 
            #dataYearth.append(Y)
            #ax.scatter(data_primary[:, 0], Y, label=labels_primary[i]+', peak= '+str(peak)+', E_peak= '+str(E_max)+'GeV'+'M_BH= '+str(M)+'g', linewidth=2)
            #plt.ylim(0,5*max(Y))
            #plt.xscale('log')
            #ax.set_ylabel(r'$\gamma$ / [GeV yr km$^{2}$]')
            #plt.title('BLACKHAWK-PBH flux on earth at='+str(r)+' [pc]', fontsize=10, y=1.02)
            ##########################################################################################
            plt.grid(b=True)
            plt.legend(loc = 0,prop={'size': 11},facecolor='white',framealpha=1,markerscale=3)
            plt.savefig("primary_spectra.png", dpi=300)
plt.show()
#print(np.shape(dataX))
#print(np.shape(dataY))
#print(np.shape(dataYearth))
np.save('dataX',dataX)
np.save('dataY',dataY)
np.save('dataYearth',dataYearth)



