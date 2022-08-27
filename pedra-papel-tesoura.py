from random import randrange
from time import sleep

print("Bem vindo ao jogo do pedra papel e tesoura!")
sleep(2)
resposta = input("escolha entre pedra, papel ou tesoura: ")
  
altorg = randrange(1,3)
if altorg == 1 :
    ppt = "papel"
    print("Cleitinho jogou papel!")
elif altorg == 2 :
    ppt = "pedra"
    print("Cleitinho jogou pedra!")
elif altorg == 3 :
    ppt = "tesoura"
    print("Cleitinho jogou tesoura!")
  
print("Calculando resultado...")  
sleep(5)
  
if resposta  == ppt :
    print("Empate!")
    print("Tente novamente")
elif resposta  == "" :
    print("Erro, digite pedra, papel ou tesoura corretamente!")

if resposta  == "pedra" and ppt == "tesoura":
    print("Você venceu!")
elif resposta  == "" :
    print("Erro, digite pedra, papel ou tesoura corretamente!")
    
if resposta  == "tesoura" and ppt == "pedra":
    print("Você perdeu!")
    print("Tente novamente")
elif resposta  == "" :
    print("Erro, digite pedra, papel ou tesoura corretamente!")
    
if resposta  == "tesoura" and ppt == "papel":
    print("Você ganhou!")
elif resposta  == "" :
    print("Erro, digite pedra, papel ou tesoura corretamente!")
    
if  resposta  == "papel" and ppt == "tesoura":
    print("Você perdeu!")
    print("Tente novamente")
elif resposta  == "" :
    print("Erro, digite pedra, papel ou tesoura corretamente!")
    
if resposta  == "papel" and ppt == "pedra":
    print("Você gannou!")
elif resposta  == "" :
    print("Erro, digite pedra, papel ou tesoura corretamente!")
    
if resposta  == "pedra" and ppt == "papel":
    print("Você perdeu!")
    print("Tente novamente")
elif resposta  == "" :
    print("Erro, digite pedra, papel ou tesoura corretamente!")
    
sleep(2)

print("Obrigado por jogar! siga @py.theuz no instagram")

sleep(2)
