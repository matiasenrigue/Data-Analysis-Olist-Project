from math import radians, sin, cos, asin, sqrt
import matplotlib.pyplot as plt
import seaborn as sns


def haversine_distance(lon1, lat1, lon2, lat2):
    """
    Compute distance between two pairs of coordinates (lon1, lat1, lon2, lat2)
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * 6371 * asin(sqrt(a))


def return_significative_coef(model):
    """
    Returns p_value, lower and upper bound coefficients
    from a statsmodels object.
    """
    # Extract p_values
    p_values = model.pvalues.reset_index()
    p_values.columns = ['variable', 'p_value']

    # Extract coef_int
    coef = model.params.reset_index()
    coef.columns = ['variable', 'coef']
    return p_values.merge(coef,
                          on='variable')\
                   .query("p_value<0.05").sort_values(by='coef',
                                                      ascending=False)


def plot_kde_plot(df, variable, dimension):
    """
    Plot a side by side kdeplot for `variable`, split
    by `dimension`.
    """
    g = sns.FacetGrid(df,
                      hue=dimension,
                      col=dimension)
    g.map(sns.kdeplot, variable)



def standardize(df, lista_columnas_del_df):

    '''
    Función para normalizar un df, solo se van a noralizar las columnas en la lista de columnas
    En la lista pon las columnas con variables numericas, que puedan normalizarse
    '''

    X_std = df.copy()

    for f in lista_columnas_del_df:
        mu = df[f].mean()
        sigma = df[f].std()
        X_std[f] = df[f].map(lambda x: (x - mu) / sigma)


    return X_std
