---
id: TC-FA-TDC-E2E-281-validasi-declining-balance-rate-kosong-dan-di-luar-rentang-create-dan-edit-ditolak
title: "Validasi Declining Balance Rate: Create Kosong serta Edit Kosong dan di Luar Rentang Ditolak Tanpa Entri Log Baru"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-936
  - TC-FA-TDC-950
sourceRules: ["V-16", "V-17", "F-FATDC-01.k4h", "FATDC-LOGIC-03f.2", "E-FATDC-04", "F-FATDC-02"]
smoke: []
dependsOn: []
trace:
  "V-16": [6, 24]
  "V-17": [27, 29]
  "F-FATDC-01.k4h": [6, 7]
  "FATDC-LOGIC-03f.2": [6, 24, 27, 29]
  "E-FATDC-04": [6, 7]
  "F-FATDC-02": [24, 25, 31, 33, 36, 37]
coverage:
  web: automated
---

# Validasi Declining Balance Rate: Create Kosong serta Edit Kosong dan di Luar Rentang Ditolak Tanpa Entri Log Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) dengan Fiscal Year Start Januari (Precondition c TC-FA-TDC-950); jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Master Data Count Limit belum tercapai (Precondition c TC-FA-TDC-936); kemampuan mengatur kuota disediakan tim FE/BE.
- Kemampuan teknis (disediakan tim FE/BE): seeding class lewat API dan pembacaan UI untuk jumlah entri log. Jumlah entri `DBE-01` dan `DBE-12` dicatat sebagai baseline tepat sebelum aksi tiap TC lewat UI: Changelog (ikon Changelog di toolbar, Search `DBE-01` atau `DBE-12`), System Log aktor (Detail User > Tab System Log), dan Activity Log (`Reports & Logs > Activity Log`, tab `User Action`); jumlah sesudah aksi dibaca lewat jalur yang sama dan dibandingkan dengan baseline (8b.10, S-12).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; kode `DBE-*` tidak dipakai TC lain):

| Kunci fixture (usulan) | Class Code | Keadaan |
|---|---|---|
| `dbe01` | `DBE-01` | belum ada (dibuat TC-FA-TDC-936 tidak berhasil; hook `before` menghapus sisa dari run sebelumnya) |
| `dbe12` | `DBE-12` | Non-building, Useful Life 8, Straight Line dan Declining Balance (Declining Balance Rate 25, End-of-Life Treatment `Charge in final period`), hanya satu versi (Current tanpa Effective From), Active, Used By 0, tanpa versi Scheduled |

- Tabel memuat tujuh class seed bawaan dan `DBE-12` (8 baris dalam satu halaman); baris target dibuka lewat Search Class Code (8b.13, R-23).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-936: Submit Create ditolak bila Declining Balance Rate kosong padahal Declining Balance dipilih

1. Catat baseline jumlah entri `DBE-01` di Changelog (Search `DBE-01`), System Log aktor, dan Activity Log, lalu buka Settings > Accounting > Tax Depreciation Class
2. Klik `+ Class` di toolbar
3. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `DBE-01`, Class Name `Kelompok uji tarif 1`, pilih Asset Type `Non-building`, isi Useful Life `8`, pilih Allowed Methods `Straight Line` dan `Declining Balance`
4. Biarkan Declining Balance Rate kosong
5. Klik `[Submit]`
6. Verifikasi caption "Declining rate must not be empty" muncul di bawah field Declining Balance Rate (%)
7. Verifikasi Drawer tetap terbuka
8. Verifikasi helper "Equivalent to [factor]× the straight-line rate" tidak tampil
9. Klik `[Clear Field]`
10. Klik `[×]` pada Drawer Create
11. Ketik Search `DBE-01`, tekan Enter
12. Verifikasi empty state "No results found" tampil (class `DBE-01` tidak dibuat)
13. Klik `(←)` pada kotak Search
14. Baca ulang jumlah entri `DBE-01` di Changelog (Search `DBE-01`), System Log aktor, dan Activity Log seperti langkah 1
15. Verifikasi jumlah entri `DBE-01` di Changelog sama dengan baseline langkah 1
16. Verifikasi jumlah entri `DBE-01` di System Log aktor sama dengan baseline langkah 1
17. Verifikasi jumlah entri `DBE-01` di Activity Log sama dengan baseline langkah 1
18. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-950: Edit: Declining Balance Rate kosong atau di luar rentang ditolak

19. Catat baseline jumlah entri `DBE-12` di Changelog (Search `DBE-12`), System Log aktor, dan Activity Log, lalu buka Settings > Accounting > Tax Depreciation Class
20. Ketik Search `DBE-12`, tekan Enter
21. Klik link Class Code `DBE-12` pada tabel
22. Kosongkan Declining Balance Rate
23. Klik `[Save]`
24. Verifikasi caption "Declining rate must not be empty" tampil
25. Verifikasi dialog D-09 tidak muncul
26. Ketik Declining Balance Rate `100.5`
27. Verifikasi caption "Declining rate must be between 0 and 100" tampil langsung saat mengetik
28. Ganti Declining Balance Rate menjadi `0`
29. Verifikasi caption "Declining rate must be between 0 and 100" tampil
30. Klik `[×]` pada Drawer Edit
31. Verifikasi dialog `Unsaved Changes` tampil
32. Klik `[Leave]`
33. Verifikasi Drawer Edit tertutup tanpa menyimpan
34. Klik link Class Code `DBE-12` pada tabel
35. Klik tautan View versions
36. Verifikasi modal Versions memuat satu baris (`DBE-12` tetap satu versi)
37. Verifikasi baris versi memuat Declining Balance Rate "25%"
38. Tutup modal Versions
39. Klik `[×]` pada Drawer Edit
40. Baca ulang jumlah entri `DBE-12` di Changelog (Search `DBE-12`), System Log aktor, dan Activity Log seperti langkah 19
41. Verifikasi jumlah entri `DBE-12` di Changelog sama dengan baseline langkah 19
42. Verifikasi jumlah entri `DBE-12` di System Log aktor sama dengan baseline langkah 19
43. Verifikasi jumlah entri `DBE-12` di Activity Log sama dengan baseline langkah 19
44. Buka Settings > Accounting > Tax Depreciation Class
45. Klik `(←)` pada kotak Search

## Notes

- Alasan melewati sekitar 35 langkah (45 langkah, 31 di luar blok baca-log): kedua TC satu topik validasi Declining Balance Rate yang ditolak dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 1, 14 sampai 18 dan 19, 40 sampai 44 adalah blok catat dan baca jumlah entri log (buka surface, cari entri, `Verifikasi` jumlah) yang tidak dihitung menurut prinsip 13 bagian 3.
- Klausa "tidak ada entri log baru" (Expected d TC-FA-TDC-936 dan f TC-FA-TDC-950) diasersi di spec ini sendiri sebagai asersi jumlah dengan baseline (S-12) pada UI yang memicu penolakan, karena TC memberi langkah baseline dan baca ulang sendiri; asersi absence ini tidak diulang di spec absence (S-05: asersi jumlah atau state memakai baseline boleh di spec fungsional). Anchor positif (8b.2): caption validasi (langkah 6 dan 24) dan empty state hasil Search (langkah 12).
- Penutupan form: langkah 9 dan 10 menyalin TC-FA-TDC-936 langkah 5 (`[Clear Field]`, lalu ikon ✕); form Create yang sudah dikosongkan lewat `[Clear Field]` tidak dirty, sehingga tidak ada dialog `Unsaved Changes` (prinsip 3.6). Form Edit yang dirty ditutup deterministik lewat `[×]`, dialog `Unsaved Changes`, `[Leave]` (S-08, langkah 30 sampai 32). Langkah 39 menutup Drawer Edit tanpa perubahan, tanpa dialog.
- Langkah penghubung (S-03): langkah 1 dan 19 (baseline), langkah 11 dan 20 (Search Class Code untuk menemukan baris target; R-16), langkah 13 dan 45 (mengosongkan Search; frasa baku `(←)` pada kotak Search), langkah 14 dan 40 (membaca ulang jumlah entri), langkah 18 dan 44 (membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul; S-14).
- Asersi tambahan di luar Expected TC (S-03): langkah 12 mengamati "class `DBE-01` tidak dibuat" (Expected b TC-FA-TDC-936) lewat Search dengan empty state "No results found" yang juga anchor absence; langkah 7 dan 33 adalah Expected TC (Drawer tetap terbuka; Drawer tertutup sesudah `[Leave]`).
- Langkah 36 dan 37 memecah Expected e TC-FA-TDC-950 (satu baris versi dan nilai "25%") per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-TDC-936 langkah 5 mengklik ikon ✕ setelah `[Clear Field]` tanpa menyebut dialog `Unsaved Changes`; spec mengikuti TC (tanpa dialog) karena form kosong tidak dirty. Perlu konfirmasi FE apakah `[Clear Field]` juga mengosongkan Asset Type dan Allowed Methods.
  - TC-FA-TDC-936 dan TC-FA-TDC-950 membaca jumlah entri log lewat tiga surface tanpa menyebut filter produk FAMS dan cara mencari entri di System Log dan Activity Log; spec membandingkan jumlah entri `DBE-01` atau `DBE-12` (Changelog: Search nama class; System Log dan Activity Log: entri dengan Name class itu).
  - TC-FA-TDC-936 mensyaratkan Class Code `DBE-01` belum ada; spec membersihkan sisa di hook `before` karena kode literal (Class Code maksimal 15 karakter).
  - TC-FA-TDC-936 dan TC-FA-TDC-950 Post Condition "Class `DBE-01` tidak ada" dan "Tidak ada data berubah" tidak punya langkah observasi sendiri selain Expected; tidak ada asersi tambahan (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
