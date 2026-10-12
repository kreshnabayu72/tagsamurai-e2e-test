---
id: TC-GS-BRAND-E2E-025-konflik-create-edit-dua-admin
title: "Konflik Create dan Edit Brand oleh Dua Admin"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-55
  - TC-GS-BRAND-237
  - TC-GS-BRAND-236
  - TC-GS-BRAND-90
coverage:
  web: automated
---

# Konflik Create dan Edit Brand oleh Dua Admin

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (admin kedua): Total Control Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Fixture akun belum ada; tim FE menyiapkan akun ini di Client A.
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` spec ini (seedSession, kredensial dari env var) dan berada di Global Settings > Master Reference > Brand. Hook `after` menutup konteks Sesi B dan mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis: `Solace Co {runId}-025` (D-10, dibuat Sesi B pada TC-55), `Lumen Co {runId}-025` (D-32, dibuat Sesi A pada TC-237); seeding lewat API di hook `before` (tidak menumpang spec lain): `Kite Co {runId}-025` (D-31) dan `Ash Co {runId}-025` (D-16), keduanya bebas relasi. Nama hasil perubahan: `Kite A {runId}-025`, `Kite B {runId}-025` (nilai akhir), `Ash Group {runId}-025` (tidak pernah tersimpan).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API `Solace Co {runId}-025`, `Lumen Co {runId}-025`, `Kite Co {runId}-025`, `Kite A {runId}-025`, `Kite B {runId}-025`, `Ash Co {runId}-025`, dan `Ash Group {runId}-025` bila masih ada.
- Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > Master Reference > Brand.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; membaca status respons Submit (422); langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-BRAND-55: Re-check keunikan atomik saat Submit menolak nama yang dibuat admin lain setelah debounce

1. [Sesi A] Klik [+ Brand] → form Create Brand terbuka
2. [Sesi A] Ketik `Solace Co {runId}-025` pada field Brand Name
3. [Sesi A] Tunggu ±500 ms (debounce pengecekan keunikan)
4. [Sesi A] Verifikasi tidak ada error inline pada field Brand Name
5. [Sesi B] Klik [+ Brand]
6. [Sesi B] Ketik `Solace Co {runId}-025` pada field Brand Name
7. [Sesi B] Klik [Submit]
8. [Sesi B] Tunggu hingga Create selesai (toast sukses tampil dan `Solace Co {runId}-025` ada di tabel)
9. [Sesi A] Klik [Submit]
10. [Sesi A] Verifikasi respons Submit berstatus `422`
11. [Sesi A] Verifikasi error inline `Brand Name already exists`
12. [Sesi A] Verifikasi form tetap terbuka dengan input `Solace Co {runId}-025` dipertahankan
13. [Sesi B] Muat ulang halaman Brand, lalu cari `Solace Co {runId}-025`
14. [Sesi B] Verifikasi hanya ada satu baris `Solace Co {runId}-025` di tabel
15. [Sesi A] Klik `✕` di header form Create Brand
16. [Sesi A] Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
17. [Sesi A] Klik [Leave]

### TC-GS-BRAND-237: Dua admin membuat nama baru yang sama bersamaan

18. [Sesi A] Klik [+ Brand]
19. [Sesi B] Klik [+ Brand]
20. [Sesi A] Ketik `Lumen Co {runId}-025` pada field Brand Name
21. [Sesi B] Ketik `Lumen Co {runId}-025` pada field Brand Name
22. [Sesi A dan Sesi B] Tunggu ±500 ms (debounce pengecekan keunikan)
23. [Sesi A] Klik [Submit]
24. [Sesi A] Verifikasi toast sukses tampil
25. [Sesi B] Klik [Submit]
26. [Sesi B] Verifikasi respons Submit berstatus `422`
27. [Sesi B] Verifikasi error inline `Brand Name already exists`
28. [Sesi B] Verifikasi form tetap terbuka
29. [Sesi B] Klik `✕` di header form Create Brand
30. [Sesi B] Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
31. [Sesi B] Klik [Leave]

### TC-GS-BRAND-236: Edit bersamaan oleh dua admin: last-write-wins

32. [Sesi A] Cari baris `Kite Co {runId}-025`, lalu klik `⋯` > Edit
33. [Sesi B] Cari baris `Kite Co {runId}-025`, lalu klik `⋯` > Edit
34. [Sesi A] Ubah isi field Brand Name menjadi `Kite A {runId}-025`
35. [Sesi A] Klik [Save]
36. [Sesi A] Verifikasi toast sukses: "Success, brand has been updated."
37. [Sesi A] Verifikasi tidak ada dialog konflik
38. [Sesi B] Ubah isi field Brand Name menjadi `Kite B {runId}-025`
39. [Sesi B] Klik [Save]
40. [Sesi B] Verifikasi toast sukses: "Success, brand has been updated."
41. [Sesi B] Verifikasi tidak ada dialog konflik
42. [Sesi A] Muat ulang halaman Brand, lalu cari `Kite`
43. [Sesi A] Verifikasi nilai akhir `Kite B {runId}-025` ada di tabel dan `Kite A {runId}-025` tidak ada

### TC-GS-BRAND-90: Edit Brand yang sudah dihapus admin lain

44. [Sesi A] Cari baris `Ash Co {runId}-025`, lalu klik `⋯` > Edit
45. [Sesi A] Ubah isi field Brand Name menjadi `Ash Group {runId}-025` (belum disimpan)
46. [Sesi B] Muat ulang halaman Brand, cari baris `Ash Co {runId}-025`, lalu klik `⋯` > Delete
47. [Sesi B] Klik [Delete]
48. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
49. [Sesi A] Klik [Save]
50. [Sesi A] Verifikasi modal tertutup
51. [Sesi A] Verifikasi toast netral: "This brand is no longer available."
52. [Sesi A] Verifikasi tabel di-refresh dan `Ash Co {runId}-025` tidak ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas harness: multi-konteks (dua sesi admin), bagian 3 prinsip 13c.
- Urutan TC: Create (TC-55, TC-237) lebih dulu, lalu Edit bersamaan (TC-236), dan TC-90 terakhir karena melibatkan penghapusan brand oleh Sesi B (aksi yang menghapus data paling akhir, prinsip 5).
- Spec memuat 52 langkah (melewati batas smell sekitar 35) karena tiap aksi per sesi ditulis satu baris; seluruhnya satu kelas harness (dua sesi admin), sehingga tidak dipecah.
- Langkah penghubung: langkah 8 dan 48 (menunggu aksi Sesi B selesai sebelum Sesi A melanjutkan); langkah 13, 42, dan 46 (muat ulang halaman supaya tabel menampilkan data terbaru); langkah 15 sampai 17 dan 29 sampai 31 (membuang form Create yang dirty lewat `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]`; teks dan tombol dialog dari TC-GS-BRAND-60 dan TC-GS-BRAND-61); langkah 22 (menunggu debounce supaya kedua form tidak menampilkan error sebelum Submit).
- Asersi "Hanya satu Solace Co di tabel" (TC-55 c) diperiksa dari Sesi B setelah muat ulang (langkah 13 dan 14), karena form di Sesi A masih terbuka dan menutup tabel.
- Temuan untuk QA: TC-237 butir a tidak mencantumkan teks toast sukses Create, sehingga langkah 24 hanya menyebut "toast sukses".
