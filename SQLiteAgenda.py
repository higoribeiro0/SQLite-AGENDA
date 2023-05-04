import os
import sqlite3
from sqlite3 import Error

###Conexão
def ConexaoBanco():
    caminho="D:\\Python\\Aulas\\Banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c=execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com Sucesso")
        #conexao.close()

def consultar(conexao,sql):
        c=conexao.cursor()
        c=execute(sql)
        res=c.fetchall()
        #conexao.close()
        return res

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro por ID")
    print("5 - Consultar Registro por Nome")
    print("6 - sair")

def menuInserir():
    os.system("cls")
    vnome=input("Digite o Nome: ")
    vtelefone=input("Digite o Telefone: ")
    vemail=input("Digite o Email: ")
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    query(vsql,vsql)

def menuDeletar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser deletado: ")
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="+vid
    query(vsql,vsql)

def menuAtualizar():
    os.system("cls")
    vid=input("Digite o ID do registro a ser alterado: ")
    r=consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
    rnome=[0][1]
    rtelefone=[0][2]
    remail=[0][3]
    vnome=input("Digite o Nome: ")
    vtelefone=input("Digite o Telefone: ")
    vemail=input("Digite o Email: ")
    if(len(vnome)==0):
        vnome=rnome
    if(len(vtelefone)==0):
        vtelefone=rtelefone
    if(len(vemail)==0):
        vemail=remail
    vsql="UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"',T_TELEFONECONTATO='"+vtelefone+"',T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATO"+vid
    query(vsql,vsql)

def menuConsultar():
    vsql="SELECT * FROM tb_contatos"
    res=consultar(vcon,vsql)
    vlim=10
    vcon=0
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} E-mail:{3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcon+=1
        if(vcon>=vlim):
            vcon=0
            os.system("pause")
            os.system("cls")
        print("Fim da Lista")
        os.system("pause")

def menuConsultarNomes():
    vnome=input("Digite o Nome: ")
    vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%'"
    res=consultar(vcon,vsql)
    vlim=10
    vcon=0
    for r in res:
        print("ID:{0:_<3} Nome:{1:_<30} Telefone:{2:_<14} E-mail:{3:_<30}".format(r[0],r[1],r[2],r[3]))
        vcon+=1
        if(vcon>=vlim):
            vcon=0
            os.system("pause")
            os.system("cls")
        print("Fim da Lista")
        os.system("pause")

opc=0
while opc !=6:
    menuPrincipal()
    opc=int(input("Digite uma opção: "))
    if opc==1:
        menuInserir()
    if opc==2:
        menuDeletar()
    if opc==3:
        menuAtualizar()
    if opc==4:
        menuConsultar()
    if opc==5:
        menuConsultarNomes()
    if opc==6:
        os.system("cls")
        print("Programa Finalizado")
    else:
        os.system("cls")
        print("Opção Invalida")
        os.system("pause")

