import matplotlib.pyplot as plt
import numpy as np
import sys

############ Folder path #################

# Here put the BlackHawk path
BH_path = "/home/lumarev/Downloads/version_finale"
result_folder = BH_path + "/results/"


data_folders =['100s_hadrochoice2','10s_hadrochoice2','1s_hadrochoice2','0.1s_hadrochoice2','0.01s_hadrochoice2'] #['10yr_hadrochoice2','5yr_hadrochoice2','1yr_hadrochoice2','3mth_hadrochoice2','1wk_hadrochoice2','1day_hadrochoice2','12h_hadrochoice2','6h_hadrochoice2','3h_hadrochoice2','1h_hadrochoice2','30min_hadrochoice2','10min_hadrochoice2','300s_hadrochoice2','100s_hadrochoice2','50s_hadrochoice2','10s_hadrochoice2','1s_hadrochoice2','0.1s_hadrochoice2','0.01s_hadrochoice2']

# ['10yr','5yr','1yr','3mth','1wk','1day','12h','6h','3h','1h','30min','10min','300s','100s','50s','10s','1s','0.1s','0.01s']# add lifetime name that you are interested


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


######################### Put 1 to plot the particle spectrum ##################

epoch = 1 # 0: BBN epoch, 1: present epoch

if epoch == 0:
    nb_fin_part = 11

    # Put 1 to plot the particle spectrum
    photon_secondary=1
    electron_secondary=0
    muon_secondary=0
    nu_e_secondary=0
    nu_mu_secondary=0
    nu_tau_secondary=0
    pipm_secondary=0
    K0L_secondary=0
    Kpm_secondary=0
    proton_secondary=0
    neutron_secondary=0

    part_show_secondary=np.zeros(nb_fin_part)
    part_show_secondary=np.array(part_show_secondary,int)
    part_show_secondary[0] = photon_secondary
    part_show_secondary[1] = electron_secondary
    part_show_secondary[2] = muon_secondary
    part_show_secondary[3] = nu_e_secondary
    part_show_secondary[4] = nu_mu_secondary
    part_show_secondary[5] = nu_tau_secondary
    part_show_secondary[6] = pipm_secondary
    part_show_secondary[7] = K0L_secondary
    part_show_secondary[8] = Kpm_secondary
    part_show_secondary[9] = proton_secondary
    part_show_secondary[10] = neutron_secondary

    labels_secondary=np.array(np.zeros(nb_fin_part),str)
    labels_secondary[0]="$\gamma$"
    labels_secondary[1]="$e^\pm$"
    labels_secondary[2]="$\mu^\pm$"
    labels_secondary[3]="$\\nu_e,\overline{\\nu}_e$"
    labels_secondary[4]="$\\nu_\mu,\overline{\\nu}_\mu$"
    labels_secondary[5]="$\\nu_\\tau,\overline{\\nu}_\\tau$"
    labels_secondary[6]="$\pi^\pm$"
    labels_secondary[7]="$K_{\\rm L}^0$"
    labels_secondary[8]="$K^\pm$"
    labels_secondary[9]="${\\rm p},\overline{\\rm p}$"
    labels_secondary[10]="${\\rm n},\overline{\\rm n}$"
elif epoch == 1:
    nb_fin_part = 6

    photon_secondary=0
    electron_secondary=0
    nu_e_secondary=0
    nu_mu_secondary=0
    nu_tau_secondary=0
    proton_secondary=1

    part_show_secondary=np.zeros(nb_fin_part)
    part_show_secondary=np.array(part_show_secondary,int)
    part_show_secondary[0] = photon_secondary
    part_show_secondary[1] = electron_secondary
    part_show_secondary[2] = nu_e_secondary
    part_show_secondary[3] = nu_mu_secondary
    part_show_secondary[4] = nu_tau_secondary
    part_show_secondary[5] = proton_secondary

    labels_secondary=np.array(np.zeros(nb_fin_part),str)
    labels_secondary[0]="$\gamma$"
    labels_secondary[1]="$e^\pm$"
    labels_secondary[2]="$\\nu_e,\overline{\\nu}_e$"
    labels_secondary[3]="$\\nu_\mu,\overline{\\nu}_\mu$"
    labels_secondary[4]="$\\nu_\\tau,\overline{\\nu}_\\tau$"
    labels_secondary[5]="${\\rm p},\overline{\\rm p}$"


#print(np.size(data_prediction),'DATA size')

r=float(input('PBH distance from Earth in [pc]= '))

#### peak value ####
dataX=[]
dataY=[]
dataYearth=[]
fig=plt.figure(figsize=(8.0,4.0), dpi=200)
ax=fig.add_subplot(111)


#kTforlegends=[]
#with open('temperatures.txt','r') as filehandle:
#    for line in filehandle:
#        current=line[:-1]
#        kTforlegends.append(current)

lifetime_leg=['100 sec.','10 sec.','1 sec.','0.1 sec.','0.01 sec.'] #by hand
kT_leg=['1.7 TeV','3.7 TeV','8 TeV','17 TeV','37 TeV']

for j in range(len(data_folders)):
    data_spectrum = np.genfromtxt(P[j]+"BH_spectrum.txt", skip_header=2)
    data_secondary = np.genfromtxt(
    P[j]+"instantaneous_secondary_spectra.txt", skip_header=2)
    #M=data_spectrum[1,0]
    for i in range(nb_fin_part):
        if part_show_secondary[i]:
            dataX.append(data_secondary[:,0])
            dataY.append(data_secondary[:,i+1])

            peak=max(data_secondary[:,i+1])
            x=data_secondary[:,i+1].argmax()
            E_max=data_secondary[x,0]
            print('peak= ',peak,' E_peak= ',E_max,'GeV ', 'M_BH= ',str(data_spectrum[1,0]),'g')

            ax.scatter(data_secondary[:,0],data_secondary[:,i+1],s=2.5,label=lifetime_leg[j]+' / '+kT_leg[j]) # s=2, label=' M_BH= '+str(data_spectrum[1,0])+'g / '+data_folders[j],linewidth=2) #labels_secondary[i]+', peak= '+str( peak)+', E_peak= '+str(E_max)+'GeV'+' M_BH= '+str(data_spectrum[1,0])+'g', linewidth=2)
            plt.xscale('log')
            plt.yscale('log')
            plt.ylim(1e10,1e35)
            plt.xlim(5e-1,3e5)
            ax.set_xlabel('$E {\\rm \,\, [GeV]}$')
            ax.set_ylabel(r'$d\dot{N}_{p^{+}}\,/\,dE\;$ [GeV$^{-1}$ s$^{-1}$]')
            plt.title('Proton spectrum from PBH evaporation obtained with BlackHawk', fontsize=12)

            ############ PLOT EARTH ##############
            #Y=[]
            #for u in data_secondary[:,i+1]:
            #    y=((1.05*10**-27)/(4*np.pi*r**2))*(3.153*10**7)*u # solid angle factor, seconds to yr
            #    Y.append(y)
            #dataYearth.append(Y)
            #ax.scatter(data_secondary[:, 0], Y,label= ' M_BH= '+str(data_spectrum[1,0])+'g / '+data_folders[j])   # peak= '+str(peak)+', E_peak= '+str(E_max)+'GeV'+'M_BH= '+str(data_spectrum[1,0])+'g', linewidth=2)
            #plt.ylim(0,5*max(Y))
            #plt.xscale('log')
            #ax.set_ylabel(r'$\gamma$ / [GeV yr km$^{2}$]')
            #plt.title('BLACKHAWK-PBH flux on earth at='+str(r)+' [pc]', fontsize=10, y=1.02)
            ##########################################################################################
            plt.grid(b=True)
            plt.legend(loc = 0,prop={'size': 10},facecolor='white',framealpha=1,markerscale=3)
            plt.savefig("proton_spectra.png", dpi=300)
plt.show()
print(np.shape(dataX))
print(np.shape(dataY))
print(np.shape(dataYearth))
np.save('dataXsec',dataX)
np.save('dataYsec',dataY)
np.save('dataYearthsec',dataYearth)



