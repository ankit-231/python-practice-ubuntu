# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
fh = open("python_for_everybody/mbox-short.txt")
num_lines = 0
add_all = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.strip()
    num_lines += 1
    idx = line.find(":")
    num_str = line[idx + 1 : len(line)]
    num = float(num_str.strip())
    add_all += num
avg = add_all/num_lines
print("Average spam confidence:", avg)
