# A concessionária União esta fazendo uma compra de uma nova leva de carros. Agora Precisamos saber quais são os carros; as marcas dos carros; o ano dos carros e por fim, de onde os carros vieram (Cidade/Estado).
#MARCA DE CARROS 
print("Olá, seja bem vindo (a) Carros Sul! Preencha as informações necessárias para ver as informações da sua compra")
pedeInform = input("Digite seu nome: ")
pedeInform2 = input("Digite seu CPF: ")

bd_cpf_pedInform = 16555754 # CPF FALSO 

if bd_cpf_pedInform == 16555754:
    print(f"Olá {pedeInform} Seu CPF está certo!")
else: 
    print("CPF incorreto!")

lista_carros = {
    "Ford" : "KA+",
    "Honda" : "Civic",
    "Chevrollet " : "s10",
    "Toyota" : "Hilux",
    "Fiat" : "Argo",
    "Hyundai" : "Hb20"
}
# LUGAR DE ONDE VIERÃO OS CARROS
lista_cidades_estados = {
    "São Luís" : "MA",
    "Belém" : "PA",
    "Campinas" : "SP",
    "Blumenau" : "SC",
    "São Paulo" : "SP",
    "Florianópolis" : "SC",
    "Joinville" : "SC"
}

lista_ano_carro = (
    2015, 
    2021, 
    2022, 
    2017, 
    2023, 
    2015
)


print(f"Olá, {pedeInform}. Verificamos as informações recebidas e seus carros são: {lista_carros} de ano {lista_ano_carro} vindos de {lista_cidades_estados}")

ptFinal = input("As informações estão corretas? (sim/não):")

if ptFinal == "sim":
    print("Compra finalizada!")
else:
    print("Por favor ligue para (98) 9849-6870 para com nosso time de vendas!")

