---
id: TC-FA-LIC-E2E-017-mobile-filter-panel-bottom-sheet-toolbar-modal-sebagai
title: "Mobile: Filter Panel Bottom Sheet, Toolbar, Modal sebagai Bottom Sheet, dan Banner"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-79
  - TC-FA-LIC-520
  - TC-FA-LIC-521
coverage:
  web: automated
---

# Mobile: Filter Panel Bottom Sheet, Toolbar, Modal sebagai Bottom Sheet, dan Banner

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite pada viewport desktop. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan viewport desktop.
- Data Pre-setup: kuota dan hierarki #12, riwayat #13, sesi aktif #14 (kartu Budi Santoso); fixture banner #15 (term live Active PT Sejahtera, Plan Owner `PT Maju Bersama`, End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1, Grace End 30/01/27). Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: ukuran viewport diubah ke mobile pada langkah 1 dan dipulihkan pada langkah 31; tanggal "hari ini" fixture banner disetel 01/12/26 (N = 30) pada langkah 26 (TC-FA-LIC-79) dan dipulihkan pada langkah 30. Hook `after` memulihkan tanggal fixture dan viewport bila spec gagal di tengah. Fixture BE penyetel tanggal dan kemampuan mengubah viewport disediakan tim FE/BE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE, pemulihan preferensi kolom): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-520: Filter Panel Bottom Sheet, toolbar `[⋯]`, `[🔍]`, dan Changelog di header halaman

1. Ubah viewport ke ukuran mobile
2. Klik Tab `Concurrent User`
3. Verifikasi toolbar menampilkan `[⋯]` dan `[🔍]`
4. Ketuk `[⋯]`
5. Verifikasi `[⋯]` membuka bottom sheet berisi Column Visibility dan Filter (tanpa Download pada tab ini)
6. Verifikasi bottom sheet `[⋯]` tidak memuat ikon Changelog
7. Pilih Filter
8. Verifikasi Filter Panel terbuka sebagai Bottom Sheet Drawer
9. Tutup Filter Panel
10. Ketuk `[🔍]`
11. Verifikasi `[🔍]` memperluas kotak pencarian inline
12. Verifikasi ikon Changelog berada di header halaman

### TC-FA-LIC-521: Modal dan dialog tampil sebagai bottom sheet

13. Ketik Search `Budi Santoso`, tekan Enter
14. Ketuk `[Force Logout]` pada kartu `Budi Santoso`
15. Verifikasi dialog `Force Logout User` tampil sebagai bottom sheet
16. Verifikasi dialog memuat Title, Body, `[Cancel]`, dan `[Confirm Logout]`
17. Klik `[Cancel]`
18. Klik `(←)` pada kotak Search
19. Klik ikon Changelog di header halaman
20. Verifikasi modal `Changelog: Concurrent User` tampil sebagai bottom sheet
21. Tutup modal `Changelog: Concurrent User` dengan `[×]`
22. Ketuk `[⋯]`
23. Buka Setup Column dari bottom sheet `[⋯]`
24. Verifikasi popup Setup Column tampil sebagai bottom sheet
25. Tutup popup Setup Column dengan `×`

### TC-FA-LIC-79: Banner tampil di atas Tabs Bar pada layout mobile

26. Setel tanggal "hari ini" fixture ke 01/12/26 (N = 30) lewat fixture BE, lalu muat ulang halaman License
27. Verifikasi banner full width tampil di atas Tabs Bar
28. Verifikasi Title dan Body banner ditumpuk vertikal
29. Verifikasi tombol `[×]` banner berada di pojok kanan atas
30. Pulihkan tanggal "hari ini" fixture lewat fixture BE
31. Pulihkan viewport ke ukuran desktop

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-79, 520, 521). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-520 dan TC-521 (Tab `Concurrent User`) di awal dan TC-79 (mengubah tanggal fixture) di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1 (mengubah viewport sesuai Precondition), langkah 2 (klik Tab), langkah 9, 17, 21, 25 (menutup panel, dialog, modal, dan popup), langkah 30 dan 31 (pemulihan). Modal dan popup ditutup tanpa perubahan sehingga dialog `Unsaved Changes` tidak muncul.
- Kartu `Budi Santoso` di tabel Active Sessions (18 sesi, lebih dari satu halaman) dibuka lewat Search sebagai langkah penghubung (R-16, bagian 8b butir 13): langkah 13 mengetik Search pada kotak pencarian inline yang sudah diperluas langkah 10, dan langkah 18 membersihkannya dengan `(←)` (S-09).
- Langkah 6 mengasersi klausa TC-520 butir e bagian "bukan di bottom sheet `[⋯]`" saat bottom sheet terbuka; langkah 12 mengasersi bagian "di header halaman".
- Temuan untuk QA:
  - TC-521 Expected a menyebut dialog `Force Logout User` memiliki "Title, Body" tanpa teks; spec hanya mengasersi keberadaan keempat elemen.
  - TC-521 langkah 4 ("Buka Setup Column dari bottom sheet `[⋯]`") tidak menyebut label item; spec memakai `Setup Column` tanpa elipsis pada langkah 23.
