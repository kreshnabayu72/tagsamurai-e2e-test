---
id: TC-AC-ACTS-E2E-009-sort-stock-list-kelas-teks-dan-label
title: "Sort Stock List: Kelas Teks (Device Name, SKU, Type) dan Kelas Label (TAG Type, Brand, Model/Type)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-36
  - TC-AC-ACTS-37
coverage:
  web: automated
---

# Sort Stock List: Kelas Teks (Device Name, SKU, Type) dan Kelas Label (TAG Type, Brand, Model/Type)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Kolom yang diuji (dipakai pengulangan langkah):

| TC | Kolom | Aturan Ascending |
|---|---|---|
| TC-AC-ACTS-36 | `Device Name` | A-Z, case-insensitive |
| TC-AC-ACTS-36 | `SKU` | A-Z, case-insensitive |
| TC-AC-ACTS-36 | `Type` | A-Z, case-insensitive |
| TC-AC-ACTS-37 | `TAG Type` | A-Z menurut accessibility label icon |
| TC-AC-ACTS-37 | `Brand` | A-Z menurut label badge atau accessibility label |
| TC-AC-ACTS-37 | `Model/Type` | A-Z menurut label badge atau accessibility label |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-36: Sort 3-state kelas teks

1. Untuk setiap baris tabel «Kolom TC-AC-ACTS-36» lakukan langkah 2 sampai 7 (tiga kolom)
2. Klik header kolom pada tabel «Kolom TC-AC-ACTS-36» sekali
3. Verifikasi Urutan Ascending (↑) (A-Z, case-insensitive)
4. Klik header kolom yang sama kedua kali
5. Verifikasi Urutan Descending (↓) terbalik dari Ascending
6. Klik header kolom yang sama ketiga kali
7. Verifikasi Indikator sort hilang dan urutan kembali Last Updated Newest First (SKU tanpa aktivitas di akhir)

### TC-AC-ACTS-37: Sort 3-state kelas label

8. Untuk setiap baris tabel «Kolom TC-AC-ACTS-37» lakukan langkah 9 sampai 14 (tiga kolom)
9. Klik header kolom pada tabel «Kolom TC-AC-ACTS-37» sekali
10. Verifikasi Urutan Ascending (↑) (A-Z menurut label)
11. Klik header kolom yang sama kedua kali
12. Verifikasi Urutan Descending (↓) terbalik dari Ascending
13. Klik header kolom yang sama ketiga kali
14. Verifikasi Indikator sort hilang dan urutan kembali Last Updated Newest First (SKU tanpa aktivitas di akhir)

## Notes

- Ekspansi di atas 35 langkah (14 langkah nominal; 38 langkah setelah blok langkah 2 sampai 7 dan 9 sampai 14 diulang untuk tiga kolom masing-masing): objek uji dan dataset sama (Sort Stock List), langkah yang diulang per kolom diparameterkan di tabel Prerequisites (8b.7); kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Langkah penghubung (S-03): klik header ketiga mengembalikan urutan netral sebelum kolom berikutnya (S-09); halaman dibuka hook `beforeEach` suite.
- Temuan untuk QA (S-15): TC-AC-ACTS-36 dan 37 menyebut klik #3 kembali ke "Last Updated Newest First" sebagai netral; spec mengikuti. Urutan pembanding `TAG Type` berbasis accessibility label sehingga pembacaan label icon disediakan tim FE.
