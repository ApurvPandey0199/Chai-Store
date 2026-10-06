# Mistvale Tea Co. — Premium E-Commerce Store

[![Live Demo](https://img.shields.io/badge/Live_Demo-surge.sh-1f3d2b?style=for-the-badge&logo=surge)](https://mistvale-tea.surge.sh)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

> **"Hill-grown tea, honestly made."**  
> Direct from single-estate gardens in Darjeeling & Assam. Hand-harvested, whole-leaf teas delivered fresh to your doorstep.

---

## 🌐 Live Demo & Deployment

- **Production URL:** [https://mistvale-tea.surge.sh](https://mistvale-tea.surge.sh)
- **Deployment Platform:** Surge.sh (CDN-backed static web hosting with automatic SSL)

---

## 🚀 Features & Business Rules (R1–R8)

This store is built as a single-file, production-ready web application strictly enforcing all business rules, accessibility requirements, and brand specifications:

| # | Business Rule | Implementation |
|---|---|---|
| **R1** | **Data-driven Pricing** | All subtotal, discount, and shipping calculations are derived dynamically from `PRODUCTS` data, avoiding text-scraping bugs. |
| **R2** | **Purchase Quantity Caps** | Enforces a maximum quantity limit of **5 units** per product, strictly capped at available `stock`. |
| **R3** | **Coupon `WELCOME10`** | Case-insensitive coupon requiring subtotal $\ge$ ₹399. Gives 10% off eligible items (excluding "Gifts" category), capped at ₹150. Auto-invalidates if subtotal drops. |
| **R4** | **Shipping Calculation** | Standard shipping is **₹49**, becoming **FREE (₹0)** when cart amount *after discount* reaches ₹499. |
| **R5** | **Indian Currency & Rounding** | Formats all prices with `₹` and Indian digit grouping (`toLocaleString('en-IN')`). Rounds only the final order total to the nearest integer. |
| **R6** | **Sold-out Handling** | Sold-out items (`stock: 0`) cannot be added to cart and are sorted **last** across all filter and sort options. |
| **R7** | **Unified View Pipeline** | Category chips, sorting, and debounced (150ms) search run as a single view state. Async race conditions are handled via `lastSearchRequestId` counters. |
| **R8** | **Pincode Delivery Check** | Integrates `API.checkPincode()` with loading states, error fallback handling (`.catch()`), and guaranteed spinner exit (`.finally()`). |

---

## 🎨 Design System (`BRAND.md`)

- **Color Tokens:**
  - `Tea green` (`#1f3d2b`): Primary headers, primary buttons, title headings
  - `Leaf` (`#4f7942`): Secondary accents, success badges
  - `Cream` (`#f6f1e7`): Main page background
  - `Parchment` (`#ebe2cf`): Alternate card sections, trust strip
  - `Saffron` (`#d9962b`): Focus rings, sale badges, CTA accents
  - `Ink` (`#1b1b1b`): Body text
  - `Error` (`#b3261e`): Form validation and warning alerts
- **Typography:** Headings rendered in `Fraunces` (serif) and body text in `Inter` (sans-serif), loaded via single Google Fonts link with `display=swap`.
- **Aesthetic:** Calm, earthy, premium, warm, like a quiet tea garden at dawn. Zero horizontal scroll from 360px up.

---

## ♿ Accessibility & SEO

- **WCAG AA Compliant:** Contrast ratio $\ge$ 4.5:1, saffron focus rings (`:focus-visible`), interactive button tags, form inputs with visible labels.
- **Keyboard Navigation:** Modals and drawer dismissible via `Escape` key. Accessible ARIA attributes (`role="dialog"`, `aria-modal="true"`, `aria-live="polite"`).
- **SEO & Schema.org:** Single `<h1>`, Open Graph tags, Twitter Cards, canonical link, and dynamic runtime JSON-LD schemas for `OnlineStore`, `Product` (ratings only on verified products), and `FAQPage`.

---

## 📁 Repository Structure

```
.
├── index.html            # Main single-file web application (HTML, CSS, JS)
├── BRAND.md              # Official brand rules & factual guidelines
├── NOTES.md              # Engineering audit notes & testing record
├── PROMPTS.md            # AI prompt log for image and code generation
├── convert_images.py     # Python script for WebP image processing
├── images/               # Product imagery (p101–p108 WebP & hero-banner)
└── CNAME                 # Surge deployment domain configuration
```

---

## 💻 Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ApurvPandey0199/Chai-Store.git
   cd Chai-Store
   ```

2. **Open `index.html` in your browser:**
   Double click `index.html` or open via Python local HTTP server:
   ```bash
   python -m http.server 8000
   ```
   Navigate to `http://localhost:8000`.

---

## 📄 License & Attribution

Developed for **Mistvale Tea Co.** assessment.  
© 2026 Apurv Pandey / Mistvale Tea Co. All rights reserved.
