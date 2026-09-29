"""
Build PDF/HTML textbooks from NEC License Exam markdown files.
Supports all 10 chapters with proper LaTeX rendering via latex2mathml.
"""
import markdown
import os
import re
import sys
import argparse

try:
    import latex2mathml.converter
    HAS_LATEX2MATHML = True
except ImportError:
    HAS_LATEX2MATHML = False
    print("Warning: latex2mathml not installed. LaTeX will not render properly.")
    print("Install with: pip install latex2mathml")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(BASE_DIR, "styles.css")

CHAPTERS = {
    1:  {"dir": "CH1",  "title": "Concept of Basic Electrical and Electronics Engineering", "code": "AExE01",
         "files": ["ch1_master_roadmap.md", "ch1_s1.1_part1.md", "ch1_s1.1_part2.md",
                   "ch1_s1.2.md", "ch1_s1.3.md", "ch1_s1.4.md", "ch1_s1.5.md", "ch1_s1.6.md"]},
    2:  {"dir": "CH2",  "title": "Digital Logic and Microprocessors", "code": "AExE02",
         "files": ["ch2_s2.1.md", "ch2_s2.2.md", "ch2_s2.3.md", "ch2_s2.4.md", "ch2_s2.5.md", "ch2_s2.6.md"]},
    3:  {"dir": "CH3",  "title": "Computer Programming (C & C++)", "code": "ACtE03",
         "files": ["ch3_s3.1.md", "ch3_s3.2.md", "ch3_s3.3.md", "ch3_s3.4.md", "ch3_s3.5.md", "ch3_s3.6.md"]},
    4:  {"dir": "CH4",  "title": "Computer Organization and Architecture", "code": "ACtE04",
         "files": ["ch4_s4.1.md", "ch4_s4.2.md", "ch4_s4.3.md", "ch4_s4.4.md", "ch4_s4.5.md", "ch4_s4.6.md"]},
    5:  {"dir": "CH5",  "title": "Computer Networks", "code": "ACtE05",
         "files": ["ch5_s5.1.md", "ch5_s5.2.md", "ch5_s5.3.md", "ch5_s5.4.md", "ch5_s5.5.md", "ch5_s5.6.md"]},
    6:  {"dir": "CH6",  "title": "Electromagnetics, Signals, and Communication", "code": "AEiE06",
         "files": ["ch6_s6.1.md", "ch6_s6.2.md", "ch6_s6.3.md", "ch6_s6.4.md", "ch6_s6.5.md", "ch6_s6.6.md"]},
    7:  {"dir": "CH7",  "title": "Data Structures, DBMS, and Operating Systems", "code": "AEiE07",
         "files": ["ch7_s7.1.md", "ch7_s7.2.md", "ch7_s7.3.md", "ch7_s7.4.md", "ch7_s7.5.md", "ch7_s7.6.md"]},
    8:  {"dir": "CH8",  "title": "Theory of Computation and Computer Graphics", "code": "AEiE08",
         "files": ["ch8_s8.1.md", "ch8_s8.2.md", "ch8_s8.3.md", "ch8_s8.4.md", "ch8_s8.5.md", "ch8_s8.6.md"]},
    9:  {"dir": "CH9",  "title": "Telecommunication and Wireless Communication", "code": "AEiE09",
         "files": ["ch9_s9.1.md", "ch9_s9.2.md", "ch9_s9.3.md", "ch9_s9.4.md", "ch9_s9.5.md", "ch9_s9.6.md"]},
    10: {"dir": "CH10", "title": "Engineering Drawings, Project Management, and Ethics", "code": "AALL10",
         "files": ["ch10_s10.1.md", "ch10_s10.2.md", "ch10_s10.3.md", "ch10_s10.4.md", "ch10_s10.5.md", "ch10_s10.6.md"]},
}

SECTION_NAMES = {
    1: ["Master Roadmap", "Basic Concept (Part 1)", "Basic Concept (Part 2)",
        "Network Theorems", "AC Fundamentals", "Semiconductor Devices",
        "Signal Generators", "Amplifiers"],
    2: ["Number Systems & Boolean Algebra", "Combinational Circuits", "Sequential Logic",
        "Microprocessor 8085", "Microprocessor Systems", "Interrupt Operations"],
    3: ["C Basics", "C Advanced", "C++ Constructs", "OOP Principles",
        "Virtual Functions & Files", "Templates & Exceptions"],
    4: ["CPU & Control Unit", "Computer Arithmetic & Memory", "I/O Organization",
        "Embedded Systems", "RTOS", "HDL & IC Technology"],
    5: ["Network Models", "Data Link Layer", "Network Layer",
        "Transport Layer", "Application Layer", "Network Security"],
    6: ["Static Fields & Maxwell", "Wave Propagation", "Analog Communication",
        "Digital Communication", "Signals & Systems", "DSP"],
    7: ["Data Structures", "Algorithms", "Database Modeling",
        "Transactions", "Operating Systems", "Memory Management"],
    8: ["Finite Automata", "Context-Free Languages", "Turing Machines",
        "CG Basics", "2D Transformations", "3D & Projections"],
    9: ["Cellular Telecom", "Diversity & MIMO", "Switching Systems",
        "Data Switching", "IP Switching & MPLS", "VoIP & NGN"],
    10: ["Engineering Drawing", "Engineering Economics", "Project Planning",
         "Project Management", "Professional Ethics", "Regulatory Bodies"],
}

# LaTeX Conversion

def convert_latex_to_mathml(text):
    def replace_display_math(match):
        latex = match.group(1).strip()
        try:
            mathml = latex2mathml.converter.convert(latex)
            return '<div class="math-block">{}</div>'.format(mathml)
        except Exception:
            return '<div class="math-block"><span class="math-inline">{}</span></div>'.format(latex)

    def replace_inline_math(match):
        latex = match.group(1).strip()
        try:
            return latex2mathml.converter.convert(latex)
        except Exception:
            return '<span class="math-inline">{}</span>'.format(latex)

    text = re.sub(r'\$\$(.*?)\$\$', replace_display_math, text, flags=re.DOTALL)
    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', replace_inline_math, text)
    return text

def convert_latex_to_html_fallback(text):
    text = re.sub(r'\$\$(.*?)\$\$', r'<div class="math-block"><span class="math-inline">\1</span></div>', text, flags=re.DOTALL)
    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', r'<span class="math-inline">\1</span>', text)
    return text

def convert_latex(text):
    if HAS_LATEX2MATHML:
        return convert_latex_to_mathml(text)
    return convert_latex_to_html_fallback(text)

# HTML Processing

def process_github_alerts(html):
    alert_types = {
        '[!NOTE]': 'alert-note',
        '[!TIP]': 'alert-tip',
        '[!IMPORTANT]': 'alert-important',
        '[!WARNING]': 'alert-warning',
        '[!CAUTION]': 'alert-caution',
    }
    for marker, css_class in alert_types.items():
        pattern = r'<blockquote>\s*<p>' + re.escape(marker)
        replacement = '<blockquote class="{}"><p>'.format(css_class)
        html = re.sub(pattern, replacement, html)
    return html

def add_section_breaks(html):
    parts = html.split('<h1')
    if len(parts) > 1:
        result = parts[0]
        for i, part in enumerate(parts[1:], 1):
            if i > 1:
                result += '<div class="section-break"></div><h1' + part
            else:
                result += '<h1' + part
        html = result
    return html

# Page Builders

def build_title_page(chapter_num, chapter_info):
    sections = SECTION_NAMES.get(chapter_num, [])
    section_li = "\n".join("<li>{}</li>".format(s) for s in sections)
    return """
    <div class="title-page">
        <h1>CHAPTER {}</h1>
        <h2>{}</h2>
        <div class="subtitle">
            <p><strong>Complete Textbook for NEC License Examination Preparation</strong></p>
            <p>Electronics, Communication and Information Engineering (AEiE)</p>
        </div>
        <div class="exam-info">
            <p><strong>Nepal Engineering Council</strong></p>
            <p>Registration Examination</p>
            <p>Code: {}</p>
            <br/>
            <ul style="list-style:none;padding:0;text-align:left;display:inline-block;">
                {}
            </ul>
        </div>
    </div>
    """.format(chapter_num, chapter_info["title"], chapter_info["code"], section_li)

def build_toc(chapter_num, chapter_info):
    sections = SECTION_NAMES.get(chapter_num, [])
    items = "\n".join("<li><strong>{}.</strong> {}</li>".format(i, s) for i, s in enumerate(sections, 1))
    return """
    <div class="toc-page">
    <h1>TABLE OF CONTENTS</h1>
    <hr/>
    <h2>Chapter {}: {}</h2>
    <ul style="list-style:none;padding-left:0;">
        {}
    </ul>
    </div>
    """.format(chapter_num, chapter_info["title"], items)

def build_dark_mode_script():
    return """
    <button class="dark-mode-toggle" id="darkModeToggle" title="Toggle dark mode">&#9789;</button>
    <script>
    (function() {
        var toggle = document.getElementById('darkModeToggle');
        var body = document.body;
        var saved = localStorage.getItem('darkMode');
        if (saved === 'true') {
            body.classList.add('dark-mode');
            toggle.innerHTML = '&#9788;';
        }
        toggle.addEventListener('click', function() {
            body.classList.toggle('dark-mode');
            var isDark = body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDark);
            toggle.innerHTML = isDark ? '&#9788;' : '&#9789;';
        });
    })();
    </script>
    """

# Main Build

def read_markdown_files(chapter_dir, files):
    combined = ""
    for fname in files:
        fpath = os.path.join(chapter_dir, fname)
        if not os.path.exists(fpath):
            print("  Warning: {} not found, skipping.".format(fpath))
            continue
        size_kb = os.path.getsize(fpath) / 1024
        print("  Reading: {} ({:.1f} KB)".format(fname, size_kb))
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        combined += content + "\n\n---\n\n"
    return combined

def build_chapter(chapter_num, args):
    info = CHAPTERS[chapter_num]
    chapter_dir = os.path.join(BASE_DIR, info["dir"])

    print("\n" + "=" * 60)
    print("Building Chapter {}: {}".format(chapter_num, info['title']))
    print("=" * 60)

    combined_md = read_markdown_files(chapter_dir, info["files"])
    if not combined_md.strip():
        print("  No content found for Chapter {}. Skipping.".format(chapter_num))
        return None, None

    print("\n  Total markdown: {:.1f} KB".format(len(combined_md)/1024))

    print("  Converting LaTeX to MathML...")
    combined_md = convert_latex(combined_md)

    print("  Converting markdown to HTML...")
    md = markdown.Markdown(
        extensions=['tables', 'fenced_code', 'toc', 'nl2br', 'sane_lists']
    )
    body_html = md.convert(combined_md)

    body_html = process_github_alerts(body_html)
    body_html = add_section_breaks(body_html)

    title_page = build_title_page(chapter_num, info)
    toc = build_toc(chapter_num, info)

    css_content = ""
    if os.path.exists(CSS_FILE):
        with open(CSS_FILE, 'r', encoding='utf-8') as f:
            css_content = f.read()
    else:
        print("  Warning: {} not found. Using minimal CSS.".format(CSS_FILE))
        css_content = "body { font-family: sans-serif; font-size: 11pt; }"

    dark_mode_script = build_dark_mode_script()

    # KaTeX auto-render delimiters need double braces in f-string
    katex_delims = """{
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ]
        }"""

    full_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEC Chapter {ch} -- {title}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {katex_delims});"></script>
    <style>
{css}
    </style>
</head>
<body class="markdown-preview-view">
    {title_page}
    {toc}
    {body}
    {dark_mode}
</body>
</html>""".format(
        ch=chapter_num,
        title=info["title"],
        katex_delims=katex_delims,
        css=css_content,
        title_page=title_page,
        toc=toc,
        body=body_html,
        dark_mode=dark_mode_script
    )

    output_html = os.path.join(BASE_DIR, "NEC_Chapter{}_Complete_Textbook.html".format(chapter_num))
    print("  Saving HTML: {}".format(output_html))
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print("  HTML saved ({:.1f} KB)".format(os.path.getsize(output_html) / 1024))

    output_pdf = None
    if not args.html_only:
        output_pdf = os.path.join(BASE_DIR, "NEC_Chapter{}_Complete_Textbook.pdf".format(chapter_num))
        print("\n  Converting to PDF using WeasyPrint...")
        try:
            from weasyprint import HTML as WeasyHTML
            WeasyHTML(filename=output_html).write_pdf(output_pdf)
            pdf_size = os.path.getsize(output_pdf) / (1024 * 1024)
            print("  PDF saved: {} ({:.2f} MB)".format(output_pdf, pdf_size))
        except Exception as e:
            print("  WeasyPrint failed: {}".format(e))
            print("  HTML file can be opened in browser and printed to PDF.")
            output_pdf = None

    return output_html, output_pdf

def main():
    parser = argparse.ArgumentParser(description="NEC License Exam Textbook Builder")
    parser.add_argument("chapters", nargs="*", type=int,
                        help="Chapter numbers to build (e.g. 1 2 3). Default: all chapters.")
    parser.add_argument("--all", action="store_true", help="Build all 10 chapters")
    parser.add_argument("--html-only", action="store_true", help="Generate HTML only, skip PDF")
    args = parser.parse_args()

    print("=" * 60)
    print("  NEC License Exam -- Textbook Builder")
    print("  LaTeX renderer: {} latex2mathml".format("Using" if HAS_LATEX2MATHML else "No"))
    print("  CSS: {}".format(CSS_FILE))
    print("  Base directory: {}".format(BASE_DIR))
    print("=" * 60)

    if args.all:
        chapters_to_build = sorted(CHAPTERS.keys())
    elif args.chapters:
        chapters_to_build = [c for c in args.chapters if c in CHAPTERS]
        invalid = [c for c in args.chapters if c not in CHAPTERS]
        if invalid:
            print("\nWarning: Invalid chapter numbers: {}. Valid: 1-10".format(invalid))
    else:
        chapters_to_build = sorted(CHAPTERS.keys())

    print("\nChapters to build: {}".format(chapters_to_build))

    results = []
    for ch_num in chapters_to_build:
        html_path, pdf_path = build_chapter(ch_num, args)
        results.append((ch_num, html_path, pdf_path))

    print("\n" + "=" * 60)
    print("  BUILD SUMMARY")
    print("=" * 60)
    for ch_num, html_path, pdf_path in results:
        status = "OK" if html_path else "FAILED"
        html_size = "{:.1f} KB".format(os.path.getsize(html_path)/1024) if html_path else "N/A"
        pdf_size = "{:.2f} MB".format(os.path.getsize(pdf_path)/(1024*1024)) if pdf_path else "Skipped"
        print("  Chapter {}: {} | HTML: {} | PDF: {}".format(ch_num, status, html_size, pdf_size))
    print("=" * 60)

if __name__ == "__main__":
    main()
