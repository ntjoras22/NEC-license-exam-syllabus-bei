## Section 8.6 — Three-Dimensional Transformation (AEiE0806)

## 📖 1. Introduction
Three-dimensional graphics adds depth to objects, requiring the addition of a z-axis. Similar to 2D transformations, 3D transformations manipulate points in 3D space. This section covers 3D geometric transformations and how 3D scenes are projected onto a 2D display surface.

## 💡 2. Basic Concept
A point in 3D space is represented as $(x, y, z)$. Using homogeneous coordinates, a 3D point is represented as a 4D vector $(x, y, z, 1)$. All transformation matrices become $4 \times 4$ matrices.

> [!NOTE] Definition
> **3D Coordinate System**: Typically, computer graphics uses a right-handed coordinate system where the positive x-axis points right, the positive y-axis points up, and the positive z-axis points towards the viewer (out of the screen).

## 3. Basic 3D Transformations

### 3.1 Translation
Moves an object by translation distances $t_x$, $t_y$, and $t_z$.

**Matrix Representation**:
$$
\begin{bmatrix} x' \\ y' \\ z' \\ 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & t_x \\ 0 & 1 & 0 & t_y \\ 0 & 0 & 1 & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
$$

### 3.2 Scaling
Scales an object along the x, y, and z axes.

**Matrix Representation**:
$$
\begin{bmatrix} x' \\ y' \\ z' \\ 1 \end{bmatrix} = \begin{bmatrix} s_x & 0 & 0 & 0 \\ 0 & s_y & 0 & 0 \\ 0 & 0 & s_z & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
$$

### 3.3 Rotation
In 3D, an object can be rotated about any of the three coordinate axes.

- **Rotation about the Z-axis** (similar to 2D rotation):

$$ R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 & 0 \\ \sin\theta & \cos\theta & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

- **Rotation about the X-axis**:

$$ R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta & 0 \\ 0 & \sin\theta & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

- **Rotation about the Y-axis**:

$$ R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta & 0 \\ 0 & 1 & 0 & 0 \\ -\sin\theta & 0 & \cos\theta & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} $$

### 3.4 Reflection
Reflection can occur across the primary planes (xy-plane, yz-plane, xz-plane).
- **Reflection across the xy-plane** ($z' = -z$):
$$
  \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

### 3.5 Shear Transformation
Shearing in 3D shifts two coordinates based on the third coordinate.
- **Z-shear** (x and y are shifted based on z):
$$
  \begin{bmatrix} 1 & 0 & sh_x & 0 \\ 0 & 1 & sh_y & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

## 4. 3D Composite Transformation
Similar to 2D, complex 3D transformations are achieved by multiplying a sequence of basic transformation matrices.

### Example: Rotation about an arbitrary axis
To rotate about an arbitrary line in 3D space:
1. Translate the object so the axis passes through the origin.
2. Rotate the object around the x and/or y-axis so the arbitrary axis aligns with the z-axis.
3. Perform the desired rotation about the z-axis.
4. Apply the inverse rotations from step 2.
5. Apply the inverse translation from step 1.

## 5. 3D Viewing Pipeline
The process of capturing a 3D scene and converting it into a 2D image.
1. **Modeling Coordinates**: Local space of the object.
2. **World Coordinates**: The global scene.
3. **Viewing (Camera) Coordinates**: Defined by the View Reference Point (VRP), View Plane Normal (VPN), and View Up Vector (VUV).
4. **Projection Coordinates**: Projecting 3D points onto a 2D view plane.
5. **Normalized Device Coordinates (NDC)**.
6. **Device (Screen) Coordinates**.

## 6. Projection Concepts
Projection maps 3D points to a 2D plane (the view plane or projection plane).

### 6.1 Parallel Projection
Projectors (lines of projection) are parallel to each other. It preserves relative proportions and is widely used in engineering and architectural drawings. It does not look realistic because objects do not appear smaller as they move further away.
- **Orthographic Projection**: The projectors are perpendicular to the projection plane. (e.g., top, front, side views).
- **Oblique Projection**: The projectors are not perpendicular to the projection plane. (e.g., Cavalier, Cabinet projections).

### 6.2 Perspective Projection
Projectors converge at a single point called the **Center of Projection (COP)** or vanishing point. This mimics human vision, where distant objects appear smaller.
- **One-point perspective**: One principal axis intersects the projection plane. (One vanishing point).
- **Two-point perspective**: Two principal axes intersect the projection plane.
- **Three-point perspective**: All three principal axes intersect the projection plane.

**Perspective Projection Matrix** (Assuming COP is at origin and projection plane is at $z = d$):
From similar triangles, $x_p = \frac{x \cdot d}{z}$ and $y_p = \frac{y \cdot d}{z}$.
Using homogeneous coordinates, this is achieved by modifying the fourth coordinate (w).
$$
\begin{bmatrix} x_h \\ y_h \\ z_h \\ w_h \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 1/d & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix} = \begin{bmatrix} x \\ y \\ z \\ z/d \end{bmatrix}
$$
Converting back to 3D by dividing by $w_h$: $x' = x / (z/d) = x \cdot d / z$.

### Comparison: Parallel vs. Perspective Projection

| Feature | Parallel Projection | Perspective Projection |
| :--- | :--- | :--- |
| **Projectors** | Parallel | Converge at a single point (COP) |
| **Distance Effect** | Distance does not affect size | Distant objects appear smaller |
| **Realism** | Less realistic | More realistic |
| **Application** | Exact measurements (CAD) | Realism (Games, Animations) |
| **Parallel Lines** | Remain parallel | May converge at a vanishing point |

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Pay attention to the negative signs in 3D rotation matrices. For rotation about the Y-axis, the negative sine term is at the bottom left ($-\sin\theta$), which is opposite to X and Z axis rotations due to the right-handed coordinate system rule.

> [!TIP]
> In perspective projection, remember that division by the z-coordinate occurs during the conversion from homogeneous to Cartesian coordinates.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> - 3D matrices are $4 \times 4$.
> - **Orthographic Projection**: Preserves true lengths and parallel lines.
> - **Perspective Projection**: Uses a Center of Projection (COP) and incorporates foreshortening.

## ✏️ Practice Problems

1. **Write the $4 \times 4$ transformation matrix for a uniform scaling by a factor of 3.**
   *Answer Sketch:* A diagonal matrix with elements $(3, 3, 3, 1)$.

2. **Differentiate between one-point and two-point perspective projection.**
   *Answer Sketch:* One-point perspective has one vanishing point because the projection plane is parallel to two principal axes. Two-point has two vanishing points because the plane is parallel to only one principal axis.

3. **Calculate the projected point on the plane $z = d$ for a point $P(2, 4, 10)$ under perspective projection with the COP at the origin, if $d = 5$.**
   *Answer Sketch:* $x_p = (x \cdot d)/z = (2 \cdot 5)/10 = 1$. $y_p = (y \cdot d)/z = (4 \cdot 5)/10 = 2$. Projected point is $(1, 2)$.
</Section 8.6: Three-Dimensional Transformation (AEiE0806)>
