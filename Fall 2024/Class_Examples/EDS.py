from datascience import *
import time                # Python time functions
from time import strptime 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import matplotlib.dates as mdates
from matplotlib import ticker
import numpy as np
def Tdate(date_string):
    return time.mktime(strptime(date_string, '%m/%d/%Y'))
def FilterTdate(tbl,d1,d2,datec=0,fmtdate='%m/%d/%Y'):
    mkd1=Tdate(d1)
    mkd2=Tdate(d2)
    print("Filtering Table dates between",d1,d2)
    if type(tbl[datec][0])!= np.float64:
        tbl.set_format(datec, DateFormatter(format='%Y-%m-%d',))    
    tbl_out = tbl.where(datec,are.between(mkd1,mkd2))
    return tbl_out    
def ptrend(tbl,datec,datac,fmtdate="%b-%Y"):
    """  Takes Datascience Table and plots time trend, returns number of days """
    # Input Data to plot
    datetrend = tbl.column(datec).astype("datetime64[s]")  # Need to convert to a datetime64[s] object
    data = tbl.column(datac)
    loc = mdates.AutoDateLocator()  # Fancy function for dates
    fmt = mdates.AutoDateFormatter(loc)
    plt.gca().xaxis.set_major_formatter(fmt)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(fmtdate))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(fmtdate))
    plt.gca().tick_params(axis="x", which="minor", direction="out", top=True)
    plt.plot(datetrend, data,label=datac)
    plt.legend(loc='center left', bbox_to_anchor=(1.1, 0.5), labelspacing=3)  
    plt.gcf().autofmt_xdate()
    days= (datetrend.max()-datetrend.min()).astype('timedelta64[D]')/np.timedelta64(1, 'D')
    return days
### Molecular Tools
import py3Dmol

from rdkit import Chem
from rdkit.Chem.Draw import IPythonConsole #Needed to show molecules
from rdkit.Chem.Draw.MolDrawing import MolDrawing, DrawingOptions #Only needed if modifying defaults
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit import DataStructs
# Options
DrawingOptions.bondLineWidth=1.8


def MolTo3DView(mol, size=(300, 300), style="stick", surface=False, opacity=0.5, label=True):
    """Draw molecule in 3D
    
    Args:
    ----
        mol: rdMol, molecule to show
        size: tuple(int, int), canvas size
        style: str, type of drawing molecule
               style can be 'line', 'stick', 'sphere', 'carton'
        surface, bool, display SAS
        opacity, float, opacity of surface, range 0.0-1.0
    Return:
    ----
        viewer: py3Dmol.view, a class for constructing embedded 3Dmol.js views in ipython notebooks.
    """
    assert style in ('line', 'stick', 'sphere', 'carton')
    mblock = Chem.MolToMolBlock(mol)
    viewer = py3Dmol.view(width=size[0], height=size[1])
    viewer.addModel(mblock, 'mol')
    viewer.setStyle({style:{}})
    if surface:
        viewer.addSurface(py3Dmol.SAS, {'opacity': opacity})
    viewer.zoomTo()
    return viewer
def smiles3D(smiles):
    '''Convert SMILES to rdkit.Mol with 3D coordinates'''
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol)
        AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
        viewer = MolTo3DView(mol, size=(600, 300), style='stick')
        viewer.show()
        return mol
    else:
        return None
def fplot(f,xrange,yrange):
    import matplotlib.ticker as ticker
    from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
    plt.style.use('default')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # Move left y-axis and bottom x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which='both', width=2)
    ax.tick_params(which='major', length=7)
    ax.tick_params(which='minor', length=4, width=.5,color='r')
    plt.plot([x for x in np.arange(xrange[0],xrange[1],abs(xrange[1]-xrange[0])/50)],[f(x) for x in np.arange(yrange[0],yrange[1],abs(yrange[1]-yrange[0])/50)],lw=4, c='chartreuse',label='function')
    ax.set_xlim(xrange)
    ax.set_ylim(yrange)
    plt.grid( which='major', color='g', linestyle='--',alpha=.15)
    plt.legend()
    plt.show()
    return True