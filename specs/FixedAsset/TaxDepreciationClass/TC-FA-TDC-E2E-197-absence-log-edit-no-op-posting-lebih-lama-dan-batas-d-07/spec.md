---
id: TC-FA-TDC-E2E-197-absence-log-edit-no-op-posting-lebih-lama-dan-batas-d-07
title: "Absence Log: Edit No-Op, Posting Tahun Pajak Sama atau Lebih Lama, dan Batas D-07 Tidak Menulis Entri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-681
  - TC-FA-TDC-694
  - TC-FA-TDC-134
coverage:
  web: automated
---

# Absence Log: Edit No-Op, Posting Tahun Pajak Sama atau Lebih Lama, dan Batas D-07 Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before` dan dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Spec absence (kelas g): pemicu kelas lain (Edit No-Op, posting J-03 lewat fixture BE, batas D-07) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5). Tiap TC punya baseline sendiri yang dicatat tepat sebelum pemicu (S-12).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`; nilai dari TC): Kode class milik spec berpola `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol.

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-681 | `KHS-197A` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Active, Used By 0, satu versi tanpa Effective From, Last Posted Tax Year kosong |
| TC-FA-TDC-694 | `KHS-197B` | Last Posted Tax Year `2026`; keadaan lain sama dengan `KHS-197A` |
| TC-FA-TDC-134 | tidak ada class milik spec | Master Data Count Limit 1000 (nilai minimum, Lifecycle Settings > System Limits) dan total class semua status 1000 (tambahan dibuat lewat API pre-setup) |

- Tabel memuat tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah dua class milik spec (9 baris); baris `KHS-197*` tampil di halaman pertama (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga baris dibuka tanpa Search (8b.13, R-23). Blok TC-FA-TDC-134 berjalan terakhir dengan tabel 1000 class.
- State global: Master Data Count Limit dan jumlah class diubah pada blok TC-FA-TDC-134 (kemampuan disediakan tim FE/BE); dipulihkan pada langkah terakhir spec dan di hook `after`. Posting tahun pajak lewat fixture BE (J-03) disediakan tim FE/BE; mekanismenya tidak disebut TC (S-13).
- Pemulihan: hook `after` menghapus `KHS-197A` dan `KHS-197B` lewat API dan mengembalikan jam, Master Data Count Limit, dan sesi.

## Test Steps

### TC-FA-TDC-681: Edit No-Op tidak menulis entri log pada surface mana pun

1. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
2. Klik link Class Code `KHS-197A` pada tabel
3. Klik `[Save]` tanpa mengubah field apa pun
4. Verifikasi toast info `No changes to save.` tampil
5. Klik `[×]` pada Drawer Edit
6. Klik ikon Changelog di toolbar
7. Verifikasi jumlah entri Changelog sama dengan baseline
8. Tutup Popup Changelog
9. Buka Detail User Rina Puspita > Tab System Log
10. Verifikasi jumlah entri System Log Rina Puspita sama dengan baseline
11. Buka Reports & Logs > Activity Log, tab `User Action`
12. Verifikasi jumlah entri Activity Log sama dengan baseline
13. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-694: Log L-10: posting tahun sama atau lebih lama tidak menulis entri

14. Catat baseline jumlah entri Changelog untuk Class Code `KHS-197B`
15. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-197B` lewat fixture BE (J-03)
16. Picu posting tahun pajak 2025 untuk `KHS-197B` lewat fixture BE
17. Klik link Class Code `KHS-197B` pada tabel
18. Verifikasi Last Posted Tax Year tetap "2026" pada Drawer Edit
19. Klik `[×]` pada Drawer Edit
20. Klik ikon Changelog di toolbar
21. Ketik Search `KHS-197B`, tekan Enter
22. Verifikasi tidak ada baris L-10 baru untuk Class Code `KHS-197B`
23. Verifikasi jumlah entri Changelog `KHS-197B` sama dengan baseline
24. Tutup Popup Changelog
25. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-134: Create yang ditolak D-07 tidak mengubah data dan tidak menulis log

26. Atur Master Data Count Limit menjadi 1000 dan tambahkan class lewat API hingga total semua status 1000 (kemampuan disediakan tim FE/BE)
27. Buka Settings > Accounting > Tax Depreciation Class
28. Catat baseline jumlah entri Changelog
29. Klik `+ Class` di toolbar
30. Verifikasi dialog D-07 tampil
31. Klik `[OK]`
32. Verifikasi total class tetap 1000 (dibaca lewat kemampuan baca jumlah class)
33. Klik ikon Changelog di toolbar
34. Verifikasi jumlah entri Changelog sama dengan baseline
35. Tutup Popup Changelog
36. Pulihkan Master Data Count Limit ke nilai awal dan hapus class tambahan lewat API hingga selesai

## Notes

- Alasan melewati sekitar 35 langkah (36 langkah, 21 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 6 sampai 12, 20 sampai 24, 33 sampai 35 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- S-05 dan prinsip 13g: seluruh TC di spec ini adalah asersi absence atas log dengan aksi nyata dan baseline sendiri (S-12). Anchor positif (8b.2): toast `No changes to save.` (langkah 4), Last Posted Tax Year `2026` pada Drawer (langkah 18), dan dialog D-07 (langkah 30). Langkah 18 ditulis sebelum asersi absence meski Expected TC menyebutnya sesudah (anchor lebih dulu).
- Urutan TC: 681, 694, 134. TC-FA-TDC-134 di akhir karena membangun state berat (1000 class) dan mengubah state global (S-10).
- Langkah penghubung (S-03): mencatat baseline, menutup Popup Changelog, `[×]` pada Drawer Edit tanpa perubahan, membangun dan memulihkan state batas D-07, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Search `KHS-197B` pada Popup Changelog adalah langkah penghubung untuk menemukan entri (R-16).
- Jam server dan jam browser tidak diubah oleh spec ini selain nilai awal hook; log tidak bercap waktu masa depan.
- Temuan untuk QA:
  - TC-FA-TDC-694 tidak menyebut surface sumber "jumlah entri Changelog KHS-LG" dan cara membaca L-10; spec membaca Popup Changelog dengan Search Class Code. Post Condition TC-681 dan TC-134 tidak menyebut langkah observasi tambahan.
  - TC-FA-TDC-134 "total class tetap 1000" tidak menyebut cara membacanya di UI; spec memakai kemampuan baca jumlah class lewat fixture BE (disediakan tim FE/BE). Jumlah class tambahan pada precondition (993) mengasumsikan hanya tujuh seed; dataset spec ini memuat 11 baris sebelum penambahan sehingga jumlah tambahan menyesuaikan sampai total 1000.
  - TC-FA-TDC-134, 681, 694 memakai kode class literal (`KHS-LG`); spec memakai satu class per TC (S-06, S-12).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
