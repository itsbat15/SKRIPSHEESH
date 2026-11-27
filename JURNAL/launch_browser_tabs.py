import webbrowser
import time
import os

urls = [
    "https://doi.org/10.1145/1593105.1593127",
    "https://doi.org/10.46576/djtechno.v6i2.7139",
    "https://doi.org/10.36040/jati.v8i3.9766",
    "https://doi.org/10.30998/jrami.v4i02.2547",
    "https://www.oreilly.com/library/view/extreme-programming-explained/0321278658/",
    "https://doi.org/10.1145/320434.320440",
    "https://www.mountaingoatsoftware.com/books/user-stories-applied",
    "https://doi.org/10.1007/978-3-662-56509-4",
    "http://hdl.handle.net/10506/647",
    "https://doi.org/10.36040/jati.v8i3.9673",
    "https://ejurnal.swadharma.ac.id/index.php/jris/article/view/1346",
    "https://doi.org/10.24269/mtkind.v14i2.2568",
    "https://doi.org/10.36040/jati.v9i6.15425",
    "http://press.umsida.ac.id/index.php/umsidapress/article/view/978-623-6833-89-6",
    "https://doi.org/10.36040/jati.v10i1.16584",
    "https://doi.org/10.47111/jti.v20i2.24540",
    "https://doi.org/10.25126/jtiik.201851610",
    "https://www.pearson.com/en-us/subject-catalog/p/management-information-systems-managing-the-digital-firm/P200000003253",
    "https://doi.org/10.11591/eecsi.v5.1701",
    "https://jtiik.ub.ac.id/index.php/jtiik/article/view/9798",
    "https://doi.org/10.22146/jpkm.100850",
    "https://peraturan.bpk.go.id/Details/43920/uu-no-20-tahun-2003",
    "https://doi.org/10.36040/jati.v10i2.17328",
    "https://doi.org/10.47233/jteksis.v7i4.2260",
    "https://iansommerville.com/software-engineering-book/",
    "https://doi.org/10.54367/means.v6i2.1450",
    "https://doi.org/10.28932/jutisi.v11i2.10713",
    "https://journal.maranatha.edu/index.php/jutisi/article/view/603",
    "https://doi.org/10.62712/juktisi.v4i3.675",
    "https://doi.org/10.28932/jutisi.v6i3.3047",
    "https://doi.org/10.24076/joism.2026v7i2.2453",
    "https://jutif.if.unsoed.ac.id/index.php/jurnal/article/view/227",
    "https://doi.org/10.25126/jtiik.2023107237",
    "https://doi.org/10.33050/ccit.v3i3.704",
    "https://doi.org/10.28932/jutisi.v9i1.5979"
]

print("Membuka 35 tab di peramban utama...")
# First open the portal dashboard
dashboard = os.path.abspath(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\buka_semua_jurnal.html")
webbrowser.open_new_tab("file:///" + dashboard.replace("\\", "/"))
time.sleep(1.0)

for idx, u in enumerate(urls, 1):
    print(f"[{idx}/35] Membuka: {u}")
    webbrowser.open_new_tab(u)
    time.sleep(0.3)

print("Selesai! Seluruh 35 tautan berhasil dikirim ke peramban.")
