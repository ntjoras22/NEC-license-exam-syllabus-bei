## Section 8.4 — Computer Graphics (AEiE0804)

## 📖 1. Introduction
Computer graphics deals with the creation, manipulation, and storage of different types of images and objects using computers. In the context of the NEC license exam, this section covers the fundamental concepts of computer graphics, including both hardware components and software standards used to produce graphical output.

## 💡 2. Basic Concept
Computer graphics systems comprise hardware devices to generate, store, and display images, and software to provide the necessary commands and algorithms.

> [!NOTE] Definition
> **Computer Graphics**: The art and science of communicating information using images that are generated and presented through computation.

### Applications of Computer Graphics
- **Computer-Aided Design (CAD)**: Used in engineering and architectural design.
- **Presentation Graphics**: Charts and graphs for summarizing data.
- **Computer Art**: Creating digital artwork.
- **Entertainment**: Movies, games, and animations.
- **Education and Training**: Flight simulators, educational software.
- **Visualization**: Scientific and data visualization.

## 3. Graphics Hardware

### 3.1 Display Technologies
The display device is the primary output mechanism for a graphics system.

#### Cathode Ray Tube (CRT)
The traditional display technology. An electron gun emits a beam of electrons that passes through focusing and deflection systems, striking a phosphor-coated screen to emit light.
- **Phosphor Persistence**: The time it takes for the emitted light from the phosphor to decay to one-tenth of its original intensity.

#### Liquid Crystal Display (LCD)
Uses the light-modulating properties of liquid crystals. It consists of a layer of liquid crystal molecules placed between two polarizing filters and two glass panels.

#### Light Emitting Diode (LED)
Similar to LCDs but uses LEDs for backlighting instead of cold cathode fluorescent lamps (CCFLs).

#### Plasma Panels
Uses small cells containing electrically charged ionized gases (plasmas) to generate light.

### 3.2 Architecture of Raster-Scan Displays
In a raster-scan system, the electron beam is swept across the screen one row at a time from top to bottom.
- **Frame Buffer**: A memory area that holds the set of intensity values for all the screen points (pixels).
- **Refresh Rate**: The number of times per second the image is redrawn. Typically 60-120 frames per second to avoid flickering.

> [!NOTE] Definition
> **Pixel (Picture Element)**: The smallest addressable screen element in a raster display.

**Raster-Scan System Architecture**:
1. CPU executes application program.
2. Graphics commands are sent to the Display Processor.
3. Display Processor rasterizes the commands and writes pixel values into the Frame Buffer.
4. Video Controller reads the Frame Buffer and generates analog signals for the monitor.

### 3.3 Vector Displays (Random-Scan Displays)
Instead of scanning the whole screen, the electron beam is directed only to the parts of the screen where a picture is to be drawn.
- Also known as stroke-writing or calligraphic displays.
- Draws pictures as a set of continuous lines.
- Does not use a frame buffer; instead, uses a **Display List** (or refresh display file) which stores the sequence of drawing commands.

### Comparison: Raster-Scan vs. Random-Scan

| Feature | Raster-Scan | Random-Scan (Vector) |
| :--- | :--- | :--- |
| **Drawing Method** | Sweeps entire screen row by row | Draws only the lines of the object |
| **Memory** | Frame buffer (stores pixels) | Display list (stores line commands) |
| **Image Type** | Suitable for realistic images | Suitable for line-drawing applications |
| **Resolution** | Limited by pixel size | Infinite resolution (smooth lines) |
| **Aliasing (Jagged lines)** | Present | Absent |
| **Cost** | Less expensive | More expensive |

### 3.4 Display Processors
A specialized processor used to free the main CPU from the graphics chores.
- Performs operations like line drawing, polygon filling, character generation, and coordinate transformations.
- In modern systems, this is known as a Graphics Processing Unit (GPU).

### 3.5 Input and Output Devices

#### Input Devices
- **Keyboards, Mouse, Trackball, Joystick**: Standard positioning and input devices.
- **Digitizers / Graphics Tablets**: Used for accurate drawing and tracing.
- **Light Pens**: A light-sensitive stylus used to directly interact with the CRT screen.
- **Touch Panels**: Allows touch interaction on the screen surface.
- **Scanners**: Converts physical images into digital formats.

#### Output Devices
- **Monitors (CRT, LCD, LED)**: Primary display devices.
- **Printers (Impact, Inkjet, Laser)**: Produces hardcopy output.
- **Plotters (Pen, Electrostatic)**: High-quality line drawings, especially used in CAD.

## 4. Graphics Software and Standards

### 4.1 Graphics Software
Graphics software provides the necessary tools and functions to create, modify, and display images.
- **General Programming Packages**: Provide an extensive set of graphics functions (e.g., OpenGL, Direct3D).
- **Special-Purpose Application Packages**: Designed for non-programmers for specific tasks (e.g., AutoCAD, Adobe Photoshop).

### 4.2 Graphics Software Standards
To ensure portability of graphics programs across different hardware platforms, various standards have been developed.

#### GKS (Graphical Kernel System)
The first recognized standard for computer graphics (ISO standard). It is a 2D standard that provides a set of basic functions for drawing and input.

#### PHIGS (Programmer's Hierarchical Interactive Graphics System)
An extension to GKS that supports 3D graphics, hierarchical object modeling, and advanced viewing operations.

#### OpenGL (Open Graphics Library)
A cross-language, cross-platform API for rendering 2D and 3D vector graphics. It is widely used in CAD, virtual reality, scientific visualization, and video games.

#### Direct3D
Part of Microsoft's DirectX API. It is heavily used in Windows-based applications and Xbox games.

## 💡 Common Mistakes / Exam Tips

> [!WARNING]
> Confusing Raster-Scan and Random-Scan displays. Remember that Raster-Scan uses a frame buffer and draws pixel by pixel, while Random-Scan uses a display list and draws continuous lines.

> [!TIP]
> The term "aliasing" (stair-step effect on lines) is specific to raster displays due to their discrete pixel nature.

> [!TIP]
> Know the differences between graphics standards. GKS is older and primarily 2D. OpenGL is widely used for both 2D and 3D modern graphics.

## 📝 Quick Reference / Formula Summary

> [!IMPORTANT]
> **Frame Buffer Size Calculation**:
> If a screen has a resolution of $W \times H$ pixels, and each pixel requires $b$ bits of color depth.
> Size in bits = $W \times H \times b$
> Size in bytes = $\frac{W \times H \times b}{8}$

**Example Calculation**:
Calculate the frame buffer size required for a resolution of $1024 \times 768$ with 24-bit color.
Size = $\frac{1024 \times 768 \times 24}{8}$ bytes
Size = $2,359,296$ bytes $\approx 2.25$ MB.

## ✏️ Practice Problems

1. **Calculate the memory required for a $1920 \times 1080$ display with 32-bit true color.**
   *Answer Sketch:* $1920 \times 1080 \times 32 / 8 = 8,294,400$ bytes $\approx 7.91$ MB.

2. **Differentiate between a frame buffer and a display list.**
   *Answer Sketch:* Frame buffer stores pixel intensity values for a raster display. A display list stores graphic commands (lines, text, etc.) used to drive a random-scan display.

3. **What is the function of a video controller in a raster-scan display?**
   *Answer Sketch:* It reads the pixel values from the frame buffer and converts them into analog signals (or digital signals for modern displays) to control the display device.
</Section 8.4: Computer Graphics (AEiE0804)>
