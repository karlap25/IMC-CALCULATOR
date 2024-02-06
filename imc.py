### Calculadora de IMC 
## variables a ingresar
peso = float(input("Ingresa tu peso en k:ilogramos "))
altura = float(input("Ingresa tu altura en metros: "))
nombre = input("Ingrese su nombre: ")

##Calculo de IMC
imc = peso / (altura  ** 2)
## categorias segun resultado
if imc < 18.5:
    categoria = "peso bajo"
elif imc >= 18.5 and imc <= 24.9:
    categoria = "peso_normal"
elif imc >= 25 and imc <= 29.9:
    categoria = "sobrepeso"
elif imc  >= 30 and imc <= 34.9:
    categoria = "obesidad"
elif imc  >= 35 and imc <= 39.9:
    categoria = "obesidad II"
elif imc  >= 40 and imc <= 49.9:
    categoria = "obesidad III"
else:
    categoria = "obesidad IV"

## resultado
    
print(f"{nombre} tu IMC es: {imc} y estás en {categoria}")

