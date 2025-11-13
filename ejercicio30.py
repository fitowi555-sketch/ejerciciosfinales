
#Pide el ingreso anual y calcula el impuesto basado en tramos de ingresos.

UVT_2024 = 47065

ingreso_anual = float(input("digite el ingreso anual (COP):"))

ingreso_uvt = ingreso_anual / UVT_2024

if ingreso_uvt <= 1090:
    inpuesto = 0

elif ingreso_uvt <= 1700:
    impuesto = (ingreso_uvt - 1090) * 0.19 * UVT_2024

elif ingreso_uvt <= 4100:
    impuesto = ((610) * 0.19 + (ingreso_uvt - 1700) * 0.28) * UVT_2024 

elif ingreso_uvt <= 8670:
    impuesto = ((610) * 0.19 + (2400) * 0.28 +  (ingreso_uvt - 4100) * 0.33) * UVT_2024

elif ingreso_uvt <= 18970:
    impuesto = ((610) * 0.19 + (2400) * 0.28 + (4570) * 0.33 (ingreso_uvt - 8670) * 0.35) * UVT_2024

elif ingreso_uvt <= 31000:
    impuesto = ((610) * 0.19 + (2400) * 0.28 + (4570) * 0.33 + (10300) * 0.35 + (ingreso_uvt - 18970) * 0.37) * UVT_2024

else:
    impuesto = ((610) * 0.19 + (2400) * 0.28 + (4570) * 0.33 + (10300) * 0.35 + (12030) * 0.37 + (ingreso_uvt - 31000) * 0.39) * UVT_2024

print(f"\ningreso anual en UVT: {ingreso_uvt:.2f} UVT")
print(f"impuesto total a pagar (DIAN 2024): ${impuesto:,.0f} COP")    