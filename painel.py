from flet import *

#Função principal
def main(pagina:Page):
  pagina.title = "Personalizando personagem"
  pagina.horizontal_alignment = CrossAxisAlignment.START
  pagina.theme_mode = ThemeMode.LIGHT

  def Login(e):
    #simular o login do jogador 
    pass

  def SalvarDados(e):
    #acessando os filhos de Conteiner onde estão os valores de TextField = nome, primeiro dropdown = raça, segundo dropdown = classe, primeira checkbox = Genero Masculino e segunda checkbox = Genero feminino. No mesmo armazena cada valor em uma variavel própria e joga tudo dentro de uma lista nomeada "cadastro" 
    nome = Conteiner.content.controls[0].value
    raca = Conteiner.content.controls[1].value
    classe = Conteiner.content.controls[2].value
    if Conteiner.content.controls[4].value == True:
      genero = 'Masculino'
    elif Conteiner.content.controls[5].value == True:
      genero = 'Feminino'
    else:
      genero = "N.D."

    cadastro = [nome, raca, classe, genero]
    print(cadastro)

    Treeview.content = (
      ElevatedButton(text=cadastro, on_click=Login)
      )

    pagina.update()

  
#Criação dos elementos
  Conteiner = Container(
    bgcolor=colors.GREY_200,
    height=600,
    expand=1,
    margin=margin.all(5),
    padding=padding.only(top=50,bottom=50,left=15, right=15),
    border_radius=border_radius.all(10),

    content=Column(
      horizontal_alignment=CrossAxisAlignment.CENTER,

      controls=[
        TextField(label="Nome",hint_text='ex: Aelian', width=250,),
        Dropdown(            
          width=250,
          label='Raça',
          options=[
            dropdown.Option("Humano"),
            dropdown.Option("Elfo"),
            dropdown.Option("Anão"),
            dropdown.Option("Orc")
           ]
          ),
        Dropdown(
          width=250,
          label="Classe",
          options=[
            dropdown.Option("Guerreiro"),
            dropdown.Option("Barbaro"),
            dropdown.Option("Mago"),
            dropdown.Option("Bardo"),
            dropdown.Option("Arqueiro"),
            dropdown.Option("Monge"),
          ]
        ),
        Text("Genero"),
        Checkbox(label="Masculino", value="Masculino"),
        Checkbox(label="Feminino", value="Feminino"),

        ElevatedButton(text="enviar", on_click=SalvarDados)
        ]
      )
    )
  Treeview = Container(expand=3)
#adicionando os elementos a pagina
  pagina.add(Row([Conteiner, Treeview]))

  
app(target=main)