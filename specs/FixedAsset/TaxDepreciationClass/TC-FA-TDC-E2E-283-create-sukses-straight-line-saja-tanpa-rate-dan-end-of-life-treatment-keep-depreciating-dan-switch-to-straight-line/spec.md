---
id: TC-FA-TDC-E2E-283-create-sukses-straight-line-saja-tanpa-rate-dan-end-of-life-treatment-keep-depreciating-dan-switch-to-straight-line
title: "Create Sukses: Class Straight Line Saja Tidak Menyimpan Declining Balance Rate dan End-of-Life Treatment serta Pilihan Keep depreciating dan Switch to straight-line Tersimpan"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-944
  - TC-FA-TDC-945
sourceRules: ["FATDC-LOGIC-03f.3", "FATDC-LOGIC-03g.5", "ST-10", "FLD-19", "FATDC-LOGIC-03g.1", "§4.1.6"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-03f.3": [3, 4, 10, 12]
  "FATDC-LOGIC-03g.5": [4, 10, 12]
  "ST-10": [4, 10, 12]
  "FLD-19": [25, 27, 32, 34]
  "FATDC-LOGIC-03g.1": [25, 27, 32, 34]
  "§4.1.6": [12, 27, 34]
coverage:
  web: automated
---

# Create Sukses: Class Straight Line Saja Tidak Menyimpan Declining Balance Rate dan End-of-Life Treatment serta Pilihan Keep depreciating dan Switch to straight-line Tersimpan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Master Data Count Limit belum tercapai (Precondition c kedua TC); kemampuan mengatur kuota disediakan tim FE/BE.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (dibuat lewat UI oleh spec; hook `before` menghapus sisa class berkode sama dari run sebelumnya lewat API dan hook `after` menghapus tiga class yang dibuat spec; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; awalan `DBE-` tidak dipakai TC lain; kemampuan seeding dan penghapusan lewat API disediakan tim FE/BE):

| Class Code | Class Name | Allowed Methods | Useful Life | Declining Balance Rate | End-of-Life Treatment |
|---|---|---|---|---|---|
| `DBE-05` | `Kelompok uji tarif 5` | `Straight Line` | 16 | tidak diisi | tidak diisi |
| `DBE-06` | `Kelompok uji tarif 6` | `Declining Balance` | 8 | `25` | `Keep depreciating` |
| `DBE-07` | `Kelompok uji tarif 7` | `Declining Balance` | 8 | `25` | `Switch to straight-line` |

  Nilai lain tiap class: Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Asset Type `Non-building`. Class Code `DBE-05`, `DBE-06`, dan `DBE-07` belum ada pada awal spec.
- Tabel berisi lebih dari satu halaman setelah class dibuat (7 class seed ditambah tiga class milik spec), sehingga baris target dibuka lewat Search Class Code (8b.13, R-23).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-944: Submit Create class Straight Line saja tidak menyimpan Declining Balance Rate dan End-of-Life Treatment

1. Klik `+ Class` di toolbar
2. Isi form valid dengan Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `DBE-05`, Class Name `Kelompok uji tarif 5`, pilih Asset Type `Non-building`, isi Useful Life `16`, pilih Allowed Methods `Straight Line`
3. Verifikasi Straight Line Rate (%) "6.25" tampil
4. Verifikasi input Declining Balance Rate dan Select End-of-Life Treatment tidak tampil
5. Klik `[Submit]`
6. Verifikasi toast sukses "Success, tax depreciation class has been created."
7. Ketik Search `DBE-05`, tekan Enter
8. Klik link Class Code `DBE-05` pada tabel
9. Verifikasi Allowed Methods "Straight Line" tampil pada Drawer Edit
10. Verifikasi Declining Balance Rate dan End-of-Life Treatment tidak tampil pada Drawer Edit
11. Klik tautan View versions
12. Verifikasi modal Versions memuat satu baris: Straight Line Rate "6.25%", Declining Balance Rate "—", End-of-Life Treatment "—"
13. Tutup modal Versions
14. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-945: Submit Create dengan End-of-Life Treatment Keep depreciating dan Switch to straight-line tersimpan dan tampil di Drawer Edit dan Versions

15. Klik `+ Class` di toolbar
16. Isi form valid dengan Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `DBE-06`, Class Name `Kelompok uji tarif 6`, pilih Asset Type `Non-building`, isi Useful Life `8`, pilih Allowed Methods `Declining Balance`, isi Declining Balance Rate `25`, pilih End-of-Life Treatment `Keep depreciating`
17. Klik `[Submit]`
18. Verifikasi toast sukses "Success, tax depreciation class has been created."
19. Klik `+ Class` di toolbar
20. Isi form valid dengan Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Code `DBE-07`, Class Name `Kelompok uji tarif 7`, pilih Asset Type `Non-building`, isi Useful Life `8`, pilih Allowed Methods `Declining Balance`, isi Declining Balance Rate `25`, pilih End-of-Life Treatment `Switch to straight-line`
21. Klik `[Submit]`
22. Verifikasi toast sukses "Success, tax depreciation class has been created."
23. Ganti isi kotak search dengan `DBE-06`, tekan Enter
24. Klik link Class Code `DBE-06` pada tabel
25. Verifikasi End-of-Life Treatment "Keep depreciating" pada Drawer Edit
26. Klik tautan View versions
27. Verifikasi modal Versions memuat satu baris dengan Declining Balance Rate "25%" dan End-of-Life Treatment "Keep depreciating"
28. Tutup modal Versions
29. Klik `[×]` pada Drawer Edit
30. Ganti isi kotak search dengan `DBE-07`, tekan Enter
31. Klik link Class Code `DBE-07` pada tabel
32. Verifikasi End-of-Life Treatment "Switch to straight-line" pada Drawer Edit
33. Klik tautan View versions
34. Verifikasi modal Versions memuat satu baris dengan Declining Balance Rate "25%" dan End-of-Life Treatment "Switch to straight-line"
35. Tutup modal Versions
36. Klik `[×]` pada Drawer Edit

## Notes

- Alasan melewati sekitar 35 langkah (36 langkah): kedua TC satu topik Create sukses dengan pilihan metode dan End-of-Life Treatment dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna).
- Langkah penghubung (S-03): langkah 7, 23, dan 30 (Search Class Code untuk menemukan baris target; R-16); langkah 13, 14, 28, 29, 35, dan 36 (menutup modal Versions dan Drawer Edit tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 (Straight Line Rate "6.25" tampil, Expected d TC-FA-TDC-944 menyebut "6.25%" pada Versions) adalah anchor positif untuk asersi absence langkah 4; langkah 9 (Allowed Methods "Straight Line" pada Drawer Edit) adalah anchor untuk asersi absence langkah 10 (8b.2).
- Asumsi: sesudah `[Submit]` yang sukses Drawer Create tertutup sehingga `+ Class` pada langkah 19 membuka form baru (TC-FA-TDC-945 langkah 3 menulis "Klik `+ Class`" lagi); perlu konfirmasi FE.
- Temuan untuk QA:
  - TC-FA-TDC-944 Expected c ("Declining Balance Rate dan End-of-Life Treatment tidak tampil" di Drawer Edit) tidak menyebut elemen anchor; spec memakai Allowed Methods.
  - TC-FA-TDC-945 langkah 4 menulis "Buka Drawer Edit `DBE-06` ... ulangi untuk `DBE-07`" tanpa cara menemukan baris; spec memakai Search Class Code (R-16) karena tabel dapat memuat lebih dari satu halaman.
  - TC-FA-TDC-944 dan TC-FA-TDC-945 Post Condition tidak punya langkah observasi sendiri selain Expected; tidak ada asersi tambahan (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
