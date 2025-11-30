import argparse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

print(Path.cwd())

TEMPLATE_DIR = Path("./src/aoc/templates")
BASE_DIR = Path(".")

#
FILES_TO_GENERATE = {
    "__init__.py.j2": "src/aoc/y_{{ year }}/d_{{ day_padded }}/__init__.py",
    "solution.py.j2": "src/aoc/y_{{ year }}/d_{{ day_padded }}/solution.py",
    "examples.py.j2": "src/aoc/y_{{ year }}/d_{{ day_padded }}/examples.py",
}


def scaffold(day: int, year: int):
    # 1. Setup Jinja Environment
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    # 2. Prepare Context (Variables available in filenames AND file content)
    context = {
        "day": str(day),
        "day_padded": f"{day:02d}",  # Ensures '01', '02', etc.
        "year": str(year),
    }

    print(f"🎄 Scaffolding Day {context['day_padded']}, {year}...")

    # 4. Generate Files
    for template_name, output_pattern in FILES_TO_GENERATE.items():
        output_rel_path = env.from_string(output_pattern).render(**context)
        output_path = BASE_DIR / output_rel_path

        print(output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_path.exists():
            print(f"  ⚠️  Skipped: {output_rel_path} (exists)")
            continue
        print(template_name)
        try:
            template = env.get_template(template_name)
            content = template.render(**context)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"  ✅ Created: {output_rel_path}")
        except Exception as e:
            print(f"  ❌ Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    parser.add_argument("--year", type=int, default=2025)
    args = parser.parse_args()

    scaffold(args.day, args.year)
