---
id: TC-AC-ACTS-E2E-013-search-stock-list-numerik-dan-alur-search-filter
title: "Search Stock List: Kelas Numerik serta Alur Search lalu Filter dan Filter lalu Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-45
  - TC-AC-ACTS-49
  - TC-AC-ACTS-50
coverage:
  web: automated
---

# Search Stock List: Kelas Numerik serta Alur Search lalu Filter dan Filter lalu Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Data seed milik spec (SKU bersuffix `{runId}-013`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): SKU N dengan Total Registered 500, Available 213, In Use 280, Damaged/Missing 7 (nilai dari Data Uji TC; volume 500 unit diwujudkan fixture BE).
- Kolom numerik yang diuji (dipakai pengulangan langkah TC-AC-ACTS-45): `Total Registered` = `500`, `Available` = `213`, `In Use` = `280`, `Damaged/Missing` = `7`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-45: Search kelas numerik

1. Untuk setiap baris tabel kolom numerik pada Prerequisites lakukan langkah 2 sampai 6 (empat kolom)
2. Ketik Search nilai kolom (mis. `500`), tekan Enter
3. Verifikasi Baris SKU N tampil
4. Ganti isi kotak search dengan `zzz-tidak-ada-` diikuti singkatan kolom (mis. `zzz-tidak-ada-tot`), tekan Enter
5. Verifikasi Empty state `No results found` tampil
6. Klik `(←)` pada kotak Search

### TC-AC-ACTS-49: Alur Search lalu Filter

7. Klik icon Search, ketik `rfid`, tekan Enter
8. Klik icon Filter, pilih `RFID Asset Tag` pada field `Device Name`, klik `[Apply]`
9. Verifikasi Hasil tabel = irisan Search dan Filter (hanya baris Device Name `RFID Asset Tag`)
10. Verifikasi Keyword Search `rfid` tidak dikosongkan oleh Apply Filter
11. Catat daftar baris hasil tabel

### TC-AC-ACTS-50: Alur Filter lalu Search

12. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
13. Klik `(←)` pada kotak Search
14. Klik icon Filter, pilih `RFID Asset Tag` pada field `Device Name`, klik `[Apply]`
15. Klik icon Search, ketik `rfid`, tekan Enter
16. Verifikasi Hasil tabel identik dengan daftar baris hasil alur Search lalu Filter
17. Verifikasi Kriteria Filter `Device Name` = `RFID Asset Tag` tetap aktif setelah Search
18. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): Filter dibersihkan sebelum TC berikutnya dan di akhir spec (S-09); `(←)` mengosongkan Search.
- Temuan untuk QA (S-15): TC-AC-ACTS-45 memakai nilai absolut 500, 213, 280, 7 (volume 500 unit) yang tidak dapat diturunkan dari data bersama; spec memakai SKU seed milik spec dengan nilai itu (diwujudkan fixture BE). TC-AC-ACTS-45 menyebut keyword `7` yang dapat cocok dengan lebih dari satu baris; spec mengasersi bahwa baris SKU N termasuk di hasil.
- Ekspansi 4 kolom numerik pada langkah 2 sampai 6 tetap di bawah 35 langkah (8b.7).
