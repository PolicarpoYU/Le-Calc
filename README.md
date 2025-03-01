# **Le-Calc: Analytical and Numerical Calculation of Ellipse Perimeters**

## **Overview**
**Le-Calc** is a Python program developed to explore a novel approach for calculating the perimeter of an ellipse using the **Ulianov Elliptic Trigonometry** model. The program aims to bridge the gap between traditional numerical integration techniques and analytical solutions, leveraging newly defined **elliptic trigonometric functions**. It also investigates the theoretical relationship between the mean orbital velocity and the perimeter of an ellipse.

This program introduces:
- A numerical method for computing the **exact perimeter** of an ellipse via integration.
- The **Ramanujan approximation** for the perimeter and its associated error.
- The application of **Ulianov Elliptical Functions** to estimate the perimeter based on **orbital velocity**.
- A **bisection search method** to determine the key angular relationships involved in elliptical motion.

## **Key Features**
- **Numerical and Analytical Ellipse Perimeter Calculation**  
  - Implements **Ramanujan's empirical formula** for estimating the perimeter.
  - Computes the **exact perimeter** via numerical integration.
  - Compares both methods, displaying the **percentage error**.

- **Orbital Mechanics Integration**  
  - Defines an **orbital period equation** in terms of ellipse parameters.
  - Derives the **mean velocity of a body in an elliptical orbit**.
  - Uses an iterative method to find the **corresponding angle** where velocity matches the mean velocity.

- **Ulianov Elliptic Trigonometry Model**  
  - Introduces **elliptic sine and cosine functions** for more precise calculations.
  - Defines **Beta(Ue)**, a crucial angle in the perimeter calculation.
  - Compares **theoretical vs. numerically computed Beta values**, refining the model.

## **Core Functions**
- **`perimeter_integral_ellipse(a, b)`**:  
  Computes the perimeter using numerical integration.

- **`Ramanujan_perimeter_ellipse(a, b)`**:  
  Approximates the perimeter using Ramanujan’s formula.

- **`Beta_FX(a, b)`**:  
  Computes a **theoretical** and an **empirical** estimate for the Beta angle.

- **`find_Alpha(a, b)`**:  
  Uses a **bisection search method** to determine the angle **α** where **V(α) = V_M**.

- **`calculate_Le(a, b, Alpha)`**:  
  Uses the orbital mechanics approach to estimate **L_e**.

- **Plotting Functions**:  
  - Generates **error plots** comparing Ramanujan’s formula to numerical integration.
  - Plots the **theoretical vs. calculated Beta angle**.
  - Displays the relationship between **Ue and Beta**.

## **Results and Observations**
- The program demonstrates that **Ramanujan's formula** remains highly accurate (error **< 0.005%**), but it fails for highly eccentric ellipses.
- Using **Ulianov's trigonometric approach**, the estimated perimeter converges towards an analytical solution.
- The **Beta(Ue) function** is critical to obtaining an exact analytical formula for the ellipse perimeter.
- The discrepancy between theoretical and calculated Beta values is **< 3%**, suggesting strong validity of the approach.

## **Installation and Usage**
### **Requirements**
Ensure you have the following Python libraries installed:
```bash
pip install numpy matplotlib mpmath
```

### **Running the Program**
Execute the script using:
```bash
python Le-Calc.py
```

### **Expected Outputs**
- **Graphs comparing the numerical and theoretical models**.
- **Error plots showing the precision of different methods**.
- **Tables of calculated values**.

## **Future Work**
- Refining the **Beta(Ue)** equation to reach an **exact analytical formula**.
- Extending the method to **other conic sections**.
- Improving computational efficiency for higher precision calculations.

## **References**
- **S. Ramanujan**, "Modular Equations and Approximations to π," *Quarterly Journal of Mathematics*, 1914.
- **Ulianov Elliptical Trigonometry**, research in progress.
- [GitHub Repository](https://github.com/your-repo-link-here)

