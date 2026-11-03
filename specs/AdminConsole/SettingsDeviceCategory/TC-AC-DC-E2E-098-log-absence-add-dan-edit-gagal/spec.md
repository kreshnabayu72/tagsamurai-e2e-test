---
id: TC-AC-DC-E2E-098-log-absence-add-dan-edit-gagal
title: "Absence Log: Add dan Edit yang Gagal serta Request Langsung yang Ditolak Server Tidak Menulis Entri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-222
  - TC-AC-DC-250
  - TC-AC-DC-251
  - TC-AC-DC-252
  - TC-AC-DC-253
coverage:
  web: automated
---

# Absence Log: Add dan Edit yang Gagal serta Request Langsung yang Ditolak Server Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE. Intercept parsial `Spectra.intercept()` di atas backend nyata dipakai pada langkah 3 sampai 16 (respons 500 untuk request create dan update Category); endpoint tidak dikarang di spec ini.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah.
- Data Dinamis (suffix `{runId}-098`): `Target Gagal {runId}-098` (leaf di bawah `Handheld Reader`), dibuat lewat sesi API aktor di hook `before`; menjadi induk Add (langkah 4) dan target Edit (langkah 10). Nama yang diketik pada Add dan Edit yang gagal: `Gagal Add {runId}-098` dan `Gagal Edit {runId}-098`.
- Data Dinamis untuk TC-AC-DC-250 sampai 253 (suffix `{runId}-098`), dibuat lewat sesi API aktor di hook `before` di bawah `Handheld Reader`: `Pemindai Nama {runId}-098` (leaf; induk request create dan target request update TC-250), `Pemindai Ganda {runId}-098` (leaf; pembanding nama duplikat TC-252), dan `Induk Rujuk {runId}-098` dengan anak `Anak Rujuk {runId}-098` yang dirujuk Device Name `DN-{runId}-098` (TC-253; nilai field wajib Device Name selain Category disediakan tim FE). Data Pre-setup #14 `Rantai L5` hanya dibaca sebagai parent request TC-251.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Gagal {runId}-098`, `Pemindai Nama {runId}-098`, `Pemindai Ganda {runId}-098`, dan `Induk Rujuk {runId}-098` beserta `Anak Rujuk {runId}-098` dan Device Name `DN-{runId}-098` (Device Name dahulu, lalu node) bila masih ada, termasuk node hasil request langsung yang dikenali dari sufiks `{runId}-098`; lepas intercept bila belum dilepas.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category, System Log akun aktor, dan Activity Log Admin Console sebagai baseline sebelum dan sesudah aksi (B222 pada langkah 2); ketiganya audit trail permanen sehingga tidak diasersi sebagai angka absolut (S-12).
- Kemampuan teknis untuk TC-AC-DC-250 sampai 253 (disediakan tim BE/FE; dinyatakan di `suite.md`): sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; membaca jumlah total entri Changelog Category sebelum aksi tiap TC (B250 pada langkah 22, B251 pada langkah 30, B252 pada langkah 39, B253 pada langkah 46) karena Changelog adalah audit trail permanen (S-12).
- State global: Hierarchy Depth Limit entitas uji (Pre-setup #18, nilai awal 50) diatur ke 5 di langkah 31 dan dipulihkan ke 50 di langkah 38; hook `after` memulihkannya ke 50 sebagai cadangan. Kemampuan mengatur Hierarchy Depth Limit (Lifecycle Settings) disediakan tim FE/BE; Pre-setup #9 tercatat berhak mengubah Lifecycle Settings.

## Test Steps

### TC-AC-DC-222: Add dan Edit yang gagal tidak menulis entri log

1. Expand `Hardware`, lalu expand `Handheld Reader`
2. Baca dan catat jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sebagai B222 (kemampuan baca)
3. Pasang intercept: request create dan update Category dipaksa mengembalikan error 500
4. Hover node `Target Gagal {runId}-098`, lalu klik aksi `+ Subcategory`
5. Ketik "Gagal Add {runId}-098", lalu klik `[Submit]`
6. Verifikasi toast error "Error, failed to create category."
7. Klik `[×]` pada input inline Add
8. Verifikasi dialog Unsaved Changes "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]`
9. Klik `[Leave]`
10. Hover node `Target Gagal {runId}-098`, lalu klik aksi Edit
11. Ubah nama menjadi "Gagal Edit {runId}-098", lalu klik `[Save]`
12. Verifikasi toast error "Error, failed to update category."
13. Klik `[×]` pada input inline Edit
14. Verifikasi dialog Unsaved Changes "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]`
15. Klik `[Leave]`
16. Lepas intercept
17. Klik ikon Changelog pada header Sidebar Category
18. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
19. Verifikasi jumlah entri Changelog Category sama dengan B222 (kemampuan baca)
20. Tutup modal Changelog lewat `[×]`
21. Verifikasi jumlah entri System Log akun aktor dan Activity Log sama dengan B222 (tidak ada entri pada kedua surface)

### TC-AC-DC-250: Request langsung dengan nama All Categories ditolak server tidak menulis entri Changelog

22. Baca dan catat jumlah entri Changelog Category sebagai B250 (kemampuan baca)
23. Kirim request create dengan parent `Pemindai Nama {runId}-098` dan nama "All Categories" memakai token Total Control
24. Kirim request update nama `Pemindai Nama {runId}-098` menjadi "all categories" memakai token Total Control
25. Verifikasi kedua request ditolak server
26. Klik ikon Changelog pada header Sidebar Category
27. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
28. Verifikasi jumlah entri Changelog Category sama dengan B250 (kemampuan baca)
29. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-251: Request langsung melampaui Hierarchy Depth Limit ditolak server tidak menulis entri Changelog

30. Baca dan catat jumlah entri Changelog Category sebagai B251 (kemampuan baca)
31. Atur Hierarchy Depth Limit entitas uji menjadi 5 di Lifecycle Settings
32. Kirim request create nama "Bypass Depth {runId}-098" dengan parent `Rantai L5` memakai token Total Control
33. Verifikasi request ditolak server
34. Klik ikon Changelog pada header Sidebar Category
35. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
36. Verifikasi jumlah entri Changelog Category sama dengan B251 (kemampuan baca)
37. Tutup modal Changelog lewat `[×]`
38. Pulihkan Hierarchy Depth Limit entitas uji ke 50

### TC-AC-DC-252: Request langsung dengan nama duplikat di parent yang sama ditolak server tidak menulis entri Changelog

39. Baca dan catat jumlah entri Changelog Category sebagai B252 (kemampuan baca)
40. Kirim request create nama "pemindai ganda {runId}-098" dengan parent `Handheld Reader` memakai token Total Control
41. Verifikasi request ditolak server
42. Klik ikon Changelog pada header Sidebar Category
43. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
44. Verifikasi jumlah entri Changelog Category sama dengan B252 (kemampuan baca)
45. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-253: Request langsung menghapus node yang dirujuk Device Name ditolak server tidak menulis entri Changelog

46. Baca dan catat jumlah entri Changelog Category sebagai B253 (kemampuan baca)
47. Kirim request delete node `Induk Rujuk {runId}-098` (anak `Anak Rujuk {runId}-098` dirujuk Device Name `DN-{runId}-098`) memakai token Total Control
48. Verifikasi request ditolak server
49. Klik ikon Changelog pada header Sidebar Category
50. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
51. Verifikasi jumlah entri Changelog Category sama dengan B253 (kemampuan baca)
52. Tutup modal Changelog lewat `[×]`

## Notes

- P-5 (a): spec ini spec absence (kelas g); pemicu kelas b (respons 500 untuk Add dan Edit) dan kelas a (request langsung TC-AC-DC-250 sampai 253) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya baseline sendiri (B222, B250, B251, B252, B253). Intercept dilepas segera setelah kedua toast diasersi dan form ditutup (S-09).
- Spec ini melewati sekitar 35 langkah (52): lima blok absence satu kelas (g), tiap blok wajib punya baseline, pemicu, anchor positif, pembukaan Changelog, dan penutupan sendiri (P-5 a), sehingga blok TC-AC-DC-250 sampai 253 (7 sampai 9 langkah masing-masing) tidak dapat digabung tanpa menghilangkan baseline per TC. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Anchor absence (bagian 8b butir 2): toast error hasil server (langkah 6 dan 12), penolakan server atas request langsung (langkah 25, 33, 41, dan 48), dan surface Changelog termuat (langkah 18, 27, 35, 43, dan 50) menjadi anchor; untuk System Log dan Activity Log anchor adalah surface agregat berupa jumlah total sebelum dan sesudah (B222).
- Langkah penghubung (S-03): langkah 7 sampai 9 dan 13 sampai 15 (menutup input yang berisi perubahan secara deterministik, S-08 dan S-09; `Verifikasi` dialog Unsaved Changes diwajibkan S-08), langkah 16 (melepas intercept), langkah 20 (menutup modal), langkah 29, 37, 45, dan 52 (menutup modal Changelog), serta langkah 31 dan 38 (mengatur dan memulihkan state global Hierarchy Depth Limit, S-09).
- Request langsung dikirim lewat klien HTTP, tidak melewati browser (8b butir 1); asersi di blok TC-AC-DC-250 sampai 253 hanya penolakan server dan jumlah entri Changelog. Penolakan server atas request yang sama dan state tree (nama tidak berubah, node tidak dibuat, node tetap ada) diasersi di spec 092; TC-AC-DC-250 sampai 253 terbagi dua spec menurut S-05 (klausa absence Changelog di spec ini).
- Pembagian TC lintas spec: Delete diblok dan Delete family gagal ada di spec 084; Save tanpa perubahan di spec 083; presence log di spec 079 sampai 082 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-222 langkah 5 menulis "Tutup input" tanpa menyebut cara. Spec menutup input Add dan Edit lewat `[×]` mengikuti S-08 dengan asumsi input masih berisi teks setelah request gagal (dialog Unsaved Changes tampil); bila input otomatis kembali bersih setelah toast error, langkah 8 dan 14 perlu disesuaikan.
  - TC-AC-DC-222 Expected b menulis "Changelog tetap 12 entri (baris teratas tidak berubah dan halaman 2 tetap berisi 2 baris)"; spec memakai selisih terhadap baseline lewat kemampuan baca karena audit trail permanen (S-12, S-14). Cara membaca jumlah entri System Log dan Activity Log di UI tidak disebut TC.
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`) sebagai target; spec memakai node bersuffix milik spec (keputusan data tulis).
  - TC-AC-DC-250 sampai 253 memakai node literal Pre-setup #14 (`Rugged Scanner`, `Barcode Handheld`, `Industrial Scanner` beserta `Rugged` dan `Rugged Kit`); spec memakai node dan Device Name bersuffix `{runId}-098` milik spec, dan hanya `Rantai L5` (TC-AC-DC-251) yang literal karena rantai kedalaman hanya ada di Pre-setup #14 dan request ditolak sehingga rantai tidak berubah. TC-AC-DC-250, 252, dan 253 tidak menyebut status respons, endpoint, atau mekanisme klien HTTP; spec mengikuti kalimat TC (S-13).
