#!/usr/bin/env python3
"""
THE WORLD TODAY — Tuesday, 24 November 2026
Entry program for make.fun bounty news-image-20261124.

Writes one deterministic 1024x1024 PNG to /output/entry.png
(or ./output/entry.png when /output is not writable).
No network, no randomness, no time-dependent values.
All stories verified for 24 November 2026 only.
"""
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (253, 252, 248)
INK = (17, 17, 17)
GREY = (85, 85, 85)
RED = (185, 28, 28)
LIGHT = (221, 221, 221)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def draw_wrapped(draw, text, font_obj, x, y, max_w, line_h):
    # Wrap by measuring width with Pillow, deterministic.
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font_obj) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    for line in lines:
        draw.text((x, y), line, fill=INK, font=font_obj)
        y += line_h
    return y

def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Top bar
    f_small = font(SANS, 9)
    d.text((28, 28), "VOL. 1 — NO. 328", fill=GREY, font=f_small)
    d.text((700, 28), "9 STORIES  •  24 NOV 2026", fill=GREY, font=f_small)
    d.line([(28, 46), (996, 46)], fill=INK, width=2)

    # Masthead
    f_mast = font(SERIF_B, 58)
    d.text((28, 54), "THE WORLD TODAY", fill=INK, font=f_mast)
    f_date = font(SANS, 12)
    d.text((28, 122), "TUESDAY, 24 NOVEMBER 2026  —  IN DEPTH", fill=INK, font=f_date)
    d.line([(28, 144), (996, 144)], fill=INK, width=2)
    d.line([(28, 148), (996, 148)], fill=INK, width=1)

    # Lead
    f_kick = font(SANS_B, 10)
    d.text((28, 158), "LEAD  —  CLIMATE  •  ANTALYA", fill=RED, font=f_kick)
    f_lead_h = font(SERIF_B, 30)
    y = draw_wrapped(d, "COP31 ends with no deal on its main text", f_lead_h, 28, 176, 620, 34)
    f_body = font(SERIF, 12)
    y = draw_wrapped(d, "The UN climate summit ended on Sunday, almost two days late, without agreement on its main text — the longest COP in history. The EU, the UK and vulnerable nations rejected the Antalya pact.", f_body, 28, y + 4, 620, 16)
    y = draw_wrapped(d, "Why it matters: for the first time since 2009, a UN climate summit ended without a consensus deal.", f_body, 28, y + 4, 620, 16)
    d.text((28, y + 4), "REPORTED  •  Carbon Brief, 24 Nov 2026; WRI, 24 Nov 2026", fill=GREY, font=font(SANS, 9))

    # Numbers strip (right of lead)
    d.rectangle([680, 158, 996, 300], outline=INK, width=1)
    d.text((694, 166), "THE DAY IN NUMBERS", fill=INK, font=font(SANS_B, 10))
    nums = [("3", "tankers"), ("14", "nations"), ("+31%", "Nvidia"), ("5.6", "Nepal quake"), ("7", "sea drones"), ("96", "drones at UA")]
    yy = 190
    for i in range(0, 6, 3):
        for j in range(3):
            n, lab = nums[i + j]
            x = 694 + j * 102
            d.text((x, yy), n, fill=INK, font=font(SERIF_B, 20))
            d.text((x, yy + 24), lab, fill=GREY, font=font(SANS, 8))
        yy += 52

    # Stories grid — 2 columns x 4 rows
    stories = [
        ("2 — HORMUZ  [CLAIM]", "Three tankers claimed hit by mines in Hormuz", "IRGC Navy said three tankers struck mines and caught fire. No names or casualties given. US CENTCOM had not responded. Unverified claim."),
        ("3 — POLAND  [CONFIRMED]", "Russian drone briefly enters Poland", "Drone flew about 20 km to Chelm in about nine minutes. Poland was authorised to shoot it down but held fire to avoid civilian risk."),
        ("4 — LIBYA  [CONFIRMED]", "Ukraine defends Libya ship strike", "Seven sea drones sank corvette Merkury in Benghazi and hit MV Angara. Ukraine said it was self-defence under Article 51."),
        ("5 — NVIDIA  [REPORTED]", "Nvidia brings back Jensen Huang", "Board reinstated Huang as CEO, effective immediately. Shares +31% to $164.79; Nasdaq +6.5%, best day in 19 months."),
        ("6 — MYANMAR  [CONFIRMED]", "Fourteen nations back Myanmar ruling", "UK and 13 others acknowledged the ICJ ruling that Myanmar committed genocide against the Rohingya. UK sanctioned five generals."),
        ("7 — GROK  [CONFIRMED]", "Two US states sue over Grok images", "Virginia and Oregon sued SpaceX on Monday, alleging Grok let users create non-consensual sexual images, including of children."),
        ("8 — NEPAL  [CONFIRMED]", "5.6 quake shakes eastern Nepal", "Magnitude 5.6 at 7:17 a.m. local near Olangchung Gola, Taplejung. Felt in Kathmandu. No casualties or major damage reported."),
        ("9 — ESTONIA  [REPORTED]", "Russia warns Estonia; satellite denied", "Russia warned Estonia its actions risk open war after border closure from 1 Dec. Kremlin denied a nuclear-armed satellite plan."),
    ]
    f_story_k = font(SANS_B, 9)
    f_story_h = font(SERIF_B, 13)
    f_story_b = font(SERIF, 10)
    y0 = 350
    row_h = 115
    for idx, (kick, head, body) in enumerate(stories):
        col = idx % 2
        row = idx // 2
        x = 28 + col * 492
        y = y0 + row * row_h
        d.line([(x, y), (x + 470, y)], fill=LIGHT, width=1)
        d.text((x, y + 6), kick, fill=RED, font=f_story_k)
        y2 = draw_wrapped(d, head, f_story_h, x, y + 22, 470, 16)
        draw_wrapped(d, body, f_story_b, x, y2 + 2, 470, 13)

    # Map strip
    y_map = y0 + 4 * row_h + 8
    d.rectangle([28, y_map, 996, y_map + 78], outline=INK, width=1)
    d.text((38, y_map + 8), "WHERE IT HAPPENED  —  1 ANTALYA  •  2 HORMUZ  •  3 POLAND  •  4 BENGHAZI  •  5 USA  •  6 MYANMAR  •  7 VIRGINIA/OREGON  •  8 TAPLEJUNG  •  9 ESTONIA", fill=INK, font=font(SANS_B, 9))
    d.text((38, y_map + 30), "LEFT OUT — NOT 24 NOV:  US measles elimination status was announced 17 Nov, not 24 Nov.  ICJ ruling itself was 19 Nov.", fill=INK, font=font(SERIF, 11))
    d.text((38, y_map + 52), "Sources: Reuters, AP, Carbon Brief, WRI, AFP, CNN, WSJ, IRNA, Nepal National Earthquake Centre, Xinhua. Tags: CONFIRMED = stated by authority; REPORTED = reported 24 Nov; CLAIM = unverified.", fill=GREY, font=font(SANS, 8))

    # Footer
    d.line([(28, 990), (996, 990)], fill=INK, width=2)
    d.text((28, 996), "THE WORLD TODAY  •  24 NOVEMBER 2026  •  DETERMINISTIC  •  NO NETWORK", fill=GREY, font=font(SANS, 8))

    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    img.save(out_path, format="PNG", optimize=True)
    # Also save a local copy next to the script for inspection.
    img.save("entry.png", format="PNG", optimize=True)
    os.makedirs("output", exist_ok=True)
    img.save(os.path.join("output", "entry.png"), format="PNG", optimize=True)
    print(f"Wrote {out_path} {W}x{H}")

if __name__ == "__main__":
    main()
