---
id: TC-AC-SG-E2E-100-konkurensi-dua-admin-create-duplikat-edit-bersamaan-refresh-sse-dan-fallback-f5
title: "Konkurensi Dua Admin: Create Duplikat, Edit Bersamaan, Refresh SSE, dan Fallback F5"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-380
  - TC-AC-SG-381
  - TC-AC-SG-390
  - TC-AC-SG-392
coverage:
  web: automated
---

# Konkurensi Dua Admin: Create Duplikat, Edit Bersamaan, Refresh SSE, dan Fallback F5

## Prerequisites

- Mode: FE+BE.
- Sesi A (akun aktor pertama): Total Control entitas Distributor Race, `totalControlRaceA_automated_{namaCompany}@qwertysystem.net` (Pre-setup #32), password `Spectra.env.AC_SG_RACEA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi B (konteks browser kedua, Pre-setup #39): Total Control entitas Distributor Race, `totalControlRaceB_automated_{namaCompany}@qwertysystem.net` (Pre-setup #32), password `Spectra.env.AC_SG_RACEB_PASSWORD`. Dibuka di langkah 1 dan ditutup di langkah 48 (S-09).
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite untuk kedua akun dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Race, dihapus atau dipulihkan hook `after`; setiap nama bersuffix `{runId}-100`; Pre-setup #32 tidak diubah): `Race Induk {runId}-100` (tanpa entitas) dan `Race Lain {runId}-100` (level 1, tanpa entitas).
- Data yang dibuat langkah spec: `Anak Kembar {runId}-100` (anak `Race Induk {runId}-100`), `Race Lain A {runId}-100` lalu `Race Lain B {runId}-100` (rename `Race Lain {runId}-100`), `Sesi Lain {runId}-100` (level 1), dan `Node Pulih {runId}-100` (level 1).
- Jendela tunggu SSE: "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD) untuk asersi absence refresh. Batas tunggu refresh otomatis lewat SSE pada langkah 24 adalah 30 detik (nilai TC-AC-SG-390).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan; disediakan tim FE/BE) dan klien HTTP untuk request langsung ke endpoint Group (Pre-setup #36; langkah 46).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka konteks browser kedua (Sesi B), login sebagai Total Control Distributor Race `totalControlRaceB_automated_{namaCompany}@qwertysystem.net`, lalu buka halaman Settings > Group

### TC-AC-SG-380: Dua admin membuat subgroup bernama sama pada parent sama hampir bersamaan

2. Pada Sesi A, klik ikon `⋯` pada node `Race Induk {runId}-100` di sidebar lalu `+ Add Subgroup`
3. Pada Sesi B, klik ikon `⋯` pada node `Race Induk {runId}-100` di sidebar lalu `+ Add Subgroup`
4. Pada Sesi A, ketik `Anak Kembar {runId}-100`
5. Pada Sesi B, ketik `Anak Kembar {runId}-100`
6. Pada Sesi A, klik `[Submit]`
7. Pada Sesi B, segera klik `[Submit]`
8. Verifikasi Sesi A menampilkan toast sukses: "Success, group has been created."
9. Verifikasi Sesi B menampilkan inline error: "Group name already exists in this level"
10. Verifikasi hanya satu group `Anak Kembar {runId}-100` di bawah `Race Induk {runId}-100` pada Sidebar Group Tree Sesi A
11. Pada Sesi B, tutup popup Add Subgroup dengan `✕`
12. Verifikasi dialog `Unsaved Changes` tampil pada Sesi B
13. Pada Sesi B, klik `[Leave]`

### TC-AC-SG-381: Dua admin mengedit node yang sama: pembaruan terakhir menang tanpa dialog konflik

14. Pada Sesi A, klik ikon `⋯` pada node `Race Lain {runId}-100` di sidebar lalu `Edit`
15. Pada Sesi B, klik ikon `⋯` pada node `Race Lain {runId}-100` di sidebar lalu `Edit`
16. Pada Sesi A, ubah nama menjadi `Race Lain A {runId}-100` lalu klik `[Save]`
17. Verifikasi Sesi A menampilkan toast sukses: "Success, group has been updated."
18. Pada Sesi B, ubah nama menjadi `Race Lain B {runId}-100` lalu klik `[Save]`
19. Verifikasi Sesi B menampilkan toast sukses: "Success, group has been updated."
20. Verifikasi Sesi B tidak menampilkan dialog konflik
21. Verifikasi nama akhir node adalah `Race Lain B {runId}-100` pada Sidebar Group Tree Sesi B

### TC-AC-SG-390: Perubahan dari sesi lain me-refresh tree dan tabel otomatis lewat SSE; Edit No-Op tidak memicu refresh

22. Pada Sesi B, klik `[+] Group` di Sidebar Group Tree
23. Pada Sesi B, ketik `Sesi Lain {runId}-100` lalu klik `[Submit]`
24. Tunggu hingga Sidebar Group Tree dan tabel Sesi A menampilkan `Sesi Lain {runId}-100` tanpa F5 (batas tunggu 30 detik)
25. Verifikasi Sidebar Group Tree Sesi A me-refresh otomatis dan memuat `Sesi Lain {runId}-100`
26. Verifikasi tabel Sesi A me-refresh otomatis dan memuat `Sesi Lain {runId}-100`
27. Pada Sesi B, klik ikon `⋯` pada node `Sesi Lain {runId}-100` di sidebar lalu `Edit`
28. Pada Sesi B, klik `[Save]` tanpa mengubah nama
29. Tunggu 5 detik tanpa memuat ulang halaman Sesi A
30. Verifikasi Sesi A tidak me-refresh sidebar dan tabel (tampilan tidak berubah dan indikator Loading tidak tampil)

### TC-AC-SG-392: F5 memulihkan node sidebar yang sudah dihapus sesi lain dengan fallback ke All Groups

31. Pada Sesi B, klik `[+] Group` di Sidebar Group Tree
32. Pada Sesi B, ketik `Node Pulih {runId}-100` lalu klik `[Submit]`
33. Pada Sesi A, muat ulang halaman
34. Pada Sesi A, klik node `Node Pulih {runId}-100` di Sidebar Group Tree
35. Pada Sesi A, ketik Search `x`, tekan Enter
36. Pada Sesi A, urutkan kolom Total User
37. Pada Sesi B, klik ikon `⋯` pada node `Node Pulih {runId}-100` di sidebar lalu `Delete`
38. Pada Sesi B, konfirmasi penghapusan pada dialog Delete dengan `[Delete]`
39. Tunggu hingga Sesi B menampilkan toast sukses penghapusan
40. Pada Sesi A, tekan F5
41. Verifikasi node sidebar terpilih Sesi A kembali ke `All Groups` (aktif)
42. Verifikasi Sesi A tidak menampilkan error
43. Verifikasi toast netral: "This group is no longer available."
44. Verifikasi Group Context Header dan tabel Sesi A menampilkan state default `All Groups`
45. Verifikasi Search, Filter, Sort, dan halaman Sesi A kembali ke default
46. Kirim request list langsung (klien HTTP) yang di-scope ke ID node `Node Pulih {runId}-100` yang sudah terhapus
47. Verifikasi respons `404 Not Found`
48. Tutup konteks browser Sesi B

## Notes

- Kelas c (multi-konteks, dua admin). Sesi B menjadi objek asersi pada TC-AC-SG-380 dan TC-AC-SG-381 dan pemicu pada TC-AC-SG-390 dan TC-AC-SG-392 dengan hasil diasersi di Sesi A; satu konteks kedua dipakai untuk semuanya sehingga tidak memakai P-2.
- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 1 (membuka Sesi B), langkah 11 sampai 13 bagian penutupan popup dirty (S-08), langkah 24 dan 29 (menunggu), langkah 39 (menunggu penghapusan selesai sebelum Sesi A memuat ulang), dan langkah 48 (menutup konteks Sesi B).
- Penutupan konteks Sesi B di akhir (langkah 48) memenuhi S-09; sesi Sesi A dipulihkan ke akun default spec di hook `after`.
- Hook `after` memulihkan pohon `Race Induk {runId}-100` dan `Race Lain {runId}-100` lewat Fixture BE (menghapus `Anak Kembar`, `Sesi Lain`, dan hasil rename).
- Asersi absence refresh (langkah 30) didahului `Verifikasi` refresh otomatis yang berhasil pada surface yang sama (langkah 25 dan 26) dan jendela tunggu 5 detik (langkah 29).
- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (kelas c, dua sesi admin pada satu entitas) dan berdiri sendiri; tiap blok memakai node milik spec sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Pemisahan menjadi beberapa spec akan mengulang login dan pembukaan Sesi B.
- Temuan untuk QA:
  - TC-AC-SG-390 Expected butir b ("Edit No-Op di Sesi B tidak memicu refresh di Sesi A") tidak menyebut cara mengamati refresh pada daftar yang isinya sama; spec memakai tampilan tidak berubah dan indikator Loading tidak tampil sebagai pengamatan, yang perlu dikonfirmasi tim FE.
  - TC-AC-SG-380 tidak menyebut keadaan popup Sesi B setelah inline error; spec menutupnya dengan `✕`, `Unsaved Changes`, dan `[Leave]` (S-08).
  - Pre-setup #39 menyebut dua sesi dengan "akun Total Control entitas yang sama" sedangkan Pre-setup #32 menyebut dua akun (`totalControlRaceA` dan `totalControlRaceB`); spec memakai satu akun per sesi.
  - TC-AC-SG-392 butir c memakai request list langsung yang hanya diasersi statusnya `404` (bagian 8b butir 1).
