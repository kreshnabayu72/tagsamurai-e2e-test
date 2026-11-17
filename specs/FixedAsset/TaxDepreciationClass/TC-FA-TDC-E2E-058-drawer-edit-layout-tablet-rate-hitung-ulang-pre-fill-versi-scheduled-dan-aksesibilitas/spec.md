---
id: TC-FA-TDC-E2E-058-drawer-edit-layout-tablet-rate-hitung-ulang-pre-fill-versi-scheduled-dan-aksesibilitas
title: "Drawer Edit: Layout Tablet, Rate Dihitung Ulang, Pre-fill Versi Scheduled, dan Aksesibilitas Keyboard"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-37
  - TC-FA-TDC-187
  - TC-FA-TDC-188
  - TC-FA-TDC-247
sourceRules: ["§4.5#b6", "FATDC-LOGIC-03f.4", "FATDC-LOGIC-03f.1", "FATDC-LOGIC-03f.2", "ST-10", "FI-03", "§4.2c#b1", "FATDC-LOGIC-04q.1", "§4.1.2#r10", "§4.5#b1", "§4.1#r2", "FATDC-LOGIC-04ad", "§4.5#b2"]
smoke: []
dependsOn: []
trace:
  "§4.5#b6": [4, 6]
  "FATDC-LOGIC-03f.4": [12, 13, 15, 18, 21]
  "FATDC-LOGIC-03f.1": [12, 29]
  "FATDC-LOGIC-03f.2": 13
  "ST-10": [15, 18, 21, 30]
  "FI-03": 16
  "§4.2c#b1": [23, 41]
  "FATDC-LOGIC-04q.1": [27, 28, 29]
  "§4.1.2#r10": 31
  "§4.5#b1": [36, 38, 40]
  "§4.1#r2": 36
  "FATDC-LOGIC-04ad": 36
  "§4.5#b2": 37
anchor: [19]
coverage:
  web: automated
---

# Drawer Edit: Layout Tablet, Rate Dihitung Ulang, Pre-fill Versi Scheduled, dan Aksesibilitas Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk versi Scheduled), flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- Kemampuan teknis: mengatur ukuran viewport browser (lebar tablet) dan memulihkannya; hook `after` memulihkan viewport ke ukuran semula sebagai cadangan.
- Data (seed idempotent di hook `before` lewat API, class `KHS-*` dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb1` | `NB-1` | Pre-setup Example Data (Used By 5, Active); hanya dibuka dan ditutup tanpa Save |
| `khsE1` | `KHS-E1` | Non-building, Useful Life `8`, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok edit uji`, Active, Used By 0, tanpa versi Scheduled, Last Posted Tax Year kosong |
| `khsV1` | `KHS-V1` | Versi Current Useful Life `8` (Straight Line dan Declining Balance) dan versi Scheduled Effective From Jan 2027 dengan Useful Life `10` (Straight Line saja) |

- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-37: Layout lebar tablet

1. Atur viewport browser ke lebar tablet
2. Ketik Search `NB-1`, tekan Enter
3. Geser tabel secara horizontal
4. Verifikasi tabel menampilkan horizontal scroll sehingga kolom Active, Class Code, Class Name, Asset Type, Useful Life (years), Straight Line Rate, Declining Balance Rate, Allowed Methods, Used By, dan Effective From dapat dijangkau
5. Klik link Class Code `NB-1`
6. Verifikasi field di Drawer disusun satu kolom
7. Klik ikon ✕
8. Pulihkan viewport browser ke ukuran semula

### TC-FA-TDC-187: Rate dihitung ulang seketika

9. Ganti isi kotak search dengan `KHS-E1`, tekan Enter
10. Klik link Class Code `KHS-E1`
11. Ganti Useful Life menjadi `10`
12. Verifikasi Straight Line Rate (%) `10`
13. Verifikasi Declining Balance Rate (%) `20` tanpa Save
14. Lepas pilihan `Declining Balance`
15. Verifikasi Declining Balance Rate (%) tidak tampil
16. Verifikasi Straight Line Rate (%) tetap `10`
17. Pilih kembali `Declining Balance`
18. Verifikasi Declining Balance Rate (%) `20` tampil
19. Verifikasi nilai rate di Drawer Edit ditulis tanpa simbol `%`
20. Hapus isi Useful Life
21. Verifikasi Straight Line Rate (%) dan Declining Balance Rate (%) tidak tampil
22. Klik ikon ✕
23. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Cancel]` dan `[Leave]`
24. Klik `[Leave]`

### TC-FA-TDC-188: Pre-fill memakai nilai versi terakhir

25. Ganti isi kotak search dengan `KHS-V1`, tekan Enter
26. Klik link Class Code `KHS-V1`
27. Verifikasi Useful Life terisi `10` (nilai versi Scheduled)
28. Verifikasi Allowed Methods terisi `Straight Line` saja
29. Verifikasi Straight Line Rate (%) `10`
30. Verifikasi Declining Balance Rate (%) tidak tampil
31. Verifikasi Effective From read-only menampilkan Effective From versi Current: `—`
32. Klik ikon ✕

### TC-FA-TDC-247: Aksesibilitas keyboard

33. Ganti isi kotak search dengan `KHS-E1`, tekan Enter
34. Klik link Class Code `KHS-E1`
35. Tekan Tab berulang kali melewati seluruh elemen interaktif Drawer
36. Verifikasi fokus berpindah berurutan antar elemen interaktif: field yang enabled, tautan `View versions`, `[Clear Field]`, `[Save]`, ikon ✕
37. Verifikasi fokus tetap di dalam Drawer (fokus ter-trap)
38. Verifikasi field Disabled dilewati
39. Tekan Esc
40. Verifikasi Drawer tertutup
41. Verifikasi tidak ada dialog Unsaved Changes

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2, 9, 25, dan 33 Search kode class agar baris target ada di halaman teramati (R-16, 8b.13); langkah 8 memulihkan viewport; langkah 7 dan 32 menutup Drawer yang bersih; langkah 22 sampai 24 menutup form dirty secara deterministik (S-08). TC-FA-TDC-37 langkah 1 ("Buka tab Tax Depreciation Class") sudah dipenuhi hook `beforeEach` suite.
- Urutan langkah 4 dan 6 (layout tablet) lebih dulu, viewport dipulihkan sebelum blok berikutnya (S-09). Pengaturan viewport pada langkah 1 dan pemulihan pada langkah 8 adalah aksi tanpa `Verifikasi`.
- Alasan spec melewati sekitar 35 langkah: seluruh blok memeriksa keadaan tampilan Drawer Edit satu class tanpa Save (tidak ada perubahan data tersimpan) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah pembuka berulang per blok (Search, klik link, tutup) dan `Verifikasi` per klausa (S-01) membentuk jumlah langkah; blok tidak dapat digabung tanpa kehilangan klausa.
- Temuan untuk QA:
  - Email akun Total Control company uji Fixed Asset tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code seed `KHS-*` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-37 Expected b ("field Drawer disusun satu kolom") tidak menyebut ukuran lebar tablet dalam piksel; nilai viewport ditetapkan tim FE.
  - TC-FA-TDC-187 langkah 5 (hapus Useful Life) membiarkan form dirty tanpa langkah penutup; spec menambah langkah 22 sampai 24 untuk menutup form (S-09).
