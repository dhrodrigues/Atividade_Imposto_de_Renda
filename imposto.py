salário = float(input("Digite o salário para cálculo do imposto (Ex.: 2500.00): "))


if salário >1903.98 and salário <=2826.65:
    imposto= (salário / 100) * 7.5 
      
if salário >2826.66 and salário <=3751.05:
    imposto= (salário / 100) * 15 

if salário >3751.06 and salário <=4664.68:
    imposto= (salário / 100) * 22.5 

if salário >=4664.68:
    imposto= (salário / 100) * 27.5 

print(salário)
print(imposto)