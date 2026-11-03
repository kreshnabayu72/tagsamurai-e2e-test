---
id: TC-AC-ACTS-E2E-213-tab-in-use-siklus-search
title: "Detail SKU Tab In Use: Siklus Search Toolbar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-439
coverage:
  web: automated
---

# Detail SKU Tab In Use: Siklus Search Toolbar

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, dicatat lewat kemampuan baca fixture BE pada langkah 3 sebelum aksi (bagian 8b butir 10), bukan diturunkan dari seeding atau dibaca dari satu halaman.
- Search hanya menyaring saat Enter. Keyword siklus: `maju`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total baris Tab In Use SKU `RFID-ASSET-CORE-R5` sebagai baseline `N` (selain teks footer pagination), disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`
2. Verifikasi tabel memuat sedikitnya satu baris data

3. Catat jumlah total baris Tab In Use SKU `RFID-ASSET-CORE-R5` sebagai `N` (kemampuan baca fixture BE)

### TC-AC-ACTS-439: Siklus Search toolbar

4. Hover icon Search
5. Verifikasi tooltip `Search`
6. Klik icon Search
7. Verifikasi input Search terbuka dengan fokus otomatis
8. Verifikasi placeholder input Search `Search by TAG code or client...`
9. Ketik `maju` tanpa menekan Enter
10. Verifikasi tabel belum tersaring (baris yang tidak memuat `maju` masih tampil)
11. Verifikasi icon (✕) muncul di dalam input
12. Tekan Enter
13. Verifikasi tabel memuat sedikitnya satu baris
14. Verifikasi seluruh baris yang tampil cocok dengan keyword `maju`
15. Klik icon (✕) pada input
16. Verifikasi input Search kosong
17. Verifikasi kursor tetap fokus di input Search
18. Verifikasi tabel masih menampilkan hasil search terakhir
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan semua data (jumlah entri pada footer sama dengan `N` yang dicatat pada langkah 3)
21. Ketik Search `maju`, tekan Enter
22. Klik icon panah (←)
23. Verifikasi kotak pencarian tertutup
24. Verifikasi keyword Search dikosongkan
25. Verifikasi tabel langsung kembali menampilkan semua data (jumlah entri pada footer sama dengan `N` yang dicatat pada langkah 3)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi hasil Search. Asersi "semua data" memakai `N` yang dicatat pada langkah 3 lewat kemampuan baca fixture BE sebelum aksi (bagian 8b butir 10, S-12); langkah 3 hanya mencatat baseline tanpa `Verifikasi`.
