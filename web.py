import streamlit as st
from funções import leitura, registrar

lista = leitura()

def adicionar():
    nova_tarefa = st.session_state["nova_tarefa"].strip() + '\n'  # Sanitize
    lista.append(nova_tarefa)
    registrar(lista)
    st.session_state["nova_tarefa"] = ""

st.title("Task-Web")
st.subheader("Lista de tarefas para produtividade!")

for i, tarefa in enumerate(lista):
    tarefa_limpa = tarefa.strip()

    if f"entrada_{i}_{tarefa_limpa}" not in st.session_state:
        st.session_state[f"entrada_{i}_{tarefa_limpa}"] = False
    caixa = st.checkbox(tarefa_limpa, key=f"entrada_{i}_{tarefa_limpa}")
    if caixa:
        lista.pop(i)
        registrar(lista)

        key = f"entrada_{i}_{tarefa_limpa}"
        if key in st.session_state:
            del st.session_state[key]
        st.rerun()

st.text_input(label=" ", key="nova_tarefa", placeholder="Adicione uma nova tarefa", on_change=adicionar)

