import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import csv

# Set precision to 25 decimal places
mp.dps = 25

def cosUell(Alpha, Ue):
    return 1 / (2 - Ue) * (np.cos(Alpha) - 1) + 1

def sinUell(Alpha, Ue):
    return 1 / np.sqrt(2 / Ue - 1) * np.sin(Alpha)

def Ramanujan_ellipse_perimeter(a, b):
    """Calculates the ellipse perimeter using Ramanujan's empirical formula."""
    h = (a - b)**2 / (a + b)**2
    Le = 2 * np.pi * (a + b) * (1 + (3 * h / (10 + np.sqrt(4 - 3 * h)))) / 2
    return Le

def ellipse_perimeter_integral(a, b):
    """Calculates the ellipse perimeter using numerical integration."""
    def integrand(alpha):
        dx_dalpha = -a * mp.sin(alpha)
        dy_dalpha = b * mp.cos(alpha)
        return mp.sqrt(dx_dalpha**2 + dy_dalpha**2)
    
    # Integrate from 0 to π/2 and multiply by 4 to get the full ellipse perimeter
    Le = 4 * mp.quad(integrand, [0, mp.pi/2])
    return float(Le)

def orbital_period(a, b):
    """Computes the orbital period based on semi-major and semi-minor axes."""
    return 2 * np.pi * b / np.sqrt(2 * (1 - np.sqrt(1 - b**2 / a**2)) - b**2 / a**2)

def velocity(Alpha, a, b):
    """Calculates the velocity of an orbiting body at a given angle Alpha."""
    Ue = b**2 / (a**2 - np.sqrt(a**4 - a**2 * b**2))
    Re = np.sqrt(cosUell(Alpha, Ue)**2 + sinUell(Alpha, Ue)**2)
    return np.sqrt(1 + 2 / Ue * (1 / Re - 1))

def Beta_FX(a, b):
    """Computes the theoretical and corrected Beta values."""
    Beta_calc = np.pi - np.arcsin(b / a)
    x2 = np.cos(Beta_calc)
    y2 = (b / a) * np.sin(Beta_calc)
    Beta_calc1 = np.arctan2(y2, x2)
    return Beta_calc, Beta_calc1

def calc_le(a, b, Alpha):
    """Calculates the ellipse perimeter using velocity and orbital period."""
    Torb = orbital_period(a, b)
    VM = velocity(Alpha, a, b)
    Le = VM * Torb  # Mean velocity times orbital period
    return Le

def find_Alpha(a, b):
    """Finds the value of Alpha that satisfies V(Alpha) = V_mean = Le/Torb."""
    Le = ellipse_perimeter_integral(a, b)
    Torb = orbital_period(a, b)
    VM = Le / Torb  # Mean velocity
    Ue = b**2 / (a**2 - np.sqrt(a**4 - a**2 * b**2))
    
    Alpha_min = np.radians(90)
    Alpha_max = np.radians(120)
    tol = 1e-12  # Convergence tolerance
    max_iter = 500
    iter_count = 0
    Beta = 0
    
    while iter_count < max_iter:
        V_Alpha_max = velocity(Alpha_max, a, b)
        V_Alpha_min = velocity(Alpha_min, a, b)
        dif = V_Alpha_max - V_Alpha_min
        
        if abs(V_Alpha_max - VM) < tol or abs(V_Alpha_min - VM) < tol:
            break
        
        Alpha = Alpha_min + (VM - V_Alpha_min) * (Alpha_max - Alpha_min) / dif  # Linear interpolation
        Beta = np.arctan2(sinUell(Alpha, Ue), cosUell(Alpha, Ue))
        V_Alpha = velocity(Alpha, a, b)
        
        if abs(V_Alpha - VM) < tol:
            return Alpha, Beta
        
        if V_Alpha > VM:
            Alpha_max = Alpha
        else:
            Alpha_min = Alpha
        
        iter_count += 1
    
    return 0, 0  # Return zero if no solution found

def compute_Alpha(a, b):
    """Computes the theoretical Alpha value."""
    return np.pi - np.arcsin(b / a)

def save_Ue_Alpha_csv(Ue_values, Alpha_values, file_path):
    """Saves computed Ue and Alpha values to a CSV file."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Ue_values", "Alpha_values"])
        for Ue, Alpha in zip(Ue_values, Alpha_values):
            writer.writerow([Ue, Alpha])

r0 = 1
Ue_values, Alpha_values, Beta_values = [], [], []
Beta_calc_values, Beta_calc1_values, real_ab = [], [], []
Error1, Error2, Error3 = [], [], []

a_values = np.arange(1, 20, 0.1)

# Compute error of Ramanujan's formula
for a in a_values:
    b = 1
    Le_ramanujan = Ramanujan_ellipse_perimeter(a, b)
    Le_integral = ellipse_perimeter_integral(a, b)
    er1 = ((Le_integral - Le_ramanujan) / Le_integral) * 100
    Error1.append(er1)
    real_ab.append(a / b)

# Plot error of Ramanujan's formula
plt.figure(figsize=(8, 6))
plt.plot(real_ab, Error1, label="Error % = |$Le_{Numerical}$ - $Le_{Ramanujan}$| / $Le_{Numerical}$*100")
plt.xlabel("Relation a/b")
plt.ylabel("% Error ")
plt.title("Error between Ramanujan's empirical formula and numerical calculation of ellipse perimeters")
plt.legend()
plt.grid(True)
plt.show()

# Compute Alpha and Beta for varying Ue values
Ue_range = np.arange(1.01, 1.99, 0.01)
for Ue in Ue_range:
    a = r0 / (2 - Ue)
    b = r0 / np.sqrt(2 / Ue - 1)
    Alpha, Beta = find_Alpha(a, b)
    Beta_calc, Beta_calc1 = Beta_FX(a, b)
    real_ab.append(a / b)
    Ue_values.append(Ue)
    Alpha_values.append(Alpha)
    Beta_values.append(Beta)
    Beta_calc_values.append(Beta_calc)
    Beta_calc1_values.append(Beta_calc1)
    er2 = Beta - Beta_calc1
    Error2.append(er2)

# Plot theoretical vs. calculated Beta
plt.figure(figsize=(8, 6))
plt.plot(Ue_values, Beta_values, label='Beta Theoretical', color='red')
plt.plot(Ue_values, Beta_calc_values, label='Beta Calculated', color='blue')
plt.xlabel('Ue')
plt.ylabel('Beta (radians)')
plt.title('Comparison between Theoretical and Calculated Beta')
plt.legend()
plt.grid()
plt.show()

# Plot theoretical vs. calculated Beta
plt.figure(figsize=(8, 6))
plt.plot(Ue_values, Beta_values, label='Beta Theoretical', color='red')
plt.plot(Ue_values, Beta_calc1_values, label='Beta Calculated', color='blue')
plt.xlabel('Ue')
plt.ylabel('Beta1 (radians)')
plt.title('Comparison between Theoretical and Calculated Beta 1')
plt.legend()
plt.grid()
plt.show()
