with open("adguard-blocklist.txt", "r") as input_file, open("blocklist.txt", "w") as output_file:
    lines = input_file.readlines()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("||"):
            domain = stripped.lstrip("||").split("^")[0]
            output_file.write(domain + "\n")