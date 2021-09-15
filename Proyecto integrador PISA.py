import random
import math
def pitagoras():
    score = 0

    #Problema 1
    a = random.randint(1,10)
    b = random.randint(1,10)
    userAnswer = float(input("En un triángulo rectángulo, la longitud de uno de sus catetos es de "+str(a)+" centímetros. El otro cateto es de "+str(b)+" centímetros. Encuentre la longitud de la hipotenusa. Redondea tu respuesta a dos espacios decimales: "))
    correctAnswer = math.hypot(a,b)
    if abs(correctAnswer - userAnswer) < 0.01:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")


    #Problema 2
    a = random.randint(1,10)
    b = random.randint(1,10)
    while a<=b:
        a = random.randint(1,10)
        b = random.randint(1,10)
    userAnswer = float(input("En un triángulo rectángulo, la longitud de la hipotenusa es de "+str(a)+" metros, y la longitud de uno de sus catetos es de "+str(b)+" metros. Encuentre la longitud del otro cateto. Redondea tu respuesta a dos espacios decimales: "))
    correctAnswer = math.sqrt(a*2-b*2)
    if abs(correctAnswer - userAnswer) < 0.01:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")


    #Problema 3
    a = random.randint(1,10)
    userAnswer = float(input("La hipotenusa de un triángulo rectángulo es "+str(a)+" pulgadas más larga que el cateto más largo. El cateto más corto es "+str(a)+" pulgadas más corto que el cateto más largo. Calcula la longitud de la hipotenusa: "))
    correctAnswer = 5*a
    if userAnswer == correctAnswer:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")


    #Problema 4
    a = random.randint(1,10)
    userAnswer = float(input("Carrie y Sarah viven en el mismo apartamento. Ambas salen al mismo tiempo: Carrie va hacia su trabajo que esta al sur, y Sarah va hacia el este. Cuando Carrie está a "+str(5*a)+" millas de su apartamento, la distancia entre ellas es de "+str(a)+" milla más que la distancia de Sarah desde el apartamento. ¿A qué distancia del apartamento está Sarah? "))
    correctAnswer = 12*a
    if userAnswer == correctAnswer:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")


    #Problema 5
    a = random.randint(1,10)
    userAnswer = float(input("Un cable “guy-wire” está conectado a un poste telefónico. La distancia desde el punto donde el cable toca el suelo hasta la base del poste telefónico es 4 pies menos que la longitud del cable. ¿A qué altura del poste telefónico está conectado el cable si la distancia desde el suelo hasta donde el cable está conectado al poste es 2 pies menos que la longitud del cable? "))
    correctAnswer = 8*a
    if userAnswer == correctAnswer:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")

    print("Tu puntaje final es de "+str(score))

def algebra():
    score = 0
    print("Resuelve para 'x' las siguientes ecuaciones:")

    #Problema 1
    a = random.randint(2,10)
    b = random.randint(2,10)
    userAnswer = int(input(str(a)+"x = "+str(a*b)+"; x = "))
    correctAnswer = b
    if userAnswer == correctAnswer:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")

    #Problema 2
    a = random.randint(5,12)
    userAnswer = int(input("x^3 - "+str(a**3)+" = 0; x = "))
    correctAnswer = a
    if userAnswer == correctAnswer:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")

    #Problema 3
    a = random.randint(11,19)
    userAnswer = int(input("0 = (x - "+str(a)+")^3; x = "))
    correctAnswer = a
    if userAnswer == correctAnswer:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")
    
    #Problema 4
    a = random.randint(2,4)
    b = random.randint(2,4)
    c = random.randint(3,5)
    d = random.randint(3,5)
    e = random.randint(1,3)
    userAnswer = float(input(str(a)+"("+str(b)+"x - "+str(c)+") = "+str(d)+"(x + "+str(e)+"); Redondea tu respuesta a dos espacios decimales; x = "))
    correctAnswer = (a*c + d*e)/(a*b - d)
    if abs(correctAnswer - userAnswer) < 0.01:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")
    
    #Problema 5
    a = random.randint(2,5)
    b = random.randint(5,9)
    c = random.randint(2,5)
    d = random.randint(5,9)
    e = random.randint(2,5)
    userAnswer = float(input("("+str(a)+"x + "+str(b)+") / ("+str(c)+"x - "+str(d)+") = "+str(e)+"; Redondea tu resuesta a dos espacios decimales; x = "))
    correctAnswer = (-b - e*d)/(a - e*c)
    if abs(correctAnswer - userAnswer) < 0.01:
        print("Correcto")
        score += 20
    else:
        print("Incorrecto")

    print("Tu puntaje final es de "+str(score))

def volume():
    counter = 0
    #problema 1  
    #se general tres tipos de valores random que será utilizados para las operaciones
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    c = random.randint(1,1000)
    userResponse = float(input("¿Cuántos peces, pequeños o medianos, se pueden introducir en un acuario cuyas medidas interiores son " + str(a) + " x " + str(b) + " x " + str(c) +" cm? (Se recomienda introducir, a lo sumo, un pez mediano o pequeño cada cuatro litros de agua):  "))
    answerKey = (a * b * c) / 4
    
    if abs(answerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter = counter + 20
    else:
        print('🚫❌ Sigue practicando! 😅')
        
    #problema 2
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    userResponse = float(input('La base de esta pirámide es un polígono de 5 lados regular con medida de lado ' + str(a) +' cm y apotema ' + str(b) + ' cm. Calcula su volumen sabiendo que su altura es ' + str(c) +  'cm'))
    base =  (5*a*b)/2
    anwerKey = (base*c)/3262
    if abs(anwerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter = counter + 20
    else:
        print('🚫❌ La tercera es la vencida! 😅')
        
    #problema 3
    a = random.randint(1,10)
    b = random.randint(1,10)
    userResponse = float(input('¿Cuántas copas se pueden llenar con 6 litros de refresco, si el recipiente cónico de cada copa tiene una altura interior de ' + str(a) + ' cm y un radio interior de ' + str(b) + ' cm? Recuerda que un ml^3 es un cm^3 y viceversa, la medida de la copa es en mililitros:  '))
    capacidadCopa = (math.pi* a * b**2)/3
    anwerKey = 6000/capacidadCopa
    
    if abs(anwerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter = counter + 20
    else:
        print('🚫❌ Los primeros serán los últimos y los últimos los primeros! 😅')
        
    #problema 4
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    userResponse = float(input('La base de un prisma hexagonal de lado '+ str(a) +' cm y apotema de '+ str(b) +' cm. Calcula su volumen sabiendo que su altura es '+ str(c) +' cm '))
    answerKey = ((6*a*b)/2)*c
    if abs(anwerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter = counter + 20
    else:
        print('🚫❌ Ya casi lo logras! 😅')
        
        
    #problema 5
    a = random.randint(1,10)
    userResponse = float(input('Calcula, por tanteo, la longitud de la arista de un cubo de ' + str(a**3) + ' m3 de volumen'))
    answerKey = (a**3/a)/a
    if abs(anwerKey - userResponse) < 0.1:
        print('Genial, +20 puntos! ✅')
        counter = counter + 20
    else:
        print('🚫❌ Corto pero divertido camino! 😅')
    print('Felicidades, obtuviste un total de: ' + str(counter) + 'puntos!! ')

def trigonometry():
    counter2 = 0
    #los nombres de ambas variables se conservan puesto que se habla de funciones distintas
    #Problema1
    a = random.randint(1,100) #definir valor de la hipotenusa
    b = random.randint(2,88)  #definir valor del ángulo

    userResponse = float(input('Nota: recuerda que el resultado de tus catetos puede ser positivo o negativos o positivos, esto no es malo, sólo mueestra que tan a la izquierda o derecha, arriba o abajo, se encuentran estos lados del cero, así también puede ser determinado por el ángulo'+ '\n' + "" + 'Encuentra el valor del cateto opuesto de un triángulo rectángulo dado el valor de su hipotenusa igual a '+ str(a) +' y un ángulo de '+ str(b) +'°'))
    answerKey = math.degrees(math.sin(b)*a)
    if abs(answerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter2 = counter2 + 20
    else:
        print('🚫❌ Sigue practicando! 😅')
        
    #Problema2
    a = random.randint(1,100)
    userResponse = float(input('Calcula la base de dos triángulos rectángulos unidos cuya altura (cateto opuesto) tiene un valor de '+ str(a) +' metros y dos magnitudes angulares de 26 y 36 grados respectivamente.'))
    answerKey = math.degrees(((math.atan(26))*a) + ((math.atan(36))*a))    
    if abs(answerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter2 = counter2 + 20
    else:
        print(' 🚫❌ La tercera es la vencida! 😅')
        
    #Problema3
    a = random.randint(200,828) #obtener la altura del edificio
    b = random.randint(30,70)  #definir valor del ángulo, se ponen el valores un tanto medianos en la suma de los ángulo par que tenga coherencia con la altura
    userResponse = float(input('Desde un supermercado se observa el ático de un rascacielos de '+ str(a) +' metros de altura bajo un ángulo de '+ str(b) +'°. Calcular la distancia de la sombra reflejada que hay desde el supermercado hasta la puerta del rascacielos.'))
    answerKey = math.degrees((math.atan(b))*a)
    if abs(answerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter2 = counter2 + 20
    else:
        print('🚫❌ Los primeros serán los últimos y los últimos los primeros! 😅')
        
    #Problema4
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    c = random.randint(1,1000)
    userResponse = float(input('Obtén el valor inverso del coseno si dicho triángulo rectángulo cuenta con una altura de '+ str(a) +' metros, una base de '+ str(b) +' metros y una hipotenusa de '+ str(c) +' metros '))
    answerKey = c/b
    if abs(answerKey - userResponse) < 0.01:
        print('Genial, +20 puntos! ✅')
        counter2 = counter2 + 20
    else:
        print('🚫❌ Ya casi lo logras! 😅')
        
    #Poblema5
        
    
    a= round(random.random(),4)
    b = round(random.random(),4)
    c = round(random.random(),4)
    d = round(random.random(),4)
    e = round(random.random(),4)
    
    print ('(Con calculadora) Calcular los ángulos α sabiendo cuánto valen su seno o su coseno. Redondea a dos espacios decimales')
    userResponse = float(input('sin(α)=' + str(a)))
    userResponse2 = float(input('cos(α)=' + str(b)))
    userResponse3 = float(input('sin(α)=' + str(c)))
    userResponse4 = float(input('cos(α)=' + str(d)))
    userResponse5 = float(input('cos(α)=' + str(e)))
    
    key1 = math.degrees(math.asin(a))
    key2 = math.degrees(math.acos(b))
    key3 = math.degrees(math.asin(c))
    key4 = math.degrees(math.acos(d))
    key5 = math.degrees(math.acos(e))
    
    respuestasss = [key1, key2,key3,key4,key5]
    humanoResponsee = [userResponse,userResponse2,userResponse3,userResponse4,userResponse5]
    
    for i in range(0,5):
        if abs(humanoResponsee[i] - respuestasss[i]) < 0.01:
            print('Genial, + 4 puntos! ✅')
            counter2 = counter2 + 4
        else:
            print('🚫❌ Más suerte a la próxima! 😅')
    print('Felicidades, obtuviste un total de: ' + str(counter2) + 'puntos!! ')


#Inicio
print("Bienvenido al repaso para el examen PISA")

while True:
    #El programa imprime la lista de opciones que puede elegir el usuario
    mynewhandle = open("project.txt", "r")
    while True:
        theline = mynewhandle.readline()
        if len(theline) == 0:
            break
        print(theline, end="")
    mynewhandle.close()

    #El usuario elige una de las opciones
    user = int(input(""))
    if user == 1:
        pitagoras()
    elif user == 2:
        algebra()
    elif user == 3:
        volume()
    elif user == 4:
        trigonometry()
    elif user == 5:
        break
    else:
        print("Numero invalido.")
print("Hasta la proxima!")