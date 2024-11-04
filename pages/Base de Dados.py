import streamlit as st

# Verificar se o DataFrame original foi carregado na page1
if "df_spotify" in st.session_state and st.session_state["df_spotify"] is not None:
    # Exibir o DataFrame original
    st.write("DataFrame Original (df_spotify):")
    st.dataframe(st.session_state["df_spotify"])
else:
    st.write("O DataFrame original ainda não foi carregado. Por favor, carregue-o na page1.")
