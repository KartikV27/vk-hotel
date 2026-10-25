# V.K Hotel — Karadichittur (வி.கே ஹோட்டல்)
> **Authentic South Indian Village Night Tiffin Restaurant Website**
> *Hot Tiffin. Homestyle Taste. • சூடான டிபன் • வீட்டு சுவை*

---

## 🍽️ 1. Project Overview

This repository contains the complete, modern, mobile-friendly website built for **V.K Hotel (வி.கே ஹோட்டல்)**, a local village evening and night-time tiffin restaurant located on Karadichittur Main Road, Tamil Nadu, India.

The website delivers an authentic South Indian dining aesthetic—blending warm cream backgrounds with deep maroon, dark roasted earth tones, and turmeric-chili accents. It features full bilingual support (Tamil and English) with an instant reactive toggle, mouthwatering food photography, a categorized tiffin menu with transparent pricing, location navigation with Google Maps, and conditional contact options.

### 📍 Business Information
- **Name:** V.K Hotel / வி.கே ஹோட்டல்
- **Location:** Karadichittur Main Road, Karadichittur, Tamil Nadu 606207, India
- **Coordinates:** `11.8285938, 78.8757887`
- **Google Maps:** [V.K Hotel on Google Maps](https://www.google.com/maps/place/V.k+Hotel/@11.8260004,78.8742624,16.75z/data=!4m6!3m5!1s0x3bab63cd567cae63:0xf87362ce2d673c6f!8m2!3d11.8285938!4d78.8757887)
- **Specialty:** Hot layered flaky porottas, crispy ghee roast & kal dosais, soft chapathis, piping hot village salna, and traditional side dishes.
- **Operating Note:** Evening & night tiffin service. (Does not falsely claim open status; hours follow fresh preparation).

---

## 🛠️ 2. Technology Stack & Architecture

- **Framework:** Angular 20 (Current Stable Release)
- **Architecture:** 100% Standalone Components & Angular Signals
- **Styling:** Modular SCSS with comprehensive design tokens and CSS variables
- **Typography:** Google Fonts (`Mukta Malar` & `Noto Sans Tamil` for Tamil script; `Plus Jakarta Sans` for English)
- **Internationalization:** Custom reactive `LanguageService` with local storage persistence and instantaneous two-way translation
- **Assets:** High-resolution food photography stored in `public/images/`

### 📂 Directory Structure
```
vk-hotel/
├── public/
│   ├── favicon.ico
│   └── images/
│       ├── hero-feast.jpg          # South Indian evening tiffin feast
│       ├── porotta.jpg             # Flaky layered porotta with hot salna
│       ├── dosa.jpg                # Crispy cone ghee roast dosa
│       ├── chapathi.jpg            # Soft chapathi with coconut vegetable kurma
│       ├── chicken-chukka.jpg      # Spicy village chicken chukka in iron kadai
│       ├── village-ambiance.jpg    # Tiffin feast food photography (replaced unverified roadside photo)
│       ├── kothu-parotta.jpg       # Street-style kothu parotta
│       └── veg-sides.jpg           # Vellai kurma, sambar, and chutneys
├── src/
│   ├── index.html                  # SEO & Social metadata, Google Fonts preconnect
│   ├── styles.scss                 # Global CSS design tokens & utilities
│   ├── main.ts                     # Application bootstrap
│   └── app/
│       ├── app.ts                  # Root standalone component
│       ├── app.html                # Semantic HTML layout & accessibility links
│       ├── app.scss                # Root styling
│       ├── models/
│       │   └── restaurant.model.ts # TypeScript interfaces for menu, config, and translations
│       ├── data/
│       │   ├── restaurant-config.ts # SINGLE CONFIG FILE for contact & location
│       │   ├── menu-data.ts        # SINGLE DATA FILE for all menu categories & dishes
│       │   └── translations.ts     # Complete Tamil & English copy dictionary
│       ├── services/
│       │   └── language.service.ts # Angular Signals-powered language toggle
│       └── components/
│           ├── header/             # Sticky header, brand, links, language toggle, mobile drawer
│           ├── hero/               # Bilingual headlines, CTAs, hero visual card, highlight pills
│           ├── menu/               # Category tabs, veg/all filter, food cards, price notice
│           ├── about/              # Authentic village tiffin story, 3 pillars, ambiance photo
│           ├── location/           # Address card, interactive Google Maps embed, directions CTA
│           ├── contact/            # Conditional Call/WhatsApp (auto-hides when unconfigured)
│           └── footer/             # Bilingual footer, quick links, copyright, back to top
├── vercel.json                     # Production SPA routing rewrites & asset caching
├── angular.json                    # Angular CLI configuration
├── package.json                    # NPM dependencies and scripts
└── tsconfig.json                   # TypeScript configuration
```

---

## ⚙️ 3. Single-File Configuration Guides

### A. Updating Restaurant Details & Contacts (`restaurant-config.ts`)
Location: `src/app/data/restaurant-config.ts`

- **Phone & WhatsApp Buttons:** Automatically hidden when left empty `""`.
- To enable calling and WhatsApp once verified:
```typescript
contact: {
  phoneNumber: '+919876543210',   // Format: +91 followed by 10 digits
  whatsappNumber: '919876543210', // Format: country code + number without plus
  email: ''
}
```

### B. Updating Menu Items & Prices (`menu-data.ts`)
Location: `src/app/data/menu-data.ts`

- Add, edit, or remove items easily under the 5 categories:
  1. `porotta` (Porotta Varieties — பரோட்டா வகைகள்)
  2. `dosai` (Dosai Varieties — தோசை வகைகள்)
  3. `chapathi` (Chapathi — சப்பாத்தி)
  4. `veg-sides` (Vegetarian Side Dishes — சைவ கறி வகைகள்)
  5. `nonveg-sides` (Non-Vegetarian Side Dishes — அசைவ கறி வகைகள்)
- Pricing is currently displayed as `"Price on request"` / `"விலை விவரம் அறிய"`. You can easily replace it with confirmed numbers (e.g., `"₹15 per piece"`, `"₹50"`).

---

## 🚀 4. Local Development

### Prerequisites
- **Node.js:** v18.19.0 or higher (v20+ recommended)
- **NPM:** v10+

### Step-by-Step Run Command
Open PowerShell or your terminal:

```bash
# Navigate to the vk-hotel directory
cd d:/PROJECT/vk-hotel

# Install dependencies (if not already installed)
npm install

# Start the local development server
npm start
```

Alternatively, from the parent workspace root (`d:/PROJECT`):
```bash
npm start
```

### Local Dev URL
Open your browser and navigate to:
```
http://localhost:4200/
```

---

## 🔍 5. Browser Verification Checklist

When viewing the website locally, check the following items:
1. **Brand & Header:** Observe "V.K HOTEL | வி.கே ஹோட்டல்" logo and subtitle "Karadichittur • கரடிசித்தூர்".
2. **Language Toggle:** Click **EN** in the header. Notice the entire interface seamlessly switches to English. Click **தமிழ்** to switch back to Tamil.
3. **Hero Section:** Verify the bilingual headlines, "Evening & Night Tiffin" pill badge, directions button, and mouthwatering hero food presentation.
4. **Menu Section:** Click through the category tabs:
   - *Porotta Varieties (பரோட்டா வகைகள்)*
   - *Dosai Varieties (தோசை வகைகள்)*
   - *Chapathi (சப்பாத்தி)*
   - *Vegetarian Side Dishes (சைவ கறி வகைகள்)*
   - *Non-Vegetarian Side Dishes (அசைவ கறி வகைகள்)*
   - Toggle the **"Veg Only / சைவம் மட்டும்"** filter button.
5. **About Section:** Verify the village roadside story and ambiance photograph.
6. **Location Section:** Check the Karadichittur Main Road address, click **"Copy Full Address"**, inspect the embedded Google Map, and test the **"Get Directions"** link.
7. **Contact Section:** Verify that because contact phone numbers are unconfirmed, the Call and WhatsApp buttons are cleanly hidden and the walk-in invitation is shown.
8. **Mobile View:** Open browser DevTools (F12) -> Toggle Device Toolbar (Ctrl+Shift+M) -> Select mobile viewport (iPhone 14 / Pixel 7). Test clicking the hamburger menu, verify the slide-out navigation drawer, and test smooth scrolling.

---

## 📦 6. Production Build & Output Directory

To generate an optimized production bundle:

```bash
cd d:/PROJECT/vk-hotel
npm run build
```

- **Build Command:** `npm run build` (or `ng build`)
- **Output Directory:** `dist/vk-hotel/browser`
- **Output Artifacts:** Minified HTML, CSS, JavaScript bundles, and static images.
- **Bundle Size:** ~91 kB (gzipped transfer size).

To run unit tests:
```bash
npm test -- --watch=false --browsers=ChromeHeadless
```

---

## ☁️ 7. Deployment Instructions (GitHub & Vercel)

> ⚠️ **Important Policy:** Do NOT push code or trigger production deployment without explicit user approval.

### A. GitHub Setup
When approved, push the repository to GitHub:
```bash
cd d:/PROJECT/vk-hotel

# Check git status
git status

# Add all files and make initial commit
git add .
git commit -m "feat: complete VK Hotel modern bilingual website"

# Connect to your GitHub repository
git remote add origin https://github.com/<YOUR_USERNAME>/vk-hotel.git
git branch -M main
git push -u origin main
```

### B. Vercel Deployment
The project includes a pre-configured `vercel.json` file with SPA fallback rewrites:
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist/vk-hotel/browser",
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

**Deploying via Vercel CLI:**
```bash
# In vk-hotel directory:
npx vercel
```

**Deploying via Vercel Web Dashboard:**
1. Log in to [vercel.com](https://vercel.com)
2. Click **"Add New Project"** and import the GitHub repository.
3. Framework Preset: **Angular**
4. Root Directory: `./` (or `vk-hotel` if deploying from the parent repo)
5. Build Command: `npm run build`
6. Output Directory: `dist/vk-hotel/browser`
7. Click **Deploy**.

---

## 📄 License & Ownership
Copyright © 2026 **V.K Hotel (வி.கே ஹோட்டல்)**, Karadichittur Main Road, Tamil Nadu 606207. All rights reserved.
