import streamlit as st

mostraTexto = st.selectbox('Mostrar Texto', options=['Sim', 'Não'], key='mostraTexto')

if st.session_state.mostraTexto == 'Sim':
    st.write(' Teste de deploy usando streamlit: OK!')
else:
    dfAreaPrest_0 = pd.read_csv("df_Mun_UF_Area.csv", dtype=str)
    st.dataframe(dfAreaPrest_0)
