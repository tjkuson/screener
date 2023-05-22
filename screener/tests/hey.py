from ebooklib import epub

def main():
    book = epub.read_epub("william-shakespeare_richard-ii.epub", options={"ignore_ncx": True})

if __name__ == "__main__":
    main()