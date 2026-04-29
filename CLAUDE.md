# CLAUDE.md — Southline Studio

## Project Overview

Static marketing landing page for Southline Studio, a web development and AI automation agency based in Argentina. Single-page site in Spanish. No build tools, no frameworks, no package managers — plain HTML, CSS, vanilla JS.

## Running Locally

```bash
python -m http.server 3000
```

Launch config: `.claude/launch.json` → server name `southline-studio` on port 3000.
Preview via `mcp__Claude_Preview__preview_start` + `preview_screenshot`.

## Architecture

- `index.html` — Full page: Navbar → Hero → Pain/Solution → Showcases → Pricing → Use Cases → Ecosystem → Integral Services → Process → CTA → FAQ → Footer
- `css/styles.css` — All styles with CSS custom properties
- `js/main.js` — DOMContentLoaded: navbar scroll, mobile menu, IntersectionObserver animations, FAQ accordion, footer year
- `Images/` — PNG logos, chatbot illustration, MP4 hero video

## Design System

**Fonts:** `Bricolage Grotesque` (headings, 400–800) + `DM Sans` (body, 300–600) via Google Fonts.

**Brand tokens in `:root`:**
- `--color-primary: #1D646B` (teal)
- `--color-primary-hover: #154D53`
- `--color-bg-dark: #080C12`
- `--radius-sm/md/lg/xl`: 6/10/16/24px
- `--shadow-sm/md/lg/glow`

**Section backgrounds (light-first system):**
- `.bg-light` — `#F7F8FA`
- `.bg-brand-tint` — `#EAF3F3` (teal-tinted, used for Ecosistema)
- `.bg-split-light` — white + ambient radial blobs (used for Pain/Solution)
- `.bg-tech-grid` — light with dot grid pattern
- `.section-dark` — `#080C12` dark, ONLY for the editorial Integral Services section

**Icons:** IonIcons 7.1.0 via CDN (`<ion-icon name="...">`)

**Responsive breakpoints:**
- `≤1024px`: grids 2-col, split stacks
- `≤768px`: mobile nav drawer, horizontal scroll carousels
- `≤480px`: hero font shrinks, buttons full-width

## Contact / External Links

- WhatsApp: `https://wa.me/5491127201600` — do NOT change without confirmation
- Email: `hola@southlinestudio.com`

---

## Frontend Design Rules

### Before writing any frontend code
- Check `Images/` for brand assets. Use the real logo, never placeholders.
- The brand color is `#1D646B`. Never substitute it.

### Anti-Generic Guardrails
- **Colors:** Derive from `--color-primary`. Never default blues/purples.
- **Shadows:** Use layered, tinted shadows (`rgba(16,25,42,...)`). Never flat `box-shadow: 0 4px 6px gray`.
- **Typography:** Bricolage Grotesque for display, DM Sans for body. Apply `letter-spacing: -0.04em` on large headings.
- **Gradients:** Layer radial gradients for depth. Add grain texture via SVG noise on dark sections only.
- **Animations:** Only animate `transform` and `opacity`. Never `transition: all`.
- **Interactive states:** Every clickable element needs hover + focus-visible. No exceptions.
- **Depth:** Light sections use blob/radial ambients for depth. Dark section uses grain + glow.
- **Spacing:** Consistent tokens — section padding 100px, card padding multiples of 8px.

### Screenshot Workflow
- Always use `mcp__Claude_Preview__preview_start` (name: `southline-studio`) before screenshots.
- Force animations visible before screenshotting: `document.querySelectorAll('.fade-in,.fade-in-up,.fade-in-left,.fade-in-right').forEach(el=>el.classList.add('visible'))`
- Check: spacing, font weight, colors, alignment, border-radius, shadows, responsive behavior.
- Minimum 2 verification rounds after visual changes.

### Hard Rules
- Edit existing files with `Edit` tool — never `Write` unless >80% rewrite.
- No narrar el plan antes de ejecutar. Solo ejecutar.
- No duplicar codigo en la respuesta si ya esta en el diff.
- Paralelizar tool calls independientes en un solo mensaje.
