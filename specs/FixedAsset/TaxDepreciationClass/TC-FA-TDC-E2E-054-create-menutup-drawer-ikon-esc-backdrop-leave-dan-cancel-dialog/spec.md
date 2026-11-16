---
id: TC-FA-TDC-E2E-054-create-menutup-drawer-ikon-esc-backdrop-leave-dan-cancel-dialog
title: "Create - Menutup Drawer Lewat Ikon, Esc, Backdrop, Leave, dan Cancel Dialog"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-118
  - TC-FA-TDC-119
  - TC-FA-TDC-120
  - TC-FA-TDC-121
  - TC-FA-TDC-122
sourceRules: ["§12#r11", "§4.2c#b1", "§4.5#b1"]
smoke: []
dependsOn: []
trace:
  "§12#r11": 3
  "§4.2c#b1": [4, 8, 12, 18, 20, 21, 26, 28, 29, 31]
  "§4.5#b1": [7, 14]
anchor: [11, 22]
coverage:
  web: automated
---

# Create - Menutup Drawer Lewat Ikon, Esc, Backdrop, Leave, dan Cancel Dialog

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (tidak ada Submit). Class Code yang diketik `KHS-12` (literal TC; Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; tidak disimpan, suite serial, kode berbeda antar spec).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-118: Tutup Drawer Create kosong lewat ikon ✕ tanpa dialog

1. Klik `+ Class` di toolbar
2. Klik ikon ✕
3. Verifikasi Drawer langsung tertutup
4. Verifikasi dialog Unsaved Changes tidak muncul

### TC-FA-TDC-119: Tutup Drawer Create kosong lewat Esc tanpa dialog

5. Klik `+ Class` di toolbar
6. Tekan `Esc`
7. Verifikasi Drawer langsung tertutup
8. Verifikasi dialog Unsaved Changes tidak muncul

### TC-FA-TDC-120: Klik backdrop tidak menutup Drawer Create

9. Klik `+ Class` di toolbar
10. Klik area gelap di luar Drawer (backdrop)
11. Verifikasi Drawer tetap terbuka
12. Verifikasi dialog Unsaved Changes tidak muncul
13. Tekan `Esc`
14. Verifikasi Drawer tertutup

### TC-FA-TDC-121: Tutup Drawer Create terisi lewat ikon ✕ lalu pilih Leave

15. Klik `+ Class` di toolbar
16. Isi Class Code `KHS-12`
17. Klik ikon ✕
18. Verifikasi dialog dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
19. Pada dialog, klik `[Leave]`
20. Verifikasi dialog dan Drawer tertutup
21. Verifikasi class `KHS-12` tidak tersimpan: tabel tetap berisi 7 class seed tanpa baris baru
22. Verifikasi tidak ada toast

### TC-FA-TDC-122: Tutup Drawer Create terisi lewat Esc lalu pilih Cancel pada dialog

23. Klik `+ Class` di toolbar
24. Isi Class Code `KHS-12`
25. Tekan `Esc`
26. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
27. Pada dialog, klik `[Cancel]`
28. Verifikasi dialog tertutup
29. Verifikasi Drawer tetap terbuka dengan Class Code `KHS-12` dipertahankan
30. Klik ikon ✕
31. Verifikasi dialog Unsaved Changes tampil
32. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 30 sampai 32 (menutup Drawer dirty dengan `[×]`, verifikasi dialog `Unsaved Changes`, dan klik `[Leave]` sesuai S-08, sebagai pemulihan akhir spec; verifikasi dialog tidak perlu dicatat lagi di Notes).
- Menutup form di akhir spec (prinsip 6): TC-FA-TDC-122 diletakkan paling akhir karena meninggalkan Drawer dirty; TC-FA-TDC-121 memakai Drawer terisi yang ditutup dengan Leave.
- Asersi absence langkah 4, 8, dan 12 didahului anchor positif pada Drawer yang sama (Drawer tertutup pada langkah 3 dan 7; Drawer tetap terbuka pada langkah 11; 8b.2). Asersi absence langkah 22 (tidak ada toast) segera sesudah pemicu dan didahului anchor positif langkah 20 (8b.11).
- Jumlah pembukaan Drawer Create (langkah 1, 5, 9, 15, 23) sama dengan jumlah penutupan (langkah 2, 6, 13, 19, 32) (S-10).
- Pembagian TC lintas spec: reload dan konfirmasi bawaan browser (TC-FA-TDC-123 sampai 125) ada di spec `TC-FA-TDC-E2E-055-create-field-dikembalikan-kosong-reload-dan-konfirmasi-bawaan-browser`.
- Temuan untuk QA:
  - TC-FA-TDC-120 tidak mencantumkan Master Data Count Limit pada Precondition (berbeda dari TC Create lain); spec memakai kondisi yang sama (belum tercapai).
  - Post Condition TC-FA-TDC-121 ("Tidak ada entri log") tidak punya langkah observasi di TC; spec tidak mengasersinya (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
