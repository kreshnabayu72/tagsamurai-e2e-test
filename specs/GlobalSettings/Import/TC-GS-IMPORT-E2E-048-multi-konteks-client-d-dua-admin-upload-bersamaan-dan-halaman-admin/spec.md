---
id: TC-GS-IMPORT-E2E-048-multi-konteks-client-d-dua-admin-upload-bersamaan-dan-halaman-admin
title: "Multi-Konteks Client D: Dua Admin Upload Bersamaan dan Halaman Admin Kedua yang Basi"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-75
  - TC-GS-IMPORT-829
coverage:
  web: automated
---

# Multi-Konteks Client D: Dua Admin Upload Bersamaan dan Halaman Admin Kedua yang Basi

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks) berjalan di konteks browser terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > Brand Client D:
  - Sesi TC: Total Control Client D (Wulan Sari) `totalControl_automated_qaTeam4@qwertysystem.net`, `Spectra.env.GS_CLIENTD_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client D (Putra Mahendra) `totalControlSecond_automated_qaTeam4@qwertysystem.net`, `Spectra.env.GS_CLIENTD_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua dan mengembalikan sesi ke akun default suite.
- Kemampuan teknis: penghalang sinkronisasi dua konteks agar kedua `[Confirm Mapping]` ditekan pada waktu yang sama (TC-GS-IMPORT-75).
- Data: `brand-12.csv` (D-01; header `Brand Name`, 12 baris) dan `brand-6.csv` (header `Brand Name`; Nikon, Ricoh, Xerox, Sony, Panasonic, Sharp). Client D tanpa draft Tab Brand sebelum tiap TC (Kontrak Fixture R1).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import untuk kedua sesi.
- Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Brand Client D (18 baris) direset lewat skrip fixture di akhir tiap blok (R1).

## Test Steps

### TC-GS-IMPORT-75: Dua admin meng-upload bersamaan saat belum ada draft

1. [Sesi TC] Klik [Upload File]
2. [Sesi TC] Pilih berkas `brand-12.csv` di file picker
3. [Sesi TC] Verifikasi Modal Column Mapping terbuka
4. [Sesi Admin kedua] Klik [Upload File]
5. [Sesi Admin kedua] Pilih berkas `brand-6.csv` di file picker
6. [Sesi Admin kedua] Verifikasi Modal Column Mapping terbuka
7. [Sesi TC dan Sesi Admin kedua] Tekan [Confirm Mapping] pada waktu yang sama
8. [Sesi TC dan Sesi Admin kedua] Tunggu aksi selesai (modal tertutup)
9. [Sesi TC dan Sesi Admin kedua] Verifikasi Breadcrumb `Import > Brand` tampil
10. Verifikasi tidak ada dialog Confirm Append Draft di layar kedua sesi
11. Verifikasi tidak ada pesan konflik bagi Admin kedua
12. Muat ulang halaman Import pada kedua sesi
13. Verifikasi hanya satu draft Brand terbentuk (Staging Table kedua sesi menampilkan draft yang sama)
14. Verifikasi Staging Metric Cards pada kedua sesi menampilkan Total Rows 18
15. Verifikasi Pagination pada kedua sesi `Showing 1 - 10 of 18 items`
16. Reset Client D ke tanpa draft Tab Brand lewat skrip fixture

### TC-GS-IMPORT-829: Halaman Admin kedua yang belum menampilkan draft

17. [Sesi Admin kedua] Muat ulang halaman Import > Brand dan perhatikan Dropzone
18. [Sesi Admin kedua] Tunggu aksi selesai (permintaan mendapat respons)
19. [Sesi TC] Muat ulang halaman Import > Brand
20. [Sesi TC] Klik [Upload File]
21. [Sesi TC] Pilih berkas `brand-12.csv` di file picker
22. [Sesi TC] Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
23. [Sesi TC] Tunggu aksi selesai (modal tertutup)
24. [Sesi Admin kedua] Tanpa memuat ulang halaman, klik [Upload File]
25. [Sesi Admin kedua] Pilih berkas `brand-6.csv` di file picker
26. [Sesi Admin kedua] Verifikasi Modal Column Mapping terbuka
27. [Sesi Admin kedua] Verifikasi tidak ada dialog Append to Draft
28. [Sesi Admin kedua] Klik [Confirm Mapping] tanpa mengubah dropdown File Column dari hasil auto-match
29. [Sesi Admin kedua] Verifikasi modal tertutup
30. [Sesi Admin kedua] Verifikasi toast "Success, row has been added."
31. [Sesi Admin kedua] Verifikasi tidak ada dialog Draft Is Being Edited
32. [Sesi Admin kedua] Verifikasi tidak ada pesan error
33. [Sesi Admin kedua] Muat ulang halaman Import > Brand
34. [Sesi Admin kedua] Verifikasi Breadcrumb `Import > Brand` tampil
35. [Sesi Admin kedua] Verifikasi Unsaved Banner tidak tampil (umur draft kurang dari 24 jam)
36. [Sesi Admin kedua] Verifikasi Staging Metric Cards: Total Rows 18 (Active), Ready to Import 18, Errors 0 (Disabled), Duplicates 0 (Disabled)
37. [Sesi Admin kedua] Verifikasi Pagination "Showing 1 - 10 of 18 items"
38. Reset Client D ke tanpa draft Tab Brand lewat skrip fixture

## Notes

- Spec melewati sekitar 35 langkah (38 langkah). Seluruhnya satu topik dengan akun dan client yang sama; langkah pembuka seed eksplisit (suite.md, `beforeEach` hanya menyiapkan keadaan dasar) menambah langkah pada spec yang sudah mendekati batas, dan memecahnya hanya menambah login, hook, dan pembersihan tanpa menambah daya deteksi.
- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (kelas c, prinsip 13c); kedua sesi UI menjadi objek asersi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 dan 38 (reset Client D); langkah 8 (menunggu kedua Confirm Mapping selesai sebelum absence dan muat ulang); langkah 23 (Sesi TC menunggu Confirm Mapping selesai sebelum Sesi Admin kedua mengunggah); langkah 17 (memuat ulang halaman Admin kedua sesudah reset langkah 16 sebelum draft ada, TC-GS-IMPORT-829 langkah 1 hanya memerhatikan Dropzone tanpa Expected); langkah 18 (menunggu pembacaan halaman Admin kedua mendapat respons sebelum Sesi TC mengunggah); langkah 19 (Sesi TC memuat ulang halaman Import > Brand sesudah reset langkah 16, supaya Sesi TC tidak berada di state halaman draft 18 baris dari TC-GS-IMPORT-75 saat langkah 20, S-03/S-09). Penanda pada langkah 8 dan 18 tidak ada di TC.
- Langkah 9 (`Verifikasi` Breadcrumb `Import > Brand` tampil pada kedua sesi) adalah asersi tambahan di luar Expected TC: anchor positif untuk absence dialog dan pesan konflik pada langkah 10 dan 11 (8b butir 2, S-03).
- Langkah 34 (`[Sesi Admin kedua] Verifikasi` Breadcrumb `Import > Brand` tampil) adalah asersi tambahan di luar Expected TC: anchor positif untuk absence Unsaved Banner pada langkah 35 sesudah muat ulang (8b butir 2, S-03).
- Langkah 31 dan 32 (absence dialog dan pesan error) memakai toast sukses langkah 30 sebagai anchor.
- Temuan untuk QA:
  - TC-GS-IMPORT-75 bertanda Manual Only (d) dua sesi paralel; spec tetap dibuat dan kemampuan penghalang sinkronisasi dua konteks dicatat di Prerequisites.
  - TC-GS-IMPORT-75 Expected b ("hanya satu draft Brand terbentuk") tidak menyebut cara membedakan satu draft dari dua draft selain total 18; spec mengasersi lewat kedua sesi menampilkan draft yang sama dan Total Rows 18.
