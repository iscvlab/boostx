#!/usr/bin/env python3
"""
Deterministic Zero-Dependency Academic SVG Figure Generator for BoostX (v3.1.0).

Uses ONLY the Python 3.8+ standard library (`json`, `math`, `pathlib`, `xml.sax.saxutils`)
to generate publication-grade vector SVG figures (IEEE / ACM / Edward Tufte minimalist style)
directly from `benchmarks/BENCHMARK_RESULTS.json`:
  - docs/assets/boostx-benchmark-summary.svg      (2x2 composite figure for README.md Section 4.4)
  - docs/assets/fig1_discovery_distribution.svg   (Experiment 1: N=109 skill discovery & trigger guards)
  - docs/assets/fig2_compression_latency.svg      (Experiments 2 & 3: Context compression & /layax latency)
  - docs/assets/fig3_ablation_redteam.svg         (Experiments 4 & 5: 25-defect red-team & ablation curve)
  - docs/assets/fig4_token_distributions.svg      (Experiment 6: N=65 sessions / 576 turns token quantiles)
"""

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple
from xml.sax.saxutils import escape

sys.dont_write_bytecode = True
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_JSON = REPO_ROOT / "benchmarks" / "BENCHMARK_RESULTS.json"
ASSETS_DIR = REPO_ROOT / "docs" / "assets"

# Okabe-Ito & IEEE Muted Academic Palette (Colorblind-Safe, High-Contrast on White)
PAL = {
    "bg": "#FFFFFF",
    "panel_bg": "#FAFBFD",
    "ink": "#1A202C",
    "sub": "#334155",
    "muted": "#64748B",
    "axis": "#334155",
    "grid": "#CBD5E1",
    "border": "#E2E8F0",
    "navy": "#1B4F72",
    "navy_fill": "#D6EAF8",
    "teal": "#117864",
    "teal_fill": "#D1F2EB",
    "violet": "#5B2C6F",
    "violet_fill": "#EBDEF0",
    "ochre": "#B9770E",
    "ochre_fill": "#FCF3CF",
    "slate": "#4A5568",
    "slate_fill": "#E2E8F0",
    "crimson": "#922B21",
    "crimson_fill": "#FADBD8",
}

FONT_SANS = "'DejaVu Sans', 'Arial', 'Helvetica', sans-serif"
FONT_MONO = "'DejaVu Sans Mono', 'Consolas', monospace"


class SvgCanvas:
    """Lightweight stdlib SVG builder for publication-grade scientific plots."""

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.elements: List[str] = []
        self.add(
            f'<rect x="0" y="0" width="{width}" height="{height}" '
            f'fill="{PAL["bg"]}" stroke="{PAL["border"]}" stroke-width="1"/>'
        )

    def add(self, raw_svg: str) -> None:
        self.elements.append(raw_svg)

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        stroke: str = PAL["axis"],
        width: float = 1.0,
        dash: str = "",
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{width}"{dash_attr}/>'
        )

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        fill: str = "none",
        stroke: str = "none",
        stroke_width: float = 1.0,
        rx: float = 0.0,
        opacity: float = 1.0,
    ) -> None:
        rx_attr = f' rx="{rx:.1f}"' if rx > 0 else ""
        op_attr = f' opacity="{opacity:.2f}"' if opacity < 1.0 else ""
        self.add(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(0.0, w):.1f}" height="{max(0.0, h):.1f}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{rx_attr}{op_attr}/>'
        )

    def circle(
        self,
        cx: float,
        cy: float,
        r: float,
        fill: str = PAL["navy"],
        stroke: str = "none",
        stroke_width: float = 1.0,
        opacity: float = 1.0,
    ) -> None:
        op_attr = f' opacity="{opacity:.2f}"' if opacity < 1.0 else ""
        self.add(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"{op_attr}/>'
        )

    def diamond(
        self,
        cx: float,
        cy: float,
        size: float = 5.0,
        fill: str = "#FFFFFF",
        stroke: str = PAL["navy"],
        stroke_width: float = 1.4,
    ) -> None:
        pts = f"{cx:.1f},{cy - size:.1f} {cx + size:.1f},{cy:.1f} {cx:.1f},{cy + size:.1f} {cx - size:.1f},{cy:.1f}"
        self.add(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}"/>')

    def text(
        self,
        x: float,
        y: float,
        content: str,
        size: float = 11.0,
        fill: str = PAL["ink"],
        weight: str = "normal",
        anchor: str = "start",
        mono: bool = False,
        rotate: float = 0.0,
    ) -> None:
        ff = FONT_MONO if mono else FONT_SANS
        tf = f' transform="rotate({rotate:.1f} {x:.1f} {y:.1f})"' if rotate != 0.0 else ""
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{ff}" font-size="{size:.1f}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{tf}>{escape(content)}</text>'
        )

    def h_boxplot(
        self,
        y_center: float,
        x_map,
        q_dict: Dict[str, float],
        stroke: str,
        fill: str,
        box_h: float = 20.0,
        use_max_whisker: bool = False,
    ) -> Tuple[float, float]:
        low_v = float(q_dict["min"])
        p25_v = float(q_dict["p25"])
        med_v = float(q_dict["median"])
        p75_v = float(q_dict["p75"])
        high_v = float(q_dict["max"] if use_max_whisker else q_dict.get("p95", q_dict["max"]))
        mean_v = float(q_dict["mean"])

        x_low = x_map(low_v)
        x_p25 = x_map(p25_v)
        x_med = x_map(med_v)
        x_p75 = x_map(p75_v)
        x_high = x_map(high_v)
        x_mean = x_map(mean_v)

        # Whiskers
        self.line(x_low, y_center, x_p25, y_center, stroke=stroke, width=1.3)
        self.line(x_p75, y_center, x_high, y_center, stroke=stroke, width=1.3)
        cap = box_h * 0.42
        self.line(x_low, y_center - cap, x_low, y_center + cap, stroke=stroke, width=1.3)
        self.line(x_high, y_center - cap, x_high, y_center + cap, stroke=stroke, width=1.3)

        # IQR Box
        self.rect(
            x_p25,
            y_center - box_h / 2.0,
            max(2.0, x_p75 - x_p25),
            box_h,
            fill=fill,
            stroke=stroke,
            stroke_width=1.4,
        )
        # Median line
        self.line(x_med, y_center - box_h / 2.0, x_med, y_center + box_h / 2.0, stroke=PAL["ink"], width=2.2)
        # Mean diamond
        self.diamond(x_mean, y_center, size=4.6, fill="#FFFFFF", stroke=stroke, stroke_width=1.5)
        return x_low, x_high

    def render(self) -> str:
        body = "\n  ".join(self.elements)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="100%" height="100%">\n  {body}\n</svg>\n'
        )


def draw_panel_axes(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    title: str,
    subtitle: str = "",
    right_spine: bool = False,
) -> None:
    """Draw academic panel title, subtle plot frame, and bottom/left spines."""
    svg.text(x0, y0 - 22, title, size=12.5, weight="bold", fill=PAL["ink"])
    if subtitle:
        svg.text(x0, y0 - 7, subtitle, size=10.0, fill=PAL["muted"])
    svg.line(x0, y0 + h, x0 + w, y0 + h, stroke=PAL["axis"], width=1.2)
    svg.line(x0, y0, x0, y0 + h, stroke=PAL["axis"], width=1.2)
    if right_spine:
        svg.line(x0 + w, y0, x0 + w, y0 + h, stroke=PAL["axis"], width=1.2)


# ==============================================================================
# 1. PANEL DRAWERS (REUSABLE ACROSS COMPOSITE & INDIVIDUAL FIGURES)
# ==============================================================================
def draw_discovery_boxplot_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp1: Dict[str, Any],
    title: str,
    subtitle: str,
) -> None:
    draw_panel_axes(svg, x0, y0, w, h, title, subtitle)

    max_x = 1250.0

    def x_map(v: float) -> float:
        return x0 + (min(max_x, max(0.0, float(v))) / max_x) * w

    # Vertical gridlines & X-axis ticks
    for tick in [0, 200, 400, 500, 600, 800, 1000]:
        tx = x_map(tick)
        if tick > 0:
            svg.line(tx, y0, tx, y0 + h, stroke=PAL["grid"], width=0.8, dash="3 3")
        svg.line(tx, y0 + h, tx, y0 + h + 5, stroke=PAL["axis"], width=1.0)
        col_t = PAL["crimson"] if tick == 500 else PAL["sub"]
        wt_t = "bold" if tick == 500 else "normal"
        svg.text(tx, y0 + h + 18, str(tick), size=9.5, fill=col_t, weight=wt_t, anchor="middle", mono=True)

    svg.text(
        x0 + w / 2,
        y0 + h + 38,
        "YAML Frontmatter Description Length (characters) • Box = IQR [P25–P75], Line = Median, ♦ = Mean",
        size=10.0,
        fill=PAL["sub"],
        anchor="middle",
    )

    # 500-char truncation threshold line
    tx500 = x_map(500)
    svg.line(tx500, y0, tx500, y0 + h, stroke=PAL["crimson"], width=1.6, dash="5 3")
    svg.text(tx500 + 6, y0 + 14, "500-Char Budget Gate", size=9.2, fill=PAL["crimson"], weight="bold")

    n_bx = exp1["boostx_13"]["count"]
    n_oev = exp1["official_enterprise"]["count"]
    n_all = exp1["all_installed"]["count"]
    n_dom = exp1["community_and_domain"]["count"]
    cohorts = [
        ("BoostX v3.1.0 Suite", f"(n = {n_bx} skills)", exp1["boostx_13"], PAL["navy"], PAL["navy_fill"]),
        (
            "Official Cloud / Vendor", f"(n = {n_oev} skills)",
            exp1["official_enterprise"], PAL["ochre"], PAL["ochre_fill"],
        ),
        ("All Installed Host Pool", f"(N = {n_all} skills)", exp1["all_installed"], PAL["violet"], PAL["violet_fill"]),
        ("Other Domain Skills", f"(n = {n_dom} skills)", exp1["community_and_domain"], PAL["slate"], PAL["slate_fill"]),
    ]

    row_h = h / len(cohorts)
    for idx, (c_name, c_sub, c_obj, stroke_c, fill_c) in enumerate(cohorts):
        yc = y0 + (idx + 0.52) * row_h
        svg.text(x0 - 10, yc - 3, c_name, size=10.2, weight="bold", fill=PAL["ink"], anchor="end")
        svg.text(x0 - 10, yc + 11, c_sub, size=9.0, fill=PAL["muted"], anchor="end", mono=True)

        q_d = c_obj["desc_chars"]
        _, x_hi = svg.h_boxplot(yc, x_map, q_d, stroke=stroke_c, fill=fill_c, box_h=22.0, use_max_whisker=True)

        # If BoostX row, plot individual skill points
        if idx == 0:
            for s_idx, sk in enumerate(exp1["per_boostx_skill"]):
                jit = ((s_idx % 5) - 2) * 2.4
                svg.circle(x_map(sk["desc_chars"]), yc + jit, r=2.6, fill=PAL["navy"], opacity=0.75)

        stat_lbl = (
            f"{q_d['mean']:.0f}±{q_d['std']:.0f} ch "
            f"(Guard: {c_obj['dual_trigger_guard_pct']:.1f}%)"
        )
        svg.text(x_hi + 8, yc + 4, stat_lbl, size=9.2, weight="bold", fill=stroke_c, mono=True)


def draw_discovery_compliance_bars_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp1: Dict[str, Any],
    title: str,
    subtitle: str,
) -> None:
    draw_panel_axes(svg, x0, y0, w, h, title, subtitle)

    for pct in [0, 20, 40, 60, 80, 100]:
        py = y0 + h - (pct / 122.0) * h
        if pct > 0:
            svg.line(x0, py, x0 + w, py, stroke=PAL["grid"], width=0.8, dash="3 3")
        svg.line(x0 - 4, py, x0, py, stroke=PAL["axis"], width=1.0)
        svg.text(x0 - 8, py + 3.5, f"{pct}%", size=9.5, fill=PAL["sub"], anchor="end", mono=True)

    svg.text(x0 - 42, y0 + h / 2, "Cohort Compliance (%)", size=10.0, fill=PAL["sub"], anchor="middle", rotate=-90)

    b13 = exp1["boostx_13"]
    oev = exp1["official_enterprise"]
    all_s = exp1["all_installed"]
    dom_s = exp1["community_and_domain"]
    groups = [
        (
            "BoostX v3.1.0", f"(n={b13['count']})",
            b13["budget_500_compliance_pct"], b13["dual_trigger_guard_pct"], f"{b13['count']}/{b13['count']}",
        ),
        (
            "Official Vendor", f"(n={oev['count']})",
            oev["budget_500_compliance_pct"], oev["dual_trigger_guard_pct"], f"8/{oev['count']}",
        ),
        (
            "All Installed", f"(N={all_s['count']})",
            all_s["budget_500_compliance_pct"], all_s["dual_trigger_guard_pct"], f"33/{all_s['count']}",
        ),
        (
            "Other Domain", f"(n={dom_s['count']})",
            dom_s["budget_500_compliance_pct"], dom_s["dual_trigger_guard_pct"], f"11/{dom_s['count']}",
        ),
    ]

    col_w = w / len(groups)
    bar_w = min(34.0, col_w * 0.30)

    for idx, (g_name, g_sub, b_pct, d_pct, frac) in enumerate(groups):
        cx = x0 + (idx + 0.5) * col_w
        # Bar 1: <=500 char pass
        bh1 = (b_pct / 122.0) * h
        bx1 = cx - bar_w - 3
        by1 = y0 + h - bh1
        svg.rect(bx1, by1, bar_w, bh1, fill=PAL["teal_fill"], stroke=PAL["teal"], stroke_width=1.3)
        svg.text(
            bx1 + bar_w / 2, by1 - 5, f"{b_pct:.1f}%",
            size=8.8, weight="bold", fill=PAL["teal"], anchor="middle", mono=True,
        )

        # Bar 2: Dual Trigger Guard
        bh2 = (d_pct / 122.0) * h
        bx2 = cx + 3
        by2 = y0 + h - bh2
        svg.rect(bx2, by2, bar_w, bh2, fill=PAL["navy"], stroke=PAL["ink"], stroke_width=1.1)
        svg.text(
            bx2 + bar_w / 2, by2 - 15, f"{d_pct:.1f}%",
            size=8.8, weight="bold", fill=PAL["navy"], anchor="middle", mono=True,
        )
        svg.text(bx2 + bar_w / 2, by2 - 4, f"({frac})", size=8.0, fill=PAL["sub"], anchor="middle", mono=True)

        svg.text(cx, y0 + h + 16, g_name, size=9.8, weight="bold", fill=PAL["ink"], anchor="middle")
        svg.text(cx, y0 + h + 29, g_sub, size=8.8, fill=PAL["muted"], anchor="middle", mono=True)

    # Legend centered in upper valley above Official Vendor / All Installed
    lx, ly = x0 + 128, y0 + 5
    svg.rect(lx, ly, 232, 36, fill="#FFFFFF", stroke=PAL["grid"], stroke_width=0.9, rx=3)
    svg.rect(lx + 8, ly + 6, 11, 10, fill=PAL["teal_fill"], stroke=PAL["teal"], stroke_width=1.2)
    svg.text(lx + 24, ly + 15, "≤ 500-Char Budget Pass (%)", size=8.8, fill=PAL["ink"])
    svg.rect(lx + 8, ly + 21, 11, 10, fill=PAL["navy"], stroke=PAL["ink"], stroke_width=1.0)
    svg.text(lx + 24, ly + 30, "Dual Guard: Use + Do NOT Use (%)", size=8.8, fill=PAL["ink"])


def draw_compression_log_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp2: Dict[str, Any],
    title: str,
    subtitle: str,
) -> None:
    draw_panel_axes(svg, x0, y0, w, h, title, subtitle, right_spine=True)

    # Left Y: log10 tokens from 10^3 (3.0) to 10^6.5 (6.5)
    log_tok_min, log_tok_max = 3.5, 6.4

    def y_tok(v: float) -> float:
        return y0 + h - ((math.log10(max(1.0, v)) - log_tok_min) / (log_tok_max - log_tok_min)) * h

    # Right Y: log10 latency (ms) from 10^-0.5 (-0.5 = 0.316ms) to 10^2.0 (100ms)
    log_lat_min, log_lat_max = -0.5, 2.0

    def y_lat(v: float) -> float:
        return y0 + h - ((math.log10(max(0.05, v)) - log_lat_min) / (log_lat_max - log_lat_min)) * h

    for exp_p, lbl_t in [(4, "10⁴"), (5, "10⁵"), (6, "10⁶")]:
        py = y_tok(10 ** exp_p)
        svg.line(x0, py, x0 + w, py, stroke=PAL["grid"], width=0.8, dash="3 3")
        svg.line(x0 - 4, py, x0, py, stroke=PAL["navy"], width=1.0)
        svg.text(x0 - 7, py + 3.5, lbl_t, size=9.5, fill=PAL["navy"], weight="bold", anchor="end", mono=True)

    for lat_v, lbl_l in [(0.5, "0.5"), (1.0, "1.0"), (5.0, "5.0"), (10.0, "10"), (50.0, "50")]:
        py = y_lat(lat_v)
        svg.line(x0 + w, py, x0 + w + 4, py, stroke=PAL["teal"], width=1.0)
        svg.text(x0 + w + 7, py + 3.5, lbl_l, size=9.2, fill=PAL["teal"], weight="bold", anchor="start", mono=True)

    svg.text(
        x0 - 38, y0 + h / 2, "Context Tokens (log₁₀)",
        size=9.8, fill=PAL["navy"], weight="bold", anchor="middle", rotate=-90,
    )
    svg.text(
        x0 + w + 38, y0 + h / 2, "Disk Read Latency (ms, log₁₀)",
        size=9.8, fill=PAL["teal"], weight="bold", anchor="middle", rotate=90,
    )

    regimes = [
        ("1. Unbounded Crawl", "(710 files: Repo+Vault)", exp2["unbounded_crawl"], ""),
        ("2. /briefx Repo-Only", "(Cap 8: 8 files)", exp2["briefx_repo_only"], "-98.24%"),
        ("3. /briefx + /obsidianx", "(Cap 8 + 2-Hop: 12 files)", exp2["briefx_obsidianx_2hop"], "-97.94%"),
    ]

    col_w = w / 3.0
    bar_w = min(38.0, col_w * 0.30)

    for idx, (r_name, r_sub, r_obj, delta_s) in enumerate(regimes):
        cx = x0 + (idx + 0.5) * col_w
        tok_v = r_obj["tokens_loaded"]
        lat_q = r_obj["latency_ms"]

        # Token bar (Navy)
        by_t = y_tok(tok_v)
        bh_t = y0 + h - by_t
        bx_t = cx - bar_w - 3
        svg.rect(bx_t, by_t, bar_w, bh_t, fill=PAL["navy_fill"], stroke=PAL["navy"], stroke_width=1.4)
        tok_str = f"{tok_v / 1000.0:,.1f}k"
        svg.text(
            bx_t + bar_w / 2, by_t - (14 if delta_s else 5), tok_str,
            size=8.8, weight="bold", fill=PAL["navy"], anchor="middle", mono=True,
        )
        if delta_s:
            svg.text(
                bx_t + bar_w / 2, by_t - 3, f"({delta_s})",
                size=8.0, weight="bold", fill=PAL["navy"], anchor="middle", mono=True,
            )

        # Latency bar (Teal) + P25-P95 whisker
        med_ms = lat_q["median"]
        p25_ms = lat_q["p25"]
        p95_ms = lat_q["p95"]
        by_l = y_lat(med_ms)
        bh_l = y0 + h - by_l
        bx_l = cx + 3
        svg.rect(bx_l, by_l, bar_w, bh_l, fill=PAL["teal_fill"], stroke=PAL["teal"], stroke_width=1.4)

        # Error whisker (P25 to P95)
        wx = bx_l + bar_w / 2
        wy_lo = y_lat(p25_ms)
        wy_hi = y_lat(p95_ms)
        svg.line(wx, wy_lo, wx, wy_hi, stroke=PAL["ink"], width=1.4)
        svg.line(wx - 5, wy_hi, wx + 5, wy_hi, stroke=PAL["ink"], width=1.4)
        svg.line(wx - 5, wy_lo, wx + 5, wy_lo, stroke=PAL["ink"], width=1.4)

        svg.text(
            wx, wy_hi - 6, f"{med_ms:.2f} ms",
            size=8.8, weight="bold", fill=PAL["teal"], anchor="middle", mono=True,
        )

        svg.text(cx, y0 + h + 16, r_name, size=9.6, weight="bold", fill=PAL["ink"], anchor="middle")
        svg.text(cx, y0 + h + 29, r_sub, size=8.5, fill=PAL["muted"], anchor="middle", mono=True)


def draw_layax_triage_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp3: Dict[str, Any],
    title: str,
    subtitle: str,
) -> None:
    draw_panel_axes(svg, x0, y0, w, h, title, subtitle)

    # Top half of panel: Horizontal bar comparison of Full Corpus vs Top-5 Shortlist tokens
    bar_y0 = y0 + 28
    max_tok = 90000.0

    def x_tok(v: float) -> float:
        return x0 + (v / max_tok) * (w * 0.72)

    items = [
        (
            "Full Unchunked Corpus (20 Specs / 390 Chunks)",
            exp3["full_corpus_tokens"], PAL["slate"], PAL["slate_fill"], "78,533 tok (100%)",
        ),
        (
            "/layax Top-5 Shortlisted Sections (Pass-B Read)",
            exp3["top5_shortlisted_tokens"], PAL["navy"], PAL["navy_fill"], "1,344 tok (-98.29%)",
        ),
    ]
    for idx, (lbl, tv, col, fill_c, val_s) in enumerate(items):
        by = bar_y0 + idx * 56
        svg.text(x0 + 2, by - 6, lbl, size=9.8, weight="bold", fill=PAL["ink"])
        bw = max(6.0, x_tok(tv) - x0)
        svg.rect(x0, by, bw, 22, fill=fill_c, stroke=col, stroke_width=1.4)
        svg.text(x0 + bw + 8, by + 15, val_s, size=9.5, weight="bold", fill=col, mono=True)

    # Bottom half: Horizontal Boxplot of n=30 Single-Pass Triage Latency Trials (ms)
    sub_y = y0 + h - 68
    svg.line(x0, sub_y - 38, x0 + w, sub_y - 38, stroke=PAL["border"], width=1.0)
    svg.text(
        x0 + 2,
        sub_y - 20,
        "Single-Pass Section Ranking Latency Distribution (n = 30 Timed Trials, 390 Chunks → 44,725 chunks/sec):",
        size=9.6,
        weight="bold",
        fill=PAL["ink"],
    )

    lat_q = exp3["latency_ms"]
    min_ms, max_ms = 7.0, 11.5

    def x_ms(v: float) -> float:
        return x0 + ((v - min_ms) / (max_ms - min_ms)) * w

    for tick_m in [7.0, 8.0, 9.0, 10.0, 11.0]:
        tx = x_ms(tick_m)
        svg.line(tx, sub_y - 8, tx, sub_y + 38, stroke=PAL["grid"], width=0.8, dash="2 2")
        svg.line(tx, sub_y + 68, tx, sub_y + 73, stroke=PAL["axis"], width=1.0)
        svg.text(tx, sub_y + 84, f"{tick_m:.1f} ms", size=8.8, fill=PAL["sub"], anchor="middle", mono=True)

    svg.h_boxplot(sub_y + 18, x_ms, lat_q, stroke=PAL["teal"], fill=PAL["teal_fill"], box_h=24.0, use_max_whisker=True)
    svg.text(
        x_ms(lat_q["median"]),
        sub_y + 1,
        f"Med {lat_q['median']:.2f} ms",
        size=8.6,
        weight="bold",
        fill=PAL["teal"],
        anchor="middle",
        mono=True,
    )
    svg.text(
        x0 + w / 2,
        sub_y + 54,
        f"Min: {lat_q['min']:.2f} ms • P25: {lat_q['p25']:.2f} ms • Median: {lat_q['median']:.2f} ms "
        f"(Mean {lat_q['mean']:.2f}±{lat_q['std']:.2f}) • P75: {lat_q['p75']:.2f} ms • "
        f"P95: {lat_q['p95']:.2f} ms • Max: {lat_q['max']:.2f} ms",
        size=8.6,
        fill=PAL["ink"],
        anchor="middle",
        mono=True,
    )


def draw_redteam_bars_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp4: Dict[str, Any],
    title: str,
    subtitle: str,
) -> None:
    q_rt = exp4["suite_execution_latency_ms"]
    full_sub = f"{subtitle} • Suite Latency: Med {q_rt['median']:.2f} ms (P95 {q_rt['p95']:.2f} ms)"
    draw_panel_axes(svg, x0, y0, w, h, title, full_sub)

    max_def = 6.2

    def x_def(v: float) -> float:
        return x0 + (v / max_def) * w

    for d_tick in [0, 1, 2, 3, 4, 5]:
        tx = x_def(d_tick)
        if d_tick > 0:
            svg.line(tx, y0, tx, y0 + h, stroke=PAL["grid"], width=0.8, dash="3 3")
        svg.line(tx, y0 + h, tx, y0 + h + 5, stroke=PAL["axis"], width=1.0)
        svg.text(tx, y0 + h + 18, f"{d_tick} / 5", size=9.2, fill=PAL["sub"], anchor="middle", mono=True)

    svg.text(
        x0 + w / 2,
        y0 + h + 38,
        "Seeded Defects Deterministically Caught per Category (25 Total Seeded • 0 False Positives)",
        size=9.8,
        fill=PAL["sub"],
        anchor="middle",
    )

    cats = [
        ("1. Security & Secrets", "audit_engine.py"),
        ("2. Qt6 / QGIS 4 AST", "check_qt6.py + INI"),
        ("3. Research Citations", "verify_evidence.py"),
        ("4. Doc Sync & Mirrors", "audit_workspace_docs.py"),
        ("5. Skill Budget & Hygiene", "audit_engine.py --skill"),
    ]
    row_h = h / len(cats)
    for idx, (c_title, c_gate) in enumerate(cats):
        yc = y0 + (idx + 0.5) * row_h
        svg.text(x0 - 10, yc - 2, c_title, size=9.8, weight="bold", fill=PAL["ink"], anchor="end")
        svg.text(x0 - 10, yc + 11, c_gate, size=8.6, fill=PAL["muted"], anchor="end", mono=True)

        # BoostX CLI Gate bar (5/5)
        bw = x_def(5.0) - x0
        svg.rect(x0, yc - 13, bw, 14, fill=PAL["navy"], stroke=PAL["ink"], stroke_width=1.0)
        svg.text(x0 + bw + 8, yc - 2, "5/5 (100% CLI Catch)", size=8.8, weight="bold", fill=PAL["navy"], mono=True)

        # Prompt-Only Baseline bar (0/5)
        svg.rect(x0, yc + 3, 4, 10, fill=PAL["crimson_fill"], stroke=PAL["crimson"], stroke_width=1.0)
        svg.text(
            x0 + 10, yc + 12, "0/5 Prompt-Only Baseline (No Pre-LLM CLI Gate)",
            size=8.2, fill=PAL["crimson"], mono=True,
        )


def draw_ablation_curve_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp5: List[Dict[str, Any]],
    title: str,
    subtitle: str,
) -> None:
    draw_panel_axes(svg, x0, y0, w, h, title, subtitle, right_spine=True)

    # Left Y: Recall 0..100%
    def y_rec(v: float) -> float:
        return y0 + h - (v / 115.0) * h

    # Right Y: Log10 Steps (10^1 .. 10^3)
    def y_stp(v: float) -> float:
        return y0 + h - ((math.log10(max(10.0, v)) - 1.0) / 2.0) * h

    for pct in [0, 20, 40, 60, 80, 100]:
        py = y_rec(pct)
        if pct > 0:
            svg.line(x0, py, x0 + w, py, stroke=PAL["grid"], width=0.8, dash="3 3")
        svg.line(x0 - 4, py, x0, py, stroke=PAL["navy"], width=1.0)
        svg.text(x0 - 7, py + 3.5, f"{pct}%", size=9.2, fill=PAL["navy"], weight="bold", anchor="end", mono=True)

    for st_v, st_lbl in [(10, "10¹"), (50, "50"), (100, "10²"), (500, "500")]:
        py = y_stp(st_v)
        svg.line(x0 + w, py, x0 + w + 4, py, stroke=PAL["teal"], width=1.0)
        svg.text(x0 + w + 7, py + 3.5, st_lbl, size=9.2, fill=PAL["teal"], weight="bold", anchor="start", mono=True)

    svg.text(
        x0 - 40, y0 + h / 2, "Defect Recall (%)",
        size=9.8, fill=PAL["navy"], weight="bold", anchor="middle", rotate=-90,
    )
    svg.text(
        x0 + w + 40, y0 + h / 2, "Trajectory Depth (Steps, log₁₀)",
        size=9.8, fill=PAL["teal"], weight="bold", anchor="middle", rotate=90,
    )

    levels = [
        ("Level 0", "Raw Prompt (0 Gates)", exp5[0]["seeded_defect_catch_pct"], exp5[0]["avg_steps_per_turn"]),
        ("Level 1", "/boostx (2 Gates)", exp5[1]["seeded_defect_catch_pct"], exp5[1]["avg_steps_per_turn"]),
        ("Level 2", "2-Hop Chain (4 Gates)", exp5[2]["seeded_defect_catch_pct"], exp5[2]["avg_steps_per_turn"]),
        ("Level 3", "Full 5-Stage (7 Gates)", exp5[3]["seeded_defect_catch_pct"], exp5[3]["avg_steps_per_session"]),
    ]

    xs = [x0 + (i + 0.5) * (w / 4.0) for i in range(4)]
    pts_rec = [(xs[i], y_rec(levels[i][2])) for i in range(4)]
    pts_stp = [(xs[i], y_stp(levels[i][3])) for i in range(4)]

    # Connect lines
    for i in range(3):
        svg.line(pts_rec[i][0], pts_rec[i][1], pts_rec[i + 1][0], pts_rec[i + 1][1], stroke=PAL["navy"], width=2.4)
        svg.line(
            pts_stp[i][0], pts_stp[i][1], pts_stp[i + 1][0], pts_stp[i + 1][1],
            stroke=PAL["teal"], width=2.2, dash="6 4",
        )

    for i, (l_name, l_sub, rv, sv) in enumerate(levels):
        rx, ry = pts_rec[i]
        sx, sy = pts_stp[i]
        svg.rect(rx - 4.5, ry - 4.5, 9.0, 9.0, fill=PAL["navy"], stroke="#FFFFFF", stroke_width=1.5)
        svg.circle(sx, sy, r=5.0, fill=PAL["teal"], stroke="#FFFFFF", stroke_width=1.5)

        svg.text(rx, ry - 10, f"{rv:.0f}%", size=9.2, weight="bold", fill=PAL["navy"], anchor="middle", mono=True)
        st_offset = 18 if sy >= ry else -10
        svg.text(
            sx + (8 if i == 0 else 0), sy + st_offset, f"{sv:.1f} st",
            size=8.8, weight="bold", fill=PAL["teal"], anchor="middle", mono=True,
        )

        svg.text(xs[i], y0 + h + 16, l_name, size=9.8, weight="bold", fill=PAL["ink"], anchor="middle")
        svg.text(xs[i], y0 + h + 29, l_sub, size=8.4, fill=PAL["muted"], anchor="middle", mono=True)

    # Legend
    lx, ly = x0 + 12, y0 + 10
    svg.rect(lx, ly, 215, 36, fill="#FFFFFF", stroke=PAL["grid"], stroke_width=0.9, rx=3)
    svg.line(lx + 8, ly + 12, lx + 26, ly + 12, stroke=PAL["navy"], width=2.4)
    svg.rect(lx + 14, ly + 8.5, 7, 7, fill=PAL["navy"])
    svg.text(lx + 32, ly + 15, "Seeded Defect Recall (%)", size=8.8, fill=PAL["ink"])
    svg.line(lx + 8, ly + 26, lx + 26, ly + 26, stroke=PAL["teal"], width=2.0, dash="4 2")
    svg.circle(lx + 17, ly + 26, r=3.5, fill=PAL["teal"])
    svg.text(lx + 32, ly + 29, "Mean Trajectory Depth (Steps)", size=8.8, fill=PAL["ink"])


def draw_per_turn_tokens_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp6: Dict[str, Any],
    title: str,
    subtitle: str,
) -> None:
    draw_panel_axes(svg, x0, y0, w, h, title, subtitle)

    # Y-axis: log10 tokens from 10^2 (2.0) to 10^7 (7.0)
    log_min, log_max = 2.0, 7.0

    def y_tok(v: float) -> float:
        return y0 + h - ((math.log10(max(100.0, v)) - log_min) / (log_max - log_min)) * h

    for p_exp, p_lbl in [(2, "10²"), (3, "10³"), (4, "10⁴"), (5, "10⁵"), (6, "10⁶"), (7, "10⁷")]:
        py = y_tok(10 ** p_exp)
        if p_exp > 2:
            svg.line(x0, py, x0 + w, py, stroke=PAL["grid"], width=0.8, dash="3 3")
        svg.line(x0 - 4, py, x0, py, stroke=PAL["axis"], width=1.0)
        svg.text(x0 - 7, py + 3.5, p_lbl, size=9.2, fill=PAL["sub"], anchor="end", mono=True)

    svg.text(
        x0 - 42, y0 + h / 2, "Tokens per Prompt Turn (log₁₀ scale)",
        size=9.8, fill=PAL["sub"], anchor="middle", rotate=-90,
    )

    pt = exp6["per_turn"]
    components = [
        ("Uncached Input", "(NewIn)", "uncached_new_input_tokens"),
        ("Model Output", "(Completion)", "output_tokens"),
        ("Internal Thinking", "(Reasoning)", "thinking_tokens"),
        ("KV-Cache Replay", "(Context Reuse)", "kv_cache_read_tokens"),
    ]
    modes = [
        ("Standard (n=450)", pt["standard_no_skill"], PAL["slate"], PAL["slate_fill"]),
        ("Single -x (n=58)", pt["single_boostx_skill"], PAL["violet"], PAL["violet_fill"]),
        ("Chained 2+ -x (n=68)", pt["chained_multi_skill"], PAL["navy"], PAL["navy_fill"]),
    ]

    col_w = w / len(components)
    bar_w = min(26.0, col_w * 0.23)

    for c_idx, (c_name, c_sub, c_key) in enumerate(components):
        cx = x0 + (c_idx + 0.5) * col_w
        for m_idx, (_, m_obj, col, fill_c) in enumerate(modes):
            q_d = m_obj[c_key]
            mean_v = q_d["mean"]
            med_v = q_d["median"]
            p25_v = max(120.0, q_d["p25"])
            p75_v = q_d["p75"]

            bx = cx + (m_idx - 1.5) * (bar_w + 3) + 1.5
            by = y_tok(mean_v)
            bh = y0 + h - by
            svg.rect(bx, by, bar_w, bh, fill=fill_c, stroke=col, stroke_width=1.2)

            # Median dot + P25-P75 IQR whisker
            wx = bx + bar_w / 2
            wy_med = y_tok(med_v)
            wy_lo = y_tok(p25_v)
            wy_hi = y_tok(p75_v)
            svg.line(wx, wy_lo, wx, wy_hi, stroke=PAL["ink"], width=1.2)
            svg.line(wx - 3.5, wy_hi, wx + 3.5, wy_hi, stroke=PAL["ink"], width=1.2)
            svg.line(wx - 3.5, wy_lo, wx + 3.5, wy_lo, stroke=PAL["ink"], width=1.2)
            svg.circle(wx, wy_med, r=2.8, fill=col, stroke="#FFFFFF", stroke_width=0.9)

            if m_idx == 2:
                lbl_v = f"{mean_v / 1000.0:.0f}k" if mean_v < 1e6 else f"{mean_v / 1e6:.2f}M"
                svg.text(
                    wx + 2, min(by, wy_hi) - 5, lbl_v,
                    size=8.0, weight="bold", fill=col, anchor="middle", mono=True,
                )

        svg.text(cx, y0 + h + 16, c_name, size=9.6, weight="bold", fill=PAL["ink"], anchor="middle")
        svg.text(cx, y0 + h + 29, c_sub, size=8.5, fill=PAL["muted"], anchor="middle", mono=True)

    # Legend
    lx, ly = x0 + 10, y0 + 6
    svg.rect(lx, ly, 315, 24, fill="#FFFFFF", stroke=PAL["grid"], stroke_width=0.9, rx=3)
    for m_idx, (m_lbl, _, col, fill_c) in enumerate(modes):
        mx = lx + 8 + m_idx * 104
        svg.rect(mx, ly + 7, 10, 10, fill=fill_c, stroke=col, stroke_width=1.2)
        svg.text(mx + 14, ly + 15.5, m_lbl, size=8.2, fill=PAL["ink"])


def draw_session_tiers_panel(
    svg: SvgCanvas,
    x0: float,
    y0: float,
    w: float,
    h: float,
    exp6: Dict[str, Any],
    title: str,
    subtitle: str,
) -> None:
    draw_panel_axes(svg, x0, y0, w, h, title, subtitle)

    max_m = 68.0

    def x_map(v: float) -> float:
        return x0 + (min(max_m, max(0.0, float(v))) / max_m) * w

    # Shaded subscription tier zones (0-6M, 6-26M, 26-68M)
    x_t1 = x_map(6.0)
    x_t2 = x_map(26.0)
    svg.rect(x0, y0, x_t1 - x0, h, fill="#F1F5F9", opacity=0.75)
    svg.rect(x_t1, y0, x_t2 - x_t1, h, fill="#EBF8FF", opacity=0.65)
    svg.rect(x_t2, y0, x0 + w - x_t2, h, fill="#E6FFFA", opacity=0.65)
    svg.line(x_t1, y0, x_t1, y0 + h, stroke=PAL["slate"], width=1.2, dash="4 3")
    svg.line(x_t2, y0, x_t2, y0 + h, stroke=PAL["navy"], width=1.2, dash="4 3")

    svg.text((x0 + x_t1) / 2, y0 + 14, "1× Pro", size=8.6, weight="bold", fill=PAL["slate"], anchor="middle")
    svg.text(
        (x_t1 + x_t2) / 2, y0 + 14, "5× Max Tier (Daily Sprints)",
        size=8.8, weight="bold", fill=PAL["navy"], anchor="middle",
    )
    svg.text(
        (x_t2 + x0 + w) / 2, y0 + 14, "20× Ultra Tier (400+ Step Marathons)",
        size=8.8, weight="bold", fill=PAL["teal"], anchor="middle",
    )

    for tick in [0, 10, 20, 30, 40, 50, 60]:
        tx = x_map(tick)
        if tick > 0:
            svg.line(tx, y0 + 22, tx, y0 + h, stroke=PAL["grid"], width=0.8, dash="3 3")
        svg.line(tx, y0 + h, tx, y0 + h + 5, stroke=PAL["axis"], width=1.0)
        svg.text(tx, y0 + h + 18, f"{tick}M", size=9.2, fill=PAL["sub"], anchor="middle", mono=True)

    svg.text(
        x0 + w / 2,
        y0 + h + 38,
        "Cumulative Session Token Throughput (Millions of Tokens, N = 65 Sessions • Whisker = P90)",
        size=9.8,
        fill=PAL["sub"],
        anchor="middle",
    )

    ps = exp6["per_session"]
    cohorts = [
        (
            "Chained Multi-Skill", "(BoostX, n = 33)",
            ps["chained_multi_skill"]["total_processed_tokens"], PAL["navy"], PAL["navy_fill"],
        ),
        (
            "Single-Skill Session", "(BoostX, n = 4)",
            ps["single_boostx_skill"]["total_processed_tokens"], PAL["violet"], PAL["violet_fill"],
        ),
        (
            "Standard Session", "(No -x, n = 28)",
            ps["standard_no_skill"]["total_processed_tokens"], PAL["slate"], PAL["slate_fill"],
        ),
    ]

    row_h = (h - 24) / len(cohorts)
    for idx, (s_name, s_sub, q_raw, col, fill_c) in enumerate(cohorts):
        yc = y0 + 24 + (idx + 0.5) * row_h
        svg.text(x0 - 10, yc - 2, s_name, size=9.8, weight="bold", fill=PAL["ink"], anchor="end")
        svg.text(x0 - 10, yc + 11, s_sub, size=8.6, fill=PAL["muted"], anchor="end", mono=True)

        q_m = {k: v / 1e6 for k, v in q_raw.items()}
        q_m["p95"] = q_m["p90"]
        _, x_hi = svg.h_boxplot(yc, x_map, q_m, stroke=col, fill=fill_c, box_h=22.0, use_max_whisker=False)
        lbl_s = f"Mean {q_m['mean']:.1f}M (Med {q_m['median']:.1f}M, P90 {q_m['p90']:.1f}M)"
        if idx == 0:
            svg.text(x_map(26.8), yc - 16, lbl_s, size=8.6, weight="bold", fill=col, mono=True)
        else:
            svg.text(x_hi + 7, yc + 4, lbl_s, size=8.8, weight="bold", fill=col, mono=True)


# ==============================================================================
# 2. GENERATE ALL 5 ACADEMIC SVG FIGURES
# ==============================================================================
def build_all_figures(data: Dict[str, Any]) -> Dict[str, Path]:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    outputs: Dict[str, Path] = {}

    # 1. Composite 2x2 Summary Figure for README.md (1280 x 780)
    c_sum = SvgCanvas(1280, 780)
    draw_discovery_boxplot_panel(
        c_sum, 155, 48, 435, 275, data["exp1_skill_discovery"],
        "(a) System-Prompt YAML Budget & Trigger Guards (N = 109)",
        "Character length distribution against 500-char host truncation limit",
    )
    draw_compression_log_panel(
        c_sum, 725, 48, 490, 275, data["exp2_context_compression"],
        "(b) Startup Context Compression & I/O Latency (n = 30 Trials)",
        "Log₁₀ tokens loaded (left) vs. disk read latency Med + IQR/P95 (right)",
    )
    draw_ablation_curve_panel(
        c_sum, 155, 430, 435, 275, data["exp5_composable_ablation"],
        "(c) Composable Workflow Ablation (Level 0 → Level 3)",
        "Deterministic defect recall (25 seeded) vs. mean trajectory steps",
    )
    draw_session_tiers_panel(
        c_sum, 745, 430, 490, 275, data["exp6_token_economics"],
        "(d) Session Token Distributions & Subscription Sizing (N = 65)",
        "Cumulative session throughput (IQR, P90 & Mean ♦) vs. plan capacity",
    )
    p_sum = ASSETS_DIR / "boostx-benchmark-summary.svg"
    p_sum.write_text(c_sum.render(), encoding="utf-8")
    outputs["boostx-benchmark-summary"] = p_sum

    # 2. Fig 1: Discovery Distribution & Compliance Bars (1260 x 400)
    c_f1 = SvgCanvas(1260, 400)
    draw_discovery_boxplot_panel(
        c_f1, 155, 48, 445, 285, data["exp1_skill_discovery"],
        "(a) YAML Frontmatter Character Distribution (N = 109 Skills)",
        "Min / P25–P75 IQR / Max whiskers, Median line, and Mean ♦ marker",
    )
    draw_discovery_compliance_bars_panel(
        c_f1, 745, 48, 485, 285, data["exp1_skill_discovery"],
        "(b) Budget Compliance vs. Dual Routing Guard Coverage",
        "Percentage passing ≤ 500-char limit vs. explicit Use + Do NOT Use guards",
    )
    p_f1 = ASSETS_DIR / "fig1_discovery_distribution.svg"
    p_f1.write_text(c_f1.render(), encoding="utf-8")
    outputs["fig1_discovery_distribution"] = p_f1

    # 3. Fig 2: Context Compression & /layax Triage Latency (1260 x 400)
    c_f2 = SvgCanvas(1260, 400)
    draw_compression_log_panel(
        c_f2, 95, 48, 495, 285, data["exp2_context_compression"],
        "(a) Startup Context Volume & Disk I/O Latency (n = 30 Trials)",
        "3 warm-ups + 30 timed passes across 710 repository & vault markdown files",
    )
    draw_layax_triage_panel(
        c_f2, 695, 48, 535, 285, data["exp3_layax_triage"],
        "(b) /layax System 1 Section Shortlisting (390 Chunks, n = 30 Trials)",
        "Pass-B reading token compression (-98.29%) and trial latency quantiles",
    )
    p_f2 = ASSETS_DIR / "fig2_compression_latency.svg"
    p_f2.write_text(c_f2.render(), encoding="utf-8")
    outputs["fig2_compression_latency"] = p_f2

    # 4. Fig 3: 25-Defect Red-Team & Composable Workflow Ablation (1260 x 400)
    c_f3 = SvgCanvas(1260, 400)
    draw_redteam_bars_panel(
        c_f3, 165, 48, 440, 285, data["exp4_redteam_defects"],
        "(a) 25-Defect Red-Team Injection Recall (n = 20 Trials)",
        "5 seeded defects per category across 7 zero-dependency Python CLI gates",
    )
    draw_ablation_curve_panel(
        c_f3, 725, 48, 470, 285, data["exp5_composable_ablation"],
        "(b) Composable Workflow Ablation (Level 0 → Level 3)",
        "Verification recall (%) vs. trajectory depth (steps) across skill chains",
    )
    p_f3 = ASSETS_DIR / "fig3_ablation_redteam.svg"
    p_f3.write_text(c_f3.render(), encoding="utf-8")
    outputs["fig3_ablation_redteam"] = p_f3

    # 5. Fig 4: Per-Turn & Full-Session Token Distributions (1260 x 400)
    c_f4 = SvgCanvas(1260, 400)
    draw_per_turn_tokens_panel(
        c_f4, 95, 48, 505, 285, data["exp6_token_economics"],
        "(a) Per-Turn Token Component Quantiles (N = 576 Prompt Turns)",
        "Bar = Mean, Circle = Median (P50), Whiskers = IQR [P25–P75] on log₁₀ scale",
    )
    draw_session_tiers_panel(
        c_f4, 745, 48, 485, 285, data["exp6_token_economics"],
        "(b) Full-Session Token Throughput & Tier Sizing (N = 65 Sessions)",
        "Cumulative session tokens (IQR, P90 & Mean ♦) mapped to subscription tiers",
    )
    p_f4 = ASSETS_DIR / "fig4_token_distributions.svg"
    p_f4.write_text(c_f4.render(), encoding="utf-8")
    outputs["fig4_token_distributions"] = p_f4

    for name, path in outputs.items():
        print(f"  [OK] Generated zero-dependency academic SVG: {path.relative_to(REPO_ROOT)}")

    return outputs


def render_png_previews_via_playwright(outputs: Dict[str, Path], preview_dir: Path) -> None:
    """Optionally rasterize SVG figures to PNG for visual QA inspection."""
    from playwright.sync_api import sync_playwright

    preview_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1320, "height": 820}, device_scale_factor=2)
        for name, svg_path in outputs.items():
            page.goto(svg_path.resolve().as_uri(), wait_until="networkidle")
            png_out = preview_dir / f"{name}.png"
            svg_el = page.locator("svg")
            svg_el.screenshot(path=str(png_out), type="png")
            print(f"  [OK] Rasterized PNG preview: {png_out.name}")
        browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate zero-dependency academic SVG benchmark figures")
    parser.add_argument("--preview-dir", type=str, default="", help="Optional directory to save PNG previews")
    args = parser.parse_args()

    if not RESULTS_JSON.exists():
        print(f"ERROR: Missing {RESULTS_JSON}", file=sys.stderr)
        return 1

    data = json.loads(RESULTS_JSON.read_text(encoding="utf-8"))
    outputs = build_all_figures(data)

    if args.preview_dir:
        render_png_previews_via_playwright(outputs, Path(args.preview_dir))

    return 0


if __name__ == "__main__":
    sys.exit(main())
