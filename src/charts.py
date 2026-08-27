"""Minimal SVG chart writers.

Hand-rolled rather than matplotlib so the whole pipeline stays dependency-free
and the Actions run needs no install step. Colours come from CSS variables with
literal fallbacks so the charts stay readable on GitHub in light and dark mode.
"""
from html import escape

FG = "#c9d1d9"
MUTED = "#8b949e"
BARS = ["#58a6ff", "#3fb950", "#d29922", "#bc8cff", "#f778ba", "#39c5cf", "#ff7b72"]

CAT_COLOR = {
    "llm": "#bc8cff", "mlcore": "#58a6ff", "framework": "#3fb950",
    "language": "#d29922", "infra": "#f778ba", "data": "#39c5cf",
    "practice": "#ff7b72",
}


def _header(w, h):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" font-family="-apple-system,BlinkMacSystemFont,'
        f'Segoe UI,Helvetica,Arial,sans-serif">'
    )


def bar_chart(items, title, width=760, row_h=26, label_w=190, value_fmt="{:,}",
              colors=None):
    """Horizontal bars. `items` is [(label, value), ...] already sorted."""
    if not items:
        return _header(width, 40) + "</svg>"
    h = 52 + row_h * len(items)
    top = 44
    max_v = max(v for _, v in items) or 1
    plot_w = width - label_w - 90

    out = [_header(width, h)]
    out.append(f'<text x="0" y="20" fill="{FG}" font-size="15" font-weight="600">{escape(title)}</text>')
    for i, (label, value) in enumerate(items):
        y = top + i * row_h
        bw = max(2, plot_w * value / max_v)
        color = (colors or {}).get(label) or BARS[i % len(BARS)]
        out.append(
            f'<text x="{label_w - 8}" y="{y + 13}" fill="{FG}" font-size="12.5" '
            f'text-anchor="end">{escape(str(label))}</text>'
        )
        out.append(
            f'<rect x="{label_w}" y="{y + 2}" width="{bw:.1f}" height="{row_h - 9}" '
            f'rx="3" fill="{color}"/>'
        )
        out.append(
            f'<text x="{label_w + bw + 7:.1f}" y="{y + 13}" fill="{MUTED}" '
            f'font-size="11.5">{escape(value_fmt.format(value))}</text>'
        )
    out.append("</svg>")
    return "".join(out)


def line_chart(series, weeks, title, width=760, height=320):
    """Multi-series trend lines. `series` is {name: [values aligned to weeks]}."""
    if not weeks or len(weeks) < 2:
        return None  # a single week is not a trend
    pad_l, pad_r, pad_t, pad_b = 52, 150, 46, 34
    pw, ph = width - pad_l - pad_r, height - pad_t - pad_b
    vals = [v for s in series.values() for v in s if v is not None]
    vmax = max(vals) if vals else 1
    vmax = vmax * 1.15 or 1

    def x(i):
        return pad_l + (pw * i / max(1, len(weeks) - 1))

    def y(v):
        return pad_t + ph - (ph * v / vmax)

    out = [_header(width, height)]
    out.append(f'<text x="0" y="20" fill="{FG}" font-size="15" font-weight="600">{escape(title)}</text>')
    # gridlines
    for frac in (0, 0.25, 0.5, 0.75, 1):
        gy = pad_t + ph * frac
        out.append(f'<line x1="{pad_l}" y1="{gy:.1f}" x2="{pad_l + pw}" y2="{gy:.1f}" stroke="{MUTED}" stroke-opacity="0.22"/>')
        out.append(f'<text x="{pad_l - 8}" y="{gy + 4:.1f}" fill="{MUTED}" font-size="10.5" text-anchor="end">{(1 - frac) * vmax:.0%}</text>')
    for i, wk in enumerate(weeks):
        if len(weeks) <= 12 or i % max(1, len(weeks) // 10) == 0:
            out.append(f'<text x="{x(i):.1f}" y="{height - 12}" fill="{MUTED}" font-size="10.5" text-anchor="middle">{escape(wk)}</text>')
    for idx, (name, points) in enumerate(series.items()):
        color = BARS[idx % len(BARS)]
        d = " ".join(
            f"{'M' if k == 0 else 'L'}{x(k):.1f},{y(v):.1f}"
            for k, v in enumerate(points) if v is not None
        )
        out.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.2" stroke-linejoin="round"/>')
        last = points[-1] if points[-1] is not None else 0
        out.append(f'<circle cx="{x(len(points) - 1):.1f}" cy="{y(last):.1f}" r="3.2" fill="{color}"/>')
        out.append(f'<text x="{pad_l + pw + 10}" y="{pad_t + 14 + idx * 19}" fill="{color}" font-size="12">{escape(name)}</text>')
    out.append("</svg>")
    return "".join(out)
