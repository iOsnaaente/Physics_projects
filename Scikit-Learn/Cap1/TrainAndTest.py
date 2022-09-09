from Downloader import load_housing 
import pandas as pd 
import numpy as np 
import hashlib 

def split_train_test( data, test_ratio ): 
    shuffled_indices = np.random.permutation( len(data) ) 
    teste_set_size   = int( len(data) * test_ratio ) 
    test_indices     = shuffled_indices[ : teste_set_size ]
    train_indices    = shuffled_indices[ teste_set_size : ]  
    return data.iloc[train_indices], data.iloc[test_indices] 

def test_set_check( identifier, test_ratio, hash ):
    return hash( np.int64(identifier)).digest()[-1]<256 * test_ratio 

def split_train_test_by_id( data, test_ratio, id_collum, hash = hashlib.md5 ):
    ids = data[ id_collum ]
    in_test_set = ids.apply( lambda id_ : test_set_check( id_, test_ratio, hash )) 
    return data.loc[~in_test_set], data.loc[in_test_set]


if __name__ == '__main__':

    housing = load_housing() 
    housing = housing.reset_index()
    
    train, test = split_train_test_by_id( housing, 0.2, 'index' ) 
    print( 'dataset have', len(train), 'data train and', len(test), 'data test.')

    import matplotlib.pyplot as plt 

    # housing.plot( kind = 'scatter', x = 'longitude', y = 'latitude', alpha = 0.2 )
    def plot_housing():
        housing.plot( kind = 'scatter', x = 'longitude', y = 'latitude', alpha = 0.2,
                    s = housing['population']/100, label = 'Population', figsize = [10,7],
                    c = 'median_house_value', cmap = plt.get_cmap('jet'), colorbar = True
                    )
        plt.show() 
    
    # To fins correlations between the values and the mean 
    corr_matrix = housing.corr() 
    print( corr_matrix['median_house_value'].sort_values(ascending = False ) )

    housing[ 'rooms_per_household' ]      = housing[ 'total_rooms' ]    / housing['households']
    housing[ 'bedrooms_per_room' ]        = housing[ 'total_bedrooms' ] / housing['total_rooms']
    housing[ 'population_per_household' ] = housing[ 'population' ]     / housing['households']

    corr_matrix = housing.corr() 
    print( corr_matrix['median_house_value'].sort_values(ascending = False ) )


    # Para os dados faltantes 

    # # 1 - Livrar-se deles 
    # housing.dropna( subset = ['total_bedroosm'] ) 
    # # 2 - Livrar-se de todos atributos 
    # housing.drop( 'total_bedrooms', axis = 1 )

    # # 3 - Definir para a media 
    # median = housing['total_bedrooms'].median() 
    # housing['total_bedrooms'].fillna( median, inplace = True )


    # 4 - Usar a média prevista com o Imputer do sklearn  
    from sklearn.impute import SimpleImputer   
    
    housing_num =  housing.drop( 'ocean_proximity', axis = 1 )
    imputer = SimpleImputer( strategy = 'median' ) 
    imputer.fit( housing_num )
    X = imputer.transform( housing_num )
    housing_tr = pd.DataFrame( X, columns = housing_num.columns )
    print( housing_tr )


    from sklearn.preprocessing import OneHotEncoder 
