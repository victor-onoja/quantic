def convert_sbv_to_srt(sbv_path, srt_path):
    with open(sbv_path, 'r') as sbv_file:
        lines = sbv_file.read().splitlines()

    srt_lines = []
    counter = 1
    i = 0
    while i < len(lines):
        if lines[i].strip() == "":
            i += 1
            continue

        # Timestamp line
        if ',' in lines[i]:
            start, end = lines[i].split(',')
            start = start.strip().replace('.', ',')
            end = end.strip().replace('.', ',')
            i += 1
            text_lines = []
            while i < len(lines) and lines[i].strip() != "":
                text_lines.append(lines[i])
                i += 1
            srt_lines.append(f"{counter}\n{start} --> {end}\n" + "\n".join(text_lines) + "\n")
            counter += 1
        i += 1

    with open(srt_path, 'w') as srt_file:
        srt_file.writelines(srt_lines)

# Example usage
convert_sbv_to_srt("captions (2).sbv", "captions(2).srt")
