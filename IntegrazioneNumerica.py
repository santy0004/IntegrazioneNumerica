#f(x) definiamo la funzione da integrare
#f_2(x) definiamo la derivata seconda per ridurre l'errore
#d_4(x) definiamo la derivata 4 per ridurre l'errore
#errore calcolo dell'errore



#>>>>>>>>>>>>>>>>>>>>>>>>> Regola Parabola >>>>>>>>>>>>>>>>>>>>>>>>>
def f(x):
    return x**7

def d_4(x):
    return 840*(x**3)

def Parabola(f, a, b, n):
    h = (b - a) / n
    integrale = f(a) + f(b)
    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0:
            integrale += 2*f(x)
        else:
            integrale += 4*f(x)
    return integrale * h / 3

def errparab(a, b, n):
    M = max([abs(d_4(x)) for x in [a, b]])
    return (b-a)**5 / (2880*n**4) * M

#>>>>>>>>>>>>>>>>>>>>>>>>> Regola dei Rettangoli >>>>>>>>>>>>>>>>>>>>>>>>>
def f(x):
    return x**7

def f_2(x):
    return (x**6)*7

def Rettangolo(f, a, b, n):
    h = (b - a) / n
    integrale = 0
    for i in range(n):
        x = a + i*h
        integrale += f(x)
    return integrale * h

def errrett(a, b, n):
    M = max([f_2(x) for x in [a, b]])
    return M * (b-a)**2 / (2*n)

#>>>>>>>>>>>>>>>>>>>>>>>>> Regola dei trapezi >>>>>>>>>>>>>>>>>>>>>>>>>
def f(x):
    return x**7

def f_2(x):
    return (x**6)*7

def Trapezi(f, a, b, n):
    h = (b-a)/n
    s = 0.5*(f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return h*s
 
def errtrap(a, b, n):
    M = max([abs(f_2(x)) for x in [a, b]])
    return M * (b-a)**3 / (12*n**2)

#>>>>>>>>>>>>>>>>>>>>>>>>> Scelta >>>>>>>>>>>>>>>>>>>>>>>>>
def sceglimet():
    print("Scegli il metodo di integrazoione:")
    print("1. Regola dei Trapezi")
    print("2. Regola dei Rettangoli")
    print("3. Regola Parabola")
    print("4. Esci")
    metodo = int(input())
    return metodo

a = float(input("Inserisci il punto a: "))
b = float(input("Inserisci il punto b: "))
n = int(input("Inserisci il numero del intervallo: "))
while True:
    metodo = sceglimet()
    if metodo == 1:
        print("L'integrale della funzione f(x) è", Trapezi(f, a, b, n))
        print("L'errore è <= ", errparab(a, b, n))
    elif metodo == 2:
        print("L'integrale della funzione f(x) è", Rettangolo(f, a, b, n))
        print("L'errore è <= ", errrett(a, b, n))
    elif metodo == 3:
        print("L'integrale della funzione f(x) è", Parabola(f, a, b, n))
        print("L'errore è <= ", errtrap(a, b, n))
    else:
        print("scelta non disponibile")