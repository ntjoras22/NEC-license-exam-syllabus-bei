## Section 8.5 — Two-Dimensional Transformation (AEiE0805)

## 📖 1. Introduction
Transformations are fundamental operations in computer graphics used to manipulate and alter the position, size, and orientation of objects. In 2D space, transformations are essential for animations, viewing pipelines, and model definitions. The NEC exam heavily focuses on mathematical formulations of these transformations using matrices.

## 💡 2. Basic Concept
Any point in 2D space is represented as a coordinate $(x, y)$. A transformation alters this point to a new location $(x', y')$. 
To combine multiple transformations easily, we use **Homogeneous Coordinates**, which represents a 2D point as a 3D vector $(x, y, 1)$.

> [!NOTE] Definition
> **Homogeneous Coordinates**: A coordinate system used in projective geometry that allows affine transformations (like translation) to be represented by matrix multiplication.

## 3. Basic 2D Transformations

### 3.1 Translation
Moves an object by adding translation distances $t_x$ and $t_y$ to the original coordinates.
$x' = x + t_x$
$y' = y + t_y$

**Matrix Representation**:
$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & t_x \\ 0 & 1 & t_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

### 3.2 Rotation
Rotates an object about the origin $(0,0)$ by an angle $\theta$. Counter-clockwise rotation is considered positive.
$x' = x \cos\theta - y \sin\theta$
$y' = x \sin\theta + y \cos\theta$

**Matrix Representation**:
$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

### 3.3 Scaling
Changes the size of an object by multiplying the coordinates by scaling factors $s_x$ and $s_y$.
$x' = x \cdot s_x$
$y' = y \cdot s_y$

**Matrix Representation**:
$$
\begin{bmatrix} x' \\ y' \\ 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ 1 \end{bmatrix}
$$

### 3.4 Reflection (Mirroring)
Produces a mirror image of the object.
- **Reflection about x-axis**: $y' = -y$
$$
  \begin{bmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$
- **Reflection about y-axis**: $x' = -x$
$$
  \begin{bmatrix} -1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$
- **Reflection about line $y = x$**: $x' = y$, $y' = x$
$$
  \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

### 3.5 Shear Transformation
Distorts the shape of an object, similar to sliding layers.
- **X-shear** (shifts x coordinates based on y): $x' = x + sh_x \cdot y$, $y' = y$
$$
  \begin{bmatrix} 1 & sh_x & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$
- **Y-shear** (shifts y coordinates based on x): $x' = x$, $y' = y + sh_y \cdot x$
$$
  \begin{bmatrix} 1 & 0 & 0 \\ sh_y & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

## 4. 2D Composite Transformation
Multiple transformations can be combined into a single composite matrix by multiplying the individual transformation matrices. 
**Note:** Matrix multiplication is not commutative. The order of transformations matters. The rightmost matrix is applied to the point first.
$P' = M_n \cdot M_{n-1} \dots M_2 \cdot M_1 \cdot P$

### Example: Rotation about an Arbitrary Point $(x_r, y_r)$
To rotate an object about a point $(x_r, y_r)$ instead of the origin:
1. Translate the object so the pivot point moves to the origin: $T(-x_r, -y_r)$.
2. Rotate the object about the origin: $R(\theta)$.
3. Translate the object back to the original position: $T(x_r, y_r)$.

Composite Matrix: $M = T(x_r, y_r) \cdot R(\theta) \cdot T(-x_r, -y_r)$

## 5. 2D Viewing Pipeline
The process of displaying a portion of a 2D scene on a device.
1. **Model Coordinate System**: Local coordinates of the object.
2. **World Coordinate System**: Global coordinates where all objects are placed.
3. **Viewing Coordinate System**: The coordinate system defined by the camera or view window.
4. **Normalized Device Coordinates (NDC)**: Resolution-independent coordinates (usually 0 to 1 or -1 to 1).
5. **Device Coordinates**: Physical screen coordinates (pixels).

## 6. Window-to-Viewport Transformation
- **Window**: A rectangular region in world coordinates that defines what is to be viewed.
- **Viewport**: A rectangular region on the display device where the window's contents are mapped.

To map a point $(x_w, y_w)$ in the window $[x_{wmin}, x_{wmax}] \times [y_{wmin}, y_{wmax}]$ to a point $(x_v, y_v)$ in the viewport $[x_{vmin}, x_{vmax}] \times [y_{vmin}, y_{vmax}]$:

$$ x_v = x_{vmin} + (x_w - x_{wmin}) \frac{x_{vmax} - x_{vmin}}{x_{wmax} - x_{wmin}} $$
$$ y_v = y_{vmin} + (y_w - y_{wmin}) \frac{y_{vmax} - y_{vmin}}{y_{wmax} - y_{wmin}} $$

## 7. Clipping
Clipping determines which parts of lines, polygons, or text are within the view window and discards the rest.

### 7.1 Cohen-Sutherland Line Clipping
Uses a 4-bit region code for each endpoint of the line to quickly identify whether the line is completely inside, completely outside, or intersecting the window.
- Bit 1: Top ($y > y_{max}$)
- Bit 2: Bottom ($y < y_{min}$)
- Bit 3: Right ($x > x_{max}$)
- Bit 4: Left ($x < x_{min}$)

**Algorithm**:
1. Assign region codes to endpoints $P_1$ and $P_2$.
2. **Trivial Accept**: Both codes are 0000 (bitwise OR is 0). Line is completely inside.
3. **Trivial Reject**: Bitwise AND of codes $\neq 0$. Line is completely outside.
4. **Calculate Intersection**: If neither, the line intersects the boundary. Calculate the intersection point and replace the outside point with the intersection point. Repeat until accepted or rejected.

### 7.2 Liang-Barsky Line Clipping
Based on the parametric equation of a line:
$x = x_1 + t \cdot \Delta x$
$y = y_1 + t \cdot \Delta y$
where $0 \le t \le 1$.
It reformulates the clipping inequalities as $p_k \cdot t \le q_k$ for the 4 boundaries (left, right, bottom, top). It calculates the intersection parameter $t$ for all edges and updates the valid range $[t_{min}, t_{max}]$. If $t_{min} > t_{max}$, the line is completely outside.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Remember that matrix multiplication is performed right-to-left. A transformation $T$ followed by $R$ is written as $R \cdot T \cdot P$.

> [!TIP]
> In Cohen-Sutherland, remember the bit order is typically Top, Bottom, Right, Left (TBRL).

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> **Homogeneous Matrices**: Always $3 \times 3$ for 2D transformations.
> Translation modifies the rightmost column.
> Rotation involves sine and cosine terms in the upper left $2 \times 2$ block.
> Scaling modifies the diagonal elements.

## ✏️ Practice Problems

1. **Find the transformation matrix that reflects an object about the line $y = x$.**
   *Answer Sketch:* $x' = y$, $y' = x$. Matrix is $\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$.

2. **Given a window from $(0,0)$ to $(100,100)$ and a viewport from $(50,50)$ to $(250,250)$, map a point $(20,40)$ from the window to the viewport.**
   *Answer Sketch:* Scaling factors $S_x = (250-50)/(100-0) = 2$, $S_y = 2$. $x_v = 50 + (20-0)*2 = 90$. $y_v = 50 + (40-0)*2 = 130$. Point is $(90, 130)$.

3. **In Cohen-Sutherland, what does a region code of 1001 represent?**
   *Answer Sketch:* Top and Left bits are set. The point is above and to the left of the clipping window.
</Section 8.5: Two-Dimensional Transformation (AEiE0805)>
