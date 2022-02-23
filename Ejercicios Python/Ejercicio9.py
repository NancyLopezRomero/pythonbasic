#ENTRADAS
Dias = float (input("Escribe los días trabajados: "))
Pagoxdia = float (input("Escribe el pago por día: "))

#PROCESOS
PagoBruto = Dias * Pagoxdia
print(f"Pago bruto = {PagoBruto}")
IVATrasl = PagoBruto * 0.16
print(f"IVA Trasladado = {IVATrasl}")
Subtotal = PagoBruto + IVATrasl
print(f"SubTotal = {Subtotal}")
IVARet = 2/3 * IVATrasl
print(f"IVA Retenido = {IVARet}")
ISRRet = PagoBruto * 0.1
print (f"ISR Retenido = {ISRRet}")
PagoNeto = (Subtotal - IVARet - ISRRet)
print (f"Pago Neto = {PagoNeto}")
