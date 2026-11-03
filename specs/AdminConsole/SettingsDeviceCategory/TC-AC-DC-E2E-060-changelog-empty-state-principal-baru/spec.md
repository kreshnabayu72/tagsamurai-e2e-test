---
id: TC-AC-DC-E2E-060-changelog-empty-state-principal-baru
title: "Modal Changelog Category: Empty State Principal Tanpa Riwayat dan Transisi Keluar dari Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-152
  - TC-AC-DC-288
  - TC-AC-DC-289
coverage:
  web: automated
---

# Modal Changelog Category: Empty State Principal Tanpa Riwayat dan Transisi Keluar dari Empty State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Fresh `totalControlFresh_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 13, Principal `Principal Tanpa Riwayat`; password `Spectra.env.AC_DCFRESH_TC_PASSWORD`, nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14) tersedia untuk entitas Principal biasa; entitas `Principal Tanpa Riwayat` (No 13) hanya memiliki pohon default hasil seed tanpa aksi Category apa pun, sehingga Changelog-nya kosong.
- Pemulihan: kemampuan fixture BE (disediakan tim FE/BE) memulihkan entitas `Principal Tanpa Riwayat` ke keadaan tanpa aksi Category (pohon default, Changelog kosong) di hook `before` dan `after`.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Data Dinamis (bersuffix `{runId}-060`): node `Pertama {runId}-060` dibuat spec lewat UI di bawah `Handheld Reader` (pohon default Principal baru); dihapus lewat API di hook `after` bila masih ada, tanpa berasumsi seeding berhasil penuh.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-152: Changelog kosong pada Principal baru menampilkan empty state dan seed pohon default tidak tercatat di log

1. Klik ikon Changelog pada header Sidebar Category
2. Verifikasi tabel Changelog tidak menampilkan baris data (seed pohon default tidak menulis entri)
3. Verifikasi empty state menampilkan ilustrasi
4. Verifikasi empty state menampilkan judul "No changelog yet"
5. Verifikasi empty state menampilkan deskripsi "Activities and changes will appear here."
6. Tutup modal lewat icon `[×]`
7. Buka Detail User aktor `totalControlFresh`, klik tab System Log
8. Verifikasi tabel System Log aktor tampil beserta header kolomnya
9. Verifikasi System Log aktor tidak memuat entri dengan Object "Category"
10. Buka Activity Log Admin Console
11. Verifikasi tabel Activity Log tampil beserta header kolomnya
12. Verifikasi Activity Log tidak memuat entri dengan Object "Category"

### TC-AC-DC-288: Dropdown Filter Changelog tanpa sumber data menampilkan No options available

13. Buka halaman Settings > Device > Device Name lewat menu sidebar
14. Klik ikon Changelog pada header Sidebar Category
15. Klik ikon Filter, buka dropdown Action
16. Verifikasi dropdown Action menampilkan teks "No options available"
17. Buka dropdown Category
18. Verifikasi dropdown Category menampilkan teks "No options available"
19. Buka dropdown Modified By
20. Verifikasi dropdown Modified By menampilkan teks "No options available"
21. Verifikasi tidak ada pesan error pada Filter Panel

### TC-AC-DC-289: Aksi Category pertama pada Principal baru mengeluarkan Changelog dari empty state

22. Tutup modal lewat icon `[×]`
23. Expand `Hardware` lalu `Handheld Reader`
24. Hover node `Handheld Reader` lalu klik aksi `+ Subcategory`
25. Ketik `Pertama {runId}-060` pada input inline Add, klik `[Submit]`
26. Tunggu aksi selesai
27. Klik ikon Changelog pada header Sidebar Category
28. Verifikasi empty state "No changelog yet" tidak tampil
29. Verifikasi tabel memuat tepat satu baris
30. Verifikasi Action baris itu "Create"
31. Verifikasi Category baris itu `Pertama {runId}-060`
32. Verifikasi Field baris itu "Category"
33. Verifikasi Old Value baris itu "—"
34. Verifikasi New Value baris itu `Pertama {runId}-060`
35. Verifikasi Modified By baris itu berformat `[First Name] [Last Initial]`

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-152, 288, 289). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di spec: 152, 288, lalu 289 (aksi tulis di akhir). Urutan 288 mendahului 289 karena 288 mengasersi dropdown tanpa opsi sehingga harus mendahului entri pertama yang dibuat 289 (S-10, S-14).
- P-1: asersi absence TC-AC-DC-152 butir c (kelas g) berada di spec ini karena bergantung pada state entitas uji khusus `Principal Tanpa Riwayat` (Pre-setup No 13) yang tidak dapat dibentuk ulang di spec absence tanpa biaya besar.
- Node tulis `Pertama {runId}-060` memakai nama bersuffix (spec membuat node sendiri); TC memakai nama literal `Pertama`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 6, 13, 22, dan langkah 26 (Tunggu aksi selesai sesudah `[Submit]` pada langkah 25 yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8).
- Temuan untuk QA:
  - Asersi absence TC-AC-DC-152 butir c tidak punya anchor positif di TC (isi System Log aktor dan Activity Log pada Principal baru tidak disebut); spec memakai Verifikasi tabel tampil beserta header kolomnya sebagai anchor terbatas (8b.2). Perlu data anchor dari QA.
  - TC-AC-DC-152 langkah 3 menyebut 'Buka Detail User aktor lalu tab System Log' tanpa jalur navigasi; spec mengikuti kalimat TC.
  - Nama env password akun `totalControlFresh` (`AC_DCFRESH_TC_PASSWORD`) dinamai penulis spec dan belum terdaftar; fixture entitas Principal `Principal Tanpa Riwayat` belum ada dan disediakan tim FE/BE.
  - TC-AC-DC-289 membuat node di bawah `Handheld Reader` literal pada pohon default Principal baru; node dihapus di hook `after` dan entitas ini dipulihkan fixture BE agar 152 dan 288 dapat diulang.
