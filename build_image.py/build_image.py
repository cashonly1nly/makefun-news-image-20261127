#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261127.
One 1024x1024 infographic summarising world news of Fri 27 Nov 2026.
News verified 27 Nov 2026 (CST) against: Reuters, Al Jazeera, BBC,
The Korea Times, The Telegraph, CNN, The Hindu, Associated Press.
Run: python3 build_image.py  -> writes entry.png (1024x1024, <1 MiB).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (246, 241, 231)      # cream paper
INK = (16, 35, 63)        # navy
RED = (178, 34, 34)
GOLD = (176, 141, 87)
GREY = (74, 74, 74)
CARD = (255, 255, 255)
NAVY = (16, 35, 63)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

STORIES = [
    ("MIDDLE EAST", (178, 34, 34),
     "Houthis hit Saudi refinery; tankers struck in Hormuz",
     "Houthi attacks hit Ras Tanura and Red Sea ports; two tankers "
     "hit mines in the strait. Oil prices jump."),
    ("ASIA", (31, 111, 183),
     "Kim vows to expand North Korea's nuclear arsenal",
     "Kim inspects nuclear sites and orders wider deployment of "
     "tactical nuclear weapons. An \u201cirreversible reality\u201d."),
    ("EUROPE", (90, 60, 140),
     "Britain contacts 100,000 reservists",
     "First such call-up since the Cold War, as the Russia threat "
     "grows. Veterans are asked to update details and skills."),
    ("DISASTER", (176, 120, 20),
     "Diesel tanker capsizes off Ibiza, one dies",
     "The Med Emre, carrying up to 7,000 tonnes of diesel, keels "
     "over off Spain. All 17 crew are rescued; no spill so far."),
    ("MIDDLE EAST", (0, 128, 96),
     "Hamas weighs response after Israel kills 10 in Gaza",
     "A third night of strikes kills a Hamas deputy minister and "
     "his wife. Netanyahu vows more targeted killings."),
    ("AMERICAS", (200, 80, 20),
     "Macy's parade postponed by storm",
     "A nor'easter forces the first weather postponement in the "
     "parade's 100-year history. It moves to Saturday."),
]

FOOTER = ("ALSO ON 27 NOVEMBER:  EU leaders deadlocked on budget and "
          "$49bn Ukraine loan  \u2022  Depardieu to stand trial on rape "
          "charge  \u2022  Duterte ICC trial set for Monday")

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# --- masthead ---
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((36, 22), "THE WORLD IN ONE DAY", font=font(BOLD, 52), fill=(255, 255, 255))
d.text((36, 92), "FRIDAY  \u00b7  27 NOVEMBER 2026", font=font(BOLD, 30), fill=(232, 197, 120))
d.rectangle([0, 148, W, 154], fill=RED)
d.text((36, 168), "Six stories that defined the day \u2014 war at sea, nuclear build-up, and a storm",
       font=font(REG, 22), fill=GREY)

# --- story grid: 2 cols x 3 rows ---
x0, y0 = 28, 212
cw, ch, gx, gy = 474, 208, 20, 16
for i, (tag, colour, head, body) in enumerate(STORIES):
    x = x0 + (i % 2) * (cw + gx)
    y = y0 + (i // 2) * (ch + gy)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=10, fill=CARD,
                        outline=(210, 200, 180), width=1)
    d.rectangle([x, y + 10, x + 9, y + ch - 10], fill=colour)
    d.text((x + 26, y + 16), tag, font=font(BOLD, 18), fill=colour)
    hl = wrap(d, head, font(BOLD, 27), cw - 52)
    yy = y + 46
    for ln in hl[:2]:
        d.text((x + 26, yy), ln, font=font(BOLD, 27), fill=INK)
        yy += 33
    bl = wrap(d, body, font(REG, 20), cw - 52)
    for ln in bl[:3]:
        d.text((x + 26, yy), ln, font=font(REG, 20), fill=(40, 40, 40))
        yy += 27

# --- footer ---
fy = y0 + 3 * ch + 2 * gy + 18  # 886
d.rectangle([0, fy, W, fy + 96], fill=NAVY)
d.text((36, fy + 12), "ALSO ON 27 NOVEMBER", font=font(BOLD, 19), fill=(232, 197, 120))
fl = wrap(d, FOOTER[len("ALSO ON 27 NOVEMBER:  "):], font(REG, 19), W - 72)
yy = fy + 40
for ln in fl[:2]:
    d.text((36, yy), ln, font=font(REG, 19), fill=(255, 255, 255))
    yy += 25
d.text((36, H - 26), "Sources: Reuters, Al Jazeera, BBC, The Korea Times, "
       "The Telegraph, CNN \u2014 27 Nov 2026",
       font=font(REG, 13), fill=(120, 110, 95))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
