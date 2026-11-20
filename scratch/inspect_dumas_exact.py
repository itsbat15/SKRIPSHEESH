with open('JURNAL/36_REFERENSI_TXT/Dumas_dkk_2018_Fundamentals_of_BPM.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== HALAMAN ')

def show_page_snippet(pdf_page, title):
    content = pages[pdf_page].encode('ascii', errors='replace').decode('ascii')
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    print(f"==================================================")
    print(f"=== {title} (PDF Page {pdf_page}) ===")
    print("\n".join(lines[:25]))
    print(f"==================================================\n")

show_page_snippet(101, "Section 3.1 First Steps with BPMN (Book page 75)")
show_page_snippet(102, "Section 3.1 First Steps with BPMN (Book page 76)")
show_page_snippet(106, "Section 3.2.1 Exclusive Decisions (Book page 80)")
show_page_snippet(108, "Section 3.2.2 Parallel Execution (Book page 82)")
show_page_snippet(122, "Section 3.4 Resources / Pools & Lanes (Book page 96)")
show_page_snippet(123, "Section 3.4 Resources / Pools & Lanes (Book page 97)")
show_page_snippet(127, "Section 3.4 Message Flows (Book page 101)")
show_page_snippet(148, "Section 4.2 Handling Events / Intermediate Events (Book page 123)")

