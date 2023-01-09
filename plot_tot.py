import matplotlib.pyplot as plt
import numpy as np
import sys

e=np.load('dataenergy.npy')
dnde=np.load('dataemission_tintegrated.npy')

e_sec=np.load('dataenergy_sec.npy')
dnde_sec=np.load('dataemission_tintegrated_sec.npy')

###########################################################
# Here put the BlackHawk path
BH_path = "/home/lumarev/Downloads/version_finale"
result_folder = BH_path + "/results/"

data_folders = ['5yrtot','1yrtot']#,'3mthtot','1wktot','1daytot','6htot','30mintot','100stot','10stot','1stot','0.1stot','0.01stot'] # ['100stot','10stot','1stot','0.1stot','0.01stot'] # add lifetime from results you are interested

P=[] #paths of lifetimes data
for i in range(len(data_folders)):
    f=str(result_folder + data_folders[i] + "/")
    P.append(f)

# set 1 to activate and see spectrum 

photon_primary=1
gluons_primary=0
higgs_primary=0
W_primary=0
Z_primary=0
neutrinos_primary=0
electron_primary=0
muon_primary=0
tau_primary=0
up_primary=0
down_primary=0
charm_primary=0
strange_primary=0
top_primary=0
bottom_primary=0
graviton_primary=0

part_show_primary=np.zeros(16)
part_show_primary=np.array(part_show_primary,int)
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

labels_primary=np.array(np.zeros(16),str)
labels_primary[0]="$\gamma$"
labels_primary[1]="$g$"
labels_primary[2]="$h$"
labels_primary[3]="$W^\pm$"
labels_primary[4]="$Z^0$"
labels_primary[5]="$\\nu,\overline{\\nu}$"
labels_primary[6]="$e^\pm$"
labels_primary[7]="$\mu^\pm$"
labels_primary[8]="$\\tau^\pm$"
labels_primary[9]="$u,\overline{u}$"
labels_primary[10]="$d,\overline{d}$"
labels_primary[11]="$c,\overline{c}$"
labels_primary[12]="s,\overline{s}"
labels_primary[13]="t,\overline{t}"
labels_primary[14]="b,\overline{b}"
labels_primary[15]="${1\rm G}$"

particles_primary=np.array(np.zeros(16),str)
particles_primary[0] = "photon"
particles_primary[1] = "gluon"
particles_primary[2] = "higgs"
particles_primary[3] = "wpm"
particles_primary[4] = "z0"
particles_primary[5] = "neutrinos"
particles_primary[6] = "electron"
particles_primary[7] = "muon"
particles_primary[8] = "tau"
particles_primary[9] = "up"
particles_primary[10] = "down"
particles_primary[11] = "charm"
particles_primary[12] = "strange"
particles_primary[13] = "top"
particles_primary[14] = "bottom"
particles_primary[15] = "graviton"

##### SECONDARY #####

### Plotting options (secondary data)

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

    particles_secondary=np.array(np.zeros(nb_fin_part),str)
    particles_secondary[0] = "photon"
    particles_secondary[1] = "electron"
    particles_secondary[2] = "muon"
    particles_secondary[3] = "nu_e"
    particles_secondary[4] = "nu_mu"
    particles_secondary[5] = "nu_tau"
    particles_secondary[6] = "pipm"
    particles_secondary[7] = "K0L"
    particles_secondary[8] = "Kpm"
    particles_secondary[9] = "proton"
    particles_secondary[10] = "neutron"

elif epoch == 1:
    nb_fin_part = 6

    # Put 1 to plot the particle spectrum
    photon_secondary=1
    electron_secondary=0
    nu_e_secondary=0
    nu_mu_secondary=0
    nu_tau_secondary=0
    proton_secondary=0


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

    particles_secondary=np.array(np.zeros(nb_fin_part),str)
    particles_secondary[0] = "photon"
    particles_secondary[1] = "electron"
    particles_secondary[2] = "nu_e"
    particles_secondary[3] = "nu_mu"
    particles_secondary[4] = "nu_tau"
    particles_secondary[5] = "proton"






##################### plot ######################



#### by hand ##### same length that data_folders

kTlegends=['15','26']#,'42','98','179','284','650','1704','3670','7907','17036','36703']
lifetimeleg=['5 years','1 year']#,'3 months','1 week','1 day','6 hours','30 min.','100 sec.','10 sec.','1 sec.','0.1 sec.','0.01 sec.']


#################
plots_indx=[0,1]#,2,3]

fig=plt.figure(figsize=(7.0,5.0), dpi=200)
ax=fig.add_subplot(111)
#for j in range(len(data_folders)):
for j in plots_indx:
    for i in range(16):
        if part_show_primary[i]: # PRIMARY
        #if part_show_secondary[i]: # SECONDARY 
            ax.scatter(e[j],dnde[j],s=2.5,label=lifetimeleg[j]+' / '+kTlegends[j]) # PRIMARY
            #ax.scatter(e_sec[j],dnde_sec[j],s=2.5,label=lifetimeleg[j]+' / '+kTlegends[j])
            plt.xscale('log')
            plt.yscale('log')
            plt.ylim(1e20,1e40)
            ax.set_xlabel(r'$E\;$[GeV]')
            ax.set_ylabel(r'$dN_{\gamma}\,/\,dE\;$[GeV$^{-1}$]')
            plt.legend(loc=0,prop={'size': 8},facecolor='white',framealpha=1)
            plt.grid(b=True)
        else:
            break
plt.show()
#exit()

