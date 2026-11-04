---
id: TC-FA-TDC-E2E-138-konflik-popup-used-by-kosong-dan-log-activate-deactivate-idempoten
title: "Konflik Dua Sesi: Popup Used By Kosong pada Data Usang dan Log Activate serta Deactivate yang Idempoten"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-586
  - TC-FA-TDC-720
  - TC-FA-TDC-721
coverage:
  web: automated
---

# Konflik Dua Sesi: Popup Used By Kosong pada Data Usang dan Log Activate serta Deactivate yang Idempoten

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A (sesi 1): Total Control (company uji Fixed Asset). Role diuji dibaca dari Precondition TC-FA-TDC-586 butir a ("dua sesi Total Control"); email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B atau sesi 2): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state (melepas Asset Class pemakai, mengaktifkan, menonaktifkan class) dan hasilnya tidak diasersi di sesi itu; hasil log milik sesi B dibaca pada langkah 19 sampai 21 lewat Detail User aktor sesi B.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Used By lewat Asset Class pemakai), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah entri Changelog, System Log aktor, dan Activity Log lewat fixture BE (disediakan tim FE/BE) untuk baseline (S-12).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4Dipakai` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 1 (satu Asset Class pemakai milik spec) pada TC-FA-TDC-586; Used By 0 pada TC-FA-TDC-721 |
| `nbOld` | `NB-OLD` | Inactive, Used By 0 |

- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-586: Popup Used By, Empty State saat tidak ada pemakai lagi

1. Ketik Search `NB-4`, tekan Enter
2. Sesi 2 (sesi API): lepaskan Asset Class pemakai dari `NB-4` hingga Used By 0 tersimpan
3. Sesi 1: klik angka `1` pada baris `NB-4`
4. Verifikasi Popup Used By menampilkan Illustration dengan Title `Not used yet` dan Description `Asset classes that use this class will appear here.`
5. Tekan Esc untuk menutup Popup Used By
6. Klik `(←)` pada kotak Search

### TC-FA-TDC-720: Activate idempoten karena class sudah Active tidak menambah log

7. Ketik Search `NB-OLD`, tekan Enter
8. Catat baseline jumlah entri Changelog dan Activity Log untuk `NB-OLD` serta jumlah entri System Log Detail User aktor sesi A dan sesi B lewat fixture BE
9. Sesi A: klik toggle `Active` baris `NB-OLD`
10. Sesi B (sesi API): aktifkan `NB-OLD` hingga status Active tersimpan
11. Sesi A: klik `[Activate]`
12. Tunggu aksi selesai
13. Klik ikon Changelog di toolbar
14. Verifikasi jumlah entri Changelog `NB-OLD` bertambah tepat satu dari baseline langkah 8
15. Verifikasi baris teratas Changelog `NB-OLD` memuat Status Inactive ke Active
16. Tutup modal Changelog
17. Buka Detail User aktor sesi A > Tab System Log
18. Verifikasi jumlah entri System Log aktor sesi A sama dengan baseline langkah 8 (tidak ada baris Status `NB-OLD`)
19. Buka Detail User aktor sesi B > Tab System Log
20. Verifikasi jumlah entri System Log aktor sesi B bertambah tepat satu dari baseline langkah 8
21. Verifikasi baris teratas System Log aktor sesi B memuat Status Inactive ke Active untuk `NB-OLD`
22. Buka `Reports & Logs > Activity Log`, tab `User Action`
23. Verifikasi jumlah entri Activity Log `NB-OLD` bertambah tepat satu dari baseline langkah 8
24. Verifikasi baris teratas Activity Log `NB-OLD` memuat Status Inactive ke Active

### TC-FA-TDC-721: Deactivate idempoten karena class sudah Inactive tidak menambah log

25. Pulihkan class `NB-4` lewat seeding API ke Active dengan Used By 0
26. Buka Fixed Asset > Settings > Accounting > Tax Depreciation Class
27. Ketik Search `NB-4`, tekan Enter
28. Catat baseline jumlah entri Changelog dan Activity Log untuk `NB-4` lewat fixture BE
29. Sesi A: klik toggle `Active` baris `NB-4`
30. Sesi B (sesi API): nonaktifkan `NB-4` hingga status Inactive tersimpan
31. Sesi A: klik `[Deactivate]`
32. Tunggu aksi selesai
33. Klik ikon Changelog di toolbar
34. Verifikasi jumlah entri Changelog `NB-4` bertambah tepat satu dari baseline langkah 28
35. Verifikasi baris teratas Changelog `NB-4` memuat Status Active ke Inactive
36. Tutup modal Changelog
37. Buka `Reports & Logs > Activity Log`, tab `User Action`
38. Verifikasi jumlah entri Activity Log `NB-4` bertambah tepat satu dari baseline langkah 28
39. Verifikasi baris teratas Activity Log `NB-4` memuat Status Active ke Inactive

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 7, dan 27 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 5 dan 6 (menutup Popup Used By dan mengosongkan Search), langkah 16 dan 36 (menutup modal Changelog), langkah 25 (membentuk precondition TC-FA-TDC-721), langkah 26 (kembali ke modul asal sesudah mengunjungi Activity Log dan Detail User; S-14). Langkah 8 dan 28 mencatat baseline (S-12, 8b.10). Langkah 12 dan 32 ("Tunggu aksi selesai", tanpa Verifikasi) menunggu `[Activate]` dan `[Deactivate]` selesai sebelum membuka Changelog (8b.8, S-03).
- Langkah 2, 10, dan 30 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20); sesi A tetap memegang dialog yang terbuka sebelum sesi B bertindak. Langkah 2 mengosongkan Used By di server sementara sesi 1 masih menampilkan Used By `1` dari data tabel usang (langkah 3 mengklik angka itu). Dialog Activate dan Deactivate yang dibuka sesi A pada langkah 9 dan 29 tetap terbuka (belum Confirm) sampai sesi B selesai bertindak.
- Langkah 18 (Expected b TC-FA-TDC-720, System Log aktor sesi A tidak memuat baris Status): asersi absence memakai surface agregat, yaitu jumlah entri sebelum dan sesudah (8b.2, S-12); langkah 20 dan 21 pada System Log aktor sesi B menunjukkan bahwa log sesi B tercatat di surface yang sama jenisnya. Entri baru dibaca pada baris teratas setelah selisih jumlah dari baseline dibuktikan (S-14).
- Alasan spec melewati sekitar 35 langkah (39 langkah): ketiga blok adalah kelas c pada dua sesi atas class yang sama dan berdiri sendiri; langkah tambahan berasal dari pembacaan tiga surface log per TC (S-01 satu `Verifikasi` per klausa).
- Temuan untuk QA:
  - Email akun Total Control (sesi 1 dan sesi 2) tidak tertulis di Pre-setup TC (S-11): disediakan tim FE. TC-FA-TDC-586 tidak menyebut company atau akun; role dibaca dari Precondition a.
  - Class Code `NB-4` dan `NB-OLD` ditulis literal tanpa suffix `{runId}-<NNN>`; kode ini dipakai TC apa adanya dan menjadi target aksi tulis (S-06, S-12). Lampiran A konvensi belum memuat pengecualian untuk modul ini; class diseed dan dipulihkan lewat fixture pada company/state khusus automation.
  - TC-FA-TDC-720 Expected a menyebut "tepat satu baris" pada Changelog dan Activity Log; spec membuktikannya sebagai selisih satu terhadap baseline karena audit trail permanen (S-12), bukan angka absolut.
  - TC-FA-TDC-721 Expected hanya menyebut Changelog dan Activity Log; System Log tidak diasersi.
  - TC-FA-TDC-586 langkah 1 menyebut klik angka `1` pada data usang tanpa menyebut cara membuat Used By tetap 1 di sesi 1; spec mencari baris `NB-4` lewat Search sebelum sesi 2 melepas pemakai sehingga tabel sesi 1 tetap menampilkan `1`.
  - Kolom Automation TC-FA-TDC-586 memuat `Manual Only — (d) dua sesi pengguna paralel`, TC-FA-TDC-720 dan TC-FA-TDC-721 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
