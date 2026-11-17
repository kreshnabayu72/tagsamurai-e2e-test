---
id: TC-FA-TDC-E2E-123-konflik-dua-admin-create-class-code-sama-batas-tercapai-dan-batas-dinaikkan
title: "Konflik Dua Admin: Create Class Code Sama, Batas Tercapai, dan Batas Dinaikkan"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-117
  - TC-FA-TDC-132
  - TC-FA-TDC-763
sourceRules: ["T-01", "V-04", "E-FATDC-01", "F-FATDC-01.k11a", "D-07", "S-01a", "F-FATDC-01.k10b", "§3.1#p1"]
smoke: []
dependsOn: []
trace:
  "T-01": 7
  "V-04": 9
  "E-FATDC-01": 10
  "F-FATDC-01.k11a": 13
  "D-07": 24
  "S-01a": 32
  "F-FATDC-01.k10b": 33
  "§3.1#p1": [37, 38]
anchor: [11, 15, 25, 26, 29]
coverage:
  web: automated
---

# Konflik Dua Admin: Create Class Code Sama, Batas Tercapai, dan Batas Dinaikkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Akun sesi B: Total Control kedua (akun berbeda dari sesi A). Email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). TC-FA-TDC-117 memakai sesi B sebagai konteks browser kedua yang hasilnya diasersi (login di langkah 1); TC-FA-TDC-132 memakai sesi API aktor sesi B hanya sebagai pemicu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Master Data Count Limit 1000 dengan 999 class), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`.
- State global yang diubah: Master Data Count Limit (1000 pada TC-FA-TDC-132 dan TC-FA-TDC-763, dinaikkan ke 1100 pada TC-FA-TDC-763); dipulihkan ke nilai semula dengan langkah eksplisit (langkah 40) dan di hook `after` sebagai cadangan, bersama penghapusan class `KHS-*` dan 999 class tambahan buatan spec.
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `khs11` | `KHS-11` | belum ada saat TC-FA-TDC-117; nilai form valid: Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok konflik 11`, Asset Type `Non-building`, Useful Life `8`, Allowed Methods `Straight Line` |
| `khs15` | `KHS-15` | belum ada; form valid dengan nilai field yang sama, Class Name `Kelompok konflik 15` |
| `khs16` | `KHS-16` | belum ada; dibuat sesi API B pada TC-FA-TDC-132 dengan nilai field yang sama, Class Name `Kelompok konflik 16` |
| `bulk999` | 992 class tambahan | dibuat lewat API sehingga total class 999 sebelum TC-FA-TDC-132 (termasuk `KHS-11` dan seed) |

- Blok berjalan berurutan: `KHS-11` dari TC-FA-TDC-117 menjadi bagian 999 class TC-FA-TDC-132, dan total 1000 class di akhir TC-FA-TDC-132 menjadi precondition TC-FA-TDC-763.
- Suite berjalan serial (`parallel: false`) karena Master Data Count Limit adalah state global dan Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-117: Dua admin Submit Create dengan Class Code sama bersamaan

1. Buka konteks browser kedua (sesi B), login sebagai Total Control kedua dengan `Spectra.env.FA_TC_B_PASSWORD`, lalu buka Settings > Accounting > Tax Depreciation Class
2. Sesi A: klik `+ Class`
3. Sesi A: isi form valid dengan Class Code `KHS-11`
4. Sesi B: klik `+ Class`
5. Sesi B: isi form valid dengan Class Code `KHS-11`
6. Sesi A: klik `[Submit]`
7. Verifikasi sesi A muncul toast sukses: `Success, tax depreciation class has been created.`
8. Sesi B: klik `[Submit]`
9. Verifikasi sesi B muncul caption `Class code already exists` pada Class Code
10. Verifikasi Drawer sesi B tetap terbuka
11. Verifikasi input Drawer sesi B dipertahankan (Class Code `KHS-11` dan field lain tetap terisi)
12. Sesi A: ketik Search `KHS-11`, tekan Enter
13. Verifikasi tabel sesi A hanya memuat satu baris Class Code `KHS-11`
14. Sesi B: klik ikon ✕ pada Drawer
15. Verifikasi dialog Unsaved Changes tampil
16. Klik `[Leave]`
17. Sesi A: klik `(←)` pada kotak Search
18. Tutup konteks browser sesi B

### TC-FA-TDC-132: Submit Create ditolak D-07 bila batas tercapai antara klik + Class dan Submit

19. Siapkan lewat seeding API: Master Data Count Limit `1000` dan total class `999`
20. Sesi A: klik `+ Class`
21. Sesi A: isi form valid dengan Class Code `KHS-15` (belum Submit)
22. Sesi B (sesi API): buat class `KHS-16` hingga total class 1000 tersimpan
23. Sesi A: klik `[Submit]`
24. Verifikasi dialog D-07 muncul dengan teks `You've reached the platform limit of 1000 records. Contact support if you need a higher limit.`
25. Verifikasi Drawer sesi A tetap terbuka
26. Verifikasi input Drawer sesi A dipertahankan (Class Code `KHS-15` tetap terisi)
27. Klik `[OK]` pada dialog D-07
28. Klik ikon ✕ pada Drawer
29. Verifikasi dialog Unsaved Changes tampil
30. Klik `[Leave]`
31. Ketik Search `KHS-1`, tekan Enter
32. Verifikasi baris `KHS-16` tampil di tabel
33. Verifikasi class `KHS-15` tidak dibuat: tidak ada baris `KHS-15` di tabel
34. Klik `(←)` pada kotak Search

### TC-FA-TDC-763: Batas yang dinaikkan di Lifecycle Settings membuka kembali pembuatan class tanpa reload

35. Tab 2 (tab browser kedua sesi A): buka Admin Console > Plans & Licensing > Lifecycle Settings > System Limits, ubah Master Data Count Limit menjadi `1100`, lalu klik `[Save]`
36. Tab 1: klik `+ Class` tanpa memuat ulang halaman
37. Verifikasi Drawer Create terbuka
38. Verifikasi dialog `Tax Depreciation Class Limit Reached` tidak tampil
39. Klik ikon ✕ pada Drawer Create (tanpa input)
40. Tab 2: kembalikan Master Data Count Limit ke nilai semula, lalu tutup Tab 2

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 12 dan 31 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 14 sampai 16 dan 28 sampai 30 (menutup Drawer dirty deterministik; S-08), langkah 17 dan 34 (mengosongkan Search; 8b.9), langkah 18 (menutup konteks sesi B; S-09), langkah 19 (membentuk precondition TC-FA-TDC-132), langkah 27 (menutup dialog D-07 dengan `[OK]`), langkah 39 dan 40 (menutup Drawer yang kosong dan memulihkan batas).
- P-1 (state berat): TC-FA-TDC-763 berada di spec ini karena preconditionnya (limit 1000 dengan 1000 class) adalah state berat yang baru dibangun TC-FA-TDC-132 pada langkah 19 sampai 22.
- P-2 (pemicu bukan objek uji): kuota Master Data Count Limit pada TC-FA-TDC-132 dan TC-FA-TDC-763 hanya pemicu state; Tab 2 pada langkah 35 hanya mengubah batas dan tidak diasersi.
- Urutan TC: TC-FA-TDC-117, TC-FA-TDC-132, lalu TC-FA-TDC-763 (S-10), mengikuti rantai state di Prerequisites.
- Langkah 22 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ... tersimpan" (R-20). Sesi B pada TC-FA-TDC-117 memakai UI karena Expected b mengasersi hasil di sesi B.
- Langkah 33 (absence): langkah 32 menampilkan baris `KHS-16` pada Search yang sama sebagai anchor positif (8b.2).
- Alasan spec melewati sekitar 35 langkah (40 langkah): semua blok adalah kelas c (dua sesi atau dua konteks pada pembuatan class), tiap blok memakai class sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; TC-FA-TDC-763 bergantung pada state berat blok sebelumnya (P-1).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `KHS-*` ditulis literal tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (S-12); Lampiran A konvensi belum memuat pengecualian untuk modul ini.
  - TC-FA-TDC-117 dan TC-FA-TDC-132 menyebut "Segera setelah itu" / urutan klik dua sesi tanpa penjamin timing race; spec mengklik berurutan tanpa jeda buatan.
  - TC-FA-TDC-117 Post Condition (satu entri L-01 untuk `KHS-11`) dan TC-FA-TDC-132 Post Condition (total class tetap 1000, tidak ada entri log untuk `KHS-15`) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini (S-01, S-05).
  - TC-FA-TDC-132 TC mengisi Class Code `KHS-15` dan `KHS-16` tanpa nilai field lain; spec memakai nilai field valid yang sama dengan TC-FA-TDC-117 (disediakan fixture).
  - TC-FA-TDC-763 mensyaratkan Tab 2 di Lifecycle Settings tanpa menyebut label field Save; spec memakai `[Save]`. Nilai awal Master Data Count Limit dipulihkan ke nilai semula (TC tidak menyebutnya).
  - Kolom Automation TC-FA-TDC-117, TC-FA-TDC-132, dan TC-FA-TDC-763 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
