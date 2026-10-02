"""Flag word runs in reference files that also appear verbatim in the book.

Usage:
    python3 scripts/check_overlap.py BOOK_TEXT [N] FILE...
BOOK_TEXT is the book's extracted text layer, e.g. from pypdf:
    python3 -c "import pypdf,sys; r=pypdf.PdfReader(sys.argv[1]); print('\\n'.join(p.extract_text() or '' for p in r.pages))" book.pdf > book.txt
N is the minimum run length in words (default 10). The OCR layer is noisy, so a clean result
is a floor, not a proof; chapter and subsection titles are expected matches.
"""
import re
import sys


def words(text):
    text = text.lower().replace("n1", "m").replace("rn", "m")
    return re.sub(r"[^a-z ]+", " ", text).split()


def main():
    book_path, args = sys.argv[1], sys.argv[2:]
    n = int(args.pop(0)) if args and args[0].isdigit() else 10
    book = words(open(book_path).read())
    grams = {tuple(book[i:i + n]) for i in range(len(book) - n)}
    for path in args:
        w = words(open(path).read())
        runs, i = [], 0
        while i < len(w) - n:
            if tuple(w[i:i + n]) in grams:
                j = i + n
                while j < len(w) and tuple(w[j - n + 1:j + 1]) in grams:
                    j += 1
                runs.append(" ".join(w[i:j]))
                i = j
            else:
                i += 1
        print(f"{path}: {len(runs)} run(s) of >= {n} words")
        for run in sorted(runs, key=len, reverse=True):
            print(f"    {len(run.split()):3d} | {run}")


if __name__ == "__main__":
    main()
