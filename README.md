# 🎨 Interactive Paint Map (2D/3D)

An interactive Python tool for painting reliefs in real-time on a 2D canvas, with instant 3D visualization.

---

## 🚀 Main Features

- **Interactive Painting**
	- Draw with the left mouse button.
	- Erase with the right mouse button.

- **Dynamic 3D Visualization**
	- Automatic real-time updates of the 3D view.
	- Button to quickly enable or disable this view.

- **Real-Time Adjustable Controls**
	- Brush radius via mouse wheel.
	- Painting intensity (`Increment`) with a slider.
	- Smooth blending of strokes (`Blend`) with a slider.

- **Filters and Effects**
	- Apply Gaussian smoothing via a dedicated button.

- **Simplified Image Management**
	- Quick save (key `z`).
	- Load external images (key `a`).
	- Fully reset the canvas (key `r`).

---

## 📥 Quick Installation

### 📌 Required Dependencies:
- `numpy`
- `matplotlib`
- `scipy`
- `tkinter`

Install via pip:
```bash
pip install numpy matplotlib scipy tkinter
```

For more details on dependencies, see the [requirements.txt](requirements.txt) file.

## ▶️ Usage

To launch the application, run this command in a terminal:

```bash
python3 main.py
```

## 🎮 Commands and Keyboard Shortcuts

| Action                             | Shortcut               |
|------------------------------------|------------------------|
| **Paint**                          | Left mouse click       |
| **Erase**                          | Right mouse click      |
| **Adjust brush radius**            | Mouse wheel            |
| **Save the current image**         | Key `z`                |
| **Reset the canvas**               | Key `r`                |
| **Import an external image**       | Key `a`                |
| **Quit the application**           | Key `q`                |
| **Gaussian smoothing**             | `Smooth` button        |
| **Show/Hide 3D view**              | `3D` button            |

## 📂 Saving and Loading

- Saved images will automatically be placed in the current folder in PNG format: `painted_image_DATE.png`
- Loading supports PNG format only.

## 📜 License

This project is distributed under the MIT license — see the [LICENSE](LICENSE) file for more details.
