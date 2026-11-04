---
id: TC-FA-TDC-E2E-037-batas-master-data-count-limit-dialog-d-07-screening-ok-esc-dan-fokus
title: "Batas Master Data Count Limit: Dialog D-07 Tax Depreciation Class Limit Reached, Screening, Tombol OK, Esc, dan Fokus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-126
  - TC-FA-TDC-127
  - TC-FA-TDC-128
  - TC-FA-TDC-129
  - TC-FA-TDC-919
coverage:
  web: automated
---

# Batas Master Data Count Limit: Dialog D-07 Tax Depreciation Class Limit Reached, Screening, Tombol OK, Esc, dan Fokus

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (kelas e, volume data; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): Master Data Count Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits bernilai 1000 (nilai minimum) dan total Tax Depreciation Class (semua status) = 1000, yaitu 7 class seed bawaan ditambah 993 class tambahan yang dibuat lewat API pre-setup di hook `before`. Total 1000 berasal dari seeding (8b.10).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengatur Master Data Count Limit dan membuat 993 class tambahan lewat fixture BE.
- State global: Master Data Count Limit dan 993 class tambahan. Hook `after` menghapus 993 class tambahan dan memulihkan Master Data Count Limit ke nilai awal.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-126, TC-FA-TDC-127, dan TC-FA-TDC-919: Dialog D-07 muncul, screening, fokus, dan Esc

1. Catat isi halaman pertama tabel Tax Depreciation Class
2. Klik `+ Class` di toolbar
3. Verifikasi dialog D-07 muncul
4. Verifikasi Drawer Add Tax Depreciation Class tidak terbuka
5. Verifikasi header dialog berjudul "Tax Depreciation Class Limit Reached"
6. Verifikasi body dialog berteks "You've reached the platform limit of 1000 records. Contact support if you need a higher limit."
7. Verifikasi footer dialog memuat satu tombol `[OK]`
8. Verifikasi tombol `[Cancel]` tidak ada
9. Tekan Tab berulang
10. Verifikasi fokus tetap di dalam dialog D-07 pada satu-satunya tombol `[OK]` dan tidak keluar ke halaman
11. Tekan Esc
12. Verifikasi dialog D-07 tertutup
13. Verifikasi Drawer Create tidak terbuka

### TC-FA-TDC-129: Esc pada dialog D-07

14. Klik `+ Class` di toolbar
15. Verifikasi dialog D-07 muncul
16. Tekan `Esc` saat dialog D-07 terbuka
17. Verifikasi dialog D-07 tertutup
18. Verifikasi Drawer Create tidak terbuka
19. Verifikasi tidak ada toast tampil

### TC-FA-TDC-128: Tombol OK pada dialog D-07

20. Klik `+ Class` di toolbar
21. Verifikasi dialog D-07 muncul
22. Klik `[OK]` pada dialog D-07
23. Verifikasi dialog D-07 tertutup
24. Verifikasi Drawer Create tidak terbuka
25. Verifikasi tidak ada toast tampil
26. Verifikasi tabel tidak berubah: isi halaman pertama sama dengan catatan pada langkah 1

## Notes

- Urutan TC diubah dan satu pembukaan dialog dipakai bersama: langkah 1 TC-FA-TDC-126, 127, dan 919 sama (klik `+ Class`), sehingga satu pembukaan pada langkah 2 memenuhi ketiganya; TC-FA-TDC-919 butir b (Esc menutup dialog) dipenuhi langkah 11 sampai 13. TC-FA-TDC-129 dan 128 membuka dialog sendiri (langkah 14 dan 20) karena langkah Esc dan `[OK]` adalah objek ujinya. Screening dialog (TC-FA-TDC-127) diletakkan di awal (S-10).
- Langkah penghubung (S-03): langkah 1 mencatat isi halaman pertama sebagai pembanding "tabel tidak berubah" (langkah 26). Langkah 15 dan 21 adalah anchor positif untuk asersi absence toast pada langkah 19 dan 25 (8b.2, 8b.11); langkah 7 adalah anchor positif untuk langkah 8.
- Post Condition TC-FA-TDC-126 dan 128 ("tidak ada entri log" / "tidak ada data berubah") tidak memiliki langkah observasi di TC dan tidak diasersi (S-01, S-05); absence log tidak dirujuk di spec absence.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control.
  - TC-FA-TDC-126, 127, 128, 129, dan 919 menyebut limit 1000 "993 tambahan dibuat lewat API pre-setup"; spec menyebut seeding oleh fixture BE tanpa endpoint karangan.
  - TC-FA-TDC-128 butir d "Tabel tidak berubah" tidak menyebut cara membandingkan; spec membandingkan isi halaman pertama.
  - TC-FA-TDC-919 butir a ("Tekan Tab berulang") tidak menyebut jumlah penekanan Tab.
