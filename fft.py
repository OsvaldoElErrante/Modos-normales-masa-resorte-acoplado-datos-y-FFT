import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

df = pd.read_excel("datos.xlsm", sheet_name= "Hoja2", header=1)

print("Elija que oscilacion quiere analizar:")
print()
print("1) Misma Dirección")
print("2) Direcciones Opuestas")
print("3) Un solo carro")
print("4) Amortiguamiento Oscilacion simple")
print("5) Amortiguamiento Misma Direccion")
print("6) Amortiguamiento Direcciones Opuestas")
print("7) Amortiguamiento Un solo carro")
      
eleccion = int(input("Elija numero: "))

if eleccion == 1:
      
    f = df["f / Hz 1"]
    amp_m1 = df["A_1 / % 1"]
    amp_m2 = df["A_2 / % 1"]

    plt.figure()

    plt.plot(f, amp_m1, label="Masa 1")
    plt.plot(f, amp_m2, label="Masa 2")

    plt.xlabel("Frecuencia")
    plt.ylabel("Amplitud")
    plt.title("FFT del sistema acoplado")
    plt.xlim(0, 2)

    plt.legend()
    plt.grid()

    indice_max = np.argmax(amp_m1)
    print("Frecuencia principal:", f.iloc[indice_max])

    plt.show()

    print(df.columns)

elif eleccion == 2:

    f = df["f / Hz 2"]
    amp_m1 = df["A_1 / % 2"]
    amp_m2 = df["A_2 / % 2"]

    plt.figure()

    plt.plot(f, amp_m1, label="Masa 1")
    plt.plot(f, amp_m2, label="Masa 2")

    plt.xlabel("Frecuencia")
    plt.ylabel("Amplitud")
    plt.title("FFT del sistema acoplado")
    plt.xlim(0, 2)

    plt.legend()
    plt.grid()

    indice_max = np.argmax(amp_m1)
    print("Frecuencia principal:", f.iloc[indice_max])

    plt.show()

    print(df.columns)


elif eleccion == 3:

    f = df["f / Hz 3"]
    amp_m1 = df["A_1 / % 3"]
    amp_m2 = df["A_2 / % 3"]

    mask = ~np.isnan(f) & ~np.isnan(amp_m1) & ~np.isnan(amp_m2)
    f = f[mask]
    amp_m1 = amp_m1[mask]
    amp_m2 = amp_m2[mask]

    plt.figure()

    plt.plot(f, amp_m1, label="Masa 1")
    plt.plot(f, amp_m2, label="Masa 2")

    plt.xlabel("Frecuencia")
    plt.ylabel("Amplitud")
    plt.title("FFT del sistema acoplado")
    plt.xlim(0, 2)

    plt.legend()
    plt.grid()

    indice_max = np.argmax(amp_m1)
    print("Frecuencia principal:", f.iloc[indice_max])

    plt.show()

    print(df.columns)
    print(f.min(), f.max())

elif eleccion == 4:

    t = df["t / s 1"]
    x = df["s_1 1"]

    # eliminar filas con NaN
    mask = ~np.isnan(t) & ~np.isnan(x)

    t = t[mask]
    x = x[mask]

    def sinusoide_amort(t,A,gamma,omega,phi, D):
        return A * np.exp(-gamma*t) * np.cos(omega*t + phi) + D

    p0 = [max(abs(x)), 0.05, 2*np.pi, 0, 0]  # [A, gamma, omega, phi]

    params, _ = curve_fit(sinusoide_amort, t, x, p0)
    A, gamma, omega, phi, D = params

    t_fit = np.linspace(min(t), max(t), 1000)
    x_fit = sinusoide_amort(t_fit, *params)

    ecuacion = (
        rf"$x(t) = {A:.2f} e^{{-{gamma:.4f}t}} \cos({omega:.2f}t + {phi:.2f}) + {D:.3f}$"
    )

    plt.scatter(t,x, label = "Medicion 1")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Posición Horizontal [m]")
    plt.plot(t_fit, x_fit, label = "Ajuste", color = "red")
    plt.text(0.05, 1.1, ecuacion, transform=plt.gca().transAxes, fontsize=11, verticalalignment='top')
    plt.legend()
    plt.xlim(0, 40)
    plt.show()

elif eleccion == 5:

    masa = input("Elige masa: ")

    t = df["t / s 2"]
    x = df[f"s_{masa} 2"]

    # eliminar filas con NaN
    mask = ~np.isnan(t) & ~np.isnan(x)

    t = t[mask]
    x = x[mask]

    def sinusoide_amort(t,A,gamma,omega,phi, D):
        return A * np.exp(-gamma*t) * np.cos(omega*t + phi) + D

    p0 = [max(abs(x)), 0.05, 2*np.pi, 0, 0]  # [A, gamma, omega, phi]

    params, _ = curve_fit(sinusoide_amort, t, x, p0)
    A, gamma, omega, phi, D = params

    t_fit = np.linspace(min(t), max(t), 1000)
    x_fit = sinusoide_amort(t_fit, *params)

    ecuacion = (
        rf"$x(t) = {A:.2f} e^{{-{gamma:.2f}t}} \cos({omega:.2f}t + {phi:.2f}) + {D:.3f}$"
    )

    plt.scatter(t,x, label = "Medicion 1")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Posición Horizontal [m]")
    plt.plot(t_fit, x_fit, label = "Ajuste", color = "red")
    plt.text(0.05, 1.1, ecuacion, transform=plt.gca().transAxes, fontsize=11, verticalalignment='top')
    plt.legend()
    plt.xlim(0, 40)
    plt.show()

elif eleccion == 6:

    masa = input("Elige masa: ")

    t = df["t / s 3"]
    x = df[f"s_{masa} 3"]

    # eliminar filas con NaN
    mask = ~np.isnan(t) & ~np.isnan(x)

    t = t[mask]
    x = x[mask]

    def sinusoide_amort(t,A,gamma,omega,phi, D):
        return A * np.exp(-gamma*t) * np.cos(omega*t + phi) + D

    p0 = [max(abs(x)), 0.05, 2*np.pi, 0, 0]  # [A, gamma, omega, phi]

    params, _ = curve_fit(sinusoide_amort, t, x, p0)
    A, gamma, omega, phi, D = params

    t_fit = np.linspace(min(t), max(t), 1000)
    x_fit = sinusoide_amort(t_fit, *params)

    ecuacion = (
        rf"$x(t) = {A:.2f} e^{{-{gamma:.2f}t}} \cos({omega:.2f}t + {phi:.2f}) + {D:.3f}$"
    )

    plt.scatter(t,x, label = "Medicion 1")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Posición Horizontal [m]")
    plt.plot(t_fit, x_fit, label = "Ajuste", color = "red")
    plt.text(0.05, 1.1, ecuacion, transform=plt.gca().transAxes, fontsize=11, verticalalignment='top')
    plt.legend()
    plt.xlim(0, 40)
    plt.show()

elif eleccion == 7:

    masa = input("Elige masa: ")

    t = df["t / s 4"]
    x = df[f"s_{masa} 4"]

    # eliminar filas con NaN
    mask = ~np.isnan(t) & ~np.isnan(x)

    t = t[mask]
    x = x[mask]

    def sinusoide_amort(t,A,gamma,omega,phi, D):
        return A * np.exp(-gamma*t) * np.cos(omega*t + phi) + D

    p0 = [max(abs(x)), 0.05, 2*np.pi, 0, 0]  # [A, gamma, omega, phi]

    params, _ = curve_fit(sinusoide_amort, t, x, p0)
    A, gamma, omega, phi, D = params

    t_fit = np.linspace(min(t), max(t), 1000)
    x_fit = sinusoide_amort(t_fit, *params)

    ecuacion = (
        rf"$x(t) = {A:.2f} e^{{-{gamma:.2f}t}} \cos({omega:.2f}t + {phi:.2f}) + {D:.3f}$"
    )

    plt.scatter(t,x, label = "Medicion 1")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Posición Horizontal [m]")
    plt.plot(t_fit, x_fit, label = "Ajuste", color = "red")
    plt.text(0.05, 1.1, ecuacion, transform=plt.gca().transAxes, fontsize=11, verticalalignment='top')
    plt.legend()
    plt.xlim(0, 40)
    plt.show()

else:
    print("El pepe")
