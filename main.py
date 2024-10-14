import M_Arquivo
import M_Banco
import Uteis
op = 0
banco=M_Banco.Banco()
while op != 6:
    print("1 - Carregar um arquivo CSV")
    print("2 - Alterar linha de um arquivo")
    print("3 - Deletar arquivo")
    print("4 - Listar arquivos")
    print("5 - Listar as linhas de um arquivo")
    print("6 - Sair")

    try:
        op = int(input("Digite uma opção válida: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    match op:
        case 1:
            while True:
                caminho = input("Digite o caminho do arquivo (exemplo: C:/Users/joao2/Downloads/pool.csv): ")
                csv = M_Arquivo.ler_CSV(caminho)
                if csv != 'ERRO':
                    break
                else:
                    print("Arquivo INVÁLIDO")
            if csv and csv[0] == ['Carro', 'fabrica', 'Valor ', 'ano', 'placa']:
                csv.pop(0)
            if len(csv)>0:
                id_arquivo = banco.inserir_arquivo(Uteis.obter_nome_arquivo(caminho))
                i=1
                linhas_erros=[]
                if id_arquivo !=0:
                    for linha in csv:
                        linha.append(id_arquivo)
                        if banco.add_linha(linha) ==0:
                            linhas_erros.append(i)
                        i+=1
                    print(f"Numeros de linhas com erro foram {len(linhas_erros)}")
                else:
                    print("não foi possivel cadastrar arquivo")

            else:
                print("Nao foi encontrado nenhum dado")
        case 2:
            while (True):
                try:
                    id_da_linha = int(input("Digite um Id de uma linha válida: "))
                    break
                except ValueError:
                    print("Por favor, digite um número válido.")
                    continue
            carro_info = []
            while True:
                try:
                    placa = input("Digite a placa do carro (ex: ABC1234): ").upper().strip()
                    if not placa:
                        raise ValueError("Placa inválida. Deve conter 7 caracteres.")
                    carro_info.append(placa)
                    modelo = input("Digite o modelo do carro: ").strip()
                    if not modelo:
                        raise ValueError("Modelo não pode estar vazio.")
                    carro_info.append(modelo)
                    ano = int(input("Digite o ano do carro (ex: 2023): "))
                    if not ano:
                        raise ValueError("Ano inválido. O ano deve ser entre 1886 e 2024.")
                    carro_info.append(ano)
                    valor = float(input("Digite o valor do carro (ex: 35000.00): "))
                    if valor <= 0:
                        raise ValueError("Valor deve ser positivo e maior que zero.")
                    carro_info.append(valor)
                    fabricante = input("Digite o fabricante do carro: ").strip()
                    if not fabricante:
                        raise ValueError("Fabricante não pode estar vazio.")
                    carro_info.append(fabricante)
                    break

                except ValueError as ve:
                    print(f"Erro de validação: {ve}")
                    print("Por favor, tente novamente.\n")
            arquivo=banco.atualizar_valor(id_da_linha,carro_info)
            if arquivo!=0:
                print("Alterado com sucesso")
            else:
                print("erro na alteração")
        case 3:
            while (True):
                try:
                    id_do_arquivo = int(input("Digite um Id de arquivo válido: "))
                    break
                except ValueError:
                    print("Por favor, digite um número válido.")
                    continue
            arquivo=banco.deletar_arquivo_e_linha(id_do_arquivo)
            if arquivo != 0:
                print(f"Arquivo e linhas deletada com sucesso")
            else:
                print("arquivo não encontrado")
        case 4:
            arquivos=banco.listar_arquivos()
            if arquivos !=0:
                for arquivo in arquivos:
                    print(f"ID: {arquivo[0]} , Nome: {arquivo[1]} e a Data de inserção é {arquivo[2]}")
            else:
                print("arquivo não encontrado")
        case 5:
            while(True):
                try:
                    id_do_arquivo = int(input("Digite um Id de arquivo válido: "))
                    break
                except ValueError:
                    print("Por favor, digite um número válido.")
                    continue
            arquivos = banco.listar_linhas_arquivo(id_do_arquivo)
            if arquivos != 0:
                for arquivo in arquivos:
                    print(f"ID: {arquivo[0]} , Modelo: {arquivo[1]} , Fabricante: {arquivo[2]}, Valor: {arquivo[3]}, Ano: {arquivo[4]}, Placa: {arquivo[5]}")
            else:
                print("arquivo não encontrado")

        case 6:
            print("Saindo...")
            break

        case _:
            print("Opção inválida, tente novamente.")
