
import subprocess
import os
import time


def main():
    sub = subprocess.Popen("pip list -o", shell=True, stdout=subprocess.PIPE)
    print("pip list -o")
    sub.wait()
    ret = sub.stdout.read()
    ret = bytes.decode(ret, "utf-8")
    print(ret)
    print("\n")
    lines = ret.split(os.linesep)
    with open("update_list.txt", "w", encoding="utf8") as output_file:
        for line in lines:
            line = line.strip()
            if line.startswith("Package") or line.startswith("--------"):
                continue
            buf = line.split(" ")[0].strip()
            output_file.write(buf)
            output_file.write("\n")
    sub = subprocess.Popen("pip install -U -r update_list.txt", shell=True)
    ret = sub.wait()
    if ret != 0:
        print("Did not updated all!")
    else:
        print("Enjoy it!!!!!!!!")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("It costs %ds.\n" % (end - start))