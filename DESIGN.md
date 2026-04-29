---
name: Clinical Precision & Compassion
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#45464f'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#757680'
  outline-variant: '#c5c6d1'
  surface-tint: '#4c5c92'
  primary: '#081d50'
  on-primary: '#ffffff'
  primary-container: '#223366'
  on-primary-container: '#8d9dd7'
  inverse-primary: '#b5c4ff'
  secondary: '#6b5199'
  on-secondary: '#ffffff'
  secondary-container: '#cbadfe'
  on-secondary-container: '#573d84'
  tertiary: '#3e1300'
  on-tertiary: '#ffffff'
  tertiary-container: '#612200'
  on-tertiary-container: '#ff7734'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b5c4ff'
  on-primary-fixed: '#02174a'
  on-primary-fixed-variant: '#344478'
  secondary-fixed: '#ebdcff'
  secondary-fixed-dim: '#d4bbff'
  on-secondary-fixed: '#260552'
  on-secondary-fixed-variant: '#523880'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#7d2d00'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.25'
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is anchored in the concept of "Clinical Precision & Human Warmth." It aims to evoke an immediate sense of institutional trust and sterile safety while maintaining a welcoming, accessible atmosphere for patients. 

The aesthetic follows a **Modern Corporate** approach with a heavy emphasis on **Minimalism**. By utilizing expansive white space (sterile whites) and a structured grid, the design system ensures that critical medical information is never obscured. It avoids unnecessary decorative flourishes, favoring functional clarity and a sense of calm efficiency. The visual language is designed to reassure users during high-stress moments, such as booking urgent appointments or reviewing medical results.

## Colors

The color palette is strategically layered to balance authority with accessibility. 

- **Primary Deep Navy (#223366):** Used for structural elements, headers, and primary navigation to establish a foundation of stability and professional expertise.
- **Secondary Royal Purple (#4A3077):** Applied to sophisticated accents and specialized service categories, adding a modern, premium feel to the clinical environment.
- **Accent Orange (#F16D2A):** Reserved exclusively for high-priority Call-to-Actions (CTAs) such as "Emergency" or "Book Appointment," providing a clear visual path for users.
- **Neutral Sterile White (#F7F7F7 & #FFFFFF):** These colors dominate the background to reinforce the feeling of cleanliness and provide high contrast for maximum readability.

Maintain a minimum contrast ratio of 4.5:1 for all informative text against background surfaces to ensure WCAG AA compliance.

## Typography

This design system utilizes a multi-font approach to maximize legibility and hierarchy. 

**Public Sans** serves as the headline face. Its institutional, clean, and highly accessible nature provides the "voice of the hospital"—authoritative yet open. **Manrope** is used for body copy; its modern, balanced proportions ensure that long-form medical descriptions or patient instructions remain comfortable to read over extended periods. **Inter** is utilized for labels, buttons, and data-heavy tables where functional utility and horizontal space efficiency are paramount.

Always prioritize generous line heights (1.6x for body text) to ensure content is digestible for users who may be under visual or cognitive stress.

## Layout & Spacing

The design system employs a **Fixed 12-column Grid** for desktop and a **4-column Fluid Grid** for mobile devices. The layout philosophy is centered on "Information Zoning," where content is grouped into distinct, well-padded blocks to prevent visual overwhelm.

Spacing follows an 8px rhythmic scale. Large vertical "breathing room" (xl spacing) should be used between major sections (e.g., separating Medical Services from Doctor Profiles) to maintain the clean, clinical aesthetic. Horizontal gutters are fixed at 24px to ensure distinct separation between cards and list items.

## Elevation & Depth

To maintain a sterile and modern appearance, the design system avoids heavy shadows and traditional skeuomorphism. Instead, it utilizes **Tonal Layers** and **Ambient Shadows**.

- **Surface Tiers:** The primary background is white (#FFFFFF). Elements like cards or input groups sit on a secondary neutral background (#F7F7F7) or use a very subtle, light-grey 1px border.
- **Shadows:** When depth is required (e.g., a floating appointment modal), use extra-diffused, low-opacity shadows (Opacity 5-8%) with a subtle blue tint derived from the primary color. This keeps the "airiness" of the UI while providing necessary functional elevation.
- **State Changes:** Hover states on interactive cards should transition from a flat state to a soft, lifted state rather than changing color dramatically.

## Shapes

The design system uses a **Rounded** shape language to soften the clinical nature of the content and make the interface feel more approachable. 

- **Standard Elements:** Buttons, input fields, and small cards use a 0.5rem (8px) corner radius.
- **Large Containers:** Doctor profile cards and medical service banners use 1rem (16px) for a modern, "friendly" appearance.
- **Iconography:** Icons should be enclosed in circular or highly rounded containers to maintain consistency with the soft-edged visual language.

## Components

### Buttons
Primary buttons utilize the Deep Navy (#223366) with white text. The "Book Appointment" CTA is the sole exception, utilizing the Accent Orange (#F16D2A) for maximum conversion. Use a medium weight for button labels to ensure legibility.

### Medical Service Cards
These should feature a top-aligned icon (using the Secondary Purple) followed by a Headline-MD title. The card itself should have a white background, a subtle border, and ample padding (md) to feel like a premium, dedicated service block.

### Doctor Profiles
Profiles should use a split-layout card. The left side features a high-quality portrait with "Soft" rounded corners. The right side contains the doctor's name (Headline-MD), specialty (Label-MD in Primary color), and a clear "Available" status indicator using a soft green tint.

### Appointment Booking
The booking flow must be broken into clear, linear steps. Each step should be housed in a clean container with a progress bar at the top. Use large touch targets for time-slot selection, ensuring that even users with limited motor precision can easily navigate the interface.

### Input Fields
Fields should have a 1px border in a light neutral shade, turning Primary Deep Navy on focus. Labels must always be visible (not just placeholder text) to meet accessibility standards for healthcare applications.