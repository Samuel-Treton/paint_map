# 🎨 Interactive Paint Map (2D/3D)

Un outil interactif en Python permettant de peindre des reliefs en temps réel sur une toile 2D, avec une visualisation instantanée en 3D.

---

## 🚀 Fonctionnalités principales

- **Peinture interactive**
	- Dessiner avec un clic gauche.
	- Gommer avec un clic droit.

- **Visualisation 3D dynamique**
	- Mise à jour automatique de la vue 3D en temps réel.
	- Bouton pour activer ou désactiver rapidement cette vue.

- **Contrôles ajustables en temps réel**
	- Rayon du pinceau via molette de la souris.
	- Intensité de la peinture (`Incrément`) avec slider.
	- Fusion douce des traits (`Blend`) avec slider.

- **Filtres et effets**
	- Application d’un lissage gaussien via bouton dédié.

- **Gestion simplifiée des images**
	- Sauvegarde rapide (touche `z`).
	- Chargement d’images externes (touche `a`).
	- Réinitialisation complète de la toile (touche `r`).

---

## 📥 Installation rapide

### 📌 Dépendances nécessaires :
- `numpy`
- `matplotlib`
- `scipy`
- `tkinter`

Installation via pip :
```bash
pip install numpy matplotlib scipy tkinter
```

## ▶️ Utilisation

Pour lancer l'application, exécute cette commande dans un terminal :

```bash
python main.py
```

## 🎮 Commandes et raccourcis clavier

| Action                             | Raccourci              |
|------------------------------------|------------------------|
| **Peindre**                        | Clic gauche souris     |
| **Effacer**                        | Clic droit souris      |
| **Modifier le rayon du pinceau**   | Molette souris         |
| **Sauvegarder l’image actuelle**   | Touche `z`             |
| **Réinitialiser la toile**         | Touche `r`             |
| **Importer une image externe**     | Touche `a`             |
| **Lissage gaussien**               | Bouton `Smooth`        |
| **Afficher/Masquer la vue 3D**     | Bouton `3D`            |

## 📂 Sauvegarde et chargement

- Les images sauvegardées seront placées automatiquement dans le dossier courant au format PNG : painted_image_DATE.png
- Le chargement supporte uniquement le format PNG.

## 📜 Licence

Ce projet est diffusé sous licence MIT — voir le fichier [LICENSE](LICENSE) pour plus de détails.
