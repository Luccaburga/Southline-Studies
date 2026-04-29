# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Southline Studio is a static marketing landing page for a web development and AI automation agency. It is a single-page site written in Spanish with no build tools, frameworks, or package managers — just HTML, CSS, and vanilla JavaScript.

## Running Locally

Open `index.html` directly in a browser, or serve it with any static file server:

```bash
# Python
python -m http.server 8080

# Node
npx serve .
```

There is no build step, no compilation, and no dependencies to install.

## Architecture

### File Structure

- `index.html` — The entire page: 13 sequential sections (Navbar → Hero → Services → Portfolio → FAQ → Contact → Footer)
- `css/styles.css` — All styles, organized into labeled sections with CSS custom properties
- `js/main.js` — All interactivity, runs on `DOMContentLoaded`
- `Images/` — Static assets (PNG logos, chatbot illustration, cloud background, MP4 video)
- `update_icons.py` — One-time migration script (Phosphor → IonIcons), already applied; not needed for ongoing work

### CSS Design System

All design tokens are defined as CSS custom properties on `:root` in `css/styles.css`:

- Brand color: `--color-primary: #1D646B` (teal)
- Fonts: `--font-heading: 'Outfit'` / `--font-body: 'Inter'` (loaded from Google Fonts)
- Max content width: `--max-width: 1200px` (navbar uses 1600px)
- Transitions: `--transition-fast`, `--transition-normal`, `--transition-slow`
- Shadows: `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-glow`

Background color utility classes: `.bg-light`, `.bg-light-alt`, `.bg-light-soft`, `.section-dark`.

### JavaScript (`js/main.js`)

Five behaviors, all in one `DOMContentLoaded` listener:

1. **Navbar scroll** — adds `.scrolled` class on `window.scrollY > 50`
2. **Mobile menu** — toggles `.active` on `.nav-links`, swaps hamburger/close icon
3. **Scroll animations** — `IntersectionObserver` adds `.visible` to elements with `.fade-in`, `.fade-in-up`, `.fade-in-left`, `.fade-in-right`
4. **FAQ accordion** — toggles `.active` and sets `maxHeight` on `.faq-answer` for smooth expand/collapse
5. **Footer year** — writes `new Date().getFullYear()` into `#year`

### Icons

Icons use **IonIcons 7.1.0** via CDN (`<ion-icon name="...">` custom elements). Both ESM and nomodule fallback scripts are included in `<head>`.

### Responsive Breakpoints

- `≤1024px`: services grid goes 2-column; portfolio goes 2-column; split layout stacks vertically
- `≤768px`: mobile nav drawer; showcase rows stack; grids become horizontal scroll carousels (`overflow-x: auto; scroll-snap-type: x mandatory`)
- `≤480px`: hero font shrinks; buttons go full-width and stack vertically

### Contact / External Links

All CTAs point to WhatsApp (`https://wa.me/5491127201600`) or `mailto:hola@southlinestudio.com`. These are the live business contact points — do not change them without confirmation.
