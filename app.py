import streamlit as st
import requests



def buscar_letra_api(banda, musica):
    endpoint_lyrics = f"https://api.lyrics.ovh/v1/{banda}/{musica}" #API lyrics
    #Enpoint é o url de busca da API


    response = requests.get(endpoint_lyrics)

    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra
    #Basicamente retorna a letra de dentro do arquivo JSON se a música existir (que é identificado como o código 200)

def busca_imagem_música(musica): #Deezer API para buscar o mp3 da música e a imagem do album
    endpoint_música = f"https://api.deezer.com/search?q={musica}"

    response = requests.get(endpoint_música)
    
    if response.status_code == 200 and response.json().get("data"):
        musica_info = response.json()["data"][0]  # Pega o primeiro resultado da lista
        capa = musica_info["album"]["cover_big"]
        musica_preview = musica_info["preview"]
        musica_nome = musica_info["title"]
        return capa, musica_preview, musica_nome    

#Tela inicial

#Nome do app 
st.markdown("<h1 style='text-align: center; color: white;'>Letras</h1>", unsafe_allow_html=True)

#imagem que aparece na página inicial.
img_principal = st.empty()
img_principal.image("https://img.freepik.com/fotos-gratis/trompete-antigo-em-partituras_23-2147781341.jpg")

st.title("Banda/Artista")

#local onde o user indicará a banda que deseja. 
banda = st.text_input("Digite o nome da banda/artista", key="banda")

st.title("Música")

#local onde o user indicará a música que deseja. 
musica = st.text_input("Digite o nome da música", key="musica")

#Botão de pesquisar
pesquisar = st.button("Pesquisar")


if pesquisar: #Se pressionarem o botão pesquisar
    letra = buscar_letra_api(banda, musica) #chama a a função, e utilizza os argumentos dos inputs do site
    capa, musica_preview, musica_nome = busca_imagem_música(musica)
    if letra:
        st.markdown(f"""<h2 style='text-align: center; color: #FF0000; font-family: Arial;'>{musica_nome}</h2>""", unsafe_allow_html=True)
        st.audio(musica_preview)
        st.text(letra)
        img_principal.image(capa)
        
        
    else:
        st.error("Não conseguimos encontrar a letra requisitada")

    #Trocar imagem para a do album e colocar um áudio da música após pressionar o botão pesquisar












