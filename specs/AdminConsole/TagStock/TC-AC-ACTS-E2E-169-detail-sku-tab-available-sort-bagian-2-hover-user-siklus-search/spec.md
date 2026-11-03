---
id: TC-AC-ACTS-E2E-169-detail-sku-tab-available-sort-bagian-2-hover-user-siklus-search
title: "Detail SKU Tab Available: Sort 3-State Per Kelas Kolom (Bagian 2), Siklus Search Toolbar, dan Hover Nama User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-393
  - TC-AC-ACTS-394
  - TC-AC-ACTS-425
coverage:
  web: automated
---

# Detail SKU Tab Available: Sort 3-State Per Kelas Kolom (Bagian 2), Siklus Search Toolbar, dan Hover Nama User

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Search hanya menyaring saat Enter. Keyword siklus: `tag-4f`; user hover: `Budi Santoso` (Data Dinamis #3).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif
2. Verifikasi tabel memuat sedikitnya satu baris data

### TC-AC-ACTS-393: Sort 3-state kelas user

3. Klik header kolom `Registered By` sekali
4. Verifikasi kolom `Registered By` Ascending (↑) (A-Z menurut nama lengkap user)
5. Klik header kolom `Registered By` kedua kali
6. Verifikasi kolom `Registered By` Descending (↓) dengan urutan terbalik
7. Klik header kolom `Registered By` ketiga kali
8. Verifikasi indikator sort kolom `Registered By` hilang (netral) dan urutan kembali Registered At Newest First

### TC-AC-ACTS-394: Siklus Search toolbar

9. Hover icon Search
10. Verifikasi tooltip `Search`
11. Klik icon Search
12. Verifikasi input Search terbuka dengan fokus otomatis
13. Verifikasi placeholder input Search `Search by TAG code or identifier...`
14. Ketik `tag-4f` tanpa menekan Enter
15. Verifikasi tabel belum tersaring (baris yang tidak memuat `tag-4f` masih tampil)
16. Verifikasi icon (✕) muncul di dalam input
17. Tekan Enter
18. Verifikasi tabel memuat sedikitnya satu baris
19. Verifikasi seluruh baris yang tampil cocok dengan keyword `tag-4f`
20. Klik icon (✕) pada input
21. Verifikasi input Search kosong
22. Verifikasi kursor tetap fokus di input Search
23. Verifikasi tabel masih menampilkan hasil search terakhir
24. Tekan Enter pada input kosong
25. Verifikasi tabel kembali menampilkan semua data (N entri pada footer)
26. Ketik Search `tag-4f`, tekan Enter
27. Klik icon panah (←)
28. Verifikasi kotak pencarian tertutup
29. Verifikasi keyword Search dikosongkan
30. Verifikasi tabel langsung kembali menampilkan semua data (N entri pada footer)

### TC-AC-ACTS-425: Hover nama user kolom Registered By

31. Hover nama user `Budi S` di kolom `Registered By`
32. Verifikasi kolom menampilkan `Budi S` (first name lengkap dan inisial last name)
33. Verifikasi tooltip menampilkan nama lengkap `Budi Santoso`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembanding "sedikitnya satu baris" mendahului asersi urutan. Asersi "semua data" memakai N dari seeding (bagian 8b butir 10).
- Temuan untuk QA: TC-AC-ACTS-394 langkah 7 berbunyi "Tekan Enter pada input kosong" tanpa menyebut bahwa hasil search terakhir masih tampil sebelumnya; spec mengikuti Expected butir d dan e.
