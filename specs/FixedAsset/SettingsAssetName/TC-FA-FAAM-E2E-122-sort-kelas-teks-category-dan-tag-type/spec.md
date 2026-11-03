---
id: TC-FA-FAAM-E2E-122-sort-kelas-teks-category-dan-tag-type
title: "Sort: Siklus Tiga State Kelas Teks, Category, dan TAG Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-389
  - TC-FA-FAAM-390
  - TC-FA-FAAM-391
coverage:
  web: automated
---

# Sort: Siklus Tiga State Kelas Teks, Category, dan TAG Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris TAG Type yang dirujuk (kunci sort gabungan label ikon): `MacBook Pro` `BLE, QR`; `Service Vehicle` `GPS, RFID`; `NFC QR Item` (Pre-setup #14v, `NFC`+`QR`) `NFC, QR`; `Warehouse Pallet` `Non-TAG`; `Ergonomic Chair` `QR`; `Dell Latitude` `QR, RFID`.
- Kolom yang diuji untuk TC-FA-FAAM-389 (diulang pada langkah 1 sampai 6):

  | Kolom |
  |---|
  | Asset Name |
  | Code |
  | UoM |
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-389: Sort kelas Asset Name, Code, UoM (teks A-Z): siklus tiga state
1. Untuk setiap baris tabel "Kolom yang diuji", klik header kolom tersebut satu kali
2. Verifikasi klik 1 Ascending: urutan A-Z tanpa membedakan huruf besar-kecil
3. Klik header kolom yang sama kedua kali
4. Verifikasi klik 2 Descending: urutan Z-A
5. Klik header kolom yang sama ketiga kali
6. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z
### TC-FA-FAAM-390: Sort kelas Category: siklus tiga state
7. Klik header kolom Category satu kali
8. Verifikasi klik 1 Ascending: A-Z menurut nama kategori yang tampil
9. Klik header kolom Category kedua kali
10. Verifikasi klik 2 Descending: Z-A
11. Klik header kolom Category ketiga kali
12. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z
### TC-FA-FAAM-391: Sort kelas TAG Type: siklus tiga state
13. Klik header kolom TAG Type satu kali
14. Verifikasi klik 1 Ascending: A-Z menurut kunci gabungan label ikon (dipisah `, `); urutan relatif baris fixture bernama menurut kunci `BLE, QR`, `GPS, RFID`, `NFC, QR`, `Non-TAG`, `QR`, `QR, RFID`
15. Klik header kolom TAG Type kedua kali
16. Verifikasi klik 2 Descending: Z-A dengan urutan relatif kunci `QR, RFID`, `QR`, `Non-TAG`, `NFC, QR`, `GPS, RFID`, `BLE, QR`
17. Klik header kolom TAG Type ketiga kali
18. Verifikasi klik 3 kembali netral dan urutan default Asset Name A-Z

## Notes

- Langkah yang diulang per kolom pada TC-FA-FAAM-389: langkah 1 sampai 6; parameter tiap iterasi ada di tabel "Kolom yang diuji" pada Prerequisites. Verifikasi diulang satu per klausa (bagian 8b butir 7).
- Tiap blok diakhiri klik ketiga yang mengembalikan sort ke netral sehingga blok berikutnya tidak mewarisi sort (S-09).
- Posisi baris `Seed Item` pada klik 1 dan 2 TC-FA-FAAM-391 tidak diasersi (Expected d TC); asersi urutan relatif memakai enam baris fixture bernama.
- Temuan untuk QA: contoh `anggur` dan `Apel` pada Expected TC-FA-FAAM-389 tidak ada di fixture Pre-setup; spec mengasersi urutan A-Z tanpa membedakan huruf besar-kecil pada data yang ada, dan dua nilai distinct pada tiap kolom terpenuhi oleh data fixture.
- Temuan untuk QA: kunci sort `Dell Latitude` `QR, RFID` pada TC-FA-FAAM-391 berbeda dari urutan label `RFID, QR` pada Expected TC-FA-FAAM-448 (isi berkas download); urutan dalam satu sel tidak ditetapkan konsisten antar TC.
