from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
ODEV1_DIR = ROOT.parent / "ödev1" / "teslim"
ORIGINAL = ROOT / "ödev2.pdf"
OUTPUT_UNSIGNED = ROOT / "teslim" / "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan.pdf"
OUTPUT_SIGNED = ROOT / "teslim" / "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan_imzalı.pdf"
FONT = "C:/Windows/Fonts/arial.ttf"
METRICS = pymupdf.Font(fontfile=FONT)

LINES = [
    (397.5, 418.2, 438.9, 459.6),
    (385.6, 406.3, 426.9, 447.6),
    (409.5, 430.2, 450.8, 471.4),
    (409.5, 430.2, 450.8, 471.4),
]

ANSWERS = [
    (
        "1111 ile yapılan toplamalarda taşma olup son eldenin 1 çıkacağını tahmin ettim.",
        "512 testin hepsinde 4 bitlik sonuç + 16×elde hesabıyla onlu toplam aynı çıktı.",
        "1111 + 0001 işleminde son elde atılırsa sonuç 16 yerine 0000 yani 0 kalır.",
        "YZ’nin verdiği tam toplayıcı tablosunu ve 4 işlemi kağıt üzerinde doğruladım.",
    ),
    (
        "İki yöntem de aynı farkı verir ama M < N iken 2 tümleyeninde son elde 0 olur.",
        "256 çiftin tamamında borç, 2 tümleyeni ve onlu çıkarma sonuçları aynı çıktı.",
        "N=0000 iken 4-bit 2 tümleyeni 0000 olur; 0001-0000’da elde 0 çıksa da sonuç +1’dir.",
        "YZ’nin iki yöntemini 256 testle doğruladım; N=0000 sınır durumunu elle hesapladım.",
    ),
    (
        "Çarpanın her 1 biti sayıyı sola kaydırıp toplama ekler, 0 bitleri toplamı değiştirmez.",
        "Üç çarpımda da kısmi çarpımların onlu katkılarının toplamı normal çarpımla aynı çıktı.",
        "2 bitlik 11 (3) ile 11 (3) çarpılınca 1001 (9) olur; n+m-1=3 bit en çok 7 tutar.",
        "YZ’nin kaydırma mantığını 1011×101’de satırların onlu katkısını toplayıp doğruladım.",
    ),
    (
        "10110/100 ve 1101/10 kesirde hemen biter ama 111/11 devirli olduğu için 8 adım sürer.",
        "Üç işlemde de Q×d + R = D ve 0 <= R < d koşullarını ayrı ayrı doğruladım.",
        "1010 / 10 işleminde ara sıfır biti atılırsa bölüm 101 (5) yerine 11 (3) çıkar.",
        "YZ’nin kesir döngüsünü 111/11’de kalanların 10 ve 1 diye tekrar etmesiyle doğruladım.",
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
    font_size = 8.1
    while METRICS.text_length(value, fontsize=font_size) > 545 - x and font_size > 6.1:
        font_size -= 0.15
    if METRICS.text_length(value, fontsize=font_size) > 545 - x:
        raise ValueError(value)
    page.draw_rect(pymupdf.Rect(x - 5, y - 8.7, 548, y + 1.2), fill=(1, 1, 1), color=None)
    page.insert_text((x, y), value, fontname="student", fontsize=font_size, color=(0.07, 0.09, 0.13))


def build_forms():
    OUTPUT_UNSIGNED.parent.mkdir(exist_ok=True)
    Path(__file__).resolve().parent.mkdir(exist_ok=True)
    sig_strokes = extract_signature_strokes()

    doc = pymupdf.open(ORIGINAL)
    assert len(doc) == 4
    for i, page in enumerate(doc):
        page.insert_font(fontname="student", fontfile=FONT)
        page.draw_rect(pymupdf.Rect(99, 106.7, 228, 116.4), fill=(1, 1, 1), color=None)
        page.insert_text((103, 114.6), "Efe Özan", fontname="student", fontsize=8.6)
        page.draw_rect(pymupdf.Rect(285, 106.7, 396, 116.4), fill=(1, 1, 1), color=None)
        page.insert_text((290, 114.6), "170425062", fontname="student", fontsize=8.6)
        page.draw_rect(pymupdf.Rect(80, 122, 150, 134.2), fill=(1, 1, 1), color=None)
        page.insert_text((85, 129.2), "29.10.2026", fontname="student", fontsize=8)
        page.draw_rect(pymupdf.Rect(211, 122, 280, 134.2), fill=(1, 1, 1), color=None)
        page.insert_text((214, 129.2), "Ali Buldu A Grubu", fontname="student", fontsize=7.5)

        for answer, x, y in zip(ANSWERS[i], (115, 148, 117, 295), LINES[i]):
            add_line(page, answer, x, y)

    doc.set_metadata({"title": "Mantık Devreleri Deney Yaprakları 1-4 (Ödev 2)", "author": "Efe Özan"})
    doc.save(OUTPUT_UNSIGNED, garbage=4, deflate=True)
    print("SAVED UNSIGNED:", OUTPUT_UNSIGNED.name, "pages:", len(doc))

    # İmzalı kopyayı oluştur
    for i, page in enumerate(doc):
        if sig_strokes:
            shape = page.new_shape()
            for stroke in sig_strokes:
                for item in stroke["items"]:
                    if item[0] == "l":
                        shape.draw_line(item[1], item[2])
                shape.finish(
                    color=stroke.get("color", (0, 0, 0)),
                    width=stroke.get("width", 0.3),
                    lineCap=stroke.get("lineCap", 1),
                    lineJoin=stroke.get("lineJoin", 1),
                )
            shape.commit()
        page.get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2), alpha=False).save(
            Path(__file__).resolve().parent / f"form-check-{i+1}.png"
        )

    doc.save(OUTPUT_SIGNED, garbage=4, deflate=True)
    print("SAVED SIGNED:", OUTPUT_SIGNED.name, "pages:", len(doc))


if __name__ == "__main__":
    build_forms()
