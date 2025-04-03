import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Slider, Button
from scipy.ndimage import gaussian_filter
from mpl_toolkits.mplot3d import Axes3D
import datetime
import tkinter as tk
from tkinter import filedialog

# 🔧 Paramètres
N = 100
grid_size = (N, N)
brush_radius = 10
brush_min = 1
brush_max = 50
paint_step = 0.8
blend = 0.1
show_3d = True

image = np.zeros(grid_size)
is_painting = False
paint_direction = +1

X, Y = np.meshgrid(np.arange(grid_size[1]), np.arange(grid_size[0]))

def paint_at(x, y):
    x, y = int(x), int(y)
    for i in range(-brush_radius, brush_radius + 1):
        for j in range(-brush_radius, brush_radius + 1):
            xi, yj = x + i, y + j
            if 0 <= xi < image.shape[1] and 0 <= yj < image.shape[0]:
                dist2 = i**2 + j**2
                if dist2 <= brush_radius**2:
                    dist = np.sqrt(dist2) / brush_radius
                    weight = (1 - blend) + blend * (1 - dist)
                    image[yj, xi] += paint_direction * paint_step * weight
                    image[yj, xi] = np.clip(image[yj, xi], 0.0, 1.0)
    update_surface()

def update_surface():
    if show_3d:
        ax3d.clear()
        ax3d.plot_surface(X, Y, image, cmap='viridis', vmin=0, vmax=1,
                          linewidth=0, antialiased=False)
        ax3d.set_zlim(0, 1)
        ax3d.set_title("Vue 3D")
        ax3d.axis('off')
        ax3d.grid(False)

def on_press(event):
    global is_painting, paint_direction
    if event.inaxes != ax or event.xdata is None or event.ydata is None:
        return
    paint_direction = +1 if event.button == 1 else -1
    is_painting = True
    paint_at(event.xdata, event.ydata)
    im.set_data(image)
    fig.canvas.draw_idle()

def on_release(event):
    global is_painting
    is_painting = False

def on_motion(event):
    if event.inaxes != ax or event.xdata is None or event.ydata is None:
        cursor.set_visible(False)
        fig.canvas.draw_idle()
        return
    cursor.center = (event.xdata, event.ydata)
    cursor.set_radius(brush_radius)
    cursor.set_visible(True)
    if is_painting:
        paint_at(event.xdata, event.ydata)
        im.set_data(image)
    fig.canvas.draw_idle()

def on_scroll(event):
    global brush_radius
    if event.step > 0:
        brush_radius = min(brush_radius + 1, brush_max)
    elif event.step < 0:
        brush_radius = max(brush_radius - 1, brush_min)
    update_title()
    cursor.set_radius(brush_radius)
    fig.canvas.draw_idle()

def on_leave(event):
    cursor.set_visible(False)
    fig.canvas.draw_idle()

def update_step(val):
    global paint_step
    paint_step = val
    update_title()

def update_blend(val):
    global blend
    blend = val
    update_title()

def update_title():
    fig.suptitle(
        f"Rayon: {brush_radius} | Incrément: {paint_step:.2f} | Blend: {blend:.2f}",
        fontsize=10
    )

def load_image():
    root = tk.Tk()
    root.withdraw()  # On masque la fenêtre principale

    file_path = filedialog.askopenfilename(
        filetypes=[("Image PNG", "*.png")],
        title="Choisir une image à charger"
    )
    if not file_path:
        print("❌ Chargement annulé.")
        return

    try:
        img = plt.imread(file_path)
        if img.ndim == 3:
            img = img[..., :3].mean(axis=-1)  # Convertir RGB -> niveaux de gris
        img_resized = np.zeros_like(image)
        h, w = img.shape
        H, W = img_resized.shape
        img_resized[:min(h, H), :min(w, W)] = img[:min(h, H), :min(w, W)]
        image[:] = np.clip(img_resized, 0.0, 1.0)

        im.set_data(image)
        update_surface()
        fig.canvas.draw_idle()
        print(f"📂 Image chargée depuis '{file_path}'")

    except Exception as e:
        print(f"❌ Erreur lors du chargement de l'image : {e}")


def on_key(event):
    if event.key == 'z':
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"painted_image_{timestamp}.png"
        plt.imsave(filename, image, cmap='gray', vmin=0, vmax=1)
        print(f"✅ Image sauvegardée sous '{filename}'")
    elif event.key == 'r':
        image[:] = 0.0
        im.set_data(image)
        update_surface()
        fig.canvas.draw_idle()
        print("🔄 Image réinitialisée")
    elif event.key == 'a':
        load_image()


def apply_smooth(event=None):
    global image
    image[:] = gaussian_filter(image, sigma=2)
    im.set_data(image)
    update_surface()
    fig.canvas.draw_idle()
    print("✨ Lissage gaussien appliqué")

def toggle_3d(event=None):
    global show_3d
    show_3d = not show_3d
    ax3d.set_visible(show_3d)
    toggle3d_button.label.set_text("Cacher 3D" if show_3d else "Afficher 3D")
    update_surface()
    fig.canvas.draw_idle()

# Création de la figure
fig = plt.figure(figsize=(20, 10))
fig.canvas.manager.key_press_handler_id = None

# Subplots
ax = fig.add_subplot(1, 2, 1)
ax3d = fig.add_subplot(1, 2, 2, projection='3d')
ax3d.set_visible(show_3d)

# Image 2D
im = ax.imshow(image, cmap='gray', vmin=0, vmax=1)
ax.set_title("Peindre (gauche) / Gommer (droit)")
ax.axis('off')

# Curseur visuel
cursor = Circle((0, 0), brush_radius, edgecolor='red', facecolor='none', lw=1.5, visible=False)
ax.add_patch(cursor)

# Lancement vue 3D
update_surface()

# Sliders
plt.subplots_adjust(bottom=0.25)
slider_step_ax = plt.axes([0.2, 0.13, 0.6, 0.03])
slider_step = Slider(slider_step_ax, 'Incrément', 0.01, 1.0, valinit=paint_step, valstep=0.01)
slider_step.on_changed(update_step)

slider_blend_ax = plt.axes([0.2, 0.07, 0.6, 0.03])
slider_blend = Slider(slider_blend_ax, 'Blend', 0.0, 1.0, valinit=blend, valstep=0.01)
slider_blend.on_changed(update_blend)

# Bouton Smooth
button_ax = plt.axes([0.83, 0.07, 0.12, 0.05])
smooth_button = Button(button_ax, 'Smooth', hovercolor='0.85')
smooth_button.on_clicked(apply_smooth)

# Bouton Vue 3D
toggle3d_ax = plt.axes([0.83, 0.15, 0.12, 0.05])
toggle3d_button = Button(toggle3d_ax, 'Cacher 3D' if show_3d else 'Afficher 3D', hovercolor='0.85')
toggle3d_button.on_clicked(toggle_3d)

# Connexions
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('scroll_event', on_scroll)
fig.canvas.mpl_connect('figure_leave_event', on_leave)
fig.canvas.mpl_connect('key_press_event', on_key)

update_title()
plt.show()
