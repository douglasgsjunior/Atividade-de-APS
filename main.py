import mysql.connector

mydb = mysql.connector.connect(
    database='db_lego',
    host='localhost',
    password='#T3cnol0g1@',
    user='root'
)

mycursor = mydb.cursor()

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Digite sua senha: ")
query = "SELECT * FROM tbl_user WHERE nome=%s AND email=%s AND senha=%s"
values = (nome, email, senha)
mycursor.execute(query, values)

if mycursor.fetchone() is not None:
    print('\nLogin válido!')
    while True:
        print("\nMENU:\n")
        print("1 - Inserir registro")
        print("2 - Atualizar registro")
        print("3 - Deletar registro")
        print("4 - Consultar registro")
        print("5 - Deletar todos os registros")
        print("6 - SAIR")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            input1 = input("Digite o nome do tema: ")
            input2 = input("Digite o nome da caixa: ")
            input3 = input("Digite a quantidade de peças: ")
            input4 = input("Digite a faixa etária: ")
            input5 = input("Digite a quantidade da caixa no estoque: ")
            input6 = input("Digite o preço da caixa: ")

            insert = "INSERT tbl_product (lego_theme, lego_set, piece_count, age_range, amount, price) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(input1, input2, input3, input4, input5, input6)

            mycursor.execute(insert)
            mydb.commit()

            print("\nInserindo registro...")

        elif escolha == "2":
            print("Digite o Tema e Caixa para localizar o registro desejado:\n")

            input1 = input("Digite o nome do tema: ")
            input2 = input("Digite o nome da caixa: ")
            condicao = "lego_theme = '{}' AND lego_set = '{}'".format(input1, input2)

            print("\nProcurando registro...\n")

            input3 = input("Digite a quantidade de peças: ")
            input4 = input("Digite a faixa etária: ")
            input5 = input("Digite a quantidade da caixa no estoque: ")
            input6 = input("Digite o preço da caixa: ")

            update = "UPDATE tbl_product SET piece_count = '{}', age_range = '{}', amount = '{}', price = '{}' WHERE {}".format(input3, input4, input5, input6, condicao)

            mycursor.execute(update)
            mydb.commit()

            print("\nAtualizando registro...")
        elif escolha == "3":
            print("Digite o Tema e Caixa para localizar o registro a ser deletado:\n")

            input1 = input("Digite o nome do tema: ")
            input2 = input("Digite o nome da caixa: ")
            condicao = "lego_theme = '{}' AND lego_set = '{}'".format(input1, input2)

            print("\nProcurando registro a ser deletado...\n")

            delete = "DELETE FROM tbl_product WHERE {}".format(condicao)

            mycursor.execute(delete)
            mydb.commit()

            print("\nDeletando registro...")
        elif escolha == "4":
            print("Digite o Tema e Caixa para realizar a consulta:\n")

            input1 = input("Digite o nome do tema: ")
            input2 = input("Digite o nome da caixa: ")
            condicao = "lego_theme = '{}' AND lego_set = '{}'".format(input1, input2)

            print("\nProcurando registro...\n")

            select = "SELECT * FROM tbl_product WHERE {}".format(condicao)

            mycursor.execute(select)
            result = mycursor.fetchone()

            if result is not None:
                print("Registro encontrado:\n")
                print(result)
            else:
                print("Registro não encontrado.")

        elif escolha == "5":
            truncate = "TRUNCATE TABLE tbl_product"

            print("\nLimpando tabela...")

            mycursor.execute(truncate)
        elif escolha == "6":
            print("Saindo do menu...")
            break
        else:
            print("Opção inválida! Tente novamente.")
else:
    print('\nLogin inválido.')

mycursor.close()
mydb.close()