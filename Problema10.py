def obtenerNumeroMes(mes):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    return meses.index(mes) + 1

def formatearFecha(fecha):
    partes = fecha.split()
    
    if '/' in fecha:
        mes, dia, anio = map(int, fecha.split('/'))
    else:
        mes = obtenerNumeroMes(partes[0])
        dia = int(partes[1].strip(','))
        anio = int(partes[2])

    return f"{anio:04d}-{mes:02d}-{dia:02d}"

cadenaFecha = input("Ingrese una fecha (mes-día-año o mes día, año): ")

fechaFormateada = formatearFecha(cadenaFecha)
print("La fecha formateada es:", fechaFormateada)
