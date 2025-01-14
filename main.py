import streamlit as st
from streamlit_modal import Modal
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

	botoes=[]
	modals=[]
	proporcao=[2,1]
	indice_img=False
	alinhamento=["right", "left"]
	for texto, titulo, linhas_vazias, url in textos:
		cols=st.columns(proporcao)
		cols[indice_img].image("textos/%s.png"%(texto))
		modals.append(Modal(key=texto, title=titulo))
		for _ in range(linhas_vazias):
			cols[not indice_img].write("")
		botoes.append(cols[not indice_img].button(key=texto, label='Leia completo aqui.'))
		cols[not indice_img].link_button("Veja o original aqui.", url)
		proporcao=proporcao[::-1]
		alinhamento=alinhamento[::-1]
		indice_img=not indice_img

	if any(botoes):
		indice=botoes.index(True)
		with modals[indice].container():
			with open("textos/%s.txt"%(textos[indice][0]), "r") as linhas:
				linhas=linhas.read().split("\n")
				for linha in linhas:
					st.write(linha)

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

	if any(textos):
		st.session_state.texto=list(textos_gpt.keys())[textos.index(True)]
		st.rerun()
	if abas[0]:
		st.session_state.page="inicio"
		st.rerun()
	elif abas[1]:
		st.session_state.page="textos"
		st.rerun()
