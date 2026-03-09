# dacastillo.github.io — Sitio web personal

Código fuente del sitio personal de [Daniel Castillo Castro](https://dacastillo.github.io).

**Sitio desplegado:** https://dacastillo.github.io

## Sobre mí

Doctor en Física (Universidad Mayor, Chile) e investigador en modelamiento multiescala de nanomateriales y computación cuántica aplicada a química molecular. Miembro del grupo Moleqlas (QuDIT, PUC Chile).

**ORCID:** [0000-0002-9556-4831](https://orcid.org/0000-0002-9556-4831)  
**LinkedIn:** [linkedin.com/in/esdacastillo](https://www.linkedin.com/in/esdacastillo/)  
**GitHub:** [github.com/Dacastillo](https://github.com/Dacastillo)

## Estructura del sitio

### Páginas principales

| Archivo | Contenido | Idioma |
|---------|-----------|--------|
| `index.html` | Página de inicio | Español |
| `eng.html` | Home page | English |
| `pt.html` | Página inicial | Português |
| `cv.html` | Curriculum vitae | Español |
| `pro.html` | Proyectos de investigación | Español |
| `man.html` | Manifiesto personal | Español |
| `link.html` | Links de interés | Español |

### Assets

| Carpeta | Contenido |
|---------|-----------|
| `assets/css/` | Hojas de estilo CSS (main.css, font-awesome) |
| `assets/img/` | Imágenes del sitio (logo, profile, etc.) |

## Tecnología

Sitio estático desplegado mediante GitHub Pages.

### Stack técnico

- **HTML5** semántico
- **CSS3** con variables custom properties
- **Google Fonts**: Spectral (títulos), DM Sans (cuerpo), JetBrains Mono (código)
- **Sin frameworks** — CSS puro para máximo rendimiento

### Diseño

- **Minimalismo científico** — tipografía clara, paleta contenida
- **Modo oscuro automático** — via `prefers-color-scheme`
- **Responsivo** — mobile-first, breakpoint único a 600px
- **Accesible** — focus visible, ARIA labels, navegación por teclado

## Paleta de colores

| Variable | Valor (light) | Valor (dark) | Uso |
|----------|---------------|--------------|-----|
| `--color-bg` | `#fafaf8` | `#141412` | Fondo principal |
| `--color-text` | `#1a1a18` | `#e8e7e3` | Texto principal |
| `--color-accent` | `#1a5c73` | `#4da6c0` | Acento (links, hover) |

## Desarrollo local

### Previsualización

```bash
# Opción 1: Python HTTP server
python3 -m http.server 8000

# Opción 2: PHP built-in server
php -S localhost:8000

# Opción 3: Node.js http-server
npx http-server -p 8000
```

Luego abrir http://localhost:8000 en el navegador.

### Añadir foto de perfil

Colocar una imagen cuadrada (mínimo 280×280px) en:
```
assets/img/profile.jpg
```

El sitio funciona sin la foto (se oculta automáticamente si no existe).

## Despliegue

El sitio se despliega automáticamente en GitHub Pages al hacer push a la rama `main`.

**URL:** https://dacastillo.github.io

**Tiempo de propagación:** 2–3 minutos después del push.

## Multilingüe

El sitio está disponible en tres idiomas:

| URL | Idioma |
|-----|--------|
| `/` o `/index.html` | Español (por defecto) |
| `/eng.html` | English |
| `/pt.html` | Português |

Cada página incluye enlaces de navegación entre idiomas en el header.

## Autor

Daniel Castillo Castro ·
[ORCID](https://orcid.org/0000-0002-9556-4831) ·
[LinkedIn](https://www.linkedin.com/in/esdacastillo/) ·
[GitHub](https://github.com/Dacastillo)

---

*Última actualización: Marzo 2026*
