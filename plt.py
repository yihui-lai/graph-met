from utils import load
import matplotlib.pyplot as plt
import numpy as np 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ckpts', default='ckpts',
                    help="Name of the ckpts folder")
parser.add_argument('--out', default='out',
                    help="Name of the plots folder")


args = parser.parse_args()
a=load(args.ckpts + '/best.resolutions')
colors = {
    'pfMET': 'black',
    'puppiMET': 'red',
    'deepMETResponse': 'blue',
    'deepMETResolution': 'green',
    'MET':  'magenta',
}
label_arr = {
    'MET':     'Graph MET' ,
    'pfMET':    'PF MET',
    'puppiMET': 'PUPPI MET',
    'deepMETResponse': 'DeepMETResponse',
    'deepMETResolution': 'DeepMETResolution',
}
resolutions_arr = {
    'MET':      [[],[],[]],
    'pfMET':    [[],[],[]],
    'puppiMET': [[],[],[]],
    'deepMETResponse': [[],[],[]],
    'deepMETResolution': [[],[],[]],
}
for key in resolutions_arr:
         plt.figure(1)
         xx = a[key]['u_perp_resolution'][1][0:20]
         yy = a[key]['u_perp_resolution'][0]
         plt.hist(xx, weights = yy, bins = xx,color=colors[key], label=label_arr[key],histtype='step',)
         plt.figure(2)
         xx = a[key]['u_perp_scaled_resolution'][1][0:20]
         yy = a[key]['u_perp_scaled_resolution'][0]
         plt.hist(xx, weights = yy, bins = xx,color=colors[key], label=key,histtype='step',)
         plt.figure(3)
         xx = a[key]['u_par_resolution'][1][0:20]
         yy = a[key]['u_par_resolution'][0]
         plt.hist(xx, weights = yy, bins = xx,color=colors[key], label=key,histtype='step',)
         plt.figure(4)
         xx = a[key]['u_par_scaled_resolution'][1][0:20]
         yy = a[key]['u_par_scaled_resolution'][0]
         plt.hist(xx, weights = yy, bins = xx,color=colors[key], label=key,histtype='step',)
         plt.figure(5)
         xx = a[key]['R'][1][0:20]
         yy = a[key]['R'][0]
         plt.hist(xx, weights = yy, bins = xx,color=colors[key], label=key,histtype='step',)

if(True):
    model_dir=args.out
    plt.figure(1)
    plt.axis([0, 400, 0, 25])
    plt.xlabel(r'$q_{T}$ [GeV]')
    plt.ylabel(r'$\sigma (u_{\perp})$ [GeV]')
    plt.legend()
    plt.savefig(model_dir+'/resol_perp.png')
    plt.clf()
    plt.close()

    plt.figure(2)
    plt.axis([0, 400, 0, 30])
    plt.xlabel(r'$q_{T}$ [GeV]')
    plt.ylabel(r'Scaled $\sigma (u_{\perp})$ [GeV]')
    plt.legend()
    plt.savefig(model_dir+'/resol_perp_scaled.png')
    plt.clf()
    plt.close()

    plt.figure(3)
    plt.axis([0, 400, 0, 45])
    plt.xlabel(r'$q_{T}$ [GeV]')
    plt.ylabel(r'$\sigma (u_{\parallel})$ [GeV]')
    plt.legend()
    plt.savefig(model_dir+'/resol_parallel.png')
    plt.clf()
    plt.close()

    plt.figure(4)
    plt.axis([0, 400, 0, 60])
    plt.xlabel(r'$q_{T}$ [GeV]')
    plt.ylabel(r'Scaled $\sigma (u_{\parallel})$ [GeV]')
    plt.legend()
    plt.savefig(model_dir+'/resol_parallel_scaled.png')
    plt.clf()
    plt.close()

    plt.figure(5)
    plt.axis([0, 400, 0, 1.2])
    plt.axhline(y=1.0, color='black', linestyle='-.')
    plt.xlabel(r'$q_{T}$ [GeV]')
    plt.ylabel(r'Response $-\frac{<u_{\parallel}>}{<q_{T}>}$')
    plt.legend()
    plt.savefig(model_dir+'/response_parallel.png')
    plt.clf()
    plt.close()



