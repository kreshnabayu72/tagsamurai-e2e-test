---
id: TC-AC-ACTS-E2E-088-add-stock-gps-cancel-meninggalkan-halaman-dan-reload-dengan-preview
title: "Add Stock GPS: Cancel dan Meninggalkan Halaman dengan Preview Berisi atau Kosong, Reload, serta Pilih Cancel Tetap di Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-254
  - TC-AC-ACTS-255
  - TC-AC-ACTS-256
  - TC-AC-ACTS-257
  - TC-AC-ACTS-258
  - TC-AC-ACTS-899
  - TC-AC-ACTS-900
coverage:
  web: automated
---

# Add Stock GPS: Cancel dan Meninggalkan Halaman dengan Preview Berisi atau Kosong, Reload, serta Pilih Cancel Tetap di Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. Spec ini tidak menekan `[Submit]`, sehingga tidak ada unit yang perlu dihapus. Preview berisi diisi lewat Manual Entry (dipakai sebagai precondition TC, tidak diasersi).
- Kemampuan teknis disediakan tim FE: penanganan dialog `beforeunload` browser (TC-AC-ACTS-258).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-900: [Cancel] dengan Preview kosong langsung keluar

1. Klik `[Cancel]` pada Preview kosong
2. Verifikasi halaman Detail SKU `GPS-TRACK-CORE-G3` Tab Available tampil
3. Verifikasi tidak ada dialog Unsaved Changes
4. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)

### TC-AC-ACTS-257: Meninggalkan halaman dengan Preview kosong langsung keluar

5. Klik breadcrumb `Stock`
6. Verifikasi Stock List tampil
7. Verifikasi tidak ada dialog Unsaved Changes
8. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)

### TC-AC-ACTS-254: [Cancel] dengan Preview berisi memunculkan dialog Unsaved Changes; pilih [Leave] membuang Preview dan keluar

9. Tambahkan tiga IMEI `356938035643809`, `356938035643811`, dan `356938035643812` lewat Manual Entry
10. Klik `[Cancel]`
11. Verifikasi dialog Unsaved Changes baku "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
12. Klik `[Leave]` pada dialog
13. Verifikasi halaman keluar ke Detail SKU `GPS-TRACK-CORE-G3` Tab Available
14. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
15. Verifikasi Preview dibuang tanpa Submit (Preview kosong)

### TC-AC-ACTS-255: Meninggalkan halaman dengan Preview berisi, pilih [Leave]

16. Tambahkan dua IMEI `356938035643809` dan `356938035643811` lewat Manual Entry
17. Klik breadcrumb `Stock`
18. Verifikasi dialog Unsaved Changes baku "You have unsaved changes. Are you sure you want to leave?" dengan `[Cancel]` dan `[Leave]`
19. Klik `[Leave]` pada dialog
20. Verifikasi halaman keluar ke Stock List
21. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
22. Verifikasi Preview dibuang (Preview kosong)

### TC-AC-ACTS-256: Meninggalkan halaman dengan Preview berisi, pilih [Cancel]

23. Tambahkan dua IMEI `356938035643809` dan `356938035643811` lewat Manual Entry
24. Klik breadcrumb `Stock`
25. Verifikasi dialog Unsaved Changes baku "You have unsaved changes. Are you sure you want to leave?" dengan `[Cancel]` dan `[Leave]`
26. Klik `[Cancel]` pada dialog
27. Verifikasi tetap di halaman Add Stock
28. Verifikasi Preview utuh (dua baris tetap ada)
29. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-899: [Cancel] dengan Preview berisi, pilih [Cancel] tetap di halaman

30. Tambahkan tiga IMEI `356938035643809`, `356938035643811`, dan `356938035643812` lewat Manual Entry
31. Klik `[Cancel]` pada halaman
32. Verifikasi dialog Unsaved Changes baku "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
33. Klik `[Cancel]` pada dialog
34. Verifikasi dialog tertutup
35. Verifikasi tetap di halaman Add Stock
36. Verifikasi Preview masih berisi 3 baris
37. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-258: Reload saat Preview berisi memunculkan konfirmasi browser

38. Tambahkan dua IMEI `356938035643809` dan `356938035643811` lewat Manual Entry
39. Tekan F5
40. Verifikasi konfirmasi bawaan browser muncul
41. Batalkan konfirmasi browser (tetap di halaman)
42. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (42 langkah); alasan: semua blok satu kelas harness dan satu halaman, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; sekitar sepertiga langkah adalah penyiapan Preview dan pembukaan kembali halaman yang diperlukan TC-AC-ACTS-900 sampai TC-AC-ACTS-258 karena keluar halaman adalah objek uji.
- Urutan TC: TC-AC-ACTS-900 dan TC-AC-ACTS-257 (Preview kosong) lebih dulu, lalu TC-AC-ACTS-254 sampai TC-AC-ACTS-899, dan TC-AC-ACTS-258 terakhir (S-10).
- Langkah penghubung tanpa Verifikasi (S-03): pengisian Preview lewat Manual Entry, "Buka kembali halaman Add Stock", "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" (S-09), dan "Batalkan konfirmasi browser" (penanganan dialog `beforeunload` tertulis di Prerequisites, S-08).
- Temuan untuk QA:
  - TC-AC-ACTS-254 dan TC-AC-ACTS-255 menyebut "Preview dibuang" tanpa cara mengamati; spec membuka kembali halaman Add Stock dan memeriksa Preview kosong.
  - TC-AC-ACTS-258 menyebut "Reload atau tutup tab" tetapi langkahnya hanya F5; spec menulis F5 saja.
