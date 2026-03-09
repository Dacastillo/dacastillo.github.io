# Instrucciones de diseño — `dacastillo.github.io`

> **Destinatario:** Gestor de código autónomo (Claude Code, Copilot Workspace o similar)
> **Repositorio objetivo:** https://github.com/Dacastillo/dacastillo.github.io
> **Rama de trabajo:** crear `redesign/visual-and-ux` antes de hacer cualquier cambio; abrir PR hacia `main` al finalizar
> **Prerrequisito:** completar primero `Reorganize_instructions_web.md` (correcciones críticas de contenido y privacidad)
> **Idioma del sitio:** bilingüe (español en `index.html`, inglés en `eng.html`) — aplicar todos los cambios en ambas versiones

---

## Principio rector

El sitio de un investigador en física computacional y computación cuántica debe comunicar **rigor y profundidad**, no decoración. La dirección estética elegida es **minimalismo científico refinado**: tipografía clara con acentos monospace que evoquen código y fórmulas, paleta contenida con un acento de color preciso, espacio en blanco generoso, y cero ornamento que no cumpla función. El visitante tipo es un colega investigador, un posible colaborador o un comité de evaluación académica — no un cliente.

---

## Índice

1. [Stack tecnológico](#1-stack-tecnológico)
2. [Tipografía](#2-tipografía)
3. [Paleta de colores](#3-paleta-de-colores)
4. [Variables CSS globales](#4-variables-css-globales)
5. [Layout y estructura de páginas](#5-layout-y-estructura-de-páginas)
6. [Componentes nuevos](#6-componentes-nuevos)
7. [Animaciones y micro-interacciones](#7-animaciones-y-micro-interacciones)
8. [Responsividad móvil](#8-responsividad-móvil)
9. [Modo oscuro](#9-modo-oscuro)
10. [Orden de implementación](#10-orden-de-implementación)
11. [Criterio de éxito visual](#11-criterio-de-éxito-visual)

---

## 1. Stack tecnológico

### 1.1 Decisión sobre Bootstrap

El sitio usa actualmente Bootstrap 3.x (2013), que depende de jQuery y tiene un CSS de ~140 KB. Hay dos opciones:

**Opción A — Migrar a Bootstrap 5.x** (recomendada si se quiere mantener el sistema de grid y los componentes conocidos)

Bootstrap 5 elimina la dependencia de jQuery, moderniza la API y reduce el tamaño del CSS.

```html
<!-- Reemplazar en el <head> de todos los HTML: -->

<!-- ANTES (Bootstrap 3): -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.x.x/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.x.x/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.x.x/js/bootstrap.min.js"></script>

<!-- DESPUÉS (Bootstrap 5.3): -->
<link rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
  integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
  crossorigin="anonymous">
<script
  src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-YvpcrYf0tY3lHB60NNkmXc4s9bIOgUxi8T/jzmqQ1sFDRKGFUR9sptY3LjRB0jzO"
  crossorigin="anonymous"></script>
```

> ⚠️ **Cambios de API entre Bootstrap 3 y 5:** la clase `col-xs-*` pasó a `col-*`, `navbar-inverse` a `navbar-dark`, `data-toggle` a `data-bs-toggle`, `data-dismiss` a `data-bs-dismiss`. Buscar y reemplazar sistemáticamente en todos los HTML.

**Opción B — Eliminar Bootstrap, usar CSS puro** (recomendada si se va a rediseñar el layout desde cero)

Un sitio de investigador con pocas páginas y sin componentes complejos (sin dropdowns animados, sin carruseles, sin modales) no necesita un framework CSS. CSS Grid + Flexbox + las variables de §4 son suficientes y resultan en un sitio más rápido y más fácil de mantener.

```css
/* layout base sin Bootstrap — añadir en assets/css/main.css */
*, *::before, *::after { box-sizing: border-box; }

body {
  max-width: 720px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

nav {
  display: flex;
  gap: 1.5rem;
  align-items: center;
  flex-wrap: wrap;
}

main {
  display: grid;
  gap: 3rem;
}
```

> **Recomendación final:** si no se va a rediseñar el layout completamente, elegir **Opción A** para no romper la estructura existente. Si se va a rediseñar, **Opción B** produce un resultado más liviano y con mayor identidad propia.

### 1.2 Mover CSS a archivo externo

Si actualmente los estilos están embebidos en `<style>` dentro de los HTML:

```bash
# Verificar si hay estilos embebidos
grep -rn "<style" *.html
```

Crear `assets/css/main.css` y mover todos los `<style>` ahí. En cada HTML:

```html
<!-- Añadir en el <head>: -->
<link rel="stylesheet" href="assets/css/main.css">
```

Esto permite mantener los estilos en un solo lugar. Si hay estilos específicos de página, crear también `assets/css/cv.css`, `assets/css/pro.css`, etc.

---

## 2. Tipografía

### 2.1 Principio

Usar exactamente dos fuentes: una para títulos y una para cuerpo. Añadir una tercera fuente monoespaciada para destacar nombres de herramientas, lenguajes y código inline.

### 2.2 Fuentes recomendadas

```html
<!-- Añadir en el <head> de todos los HTML, antes de main.css: -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;0,600;1,300&family=DM+Sans:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

| Rol | Fuente | Peso | Uso |
|---|---|---|---|
| Títulos y nombre | **Spectral** (serif) | 300, 600 | `<h1>`, `<h2>`, nombre en hero |
| Cuerpo y navegación | **DM Sans** (sans-serif) | 300, 400 | `<p>`, `<nav>`, `<li>` |
| Código y herramientas | **JetBrains Mono** (monospace) | 400 | `<code>`, nombres de stacks, badges |

> **Justificación:** Spectral es una serif de lectura larga diseñada para pantallas — evoca publicaciones académicas sin parecer anticuada. DM Sans es una sans-serif geométrica neutra que complementa sin competir. JetBrains Mono como tercera voz da inmediatamente el tono técnico-científico cada vez que se nombra una herramienta.

```css
/* En assets/css/main.css: */
body {
  font-family: 'DM Sans', sans-serif;
  font-weight: 300;
  font-size: 1rem;
  line-height: 1.75;
}

h1, h2, h3 {
  font-family: 'Spectral', serif;
  font-weight: 300;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

h1 { font-size: clamp(2rem, 5vw, 3.5rem); }
h2 { font-size: clamp(1.25rem, 3vw, 1.75rem); }

/* Nombres de herramientas, lenguajes y stacks */
code, .stack-tag, .tool-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85em;
  background: var(--color-code-bg);
  padding: 0.1em 0.4em;
  border-radius: 3px;
}
```

---

## 3. Paleta de colores

### 3.1 Paleta principal

Una paleta contenida: fondo blanco (o casi blanco), texto casi negro, y un único color de acento. El acento es lo único que da identidad visual — elegirlo con cuidado.

```css
/* Opción de acento recomendada: azul-teal profundo */
/* Evoca materiales 2D, física del estado sólido, profundidad */

:root {
  /* Fondos */
  --color-bg:         #fafaf8;  /* blanco cálido, no frío */
  --color-bg-subtle:  #f2f1ed;  /* para tarjetas y secciones alternadas */
  --color-code-bg:    #ebebeb;  /* fondo para <code> inline */

  /* Texto */
  --color-text:       #1a1a18;  /* casi negro, ligeramente cálido */
  --color-text-muted: #666660;  /* texto secundario, fechas, subtítulos */

  /* Acento único */
  --color-accent:     #1a5c73;  /* azul petróleo — evoca agua, física, profundidad */
  --color-accent-light: #e8f3f7; /* versión muy clara para fondos hover */

  /* Bordes */
  --color-border:     #d8d7d3;

  /* Navegación activa */
  --color-nav-active: var(--color-accent);
}
```

> **Alternativas de acento** si se prefiere otro tono:
> - `#2d5a27` — verde oscuro (evoca materiales, química)
> - `#4a3728` — marrón tierra (más humanístico, filosófico — coherente con el Manifiesto)
> - `#2a2a4a` — azul medianoche (computación cuántica, circuitos)

### 3.2 Uso del acento

El acento se aplica **solo** a:
- Links en hover y focus
- El indicador de sección activa en la navegación
- La línea decorativa bajo el nombre en el hero
- Los badges de ORCID/GitHub (ver §6.2)
- Los tags de stack tecnológico en las tarjetas de proyectos

**Nunca** se usa como color de fondo de secciones grandes ni como color de texto del cuerpo.

---

## 4. Variables CSS globales

Crear un bloque de variables CSS completo al inicio de `assets/css/main.css`:

```css
/* assets/css/main.css */

:root {
  /* ─── Colores ──────────────────────────────────────────────────── */
  --color-bg:           #fafaf8;
  --color-bg-subtle:    #f2f1ed;
  --color-code-bg:      #ebebeb;
  --color-text:         #1a1a18;
  --color-text-muted:   #666660;
  --color-accent:       #1a5c73;
  --color-accent-light: #e8f3f7;
  --color-border:       #d8d7d3;

  /* ─── Tipografía ───────────────────────────────────────────────── */
  --font-body:    'DM Sans', system-ui, sans-serif;
  --font-heading: 'Spectral', Georgia, serif;
  --font-mono:    'JetBrains Mono', 'Courier New', monospace;

  /* ─── Espaciado ────────────────────────────────────────────────── */
  --space-xs:   0.25rem;
  --space-sm:   0.5rem;
  --space-md:   1rem;
  --space-lg:   2rem;
  --space-xl:   4rem;

  /* ─── Layout ───────────────────────────────────────────────────── */
  --max-width:    720px;
  --max-width-wide: 960px;

  /* ─── Bordes y radios ──────────────────────────────────────────── */
  --radius-sm: 4px;
  --radius-md: 8px;
  --border: 1px solid var(--color-border);

  /* ─── Transiciones ─────────────────────────────────────────────── */
  --transition-fast: 150ms ease;
  --transition-mid:  300ms ease;
}
```

---

## 5. Layout y estructura de páginas

### 5.1 Hero section (`index.html` y `eng.html`)

El área hero — la primera impresión — debe incluir:

1. **Nombre completo** en Spectral, grande
2. **Línea decorativa** con el color acento (un `<hr>` estilizado o un `border-bottom`)
3. **Título profesional** en DM Sans, muted
4. **Descripción breve** (2–3 líneas, actualizada según §3.1 de Reorganize_instructions_web.md)
5. **Row de badges** de redes académicas (ver §6.2)
6. **Foto de perfil** (ver §6.1), flotando a la derecha o en grid al lado del texto

```html
<!-- Estructura HTML del hero — reemplazar el contenido actual del hero en index.html -->
<section class="hero">
  <div class="hero-text">
    <h1>Daniel Castillo Castro</h1>
    <p class="hero-title">Doctor en Física · Investigador en Nanomateriales Computacionales</p>
    <p class="hero-bio">
      Trabajo en el modelamiento multiescala de materiales 2D y en la intersección
      entre simulación computacional, potenciales interatómicos basados en ML y
      computación cuántica aplicada a química molecular. Miembro del grupo Moleqlas
      (QuDIT, PUC Chile).
    </p>
    <div class="hero-badges">
      <!-- Ver §6.2 para el HTML de cada badge -->
    </div>
  </div>
  <div class="hero-photo">
    <!-- Ver §6.1 para la foto de perfil -->
  </div>
</section>
```

```css
/* CSS del hero */
.hero {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: var(--space-lg);
  align-items: start;
  padding: var(--space-xl) 0 var(--space-lg);
  border-bottom: var(--border);
}

.hero h1 {
  margin: 0 0 var(--space-xs);
  color: var(--color-text);
}

/* Línea decorativa bajo el h1 */
.hero h1::after {
  content: '';
  display: block;
  width: 3rem;
  height: 2px;
  background: var(--color-accent);
  margin-top: var(--space-sm);
}

.hero-title {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin: 0 0 var(--space-md);
  letter-spacing: 0.02em;
}

.hero-bio {
  max-width: 55ch;
  color: var(--color-text);
  margin-bottom: var(--space-md);
}

/* Mobile: apilar verticalmente */
@media (max-width: 600px) {
  .hero {
    grid-template-columns: 1fr;
  }
  .hero-photo { order: -1; }
}
```

### 5.2 Navegación

La barra de navegación actual probablemente es un navbar de Bootstrap. Simplificarla:

```html
<!-- Reemplazar la navbar actual con: -->
<header>
  <nav class="site-nav">
    <a href="index.html" class="nav-logo">DC</a>
    <ul>
      <li><a href="man.html">Manifiesto</a></li>
      <li><a href="cv.html">CV</a></li>
      <li><a href="pro.html">Proyectos</a></li>
      <li><a href="link.html">Links</a></li>
      <li><a href="eng.html" class="nav-lang">EN</a></li>
    </ul>
  </nav>
</header>
```

```css
.site-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: var(--space-md) 0;
  border-bottom: var(--border);
  gap: var(--space-md);
}

.site-nav ul {
  display: flex;
  list-style: none;
  gap: var(--space-lg);
  margin: 0; padding: 0;
}

.site-nav a {
  font-size: 0.9rem;
  font-weight: 400;
  color: var(--color-text-muted);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.site-nav a:hover,
.site-nav a[aria-current="page"] {
  color: var(--color-accent);
}

.nav-logo {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--color-text) !important;
}

/* Indicar la página activa añadiendo aria-current="page" en el HTML */
/* de cada página a su propio link de navegación */
```

### 5.3 Footer

```html
<!-- Reemplazar el footer actual con: -->
<footer class="site-footer">
  <div class="footer-location">Santiago, Chile</div>
  <div class="footer-links">
    <a href="https://github.com/Dacastillo" target="_blank" rel="noopener noreferrer">GitHub</a>
    <a href="https://www.linkedin.com/in/esdacastillo/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
    <a href="https://orcid.org/0000-0002-9556-4831" target="_blank" rel="noopener noreferrer">ORCID</a>
    <a href="https://www.instagram.com/castillocastro_/" target="_blank" rel="noopener noreferrer">Instagram</a>
    <!-- Mastodon si sigue activo: -->
    <a href="https://chilemasto.casa/@dacastillo" target="_blank" rel="noopener noreferrer">Mastodon</a>
  </div>
  <div class="footer-copy">© 2018–2026 Daniel Castillo Castro</div>
</footer>
```

```css
.site-footer {
  margin-top: var(--space-xl);
  padding-top: var(--space-lg);
  border-top: var(--border);
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
  align-items: center;
  text-align: center;
}

.footer-links {
  display: flex;
  gap: var(--space-lg);
  flex-wrap: wrap;
  justify-content: center;
}

.footer-links a {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--color-text-muted);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-links a:hover { color: var(--color-accent); }

.footer-copy {
  font-size: 0.75rem;
  color: var(--color-text-muted);
}
```

---

## 6. Componentes nuevos

### 6.1 Foto de perfil

Añadir una foto profesional en el hero. Si no se tiene una foto, una ilustración abstracta o simplemente omitir el componente.

```html
<!-- En la sección hero de index.html: -->
<div class="hero-photo">
  <img
    src="assets/img/profile.jpg"
    alt="Daniel Castillo Castro"
    width="140" height="140"
    loading="eager">
</div>
```

```css
.hero-photo img {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--color-bg-subtle);
  filter: grayscale(15%);           /* ligeramente desaturada — más formal */
  transition: filter var(--transition-mid);
}

.hero-photo img:hover {
  filter: grayscale(0%);
}
```

> **Sobre la imagen:** usar una foto de resolución mínima 280×280px (se mostrará a 140px, el doble para pantallas retina). Guardar como `assets/img/profile.jpg` con compresión ~80%.

### 6.2 Badges académicos

Reemplazar o complementar los iconos SVG de redes sociales con badges de identidad académica en el hero:

```html
<!-- Row de badges — insertar en .hero-badges -->
<div class="hero-badges">
  <a href="https://orcid.org/0000-0002-9556-4831"
     class="badge-link" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/ORCID-0000--0002--9556--4831-brightgreen?style=flat&logo=orcid"
         alt="ORCID" loading="lazy">
  </a>
  <a href="https://github.com/Dacastillo"
     class="badge-link" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/GitHub-Dacastillo-181717?style=flat&logo=github"
         alt="GitHub" loading="lazy">
  </a>
  <a href="https://www.linkedin.com/in/esdacastillo/"
     class="badge-link" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/LinkedIn-esdacastillo-0077B5?style=flat&logo=linkedin"
         alt="LinkedIn" loading="lazy">
  </a>
</div>
```

```css
.hero-badges {
  display: flex;
  gap: var(--space-sm);
  flex-wrap: wrap;
}

.badge-link img {
  height: 20px;
  transition: opacity var(--transition-fast);
}

.badge-link:hover img {
  opacity: 0.8;
}
```

### 6.3 Tarjetas de proyectos (`pro.html`)

Las tarjetas de proyectos deben ser uniformes y scanneables. Para cada proyecto:

```html
<!-- Plantilla de tarjeta de proyecto — repetir para cada proyecto en pro.html -->
<article class="project-card">
  <div class="project-header">
    <h3 class="project-title">
      <a href="https://github.com/Dacastillo/QQuipu3" target="_blank" rel="noopener noreferrer">
        QQuipu3
      </a>
    </h3>
    <span class="project-year">2024</span>
  </div>
  <p class="project-description">
    Simulación de estados térmicos/Gibbs con circuitos cuánticos.
    Preparación del estado ρ<sub>β</sub> = e<sup>−βH</sup>/Z usando Qiskit.
  </p>
  <div class="project-stack">
    <code>Qiskit</code>
    <code>Python</code>
    <code>Jupyter</code>
  </div>
</article>
```

```css
.project-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--space-md);
}

.project-card {
  padding: var(--space-md);
  border: var(--border);
  border-radius: var(--radius-md);
  background: var(--color-bg);
  transition: border-color var(--transition-fast),
              box-shadow var(--transition-fast);
}

.project-card:hover {
  border-color: var(--color-accent);
  box-shadow: 0 2px 12px rgba(26, 92, 115, 0.08);
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: var(--space-sm);
}

.project-title {
  font-family: var(--font-heading);
  font-size: 1.1rem;
  font-weight: 400;
  margin: 0;
}

.project-title a {
  color: var(--color-text);
  text-decoration: none;
}

.project-title a:hover { color: var(--color-accent); }

.project-year {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--color-text-muted);
}

.project-description {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  margin: 0 0 var(--space-sm);
  line-height: 1.6;
}

.project-stack {
  display: flex;
  gap: var(--space-xs);
  flex-wrap: wrap;
}
```

### 6.4 Sección de publicaciones (`cv.html`)

Si hay papers publicados con DOI, añadir una sección de publicaciones en `cv.html`:

```html
<!-- Sección de publicaciones en cv.html -->
<section class="publications">
  <h2>Publicaciones</h2>
  <ol class="pub-list" reversed>
    <li class="pub-item">
      <span class="pub-authors">Castillo-Castro, D., [coautores].</span>
      <span class="pub-title">"[Título del artículo]."</span>
      <span class="pub-venue"><em>[Nombre de la revista]</em>, [volumen], [páginas] ([año]).</span>
      <a class="pub-doi" href="https://doi.org/[DOI]"
         target="_blank" rel="noopener noreferrer">
        DOI: [DOI]
      </a>
    </li>
    <!-- Repetir para cada publicación, del más reciente al más antiguo -->
  </ol>
</section>
```

```css
.pub-list {
  list-style: none;
  padding: 0;
  counter-reset: pub-counter;
}

.pub-item {
  padding: var(--space-md) 0;
  border-bottom: var(--border);
  line-height: 1.7;
  font-size: 0.95rem;
}

.pub-item:last-child { border-bottom: none; }

.pub-authors {
  color: var(--color-text-muted);
}

.pub-title {
  font-weight: 500;
}

.pub-doi {
  display: inline-block;
  margin-top: var(--space-xs);
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--color-accent);
  text-decoration: none;
}

.pub-doi:hover { text-decoration: underline; }
```

---

## 7. Animaciones y micro-interacciones

El sitio es de contenido denso — las animaciones deben ser **sutiles y funcionales**, no llamativas. Nada que distraiga de la lectura.

### 7.1 Animación de entrada del hero

```css
/* Aparición suave del contenido al cargar */
@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero {
  animation: fadeUp 0.5s ease both;
}

.hero-text h1  { animation: fadeUp 0.5s 0.05s ease both; }
.hero-title    { animation: fadeUp 0.5s 0.10s ease both; }
.hero-bio      { animation: fadeUp 0.5s 0.15s ease both; }
.hero-badges   { animation: fadeUp 0.5s 0.20s ease both; }
```

### 7.2 Hover en links de navegación

```css
/* Subrayado animado en los links de nav */
.site-nav a {
  position: relative;
}

.site-nav a::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 1px;
  background: var(--color-accent);
  transition: width var(--transition-fast);
}

.site-nav a:hover::after,
.site-nav a[aria-current="page"]::after {
  width: 100%;
}
```

### 7.3 Scroll suave

```css
/* En :root o html */
html {
  scroll-behavior: smooth;
}
```

### 7.4 Focus visible para accesibilidad

```css
/* Esencial para navegación por teclado */
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}
```

### 7.5 Respeto por `prefers-reduced-motion`

```css
/* Los usuarios que han configurado reducir movimiento en su SO no deben ver animaciones */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. Responsividad móvil

### 8.1 Viewport meta tag

Verificar que **todos** los HTML tienen este tag en el `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 8.2 Breakpoints clave

```css
/* Un solo breakpoint es suficiente para este sitio */
@media (max-width: 600px) {

  /* Hero: apilar verticalmente */
  .hero {
    grid-template-columns: 1fr;
  }
  .hero-photo {
    order: -1;          /* foto arriba en mobile */
    display: flex;
    justify-content: center;
  }

  /* Navegación: reducir gap */
  .site-nav ul {
    gap: var(--space-md);
  }
  .site-nav a {
    font-size: 0.8rem;
  }

  /* Tarjetas de proyectos: una columna */
  .project-grid {
    grid-template-columns: 1fr;
  }

  /* Footer: reducir gap */
  .footer-links {
    gap: var(--space-md);
  }
}
```

### 8.3 Imágenes responsivas

Todas las imágenes del sitio deben tener `max-width: 100%`:

```css
img {
  max-width: 100%;
  height: auto;
}
```

---

## 9. Modo oscuro

Añadir soporte para modo oscuro automático (respeta la preferencia del SO del visitante) sin añadir un toggle manual — mantiene el sitio simple.

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg:           #141412;
    --color-bg-subtle:    #1e1e1c;
    --color-code-bg:      #2a2a28;
    --color-text:         #e8e7e3;
    --color-text-muted:   #8a8a85;
    --color-accent:       #4da6c0;  /* acento más claro en dark mode */
    --color-accent-light: #1a3a44;
    --color-border:       #2e2e2c;
  }

  /* Ajustes específicos para dark mode */
  .hero-photo img {
    filter: grayscale(10%) brightness(0.9);
  }

  .project-card:hover {
    box-shadow: 0 2px 12px rgba(77, 166, 192, 0.12);
  }
}
```

> Con solo estas variables redefinidas, todo el sitio cambia al modo oscuro automáticamente porque todo está construido sobre variables CSS de §4.

---

## 10. Orden de implementación

Hacer cada paso en un commit separado para poder revertir fácilmente si algo se rompe.

| Paso | Tarea | Commit message sugerido |
|------|-------|------------------------|
| 1 | Actualizar Bootstrap CDN (§1.1) | `style: upgrade Bootstrap 3 to 5.3` |
| 2 | Crear `assets/css/main.css` con variables y tipografía base (§4, §2) | `style: add CSS variables and typography system` |
| 3 | Añadir Google Fonts al `<head>` de todos los HTML (§2.2) | `style: add Spectral, DM Sans, JetBrains Mono fonts` |
| 4 | Modernizar navbar con CSS nuevo (§5.2) | `style: refactor navigation bar` |
| 5 | Refactorizar hero section (§5.1) | `style: redesign hero section with grid layout` |
| 6 | Añadir foto de perfil al hero (§6.1) | `content: add profile photo to hero` |
| 7 | Añadir badges académicos (§6.2) | `content: add ORCID, GitHub, LinkedIn badges to hero` |
| 8 | Refactorizar footer (§5.3) | `style: clean up footer layout` |
| 9 | Refactorizar tarjetas de proyectos en `pro.html` (§6.3) | `style: add project cards with stack tags` |
| 10 | Añadir sección de publicaciones en `cv.html` (§6.4) | `content: add publications section with DOIs` |
| 11 | Añadir animaciones de entrada y hover (§7) | `style: add subtle entrance animations and hover states` |
| 12 | Añadir soporte responsive (§8) | `style: add mobile responsive breakpoints` |
| 13 | Añadir dark mode (§9) | `style: add automatic dark mode via prefers-color-scheme` |
| 14 | Verificar en mobile, dark mode, y con navegación por teclado | — |
| 15 | Abrir PR hacia `main` | — |

---

## 11. Criterio de éxito visual

Antes de aprobar el PR, verificar manualmente:

**Tipografía:**
- [ ] Los títulos se renderizan en Spectral (serif)
- [ ] El cuerpo se renderiza en DM Sans (sans-serif)
- [ ] Los nombres de herramientas y stacks se renderizan en JetBrains Mono

**Color:**
- [ ] El fondo es `#fafaf8` (no blanco puro)
- [ ] El único elemento con `--color-accent` son links hover, el indicador nav y los badges
- [ ] No hay ningún color de fondo de sección en el acento

**Hero:**
- [ ] El nombre aparece grande (≥2rem) en Spectral
- [ ] La línea de título profesional está en monospace, muted
- [ ] Los badges de ORCID, GitHub y LinkedIn son visibles y sus links son correctos
- [ ] La foto de perfil (si se añade) es circular y carga sin desplazar el layout

**Proyectos:**
- [ ] Cada tarjeta muestra: nombre (link), descripción, stack en monospace
- [ ] El hover en cada tarjeta muestra `border-color: var(--color-accent)` suavemente

**Mobile (redimensionar a 375px):**
- [ ] El hero apila verticalmente: foto arriba, texto abajo
- [ ] La navegación no se desborda horizontalmente
- [ ] Las tarjetas de proyectos ocupan el ancho completo

**Dark mode (activar en el SO):**
- [ ] El fondo cambia a `#141412`
- [ ] El texto sigue siendo legible
- [ ] El acento es más claro (`#4da6c0`)

**Accesibilidad:**
- [ ] Todos los links tienen texto visible o `alt` descriptivo
- [ ] El foco de teclado es visible (outline azul-teal)
- [ ] No hay animaciones con `prefers-reduced-motion: reduce` activo
