import matplotlib.pyplot as plt 
import pandas as pd 
import tarfile 
import os 

from six.moves import urllib 


DOWNLOAD_ROOT = 'https://github.com/SeveredSurvival/ageron_handson-ml/blob/master/'
HOUSING_PATH = os.path.join( 'datasets', 'housing')
HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.tgz'

def fetch_housing_data( housing_url = HOUSING_URL, housing_path = HOUSING_PATH ):
    if not os.path.isdir( housing_path ):
        os.makedirs( housing_path )
    tgz_path = os.path.join( housing_path, 'housing.tgz' )

    urllib.request.urlretrieve( housing_url, tgz_path )
    housing_tgz = tarfile.open( tgz_path )
    housing_tgz.extractall( path = housing_path )
    housing_tgz.close() 

# LOADER DATASET 
def load_housing( housing_path = HOUSING_PATH ):
    csv_path = os.path.join(  housing_path, 'housing.csv' )
    return pd.read_csv( csv_path )  


if __name__ == '__main__':

    # fetch_housing_data() 

    dataset = load_housing() 
    print( dataset.describe()  )

    dataset.hist( bins = 50, figsize = (20,15) )
    plt.show() 








