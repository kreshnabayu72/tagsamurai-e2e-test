---
id: TC-AC-ACTS-E2E-037-download-stock-list-isi-sel-xlsx
title: "Download Stock List: Isi Sel XLSX per Tipe Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-73
coverage:
  web: automated
---

# Download Stock List: Isi Sel XLSX per Tipe Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis (kelas f): pembaca isi berkas XLSX unduhan dan pembanding dengan tabel di layar (disediakan tim FE).
- Data uji: tabel berisi seluruh jenis nilai kolom termasuk sel kosong (`—` pada Last Updated), icon TAG Type, badge Brand dan Model/Type, dan foto.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat isi tabel Stock List yang tampil di layar (nilai tiap kolom pada tiap baris)
2. Klik icon Download
3. Pilih `Download as XLSX`
4. Buka isi berkas XLSX yang terunduh
5. Verifikasi Foto tidak ikut di berkas
6. Verifikasi Icon TAG Type ditulis sebagai accessibility label teks (`RFID`, `NFC`, `BLE`, `GPS`)
7. Verifikasi Badge Brand dan Model/Type ditulis sebagai label teks tanpa warna
8. Verifikasi Total Registered, Available, In Use, dan Damaged/Missing ditulis sebagai sel angka
9. Verifikasi Last Updated mengikuti format General Settings
10. Verifikasi Sel `—` ditulis `-`
11. Verifikasi Hanya kolom yang sedang tampil dan baris hasil Search atau Filter yang ikut

## Notes

- TC-AC-ACTS-73 adalah kelas f (binary buffer: isi file); spec ini memisahkannya dari nama berkas CSV dan XLSX di spec 021 (prinsip 13f).
- Temuan untuk QA (S-15): TC-AC-ACTS-73 butir e ("Hanya kolom yang sedang tampil dan baris hasil Search/Filter yang ikut") tidak menyebut Search atau Filter yang diaktifkan di langkah; spec mengasersi terhadap tabel yang tampil saat unduh (tanpa Search atau Filter aktif).
