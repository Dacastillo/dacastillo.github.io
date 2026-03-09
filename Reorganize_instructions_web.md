# Instrucciones de reorganización y documentación — `Dacastillo/dacastillo.github.io`

> **Destinatario:** Gestor de código autónomo (Claude Code, Copilot Workspace o similar)
> **Repositorio objetivo:** https://github.com/Dacastillo/dacastillo.github.io
> **Sitio desplegado:** https://dacastillo.github.io
> **Nombre del archivo de instrucciones:** `Reorganize_instructions_web.md`
> **Rama de trabajo:** crear `refactor/content-and-structure` antes de hacer cualquier cambio; abrir PR hacia `main` al finalizar
> **Idioma de documentación del repo:** español para comentarios narrativos; seguir el idioma ya usado en cada archivo HTML para el contenido visible

---

## 0. Diagnóstico del estado actual

### Estructura conocida del repositorio

```
dacastillo.github.io/
├── index.html          ← Página de inicio (versión español)
├── eng.html            ← Página de inicio (versión inglés)
├── man.html            ← Manifiesto
├── cv.html             ← Curriculum vitae
├── pro.html            ← Proyectos
├── link.html           ← Links de interés
├── sub1.html           ← Sub-página (panel 1 — contenido desconocido hasta auditoría)
├── sub2.html           ← Sub-página (panel 2)
├── sub3.html           ← Sub-página (panel 3)
├── logo2.png           ← Logo del sitio
├── panel1.png          ← Imagen de panel de la homepage
├── panel2.png          ← Imagen de panel de la homepage
├── panel3.png          ← Imagen de panel de la homepage
├── facebook.svg        ← Ícono de red social
├── instagram.svg       ← Ícono de red social
├── twitter.svg         ← Ícono de red social
├── linkedin.svg        ← Ícono de red social
├── README.md           ← Solo dice "Web"
└── (sin .gitignore)
```

**Nota:** los archivos de fuente QuattrocentoSans (×4) también fueron identificados en el repo `t` (docencia). Si también existen aquí, se encuentran en el root o en alguna carpeta `assets/`. Verificar en auditoría.

### Diagnóstico completo por categoría

| Problema | Descripción | Severidad |
|---|---|---|
| **Datos personales expuestos** | Número de teléfono (+56951215184) y domicilio (Batalla de Rancagua 573, Maipú) visibles públicamente en el footer del sitio | 🔴 **CRÍTICO — acción inmediata** |
| **LinkedIn URL incorrecto** | El footer enlaza a `linkedin.com/in/infostructuras/` en lugar de `linkedin.com/in/esdacastillo/` | 🔴 Crítico |
| **Sin ORCID** | No hay enlace al perfil ORCID `0000-0002-9556-4831` | 🟠 Importante |
| **Copyright 2018** | El footer muestra `© 2018`, tiene 8 años de atraso | 🟠 Importante |
| **Bio desactualizada** | "Interesado en las ciencias exactas, la informática y la filosofia" no refleja el perfil actual de investigador en nanomateriales y computación cuántica | 🟠 Importante |
| **CV desactualizado** | Probablemente refleja estado pre-2018; no incluye grado doctoral (Universidad Mayor), Moleqlas, ni proyectos actuales | 🟠 Importante |
| **Proyectos desactualizados** | La página `pro.html` no incluye repos actuales: `r`, `QQuipu3`, `Shore-Test`, `PDE-Test`, `LAMMPS-tutorial`, `Moleqlas` | 🟠 Importante |
| **README.md mínimo** | Solo dice "Web" — no da contexto para quien visite el repo en GitHub | 🟡 Deseable |
| **Sin .gitignore** | Ausente para un repo HTML/CSS/JS | 🟡 Deseable |
| **Sin meta tags SEO** | Probable falta de `<meta description>`, Open Graph, y canonical URL | 🟡 Deseable |
| **Tipografía en inglés** | La descripción del footer en inglés en `man.html` podría tener errores (verificar en auditoría) | 🟡 Deseable |
| **Links de medios** | tvenserio.com, etilmercurio.com, doblepunto.com, eldefinido.cl, c15.fernastro.com — verificar si siguen activos | 🟡 Deseable |

---

## 1. Tarea previa obligatoria: auditoría del contenido

Ejecutar antes de cualquier modificación. Guardar en `audit_log.txt` (no commitear):

```bash
# 1. Inventario completo
find . -not -path './.git/*' -type f | sort > audit_log.txt

# 2. Detectar datos personales expuestos en TODOS los archivos HTML
echo "=== BÚSQUEDA DE DATOS PERSONALES ===" >> audit_log.txt
grep -rn "+56\|Rancagua\|Maipú\|Maipu\|Battle\|Batalla" *.html >> audit_log.txt 2>/dev/null

# 3. Auditar todos los links del sitio (buscar LinkedIn incorrecto y otros)
echo "=== TODOS LOS HREFS ===" >> audit_log.txt
grep -rn 'href=' *.html | grep -v "^Binary" >> audit_log.txt

# 4. Verificar contenido de sub-páginas (desconocido hasta auditoría)
echo "=== CONTENIDO sub1 sub2 sub3 ===" >> audit_log.txt
for f in sub1.html sub2.html sub3.html; do
    echo "--- $f ---" >> audit_log.txt
    cat "$f" >> audit_log.txt 2>/dev/null || echo "(no encontrado)" >> audit_log.txt
done

# 5. Buscar tipografías versionadas
find . -name "*.ttf" -o -name "*.woff" -o -name "*.woff2" -o -name "*.otf" | \
    sort >> audit_log.txt

# 6. Verificar links de medios (si hay red disponible)
for url in \
    "http://www.tvenserio.com" \
    "http://www.etilmercurio.com" \
    "http://www.doblepunto.com" \
    "http://www.eldefinido.cl" \
    "http://c15.fernastro.com"; do
    status=$(curl -o /dev/null -s -w "%{http_code}" --max-time 5 "$url" 2>/dev/null || echo "TIMEOUT")
    echo "$url → HTTP $status" >> audit_log.txt
done

# 7. Detectar todos los Copyright/año en el sitio
grep -rn "©\|copyright\|2018\|2019\|2020\|2021\|2022\|2023\|2024" \
    *.html >> audit_log.txt 2>/dev/null

# 8. Verificar si hay referencias a Bootstrap y qué versión
grep -rn "bootstrap" *.html >> audit_log.txt 2>/dev/null

# 9. Buscar todos los textos de la bio/descripción personal
grep -rn "investigador\|physicist\|researcher\|vocación\|interesado" \
    *.html >> audit_log.txt 2>/dev/null

# 10. Verificar si hay meta tags existentes
grep -rn "<meta " *.html >> audit_log.txt 2>/dev/null
```

Registrar especialmente:
- ¿En cuántos archivos HTML aparece el número de teléfono y la dirección?
- ¿Qué contienen sub1.html, sub2.html, sub3.html?
- ¿Qué versión de Bootstrap usa el sitio (3.x, 4.x, 5.x)?
- ¿Hay archivos de fuente (.ttf/.woff) versionados además de los del repo `t`?
- ¿Qué links de medios siguen activos?

---

## 2. Correcciones críticas e inmediatas

### 2.1 🔴 Eliminar datos personales del sitio público

**Esta es la acción más urgente del repositorio.** Un número de teléfono personal y una dirección domiciliaria expuestos en un sitio web indexado por Google representan un riesgo de privacidad serio. Hacer esto en un commit separado y aislado, antes de cualquier otro cambio.

Buscar en todos los archivos HTML y eliminar o reemplazar:

```bash
# Verificar primero exactamente dónde aparecen
grep -rn "+56951215184\|Batalla de Rancagua\|Maipú\|Maipu" *.html
```

Para cada aparición encontrada:

**Reemplazar el teléfono:**
```html
<!-- ANTES (eliminar): -->
+56951215184

<!-- DESPUÉS (opciones, elegir una): -->
<!-- Opción A: eliminar completamente la línea -->
<!-- Opción B: reemplazar por email académico si se desea mantener contacto -->
<a href="mailto:[EMAIL_ACADÉMICO]">[EMAIL_ACADÉMICO]</a>
<!-- Opción C: enlace al formulario de contacto de LinkedIn -->
<a href="https://www.linkedin.com/in/esdacastillo/">LinkedIn</a>
```

**Reemplazar la dirección:**
```html
<!-- ANTES (eliminar): -->
Batalla de Rancagua 573
Maipú

<!-- DESPUÉS: -->
Santiago, Chile
```

Commit aislado con mensaje:
```
security: remove personal contact information from public site

- Remove home phone number from footer/contact sections
- Replace home address with city-level location (Santiago, Chile)
- Retain professional contact channels (LinkedIn, ORCID, GitHub)
```

### 2.2 🔴 Corregir el LinkedIn URL

En **todos** los archivos HTML donde aparezca el link incorrecto:

```bash
# Buscar el link incorrecto
grep -rn "infostructuras" *.html
```

Reemplazar en cada archivo encontrado:

```html
<!-- ANTES: -->
<a href="https://www.linkedin.com/in/infostructuras/">
<!-- o también posiblemente: -->
href="https://www.linkedin.com/in/infostructuras/"

<!-- DESPUÉS: -->
<a href="https://www.linkedin.com/in/esdacastillo/">
```

> **Atención:** `infostructuras` también aparece como link de Facebook (`facebook.com/infostructuras`). Decidir si esa página de Facebook sigue vigente o si también debe actualizarse/eliminarse.

---

## 3. Actualizaciones de contenido

### 3.1 Bio principal (`index.html` y `eng.html`)

La descripción actual es genérica y de 2018. Reemplazar en ambas versiones idiomáticas:

**Versión española** (`index.html`):
```html
<!-- ANTES: -->
Investigador independiente nacido en Santiago de Chile y con vocación global.
Interesado en las ciencias exactas, la informática y la filosofia

<!-- DESPUÉS: -->
Doctor en Física (Universidad Mayor, Chile) e investigador en modelamiento
multiescala de nanomateriales. Trabajo en la intersección entre simulación
computacional, potenciales interatómicos basados en ML y computación cuántica
aplicada a química molecular. Miembro del grupo Moleqlas (QuDIT, PUC Chile).
```

**Versión inglesa** (`eng.html`):
```html
<!-- DESPUÉS: -->
PhD in Physics (Universidad Mayor, Chile) and researcher in multiscale modeling
of nanomaterials. My work sits at the intersection of computational simulation,
machine-learning interatomic potentials, and quantum computing applied to
molecular chemistry. Member of the Moleqlas group (QuDIT, PUC Chile).
```

### 3.2 Añadir ORCID al footer/sección de contacto

En todos los archivos que tengan la sección de redes sociales del footer:

```html
<!-- Añadir junto a los otros links de redes sociales: -->
<a href="https://orcid.org/0000-0002-9556-4831"
   title="ORCID" target="_blank" rel="noopener noreferrer">
  <!-- Si se usa texto: -->
  ORCID: 0000-0002-9556-4831
  <!-- Si se usa ícono, descargar el SVG oficial de ORCID: -->
  <!-- https://orcid.org/sites/default/files/images/orcid_16x16.png -->
  <img src="assets/icons/orcid.svg" alt="ORCID" width="16" height="16">
</a>
```

Descargar el SVG oficial de ORCID:
```bash
mkdir -p assets/icons
curl -o assets/icons/orcid.svg \
    "https://orcid.org/sites/default/files/images/orcid_16x16(1).gif"
# Alternativamente, usar el SVG de shields.io embebido directamente
```

### 3.3 Actualizar el Copyright

Buscar y reemplazar en **todos** los archivos HTML:

```bash
grep -rn "2018\|© " *.html
```

```html
<!-- ANTES: -->
© 2018 Daniel Castillo Castro

<!-- DESPUÉS: -->
© 2018–2026 Daniel Castillo Castro
```

> Mantener `2018` como año de inicio documenta cuándo se creó el sitio, lo cual es válido y más honesto que un año único.

### 3.4 Actualizar `cv.html`

Esta es la página con mayor deuda de contenido. Actualizar con información actual:

**Sección de Educación** — debe incluir:
```
Doctor en Física — Universidad Mayor, Chile
  Tesis: [COMPLETAR: título de la tesis doctoral]
  [AÑO de inicio] – [AÑO de término]

Licenciado en Física — Pontificia Universidad Católica de Chile
  [AÑO]
```

**Sección de Investigación / Posición actual** — incluir:
```
Investigador / Postdoctorante
  Grupo Moleqlas, QuDIT — PUC Chile
  [AÑO] – presente
  Foco: computación cuántica aplicada a simulación molecular (VQE, estados térmicos)

Investigador en Nanomateriales Computacionales
  Modelamiento multiescala de materiales 2D (hBN, grafeno, heteroestructuras vdW)
  Potenciales interatómicos basados en ML (MLIP, Behler-Parrinello / AMP)
  Dinámica molecular con LAMMPS, DFT con GPAW / Quantum Espresso / ORCA
```

**Sección de Proyectos activos** — enlazar a GitHub:
```
Pipeline MLIP para hBN bajo deformación (GPAW → AMP, aprendizaje activo)
Sistema bibliométrico en R para IA aplicada a simulación de reacciones
Agente de auditoría LAMMPS con Claude Code
VQE con ansätze compactos (mínimo CNOT) en Qiskit
```

**Habilidades / Stack técnico** — actualizar:
```
Lenguajes: Python, R, Shell, MATLAB, Wolfram, TeX, HTML
Simulación: LAMMPS, GPAW, Quantum Espresso, ORCA
Computación cuántica: Qiskit (VQE, ansätze, estados de Gibbs)
Análisis de datos: pandas, numpy, scipy, matplotlib, ggplot2
Sistemas: Linux (HP Victus 16 / GTX 1650), Git, HPC clusters (SLURM)
```

### 3.5 Actualizar `pro.html` (Proyectos)

La página de proyectos debe reflejar el estado actual de los repositorios. Para cada proyecto, incluir: título, descripción breve, enlace al repo en GitHub, stack, y año.

Proyectos a incluir (organizados de más a menos recientes):

```
─── INVESTIGACIÓN ────────────────────────────────────────────────
r — Investigación computacional
  DFT, LAMMPS, dinámica molecular de materiales 2D y heteroestructuras
  Python · LAMMPS · TeX · MATLAB · Wolfram
  https://github.com/Dacastillo/r

Moleqlas group-repo — Computación cuántica aplicada a química
  Simulaciones cuánticas para sistemas moleculares (QuDIT, PUC Chile)
  Jupyter · Python · Qiskit
  https://github.com/Dacastillo/Moleqlas---group-repo

QQuipu3 — Simulación de estados térmicos/Gibbs
  Circuitos cuánticos para preparar estados ρ_β = e^{-βH}/Z
  Qiskit · Python
  https://github.com/Dacastillo/QQuipu3

Shore-Test — Rastreo de costas con teledetección
  CoastSat aplicado a costas chilenas: Landsat/Sentinel-2 + Google Earth Engine
  Python · Jupyter · GEE
  https://github.com/Dacastillo/Shore-Test

PDE-Test — Resolución de EDPs con elementos finitos
  FEM sobre geometrías 3D definidas por STL
  Python · Jupyter
  https://github.com/Dacastillo/PDE-Test

─── EDUCACIÓN / DIVULGACIÓN ──────────────────────────────────────
t — Material docente
  Apuntes, presentaciones y material de cursos universitarios
  LaTeX · HTML
  https://github.com/Dacastillo/t

LAMMPS-tutorial — Tutorial de LAMMPS
  Presentado en LAMMPS Workshop
  Shell · LAMMPS
  https://github.com/Dacastillo/LAMMPS-tutorial

─── HACKATHONES ──────────────────────────────────────────────────
project_Dacastillo — QHack 2023
  Proyecto presentado en el hackathon de computación cuántica QHack 2023
  Jupyter · Python
  https://github.com/Dacastillo/project_Dacastillo
```

### 3.6 Revisar `man.html` (Manifiesto)

Leer el contenido completo en la auditoría. Si el manifiesto expresa valores e intereses de 2018 que han evolucionado, actualizar para reflejar la perspectiva actual. No es necesario reescribirlo completo — solo asegurarse de que:
- No contenga datos personales (misma revisión del §2.1)
- El tono y los intereses expresados sean consistentes con el perfil actual
- Si hay referencias a proyectos o afiliaciones antiguas, actualizarlas

### 3.7 Revisar `link.html` (Links de interés)

Verificar que todos los links sigan activos (ver comando en §1). Los links de medios listados en el footer (`tvenserio.com`, `etilmercurio.com`, `doblepunto.com`, `eldefinido.cl`, `c15.fernastro.com`) son proyectos aparentemente periodísticos o de divulgación. Para cada uno:

- Si el dominio sigue activo → mantener
- Si el dominio está caído o redirige a spam → eliminar
- Si el dominio fue adquirido por terceros → eliminar inmediatamente (riesgo de que apunte a contenido no deseado)

```bash
# Verificar estado de cada dominio (ejecutar desde terminal con red)
for url in tvenserio.com etilmercurio.com doblepunto.com eldefinido.cl c15.fernastro.com; do
    echo "$url:"
    curl -sIL --max-time 5 "http://www.$url" | grep -E "HTTP|Location" | head -3
    echo "---"
done
```

---

## 4. Mejoras técnicas

### 4.1 Añadir meta tags de SEO a todos los archivos HTML

En el `<head>` de cada archivo HTML, verificar y completar:

```html
<!-- En index.html (español): -->
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Sitio oficial de Daniel Castillo Castro —
    Doctor en Física, investigador en nanomateriales computacionales y
    computación cuántica. Santiago, Chile.">
  <meta name="keywords" content="física computacional, nanomateriales,
    computación cuántica, LAMMPS, DFT, MLIP, Qiskit, Chile">
  <meta name="author" content="Daniel Castillo Castro">

  <!-- Open Graph (para compartir en redes sociales) -->
  <meta property="og:title" content="Daniel Castillo Castro — Físico Computacional">
  <meta property="og:description" content="Investigador en modelamiento multiescala
    de nanomateriales y computación cuántica aplicada a química molecular.">
  <meta property="og:url" content="https://dacastillo.github.io/">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://dacastillo.github.io/logo2.png">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://dacastillo.github.io/">

  <title>Daniel Castillo Castro — Físico Computacional</title>
</head>
```

Para las sub-páginas, ajustar `<meta name="description">`, `<link rel="canonical">` y `<title>` con el contenido específico de cada página.

En `eng.html`, adaptar al inglés:
```html
<meta name="description" content="Official site of Daniel Castillo Castro —
  PhD in Physics, researcher in computational nanomaterials and quantum computing.
  Santiago, Chile.">
<link rel="canonical" href="https://dacastillo.github.io/eng.html">
<title>Daniel Castillo Castro — Computational Physicist</title>
```

### 4.2 Añadir GitHub profile link al footer

Junto con los demás iconos de redes sociales:

```html
<!-- Añadir en la sección de iconos sociales del footer -->
<a href="https://github.com/Dacastillo"
   title="GitHub" target="_blank" rel="noopener noreferrer">
  <!-- Descargar o embeber el SVG de GitHub -->
  <img src="assets/icons/github.svg" alt="GitHub" width="24" height="24">
</a>
```

```bash
# Descargar el SVG oficial de GitHub
mkdir -p assets/icons
curl -o assets/icons/github.svg \
    "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/github.svg"
```

> **Nota sobre los SVGs existentes:** el repo probablemente ya tiene `facebook.svg`, `instagram.svg`, `twitter.svg`, `linkedin.svg` en el root. Moverlos a `assets/icons/` como parte de la reorganización de carpetas (§5), y actualizar todas las referencias en los HTML.

### 4.3 Añadir `.gitignore`

```gitignore
# ─── Sistema operativo ────────────────────────────────────────────────────────
.DS_Store
Thumbs.db
*~
*.swp

# ─── Editores ─────────────────────────────────────────────────────────────────
.vscode/
.idea/

# ─── Logs de auditoría (temporales) ──────────────────────────────────────────
audit_log.txt

# ─── Node.js (si se añade tooling en el futuro) ───────────────────────────────
node_modules/
package-lock.json
```

### 4.4 Reemplazar Twitter/X con enlace actualizado

El link a Twitter (`https://twitter.com/castillocastro_/`) ahora apunta a X.com. Actualizar:

```html
<!-- ANTES: -->
<a href="https://twitter.com/castillocastro_/">

<!-- DESPUÉS (si sigue activo en X): -->
<a href="https://x.com/castillocastro_/" title="X (Twitter)">
```

Si la cuenta ya no se usa activamente, considerar eliminar el enlace.

### 4.5 Agregar `rel="noopener noreferrer"` a todos los enlaces externos

Por seguridad y buenas prácticas:

```bash
# Detectar enlaces externos sin el atributo
grep -rn 'target="_blank"' *.html | grep -v "noopener"
```

Para cada enlace encontrado, añadir:

```html
<!-- ANTES: -->
<a href="https://..." target="_blank">

<!-- DESPUÉS: -->
<a href="https://..." target="_blank" rel="noopener noreferrer">
```

---

## 5. Reorganización de archivos

### 5.1 Nueva estructura de carpetas propuesta

```
dacastillo.github.io/
│
├── index.html              ← Root: página de inicio (español) — GitHub Pages lo sirve aquí
├── eng.html                ← Versión inglés
├── man.html                ← Manifiesto
├── cv.html                 ← CV
├── pro.html                ← Proyectos
├── link.html               ← Links
├── sub1.html               ← Sub-páginas de panels (renombrar según contenido, §5.2)
├── sub2.html
├── sub3.html
│
├── assets/
│   ├── icons/              ← SVGs de redes sociales (actualmente en root)
│   │   ├── facebook.svg
│   │   ├── instagram.svg
│   │   ├── twitter.svg     (o x.svg)
│   │   ├── linkedin.svg
│   │   ├── github.svg      ← NUEVO (§4.2)
│   │   └── orcid.svg       ← NUEVO (§3.2)
│   ├── fonts/              ← Fuentes tipográficas (si existen en el repo)
│   │   └── QuattrocentoSans-*.ttf
│   └── img/                ← Imágenes (actualmente en root)
│       ├── logo2.png
│       ├── panel1.png
│       ├── panel2.png
│       └── panel3.png
│
├── README.md               ← Reescribir (§6)
└── .gitignore              ← Crear (§4.3)
```

> **Advertencia crítica sobre GitHub Pages:** los archivos HTML deben quedarse en el **root** del repositorio (o en la carpeta `/docs/`, pero solo si se configura esa opción en Settings → Pages). **No mover** `index.html` ni los demás `.html` a subcarpetas — GitHub Pages dejaría de servirlos correctamente.

### 5.2 Mover SVGs e imágenes a `assets/`

```bash
mkdir -p assets/icons assets/img

# Mover imágenes
git mv logo2.png assets/img/
git mv panel1.png assets/img/
git mv panel2.png assets/img/
git mv panel3.png assets/img/

# Mover SVGs de redes sociales
git mv facebook.svg assets/icons/
git mv instagram.svg assets/icons/
git mv twitter.svg assets/icons/
git mv linkedin.svg assets/icons/
```

Después de mover, actualizar **todas** las referencias en los HTML:

```bash
# Buscar todas las referencias a las imágenes movidas
grep -rn "logo2.png\|panel1\|panel2\|panel3\|facebook.svg\|instagram.svg\|twitter.svg\|linkedin.svg" \
    *.html
```

Reemplazar en cada archivo:

```html
<!-- ANTES: -->
<img src="logo2.png" ...>
<img src="facebook.svg" ...>

<!-- DESPUÉS: -->
<img src="assets/img/logo2.png" ...>
<img src="assets/icons/facebook.svg" ...>
```

> **Hacer esto en un solo commit para que el sitio no quede roto.** No hacer el `git mv` y el commit por separado de la actualización de referencias HTML.

### 5.3 Renombrar sub-páginas según contenido

Leer `sub1.html`, `sub2.html`, `sub3.html` en la auditoría (§1) e inferir nombres descriptivos:

```bash
# Ejemplos de posibles renombres:
git mv sub1.html [nombre-descriptivo-1].html
git mv sub2.html [nombre-descriptivo-2].html
git mv sub3.html [nombre-descriptivo-3].html
```

Actualizar las referencias en `index.html` y `eng.html` donde los panels enlazan a estas sub-páginas.

### 5.4 Mover fuentes a `assets/fonts/` (si existen)

```bash
# Detectar si hay fuentes en el repo
find . -name "*.ttf" -o -name "*.woff" -o -name "*.woff2" -o -name "*.otf"
```

Si existen:
```bash
mkdir -p assets/fonts
git mv *.ttf assets/fonts/ 2>/dev/null
git mv *.woff assets/fonts/ 2>/dev/null
```

Actualizar las referencias `@font-face` en los CSS o en los `<style>` embebidos de los HTML.

---

## 6. Actualizar `README.md` del repositorio

El README actual solo dice "Web". Reemplazarlo con:

```markdown
# dacastillo.github.io — Sitio web personal

Código fuente del sitio personal de [Daniel Castillo Castro](https://dacastillo.github.io).

**Sitio desplegado:** https://dacastillo.github.io

## Estructura

| Archivo | Contenido |
|---------|-----------|
| `index.html` | Página de inicio (español) |
| `eng.html` | Página de inicio (inglés) |
| `man.html` | Manifiesto |
| `cv.html` | Curriculum vitae |
| `pro.html` | Proyectos |
| `link.html` | Links de interés |
| `assets/` | Imágenes, iconos y fuentes |

## Tecnología

Sitio estático desplegado mediante GitHub Pages.

## Autor

Daniel Castillo Castro ·
[ORCID](https://orcid.org/0000-0002-9556-4831) ·
[LinkedIn](https://www.linkedin.com/in/esdacastillo/) ·
[GitHub](https://github.com/Dacastillo)
```

---

## 7. Consideraciones adicionales de diseño

> Esta sección no es obligatoria para la reorganización, pero sí relevante si se decide modernizar el sitio visualmente en el mismo proceso.

**El sitio tiene 8 años** y probablemente usa Bootstrap 3.x (lanzado en 2013). Algunos puntos a evaluar:

**Si se quiere modernizar el stack:**
- Migrar a Bootstrap 5.x (ya no requiere jQuery)
- O eliminar Bootstrap completamente y usar CSS moderno (Grid + Flexbox) — un sitio de investigador puede ser deliberadamente minimalista y funciona perfectamente con CSS puro
- Actualizar cualquier referencia a CDNs de versiones antiguas (Bootstrap 3, jQuery 2.x, etc.)

**Si se quiere mantener el diseño actual:**
- Actualizar solo las versiones de Bootstrap y jQuery en los CDN links
- Verificar que el sitio sea responsive en mobile (muy probable que ya lo sea si usa Bootstrap)

**Elementos de diseño que podrían añadirse sin rediseñar:**
- Una imagen de perfil profesional (foto o ilustración)
- Badges de ORCID y LinkedIn en la sección principal (igual que en el README de GitHub)
- Una sección de publicaciones seleccionadas con DOIs (si hay papers publicados)

---

## 8. Orden de ejecución recomendado

| Paso | Tarea | Sección | Prioridad |
|------|-------|---------|-----------|
| 1 | Crear rama `refactor/content-and-structure` | — | — |
| 2 | Ejecutar auditoría completa y leer `audit_log.txt` | §1 | **Obligatorio primero** |
| 3 | **Eliminar teléfono y dirección domiciliaria** en commit aislado | §2.1 | 🔴 **CRÍTICO** |
| 4 | Corregir LinkedIn URL en todos los archivos | §2.2 | 🔴 Crítico |
| 5 | Verificar y limpiar links de medios externos | §3.7 | 🔴 Crítico (riesgo de spam) |
| 6 | Actualizar bio en `index.html` y `eng.html` | §3.1 | 🟠 Importante |
| 7 | Añadir ORCID al footer/contacto | §3.2 | 🟠 Importante |
| 8 | Actualizar copyright a `2018–2026` | §3.3 | 🟠 Importante |
| 9 | Actualizar `cv.html` con información actual | §3.4 | 🟠 Importante |
| 10 | Actualizar `pro.html` con proyectos actuales | §3.5 | 🟠 Importante |
| 11 | Revisar y actualizar `man.html` | §3.6 | 🟠 Importante |
| 12 | Crear carpetas `assets/icons/` y `assets/img/` | §5 | 🟠 Importante |
| 13 | Mover SVGs e imágenes + actualizar referencias en HTML (un solo commit) | §5.2 | 🟠 Importante |
| 14 | Renombrar sub-páginas según contenido real | §5.3 | 🟡 Deseable |
| 15 | Añadir meta tags SEO a todos los HTML | §4.1 | 🟡 Deseable |
| 16 | Añadir GitHub link al footer | §4.2 | 🟡 Deseable |
| 17 | Crear `.gitignore` | §4.3 | 🟡 Deseable |
| 18 | Actualizar Twitter → X y añadir `noopener noreferrer` | §4.4, §4.5 | 🟡 Deseable |
| 19 | Mover fuentes a `assets/fonts/` si existen | §5.4 | 🟡 Deseable |
| 20 | Reescribir `README.md` del repo | §6 | 🟡 Deseable |
| 21 | Commit: `refactor: update content, fix links, reorganize assets` | — | — |
| 22 | Verificar sitio desplegado en https://dacastillo.github.io | — | — |
| 23 | Abrir PR hacia `main` con descripción de cambios | — | — |

---

## 9. Restricciones y advertencias

- **Los archivos HTML deben permanecer en el root.** Moverlos a subcarpetas romperá el sitio en GitHub Pages (excepto si se configura `/docs/` en Settings → Pages, pero eso requiere un cambio de configuración explícito).
- **El paso de mover assets (§5.2) debe ser un único commit atómico** que incluya tanto el `git mv` como la actualización de referencias en los HTML. Si se separa en dos commits, entre ambos el sitio estará roto (imágenes rotas en producción).
- **No hacer `--force-push` sobre `main`.** GitHub Pages se sirve directamente desde `main` — un force push con errores podría romper el sitio.
- **Verificar el sitio en el navegador después de cada commit significativo.** GitHub Pages puede tardar hasta 2–3 minutos en reflejar los cambios.
- **El teléfono puede estar indexado por Google.** Aunque se elimine del código, puede seguir apareciendo en caché de buscadores. Eso se normaliza solo con el tiempo (Google recrawlea el sitio periódicamente).
- **No modificar el contenido científico** de publicaciones, afiliaciones o proyectos — solo actualizar lo que esté verificadamente obsoleto.

---

## 10. Criterio de éxito

El trabajo está completo cuando:

- [ ] `grep -rn "+56\|Rancagua\|Maipú" *.html` devuelve vacío
- [ ] `grep -rn "infostructuras" *.html` devuelve vacío (LinkedIn URL corregido)
- [ ] El sitio muestra `© 2018–2026` en el footer
- [ ] La bio refleja el perfil actual de investigador (PhD, nanomateriales, computación cuántica)
- [ ] El footer incluye enlace a ORCID `0000-0002-9556-4831`
- [ ] El footer incluye enlace a GitHub `github.com/Dacastillo`
- [ ] `cv.html` incluye el doctorado en Universidad Mayor y proyectos actuales
- [ ] `pro.html` incluye `r`, `QQuipu3`, `LAMMPS-tutorial`, `Shore-Test`, `PDE-Test`, `Moleqlas`
- [ ] Los SVGs e imágenes están en `assets/icons/` y `assets/img/` respectivamente
- [ ] El sitio sigue cargando correctamente en https://dacastillo.github.io (todas las imágenes y links OK)
- [ ] El README del repo ya no dice solo "Web"
- [ ] Existe `.gitignore`
- [ ] El PR está abierto con descripción clara, especialmente del commit de privacidad
