salario = float(input("Digite o salário para cálculo do imposto (Ex.: 2500.00): "))
ir=0

if salario <=1903.98:
    print ("Insento de imposto")

elif salario  >1903.98 and salario <=2826.65:
    imposto= (salario*0.075)
    ir =salario-imposto
    print ("Imposto é de 7.5%, seu salário com desconto é", ir)

elif salario >=2826.65 and salario <=3751.05:
    imposto= (salario*0.15)
    ir =salario-imposto
    print ("Imposto é de 15%, seu salário com desconto é", ir)    

elif salario >=3751.05 and salario <=4664.68:
    imposto= (salario*0.225)
    ir =salario-imposto
    print ("Imposto é de 22,5%, , seu salário com desconto é", ir)

elif salario >=4664.68:
    imposto= (salario *0.275) 
    ir =salario-imposto
    print ("Imposto é de 27,5%, seu salário com desconto é", ir)
