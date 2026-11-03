---
id: TC-AC-SG-E2E-053-filter-tabel-utama-modified-by-search-dropdown-dan-last-updated
title: "Filter Tabel Utama: Modified By, Search Dropdown, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-190
  - TC-AC-SG-191
  - TC-AC-SG-192
  - TC-AC-SG-193
coverage:
  web: automated
---

# Filter Tabel Utama: Modified By, Search Dropdown, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #20), node `All Groups` terpilih, 14 group, urutan bawaan Group A-Z. Modified By dan Last Updated yang dipakai: `Default Group` `System` 10 Jul 2026; `Region A` `Admin A` 14 Jul 2026; `Region B` `Admin A` 14 Jul 2026; `Head Office` `Admin C` 11 Jul 2026; `Branch 1` dan `Branch 2` `Admin B` 12 Jul 2026. Nilai Modified By distinct: `Admin A`, `Admin B`, `Admin C`, `System` (S-11). Format tanggal Last Updated mengikuti General Settings; zona waktu browser dan server sama.
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik ikon Filter pada toolbar

### TC-AC-SG-190: Filter tabel utama by Modified By: satu opsi

2. Pilih `Admin B` pada Modified By
3. Klik `[Apply]`
4. Verifikasi tabel menampilkan `Branch 1`
5. Verifikasi setiap baris yang tampil ber-Modified By `Admin B`
6. Verifikasi indikator filter aktif tampil pada ikon Filter

### TC-AC-SG-191: Filter Modified By dengan dua opsi memakai logika OR

7. Klik `[Clear Field]`
8. Klik `[Apply]`
9. Centang `Admin A` dan `Admin C` pada Modified By
10. Klik `[Apply]`
11. Verifikasi tabel menampilkan baris ber-Modified By `Admin A` atau `Admin C`: `Region A` dan `Head Office`
12. Verifikasi baris ber-Modified By `Admin B` (`Branch 1` dan `Branch 2`) tidak tampil

### TC-AC-SG-192: Search internal dropdown dan chip opsi terpilih pada Modified By

13. Klik `[Clear Field]`
14. Buka dropdown Modified By, ketik `admin b` di kotak search dropdown
15. Verifikasi daftar opsi menyempit ke `Admin B`
16. Hapus teks di kotak search dropdown, centang `Admin A` lalu `Admin B`
17. Verifikasi kedua chip `Admin A` dan `Admin B` tampil di dalam field
18. Klik (✕) pada chip `Admin A`
19. Verifikasi chip `Admin A` terhapus dari field
20. Verifikasi opsi `Admin A` tidak tercentang di dropdown
21. Verifikasi chip `Admin B` tetap tampil

### TC-AC-SG-193: Filter tabel utama by Last Updated: rentang tanggal inklusif

22. Klik `[Clear Field]`
23. Pilih rentang 11 Jul 2026 sampai 12 Jul 2026 pada Last Updated
24. Klik `[Apply]`
25. Verifikasi tabel menampilkan baris ber-Last Updated dalam periode, inklusif kedua ujung: `Head Office` (11 Jul 2026), `Branch 1` dan `Branch 2` (12 Jul 2026)
26. Pilih rentang satu hari 14 Jul 2026 (Start = End)
27. Klik `[Apply]`
28. Verifikasi tabel menampilkan baris ber-Last Updated 14 Jul 2026: `Region A` dan `Region B`

## Notes

- Langkah penghubung (S-03): langkah 7 dan 8 (mengosongkan lalu menerapkan filter kosong supaya tabel pulih sebelum TC-191, S-09), langkah 13 dan 22 (mengosongkan draft filter sebelum blok berikutnya). Filter Panel tetap terbuka dari langkah 1 sampai akhir; perilaku panel tetap terbuka sesudah `[Apply]` mengikuti TC-AC-SG-196.
- Langkah 5 (asersi universal) didahului langkah 4 yang membuktikan sedikitnya satu baris tampil pada surface yang sama (8b butir 2). Langkah 12 (absence) didahului langkah 11.
- Langkah 25 dan 28: Expected TC-193 menyebut "baris dalam periode" tanpa nama baris; spec memakai baris menurut Pre-setup #20. Node lain ber-Modified By dan Last Updated "bervariasi" dan tidak tercantum nilainya, sehingga tidak ada asersi bahwa baris lain di luar periode tidak tampil.
- Temuan untuk QA:
  - TC-AC-SG-193: Pre-setup #20 tidak menyebut Last Updated seluruh node; asersi "hanya baris dalam periode" tidak dapat ditulis lengkap. Usulan: Pre-setup menyebut Last Updated tiap node.
  - TC-AC-SG-192: TC tidak menyatakan apakah dropdown tetap terbuka sesudah klik (✕) pada chip; langkah 20 mengasersi opsi di dropdown tanpa langkah membuka ulang.
