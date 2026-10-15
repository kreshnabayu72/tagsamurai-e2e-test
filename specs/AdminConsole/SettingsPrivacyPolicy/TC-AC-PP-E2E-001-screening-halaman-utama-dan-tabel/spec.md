---
id: TC-AC-PP-E2E-001-screening-halaman-utama-dan-tabel
title: "Screening Halaman Utama Privacy Policy: Layout Tabel Version History, Badge Active, Format Sel, dan Row Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-01
  - TC-AC-PP-02
  - TC-AC-PP-03
  - TC-AC-PP-05
  - TC-AC-PP-06
  - TC-AC-PP-79
  - TC-AC-PP-163
coverage:
  web: automated
---

# Screening Halaman Utama Privacy Policy: Layout Tabel Version History, Badge Active, Format Sel, dan Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Dataset Riwayat A: Version 3 Active (10 Aug 2026 pukul 20:30 UTC, `John Doe`), Version 2 (02 Jul 2026 pukul 09:14 UTC, `John Doe`), Version 1 (15 Jan 2026 pukul 02:11 UTC, `Jane Smith`, akun sudah dihapus). Hook `before` men-seed dataset ini lewat Fixture BE (riwayat append-only sehingga tidak dapat dihapus lewat UI); hook `after` mengembalikan dataset ke Riwayat A. Spec ini tidak membuat atau mengubah data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah oleh spec ini).
- Kemampuan teknis: Fixture BE (membuat ulang dataset Riwayat). Tidak memakai intercept, jam server, atau klien HTTP.
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PP-01: Screening halaman utama Settings > Privacy Policy saat Version History berisi 3 versi

1. Klik menu Settings > Privacy Policy di sidebar
2. Verifikasi halaman `Settings > Privacy Policy` tampil
3. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
4. Verifikasi Header: Breadcrumb "Settings > Privacy Policy"
5. Verifikasi Header: Table Tools `Search | Filter | Download`
6. Verifikasi Header: tidak ada icon Changelog dan tidak ada tombol Create di toolbar
7. Verifikasi Header: tidak ada judul halaman terpisah dan tidak ada label section "Version History" di bawah Breadcrumb
8. Verifikasi Body: kolom `Version (sortable) | Published At (sortable) | Published By (sortable) | Actions (⋯)`
9. Hover header kolom Actions `(⋯)`
10. Verifikasi header Actions `(⋯)` unsortable
11. Verifikasi tooltip "Column Visibility" tampil pada header Actions `(⋯)`
12. Verifikasi Body: baris pertama dari atas `Version 3` + badge `Active` | `10 Aug 26` | `John D`
13. Verifikasi Body: baris kedua `Version 2` | `02 Jul 26` | `John D`
14. Verifikasi Body: baris ketiga `Version 1` | `15 Jan 26` | `Jane S`
15. Verifikasi Body: sel Actions pada tiap baris berisi row action menu `[⋯]`
16. Verifikasi Published At hanya tanggal, tanpa jam
17. Verifikasi tidak ada kolom Status
18. Verifikasi tidak ada kolom checkbox
19. Verifikasi konten Privacy Policy tidak dirender di halaman utama
20. Verifikasi Footer: pagination menampilkan `1–3 of 3`
21. Verifikasi Footer: page size `10`
22. Verifikasi Footer: navigasi halaman tampil

### TC-AC-PP-02: Badge Active hanya menempel pada versi dengan nomor tertinggi dan tidak ada badge Superseded

23. Amati kolom Version pada ketiga baris
24. Verifikasi hanya baris `Version 3` membawa badge `Active`
25. Verifikasi badge `Active` berseverity success
26. Verifikasi badge `Active` menempel di sel Version
27. Verifikasi baris `Version 2` dan `Version 1` tidak membawa badge apa pun (tidak ada badge "Superseded")
28. Hover badge `Active` pada baris `Version 3`
29. Verifikasi badge `Active` memiliki `aria-label` "Status: Active version"

### TC-AC-PP-03: Format sel kolom Published By memakai nama singkat dengan tooltip nama lengkap pada hover

30. Amati sel Published By baris `Version 3` dan baris `Version 1`
31. Verifikasi sel Published By tampil sebagai plain text `John D` (baris Version 3 dan Version 2) dan `Jane S` (baris Version 1)
32. Verifikasi sel Published By bukan badge dan bukan avatar
33. Hover teks `John D` pada baris `Version 3`
34. Verifikasi tooltip `John Doe` tampil
35. Hover teks `Jane S` pada baris `Version 1`
36. Verifikasi tooltip `Jane Smith` tampil
37. Verifikasi nama `Jane Smith` tetap tampil walaupun akun user tersebut sudah dihapus (bukan `—`)

### TC-AC-PP-05: Teks tautan Version berwarna netral, berubah ke warna primary produk saat hover tanpa underline, dan tidak dipotong

38. Amati warna teks `Version 3` pada keadaan default
39. Verifikasi warna default teks tautan netral (body text)
40. Hover teks `Version 3`
41. Verifikasi warna berubah ke warna primary Admin Console (merah)
42. Verifikasi teks tautan tanpa garis bawah saat hover
43. Amati lebar sel Version dan teks `Version 3`
44. Verifikasi teks `Version 3` tampil utuh tanpa pemotongan `..`
45. Verifikasi tidak ada tooltip pada teks `Version 3`

### TC-AC-PP-06: Klik area baris di luar tautan Version dan row action tidak melakukan aksi apa pun

46. Klik sel Published At baris `Version 3`
47. Verifikasi tidak ada Modal yang terbuka
48. Verifikasi tidak ada navigasi
49. Klik sel Published By baris `Version 3`
50. Verifikasi tidak ada Modal yang terbuka
51. Verifikasi tidak ada navigasi
52. Verifikasi tabel tetap menampilkan 3 baris tanpa perubahan

### TC-AC-PP-79: Tabel Version History tidak menyediakan aksi Delete, Restore, atau Reactivate dan Edit hanya pada baris Active

53. Klik `[⋯]` pada baris `Version 3`, catat opsi, lalu tutup dropdown
54. Verifikasi dropdown baris `Version 3` berisi opsi `Detail` dan `Edit`
55. Klik `[⋯]` pada baris `Version 2`, catat opsi, lalu tutup dropdown
56. Verifikasi dropdown baris `Version 2` hanya berisi `Detail`
57. Klik `[⋯]` pada baris `Version 1`, catat opsi
58. Verifikasi dropdown baris `Version 1` hanya berisi `Detail`
59. Verifikasi tidak ada opsi Delete, Restore, atau Reactivate pada baris mana pun
60. Verifikasi tidak ada icon aksi langsung di luar dropdown `[⋯]`
61. Tutup dropdown `[⋯]`

### TC-AC-PP-163: Halaman Privacy Policy tidak memiliki surface Changelog

62. Amati toolbar tabel
63. Verifikasi toolbar tidak memuat icon Changelog
64. Hover seluruh icon toolbar (Search, Filter, Download)
65. Verifikasi tidak ada icon Changelog
66. Verifikasi tidak ada modal Changelog yang dapat dibuka

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec read-only (screening tabel), tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 3, 9, 28, 33, 35, 40, 61, 64 adalah aksi hover/susur atau penutupan dropdown yang menjadi prasyarat asersi (S-14); langkah 9 ditambahkan karena asersi tooltip "Column Visibility" pada TC-AC-PP-01 membutuhkan hover. Langkah 23, 30, 38, 43, 62 adalah penanda pengamatan sebelum Verifikasi. Perilaku klik header `(⋯)` membuka overlay Column Visibility diuji pada TC-AC-PP-128 (spec 043).
- Verifikasi langkah 2 (halaman tampil) diturunkan dari tanda "→" di kolom Langkah Uji TC-AC-PP-01, bukan dari kolom Expected Result; ditambahkan sebagai penanda state sebelum asersi layout (S-03).
- Verifikasi langkah 15 (sel Actions berisi row action menu) berasal dari klausa "body per baris = row action menu" pada Expected b.i TC-AC-PP-01; isi dropdown per baris diasersi rinci pada TC-AC-PP-79 (langkah 53 sampai 60).
- Penyimpangan urutan: TC-AC-PP-79 dan TC-AC-PP-163 ditaruh sesudah TC-AC-PP-06 (semua screening tanpa aksi tulis); urutan TC sumber tidak memengaruhi state karena spec tidak mengubah data.
- Pembagian TC lintas spec: row action Total Control juga muncul pada TC-AC-PP-17 (spec 009, Role Matrix visibilitas); TC-AC-PP-79 di sini memeriksa tiga baris tanpa opsi Delete/Restore/Reactivate.
- Ukuran spec (66 langkah, melewati sekitar 35): langkah membengkak karena tiap klausa Expected menjadi satu Verifikasi (S-01). Satu dataset (Riwayat A), satu akun, tanpa aksi tulis, dan tiap blok TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal; spec tidak dipecah (konvensi bagian 3, batas ukuran).
- Temuan untuk QA:
  - TC-AC-PP-05 menyebut warna hover "warna primary Admin Console (merah)" tanpa nilai warna atau token; asersi memakai deskripsi TC dan perlu nilai acuan dari QA/FE.
  - TC-AC-PP-01 Expected b.iii (tanpa icon Changelog dan tanpa tombol Create di toolbar) tumpang tindih dengan TC-AC-PP-163; keduanya tetap diasersi sesuai TC.
