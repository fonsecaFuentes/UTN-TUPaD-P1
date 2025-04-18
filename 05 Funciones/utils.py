def validar_num(mensaje, min=float("-inf"), max=(float("inf"))):
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n