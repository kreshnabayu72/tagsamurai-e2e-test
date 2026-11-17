---
id: TC-FA-TDC-E2E-075-tahun-pajak-tertutup-menolak-effective-from-dan-pilihan-fiscal-year-start
title: "Tahun Pajak Tertutup pada Pilihan Effective From D-09: Closed Tidak Ditawarkan, Sebagian Closed Ditawarkan, dan Apply Ditolak dengan Caption V-21"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-756
  - TC-FA-TDC-757
  - TC-FA-TDC-758
  - TC-FA-TDC-934
sourceRules: ["FATDC-LOGIC-04af", "FATDC-LOGIC-04ag", "FATDC-LOGIC-04e", "FATDC-LOGIC-04t", "V-20", "V-21", "F-FATDC-02.k7b", "E-FATDC-18", "L-03", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04af": [6, 7, 8, 13, 18]
  "FATDC-LOGIC-04ag": 6
  "FATDC-LOGIC-04e": [7, 8, 13, 18]
  "FATDC-LOGIC-04t": 19
  "V-20": 20
  "V-21": 27
  "F-FATDC-02.k7b": 27
  "E-FATDC-18": [28, 29]
  "L-03": 30
  "§4.2c#b1": 33
coverage:
  web: automated
---

# Tahun Pajak Tertutup pada Pilihan Effective From D-09: Closed Tidak Ditawarkan, Sebagian Closed Ditawarkan, dan Apply Ditolak dengan Caption V-21

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global (diubah spec ini, dipulihkan di hook `after` dan di langkah 35): jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00), Fiscal Year Start Januari, dan status periode Accounting Period tahun pajak 2026. Status periode diatur lewat fixture BE Accounting Period (aksi Period Close belum tersedia di UI; disediakan tim FE/BE). Tahun pajak 2027 sampai 2031 belum memiliki periode akuntansi. Hook `before` menyetel keadaan TC-756; hook `after` memulihkan status periode ke keadaan semula.
  - TC-756: periode 2026 Jan sampai Des seluruhnya Closed.
  - TC-757: periode 2026 Jan sampai Nov Closed, satu periode Soft Closed.
  - TC-934: periode 2026 Jan sampai Jun Closed, Jul sampai Des Open.
  - TC-758: periode 2026 seluruhnya Open; Sesi B (fixture BE) mengubah seluruhnya menjadi Closed setelah dialog Save Changes dibuka.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Kemampuan teknis: pembacaan versi dan jumlah entri log Changelog class lewat fixture BE (disediakan tim FE/BE); sesi API aktor / fixture BE sebagai pelaku kedua (Sesi B) pada TC-758.
- Data Pre-setup (hanya dibaca, tidak diubah; Apply tidak pernah berhasil di spec ini, sehingga Last Updated tidak berubah): class Example Data `NB-4` (Non-building, Useful Life 20, hanya versi pertama tanpa Effective From).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `NB-4`, tekan Enter
2. Klik link Class Code `NB-4` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`

### TC-FA-TDC-756: Tahun pajak dengan seluruh periode Closed tidak ditawarkan

5. Klik field Effective From
6. Verifikasi pilihan yang ditawarkan berlabel `Jan 2027`, `Jan 2028`, `Jan 2029`, `Jan 2030`, dan `Jan 2031`
7. Verifikasi pilihan Effective From tidak memuat `Jan 2026`
8. Verifikasi `Jan 2029` tetap ditawarkan walau tahun pajak 2029 belum memiliki periode akuntansi
9. Klik `[Cancel]` pada dialog Save Changes

### TC-FA-TDC-757: Tahun pajak dengan periode Soft Closed tetap ditawarkan

10. Ubah status periode 2026 menjadi 11 periode Closed dan satu periode Soft Closed lewat fixture BE hingga tersimpan
11. Klik `[Save]`
12. Klik field Effective From
13. Verifikasi pilihan Effective From memuat `Jan 2026`, `Jan 2027`, `Jan 2028`, `Jan 2029`, `Jan 2030`, dan `Jan 2031`
14. Klik `[Cancel]` pada dialog Save Changes

### TC-FA-TDC-934: Tahun pajak yang hanya sebagian periodenya Closed tetap ditawarkan

15. Ubah status periode 2026 menjadi Jan sampai Jun Closed dan Jul sampai Des Open lewat fixture BE hingga tersimpan
16. Klik `[Save]`
17. Klik field Effective From
18. Verifikasi pilihan Effective From memuat `Jan 2026`, `Jan 2027`, `Jan 2028`, `Jan 2029`, `Jan 2030`, dan `Jan 2031`
19. Verifikasi nilai awal terpilih `Jan 2026`
20. Verifikasi tidak ada caption error pada Effective From
21. Klik `[Cancel]` pada dialog Save Changes

### TC-FA-TDC-758: Apply ditolak dengan caption V-21 setelah tahun pajak terpilih menjadi tertutup

22. Ubah seluruh periode 2026 menjadi Open lewat fixture BE hingga tersimpan
23. Catat jumlah entri log Changelog class `NB-4` sebagai baseline lewat fixture BE
24. Klik `[Save]`
25. Ubah seluruh periode 2026 menjadi Closed (Sesi B) lewat fixture BE hingga tersimpan
26. Klik `[Apply]` dengan Effective From bernilai awal `Jan 2026`
27. Verifikasi caption `Tax year 2026 is closed. Choose a later tax year.` tampil pada dialog Save Changes
28. Verifikasi dialog Save Changes tetap terbuka
29. Verifikasi Useful Life Current `NB-4` tetap `20` (dibaca lewat fixture BE)
30. Verifikasi jumlah entri log Changelog class `NB-4` sama dengan baseline (selisih 0)
31. Klik `[Cancel]` pada dialog Save Changes
32. Klik `[×]` pada Drawer Edit
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`
35. Pulihkan status periode Accounting Period tahun pajak 2026 ke keadaan semula lewat fixture BE hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 9, 14, 21, dan 31 (menutup dialog Save Changes dengan `[Cancel]` agar status periode dapat diubah dan dialog dibuka ulang), langkah 10, 15, dan 22 (mengatur status periode untuk TC berikutnya; pelaku lewat fixture BE, R-20), langkah 32 sampai 34 (menutup Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08), langkah 35 (pemulihan state global).
- Keempat TC memakai satu Drawer Edit `NB-4` yang dibuka pada langkah 2 sampai 4; langkah 1 dan 2 tiap TC berikutnya identik dengan keadaan yang sudah terbentuk (Useful Life `10`), dan dialog dibuka ulang dengan `[Save]` agar pilihan Effective From dihitung dari status periode terbaru. Urutan TC: 756, 757, 934, 758 (TC yang berakhir dengan penolakan Apply paling akhir; S-10).
- Absence pada langkah 7: anchor positif adalah langkah 6. Absence pada langkah 20: anchor positif adalah langkah 18 dan 19. Absence jumlah entri log pada langkah 30: anchor positif adalah caption penolakan (langkah 27) dan baseline langkah 23 (S-12).
- P-1 (state berat): asersi "tidak ada entri log baru" (TC-758 Expected b) ditulis di spec ini dengan baseline karena bergantung pada keadaan periode Closed yang baru dibentuk Sesi B pada langkah 25.
- Temuan untuk QA:
  - TC-758 Expected b ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Changelog class `NB-4` dibaca lewat fixture BE sebagai satu-satunya surface yang dapat diasersi. QA perlu menetapkan surface log (Changelog, System Log, Activity Log).
  - TC-756 sampai 934 memakai class Example Data `NB-4`, bukan class milik spec bersuffix; spec hanya membaca `NB-4` dan Apply tidak pernah berhasil (S-06). Bila Example Data diubah test lain, Useful Life Current `20` pada TC-758 dapat tidak berlaku.
  - TC-756 Precondition e menyebut "Class NB-4 hanya memiliki versi pertama tanpa Effective From" tanpa menyebut Used By; tidak diasersi.
  - TC-758 Post Condition ("Useful Life baru 10" pada kolom Data Uji) tidak diasersi karena Apply ditolak.
  - Tahun pajak 2027 sampai 2031 tanpa periode akuntansi disiapkan tim FE/BE; TC tidak menyebut cara menyiapkannya.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
