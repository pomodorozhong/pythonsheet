def line_slice(in_path, out_path, start: int, end: int):
    with open(in_path, "r") as input:
        with open(out_path, "w") as out:
            for i, line in enumerate(input):
                if i >= start and i < end:
                    out.write(line)
