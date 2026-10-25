import os
import io
import base64
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Paths
SOURCE_IMG = r'C:\Users\KARTIK\.gemini\antigravity-ide\brain\901bc63a-d23e-40c3-9428-885a8934c719\vk_chef_tawa_art_1792907987239.jpg'
PUBLIC_LOGO_DIR = r'd:\PROJECT\vk-hotel\public\logo'
SRC_LOGO_DIR = r'd:\PROJECT\vk-hotel\src\assets\logo'
PUBLIC_DIR = r'd:\PROJECT\vk-hotel\public'

os.makedirs(PUBLIC_LOGO_DIR, exist_ok=True)
os.makedirs(SRC_LOGO_DIR, exist_ok=True)

print("Processing emblem...")
# 1. Crop circular emblem with high-quality anti-aliasing
img = Image.open(SOURCE_IMG).convert('RGBA')
cx, cy = 511.0, 513.5
r = 440.0
box = (int(cx - r), int(cy - r), int(cx + r), int(cy + r))
cropped = img.crop(box)
w, h = cropped.size

# 4x supersampling mask for smooth edges
scale = 4
mask_large = Image.new('L', (w * scale, h * scale), 0)
draw_mask = ImageDraw.Draw(mask_large)
draw_mask.ellipse((0, 0, w * scale - 1, h * scale - 1), fill=255)
mask = mask_large.resize((w, h), Image.Resampling.LANCZOS)
cropped.putalpha(mask)

# Save clean emblem PNG (high-res 880x880)
emblem_path = os.path.join(PUBLIC_LOGO_DIR, 'emblem-round.png')
cropped.save(emblem_path, 'PNG', optimize=True)

# Also save compact logo (512x512)
compact_512 = cropped.resize((512, 512), Image.Resampling.LANCZOS)
compact_512.save(os.path.join(PUBLIC_LOGO_DIR, 'logo-compact.png'), 'PNG', optimize=True)

# Create optimized base64 data for SVG embedding
buffer = io.BytesIO()
# 360x360 is plenty sharp for header emblems while keeping SVG lightweight
emblem_web = cropped.resize((360, 360), Image.Resampling.LANCZOS)
emblem_web.save(buffer, format='PNG', optimize=True)
emblem_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
emblem_data_uri = f"data:image/png;base64,{emblem_b64}"

print("Creating Primary Horizontal Logo (SVG)...")
# 2. Primary Horizontal Logo SVG (for Header - Light background)
# ViewBox: 0 0 620 120
svg_horizontal = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 120" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@700;800&amp;family=Plus+Jakarta+Sans:wght@700;800;900&amp;display=swap');
      .brand-en {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 0.03em;
        fill: #7A1919;
      }}
      .brand-hotel {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: 0.02em;
        fill: #2C1810;
      }}
      .brand-sep {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 26px;
        font-weight: 400;
        fill: #D9531E;
        opacity: 0.8;
      }}
      .brand-ta {{
        font-family: 'Mukta Malar', 'Nirmala UI', sans-serif;
        font-size: 26px;
        font-weight: 800;
        letter-spacing: 0.01em;
        fill: #7A1919;
      }}
      .sub-loc {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 11.5px;
        font-weight: 800;
        letter-spacing: 0.18em;
        fill: #D9531E;
      }}
      .sub-tag {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.16em;
        fill: #6E473B;
      }}
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.15"/>
    </filter>
  </defs>

  <!-- Circular Chef Emblem -->
  <g transform="translate(10, 8)" filter="url(#shadow)">
    <!-- Outer Glow Ring -->
    <circle cx="52" cy="52" r="51" fill="none" stroke="#D4AF37" stroke-width="1.5" stroke-opacity="0.6"/>
    <circle cx="52" cy="52" r="49" fill="#FAF6EE"/>
    <!-- Clipped Emblem Image -->
    <clipPath id="circleClip">
      <circle cx="52" cy="52" r="48"/>
    </clipPath>
    <image href="{emblem_data_uri}" x="4" y="4" width="96" height="96" clip-path="url(#circleClip)" />
    <!-- Fine Inner Stroke -->
    <circle cx="52" cy="52" r="48" fill="none" stroke="#7A1919" stroke-width="1.5"/>
  </g>

  <!-- Brand Typography -->
  <g transform="translate(126, 0)">
    <!-- Decorative Green Sprout Accent above V.K -->
    <path d="M 2 24 C 6 17 14 16 18 20 C 14 25 7 26 2 24 Z" fill="#1B7A32" />
    <path d="M 12 21 C 15 15 22 15 25 18 C 22 23 16 23 12 21 Z" fill="#2E7D32" />

    <!-- English & Tamil Brand Line -->
    <text x="0" y="58">
      <tspan class="brand-en">V.K </tspan>
      <tspan class="brand-hotel">HOTEL</tspan>
      <tspan class="brand-sep" dx="8">|</tspan>
      <tspan class="brand-ta" dx="10">வி.கே ஹோட்டல்</tspan>
    </text>

    <!-- Subtitle Bar: Location & Authentic Village Identity -->
    <g transform="translate(2, 86)">
      <!-- Left ornament -->
      <line x1="0" y1="-4" x2="20" y2="-4" stroke="#D9531E" stroke-width="1.2" stroke-opacity="0.5"/>
      <circle cx="26" cy="-4" r="2" fill="#D9531E"/>

      <text x="36" y="0">
        <tspan class="sub-loc">KARADICHITTUR</tspan>
        <tspan fill="#7A1919" font-weight="900" dx="6" dy="0">•</tspan>
        <tspan class="sub-tag" dx="8">NIGHT TIFFIN</tspan>
      </text>

      <!-- Right ornament -->
      <circle cx="296" cy="-4" r="2" fill="#D9531E"/>
      <line x1="302" y1="-4" x2="332" y2="-4" stroke="#D9531E" stroke-width="1.2" stroke-opacity="0.5"/>
    </g>
  </g>
</svg>'''

with open(os.path.join(PUBLIC_LOGO_DIR, 'logo-horizontal.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_horizontal)

print("Creating Dark Background Logo (SVG)...")
# 3. Dark Background Logo SVG (for Footer / Dark Theme)
svg_dark = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 120" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@700;800&amp;family=Plus+Jakarta+Sans:wght@700;800;900&amp;display=swap');
      .brand-en-dark {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 0.03em;
        fill: #FFFFFF;
      }}
      .brand-hotel-dark {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 32px;
        font-weight: 800;
        letter-spacing: 0.02em;
        fill: #FAF6EE;
      }}
      .brand-sep-dark {{
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 26px;
        font-weight: 400;
        fill: #E6652B;
      }}
      .brand-ta-dark {{
        font-family: 'Mukta Malar', 'Nirmala UI', sans-serif;
        font-size: 26px;
        font-weight: 800;
        letter-spacing: 0.01em;
        fill: #F5EBE1;
      }}
      .sub-loc-dark {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 11.5px;
        font-weight: 800;
        letter-spacing: 0.18em;
        fill: #F09A38;
      }}
      .sub-tag-dark {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.16em;
        fill: #FAF6EE;
        opacity: 0.85;
      }}
    </style>
  </defs>

  <!-- Circular Chef Emblem with Warm Golden Rim -->
  <g transform="translate(10, 8)">
    <circle cx="52" cy="52" r="51" fill="none" stroke="#F09A38" stroke-width="2"/>
    <circle cx="52" cy="52" r="49" fill="#2C1810"/>
    <clipPath id="circleClipDark">
      <circle cx="52" cy="52" r="48"/>
    </clipPath>
    <image href="{emblem_data_uri}" x="4" y="4" width="96" height="96" clip-path="url(#circleClipDark)" />
    <circle cx="52" cy="52" r="48" fill="none" stroke="#D4AF37" stroke-width="1.2"/>
  </g>

  <!-- Brand Typography -->
  <g transform="translate(126, 0)">
    <path d="M 2 24 C 6 17 14 16 18 20 C 14 25 7 26 2 24 Z" fill="#4CAF50" />
    <path d="M 12 21 C 15 15 22 15 25 18 C 22 23 16 23 12 21 Z" fill="#81C784" />

    <text x="0" y="58">
      <tspan class="brand-en-dark">V.K </tspan>
      <tspan class="brand-hotel-dark">HOTEL</tspan>
      <tspan class="brand-sep-dark" dx="8">|</tspan>
      <tspan class="brand-ta-dark" dx="10">வி.கே ஹோட்டல்</tspan>
    </text>

    <g transform="translate(2, 86)">
      <line x1="0" y1="-4" x2="20" y2="-4" stroke="#F09A38" stroke-width="1.2" stroke-opacity="0.6"/>
      <circle cx="26" cy="-4" r="2" fill="#F09A38"/>

      <text x="36" y="0">
        <tspan class="sub-loc-dark">KARADICHITTUR</tspan>
        <tspan fill="#F09A38" font-weight="900" dx="6" dy="0">•</tspan>
        <tspan class="sub-tag-dark" dx="8">NIGHT TIFFIN</tspan>
      </text>

      <circle cx="296" cy="-4" r="2" fill="#F09A38"/>
      <line x1="302" y1="-4" x2="332" y2="-4" stroke="#F09A38" stroke-width="1.2" stroke-opacity="0.6"/>
    </g>
  </g>
</svg>'''

with open(os.path.join(PUBLIC_LOGO_DIR, 'logo-dark.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_dark)

print("Creating Compact Logo (SVG)...")
# 4. Compact Logo SVG (Icon / Mobile Drawer / Social Badge)
svg_compact = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%">
  <defs>
    <filter id="compactShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.25"/>
    </filter>
  </defs>
  <g filter="url(#compactShadow)">
    <circle cx="100" cy="100" r="96" fill="#7A1919"/>
    <circle cx="100" cy="100" r="92" fill="none" stroke="#D4AF37" stroke-width="2"/>
    <circle cx="100" cy="100" r="88" fill="#FAF6EE"/>
    <clipPath id="compactClip">
      <circle cx="100" cy="100" r="86"/>
    </clipPath>
    <image href="{emblem_data_uri}" x="14" y="14" width="172" height="172" clip-path="url(#compactClip)"/>
    <circle cx="100" cy="100" r="86" fill="none" stroke="#7A1919" stroke-width="2"/>
  </g>
</svg>'''

with open(os.path.join(PUBLIC_LOGO_DIR, 'logo-compact.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_compact)

print("Creating Full Stacked Logo (SVG)...")
# 5. Full Stacked Badge Logo (SVG) - Perfect for vertical displays, cards, posters
svg_full = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 720" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@700;800&amp;family=Plus+Jakarta+Sans:wght@700;800;900&amp;display=swap');
      .full-brand-en {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 56px;
        font-weight: 900;
        letter-spacing: 0.04em;
        text-anchor: middle;
      }}
      .full-brand-ta {{
        font-family: 'Mukta Malar', 'Nirmala UI', sans-serif;
        font-size: 38px;
        font-weight: 800;
        fill: #7A1919;
        text-anchor: middle;
      }}
      .full-sub {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 18px;
        font-weight: 800;
        letter-spacing: 0.22em;
        fill: #D9531E;
        text-anchor: middle;
      }}
      .full-tag {{
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 0.24em;
        fill: #5C3A21;
        text-anchor: middle;
      }}
    </style>
    <filter id="fullShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.18"/>
    </filter>
  </defs>

  <!-- Big Circular Emblem in Top Center -->
  <g transform="translate(100, 30)" filter="url(#fullShadow)">
    <circle cx="200" cy="200" r="196" fill="#7A1919"/>
    <circle cx="200" cy="200" r="190" fill="none" stroke="#D4AF37" stroke-width="4"/>
    <circle cx="200" cy="200" r="182" fill="#FAF6EE"/>
    <clipPath id="fullClip">
      <circle cx="200" cy="200" r="180"/>
    </clipPath>
    <image href="{emblem_data_uri}" x="20" y="20" width="360" height="360" clip-path="url(#fullClip)" />
    <circle cx="200" cy="200" r="180" fill="none" stroke="#7A1919" stroke-width="3"/>
  </g>

  <!-- Stylized Brand Typography -->
  <g transform="translate(300, 480)">
    <!-- Sprout ornament on V.K -->
    <path d="M -90 -45 C -84 -55 -74 -56 -68 -50 C -74 -44 -82 -43 -90 -45 Z" fill="#1B7A32" />
    <path d="M -77 -49 C -73 -57 -63 -57 -59 -53 C -63 -47 -71 -47 -77 -49 Z" fill="#2E7D32" />

    <text y="0" class="full-brand-en">
      <tspan fill="#7A1919">V.K </tspan>
      <tspan fill="#2C1810">HOTEL</tspan>
    </text>

    <!-- Tamil Name -->
    <text y="54" class="full-brand-ta">வி.கே ஹோட்டல்</text>

    <!-- Decorative divider -->
    <g transform="translate(0, 86)">
      <line x1="-180" y1="0" x2="-20" y2="0" stroke="#D9531E" stroke-width="1.8" stroke-opacity="0.6"/>
      <polygon points="0,-6 6,0 0,6 -6,0" fill="#7A1919" />
      <circle cx="-10" cy="0" r="3" fill="#D9531E" />
      <circle cx="10" cy="0" r="3" fill="#D9531E" />
      <line x1="20" y1="0" x2="180" y2="0" stroke="#D9531E" stroke-width="1.8" stroke-opacity="0.6"/>
    </g>

    <!-- Location & Tiffin Tagline -->
    <text y="125" class="full-sub">KARADICHITTUR</text>
    <text y="152" class="full-tag">— NIGHT TIFFIN —</text>
  </g>
</svg>'''

with open(os.path.join(PUBLIC_LOGO_DIR, 'logo.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_full)

print("Creating High-Res Raster PNGs with Pillow...")
# 6. Render High-Res PNGs using Pillow
# High-res Full Vertical Logo (1024x1200, transparent PNG)
canvas_w, canvas_h = 1024, 1220
logo_png = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))

# Place 640x640 emblem centered at top
emblem_large = cropped.resize((640, 640), Image.Resampling.LANCZOS)
logo_png.paste(emblem_large, (int((canvas_w - 640) / 2), 60), emblem_large)

# Text on PNG
draw = ImageDraw.Draw(logo_png)

# Load fonts
font_en_big = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 76)
font_ta_big = ImageFont.truetype(r'C:\Windows\Fonts\Nirmala.ttc', 60)
font_sub = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 26)

# Text: V.K HOTEL
text_vk = "V.K "
text_hotel = "HOTEL"
w_vk = draw.textlength(text_vk, font=font_en_big)
w_hotel = draw.textlength(text_hotel, font=font_en_big)
w_total_en = w_vk + w_hotel
start_x = (canvas_w - w_total_en) / 2
y_en = 740

draw.text((start_x, y_en), text_vk, fill=(122, 25, 25, 255), font=font_en_big)
draw.text((start_x + w_vk, y_en), text_hotel, fill=(44, 24, 16, 255), font=font_en_big)

# Tamil Text: வி.கே ஹோட்டல் (decomposed kombu+ha+kaal for perfect raster rendering in Pillow)
text_ta = "\u0bb5\u0bbf.\u0b95\u0bc7 \u0bc7\u0bb9\u0bbe\u0b9f\u0bcd\u0b9f\u0bb2\u0bcd"
w_ta = draw.textlength(text_ta, font=font_ta_big)
start_ta = (canvas_w - w_ta) / 2
y_ta = 840
draw.text((start_ta, y_ta), text_ta, fill=(122, 25, 25, 255), font=font_ta_big)

# Decorative Divider
divider_y = 935
cx_div = canvas_w / 2
draw.line([(cx_div - 260, divider_y), (cx_div - 30, divider_y)], fill=(217, 83, 30, 200), width=3)
draw.line([(cx_div + 30, divider_y), (cx_div + 260, divider_y)], fill=(217, 83, 30, 200), width=3)
draw.polygon([(cx_div, divider_y - 8), (cx_div + 8, divider_y), (cx_div, divider_y + 8), (cx_div - 8, divider_y)], fill=(122, 25, 25, 255))
draw.ellipse([(cx_div - 18, divider_y - 4), (cx_div - 10, divider_y + 4)], fill=(217, 83, 30, 255))
draw.ellipse([(cx_div + 10, divider_y - 4), (cx_div + 18, divider_y + 4)], fill=(217, 83, 30, 255))

# Subtitle: KARADICHITTUR • NIGHT TIFFIN
text_sub = "KARADICHITTUR  •  NIGHT TIFFIN"
w_sub = draw.textlength(text_sub, font=font_sub)
start_sub = (canvas_w - w_sub) / 2
y_sub = 970
draw.text((start_sub, y_sub), text_sub, fill=(217, 83, 30, 255), font=font_sub)

logo_png.save(os.path.join(PUBLIC_LOGO_DIR, 'logo.png'), 'PNG', optimize=True)

# 7. Create logo-badge-dark.png (Full vertical badge on rich dark background)
logo_badge_dark = Image.new('RGBA', (canvas_w, canvas_h), (28, 16, 12, 255))
logo_badge_dark.paste(emblem_large, (int((canvas_w - 640) / 2), 60), emblem_large)
draw_dark = ImageDraw.Draw(logo_badge_dark)

draw_dark.text((start_x, y_en), text_vk, fill=(255, 255, 255, 255), font=font_en_big)
draw_dark.text((start_x + w_vk, y_en), text_hotel, fill=(250, 246, 238, 255), font=font_en_big)
draw_dark.text((start_ta, y_ta), text_ta, fill=(245, 235, 225, 255), font=font_ta_big)

draw_dark.line([(cx_div - 260, divider_y), (cx_div - 30, divider_y)], fill=(240, 154, 56, 180), width=3)
draw_dark.line([(cx_div + 30, divider_y), (cx_div + 260, divider_y)], fill=(240, 154, 56, 180), width=3)
draw_dark.polygon([(cx_div, divider_y - 8), (cx_div + 8, divider_y), (cx_div, divider_y + 8), (cx_div - 8, divider_y)], fill=(240, 154, 56, 255))
draw_dark.ellipse([(cx_div - 18, divider_y - 4), (cx_div - 10, divider_y + 4)], fill=(240, 154, 56, 255))
draw_dark.ellipse([(cx_div + 10, divider_y - 4), (cx_div + 18, divider_y + 4)], fill=(240, 154, 56, 255))

draw_dark.text((start_sub, y_sub), text_sub, fill=(240, 154, 56, 255), font=font_sub)

logo_badge_dark.save(os.path.join(PUBLIC_LOGO_DIR, 'logo-badge-dark.png'), 'PNG', optimize=True)

# 8. Create High-Res Horizontal PNG: logo-horizontal.png (1240x240, matching 620:120)
h_w, h_h = 1240, 240
h_png = Image.new('RGBA', (h_w, h_h), (0, 0, 0, 0))
emblem_h = cropped.resize((200, 200), Image.Resampling.LANCZOS)
h_png.paste(emblem_h, (24, 20), emblem_h)

draw_h = ImageDraw.Draw(h_png)
font_h_en = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 58)
font_h_ta = ImageFont.truetype(r'C:\Windows\Fonts\Nirmala.ttc', 46)
font_h_sub = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 22)

x_text = 252
draw_h.text((x_text, 44), "V.K ", fill=(122, 25, 25, 255), font=font_h_en)
x_text += int(draw_h.textlength("V.K ", font=font_h_en))
draw_h.text((x_text, 44), "HOTEL", fill=(44, 24, 16, 255), font=font_h_en)
x_text += int(draw_h.textlength("HOTEL", font=font_h_en)) + 14
draw_h.text((x_text, 48), "|", fill=(217, 83, 30, 200), font=font_h_en)
x_text += int(draw_h.textlength("|", font=font_h_en)) + 16
draw_h.text((x_text, 52), text_ta, fill=(122, 25, 25, 255), font=font_h_ta)

# Subtitle on horizontal logo
draw_h.line([(254, 148), (284, 148)], fill=(217, 83, 30, 180), width=2)
draw_h.ellipse([(290, 146), (294, 150)], fill=(217, 83, 30, 255))
draw_h.text((308, 136), "KARADICHITTUR  •  NIGHT TIFFIN", fill=(217, 83, 30, 255), font=font_h_sub)
w_h_sub = draw_h.textlength("KARADICHITTUR  •  NIGHT TIFFIN", font=font_h_sub)
end_sub_x = 308 + int(w_h_sub) + 14
draw_h.ellipse([(end_sub_x, 146), (end_sub_x + 4, 150)], fill=(217, 83, 30, 255))
draw_h.line([(end_sub_x + 10, 148), (end_sub_x + 40, 148)], fill=(217, 83, 30, 180), width=2)

h_png.save(os.path.join(PUBLIC_LOGO_DIR, 'logo-horizontal.png'), 'PNG', optimize=True)

# 8b. Create Dark Horizontal PNG: logo-dark.png (1240x240, on rich dark charcoal background with warm tones)
h_dark_png = Image.new('RGBA', (h_w, h_h), (28, 16, 12, 255))
h_dark_png.paste(emblem_h, (24, 20), emblem_h)
draw_hd = ImageDraw.Draw(h_dark_png)

x_text_d = 252
draw_hd.text((x_text_d, 44), "V.K ", fill=(255, 255, 255, 255), font=font_h_en)
x_text_d += int(draw_hd.textlength("V.K ", font=font_h_en))
draw_hd.text((x_text_d, 44), "HOTEL", fill=(250, 246, 238, 255), font=font_h_en)
x_text_d += int(draw_hd.textlength("HOTEL", font=font_h_en)) + 14
draw_hd.text((x_text_d, 48), "|", fill=(230, 101, 43, 220), font=font_h_en)
x_text_d += int(draw_hd.textlength("|", font=font_h_en)) + 16
draw_hd.text((x_text_d, 52), text_ta, fill=(245, 235, 225, 255), font=font_h_ta)

draw_hd.line([(254, 148), (284, 148)], fill=(240, 154, 56, 180), width=2)
draw_hd.ellipse([(290, 146), (294, 150)], fill=(240, 154, 56, 255))
draw_hd.text((308, 136), "KARADICHITTUR  •  NIGHT TIFFIN", fill=(240, 154, 56, 255), font=font_h_sub)
draw_hd.ellipse([(end_sub_x, 146), (end_sub_x + 4, 150)], fill=(240, 154, 56, 255))
draw_hd.line([(end_sub_x + 10, 148), (end_sub_x + 40, 148)], fill=(240, 154, 56, 180), width=2)

h_dark_png.save(os.path.join(PUBLIC_LOGO_DIR, 'logo-dark.png'), 'PNG', optimize=True)

print("Creating Favicon assets...")
# 9. Create Favicon (SVG and Multi-Resolution ICO)
# Favicon SVG: Crisp icon with chef hat, stylized VK, and tawa
svg_favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="100%" height="100%">
  <defs>
    <linearGradient id="favBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#8B1D1D"/>
      <stop offset="100%" stop-color="#5C1010"/>
    </linearGradient>
    <linearGradient id="hatGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFA000"/>
      <stop offset="100%" stop-color="#D9531E"/>
    </linearGradient>
  </defs>

  <!-- Rounded Tile -->
  <rect width="128" height="128" rx="28" fill="url(#favBg)"/>
  <rect x="3" y="3" width="122" height="122" rx="25" fill="none" stroke="#D4AF37" stroke-width="3" stroke-opacity="0.8"/>

  <!-- Chef Hat / Toque Icon at top -->
  <g transform="translate(64, 34)">
    <path d="M -24 6 C -28 -6 -16 -18 -8 -12 C -2 -22 16 -22 22 -12 C 30 -18 38 -6 34 6 Z" fill="url(#hatGrad)"/>
    <rect x="-24" y="6" width="58" height="8" rx="3" fill="#FFF"/>
  </g>

  <!-- Bold VK Letters in White / Cream -->
  <g transform="translate(64, 82)">
    <text font-family="'Plus Jakarta Sans', Arial, sans-serif" font-size="44" font-weight="900" text-anchor="middle" fill="#FFFFFF" letter-spacing="1">
      VK
    </text>
    <!-- Leaf Sprig on V -->
    <path d="M -30 -32 C -26 -38 -18 -38 -14 -34 C -18 -30 -24 -29 -30 -32 Z" fill="#4CAF50" />
  </g>

  <!-- Hot Tawa Underline Curve with Sizzle Dots -->
  <path d="M 28 102 Q 64 116 100 102" fill="none" stroke="#F09A38" stroke-width="4.5" stroke-linecap="round"/>
</svg>'''

with open(os.path.join(PUBLIC_LOGO_DIR, 'favicon.svg'), 'w', encoding='utf-8') as f:
    f.write(svg_favicon)

# Generate multi-size .ICO from Pillow
# Render high-contrast 256x256 favicon image
fav_base = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
fav_draw = ImageDraw.Draw(fav_base)

# Rounded rectangle background
fav_draw.rounded_rectangle([(8, 8), (248, 248)], radius=54, fill=(122, 25, 25, 255), outline=(212, 175, 55, 230), width=7)

# Chef hat
hat_y = 66
fav_draw.ellipse([(70, hat_y - 36), (110, hat_y + 10)], fill=(217, 83, 30, 255))
fav_draw.ellipse([(100, hat_y - 48), (156, hat_y + 10)], fill=(230, 101, 43, 255))
fav_draw.ellipse([(146, hat_y - 36), (186, hat_y + 10)], fill=(217, 83, 30, 255))
fav_draw.rounded_rectangle([(70, hat_y + 8), (186, hat_y + 24)], radius=6, fill=(255, 255, 255, 255))

# VK Text
font_fav = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 96)
fav_draw.text((128, 158), "VK", fill=(255, 255, 255, 255), font=font_fav, anchor="mm")

# Leaf sprig on V
fav_draw.polygon([(68, 98), (84, 88), (76, 104)], fill=(76, 175, 80, 255))

# Tawa curve
fav_draw.arc([(50, 176), (206, 226)], start=20, end=160, fill=(240, 154, 56, 255), width=9)

# Save ICO containing 16x16, 32x32, 48x48, 64x64, 128x128
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]
ico_images = [fav_base.resize(sz, Image.Resampling.LANCZOS) for sz in ico_sizes]

# Save to public/favicon.ico and public/logo/favicon.ico
fav_base.save(os.path.join(PUBLIC_DIR, 'favicon.ico'), format='ICO', sizes=ico_sizes)
fav_base.save(os.path.join(PUBLIC_LOGO_DIR, 'favicon.ico'), format='ICO', sizes=ico_sizes)

# Save favicon.png
fav_base.resize((192, 192), Image.Resampling.LANCZOS).save(os.path.join(PUBLIC_LOGO_DIR, 'favicon.png'), 'PNG')
fav_base.resize((192, 192), Image.Resampling.LANCZOS).save(os.path.join(PUBLIC_DIR, 'favicon.png'), 'PNG')

print("Copying all generated assets to src/assets/logo/...")
# Copy all files from public/logo to src/assets/logo
import shutil
for f in os.listdir(PUBLIC_LOGO_DIR):
    shutil.copy2(os.path.join(PUBLIC_LOGO_DIR, f), os.path.join(SRC_LOGO_DIR, f))

print("Asset build complete! Assets created in:")
print(" -", PUBLIC_LOGO_DIR)
print(" -", SRC_LOGO_DIR)
for f in os.listdir(PUBLIC_LOGO_DIR):
    size_kb = os.path.getsize(os.path.join(PUBLIC_LOGO_DIR, f)) / 1024
    print(f"    * {f} ({size_kb:.1f} KB)")
