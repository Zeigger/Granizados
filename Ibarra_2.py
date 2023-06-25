import os
from datetime import datetime
prom=input("Es dia de promoción?(S/N): ")
precio1=0
pedido1= []
precio2=0
pedido2= []
precio3=0
pedido3= []
precio4=0
pedido4= []
precio5=0
pedido5= []
precio6=0
pedido6= []
precio7=0
pedido7= []
while True:
    mesa=int(input("Ingrese el número de mesa: "))
    if mesa==1:
        print("Haz elegido la mesa 1")
        accion=input("¿Que vas a hacer con esa mesa?(F/C/A): ")
        if accion.lower()=="c":
            print("La orden de la mesa es:", pedido1)
            print("El valor total de la compra es de:", precio1)
        elif accion.lower()=="f":
            file=with open(r"..\registro_pedidos_mesa_1.txt", "w") as file:
                file.write("--------------------\n")
                file.write("Registros de pedidos mesa #1 "+str(datetime.now())+"\n")
                file.write("--------------------\n")
                file.write("Productos pedidos:\n")
                for item in pedido1:
                    file.write("- " + item + "\n")
                file.write("Total de compra: " + str(precio1) + "\n")
                pedido1=[]
                precio1=0
        elif accion.lower()=="a":
            while True:
                tipo=input("Qué tipo de producto es(G/B): ")
                if tipo.lower()=="g":
                    print("Granizados")
                    print("1: Pequeño")
                    print("2: Mediano")
                    print("3: Grande")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        if cantidad%2==0 and prom.lower()=="s":
                            precio1=precio1+(cantidad*7000)
                            pedido1.append(str(cantidad)+" Granizado pequeño")
                        else:
                            precio1=precio1+(((cantidad-1)*7000)+9000)
                            pedido1.append(str(cantidad)+" Granizado pequeño")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*15000)
                        pedido1.append(str(cantidad)+" Granizado mediano")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*20000)
                        pedido1.append(str(cantidad)+" Granizado grande")
                    else:
                        print("Producto inexistente en la base de datos")
                elif tipo.lower()=="b":
                    print("Bebidas")
                    print("1: Fourloko")
                    print("2: Smirnoff")
                    print("3: Coronita")
                    print("4: Budweiser")
                    print("5: Gordon´s")
                    print("6: Corona Tropical")
                    print("7: Agua")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*20000)
                        pedido1.append(str(cantidad)+" Fourloko")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*15000)
                        pedido1.append(str(cantidad)+" Smirnoff")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*6000)
                        pedido1.append(str(cantidad)+" Coronita")
                    elif producto==4:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*6000)
                        pedido1.append(str(cantidad)+" Budweiser")
                    elif producto==5:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*12000)
                        pedido1.append(str(cantidad)+" Gordon´s")
                    elif producto==6:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*6000)
                        pedido1.append(str(cantidad)+" Corona Tropical")          
                    elif producto==7:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio1=precio1+(cantidad*2000)
                        pedido1.append(str(cantidad)+" Agua")          
                    else:
                        print("Producto inexistente en la base de datos")
                    adicion=input("Desea algun shot?(S/N): ")
                    if adicion.lower()=="s":
                        can_adicion=int(input("Cuantos shots?: "))
                        if can_adicion%2==0:
                            precio1=precio1+(can_adicion*2500)
                            pedido1.append(str(cantidad)+" Shot")
                        else:
                            precio1=precio1+(((can_adicion-1)*2500)+3000)
                            pedido1.append(str(cantidad)+" Shot")
                    else:
                        pass
                else:
                    print("Tipo de producto invalido")
                continuacion = input("¿Deseas agregar otro producto? (S/N): ")
                if continuacion.lower() == "s":
                    pass
                else:
                    print("Los productos pedidos fueron:", pedido1)
                    print("El valor total de la compra es de:", precio1)
                    break
        else:
            print("Opción no valida")
    elif mesa==2:
        print("Haz elegido la mesa 2")
        accion=input("¿Que vas a hacer con esa mesa?(F/C/A): ")
        if accion.lower()=="c":
            print("La orden de la mesa es:", pedido2)
            print("El valor total de la compra es de:", precio2)
        elif accion.lower()=="f":
            with open(r"C:\Users\sebas\OneDrive\Escritorio\registro_pedidos_mesa_2.txt", "a") as file:
                file.write("--------------------\n")
                file.write("Registros de pedidos mesa #2 "+str(datetime.now())+"\n")
                file.write("--------------------\n")
                file.write("Productos pedidos:\n")
                for item in pedido2:
                    file.write("- " + item + "\n")
                file.write("Total de compra: " + str(precio2) + "\n")
                pedido2=[]
                precio2=0
        elif accion.lower()=="a":
            while True:
                tipo=input("Qué tipo de producto es(G/B): ")
                if tipo.lower()=="g":
                    print("Granizados")
                    print("1: Pequeño")
                    print("2: Mediano")
                    print("3: Grande")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        if cantidad%2==0 and prom.lower()=="s":
                            precio2=precio2+(cantidad*7000)
                            pedido2.append(str(cantidad)+" Granizado pequeño")
                        else:
                            precio2=precio2+(((cantidad-1)*7000)+9000)
                            pedido2.append(str(cantidad)+" Granizado pequeño")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*15000)
                        pedido2.append(str(cantidad)+" Granizado mediano")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*20000)
                        pedido2.append(str(cantidad)+" Granizado grande")
                    else:
                        print("Producto inexistente en la base de datos")
                elif tipo.lower()=="b":
                    print("Bebidas")
                    print("1: Fourloko")
                    print("2: Smirnoff")
                    print("3: Coronita")
                    print("4: Budweiser")
                    print("5: Gordon´s")
                    print("6: Corona Tropical")
                    print("7: Agua")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*20000)
                        pedido2.append(str(cantidad)+" Fourloko")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*15000)
                        pedido2.append(str(cantidad)+" Smirnoff")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*6000)
                        pedido2.append(str(cantidad)+" Coronita")
                    elif producto==4:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*6000)
                        pedido2.append(str(cantidad)+" Budweiser")
                    elif producto==5:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*12000)
                        pedido2.append(str(cantidad)+" Gordon´s")
                    elif producto==6:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*6000)
                        pedido2.append(str(cantidad)+" Corona Tropical")          
                    elif producto==7:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio2=precio2+(cantidad*2000)
                        pedido2.append(str(cantidad)+" Agua")          
                    else:
                        print("Producto inexistente en la base de datos")
                    adicion=input("Desea algun shot?(S/N): ")
                    if adicion.lower()=="s":
                        can_adicion=int(input("Cuantos shots?: "))
                        if can_adicion%2==0:
                            precio2=precio2+(can_adicion*2500)
                            pedido2.append(str(cantidad)+" Shot")
                        else:
                            precio2=precio2+(((can_adicion-1)*2500)+3000)
                            pedido2.append(str(cantidad)+" Shot")
                    else:
                        pass
                else:
                    print("Tipo de producto invalido")
                continuacion = input("¿Deseas agregar otro producto? (S/N): ")
                if continuacion.lower() == "s":
                    pass
                else:
                    print("Los productos pedidos fueron:", pedido2)
                    print("El valor total de la compra es de:", precio2)
                    break
        else:
            print("Opción no valida")
    elif mesa==3:
        print("Haz elegido la mesa 3")
        accion=input("¿Que vas a hacer con esa mesa?(F/C/A): ")
        if accion.lower()=="c":
            print("La orden de la mesa es:", pedido3)
            print("El valor total de la compra es de:", precio3)
        elif accion.lower()=="f":
            with open(r"C:\Users\sebas\OneDrive\Escritorio\registro_pedidos_mesa_3.txt", "a") as file:
                file.write("--------------------\n")
                file.write("Registros de pedidos mesa #3 "+str(datetime.now())+"\n")
                file.write("--------------------\n")
                file.write("Productos pedidos:\n")
                for item in pedido3:
                    file.write("- " + item + "\n")
                file.write("Total de compra: " + str(precio3) + "\n")
                pedido3=[]
                precio3=0
        elif accion.lower()=="a":
            while True:
                tipo=input("Qué tipo de producto es(G/B): ")
                if tipo.lower()=="g":
                    print("Granizados")
                    print("1: Pequeño")
                    print("2: Mediano")
                    print("3: Grande")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        if cantidad%2==0 and prom.lower()=="s":
                            precio3=precio3+(cantidad*7000)
                            pedido3.append(str(cantidad)+" Granizado pequeño")
                        else:
                            precio3=precio3+(((cantidad-1)*7000)+9000)
                            pedido3.append(str(cantidad)+" Granizado pequeño")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*15000)
                        pedido3.append(str(cantidad)+" Granizado mediano")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*20000)
                        pedido3.append(str(cantidad)+" Granizado grande")
                    else:
                        print("Producto inexistente en la base de datos")
                elif tipo.lower()=="b":
                    print("Bebidas")
                    print("1: Fourloko")
                    print("2: Smirnoff")
                    print("3: Coronita")
                    print("4: Budweiser")
                    print("5: Gordon´s")
                    print("6: Corona Tropical")
                    print("7: Agua")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*20000)
                        pedido3.append(str(cantidad)+" Fourloko")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*15000)
                        pedido3.append(str(cantidad)+" Smirnoff")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*6000)
                        pedido3.append(str(cantidad)+" Coronita")
                    elif producto==4:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*6000)
                        pedido3.append(str(cantidad)+" Budweiser")
                    elif producto==5:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*12000)
                        pedido3.append(str(cantidad)+" Gordon´s")
                    elif producto==6:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*6000)
                        pedido3.append(str(cantidad)+" Corona Tropical")          
                    elif producto==7:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio3=precio3+(cantidad*2000)
                        pedido3.append(str(cantidad)+" Agua")          
                    else:
                        print("Producto inexistente en la base de datos")
                    adicion=input("Desea algun shot?(S/N): ")
                    if adicion.lower()=="s":
                        can_adicion=int(input("Cuantos shots?: "))
                        if can_adicion%2==0:
                            precio3=precio3+(can_adicion*2500)
                            pedido3.append(str(cantidad)+" Shot")
                        else:
                            precio3=precio3+(((can_adicion-1)*2500)+3000)
                            pedido3.append(str(cantidad)+" Shot")
                    else:
                        pass
                else:
                    print("Tipo de producto invalido")
                continuacion = input("¿Deseas agregar otro producto? (S/N): ")
                if continuacion.lower() == "s":
                    pass
                else:
                    print("Los productos pedidos fueron:", pedido3)
                    print("El valor total de la compra es de:", precio3)
                    break
        else:
            print("Opción no valida")
    elif mesa==4:
        print("Haz elegido la mesa 4")
        accion=input("¿Que vas a hacer con esa mesa?(F/C/A): ")
        if accion.lower()=="c":
            print("La orden de la mesa es:", pedido4)
            print("El valor total de la compra es de:", precio4)
        elif accion.lower()=="f":
            with open(r"C:\Users\sebas\OneDrive\Escritorio\registro_pedidos_mesa_4.txt", "a") as file:
                file.write("--------------------\n")
                file.write("Registros de pedidos mesa #4 "+str(datetime.now())+"\n")
                file.write("--------------------\n")
                file.write("Productos pedidos:\n")
                for item in pedido4:
                    file.write("- " + item + "\n")
                file.write("Total de compra: " + str(precio4) + "\n")
                pedido4=[]
                precio4=0
        elif accion.lower()=="a":
            while True:
                tipo=input("Qué tipo de producto es(G/B): ")
                if tipo.lower()=="g":
                    print("Granizados")
                    print("1: Pequeño")
                    print("2: Mediano")
                    print("3: Grande")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        if cantidad%2==0 and prom.lower()=="s":
                            precio4=precio4+(cantidad*7000)
                            pedido4.append(str(cantidad)+" Granizado pequeño")
                        else:
                            precio4=precio4+(((cantidad-1)*7000)+9000)
                            pedido4.append(str(cantidad)+" Granizado pequeño")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*15000)
                        pedido4.append(str(cantidad)+" Granizado mediano")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*20000)
                        pedido4.append(str(cantidad)+" Granizado grande")
                    else:
                        print("Producto inexistente en la base de datos")
                elif tipo.lower()=="b":
                    print("Bebidas")
                    print("1: Fourloko")
                    print("2: Smirnoff")
                    print("3: Coronita")
                    print("4: Budweiser")
                    print("5: Gordon´s")
                    print("6: Corona Tropical")
                    print("7: Agua")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*20000)
                        pedido4.append(str(cantidad)+" Fourloko")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*15000)
                        pedido4.append(str(cantidad)+" Smirnoff")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*6000)
                        pedido4.append(str(cantidad)+" Coronita")
                    elif producto==4:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*6000)
                        pedido4.append(str(cantidad)+" Budweiser")
                    elif producto==5:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*12000)
                        pedido4.append(str(cantidad)+" Gordon´s")
                    elif producto==6:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*6000)
                        pedido4.append(str(cantidad)+" Corona Tropical")          
                    elif producto==7:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio4=precio4+(cantidad*2000)
                        pedido4.append(str(cantidad)+" Agua")          
                    else:
                        print("Producto inexistente en la base de datos")
                    adicion=input("Desea algun shot?(S/N): ")
                    if adicion.lower()=="s":
                        can_adicion=int(input("Cuantos shots?: "))
                        if can_adicion%2==0:
                            precio4=precio4+(can_adicion*2500)
                            pedido4.append(str(cantidad)+" Shot")
                        else:
                            precio4=precio4+(((can_adicion-1)*2500)+3000)
                            pedido4.append(str(cantidad)+" Shot")
                    else:
                        pass
                else:
                    print("Tipo de producto invalido")
                continuacion = input("¿Deseas agregar otro producto? (S/N): ")
                if continuacion.lower() == "s":
                    pass
                else:
                    print("Los productos pedidos fueron:", pedido4)
                    print("El valor total de la compra es de:", precio4)
                    break
        else:
            print("Opción no valida")
    elif mesa==5:
        print("Haz elegido la mesa 5")
        accion=input("¿Que vas a hacer con esa mesa?(F/C/A): ")
        if accion.lower()=="c":
            print("La orden de la mesa es:", pedido5)
            print("El valor total de la compra es de:", precio5)
        elif accion.lower()=="f":
            with open(r"C:\Users\sebas\OneDrive\Escritorio\registro_pedidos_mesa_5.txt", "a") as file:
                file.write("--------------------\n")
                file.write("Registros de pedidos mesa #5 "+str(datetime.now())+"\n")
                file.write("--------------------\n")
                file.write("Productos pedidos:\n")
                for item in pedido5:
                    file.write("- " + item + "\n")
                file.write("Total de compra: " + str(precio5) + "\n")
                pedido5=[]
                precio5=0
        elif accion.lower()=="a":
            while True:
                tipo=input("Qué tipo de producto es(G/B): ")
                if tipo.lower()=="g":
                    print("Granizados")
                    print("1: Pequeño")
                    print("2: Mediano")
                    print("3: Grande")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        if cantidad%2==0 and prom.lower()=="s":
                            precio5=precio5+(cantidad*7000)
                            pedido5.append(str(cantidad)+" Granizado pequeño")
                        else:
                            precio5=precio5+(((cantidad-1)*7000)+9000)
                            pedido5.append(str(cantidad)+" Granizado pequeño")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*15000)
                        pedido5.append(str(cantidad)+" Granizado mediano")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*20000)
                        pedido5.append(str(cantidad)+" Granizado grande")
                    else:
                        print("Producto inexistente en la base de datos")
                elif tipo.lower()=="b":
                    print("Bebidas")
                    print("1: Fourloko")
                    print("2: Smirnoff")
                    print("3: Coronita")
                    print("4: Budweiser")
                    print("5: Gordon´s")
                    print("6: Corona Tropical")
                    print("7: Agua")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*20000)
                        pedido5.append(str(cantidad)+" Fourloko")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*15000)
                        pedido5.append(str(cantidad)+" Smirnoff")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*6000)
                        pedido5.append(str(cantidad)+" Coronita")
                    elif producto==4:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*6000)
                        pedido5.append(str(cantidad)+" Budweiser")
                    elif producto==5:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*12000)
                        pedido5.append(str(cantidad)+" Gordon´s")
                    elif producto==6:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*6000)
                        pedido5.append(str(cantidad)+" Corona Tropical")          
                    elif producto==7:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio5=precio5+(cantidad*2000)
                        pedido5.append(str(cantidad)+" Agua")          
                    else:
                        print("Producto inexistente en la base de datos")
                    adicion=input("Desea algun shot?(S/N): ")
                    if adicion.lower()=="s":
                        can_adicion=int(input("Cuantos shots?: "))
                        if can_adicion%2==0:
                            precio5=precio5+(can_adicion*2500)
                            pedido5.append(str(cantidad)+" Shot")
                        else:
                            precio5=precio5+(((can_adicion-1)*2500)+3000)
                            pedido5.append(str(cantidad)+" Shot")
                    else:
                        pass
                else:
                    print("Tipo de producto invalido")
                continuacion = input("¿Deseas agregar otro producto? (S/N): ")
                if continuacion.lower() == "s":
                    pass
                else:
                    print("Los productos pedidos fueron:", pedido5)
                    print("El valor total de la compra es de:", precio5)
                    break
        else:
            print("Opción no valida")        
    elif mesa==6:
        print("Haz elegido la mesa 6")
        accion=input("¿Que vas a hacer con esa mesa?(F/C/A): ")
        if accion.lower()=="c":
            print("La orden de la mesa es:", pedido6)
            print("El valor total de la compra es de:", precio6)
        elif accion.lower()=="f":
            with open(r"C:\Users\sebas\OneDrive\Escritorio\registro_pedidos_mesa_6.txt", "a") as file:
                file.write("--------------------\n")
                file.write("Registros de pedidos mesa #6 "+str(datetime.now())+"\n")
                file.write("--------------------\n")
                file.write("Productos pedidos:\n")
                for item in pedido6:
                    file.write("- " + item + "\n")
                file.write("Total de compra: " + str(precio6) + "\n")
                pedido6=[]
                precio6=0
        elif accion.lower()=="a":
            while True:
                tipo=input("Qué tipo de producto es(G/B): ")
                if tipo.lower()=="g":
                    print("Granizados")
                    print("1: Pequeño")
                    print("2: Mediano")
                    print("3: Grande")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        if cantidad%2==0 and prom.lower()=="s":
                            precio6=precio6+(cantidad*7000)
                            pedido6.append(str(cantidad)+" Granizado pequeño")
                        else:
                            precio6=precio6+(((cantidad-1)*7000)+9000)
                            pedido6.append(str(cantidad)+" Granizado pequeño")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*15000)
                        pedido6.append(str(cantidad)+" Granizado mediano")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*20000)
                        pedido6.append(str(cantidad)+" Granizado grande")
                    else:
                        print("Producto inexistente en la base de datos")
                elif tipo.lower()=="b":
                    print("Bebidas")
                    print("1: Fourloko")
                    print("2: Smirnoff")
                    print("3: Coronita")
                    print("4: Budweiser")
                    print("5: Gordon´s")
                    print("6: Corona Tropical")
                    print("7: Agua")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*20000)
                        pedido6.append(str(cantidad)+" Fourloko")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*15000)
                        pedido6.append(str(cantidad)+" Smirnoff")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*6000)
                        pedido6.append(str(cantidad)+" Coronita")
                    elif producto==4:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*6000)
                        pedido6.append(str(cantidad)+" Budweiser")
                    elif producto==5:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*12000)
                        pedido6.append(str(cantidad)+" Gordon´s")
                    elif producto==6:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*6000)
                        pedido6.append(str(cantidad)+" Corona Tropical")          
                    elif producto==7:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio6=precio6+(cantidad*2000)
                        pedido6.append(str(cantidad)+" Agua")          
                    else:
                        print("Producto inexistente en la base de datos")
                    adicion=input("Desea algun shot?(S/N): ")
                    if adicion.lower()=="s":
                        can_adicion=int(input("Cuantos shots?: "))
                        if can_adicion%2==0:
                            precio6=precio6+(can_adicion*2500)
                            pedido6.append(str(cantidad)+" Shot")
                        else:
                            precio6=precio6+(((can_adicion-1)*2500)+3000)
                            pedido6.append(str(cantidad)+" Shot")
                    else:
                        pass
                else:
                    print("Tipo de producto invalido")
                continuacion = input("¿Deseas agregar otro producto? (S/N): ")
                if continuacion.lower() == "s":
                    pass
                else:
                    print("Los productos pedidos fueron:", pedido6)
                    print("El valor total de la compra es de:", precio6)
                    break
        else:
            print("Opción no valida")
    elif mesa==7:
        print("Haz elegido la mesa 7")
        accion=input("¿Que vas a hacer con esa mesa?(F/C/A): ")
        if accion.lower()=="c":
            print("La orden de la mesa es:", pedido7)
            print("El valor total de la compra es de:", precio7)
        elif accion.lower()=="f":
            with open(r"C:\Users\sebas\OneDrive\Escritorio\registro_pedidos_mesa_7.txt", "a") as file:
                file.write("--------------------\n")
                file.write("Registros de pedidos mesa #7 "+str(datetime.now())+"\n")
                file.write("--------------------\n")
                file.write("Productos pedidos:\n")
                for item in pedido7:
                    file.write("- " + item + "\n")
                file.write("Total de compra: " + str(precio7) + "\n")
                pedido7=[]
                precio7=0
        elif accion.lower()=="a":
            while True:
                tipo=input("Qué tipo de producto es(G/B): ")
                if tipo.lower()=="g":
                    print("Granizados")
                    print("1: Pequeño")
                    print("2: Mediano")
                    print("3: Grande")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        if cantidad%2==0 and prom.lower()=="s":
                            precio7=precio7+(cantidad*7000)
                            pedido7.append(str(cantidad)+" Granizado pequeño")
                        else:
                            precio7=precio7+(((cantidad-1)*7000)+9000)
                            pedido7.append(str(cantidad)+" Granizado pequeño")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*15000)
                        pedido7.append(str(cantidad)+" Granizado mediano")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*20000)
                        pedido7.append(str(cantidad)+" Granizado grande")
                    else:
                        print("Producto inexistente en la base de datos")
                elif tipo.lower()=="b":
                    print("Bebidas")
                    print("1: Fourloko")
                    print("2: Smirnoff")
                    print("3: Coronita")
                    print("4: Budweiser")
                    print("5: Gordon´s")
                    print("6: Corona Tropical")
                    print("7: Agua")
                    producto=int(input("Ingrese el codigo de su producto: "))
                    if producto==1:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*20000)
                        pedido7.append(str(cantidad)+" Fourloko")
                    elif producto==2:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*15000)
                        pedido7.append(str(cantidad)+" Smirnoff")
                    elif producto==3:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*6000)
                        pedido7.append(str(cantidad)+" Coronita")
                    elif producto==4:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*6000)
                        pedido7.append(str(cantidad)+" Budweiser")
                    elif producto==5:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*12000)
                        pedido7.append(str(cantidad)+" Gordon´s")
                    elif producto==6:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*6000)
                        pedido7.append(str(cantidad)+" Corona Tropical")          
                    elif producto==7:
                        cantidad=int(input("Ingrese la cantidad: "))
                        precio7=precio7+(cantidad*2000)
                        pedido7.append(str(cantidad)+" Agua")          
                    else:
                        print("Producto inexistente en la base de datos")
                    adicion=input("Desea algun shot?(S/N): ")
                    if adicion.lower()=="s":
                        can_adicion=int(input("Cuantos shots?: "))
                        if can_adicion%2==0:
                            precio7=precio7+(can_adicion*2500)
                            pedido7.append(str(cantidad)+" Shot")
                        else:
                            precio7=precio7+(((can_adicion-1)*2500)+3000)
                            pedido7.append(str(cantidad)+" Shot")
                    else:
                        pass
                else:
                    print("Tipo de producto invalido")
                continuacion = input("¿Deseas agregar otro producto? (S/N): ")
                if continuacion.lower() == "s":
                    pass
                else:
                    print("Los productos pedidos fueron:", pedido7)
                    print("El valor total de la compra es de:", precio7)
                    break
        else:
            print("Opción no valida")
    elif mesa==0:
        print("Haz cerrado el programa")
        print("Developed by: Cevrim Studios")
        break
    else:
        print("Número de mesa invalido")