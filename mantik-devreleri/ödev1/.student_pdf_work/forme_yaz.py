from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parent.parent
ORIGINAL = ROOT / 'mantık_devre_odev_1.pdf'
OUTPUT = ROOT / 'teslim/BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan.pdf'
FONT = 'C:/Windows/Fonts/arial.ttf'
METRICS = pymupdf.Font(fontfile=FONT)

LINES = [
    (440.7, 461.0, 481.6, 502.0),
    (408.7, 429.2, 449.5, 470.3),
    (380.5, 401.0, 422.0, 442.5),
    (416.5, 438.0, 459.0, 479.5),
    (474.2, 494.7, 515.5, 536.0),
    (507.8, 528.4, 548.8, 569.1),
    (421.1, 442.0, 462.9, 483.2),
]

ANSWERS = [
    (
        'Tam sayıyı çevirmek kolay olur ama kesir kısmı zorlayabilir diye düşündüm.',
        '101101.01101 ve 2D.68 sayıları onlukta 45.40625 ediyor.',
        'Program iki tarafta da aynı yanlışı yaparsa eski sayıyı yine verebilir.',
        'Kod kısmında YZ’den yardım aldım. Sonuçları elle de kontrol ettim.',
    ),
    (
        '12 bit pek yetmeyecek gibi geldi. Hem 1000 var hem de adım çok küçük.',
        '8001 değer var, 12 bit ise 4096 değer tutuyor. 13 bit gerekiyor.',
        '10 tam ve 2 kesir biti seçilirse 0.125 yerine en küçük adım 0.25 olur.',
        'Bit hesabında YZ’den de yardım aldım. İki farklı yoldan kontrol ettim.',
    ),
    (
        'Sıfırları doğru tarafa koyarsam sayı değişmez diye düşündüm.',
        'İkili, sekizli ve onaltılı hâllerini onluğa çevirdim; hepsi 45.40625.',
        'Kesrin soluna sıfır koyunca 2D.68 yerine 2D.0D çıkıyor.',
        'Gruplarken YZ’den yardım aldım. Sıfırların yerlerini tekrar kontrol ettim.',
    ),
    (
        '0.625 hemen biter, 0.1 ise uzar diye tahmin ettim.',
        '8 basamağı geri onluğa çevirdim. Yalnız 0.625 tam çıktı.',
        '0.1 sayısının paydası 10, yani içinde 5 var; ikilide bitmiyor.',
        'YZ’den de yardım aldım. Sayıları onluğa çevirip kontrol ettim.',
    ),
    (
        'A ve B bana tam eşit görünmedi. C’de de sıfırlar karışmış olabilir.',
        'A’nın farkı 0.025, B’nin 0.000146484375, C’nin 0.35546875 çıktı.',
        '101 ikilide 5; sağına 0 ekleyince 1010, yani 10 oluyor.',
        'YZ’den yardım aldım. Dört ifadeyi de tek tek onluğa çevirdim.',
    ),
    (
        'Üç kayıtta da aynı sayıyı veren bir taban seçimi vardır diye düşündüm.',
        'A onluk, B sekizli, C ikili olursa hepsi 17 oluyor. Başka seçenek yok.',
        '17 hem 8 hem 10 tabanında yazılabilir; hangisi olduğu belli değil.',
        'Tabanları kontrol ederken YZ’den yardım aldım. Diğerlerini de denedim.',
    ),
    (
        'Soldaki bir bit değişirse sayı daha çok etkilenir diye düşündüm.',
        '8 biti ayrı ayrı değiştirdim; yalnız 237, 0-200 aralığını aştı.',
        'En soldaki 1 sıfır olunca 173 sayısı 45’e iniyor, artmıyor.',
        'YZ’den yardım aldım. Her bitin sayıyı ne kadar değiştirdiğine baktım.',
    ),
]


def add_line(page, value, x, y):
    font_size = 8.1
    while METRICS.text_length(value, fontsize=font_size) > 545-x and font_size > 6.1:
        font_size -= 0.15
    if METRICS.text_length(value, fontsize=font_size) > 545-x:
        raise ValueError(value)
    page.draw_rect(pymupdf.Rect(x-5, y-8.7, 548, y+1.2), fill=(1,1,1), color=None)
    page.insert_text((x, y), value, fontname='student', fontsize=font_size,
                     color=(0.07,0.09,0.13))


OUTPUT.parent.mkdir(exist_ok=True)
doc = pymupdf.open(ORIGINAL)
assert len(doc) == 7
for i, page in enumerate(doc):
    page.insert_font(fontname='student', fontfile=FONT)
    # Boş alanlardaki noktalı çizgileri baştan sona kapat.
    page.draw_rect(pymupdf.Rect(99,106.7,228,116.4), fill=(1,1,1),color=None)
    page.insert_text((103,114.6),'Efe Özan',fontname='student',fontsize=8.6)
    page.draw_rect(pymupdf.Rect(285,106.7,396,116.4), fill=(1,1,1),color=None)
    page.insert_text((290,114.6),'170425062',fontname='student',fontsize=8.6)
    page.draw_rect(pymupdf.Rect(80,122,150,134.2),fill=(1,1,1),color=None)
    page.insert_text((85,129.2),'12.10.2026',fontname='student',fontsize=8)
    # Şube/Grup alanını doldur; hemen sağındaki imza çizgisine dokunma.
    page.draw_rect(pymupdf.Rect(211,122,280,134.2),fill=(1,1,1),color=None)
    page.insert_text((214,129.2),'Ali Buldu A Grubu',fontname='student',fontsize=7.5)
    for answer,x,y in zip(ANSWERS[i],(115,148,117,295),LINES[i]):
        add_line(page,answer,x,y)
    page.get_pixmap(matrix=pymupdf.Matrix(1.2,1.2),alpha=False).save(
        ROOT / '.student_pdf_work' / f'form-check-{i+1}.png')
doc.set_metadata({'title':'Mantık Devreleri Deney Yaprakları 1-7','author':'Efe Özan'})
doc.save(OUTPUT,garbage=4,deflate=True)
print('SAVED',OUTPUT.name,'pages',len(doc))
