# === Stage 32: Add pagination helpers for long console output ===
# Project: BillWatch
def paginate(text, page_size=60):
    pages = []
    for i in range(0, len(text), page_size):
        pages.append(text[i:i+page_size])
    return pages

def print_paged(text, page_size=60):
    pages = paginate(text, page_size)
    for i, page in enumerate(pages, 1):
        print(f"--- Page {i} ---")
        print(page)
        print()

def get_page_count(text, page_size=60):
    return len(paginate(text, page_size))

def truncate(text, max_length=60):
    if len(text) <= max_length:
        return text
    return text[:max_length] + "\n..."

def format_summary(text):
    return "\n".join(truncate(line) for line in text.split("\n"))
