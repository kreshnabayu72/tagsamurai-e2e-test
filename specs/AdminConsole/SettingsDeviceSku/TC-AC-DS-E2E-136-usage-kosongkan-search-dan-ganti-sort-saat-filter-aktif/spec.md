---
id: TC-AC-DS-E2E-136-usage-kosongkan-search-dan-ganti-sort-saat-filter-aktif
title: "Usage: Mengosongkan Search dan Mengganti Kolom Sort saat Search dan Filter Aktif"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-587
  - TC-AC-DS-588
coverage:
  web: automated
---

# Usage: Mengosongkan Search dan Mengganti Kolom Sort saat Search dan Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `TAG-ARC-USR` serta seed (#29, #30); data Usage `TAG-ARC-USR` 13 baris (#32, #24): `PT Arunika Prima` (Principal) Total Stock 20 dan 12 Client `PT Klien Uji 01` sampai `PT Klien Uji 12` masing-masing Total Stock 40. Nilai dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup di atas ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Ketik Search `TAG-ARC-USR` pada List, tekan Enter
2. Klik SKU `TAG-ARC-USR`
3. Verifikasi Popup `Device SKU Detail` tampil
4. Verifikasi tabel Usage memuat sedikitnya satu baris

### TC-AC-DS-587: Mengosongkan Search pada Usage by Company saat Filter dan Sort aktif hanya melepas Search

5. Klik ikon Filter pada popup
6. Pada field Entity Type pilih `Client`
7. Klik `[Apply]` pada Filter Panel popup
8. Klik header kolom Company sekali
9. Klik header kolom Company sekali lagi
10. Ketik Search `Klien Uji 0`, tekan Enter
11. Verifikasi tabel memuat 9 baris berurutan Descending dari `PT Klien Uji 09` sampai `PT Klien Uji 01`
12. Verifikasi `PT Arunika Prima` tidak tampil pada tahap Search
13. Klik `✕` pada Search, tekan Enter
14. Verifikasi Filter Entity Type `Client` tetap aktif
15. Verifikasi Sort Company Descending tetap aktif: halaman 1 memuat 10 baris dari `PT Klien Uji 12` sampai `PT Klien Uji 03`
16. Verifikasi `PT Arunika Prima` tidak tampil pada halaman 1 setelah Search dilepas
17. Pindah ke halaman 2
18. Verifikasi halaman 2 memuat `PT Klien Uji 02` dan `PT Klien Uji 01`
19. Verifikasi `PT Arunika Prima` tidak tampil pada halaman 2 setelah Search dilepas

### Pemulihan state antar TC

20. Pindah ke halaman 1; klik header kolom Company sekali lagi (kembali ke default); klik `[Clear Field]`

### TC-AC-DS-588: Mengganti kolom Sort pada Usage by Company saat Search dan Filter aktif melepas Sort lama dan mempertahankan Search dan Filter

21. Ketik Search `Klien Uji 1`, tekan Enter
22. Pada field Entity Type pilih `Client`
23. Klik `[Apply]` pada Filter Panel popup
24. Klik header kolom Company sekali
25. Klik header kolom Company sekali lagi
26. Verifikasi setelah Sort Company Descending tabel memuat tiga baris berurutan `PT Klien Uji 12`, `PT Klien Uji 11`, `PT Klien Uji 10`
27. Klik header kolom Total Stock sekali
28. Verifikasi Sort Total Stock Ascending aktif dan Sort Company dilepas
29. Verifikasi ketiga baris bernilai Total Stock 40
30. Verifikasi ketiga baris berurutan menurut default sort Company A-Z: `PT Klien Uji 10`, `PT Klien Uji 11`, `PT Klien Uji 12`
31. Verifikasi Search `Klien Uji 1` dan Filter Entity Type `Client` tetap aktif (tiga baris)

### Pemulihan state akhir

32. Klik `(←)` pada kotak Search; klik `[Clear Field]`, klik `[Apply]`; klik header kolom Total Stock sekali lagi dua kali (kembali ke default); tutup popup dengan ikon close `[✕]`
33. Klik `(←)` pada kotak Search List

## Notes

- Langkah 1 sampai 4 adalah pembuka bersama (Search List untuk menemukan `TAG-ARC-USR`, lalu popup dibuka sekali). Langkah 4 adalah pembanding generik sebelum asersi (8b butir 2).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search List untuk menemukan baris `TAG-ARC-USR`, R-16), langkah 20 dan 32 (membersihkan Search, Filter, Sort, dan halaman, S-03, S-09), dan langkah 33 (mengosongkan Search List). Di TC-AC-DS-588 Filter Panel dianggap masih terbuka seperti pada TC-AC-DS-587 (langkah 22 tidak membuka ikon Filter lagi).
- Expected 587 butir a ditulis langkah 11; butir b dipecah langkah 14, 15, 18; butir c langkah 12, 16, 19 (pada kedua tahap, anchor positif: baris pada langkah 11, 15, 18). Expected 588 butir b dipecah langkah 28, 29, 30; butir c langkah 31.
- Temuan untuk QA:
  - S-11/S-14: TC 588 butir b memakai tiga baris yang semuanya Total Stock 40, sehingga sort Total Stock Ascending tidak dapat dibedakan dari default Company A-Z; hasil sort tanpa dua nilai distinct bukan asersi sort. Spec mengikuti TC dan hanya mengasersi indikator sort (langkah 28) dan urutan default (langkah 30).
  - S-15: TC tidak menyatakan apakah Filter Panel tertutup sesudah `[Apply]`; spec mengikuti TC (panel tetap terbuka).
  - S-14: TC tidak menyebut Search untuk menemukan baris `TAG-ARC-USR`, padahal baris itu tidak berada di halaman pertama List (default sort SKU A-Z); spec menambah langkah Search `TAG-ARC-USR` (langkah 1) sebagai langkah penghubung.
  - Fixture rancangan Pre-setup #32 dan #24 (12 Client uji) belum terverifikasi ada di environment; `Fixture.settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
