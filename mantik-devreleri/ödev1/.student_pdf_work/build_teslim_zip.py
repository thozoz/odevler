"""Build the final BLM2007 submission archive from the signed handout.

The unsigned handout stays available as a backup but is not included in ZIP.
"""

from pathlib import Path
import os
from zipfile import ZipFile, ZIP_DEFLATED

import pymupdf


ROOT = Path(__file__).resolve().parent.parent
TESLIM = ROOT / "teslim"
FORM = "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan_imzalı.pdf"
REPORT = "BLM2007_Ayrintili_Cozum_Efe_Ozan.pdf"
PYTHON_FILES = ["sayi_donusturucu.py", *[f"dogrulama_{i}.py" for i in range(1, 8)]]

source_form = TESLIM / FORM
source_report = TESLIM / REPORT
assert source_form.is_file() and source_report.is_file()

with pymupdf.open(source_form) as document:
    assert len(document) == 7
    assert all("170425062" in page.get_text() for page in document)
    assert all("Ali Buldu A Grubu" in page.get_text().replace("\xa0", " ") for page in document)

with pymupdf.open(source_report) as document:
    assert len(document) == 4
    assert all(f"Deney {i} -" in "\n".join(page.get_text() for page in document)
               for i in range(1, 8))

files = [(source_form, FORM), (source_report, REPORT)]
for filename in PYTHON_FILES:
    src = ROOT / filename
    packaged = TESLIM / "kodlar" / filename
    assert src.is_file() and packaged.is_file()
    assert src.read_bytes() == packaged.read_bytes(), f"Code is out of sync: {filename}"
    files.append((packaged, f"kodlar/{filename}"))

archive_path = TESLIM / "teslim.zip"
temp_path = TESLIM / ".teslim.zip.tmp"
try:
    with ZipFile(temp_path, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for source, arcname in files:
            archive.write(source, arcname=arcname)

    with ZipFile(temp_path, "r") as archive:
        assert archive.testzip() is None
        assert sorted(archive.namelist()) == sorted(arcname for _, arcname in files)
        for source, arcname in files:
            assert archive.read(arcname) == source.read_bytes(), arcname
    os.replace(temp_path, archive_path)
finally:
    if temp_path.exists():
        temp_path.unlink()

print(f"Submission archive ready: {archive_path}")
for _, arcname in files:
    print(" ", arcname)
print("Total ZIP bytes:", archive_path.stat().st_size)
