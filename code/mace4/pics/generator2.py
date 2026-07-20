from pathlib import Path

OUTPUT_DIR = Path("mace4_inputs")
OUTPUT_DIR.mkdir(exist_ok=True)

HEADER = """\
assign(start_size,2).
assign(end_size,8).

op(400,infix,"^").
op(500,infix,"+").
"""

AXIOMS = {
    "M0": [
        "x ^ x = x."
    ],

    "M1": [
        "x ^ (y ^ z) = (x ^ y) ^ z."
    ],

    "M2": [
        "x ^ y = y ^ x."
    ],

    "M3": [
        "x ^ em = x."
    ],

    "S1": [
        "x + (y + z) = (x + y) + z."
    ],

    "S2": [
        "x + y = y + x."
    ],

    "S3": [
        "x + ez = x."
    ],

    "SM1": [
        "x + (y ^ z) = (x + y) ^ (x + z)."
    ],

    "SM2": [
        "x + em = em."
    ],

    "P": [
        "star(star(x)) = x."
    ],

    # PM phải là một công thức duy nhất
    "PM": [
        "(x ^ y = x) <-> "
        "(star(y) ^ star(x) = star(y))."
    ],
}


def build_assumptions(excluded=None):
    lines = ["formulas(assumptions).", ""]

    for name, formulas in AXIOMS.items():
        if name == excluded:
            continue

        lines.append(f"% {name}")
        lines.extend(formulas)
        lines.append("")

    lines.append("end_of_list.")
    return lines


def write_full():
    lines = [
        HEADER,
        "",
        *build_assumptions(),
        "",
    ]

    output_file = OUTPUT_DIR / "PICS_full.in"
    output_file.write_text("\n".join(lines), encoding="utf-8")


def write_independence(removed_axiom):
    lines = [
        HEADER,
        "",
        *build_assumptions(excluded=removed_axiom),
        "",
        "formulas(goals).",
        "",
        f"% Test independence of {removed_axiom}",
        *AXIOMS[removed_axiom],
        "",
        "end_of_list.",
        "",
    ]

    output_file = OUTPUT_DIR / f"without_{removed_axiom}.in"
    output_file.write_text("\n".join(lines), encoding="utf-8")


def main():
    write_full()

    for axiom_name in AXIOMS:
        write_independence(axiom_name)

    print(
        f"Generated {len(AXIOMS) + 1} files "
        f"in: {OUTPUT_DIR.resolve()}"
    )


if __name__ == "__main__":
    main()