# titulo:
# botão iniciar chat
# clicou no botão
# popup
# titulo de bem-vindo
# campo: escreva seu nome no chat
# botão entar no chat
# chat
# embaixo do chat
# campo de digite sua mensagem
# botão enviar

# flet = framework Python
import flet as ft  # Importar


def main(pagina):  # criar a função principal
    texto = ft.Text("Acolhimentozap")
    # texto2 = ft.Text("texto dois") # Exemplo/ delete

    chat = ft.Column()  # chat é  uma coluna que tem varias msg uma embaixo da outra

    # criar um tunel de comunicação

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
        # adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)  # qndo vc rodar a funçao mensagem tunel ira chamr o send_all

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")  # enviar msg para todos os usuarios
        # limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)  # campo de texto
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrar_chat(evento):
        print("Entrar no chat")
        # fechar o popup
        popup.open = False
        # tirar o botao inciar chat
        pagina.remove(botao_iniciar)
        # tirar  titulo Acolhimentozap
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(
            f"{nome_usuario.value} entrou no chat")  # usando o nome_usuario.value você esta pegando o valor que esta dentro do nome de usuario
        # colocar o campo de digitar mensagem
        # criar o botao de enviar
        pagina.add(linha_enviar)
        pagina.update()

        # criar popup

    titulo_popup = ft.Text("Bem vindo ao Acolhimentozap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")  # label não é um texto fixo
    botao_entrar = ft.ElevatedButton("Entrar no char", on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False,
        modal=True,  # aparece como uma janela no meio da tela em vez de no canto
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]  # por padrao pede uma lista por mais que tenha apenas um item
    )  # toda pagina pode ter um popup/ posso criar qts popup eu quiser

    # Executar Popup
    def abrir_popup(evento):  # para abrir um modal
        # pass não  fazer nada
        pagina.dialog = popup
        print("abrir o chat")  # tenho que colocar qual popup ira abri da seguinte forma pagina.dialog = popup
        popup.open = True  # para abrir o popup na pagina
        pagina.update()  # atualiza a pag sem que você usuario tenha que atualiza a pag

    # temos que atualizar a pagina sempre/sempre que você editar a pag para rodar a pag sem ficar atualizando a pag
    # usamos pagina.update() sempre que fizer uma edição na pag usar o update

    # para o botão funcionar eu preciso criar a função
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)  # botão iniciar

    pagina.add(texto)
    # pagina.add(texto2) # Exemplo/delete
    pagina.add(botao_iniciar)


ft.app(target=main, view=ft.WEB_BROWSER)  # criar o app chamando a função principal
