import os
import pandas as pd
import numpy as np
import pickle

#app_path = os.path.join(os.getcwd(), 'app\\')
app_path = os.getcwd()
model_path = os.path.join(app_path, 'model.sav')

X_var = ['surface_reelle_bati',
         'log_prixcible_surface',
         'prixcible_surface',
         'surface_terrain',
         'nombre_pieces_principales',
         'P16_POP_PER_SUPERF',
         'surface_par_piece',
         'P16_LOG_PER_POP',
         'P16_LOGVAC_PER_POP',
         'type_local_Maison',
         'code_postal_31100',
         'code_postal_31120',
         'code_postal_31170',
         'code_postal_31200',
         'code_postal_31270',
         'code_postal_31300',
         'code_postal_31400',
         'code_postal_31470',
         'code_postal_31500',
         'code_postal_31600',
         'code_postal_31700',
         'code_postal_31820',
         'code_postal_31830'
        ]
def preprocessing(df):
    insee_code_postal_df = pd.read_csv(app_path+'\\insee_code_postal.csv')
    df_2 = df.copy()
    df_2 = df_2.merge(insee_code_postal_df, left_on='code_postal', right_on='Code_postal')
    df_2['P16_POP_PER_SUPERF'] = df_2['P16_POP'] / df_2['SUPERF']
    df_2['surface_par_piece'] = df_2['surface_reelle_bati'] / df_2['nombre_pieces_principales']
    df_2['P16_LOG_PER_POP'] = df_2['P16_LOG'] / df_2['P16_POP']
    df_2['P16_LOGVAC_PER_POP'] = df_2['P16_LOGVAC'] / df_2['P16_POP']
    df_2 = pd.get_dummies(df_2, columns=['type_local', 'code_postal'], drop_first=True)
    df_2['prixcible_surface'] = df_2['prixcible'] / df_2['surface_reelle_bati']
    df_2['log_prixcible_surface'] = np.log(df_2['prixcible_surface'])
    df_2 = df_2.reindex(columns = X_var, fill_value=0)
    df_2 = df_2[X_var]
    return df_2

def estimate(df):
    model = pickle.load(open(model_path, 'rb'))
    result_m2 = np.exp(model.predict(np.array(df.loc[0]).reshape(1, -1))[0])
    result = (result_m2 * df['surface_reelle_bati'])[0]
    result =  "Valeur foncière estimée : {:,.0f} €". format(result).replace(',', ' ')
    return result