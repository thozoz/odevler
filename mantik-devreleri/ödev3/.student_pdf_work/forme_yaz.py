from pathlib import Path
import os
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
ODEV1_DIR = ROOT.parent / "ödev1" / "teslim"
ORIGINAL = ROOT / "ödev3.pdf"
OUTPUT_UNSIGNED = ROOT / "teslim" / "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan.pdf"
OUTPUT_SIGNED = ROOT / "teslim" / "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan_imzalı.pdf"

# Font seçimi: Linux'ta Arimo / Liberation Sans, Windows'ta Arial
if os.path.exists("/usr/share/fonts/truetype/croscore/Arimo-Regular.ttf"):
    FONT = "/usr/share/fonts/truetype/croscore/Arimo-Regular.ttf"
elif os.path.exists("C:/Windows/Fonts/arial.ttf"):
    FONT = "C:/Windows/Fonts/arial.ttf"
else:
    FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

METRICS = pymupdf.Font(fontfile=FONT)

LINES = [
    (393.0, 414.2, 435.5, 456.7),
    (397.0, 418.2, 439.5, 460.7),
    (395.0, 416.2, 437.5, 458.7),
    (514.5, 535.7, 557.0, 578.2),
]

ANSWERS = [
    (
        "Artı-3 ve Aiken'de bitler terslendiğinde 9 tümleyeninin elde edileceğini, BCD'de ise bozulacağını öngördüm.",
        "48 ve 003 dönüşümlerini elle yazıp kodla eşleştirdim; 16 desenin 10 geçerli, 6 geçersiz kümesini doğruladım.",
        "BCD d=2 (0010) tersi 1101 olup BCD'de geçersizdir; Aiken 0101 ağırlığı 5 olsa da sözlükte yer almaz.",
        "YZ'nin Aiken tablosunu ve 0101'in reddini kağıt üzerinde doğruladım.",
    ),
    (
        "0-15 Gray kodunda 15->0 geçişinde tek bit değişeceğini, 0-9'da kesilirse komşuluğun bozulacağını öngördüm.",
        "0-15 arası 15 ardışık geçişte Hamming mesafesinin tam 1 olduğunu ve 15->0'da 1 bit kaldığını doğruladım.",
        "9->0 geçişinde 3 bit (1101 vs 0000) değişir; Gray 1100'da hatalı yöntem 1010 verirken doğru ikili 1000'dir.",
        "YZ'nin Gray->İkili kuralını 1100 örneğinde adım adım doğruladım.",
    ),
    (
        "Tek bit hatalarının %100 saptanacağını, iki bit hatalarında ise birler kayarsa hataların kaçacağını öngördüm.",
        "50 tek bit hatasının 50'sinin de saptandığını, 100 iki bit hatasından 60'ının başka rakama dönüşüp kaçtığını doğruladım.",
        "Rakam 0 (11000) 0. ve 2. bitler terslenirse 01100 (6) olup kaçar; çift eşlik 11000011'de 28 iki bit hatası kaçar.",
        "YZ'nin hata tarama sonucunu 11000->01100 geçişinde doğruladım.",
    ),
    (
        "Code 128'in boşluk ve önemsiz sıfırları ayrı karakter olarak koruyacağını, bağımsız okuyucuyla okunacağını öngördüm.",
        "HELP 2031, HELP2031, 000123 ve 123 dizilerini python-barcode ile üretip pyzbar ile karakter karakter doğruladım.",
        "ASCII->EBCDIC'te MSB ekleme L (4C->CC!=D3) ve 0'da (30->B0!=F0) çöker; küçültülen barkodda okuma %0'a düşer.",
        "YZ'nin barkod okuma önerisini pyzbar ile test edip doğruladım.",
    ),
]


def extract_signature_strokes():
    unsigned_p = ODEV1_DIR / "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan.pdf"
    signed_p = ODEV1_DIR / "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan_imzalı.pdf"
    if not (unsigned_p.is_file() and signed_p.is_file()):
        return []
    with pymupdf.open(unsigned_p) as d1, pymupdf.open(signed_p) as d2:
        n_base = len(d1[0].get_drawings())
        return d2[0].get_drawings()[n_base:]


def add_line(page, value, x, y):
    font_size = 7.8
    while METRICS.text_length(value, fontsize=font_size) > 545 - x and font_size > 5.5:
        font_size -= 0.1
    if METRICS.text_length(value, fontsize=font_size) > 545 - x:
        raise ValueError(f"Metin çok uzun: {value}")
    # Noktalı çizgiyi beyaz dikdörtgenle örtüp üzerine yaz
    page.draw_rect(pymupdf.Rect(x - 3, y - 8.5, 548, y + 1.5), fill=(1, 1, 1), color=None)
    page.insert_text((x, y), value, fontname="student", fontsize=font_size, color=(0.07, 0.09, 0.13))


def build_forms():
    OUTPUT_UNSIGNED.parent.mkdir(parents=True, exist_ok=True)
    Path(__file__).resolve().parent.mkdir(parents=True, exist_ok=True)
    sig_strokes = extract_signature_strokes()

    doc = pymupdf.open(ORIGINAL)
    assert len(doc) == 4
    for i, page in enumerate(doc):
        page.insert_font(fontname="student", fontfile=FONT)
        # Noktalı alanları tamamen ört; değerleri etiketlerle aynı taban çizgisine yaz.
        page.draw_rect(pymupdf.Rect(103, 108, 235, 121), fill=(1, 1, 1), color=None)
        page.insert_text((106, 118.3872), "Efe Özan", fontname="student", fontsize=8.6)
        page.draw_rect(pymupdf.Rect(292, 108, 395, 121), fill=(1, 1, 1), color=None)
        page.insert_text((295, 118.3872), "170425062", fontname="student", fontsize=8.6)
        page.draw_rect(pymupdf.Rect(82, 122, 155, 135), fill=(1, 1, 1), color=None)
        page.insert_text((85, 132.6096), "10.11.2026", fontname="student", fontsize=8.0)
        page.draw_rect(pymupdf.Rect(216, 122, 290, 135), fill=(1, 1, 1), color=None)
        page.insert_text((218, 132.6096), "Ali Buldu A Grubu", fontname="student", fontsize=7.5)

        for answer, x, y in zip(ANSWERS[i], (115, 148, 123, 303), LINES[i]):
            add_line(page, answer, x, y)

    doc.set_metadata({"title": "Mantık Devreleri Deney Yaprakları 1-4 (Ödev 3)", "author": "Efe Özan"})
    doc.save(OUTPUT_UNSIGNED, garbage=4, deflate=True)
    print("SAVED UNSIGNED:", OUTPUT_UNSIGNED.name, "pages:", len(doc))

    # İmzalı kopyayı oluştur
    dx, dy = 12.0, 0.0
    for i, page in enumerate(doc):
        if sig_strokes:
            shape = page.new_shape()
            for stroke in sig_strokes:
                for item in stroke["items"]:
                    if item[0] == "l":
                        p1 = pymupdf.Point(item[1][0] + dx, item[1][1] + dy)
                        p2 = pymupdf.Point(item[2][0] + dx, item[2][1] + dy)
                        shape.draw_line(p1, p2)
                line_cap = stroke.get("lineCap", 1)
                if isinstance(line_cap, (list, tuple)):
                    line_cap = line_cap[0]
                line_join = stroke.get("lineJoin", 1)
                if isinstance(line_join, (list, tuple)):
                    line_join = line_join[0]
                shape.finish(
                    color=stroke.get("color", (0, 0, 0)),
                    width=stroke.get("width", 0.3),
                    lineCap=int(line_cap),
                    lineJoin=int(line_join),
                )
            shape.commit()
        page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False).save(
            Path(__file__).resolve().parent / f"form-check-{i+1}.png"
        )

    doc.save(OUTPUT_SIGNED, garbage=4, deflate=True)
    print("SAVED SIGNED:", OUTPUT_SIGNED.name, "pages:", len(doc))


if __name__ == "__main__":
    build_forms()
