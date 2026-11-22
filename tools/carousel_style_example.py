from PIL import Image, ImageDraw, ImageFont
import os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350
NAVY, GREEN, WHITE, YELLOW, SOFT = "#0F2A44", "#1FB57A", "#FFFFFF", "#FFD166", "#C9D6E3"
F = "/usr/share/fonts/opentype/inter/"
def font(w, s): return ImageFont.truetype(F + f"Inter-{w}.otf", s)

def wrap(d, text, f, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = word
    lines.append(cur); return lines

def para(d, xy, text, f, fill, maxw, gap=1.25):
    x, y = xy
    for ln in wrap(d, text, f, maxw):
        d.text((x, y), ln, font=f, fill=fill); y += int(f.size * gap)
    return y

def base(n, total):
    im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
    # brand mark
    d.ellipse((80, 80, 150, 150), fill=GREEN)
    d.text((115, 113), "£", font=font("Bold", 48), fill=NAVY, anchor="mm")
    d.text((170, 98), "SMART MONEY UK", font=font("Bold", 30), fill=WHITE)
    d.text((W - 80, 98), f"{n}/{total}", font=font("Medium", 28), fill=SOFT, anchor="ra")
    d.text((80, H - 110), "@smartmoneyuk_", font=font("SemiBold", 30), fill=GREEN)
    if n < total:
        d.text((W - 80, H - 110), "Swipe  →", font=font("SemiBold", 30), fill=WHITE, anchor="ra")
    return im, d

T = 5; M = 80; MW = W - 2 * M

# 1 cover
im, d = base(1, T)
y = 330
d.text((M, y), "Hey UK!", font=font("Bold", 58), fill=YELLOW); y += 110
y = para(d, (M, y), "Welcome to Smart Money UK", font("Bold", 104), WHITE, MW, 1.08)
y += 50
para(d, (M, y), "Free stuff, saving hacks and ways to earn more. For everyone living in the UK.", font("Medium", 44), SOFT, MW)
im.save(f"{OUT}/slide1.jpg", quality=92)

# 2 what you'll find
im, d = base(2, T)
y = 260
y = para(d, (M, y), "What you'll find here", font("Bold", 80), WHITE, MW, 1.1) + 60
for title, sub in [("Freebies you're missing", "Things you can get or do for free"),
                   ("Bills and savings hacks", "Simple ways to spend less every month"),
                   ("Ways to earn more", "CV, interview and pay rise tips"),
                   ("Easy UK money guides", "Everything in one place, step by step")]:
    d.rounded_rectangle((M, y, W - M, y + 170), radius=28, fill="#16385A")
    d.ellipse((M + 36, y + 55, M + 96, y + 115), fill=GREEN)
    d.text((M + 66, y + 85), "✓", font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36), fill=NAVY, anchor="mm")
    d.text((M + 130, y + 38), title, font=font("Bold", 46), fill=WHITE)
    d.text((M + 130, y + 100), sub, font=font("Medium", 32), fill=SOFT)
    y += 200
im.save(f"{OUT}/slide2.jpg", quality=92)

# 3 why me
im, d = base(3, T)
y = 300
y = para(d, (M, y), "How this page works", font("Bold", 84), WHITE, MW, 1.1) + 60
y = para(d, (M, y), "Short, simple tips you can use today.", font("Bold", 52), YELLOW, MW) + 30
y = para(d, (M, y), "Facts are checked against official UK sources like gov.uk and the NHS before they go up.", font("Medium", 44), SOFT, MW) + 40
para(d, (M, y), "No jargon. No get-rich-quick. Just practical money wins.", font("SemiBold", 44), WHITE, MW)
im.save(f"{OUT}/slide3.jpg", quality=92)

# 4 this week
im, d = base(4, T)
y = 260
y = para(d, (M, y), "Coming up next", font("Bold", 80), WHITE, MW, 1.1) + 60
for day, what in [("1", "5 free things most people never use"),
                  ("2", "Don't get fooled this Black Friday"),
                  ("3", "3 CV mistakes recruiters reject"),
                  ("4", "Christmas on a budget")]:
    d.rounded_rectangle((M, y, M + 110, y + 110), radius=22, fill=GREEN)
    d.text((M + 55, y + 55), day, font=font("Bold", 40), fill=NAVY, anchor="mm")
    para(d, (M + 150, y + 30), what, font("SemiBold", 42), WHITE, MW - 150, 1.15)
    y += 160
im.save(f"{OUT}/slide4.jpg", quality=92)

# 5 CTA
im, d = base(5, T)
y = 360
y = para(d, (M, y), "Let's make your money go further.", font("Bold", 88), WHITE, MW, 1.1) + 70
for ln in ["Follow @smartmoneyuk_", "Turn on post notifications", "Comment: what should I cover first?"]:
    d.ellipse((M, y + 14, M + 26, y + 40), fill=GREEN)
    d.text((M + 50, y), ln, font=font("SemiBold", 46), fill=WHITE); y += 90
im.save(f"{OUT}/slide5.jpg", quality=92)
print("ok")
