## Frattali e Figure Geometriche 🇮🇹

Raccolta di script Python per generare frattali e figure geometriche ricorsive, utilizzando librerie standard e grafiche (turtle, matplotlib, numpy).

---

## 📁 Struttura delle directory

```
.
├── albero-turtle/
│   └── script.py       # Albero frattale con Turtle
├── cavolfiore/
│   └── script.py       # Frattale tipo "cavolfiore"
├── curva-di-koch-fiocco-di-neve/
│   └── script.py       # Curva di Koch e fiocco di neve
├── frattale-3d/
│   └── script.py       # Tetraedro di Sierpinski 3D con matplotlib
├── frattale-di-barnsley-felce/
│   └── script.py       # Felce di Barnsley usando IFS
├── frattale-musicale/
│   └── script.py       # Visualizzazione ricorsiva musicale
├── set-di-mandelbrot/
│   └── script.py       # Generazione del set di Mandelbrot
└── triangolo-di-sierpiski/
    └── script.py       # Triangolo di Sierpinski con Turtle
```

---

## 🧰 Requisiti di sistema

* Python 3.8+
* `pip`
* Librerie Python:

  * `matplotlib`
  * `numpy`
  * (`turtle` è parte della libreria standard)

---

## 📦 Installazione su Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install python3-pip
```

---

## ⚙️ Setup ambiente virtuale

```bash
git clone https://github.com/<tuo-username>/nome-repo-frattali.git
cd nome-repo-frattali
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📋 Contenuto di requirements.txt

```
matplotlib
numpy
```

---

## 🚀 Esecuzione degli script

Di seguito un esempio di comando per ciascun progetto, da eseguire con venv attivo:

```bash
python albero-turtle/script.py        # Disegna un albero frattale
python cavolfiore/script.py           # Frattale tipo "cavolfiore"
python curva-di-koch-fiocco-di-neve/script.py  # Curva di Koch e fiocco di neve
python frattale-3d/script.py          # Tetraedro di Sierpinski 3D
python frattale-di-barnsley-felce/script.py  # Felce di Barnsley
python frattale-musicale/script.py    # Frattale musicale ricorsivo
python set-di-mandelbrot/script.py    # Set di Mandelbrot
python triangolo-di-sierpiski/script.py  # Triangolo di Sierpinski
```

---

## 🧹 Pulizia

Per rimuovere ambiente virtuale e cache Python:

```bash
deactivate
rm -rf venv __pycache__
```

---

# Fractals and Geometric Figures 🇬🇧

Collection of Python scripts to generate fractals and recursive geometric figures using standard and graphical libraries (turtle, matplotlib, numpy).

---

## 📁 Directory Structure

```
.
├── albero-turtle/
│   └── script.py       # Fractal tree with Turtle
├── cavolfiore/
│   └── script.py       # Cauliflower-like fractal
├── curva-di-koch-fiocco-di-neve/
│   └── script.py       # Koch curve and snowflake
├── frattale-3d/
│   └── script.py       # 3D Sierpinski tetrahedron with matplotlib
├── frattale-di-barnsley-felce/
│   └── script.py       # Barnsley Fern via IFS
├── frattale-musicale/
│   └── script.py       # Recursive musical visualization
├── set-di-mandelbrot/
│   └── script.py       # Mandelbrot set generation
└── triangolo-di-sierpiski/
    └── script.py       # Sierpinski triangle with Turtle
```

---

## 🧰 System Requirements

* Python 3.8+
* `pip`
* Python libraries:

  * `matplotlib`
  * `numpy`
  * (`turtle` is part of the standard library)

---

## 📦 Installation on Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install python3-pip
```

---

## ⚙️ Virtual Environment Setup

```bash
git clone https://github.com/<your-username>/fractal-collection.git
cd fractal-collection
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📋 requirements.txt

```
matplotlib
numpy
```

---

## 🚀 Running the Scripts

With venv active:

```bash
python albero-turtle/script.py        # Draw fractal tree
python cavolfiore/script.py           # Cauliflower-like fractal
python curva-di-koch-fiocco-di-neve/script.py  # Koch curve and snowflake
python frattale-3d/script.py          # Sierpinski tetrahedron 3D
python frattale-di-barnsley-felce/script.py  # Barnsley Fern
python frattale-musicale/script.py    # Recursive musical fractal
python set-di-mandelbrot/script.py    # Mandelbrot set
python triangolo-di-sierpiski/script.py  # Sierpinski triangle
```

---

## 🧹 Cleanup

To remove virtual environment and Python cache:

```bash
deactivate
rm -rf venv __pycache__
```
Happy coding! 🚀
