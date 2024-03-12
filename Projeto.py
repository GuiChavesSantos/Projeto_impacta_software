import os

funcionarios = []
clientes = [{'nome' , 'cnpj'}]

#Função para exibir o nome do projeto.
def exibir_nome_projeto():
    print('ESCUDO\n')

# Função para exibir o Subtitulos das funções.
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

# Função para voltar ao menu de escolhas.
def voltar_ao_menu():
    input('Aperte qualquer tecla para voltar ao menu principal')
    main()

# Função que exibe as opções disponiveis.
def exibir_opcoes():
    print('1. Cadastrar Funcionarios')
    print('2. Cadastrar Clientes')
    print('3. Liberação de Cesta Basica')
    print('4. Desligar funcionario')
    print('5. Listar Funcionarios \n')

# Função para escolher as opções disponiveis.
def escolher_opcao():
    try:
        
        opcao_escolhida = int(input('Escolha uma opção:'))
        
        if opcao_escolhida == 1:
            cadastrar_funcionario(funcionarios)

        elif opcao_escolhida == 2:
            cadastra_clientes()
        
        elif opcao_escolhida == 3:
            saida_de_cesta_basica()
        
        elif opcao_escolhida == 4:
            desligamento_funcionario (funcionarios)

        elif opcao_escolhida == 5:
            listar_funcionarios(funcionarios)

        else:
            opcao_invalida()
    except:
        opcao_invalida()

# Retorna erro se caso não existir a função
def opcao_invalida():
    print('Esta opção não existe')
    voltar_ao_menu()

#Função para cadastrar os funcionarios.
def cadastrar_funcionario(lista):
    
    exibir_subtitulo('Cadastro de funcionario')
    
    nome_do_funcionario = input('Digite o nome do Funcionario: ')
    cpf_funcinario = int(input(f'\nDigite o CPF do funcionario {nome_do_funcionario}: '))
    fez_exame = input(f'\nEntregou o exame admissional? S/N ')
    
    if fez_exame == 'S':
        
        dados_funcionario = {'nome': nome_do_funcionario, 'cpf' : cpf_funcinario, 'examead': True, 'examedm': False}
        lista.append(dados_funcionario)
        print(f'\nO funcionario {nome_do_funcionario} foi cadastrado com sucesso\n')

    else:
        print('Funcionario não pode ser cadastrado porque não fez o exame')

    voltar_ao_menu()
    return lista

#Função para cadastrar os clientes.
def cadastra_clientes():
    exibir_subtitulo('Cadastro de Clientes')
    nome_do_cliente = input('Digite o nome do Cliente: ')
    cnpj_cliente = int(input (f'\nDigite o CNPJ do cliente {nome_do_cliente}: '))
    dados_cliente = {'nome' : nome_do_cliente, 'cnpj' : cnpj_cliente}
    clientes.append(dados_cliente)
    print(f' O cliente {nome_do_cliente} foi cadastrado com sucesso\n')
    voltar_ao_menu()

#Função para liberação de cesta basica do funcionario.
def saida_de_cesta_basica():
    
    exibir_subtitulo('Liberação de Cesta Basica')

    nome_do_funcionario = input ('Digite o nome do funcionario que irá receber a cesta: ')
    funcionario_encontrado = False
    
    for index in range(len(funcionarios)):
        # print(funcionarios[index])   
       
        if nome_do_funcionario == funcionarios[index]['nome']:
            funcionario_encontrado = True
            data_de_liberação = input('\nDigite a data de liberação: ')
            mensagem = f'\nA cesta do funcionario {nome_do_funcionario} foi liberada com sucesso no dia {data_de_liberação}' 
            print(mensagem)

    if not funcionario_encontrado:
        print('O funcionario não foi encontrado')   
    
    voltar_ao_menu()

#Função para desligar o Funcionario.
def desligamento_funcionario(lista):
    nome_do_funcionario = input('Digite o nome funcionario que voce quer dar baixa: ')
    
    for index in range(len(lista)):
        if nome_do_funcionario == lista[index]['nome']:
            exame_demissional = input('\nO funcionario ja fez o exame demissional? S/N ') 

            if exame_demissional == 'S':
        
                print (' Funcionario Desligado')
                lista.pop(index)
                print (lista)

            else:
                print('Solicite ao funcionario fazer o exame demissional')
        else:
            print('Funcionario não encontrado')

    voltar_ao_menu()

#Listagem de Funcionarios
def listar_funcionarios(lista):
    
    exibir_subtitulo('Listagem de Funcionarios')
    
    for funcionario in lista:
        print(f'nome: {funcionario['nome']}')
        print(f'CPF: {funcionario['cpf']}')
        print(f'Exame Admissional: {funcionario['examead']}')
        print('---------------------------------------------')
        
    voltar_ao_menu()

#Função Main
def main():
    os.system('cls')
    exibir_nome_projeto()
    exibir_opcoes()
    escolher_opcao()
    cadastrar_funcionario()
    cadastra_clientes()
    saida_de_cesta_basica()
    desligamento_funcionario()
    listar_funcionarios()
  
if __name__ == '__main__':
    main()