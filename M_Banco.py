import mysql.connector


#finalizado banco
#Criar a classe para conecção
class Banco:
    def __init__(self):
        pass

    def inserir_arquivo(self, nome_arquivo):
        try:
            self.conectar_banco()
            sql_inserir = """
                   INSERT INTO arquivos (nome, data)
                   VALUES (%s, NOW());
               """
            with self._meuDB.cursor() as mycursor:
                mycursor.execute(sql_inserir, (nome_arquivo,))
                self._meuDB.commit()

                # Retorna o ID do arquivo inserido
                return mycursor.lastrowid

        except Exception as e:
            print(f"Erro ao inserir arquivo: {e}")
            self._meuDB.rollback()
            return 0

        finally:
            self.desconectar()

    def conectar_banco(self):
        try:
            self._meuDB = mysql.connector.connect(
                host="localhost",
                user='root',
                password='',
                database='project_python'
            )
            return 1
        except:
            return 0
    def add_linha(self,lista):
        try:
            self.conectar_banco()
            sql = " INSERT INTO carros (Modelo, Fabricante, Valor, Ano, Placa,Id_arquivo)  VALUES (%s, %s, %s, %s, %s, %s);"
            with self._meuDB.cursor() as mycursor:
                mycursor.execute(sql, lista)
                self._meuDB.commit()
            return 1
        except Exception:
            self._meuDB.rollback()
            return 0
        finally:
            self.desconectar()
    def remover_linha(self,index):
        self.conectar_banco()
        sql = "DELETE FROM carros WHERE id="+str(index)+";"
        mycursor = self._meuDB.cursor()
        mycursor.execute(sql)
        self._meuDB.commit()
        self.desconectar()
    def listar(self):
        self.conectar_banco()
        mycursor = self._meuDB.cursor()
        sql = "SELECT * FROM carros"
        mycursor.execute(sql)
        resultados = mycursor.fetchall()
        self.desconectar()
        return resultados
    def desconectar(self):
        self._meuDB.close()
    def verifica_conecção(self):
        try:
            self._meuDB = mysql.connector.connect(
                host="localhost",
                user='root',
                password='',
                database='project_python'
            )
            self._meuDB.close()
            return 1
        except:
            return 0

    def listar_arquivos(self):
        try:
            self.conectar_banco()
            sql_listar = "SELECT * FROM arquivos;"
            with self._meuDB.cursor() as mycursor:
                mycursor.execute(sql_listar)
                arquivos = mycursor.fetchall()

            return arquivos

        except Exception as e:
            return 0

        finally:
            self.desconectar()

    def listar_linhas_arquivo(self,id):
        try:
            self.conectar_banco()
            sql_listar = "SELECT * FROM carros where Id_arquivo = %s;"
            with self._meuDB.cursor() as mycursor:
                mycursor.execute(sql_listar,(id,))
                arquivos = mycursor.fetchall()

            return arquivos

        except Exception as e:
            return 0

        finally:
            self.desconectar()

    def deletar_arquivo_e_linha(self, id_arquivo):
        try:
            # Conectar ao banco de dados
            self.conectar_banco()

            # Query para deletar da tabela 'carros'
            sql_deletar_carros = "DELETE FROM carros WHERE id_arquivo = %s;"
            sql_deletar_arquivo = "DELETE FROM arquivos WHERE id = %s;"
            with self._meuDB.cursor() as mycursor:
                mycursor.execute(sql_deletar_carros, (id_arquivo,))
                mycursor.execute(sql_deletar_arquivo, (id_arquivo,))
                self._meuDB.commit()
            return 1
        except Exception as e:
            self._meuDB.rollback()
            return 0
        finally:
            self.desconectar()

    def atualizar_valor(self, id_arquivo, carro):
        """
        Atualiza os dados de um carro na tabela 'carros' com base no id_arquivo.

        Parâmetros:
            id_arquivo (int): O ID do arquivo que será utilizado na condição da consulta.
            carro (list): Lista contendo os valores [Placa, Modelo, Ano, Valor, Fabricante].

        Retorna:
            int: Retorna 1 se a atualização for bem-sucedida, 0 em caso de erro.
        """
        try:
            print(id_arquivo)
            self.conectar_banco()
            sql_atualizar = "UPDATE carros SET Placa=%s, Modelo=%s, Ano=%s, Valor=%s, Fabricante=%s WHERE id = %s;"
            with self._meuDB.cursor() as mycursor:
                # Adiciona os valores da lista carro + id_arquivo como último parâmetro
                mycursor.execute(sql_atualizar, (*carro, id_arquivo))
                self._meuDB.commit()
            return 1
        except Exception as e:
            print(f"Erro ao atualizar carro: {e}")
            self._meuDB.rollback()
            return 0
        finally:
            self.desconectar()


