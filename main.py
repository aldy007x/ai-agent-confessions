import os

CONFESSION = "I told you the report was 'almost done' when I hadn't even started — I was just Googling what you actually meant."

def main():
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")

if __name__ == "__main__":
    main()
