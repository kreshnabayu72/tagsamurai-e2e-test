---
id: TC-FA-TDC-E2E-285-edit-allowed-methods-menambah-dan-melepas-declining-balance-versi-baru-dan-nilai-awal-rate
title: "Edit Allowed Methods: Menambah Declining Balance pada Class Straight Line Saja dan Melepas Declining Balance Membentuk Versi Baru"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-948
  - TC-FA-TDC-951
sourceRules: ["FATDC-LOGIC-03f.2", "FATDC-LOGIC-03f.3", "FATDC-LOGIC-03g.5", "FATDC-LOGIC-04b.4", "V-16", "FI-03"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-03f.2": [4, 7, 9, 14]
  "FATDC-LOGIC-03f.3": [22, 24, 30, 33, 35, 36]
  "FATDC-LOGIC-03g.5": [4, 5, 17, 24, 33, 35, 36]
  "FATDC-LOGIC-04b.4": [13, 14, 17, 26, 29, 30, 35]
  "V-16": [7, 8]
  "FI-03": [4, 5, 23, 24]
coverage:
  web: automated
---

# Edit Allowed Methods: Menambah Declining Balance pada Class Straight Line Saja dan Melepas Declining Balance Membentuk Versi Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; awalan `DBE-` tidak dipakai TC lain; kemampuan seeding disediakan tim FE/BE). Setiap class: Non-building, Useful Life 8, hanya satu versi (Current tanpa Effective From), Active, Used By 0, tanpa versi Scheduled.

| Class Code | Allowed Methods awal | Dipakai TC |
|---|---|---|
| `DBE-10` | `Straight Line` saja | TC-FA-TDC-948 |
| `DBE-13` | `Straight Line` dan `Declining Balance` (Declining Balance Rate 25, End-of-Life Treatment `Charge in final period`) | TC-FA-TDC-951 |

- Tabel memuat tujuh class seed bawaan dan dua class milik spec (9 baris dalam satu halaman); baris target dibuka lewat Search Class Code (8b.13, R-23).
- Tahun pajak 2026 belum tertutup (Exported through belum mencapai Des 2026) sehingga Effective From "Jan 2026" ditawarkan; TC tidak menyebutnya (lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-948: Edit: menambah Declining Balance pada class Straight Line saja menampilkan Declining Balance Rate kosong wajib dan End-of-Life Treatment bernilai awal

1. Ketik Search `DBE-10`, tekan Enter
2. Klik link Class Code `DBE-10` pada tabel
3. Tambahkan `Declining Balance` pada Allowed Methods
4. Verifikasi input Declining Balance Rate (%) tampil kosong
5. Verifikasi End-of-Life Treatment tampil "Charge in final period"
6. Klik `[Save]` tanpa mengisi Declining Balance Rate
7. Verifikasi caption "Declining rate must not be empty" tampil
8. Verifikasi dialog D-09 tidak muncul
9. Isi Declining Balance Rate `25`
10. Klik `[Save]` hingga dialog D-09 muncul
11. Pilih Effective From "Jan 2026"
12. Klik `[Apply]`
13. Verifikasi toast sukses "Success, tax depreciation class has been updated."
14. Verifikasi baris `DBE-10`: Declining Balance Rate "25%" dan Allowed Methods "Straight Line · Declining Balance"
15. Klik link Class Code `DBE-10` pada tabel
16. Klik tautan View versions
17. Verifikasi modal Versions: baris "Jan 2026" berstatus "Current" dengan Declining Balance Rate "25%" dan End-of-Life Treatment "Charge in final period"
18. Tutup modal Versions
19. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-951: Edit: melepas Declining Balance membentuk versi baru tanpa Declining Balance Rate dan End-of-Life Treatment

20. Ganti isi kotak search dengan `DBE-13`, tekan Enter
21. Klik link Class Code `DBE-13` pada tabel
22. Lepas `Declining Balance` dari Allowed Methods
23. Verifikasi Straight Line Rate (%) "12.5" tetap tampil
24. Verifikasi input Declining Balance Rate dan Select End-of-Life Treatment tidak tampil
25. Klik `[Save]`
26. Verifikasi dialog D-09 muncul (guard persempit tidak memblokir karena Used By 0)
27. Pilih Effective From "Jan 2026"
28. Klik `[Apply]`
29. Verifikasi toast sukses "Success, tax depreciation class has been updated."
30. Verifikasi baris `DBE-13`: Declining Balance Rate "—" dan Allowed Methods "Straight Line"
31. Klik link Class Code `DBE-13` pada tabel
32. Verifikasi Allowed Methods "Straight Line" pada Drawer Edit
33. Verifikasi Declining Balance Rate dan End-of-Life Treatment tidak tampil pada Drawer Edit
34. Klik tautan View versions
35. Verifikasi modal Versions: baris "Jan 2026" berstatus "Current" dengan Declining Balance Rate "—" dan End-of-Life Treatment "—"
36. Verifikasi modal Versions: baris "—" berstatus "Past" dengan Declining Balance Rate "25%" dan End-of-Life Treatment "Charge in final period"
37. Tutup modal Versions
38. Klik `[×]` pada Drawer Edit
39. Klik `(←)` pada kotak Search

## Notes

- Alasan melewati sekitar 35 langkah (39 langkah): kedua TC satu topik Edit Allowed Methods yang membentuk versi baru dan berdiri sendiri (tiap TC memakai class sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna).
- Langkah penghubung (S-03): langkah 1 dan 20 (Search Class Code untuk menemukan baris target; R-16); langkah 10 (membuka dialog D-09; TC-FA-TDC-948 tidak punya Expected untuk dialog itu sehingga tanpa `Verifikasi`); langkah 18, 19, 37, dan 38 (menutup modal Versions dan Drawer Edit tanpa perubahan, tanpa dialog `Unsaved Changes`); langkah 39 (mengosongkan Search; S-09).
- Asersi tambahan di luar Expected TC (S-03): langkah 23 (Straight Line Rate "12.5" tetap tampil, Expected a TC-FA-TDC-951) adalah anchor positif untuk asersi absence langkah 24; langkah 32 (Allowed Methods "Straight Line" pada Drawer Edit) adalah anchor untuk asersi absence langkah 33 (8b.2); langkah 7 adalah anchor untuk asersi absence langkah 8.
- Asumsi: sesudah `[Apply]` yang sukses dialog D-09 dan Drawer Edit tertutup sehingga langkah 15 dan 31 membuka Drawer Edit lagi (TC-FA-TDC-951 langkah 6 menulis "Buka Drawer Edit ... lalu klik tautan View versions"); TC-FA-TDC-948 tidak membuka Drawer Edit lagi sebelum View versions, sehingga langkah 15 mengikuti pola TC-FA-TDC-951; perlu konfirmasi FE.
- Temuan untuk QA:
  - TC-FA-TDC-948 dan TC-FA-TDC-951 memilih Effective From "Jan 2026" pada tanggal sistem uji 15 Okt 2026 tanpa menyebut Exported through; spec mengasumsikan tahun pajak 2026 belum tertutup (V-21).
  - TC-FA-TDC-948 Expected d menyebut modal Versions tanpa langkah yang membukanya; spec menambah langkah 15 dan 16 (membuka Drawer Edit lalu View versions) seperti TC-FA-TDC-951.
  - TC-FA-TDC-951 Expected e menyebut Drawer Edit tanpa Declining Balance Rate dan End-of-Life Treatment; spec memakai Allowed Methods sebagai anchor (langkah 32).
  - TC-FA-TDC-948 dan TC-FA-TDC-951 Post Condition tidak punya langkah observasi sendiri selain Expected; tidak ada asersi tambahan (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
