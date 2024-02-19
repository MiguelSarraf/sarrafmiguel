import streamlit as st
from constantes import *

if "page" not in st.session_state:
	st.session_state.page="inicio"

if st.session_state.page=="inicio":
	abas=[
		st.sidebar.button("Início"),
		st.sidebar.button("Meus textos"),
		st.sidebar.button("Experimentos com Chat-GPT")
		]

	st.image("perfil.png", width=500)
	st.write("Olá. Eu sou o Miguel Sarraf.")
	st.write("Sou um engenheiro brincando de escrever.")
	st.write("Comecei na poesia aos 13 anos e nunca mais perdi o gosto. Mais recentemente estou escrevendo contos/crônicas também.")
	st.write("Se você ainda não me segue no insta, dá uma força lá:wink::@sarraf_miguel")
	st.write("Estou fazendo posts toda primeira semana do mês, mas sempre compartilho alguns pensamentos e leituras nos stories.")
	st.write("Todos os meus textos publicados estão aqui também, além de alguns experimentos com o chat-GPT, dá uma olhada nas abas aqui na esquerda:arrow_left:")

	if abas[1]:
		st.session_state.page="textos"
		st.rerun()
	elif abas[2]:
		st.session_state.page="chatgpt"
		st.rerun()

elif st.session_state.page=="textos":
	abas=[
		st.sidebar.button("Início"),
		st.sidebar.button("Meus textos"),
		st.sidebar.button("Experimentos com Chat-GPT")
		]

	for texto in textos:
		img,txt=st.columns([1,2])
		img.image("textos/%s.png"%(texto))
		with open("textos/%s.txt"%(texto), "r") as linhas:
			linhas=linhas.read().split("\n")
			linha_1=linhas[:textos[texto]]
			linhas=linhas[textos[texto]:]
			for linha in linha_1:
				txt.write(linha)
			exp=st.expander("Continue lendo")
			for linha in linhas:
				exp.write(linha)

	if abas[0]:
		st.session_state.page="inicio"
		st.rerun()
	elif abas[2]:
		st.session_state.page="chatgpt"
		st.rerun()

elif st.session_state.page=="chatgpt":
	abas=[
		st.sidebar.button("Início"),
		st.sidebar.button("Meus textos"),
		st.sidebar.button("Experimentos com Chat-GPT")
		]

	cols=st.columns(len(textos_gpt))
	textos=[]
	for col,texto in zip(cols, textos_gpt):
		textos.append(col.button(texto))

	if "texto" not in st.session_state:
		st.session_state.texto="Metrô"

	st.header(st.session_state.texto)

	etapas=textos_gpt[st.session_state.texto]
	for etapa in etapas:
		exp=st.expander(etapa[0])
		for linha in etapa[1]:
			exp.write(linha)

	if abas[0]:
		st.session_state.page="inicio"
		st.rerun()
	elif abas[1]:
		st.session_state.page="textos"
		st.rerun()
