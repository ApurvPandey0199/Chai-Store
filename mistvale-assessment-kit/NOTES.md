# Rescue the Mistvale Tea Store — Developer Assessment Notes

## 1. What I Changed

- **Legacy Refactoring & Layout Order:** Rebuilt `index.html` as a clean, single-file vanilla application structured into the 10 required sections strictly following `BRAND.md` order.
- **Business Rules Implementation (R1–R8):**
  - **R1 (Data-driven Pricing):** Computed all pricing dynamically from `PRODUCTS` rather than DOM string text.
  - **R2 (Purchase Caps):** Enforced a maximum quantity limit of 5 units per item, capped at available `stock` across add-to-cart, quantity adjusters, and rapid double-clicks.
  - **R3 (WELCOME10 Coupon):** Implemented case-insensitive `WELCOME10` code requiring subtotal $\ge$ ₹399, 10% discount capped at ₹150, excluding "Gifts" category items. Auto-removes coupon if cart subtotal drops below ₹399.
  - **R4 (Shipping Calculation):** Applied ₹49 standard shipping, free when cart subtotal *after discount* reaches ₹499.
  - **R5 (Indian Currency Formatting):** Rounded final total to nearest rupee and formatted all amounts using `toLocaleString('en-IN')`.
  - **R6 (Sold-out Items Last):** Disabled add-to-cart buttons for out-of-stock items (`stock === 0`) and sorted sold-out items last across all sort orders.
  - **R7 (Unified Shop State):** Combined category filtering, sorting, and debounced `API.search()` into a single pipeline with request ID tracking to resolve async race conditions.
  - **R8 (Pincode Checker):** Handled `.catch()` error states and disabled button during loading to prevent stuck "Checking..." UI.
- **SEO & Structured Data:** Added unique `<title>` (51 chars), meta description (147 chars), canonical link, Open Graph, Twitter cards, and runtime dynamic JSON-LD schema generation for `OnlineStore`, `Product` (ratings only on 102 & 104), and `FAQPage`.
- **Design System:** Applied CSS custom properties (`--tea-green: #1f3d2b`, `--leaf: #4f7942`, `--cream: #f6f1e7`, `--parchment: #ebe2cf`, `--saffron: #d9962b`, `--ink: #1b1b1b`, `--error: #b3261e`), loaded `Fraunces` and `Inter` fonts, and embedded SVG logo.

---

## 2. What the AI Got Wrong

- **Search Array Filtering Bug:** The AI initially suggested using `ids.indexOf(p.id)` inside Array `.filter()`. Because `indexOf()` returns index `0` for the first match, JavaScript evaluated `0` as falsy, hiding the top search result while returning non-matching `-1` items. I identified this via console inspection and corrected it to `currentSearchIds.includes(p.id)`.
- **Cart Quantity String Concatenation:** AI code suggested `cart[i].qty = input.value + 1`, which concatenated string `"1"` into `"11"`. Fixed by explicitly parsing integers using `parseInt(..., 10)`.
- **Coupon Multi-application Bug:** Initial AI logic compounded discounts on repeated clicks (`discount += subtotal * 0.1`). Refactored to derive discount dynamically inside a pure `computeTotals()` state function.
- **Windows Terminal Unicode Encoding Crash:** Python Pillow image conversion script initially crashed on Windows command prompt due to the `\u2713` checkmark symbol encoding in `cp1252`. Fixed by replacing unicode symbols with plain text `[OK]`.

---

## 3. Images

- **Generation:** Generated 8 product images matching `PRODUCTS` descriptions (kraft pouch/tin with dry tea leaves, spices, or gift box beside) and 1 wide hero banner of Darjeeling tea garden hills at dawn under soft mist.
- **Resizing & Format:** Resized products to 800x800 and hero to 1600px width; converted all images to WebP format using Python Pillow.
- **File Size Budget:** All product WebP images are strictly under 150 KB (50–103 KB) and the hero banner is under 250 KB (237 KB).
- **Alt Text:** Added descriptive `alt` text to every image on the page.

---

## 4. How I Tested It

- **Cross-Browser & Device Viewports:** Verified functionality in Chrome, Firefox, and Edge. Tested responsive layout down to 360px mobile width with zero horizontal scrolling (`overflow-x: hidden`).
- **Keyboard & Accessibility:** Verified Tab / Shift+Tab focus navigation, saffron focus indicator rings (`:focus-visible`), button roles, and `aria-live="polite"` feedback regions.
- **Edge Cases & Business Rules:** Tested empty cart load from `localStorage`, rapid double-clicking add-to-cart, purchasing 5+ units, applying `WELCOME10` with and without gift boxes, subtotal ₹398 vs ₹399 threshold, pincode API check success/error states, and form submission payload in `<form id="checkout-form">`.

---

## 5. Questions for the Team

1. **Unverified Claims Removal:** Removed `"AS SEEN ON SHARK TANK INDIA"`, `"Rated 4.9/5 by 10,000+ happy customers!!"`, and `"BEST TEA IN THE WORLD!!!"`. Should we replace these with verified press mentions or organic customer quotes?
2. **Diwali Sale Countdown Removal:** Removed the expired/fake sale countdown timer (`2025-11-01`) and banner. Should we build a real seasonal promotion system for future harvests?
3. **Copyright Year vs Founded Year:** The footer legal text specifies `© 2020 Mistvale`, whereas company facts state founded in `2019`. Should the notice be updated to `© 2019-2026 Mistvale Tea Co.`?
4. **Free Shipping Threshold:** Confirmed free shipping applies when cart subtotal *after discount* reaches ₹499 (standard shipping ₹49). Is this threshold aligned with logistics margins?

---

## 6. Time Spent

- **Total Time:** ~3.5 hours (Audit, state refactoring, brand styling, SEO/JSON-LD, image optimization, and manual testing).

---

## 7. Extra Features

- **Debounced Search with Request ID Tracking:** 150ms input debounce with request counting to eliminate async race conditions.
- **Live Free-Shipping Progress Bar:** Visual progress bar in cart drawer indicating remaining amount needed for free shipping.
- **Dynamic JSON-LD Schema Generator:** Automatically generates Product JSON-LD from `PRODUCTS` array at runtime to eliminate schema data drift.
- **Accessible FAQ Accordion:** Interactive accordion displaying the 6 approved FAQ answers verbatim.

---

## 8. With More Time I Would

- Synchronize category filter, sort selection, and search query to URL query parameters (`?category=black&sort=low`) for shareable state links.
- Implement a "Recently Viewed Teas" bar stored in `sessionStorage`.
