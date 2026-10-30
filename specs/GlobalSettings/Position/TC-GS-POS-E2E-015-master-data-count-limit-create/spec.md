---
id: TC-GS-POS-E2E-015-master-data-count-limit-create
title: "Master Data Count Limit: [+ Position] Diblokir, Dialog Limit Reached, Submit Ditolak Setelah Popup Dibuka, Create Berulang hingga Batas, Baca Limit Dinamis, dan Create Missing Positions"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-69
  - TC-GS-POS-70
  - TC-GS-POS-71
  - TC-GS-POS-72
  - TC-GS-POS-259
  - TC-GS-POS-280
coverage:
  web: automated
---

# Master Data Count Limit: [+ Position] Diblokir, Dialog Limit Reached, Submit Ditolak Setelah Popup Dibuka, Create Berulang hingga Batas, Baca Limit Dinamis, dan Create Missing Positions

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global Master Data Count Limit entitas aktor di Admin Console. Nilai awal dicatat di hook `before` dan dipulihkan di hook `after`.
- Akun aktor (tiga konteks browser; ketiganya login di hook `before`, password hanya lewat env var dan tidak ditulis di spec atau fixture):
  - Admin A: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`. Konteks utama untuk semua langkah Position.
  - Admin B: Total Control (Andi Wijaya) `superAdminGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Pre-setup 2), `Spectra.env.GS_TC2_PASSWORD`. Konteks kedua, dipakai hanya sebagai pemicu di TC-GS-POS-71.
  - Super Admin Admin Console `superAdminAdminConsole_automated_{namaPrincipal}@qwertysystem.net` (Pre-setup 9), `Spectra.env.AC_TC_PASSWORD`. Konteks ketiga, dipakai hanya untuk mengubah Master Data Count Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits.
  - Hook `after` mengembalikan sesi utama ke akun Total Control default suite dan menutup konteks kedua dan ketiga.
- Layar awal Global Settings > User > Position (Admin A) dibuka hook `beforeEach`.
- Jumlah Position entitas Admin A (N) diturunkan dari seeding dan dibaca hook `before` lewat API (`totalRecords` pada respons `POST /v2/iam/positions/list`, openapi.yaml:11 dan :38), bukan dari tabel UI yang hanya menampilkan satu halaman: N1 = jumlah saat hook `before` selesai; N2 = N1 (TC-GS-POS-69, 70, dan 259 tidak menyimpan Position); N3 = N2 + 1 (`Branch Manager {runId}-015` dibuat Admin B pada TC-GS-POS-71); N4 = N3 + 1 (`Event Coordinator {runId}-015` dibuat pada TC-GS-POS-72). Nilai N tidak di-hardcode.
- Data Dinamis (nama bersuffix `{runId}-015`; fixture baru `Fixture.position.limitSeed015`):
  - TC-GS-POS-71: `Store Manager {runId}-015` (diketik Admin A, tidak tersimpan) dan `Branch Manager {runId}-015` (dibuat Admin B, tersimpan).
  - TC-GS-POS-72: `Event Coordinator {runId}-015` (tersimpan) dan `Event Planner {runId}-015` (ditolak limit).
  - TC-GS-POS-280: staging Import Type "User Login" di Global Settings > Import memuat satu Position belum terdaftar `Lab Technician {runId}-015`. Staging disiapkan di hook `before` lewat mekanisme yang disediakan tim FE/BE (TC tidak mendefinisikan caranya).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan Master Data Count Limit ke nilai awal yang dicatat di `before`; hapus lewat API semua Position bersuffix `{runId}-015` yang masih ada (`Store Manager`, `Branch Manager`, `Event Coordinator`, `Event Planner`, `Lab Technician`); bersihkan staging Import.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis: tiga konteks browser aktif bersamaan; membaca dan mengubah Master Data Count Limit lewat UI Admin Console (nilai awal dibaca di `before`); membaca total Position entitas lewat API di hook `before`.
- State global: Master Data Count Limit (dipulihkan seperti di atas) dan flag Guided Tooltip (dikelola hook suite).

## Test Steps

### TC-GS-POS-69: Klik [+ Position] saat Master Data Count Limit tercapai

1. Muat ulang halaman Position (F5)
2. Di sesi Super Admin Admin Console, buka Plans & Licensing > Lifecycle Settings > System Limits, setel Master Data Count Limit = N1, lalu simpan
3. Tunggu aksi selesai (limit tersimpan)
4. Verifikasi `[+ Position]` tampil
5. Verifikasi `[+ Position]` enabled
6. Klik `[+ Position]`
7. Verifikasi Popup Create Position tidak terbuka
8. Verifikasi dialog Header menampilkan Title "Limit Reached"
9. Verifikasi dialog Header berseverity warning
10. Verifikasi dialog Body menampilkan "You've reached the position limit for this workspace."
11. Verifikasi dialog Footer hanya berisi satu tombol `[OK]`
12. Verifikasi tombol `[OK]` bergaya text, contrast

### TC-GS-POS-70: Dialog Limit Reached, tombol OK

13. Klik `[OK]`
14. Verifikasi dialog tertutup
15. Verifikasi tetap di tabel Position
16. Verifikasi Popup Create Position tidak terbuka
17. Verifikasi tidak ada toast

### TC-GS-POS-259: Perubahan Master Data Count Limit dibaca langsung tanpa hardcode

18. Klik `[+ Position]`
19. Verifikasi Dialog Limit Reached muncul (limit masih N1)
20. Klik `[OK]`
21. Di sesi Super Admin Admin Console, naikkan Master Data Count Limit menjadi N1 + 1, lalu simpan
22. Tunggu aksi selesai (limit tersimpan)
23. Klik `[+ Position]`
24. Verifikasi Popup Create Position terbuka
25. Klik `✕` pada Popup Create Position (form kosong, tanpa dialog)

### TC-GS-POS-71: Submit Create ditolak karena limit tercapai setelah popup dibuka

26. Muat ulang halaman Position (F5)
27. Di sesi Super Admin Admin Console, setel Master Data Count Limit = N2 + 1 (sisa kuota 1), lalu simpan
28. Tunggu aksi selesai (limit tersimpan)
29. Klik `[+ Position]`
30. Ketik `Store Manager {runId}-015` pada field Position Name (sesi Admin A)
31. Di sesi Admin B, buka Global Settings > User > Position, klik `[+ Position]`, ketik `Branch Manager {runId}-015`, klik `[Submit]` hingga Position tersimpan
32. Di sesi Admin A, klik `[Submit]`
33. Verifikasi dialog Limit Reached muncul dengan body "You've reached the position limit for this workspace."
34. Verifikasi dialog memiliki tombol `[OK]`
35. Verifikasi tidak ada toast sukses
36. Klik `[OK]`
37. Verifikasi Popup Create Admin A tetap terbuka
38. Verifikasi field Position Name tetap berisi `Store Manager {runId}-015`
39. Klik `✕` pada Popup Create Admin A
40. Verifikasi dialog Unsaved Changes muncul
41. Klik `[Leave]`

### TC-GS-POS-72: Create berulang dengan Stay hingga menyentuh Master Data Count Limit

42. Muat ulang halaman Position (F5)
43. Di sesi Super Admin Admin Console, setel Master Data Count Limit = N3 + 1, lalu simpan
44. Tunggu aksi selesai (limit tersimpan)
45. Klik `[+ Position]`
46. Centang `Stay on this form after submitting`
47. Ketik `Event Coordinator {runId}-015`, klik `[Submit]`
48. Verifikasi toast sukses "Success, position has been created."
49. Verifikasi form direset (field Position Name kosong)
50. Verifikasi Popup Create tetap terbuka
51. Ketik `Event Planner {runId}-015`, klik `[Submit]`
52. Verifikasi Dialog Limit Reached muncul
53. Klik `[OK]`
54. Verifikasi form tetap terbuka
55. Verifikasi field Position Name tetap berisi `Event Planner {runId}-015`
56. Klik `✕` pada Popup Create
57. Verifikasi dialog Unsaved Changes muncul
58. Klik `[Leave]`

### TC-GS-POS-280: [Create Missing Positions] dihitung terhadap Master Data Count Limit

59. Muat ulang halaman Position (F5)
60. Di sesi Super Admin Admin Console, setel Master Data Count Limit = N4 (tercapai), lalu simpan
61. Tunggu aksi selesai (limit tersimpan)
62. Buka Global Settings > Import (staging Import Type "User Login" memuat `Lab Technician {runId}-015`)
63. Klik `[Create Missing Positions]`
64. Verifikasi Error Summary Callout di modul Import menampilkan "You've reached the platform limit of {N4} positions. Contact support if you need a higher limit." (pembuatan `Lab Technician {runId}-015` ditolak karena limit)
65. Buka Global Settings > User > Position
66. Ketik Search `{runId}-015`, tekan Enter
67. Verifikasi baris `Event Coordinator {runId}-015` tampil di tabel
68. Verifikasi `Lab Technician {runId}-015` tidak ada di tabel
69. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 69, 70, 259, 71, 72, 280. TC-GS-POS-259 ditaruh sesudah TC-GS-POS-70 karena limit tercapai (N1) dari TC-GS-POS-69 masih berlaku dan langkah 1 TC-GS-POS-259 ("Klik `[+ Position]`, klik `[OK]`") sama dengan langkah 18 sampai 20. Urutan ini menyimpang dari urutan TC sumber (69, 70, 71, 72, 259, 280).
- Langkah 6 (klik `[+ Position]`) dipakai bersama TC-GS-POS-69 dan TC-GS-POS-70: dialog yang diamati di TC-GS-POS-69 adalah dialog yang ditutup lewat `[OK]` di TC-GS-POS-70.
- Jumlah pembukaan Popup Create: 3 (langkah 23, 29, 45), jumlah penutupan: 3 (langkah 25, 39 sampai 41, 56 sampai 58).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 26, 42, 59 (muat ulang halaman), langkah 2, 21, 27, 43, 60 (mengubah Master Data Count Limit di sesi Admin Console sebagai pemicu state), langkah 3, 22, 28, 44, 61 (Tunggu aksi selesai (limit tersimpan): menunggu penyimpanan limit di Admin Console selesai sebelum langkah berikutnya pindah ke surface Position atau sesi lain; tanpa `Verifikasi`, butir 8 bagian 8b konvensi), langkah 25 (menutup form kosong), langkah 31 (Admin B membuat `Branch Manager` sebagai pemicu), langkah 39 sampai 41 dan 56 sampai 58 (menutup form dirty; dialog Unsaved Changes pada langkah 40 dan 57 diasersi sebagai bagian penutupan deterministik, S-08), dan langkah 69 (mengosongkan Search). Langkah 66 mencari `{runId}-015` supaya hasil Search memuat baris pembanding; langkah 67 adalah `Verifikasi` tambahan di luar Expected TC-GS-POS-280 yang menjadi anchor positif (baris `Event Coordinator` dari langkah 47 tampil) bagi asersi absence pada langkah 68 (butir 2 bagian 8b konvensi).
- Konteks kedua (Admin B) dan ketiga (Admin Console) hanya pemicu state UI yang diuji dan bukan objek asersi (P-2). Tidak ada asersi pada tampilan sesi Admin B atau Admin Console. Admin B berjalan sebagai sesi UI karena TC-GS-POS-71 menulis sesi Admin B; konvensi P-2 memakai sesi API untuk pelaku kedua yang hanya memicu perubahan state, dan hal itu menunggu konfirmasi QA (lihat Temuan untuk QA).
- Spec melewati sekitar 35 langkah (69 langkah). Seluruhnya satu kelas harness (volume data / Master Data Count Limit pada Create), satu dataset dan satu state global yang sama. Tiap blok membaca jumlah Position sendiri dan menyetel limit sendiri di awal blok, sehingga blok sesudahnya tetap bermakna bila blok sebelumnya gagal (kecuali kegagalan keras konteks, yang tidak ditangani soft assertion).
- Asersi "tidak ada toast" pada langkah 17 dan 35 diletakkan tepat setelah pemicu, sebelum langkah berikutnya mengubah state.
- Temuan untuk QA:
  - TC-GS-POS-69, 71, 72, 259: TC tidak menyebut entitas dan plan yang System Limits-nya diubah; spec mengubah Master Data Count Limit untuk entitas aktor Total Control. Mekanisme dan batas minimum nilai yang bisa disimpan di Admin Console tidak didefinisikan di TC.
  - Sesi UI Admin B pada langkah 31 (TC-GS-POS-71) dapat diganti sesi API ("disediakan tim FE/BE") setelah QA mengonfirmasi; langkah 31 lalu tidak lagi membuka UI Admin B.
  - TC-GS-POS-70: Post Condition "Jumlah record tidak berubah" tanpa langkah observasi di TC; tidak diasersi.
  - TC-GS-POS-71: Post Condition "Record `Store Manager` tidak dibuat; tidak ada entri Changelog untuk `Store Manager`" tanpa langkah observasi di TC; tidak diasersi. Langkah 3 TC ("hingga sukses") tidak punya Expected; langkah 31 tidak diberi `Verifikasi`.
  - TC-GS-POS-72: Post Condition "Hanya `Event Coordinator` tersimpan" tanpa langkah observasi di TC; tidak diasersi.
  - TC-GS-POS-280: Cara menyiapkan staging Import Type "User Login" tidak didefinisikan di TC, PRD, atau LLD sehingga disediakan tim FE/BE. TC bertanda Manual Only di kolom Automation, namun tetap dimasukkan sesuai konvensi bagian 2.
