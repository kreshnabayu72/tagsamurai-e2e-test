---
id: TC-AC-DC-E2E-051-multi-konteks-dua-admin-add
title: "Dua Admin: Add Subcategory saat Parent Dihapus, Node Hasil Pencarian Dihapus, dan Hierarchy Depth Limit Turun"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-94
  - TC-AC-DC-305
  - TC-AC-DC-93
coverage:
  web: automated
---

# Dua Admin: Add Subcategory saat Parent Dihapus, Node Hasil Pencarian Dihapus, dan Hierarchy Depth Limit Turun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Admin kedua (Pre-setup #9, Maya Putri, Total Control Principal, berhak mengubah Lifecycle Settings): `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DC_TC2_PASSWORD` (nama env baru; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`, satu arti: password Total Control kedua Admin Console Settings Device Category). Admin kedua bertindak lewat sesi API aktor (hanya memicu perubahan state; tidak ada konteks UI kedua).
- Login akun aktor pertama di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- State global yang diubah: Hierarchy Depth Limit entitas uji (Pre-setup #18, nilai awal 50) diset 6 di hook `before` spec ini, diturunkan menjadi 5 oleh admin kedua pada TC-93, dan dipulihkan ke 50 di hook `after`. Kemampuan mengubah Hierarchy Depth Limit pada Lifecycle Settings lewat sesi API admin kedua disediakan tim FE/BE (TC tidak menyebut endpoint; tidak dikarang di spec ini).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware`, `Handheld Reader`, dan rantai `Smart Fixed Reader` > `Rantai L3` > `Rantai L4` > `Rantai L5`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-051`): `Daun {runId}-051` (leaf; TC-94, dihapus admin kedua) dan `Daun Cari {runId}-051` (leaf; TC-305, dihapus admin kedua). Hook `after` menghapus sisa node milik spec lewat sesi API. Entri Changelog hasil seeding, aksi admin kedua, dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Parent dihapus admin lain sebelum Submit (TC-94)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Daun {runId}-051`, klik aksi `+ Subcategory`
3. Ketik `Anak Hilang {runId}-051` tetapi belum klik `[Submit]`
4. Admin kedua (sesi API) menghapus node `Daun {runId}-051` hingga terhapus
5. Tunggu aksi admin kedua selesai
6. Klik `[Submit]`
7. Verifikasi toast netral "This category is no longer available."
8. Verifikasi toast tersebut bukan toast error
9. Verifikasi input inline Add ditutup
10. Verifikasi tree di-refresh sehingga `Daun {runId}-051` tidak lagi tampil
11. Verifikasi `Hardware` dan `Handheld Reader` tetap ter-expand

### Node hasil pencarian dihapus admin lain (TC-305)

12. Ketik Search tree `Daun Cari {runId}-051` pada TreeSearchInput, tekan Enter
13. Hover node `Daun Cari {runId}-051`, klik aksi `+ Subcategory`
14. Ketik `Anak Hilang {runId}-051b` tetapi belum klik `[Submit]`
15. Admin kedua (sesi API) menghapus node `Daun Cari {runId}-051` hingga terhapus
16. Tunggu aksi admin kedua selesai
17. Klik `[Submit]`
18. Verifikasi toast netral "This category is no longer available."
19. Verifikasi kotak TreeSearchInput masih berisi `Daun Cari {runId}-051`
20. Verifikasi pencarian dijalankan ulang dan tree menampilkan empty state dengan judul "No results found" di bawah `All Categories`
21. Klik `(←)` pada TreeSearchInput

### Hierarchy Depth Limit turun antara input dibuka dan Submit (TC-93)

22. Expand `Hardware`, `Smart Fixed Reader`, `Rantai L3`, `Rantai L4` sampai `Rantai L5` terlihat
23. Hover node `Rantai L5`, klik aksi `+ Subcategory`
24. Ketik `Batas Enam {runId}-051` tetapi belum klik `[Submit]`
25. Admin kedua (sesi API) menurunkan Hierarchy Depth Limit menjadi 5 hingga tersimpan
26. Tunggu aksi admin kedua selesai
27. Klik `[Submit]`
28. Verifikasi dialog blok "Cannot Add Category" dengan isi "You've reached the platform limit of 5 levels. Contact support if you need a higher limit." dan satu tombol `[OK]`
29. Klik `[OK]`
30. Verifikasi input Add ditutup tanpa menyimpan
31. Verifikasi tampilan tree tidak di-refresh (tidak ada perubahan pada tree)

### Pemeriksaan akhir tidak ada node dan tidak ada entri Create

32. Klik ikon Changelog pada header Sidebar Category
33. Verifikasi modal Changelog memuat entri `Delete` untuk Category `Daun {runId}-051` (anchor: aksi admin kedua tercatat)
34. Ketik Search `Anak Hilang {runId}-051`, tekan Enter
35. Verifikasi empty state "No results found" (tidak ada entri Create untuk `Anak Hilang {runId}-051` dan `Anak Hilang {runId}-051b`)
36. Ganti isi kotak search dengan `Batas Enam {runId}-051`, tekan Enter
37. Verifikasi empty state "No results found" (tidak ada entri Create untuk `Batas Enam {runId}-051`)
38. Klik `[×]` pada modal Changelog

## Notes

- Spec ini melewati sekitar 35 langkah (38) karena tiga TC masing-masing memerlukan setup dua pelaku dan satu blok pemeriksaan akhir yang menggabungkan tiga asersi "tidak ada node dan tidak ada entri log". Seluruh blok satu topik (Add saat state berubah oleh admin kedua) dan satu kelas harness (dua pelaku); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- S-03, langkah penghubung: langkah 1 dan 22 (membuka cabang tree), langkah 5, 16, 26 (menunggu aksi admin kedua selesai sebelum aksi sesi pertama), langkah 12 (Search tree untuk menjalankan pencarian aktif), langkah 21 (mengosongkan TreeSearchInput), langkah 29 (`[OK]` menutup dialog blok, bagian Expected TC-93), langkah 38 (menutup modal Changelog). Search pada modal Changelog (langkah 34, 36) menemukan entri berdasarkan nama bersuffix unik (baseline nol).
- Pelaku kedua memakai sesi API (langkah 4, 15, 25) karena hanya memicu perubahan state dan hasil di sesi itu tidak diasersi.
- S-05: klausa "node tidak dibuat dan tidak ada entri log Create" pada TC-94, TC-305, TC-93 dinyatakan sebagai asersi nama bersuffix unik dengan baseline nol (langkah 33 sampai 37), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Hapus Daun` sebagai parent yang dihapus admin kedua. Spec memakai `Daun {runId}-051` dan `Daun Cari {runId}-051` milik spec; nama anak `Anak Hilang` diberi suffix.
  - TC-93 dan TC-94 ditandai `Manual Only (d)` pada kolom Automation; dua pelaku tidak menghambat penulisan karena pelaku kedua hanya memicu perubahan state lewat sesi API.
  - TC-93 menyebut "tree tidak di-refresh" tanpa cara mengamatinya; spec mengasersi tampilan tree tidak berubah.
  - TC-93 menyebut sesi admin kedua "dengan akses Lifecycle Settings" tanpa mekanisme penurunan limit lewat sesi API; disediakan tim FE/BE.
