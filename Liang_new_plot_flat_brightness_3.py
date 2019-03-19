#!/usr/bin/env python3
import os
import numpy as np
import astropy.io.fits as fits
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.optimize import curve_fit

#######################################
### to be specified by the User:
path = '/mnt/c/Users/Vanessa/Documents/work/science/FOCES_reduction/'
analyse_folder= ['20190313','20190317','20190318']
# true= all folders in the specified path are analysed
# false= only the folders in analyse_folder are analysed
dec_path_list = False

#######################################

def get_flux(data, head, offset):
    exptime = head['EXPOSURE']

    spec1 = data[730-9+offset:730+10+offset, 976-1:976+2].mean(axis=1)
    bkg1  = (spec1[0:2].sum() + spec1[-2:].sum())/4.
    spec1 = spec1 - bkg1
    contra1 = spec1.max()/bkg1
    flux1 = spec1.sum()/exptime

    spec2 = data[1765-9+offset:1765+10+offset, 976-1:976+2].mean(axis=1)
    bkg2  = (spec2[0:2].sum() + spec2[-2:].sum())/4.
    spec2 = spec2 - bkg2
    contra2 = spec2.max()/bkg2
    flux2 = spec2.sum()/exptime

    return flux1, flux2, spec1, spec2, contra1, contra2

def get_flux_lst(filename_lst, offset_lst, name):
    fig = plt.figure(dpi=120, figsize=(12,6))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    time_lst, flux1_lst, flux2_lst = [], [], []
    bkg1_lst, bkg2_lst = [], []
    for ifile, filename in enumerate(filename_lst):
        fname = os.path.basename(filename)
        data, head = fits.getdata(filename, header=True)
        data = data - data[:, 0:20].mean()
        time = head['FRAME']
        flux1, flux2, spec1, spec2, bkg1, bkg2 = get_flux(data, head, offset_lst[ifile])
        time_lst.append(time)
        flux1_lst.append(flux1)
        flux2_lst.append(flux2)
        bkg1_lst.append(bkg1)
        bkg2_lst.append(bkg2)

        ax1.plot(spec1, color='C0', alpha=0.5)
        ax2.plot(spec2, color='C1', alpha=0.5)
        ax1.set_title(name)
        ax2.set_title(name)
    time_lst = mdates.datestr2num(time_lst)
    time_lst = [(time - time_lst[0])*24 for time in time_lst]
    return time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst, fig

def gaus(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def main():
    fig1 = plt.figure(dpi=100, figsize=(15,5))
    ax1 = fig1.add_subplot(221)
    ax2 = fig1.add_subplot(222)
    ax3 = fig1.add_subplot(223)
    ax4 = fig1.add_subplot(224)

    #############################################################################
    #filename_lst = []
    #offset_lst = []
    #for fname in sorted(os.listdir('../2018-11-27/rawdata')):
    #    if 'FLA0' in fname:
    #        filename = os.path.join('../2018-11-27/rawdata', fname)
    #        filename_lst.append(filename)
    #        frameno = int(fname[9:13])
    #        offset_lst.append(3)
    #time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst = get_flux_lst(filename_lst, offset_lst)
    #ax1.plot(time_lst, flux1_lst, 'o-', color='C6', alpha=0.7)
    #ax2.plot(time_lst, flux2_lst, 'o-', color='C6', alpha=0.7)
    #ax3.plot(time_lst, bkg1_lst, 'o-', color='C6', alpha=0.7)
    #ax4.plot(time_lst, bkg2_lst, 'o-', color='C6', alpha=0.7)
    # ############################################################################
    # filename_lst = []
    # offset_lst = []
    # for fname in sorted(os.listdir('raw_20181218')):
    #     if 'FLA0' in fname:
    #         filename = os.path.join('raw_20181218', fname)
    #         filename_lst.append(filename)
    #         frameno = int(fname[9:13])
    #         offset_lst.append(3)
    # time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst = get_flux_lst(filename_lst, offset_lst)
    # ax1.plot(time_lst, flux1_lst, 'o-', color='C1', alpha=0.7)
    # ax2.plot(time_lst, flux2_lst, 'o-', color='C1', alpha=0.7)
    # ax3.plot(time_lst, bkg1_lst, 'o-', color='C1', alpha=0.7)
    # ax4.plot(time_lst, bkg2_lst, 'o-', color='C1', alpha=0.7)
    # ############################################################################
    # filename_lst = []
    # offset_lst = []
    # for fname in sorted(os.listdir('raw_20181219')):
    #     if 'FLA0' in fname:
    #         filename = os.path.join('raw_20181219', fname)
    #         filename_lst.append(filename)
    #         frameno = int(fname[9:13])
    #         offset_lst.append(3)
    # time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst = get_flux_lst(filename_lst, offset_lst)
    # ax1.plot(time_lst, flux1_lst, 'o-', color='C2', alpha=0.7)
    # ax2.plot(time_lst, flux2_lst, 'o-', color='C2', alpha=0.7)
    # ax3.plot(time_lst, bkg1_lst, 'o-', color='C2', alpha=0.7)
    # ax4.plot(time_lst, bkg2_lst, 'o-', color='C2', alpha=0.7)
    # ############################################################################
    # filename_lst = []
    # offset_lst = []
    # for fname in sorted(os.listdir('raw_20190205')):
    #     if 'FLA0' in fname:
    #         filename = os.path.join('raw_20190205', fname)
    #         filename_lst.append(filename)
    #         frameno = int(fname[9:13])
    #         offset_lst.append(3)
    # time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst = get_flux_lst(filename_lst, offset_lst)
    # ax1.plot(time_lst, flux1_lst, 'o-', color='C3', alpha=0.7)
    # ax2.plot(time_lst, flux2_lst, 'o-', color='C3', alpha=0.7)
    # ax3.plot(time_lst, bkg1_lst, 'o-', color='C3', alpha=0.7)
    # ax4.plot(time_lst, bkg2_lst, 'o-', color='C3', alpha=0.7)
    # ############################################################################
    # filename_lst = []
    # offset_lst = []
    # for fname in sorted(os.listdir('raw_20190206')):
    #     if 'FLA0' in fname:
    #         filename = os.path.join('raw_20190206', fname)
    #         filename_lst.append(filename)
    #         frameno = int(fname[9:13])
    #         offset_lst.append(3)
    # time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst = get_flux_lst(filename_lst, offset_lst)
    # ax1.plot(time_lst, flux1_lst, 'o-', color='C4', alpha=0.7)
    # ax2.plot(time_lst, flux2_lst, 'o-', color='C4', alpha=0.7)
    # ax3.plot(time_lst, bkg1_lst, 'o-', color='C4', alpha=0.7)
    # ax4.plot(time_lst, bkg2_lst, 'o-', color='C4', alpha=0.7)
    # ############################################################################
    # filename_lst = []
    # offset_lst = []
    # for fname in sorted(os.listdir('raw_20190214')):
    #     if 'FLA0' in fname:
    #         filename = os.path.join('raw_20190214', fname)
    #         filename_lst.append(filename)
    #         frameno = int(fname[9:13])
    #         offset_lst.append(3)
    # time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst = get_flux_lst(filename_lst, offset_lst)
    # ax1.plot(time_lst, flux1_lst, 'o-', color='C5', alpha=0.7)
    # ax2.plot(time_lst, flux2_lst, 'o-', color='C5', alpha=0.7)
    # ax3.plot(time_lst, bkg1_lst, 'o-', color='C5', alpha=0.7)
    # ax4.plot(time_lst, bkg2_lst, 'o-', color='C5', alpha=0.7)
    # ############################################################################
    # filename_lst = []
    # offset_lst = []
    # for fname in sorted(os.listdir('raw_20190215')):
    #     if 'FLA0' in fname:
    #         filename = os.path.join('raw_20190215', fname)
    #         filename_lst.append(filename)
    #         frameno = int(fname[9:13])
    #         offset_lst.append(3)
    # time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst = get_flux_lst(filename_lst, offset_lst)
    # ax1.plot(time_lst, flux1_lst, 'o-', color='C6', alpha=0.7)
    # ax2.plot(time_lst, flux2_lst, 'o-', color='C6', alpha=0.7)
    # ax3.plot(time_lst, bkg1_lst, 'o-', color='C6', alpha=0.7)
    # ax4.plot(time_lst, bkg2_lst, 'o-', color='C6', alpha=0.7)
    ############################################################################
    path_cont=''
    if dec_path_list==True: path_cont=os.listdir(path)
    else: path_cont=analyse_folder
    
    i = 0
    offset_lst = []
    for folder in path_cont:
        if folder.find('.')==-1:
            # print(folder)
            filename_lst = []
            offset_lst = []
            for fname in sorted(os.listdir(path+folder)):
                    if 'FLA0' in fname:
                            filename = os.path.join(path+folder, fname)
                            filename_lst.append(filename)
                            frameno = int(fname[9:13])
                            data, head = fits.getdata(filename, header=True)
                            flux1, flux2, spec1, spec2, contra1, contra2=get_flux(data,head, 0)
                            popt1,pcov1 = curve_fit(gaus,np.arange(0,len(spec1)),spec1,p0=[np.max(spec1),10,5])
                            #print(filename,popt1[1])
                            print(fname,int(np.round(9.75-popt1[1])))
                            offset_lst.append(int(-1*np.round(9.75-popt1[1])))
                            if abs(int(-1*np.round(9.75-popt1[1])))>5:print('WARNING!!!: OFFSET IS TOO BIG!!')
                            #offset_lst.append(0)
            time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst, fig2 = get_flux_lst(filename_lst, offset_lst,folder)
            plot_col='C'+str(i)
            ax1.plot(time_lst, flux1_lst, 'o-', color=plot_col, alpha=0.7)
            ax2.plot(time_lst, flux2_lst, 'o-', color=plot_col, label=folder, alpha=0.7)
            ax3.plot(time_lst, bkg1_lst,  'o-', color=plot_col, alpha=0.7)
            ax4.plot(time_lst, bkg2_lst,  'o-', color=plot_col, alpha=0.7)
            #plt.legend()
            fig2.savefig(path+'flat_brightness_profile_'+folder+'.png')
            offset_lst = []
        i=i+1
    ############################################################################
    '''
    filename_lst = []
    offset_lst = []
    for fname in sorted(os.listdir('raw_20190219')):
        if 'FLA0' in fname:
            filename = os.path.join('raw_20190219', fname)
            filename_lst.append(filename)
            frameno = int(fname[9:13])
            offset_lst.append(3)
    time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst, fig2 = get_flux_lst(filename_lst, offset_lst)
    ax1.plot(time_lst, flux1_lst, 'o-', color='C8', alpha=0.7)
    ax2.plot(time_lst, flux2_lst, 'o-', color='C8', alpha=0.7)
    ax3.plot(time_lst, bkg1_lst, 'o-', color='C8', alpha=0.7)
    ax4.plot(time_lst, bkg2_lst, 'o-', color='C8', alpha=0.7)
    fig2.savefig('flat_brightness_profile_20190219.png')
    ############################################################################
    filename_lst = []
    offset_lst = []
    for fname in sorted(os.listdir('raw_20190222')):
        if 'FLA0' in fname:
            filename = os.path.join('raw_20190222', fname)
            filename_lst.append(filename)
            frameno = int(fname[9:13])
            offset_lst.append(5)
    time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst, fig2 = get_flux_lst(filename_lst, offset_lst)
    ax1.plot(time_lst, flux1_lst, 'o-', color='C9', alpha=0.7)
    ax2.plot(time_lst, flux2_lst, 'o-', color='C9', alpha=0.7)
    ax3.plot(time_lst, bkg1_lst, 'o-', color='C9', alpha=0.7)
    ax4.plot(time_lst, bkg2_lst, 'o-', color='C9', alpha=0.7)
    fig2.savefig('flat_brightness_profile_20190222.png')
    ############################################################################
    filename_lst = []
    offset_lst = []
    for fname in sorted(os.listdir('raw_20190225')):
        if 'FLA0' in fname:
            filename = os.path.join('raw_20190225', fname)
            filename_lst.append(filename)
            frameno = int(fname[9:13])
            offset_lst.append(5)
    time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst, fig2 = get_flux_lst(filename_lst, offset_lst)
    ax1.plot(time_lst, flux1_lst, 'o-', color='C0', alpha=0.7)
    ax2.plot(time_lst, flux2_lst, 'o-', color='C0', alpha=0.7)
    ax3.plot(time_lst, bkg1_lst, 'o-', color='C0', alpha=0.7)
    ax4.plot(time_lst, bkg2_lst, 'o-', color='C0', alpha=0.7)
    fig2.savefig('flat_brightness_profile_20190225.png')
    ############################################################################
    filename_lst = []
    offset_lst = []
    for fname in sorted(os.listdir('raw_20190226')):
        if 'FLA0' in fname:
            filename = os.path.join('raw_20190226', fname)
            filename_lst.append(filename)
            frameno = int(fname[9:13])
            offset_lst.append(5)
    time_lst, flux1_lst, flux2_lst, bkg1_lst, bkg2_lst,fig2 = get_flux_lst(filename_lst, offset_lst)
    #fig2 = plt.figure(dpi=150, figsize=(15,5))
    ax1.plot(time_lst, flux1_lst, 'o-', color='C1', alpha=0.7)
    ax2.plot(time_lst, flux2_lst, 'o-', color='C1', alpha=0.7)
    ax3.plot(time_lst, bkg1_lst, 'o-', color='C1', alpha=0.7)
    ax4.plot(time_lst, bkg2_lst, 'o-', color='C1', alpha=0.7)
    fig2.savefig('flat_brightness_profile_20190226.png')
    '''
    ############################################################################
    ############################################################################

    #ax1.set_ylim(0,)
    #ax2.set_ylim(0,)
    #fig.legend()
    ax2.legend(bbox_to_anchor=(1.02,1),loc=2)
    ax3.set_xlabel('Time offset (Hour)')
    ax4.set_xlabel('Time offset (Hour)')
    ax1.grid(True)
    ax2.grid(True)
    fig1.savefig('flat_brightness.png')
    plt.show()

if __name__=='__main__':
    main()
