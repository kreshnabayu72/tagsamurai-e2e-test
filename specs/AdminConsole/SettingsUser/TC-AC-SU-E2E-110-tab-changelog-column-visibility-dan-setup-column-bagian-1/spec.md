---
id: TC-AC-SU-E2E-110-tab-changelog-column-visibility-dan-setup-column-bagian-1
title: "Tab Changelog: Column Visibility dan Setup Column (Screening, Toggle Kolom, Reorder)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-392
  - TC-AC-SU-393
  - TC-AC-SU-394
  - TC-AC-SU-395
coverage:
  web: automated
---

# Tab Changelog: Column Visibility dan Setup Column (Screening, Toggle Kolom, Reorder)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-110` (email `janesmith+{runId}-110@qwertysystem.net`) dengan sedikitnya 1 entri Changelog (isi entri tidak diasersi, dipakai sebagai precondition TC).

| Kolom toggle |
|---|
| Date |
| Action |
| Field |
| Old Value |
| New Value |

- Konfigurasi kolom Tab Changelog saat spec mulai adalah default. Pemulihan konfigurasi kolom yang disimpan spec: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan `[Reset to Default]`).
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-392: Screening Overlay Column Visibility Tab Changelog

1. Cari `Jane Smith {runId}-110` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `Changelog`
3. Hover header kolom Actions `⋯`
4. Verifikasi tooltip `Column Visibility` tampil
5. Klik header `⋯`
6. Verifikasi overlay terbuka dengan tombol `[Setup Column]` di atas
7. Verifikasi daftar kolom pada overlay berurutan default `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
8. Verifikasi setiap kolom pada overlay berupa checkbox checked dan enabled
9. Verifikasi setiap kolom pada overlay memiliki drag handle

### TC-AC-SU-393: Screening Popup Setup Column Tab Changelog

10. Klik `[Setup Column]`
11. Verifikasi header popup menampilkan Title `Setup Column`
12. Verifikasi header popup menampilkan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
13. Verifikasi header popup menampilkan icon `(X)`
14. Verifikasi body popup memuat daftar `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
15. Verifikasi setiap baris pada body popup berupa checkbox checked dan enabled
16. Verifikasi setiap baris pada body popup memiliki drag handle
17. Verifikasi setiap baris pada body popup memiliki icon Pin
18. Verifikasi Live Preview menampilkan header dan isi sel sesuai tabel asli
19. Verifikasi footer popup menampilkan `[Reset to Default]` dan `[Save]` rata kanan
20. Verifikasi footer popup tidak memuat `[Cancel]`
21. Klik icon `(X)` pada popup

### TC-AC-SU-394: Unceklis atau ceklis kolom lalu Save

22. Klik header `⋯`, lalu klik `[Setup Column]`
23. Unceklis kolom pada baris tabel 'Kolom toggle' di popup
24. Verifikasi Live Preview menyembunyikan kolom itu
25. Ceklis kembali kolom itu
26. Verifikasi Live Preview menampilkan kembali kolom itu
27. Unceklis kolom `Action`
28. Klik `[Save]`
29. Verifikasi kolom `Action` tidak tampil di tabel sementara kolom `Date`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil
30. Muat ulang halaman dengan F5
31. Klik tab `Changelog`
32. Verifikasi kolom `Action` tetap tersembunyi di tabel sementara kolom `Date` tampil
33. Klik header `⋯`, lalu klik `[Setup Column]`
34. Ceklis kembali kolom `Action`, lalu klik `[Save]`

### TC-AC-SU-395: Drag reorder kolom lalu Save

35. Klik header `⋯`, lalu klik `[Setup Column]`
36. Drag `Modified By` ke posisi pertama
37. Drag `Date` ke posisi terakhir
38. Verifikasi Live Preview mengikuti urutan baru (Modified By pertama, Date terakhir)
39. Klik `[Save]`
40. Verifikasi tabel memakai urutan kolom baru
41. Muat ulang halaman dengan F5
42. Klik tab `Changelog`
43. Verifikasi tabel tetap memakai urutan kolom baru

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Toggle kolom diulang per baris tabel 'Kolom toggle': langkah 23 sampai 26 (5 kolom).
- Muat ulang F5 diikuti klik tab `Changelog` adalah langkah penghubung; mengembalikan centang kolom `Action` dan Save memulihkan konfigurasi sebelum TC-395 (S-09). `[Save]` Setup Column adalah aksi sisi klien tanpa langkah 'Tunggu aksi selesai'.
- Temuan untuk QA:
  - Penyimpanan konfigurasi Setup Column Tab Changelog (spec ini dan 111) belum terdaftar di `suite.md` sebagai konfigurasi yang dipulihkan hook `after` (konvensi bagian 4); perlu ditambahkan oleh pemilik suite.
  - Asumsi bahwa setelah F5 halaman Detail tidak membuka tab yang sedang diuji (sehingga perlu klik tab) tidak dinyatakan di TC.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (43 langkah nominal, sekitar 59 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
