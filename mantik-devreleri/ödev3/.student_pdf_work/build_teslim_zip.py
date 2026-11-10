"""Build the final BLM2007 Homework 3 submission archive."""

from pathlib import Path
import os
import shutil
from zipfile import ZipFile, ZIP_DEFLATED

import pymupdf


ROOT = Path(__file__).resolve().parent.parent
TESLIM = ROOT / "teslim"
KODLAR = TESLIM / "kodlar"
FORM = "BLM2007_Doldurulmus_Deney_Yapraklari_Efe_Ozan_imzalı.pdf"
REPORT = "BLM2007_Ayrintili_Cozum_Efe_Ozan.pdf"
PYTHON_FILES = [
    "rakam_donusturucu.py",
    "gray_donusturucu.py",
    "bes_bit_ve_eslik.py",
    "karakter_ve_barkod.py",
    *[f"dogrulama_{i}.py" for i in range(1, 5)],
]

KODLAR.mkdir(parents=True, exist_ok=True)
for filename in PYTHON_FILES:
    shutil.copy2(ROOT / filename, KODLAR / filename)

source_form = TESLIM / FORM
source_report = TESLIM / REPORT
assert source_form.is_file() and source_report.is_file()

with pymupdf.open(source_form) as document:
    assert len(document) == 4
    assert all("170425062" in page.get_text() for page in document)
    assert all("Ali Buldu A Grubu" in page.get_text().replace("\xa0", " ") for page in document)

with pymupdf.open(source_report) as document:
    assert len(document) == 4
    full_text = "\n".join(page.get_text() for page in document)
    assert all(f"Deney {i} -" in full_text for i in range(1, 5))

files = [(source_form, FORM), (source_report, REPORT)]
for filename in PYTHON_FILES:
    src = ROOT / filename
    packaged = KODLAR / filename
    assert src.is_file() and packaged.is_file()
    assert src.read_bytes() == packaged.read_bytes(), f"Code is out of sync: {filename}"
    files.append((packaged, f"kodlar/{filename}"))

for zip_name in ["EfeÖzan_170425062.zip", "teslim.zip"]:
    archive_path = TESLIM / zip_name
    temp_path = TESLIM / f".{zip_name}.tmp"
    try:
        with ZipFile(temp_path, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
            for source, arcname in files:
                archive.write(source, arcname=arcname)

        with ZipFile(temp_path, "r") as archive:
            assert archive.testzip() is None
            assert sorted(archive.namelist()) == sorted(arcname for _, arcname in files)
            for source, arcname in files:
                assert archive.read(arcname) == source.read_bytes(), arcname
        try:
            if archive_path.exists():
                archive_path.unlink()
            os.replace(temp_path, archive_path)
        except PermissionError:
            shutil.copyfile(temp_path, archive_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()

    print(f"Submission archive ready: {archive_path} ({archive_path.stat().st_size} bytes)")

for _, arcname in files:
    print(" ", arcname)
