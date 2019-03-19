#!/usr/bin/env python3
import re
import os
import dateutil
import numpy as np
import astropy.io.fits as fits
import scipy.interpolate as intp
import scipy.optimize as opt
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


filename_lst = []

if False:
    path = '../2018-11-01/rawdata'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
if False:
    path = '../2018-11-02/rawdata'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
if False:
    path = '../2018-11-03/rawdata'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
if False:
    path = '../2018-11-04/rawdata'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
if False:
    path = '../2018-11-27/rawdata'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
if False:
    path = '../2018-11-28/rawdata'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
if False:
    path = '../2018-11-29/rawdata'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
if False:
    path = 'raw_20181205'
    for fname in sorted(os.listdir(path)):
        # print(fname)
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20181206'
    for fname in sorted(os.listdir(path)):
        # print(fname)
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20181218'
    for fname in sorted(os.listdir(path)):
        # print(fname)
        # print(fname[9:13])
        fileid = int(fname[9:13])
        if 'THA0' in fname and fileid not in [43, 44, 45, 109, 110]:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20181219'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20190205'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)
            
if False:
    path = 'raw_20190206'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20190214'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20190215'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20190218'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20190219'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20190222'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = 'raw_20190225'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190226'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190227'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190228'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190301'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190304'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190305'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190307'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190308'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190312'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if False:
    path = '20190313'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if True:
    path = '20190317'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)

if True:
    path = '20190318'
    for fname in sorted(os.listdir(path)):
        if 'THA0' in fname:
            filename = os.path.join(path, fname)
            filename_lst.append(filename)


def find_shift_ccf(data1, data2, shift0=[0.0,0.0]):
    h, w = data1.shape

    f = intp.RectBivariateSpline(np.arange(h), np.arange(w), data1)

    def func(shift):
        ynew = np.arange(h)-shift[1]
        xnew = np.arange(w)-shift[0]
        datanew = f(ynew, xnew)
        return (datanew - data2).flatten()

    res = opt.least_squares(func, shift0)

    return res['x']

def main():
    time_lst = []
    shiftx_lst = []
    shifty_lst = []
    for ifile, filename in enumerate(filename_lst):
        data, head = fits.getdata(filename, header=True)
        time = head['FRAME']
        data = data[:, 20:2068] - data[:, 0:20].mean()
        data = data[500:1500, 500:1500]
        if ifile==0:
            ref_data = data

        shift = find_shift_ccf(ref_data, data)
        shift_x, shift_y = shift
        time_lst.append(time)
        shiftx_lst.append(shift_x)
        shifty_lst.append(shift_y)
        print('%s %s %+8.5f %+8.5f'%(os.path.basename(filename)[0:13], time, shift_x, shift_y))
        ref_data = data

    shiftx_lst = np.array(shiftx_lst)
    shifty_lst = np.array(shifty_lst)
    shiftx_lst = shiftx_lst.cumsum(dtype=np.float64)
    shifty_lst = shifty_lst.cumsum(dtype=np.float64)

    datenums = mdates.datestr2num(time_lst)

    fig2 = plt.figure(dpi=150,figsize=(15,6), tight_layout=True)
    ax21 = fig2.add_subplot(121)
    ax22 = fig2.add_subplot(122)
    ax21.plot_date(datenums, shiftx_lst, 'o-', ms=5, alpha=0.8)
    ax22.plot_date(datenums, shifty_lst, 'o-', ms=5, alpha=0.8)

    if datenums[-1]-datenums[0]>1:
        xfmt = '%m-%d %H:%M'
    else:
        xfmt = '%H:%M'
    for ax in fig2.get_axes():
        ax.xaxis.set_major_formatter(mdates.DateFormatter(xfmt))
        ax.grid(True, ls='--')
    ax21.set_ylabel(u'\u0394X (pixel)')
    ax22.set_ylabel(u'\u0394Y (pixel)')
    plt.setp(ax21.get_xticklabels(), rotation=45)
    plt.setp(ax22.get_xticklabels(), rotation=45)
    fig2.savefig('shift_thar.png')

    plt.show()


if __name__=='__main__':
    main()
