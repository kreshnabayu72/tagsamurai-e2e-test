---
id: TC-GS-BRAND-E2E-028-bulk-selection-bar-select-all-dan-retensi
title: "Bulk Action Bar: Screening, Checkbox Header, Select All, dan Retensi Seleksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-108
  - TC-GS-BRAND-109
  - TC-GS-BRAND-110
  - TC-GS-BRAND-111
  - TC-GS-BRAND-126
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Checkbox Header, Select All, dan Retensi Seleksi

## Prerequisites

- Mode: FE+BE. Spec tidak menghapus atau mengubah data (dialog Bulk Delete pada TC-GS-BRAND-126 hanya dibatalkan).
- Akun: Total Control Client A, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`. Ini akun default suite, sehingga hook `after` tidak perlu mengganti sesi.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (12 brand, Last Updated sebelum hari uji): Acme Corp, Brightway, Duo Brand, Helix Works, Kestrel, Lumina Co, Nimbus Gear, Northwind Co, Orion Tech, Tagline Co, Vertex Labs, Zenith Corp.
- Seeding: Population D-01 (setara TC-GS-BRAND-1) dibuat lewat API di hook `before` dengan 12 nama literal tanpa suffix: Apex Tools, Bolt Systems, Cedar Supply, Delta Instruments, Echo Devices, Falcon Gear, Granite Works, Harbor Tech, Iris Optics, Juniper Labs, Keystone Mfg, Linear Dynamics. Hasilnya total 24 brand, default urutan A-Z, 10 per halaman: halaman 3 berisi Orion Tech, Tagline Co, Vertex Labs, Zenith Corp. Seeding idempotent: brand yang sudah ada dilewati.
- Suite berjalan serial pada Client A (spec 028, 029, dan 035 memakai nama literal Population D-01 yang sama; spec 030 memakai brand bersuffix miliknya sendiri).
- Cleanup: hook `after` menghapus hanya brand Population D-01 yang dibuat spec ini lewat API tanpa berasumsi seeding berhasil penuh, dan memulihkan Search, Sort, serta seleksi tabel ke default (cadangan dari langkah pemulihan di Test Steps).
- Kemampuan teknis: scroll di dalam container dialog.
- TC-GS-BRAND-108 sampai TC-GS-BRAND-126: Brand Pre-setup Client A (12) dan Population D-01 (12) tersedia, total 24 brand (dependensi TC-GS-BRAND-1 dipenuhi lewat seeding).
- TC-GS-BRAND-126 data: 24 brand (seluruh hasil Select All).

## Test Steps

### TC-GS-BRAND-108: Screening Bulk Action Bar dan counter singular/plural

1. Pindah ke halaman 3 tabel Brand
2. Centang baris Orion Tech
3. Verifikasi Bulk Action Bar tampil di kiri sejajar Table Tools dengan urutan: `Bulk Action` | `1 brand selected` | `Select All (24 records)` | `(✕)`
4. Pindah ke halaman 1
5. Centang baris Brightway
6. Verifikasi counter menjadi `2 brands selected`
7. Uncheck baris Brightway
8. Verifikasi counter menjadi `1 brand selected`
9. Klik icon `(✕)` pada Bulk Action Bar
10. Verifikasi seleksi dibatalkan: tidak ada baris tercentang
11. Verifikasi Bulk Action Bar hilang

### TC-GS-BRAND-109: Checkbox header memilih baris halaman aktif dan status indeterminate

12. Centang satu baris di halaman 1
13. Verifikasi checkbox header berstatus indeterminate
14. Klik checkbox header
15. Verifikasi 10 baris halaman 1 tercentang
16. Verifikasi counter `10 brands selected`
17. Uncheck checkbox header
18. Verifikasi semua baris tidak tercentang
19. Verifikasi Bulk Action Bar hilang

### TC-GS-BRAND-110: Select All lintas halaman dan toggle Unselect All

20. Centang satu baris di halaman 1
21. Klik `Select All (24 records)`
22. Verifikasi seluruh 24 baris tercentang lintas halaman
23. Verifikasi tombol berubah menjadi `Unselect All`
24. Pindah ke halaman 3
25. Uncheck satu baris
26. Verifikasi counter menjadi `23 brands selected`
27. Verifikasi tombol kembali menjadi `Select All (24 records)`
28. Centang kembali baris tersebut
29. Klik `Unselect All`
30. Verifikasi semua seleksi dibatalkan
31. Verifikasi Bulk Action Bar hilang

### TC-GS-BRAND-111: Seleksi dipertahankan saat pindah halaman, search, dan sort

32. Centang Orion Tech di halaman 3
33. Pindah ke halaman 2
34. Kembali ke halaman 3
35. Verifikasi Orion Tech tetap tercentang dan counter tetap `1 brand selected`
36. Klik icon Search
37. Ketik `zz` di input Search
38. Tekan Enter
39. Verifikasi counter tetap `1 brand selected` dan Bulk Action Bar tetap tampil
40. Klik `(✕)` pada input Search untuk mengosongkan
41. Tekan Enter
42. Verifikasi counter tetap `1 brand selected`
43. Pindah ke halaman 3
44. Verifikasi Orion Tech tetap tercentang
45. Sort kolom Brand Name descending
46. Pindah ke halaman 1
47. Verifikasi Orion Tech (baris ke-4 pada halaman 1 dalam urutan descending: Zenith Corp, Vertex Labs, Tagline Co, Orion Tech) tetap tercentang
48. Verifikasi counter tetap `1 brand selected`

### TC-GS-BRAND-126: Daftar dialog bulk tidak diringkas walau banyak brand

49. Klik `(←)` untuk menutup Search
50. Pulihkan Sort kolom Brand Name ke default A-Z
51. Klik icon `(✕)` pada Bulk Action Bar
52. Centang satu baris
53. Klik `Select All (24 records)`
54. Klik `Bulk Action` > `Delete`
55. Verifikasi dialog campuran `Delete Brands` menampilkan seluruh 24 nama brand dalam container scrollable
56. Scroll daftar di dalam dialog sampai ujung
57. Verifikasi tidak ada ringkasan `...and N more`
58. Klik [Cancel]
59. Verifikasi dialog tertutup tanpa toast
60. Verifikasi 24 brand tetap terpilih
61. Klik icon `(✕)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 dan 4 (TC hanya menyebut "Centang Orion Tech" lalu "Centang Brightway", dua baris itu berada di halaman berbeda sehingga pindah halaman di antara dua centang), 28 (TC tidak menyebut label tombol sesudah baris dicentang kembali, langkah 29 memakai `Unselect All` seperti langkah TC), 43 (kembali ke halaman 3 sesudah Search), 46 (pindah ke halaman 1 sebelum posisi Orion Tech dicek pada urutan descending), 49 sampai 52 (menutup Search, memulihkan Sort, membersihkan seleksi sisa TC-GS-BRAND-111, dan memilih satu baris agar Bulk Action Bar tampil sebelum `Select All`), 61 (membersihkan seleksi).
- Langkah 12 dan 20 (TC-GS-BRAND-109 dan TC-GS-BRAND-110) memakai baris halaman 1; TC tidak menentukan baris tertentu.
- Langkah 5 sampai 8 memakai Brightway sebagai baris halaman 1; Orion Tech berada di halaman 3 pada urutan A-Z default.
- Sumber TC-GS-BRAND-111 menyebut "Search `zz`, tekan Enter, lalu kosongkan"; langkah 41 menekan Enter sesudah input dikosongkan agar tabel kembali ke daftar penuh.
- Spec ini melebihi sekitar 35 langkah karena memuat lima TC seleksi pada dataset dan layar yang sama dan tiap Expected Result bermajemuk dipecah satu `Verifikasi` per klausa; tidak ada kelas harness yang berbeda.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
