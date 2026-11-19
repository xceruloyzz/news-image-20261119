#!/usr/bin/env python3
"""Render the 19 November 2026 front page as a 1024x1024 PNG.

Every word on the page is fixed text chosen for Thursday 19 November 2026
and drawn with PIL from the DejaVu fonts on this machine. The script takes
no input, reads no clock, rolls no dice and makes no network calls, so
running it twice produces the same bytes twice. The picture lands in the
repository root as entry.png.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
MARGIN = 28
EDGE = PAGE - MARGIN

PALETTE = {
    "ink": (18, 18, 18),
    "body": (42, 42, 42),
    "paper": (250, 248, 242),
    "red": (178, 24, 24),
    "rule": (190, 185, 175),
    "white": (255, 255, 255),
}

FONT_FILES = {
    "bold": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "regular": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "serif": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
}


def font(name, size):
    return ImageFont.truetype(FONT_FILES[name], size)


def shrink_to_fit(draw, text, name, size, width):
    """Largest size at or below `size` that fits `text` in `width`."""
    while size > 10:
        candidate = font(name, size)
        if draw.textlength(text, font=candidate) <= width:
            return candidate
        size -= 2
    return font(name, 10)


def wrap_text(draw, text, face, width):
    """Split `text` into lines no wider than `width` in `face`."""
    lines, current = [], ""
    for word in text.split():
        attempt = f"{current} {word}".strip()
        if draw.textlength(attempt, font=face) <= width:
            current = attempt
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_centered(draw, y, text, face, colour):
    x = (PAGE - draw.textlength(text, font=face)) / 2
    draw.text((x, y), text, font=face, fill=colour)


LEAD = {
    "kicker": "GAMING  •  AFTER 13 YEARS",
    "lines": ["GTA VI IS OUT", "VICE CITY OPENS"],
    "standfirst": (
        "Rolling midnight launch starts in New Zealand; PS5 and Xbox. "
        "Preorders near 16m, over $1.5bn, and reviews score 99."
    ),
}

GRID = [
    {
        "kicker": "US POLITICS",
        "head": "Jeffries nominated for Speaker",
        "body": (
            "Democrats pick Jeffries 251-11; if elected Jan 3 he would be "
            "the first Black Speaker of the House."
        ),
    },
    {
        "kicker": "GULF ESCALATION",
        "head": "Iran widens attacks to Kuwait",
        "body": (
            "Tehran hits a US air base in Kuwait and Bahrain again; a Houthi "
            "missile aimed at Riyadh is destroyed."
        ),
    },
    {
        "kicker": "DIPLOMACY • SHENZHEN",
        "head": "Trump, Xi, Putin meet today",
        "body": (
            "First trilateral of the three leaders at APEC: nuclear arms, "
            "Ukraine and Iran on the agenda for one hour."
        ),
    },
    {
        "kicker": "UKRAINE AID • EU",
        "head": "EU proposes €45bn Ukraine loan",
        "body": (
            "Kyiv repays only after Russia pays reparations; the loan fills "
            "two-thirds of a €70bn gap for 2027."
        ),
    },
    {
        "kicker": "WEATHER • INDIA",
        "head": "Cyclone Akvan nears the coast",
        "body": (
            "Severe storm to cross Machilipatnam-Puri by noon Fri, 90-100 "
            "km/h; red alert as heavy rain lashes the coast."
        ),
    },
    {
        "kicker": "SPACE • NASA",
        "head": "Voyager 1 one light-day away",
        "body": (
            "First human-made object a light-day out, 16bn miles; NASA "
            "briefs the milestone today at noon EST."
        ),
    },
]

TICKER_ITEMS = [
    "Modi meets the Prince and Princess of Wales",
    "Australia sanctions Israeli settlers",
    "Peltola wins Alaska Senate seat",
    "Pew: Islam largest faith by 2035",
    "Duckett 133 as England beat Australia",
]


def draw_story(draw, x, y, width, item):
    """Draw one grid story; return the y just below it."""
    draw.text((x, y), item["kicker"], font=font("bold", 17), fill=PALETTE["red"])
    y += 23
    headline = font("bold", 25)
    head_lines = wrap_text(draw, item["head"], headline, width)
    assert len(head_lines) <= 2, f"head too long: {item['head']}"
    for line in head_lines:
        draw.text((x, y), line, font=headline, fill=PALETTE["ink"])
        y += 30
    y += 1
    body_face = font("regular", 18)
    body_lines = wrap_text(draw, item["body"], body_face, width)
    assert len(body_lines) <= 3, f"body too long: {item['body']}"
    for line in body_lines:
        draw.text((x, y), line, font=body_face, fill=PALETTE["body"])
        y += 23
    return y


def build_page():
    img = Image.new("RGB", (PAGE, PAGE), PALETTE["paper"])
    draw = ImageDraw.Draw(img)

    # Masthead: red rule, nameplate, black date bar.
    draw.rectangle([0, 0, PAGE, 9], fill=PALETTE["red"])
    nameplate = shrink_to_fit(draw, "THE WORLD TODAY", "serif", 80, 950)
    draw_centered(draw, 12, "THE WORLD TODAY", nameplate, PALETTE["ink"])
    draw.rectangle([MARGIN, 100, EDGE, 146], fill=PALETTE["ink"])
    date_face = font("bold", 32)
    draw_centered(draw, 108, "THURSDAY  19  NOVEMBER  2026", date_face, PALETTE["white"])

    # Lead story: kicker, two-line splash headline, standfirst.
    draw_centered(draw, 158, LEAD["kicker"], font("bold", 23), PALETTE["red"])
    y = 190
    splash = font("bold", 57)
    for line in LEAD["lines"]:
        draw_centered(draw, y, line, splash, PALETTE["ink"])
        y += 66
    standfirst = font("regular", 23)
    for line in wrap_text(draw, LEAD["standfirst"], standfirst, 930):
        draw_centered(draw, y + 2, line, standfirst, PALETTE["body"])
        y += 30
    y += 8
    draw.line([MARGIN, y, EDGE, y], fill=PALETTE["ink"], width=4)
    y += 14

    # Secondary stories: two columns, three rows, ruled between rows.
    column = 462
    left_x, right_x = 32, 530
    for index in range(0, len(GRID), 2):
        left_end = draw_story(draw, left_x, y, column, GRID[index])
        right_end = draw_story(draw, right_x, y, column, GRID[index + 1])
        y = max(left_end, right_end) + 7
        draw.line([MARGIN, y - 5, EDGE, y - 5], fill=PALETTE["rule"], width=2)
    assert y <= PAGE - 124, f"grid overflow: y={y}"

    # Ticker strip along the foot of the page.
    draw.rectangle([0, PAGE - 118, PAGE, PAGE], fill=PALETTE["ink"])
    ticker = "ALSO TODAY  ▸  " + "  ▸  ".join(TICKER_ITEMS)
    ty = PAGE - 100
    for line in wrap_text(draw, ticker, font("bold", 23), 950):
        draw_centered(draw, ty, line, font("bold", 23), PALETTE["white"])
        ty += 33
    return img


def main():
    out = Path(__file__).resolve().parent.parent / "entry.png"
    build_page().save(out, format="PNG", optimize=False)
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
