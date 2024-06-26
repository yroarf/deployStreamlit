import streamlit as st
import pandas as pd

mostraTexto = st.selectbox('Mostrar Texto', options=['Sim', 'Não', 'Talvez'], key='mostraTexto')

if st.session_state.mostraTexto == 'Sim':
    st.write(' Teste de deploy usando streamlit: OK!')
elif st.session_state.mostraTexto == 'Não':
    dfAreaPrest_0 = pd.read_csv("df_Mun_UF_Area.csv", dtype=str)
    st.dataframe(dfAreaPrest_0)
else:
    df_pop = pd.read_csv("teste/pop_2014_2021.csv", dtype=str)
    st.dataframe(df_pop)
