import streamlit as st

mostraTexto = st.selectbox('Mostrar Texto', options=['Sim', 'Não'], key='mostraTexto')

if st.session_state.mostraTexto == 'Sim':
    st.write(' Teste de deploy usando streamlit: OK!')
else:
    pass
