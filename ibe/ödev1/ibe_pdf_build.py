from pathlib import Path
import pymupdf as fitz

home = Path.home()
folder = home / 'Downloads'
out = folder / 'IBE_Tasarim_Problemi.pdf'
if out.exists():
    out = folder / 'IBE_Tasarim_Problemi_v2.pdf'
    if out.exists():
        raise RuntimeError('PDF hedefi zaten mevcut; üzerine yazılmadı.')
font_regular = 'C:/Windows/Fonts/arial.ttf'
font_bold = 'C:/Windows/Fonts/arialbd.ttf'
fonts = {'regular': fitz.Font(fontfile=font_regular), 'bold': fitz.Font(fontfile=font_bold)}
doc = fitz.open()
ink = (0.13, 0.15, 0.16)
muted = (0.38, 0.41, 0.42)
accent = (0.30, 0.39, 0.22)

def text(page, value, x, y, width, size=10.5, bold=False, color=ink, leading=None):
    key = 'bold' if bold else 'regular'
    leading = leading or size * 1.4
    for paragraph in value.split('\n'):
        words = paragraph.split()
        line = ''
        for word in words:
            candidate = (line + ' ' + word).strip()
            if fonts[key].text_length(candidate, fontsize=size) > width and line:
                page.insert_text((x, y), line, fontname=key, fontsize=size, color=color)
                y += leading
                line = word
            else:
                line = candidate
        if line:
            page.insert_text((x, y), line, fontname=key, fontsize=size, color=color)
            y += leading
        else:
            y += leading * 0.5
    return y

def base(number, subtitle):
    p = doc.new_page(width=595.28, height=841.89)
    p.insert_font(fontname='regular', fontfile=font_regular)
    p.insert_font(fontname='bold', fontfile=font_bold)
    text(p, 'İnsan Bilgisayar Etkileşimi ve Görsellik · 2026 Güz', 40, 42, 515, 9, color=muted)
    text(p, 'Lehim ve Sıcak Hava İstasyonunda', 40, 77, 515, 19, True)
    text(p, 'Kontrol ve Gösterge Belirsizliği', 40, 103, 515, 19, True)
    text(p, subtitle, 40, 135, 515, 12, True, accent)
    p.draw_line((40, 150), (555, 150), color=(0.80, 0.82, 0.79), width=0.7)
    p.draw_line((40, 794), (555, 794), color=(0.80, 0.82, 0.79), width=0.7)
    text(p, 'Günlük kullanımda karşılaşılan bir arayüz probleminin incelenmesi', 40, 810, 475, 8, color=muted)
    text(p, str(number) + ' / 2', 524, 810, 40, 8, color=muted)
    return p

p = base(1, '1. Orijinal tasarım ve yaşadığım sorun')
p.insert_image(fitz.Rect(40, 168, 300, 519.5), filename=str(folder / 'ibe default.png'))
text(p, 'Fotoğraf 1. Cihazın orijinal hâli.', 40, 537, 260, 8.5, color=muted)
y = text(p, 'Cihaz hakkında', 320, 180, 235, 12, True)
y = text(p, 'Kullandığım YIHUA 878D cihazında hem lehim havyası hem de sıcak hava tabancası var. İkisinin düğmeleri aynı panelde bulunuyor. Fakat hangi düğmenin hangisine ait olduğu ilk bakışta anlaşılmıyor.', 320, y + 5, 235)
y = text(p, 'Yazılar yeterince açık değil', 320, y + 15, 235, 12, True)
y = text(p, 'Ekranın altında TEMP yazıyor ama sıcaklığın hangi cihaza ait olduğu yazmıyor. HEATER ışığının lehimin ısınmasını gösterdiği de belli değil. AIR yazan düğmenin hava hızını ayarladığını kullanınca anladım.', 320, y + 5, 235)
y = text(p, 'Yerleşim kafa karıştırıyor', 320, y + 15, 235, 12, True)
y = text(p, 'HEATER ışığı ekranın hemen altında olduğu için ikisinin aynı cihaza ait olduğunu düşündüm. Oysa ekran sıcak havanın sıcaklığını, ışık ise lehimin ısınmasını gösteriyor. Alttaki açma kapama düğmelerinde de hangisini açtıkları yazmıyor.', 320, y + 5, 235)
y = text(p, 'İlk kullanımda ne yaşadım?', 40, 582, 515, 12, True)
y = text(p, 'İlk başta ekrandaki sıcaklığı lehimin sıcaklığı sandım. Yeşil tuşların sıcak havayı mı yoksa lehimi mi ayarladığını anlayamadım. HEATER ışığı ve sağdaki sıcaklık düğmesi için de aynı karışıklığı yaşadım. AIR düğmesini çevirince hava hızını değiştirdiğini fark ettim. Açma kapama düğmelerinin neyi açtığını ise yanlarındaki kablo bağlantılarına bakarak anladım.', 40, y + 5, 515)
y = text(p, 'Bu neden bir tasarım sorunu?', 40, y + 14, 515, 12, True)
y = text(p, 'Cihazın düğmelerini anlamak için deneme yanılma yapmak zorunda kaldım. Hangi düğmenin ne işe yaradığı daha açık yazılsaydı ilk kullanım daha kolay olurdu. Sorun cihazın çalışmasında değil, düğmelerin ve yazıların nasıl yerleştirildiğinde.', 40, y + 5, 515)
assert y < 780, y

p = base(2, '2. Nasıl düzeltirdim?')
p.insert_image(fitz.Rect(40, 168, 300, 519.5), filename=str(folder / 'ibe ödev bitt.png'))
text(p, 'Fotoğraf 2. Photoshop ile düzenlediğim hâli.', 40, 537, 260, 8.5, color=muted)
y = text(p, 'İki bölüme ayırdım', 320, 180, 235, 12, True)
y = text(p, 'Beyaz bir çizgi çizerek sıcak hava ve lehim kısmını ayırdım. Sıcak hava bölümüne HOT AIR, lehim bölümüne SOLDERING IRON yazdım. Böylece hangi düğmenin hangi bölüme ait olduğu daha kolay anlaşılabilir.', 320, y + 5, 235)
y = text(p, 'Yazıları daha açık yaptım', 320, y + 14, 235, 12, True)
y = text(p, 'AIR yazısının altına SPEED ekledim. Yeşil tuşların yanına TEMP yazdım. Ekranın altındaki TEMP yazısını da ekranın yanına taşıdım. Bu yazılarla hava hızı ve sıcaklık ayarlarını daha açık göstermeye çalıştım.', 320, y + 5, 235)
y = text(p, 'Düğmeleri belli ettim', 320, y + 14, 235, 12, True)
y = text(p, 'Ekran, yeşil tuşlar ve hava hızı düğmesi sıcak hava bölümünde kaldı. HEATER ışığı ve sağdaki sıcaklık düğmesi ise lehim bölümünde kaldı. Çizgiyi aşağıya uzatarak açma kapama düğmelerini de bu bölümlere ayırdım.', 320, y + 5, 235)
y = text(p, 'Bu değişiklikler neyi kolaylaştırır?', 40, 582, 515, 12, True)
y = text(p, 'Başlıklar sayesinde sıcak hava ve lehim ayarları birbirinden ayrılıyor. Beyaz çizgi, hangi düğmenin hangi bölüme ait olduğunu gösteriyor. AIR SPEED yazısı da düğmenin hava hızını ayarladığını açıklıyor. Böylece cihazı ilk kez kullanan biri, düğmeleri tek tek deneyerek öğrenmek yerine yazılara bakarak daha kolay anlayabilir.', 40, y + 5, 515)
y = text(p, 'Sonuç', 40, y + 13, 515, 12, True)
y = text(p, 'Cihazın düğmelerini değiştirmeden, sadece yazı ve çizgi ekleyerek daha anlaşılır bir panel hazırlamaya çalıştım. Bu düzenlemeyi Photoshop üzerinde yaptım, cihazın kendisini değiştirmedim. Açma kapama düğmelerine de neyi açtıklarını yazmak daha iyi olur. Düzenlenmiş hâlini başka kullanıcılarla henüz denemedim.', 40, y + 5, 515)
assert y < 780, y

doc.set_metadata({'title': 'Lehim ve Sıcak Hava İstasyonunda Kontrol ve Gösterge Belirsizliği', 'subject': 'İnsan Bilgisayar Etkileşimi ve Görsellik 2026 Güz'})
doc.save(str(out), garbage=4, deflate=True)
doc.close()
check = fitz.open(str(out))
for i, page in enumerate(check):
    assert 'Kontrol ve Gösterge Belirsizliği' in page.get_text().replace(' ', ' ')
    page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2)).save(str(home / 'AppData/Local/Temp' / f'ibe_pdf_page_{i+1}.png'))
print(f'PDF: {out}')
print(f'Pages: {len(check)}; selectable Turkish text verified')
