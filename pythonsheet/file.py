def line_slice(in_path, out_path, start: int, end: int):
    with open(in_path, "r") as input:
        with open(out_path, "w") as out:
            for i, line in enumerate(input):
                if i >= start and i < end:
                    out.write(line)


def replace_a_char_each_line(file_in, file_out, char_index: int, replace_with):
    with open(file_in) as fp:
        lines_to_be_replace = fp.read().splitlines()

    with open(file_out, "w") as fp:
        for line in lines_to_be_replace:
            if len(line) > char_index:
                char_list = list(line)
                char_list[char_index] = replace_with
                modifid_line = ''.join(char_list)
                print(modifid_line, file=fp)
            else:
                print(line, file=fp)


def replace_a_char_series_each_line(file_in, file_out, start_index: int, end_index: int, replace_with):
    if end_index < start_index:
        raise Exception("end_index < start_index")

    with open(file_in) as fp:
        lines_to_be_replace = fp.read().splitlines()

    with open(file_out, "w") as fp:
        for line in lines_to_be_replace:
            if len(line) > end_index:
                char_list = list(line)
                left = char_list[:start_index]
                right = char_list[end_index+1:]
                modifid_line = ''.join(left) + replace_with + ''.join(right)
                print(modifid_line, file=fp)
            else:
                print(line, file=fp)
