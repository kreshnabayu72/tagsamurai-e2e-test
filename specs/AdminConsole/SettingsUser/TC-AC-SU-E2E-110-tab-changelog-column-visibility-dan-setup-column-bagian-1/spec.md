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

- Konfigurasi kolom Tab Changelog saat spec mulai adalah default. Konfigurasi kolom yang disimpan TC-395 dipulihkan di langkah 46 lewat `[Reset to Default]` lalu `[Save]`; hook `after` menghapus preferensi kolom di browser sebagai pengaman (kemampuan disediakan tim FE).
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-392: Screening Overlay Column Visibility Tab Changelog

1. Ketik Search `Jane Smith {runId}-110`, tekan Enter
2. Klik Name `Jane Smith {runId}-110`
3. Klik tab `Changelog`
4. Hover header kolom Actions `⋯`
5. Verifikasi tooltip `Column Visibility` tampil
6. Klik header `⋯`
7. Verifikasi overlay terbuka dengan tombol `[Setup Column]` di atas
8. Verifikasi daftar kolom pada overlay berurutan default `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
9. Verifikasi setiap kolom pada overlay berupa checkbox checked dan enabled
10. Verifikasi setiap kolom pada overlay memiliki drag handle

### TC-AC-SU-393: Screening Popup Setup Column Tab Changelog

11. Klik `[Setup Column]`
12. Verifikasi header popup menampilkan Title `Setup Column`
13. Verifikasi header popup menampilkan deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
14. Verifikasi header popup menampilkan icon `(X)`
15. Verifikasi body popup memuat daftar `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
16. Verifikasi setiap baris pada body popup berupa checkbox checked dan enabled
17. Verifikasi setiap baris pada body popup memiliki drag handle
18. Verifikasi setiap baris pada body popup memiliki icon Pin
19. Verifikasi Live Preview menampilkan header dan isi sel sesuai tabel asli
20. Verifikasi footer popup menampilkan `[Reset to Default]` dan `[Save]` rata kanan
21. Verifikasi footer popup tidak memuat `[Cancel]`
22. Klik icon `(X)` pada popup

### TC-AC-SU-394: Unceklis atau ceklis kolom lalu Save

23. Klik header `⋯`, lalu klik `[Setup Column]`
24. Untuk setiap baris tabel "Kolom toggle" di Prerequisites, lakukan langkah 25 sampai 28
25. Unceklis kolom pada baris tabel 'Kolom toggle' di popup
26. Verifikasi Live Preview menyembunyikan kolom itu
27. Ceklis kembali kolom itu
28. Verifikasi Live Preview menampilkan kembali kolom itu
29. Unceklis kolom `Action`
30. Klik `[Save]`
31. Verifikasi kolom `Action` tidak tampil di tabel sementara kolom `Date`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil
32. Muat ulang halaman dengan F5
33. Klik tab `Changelog`
34. Verifikasi kolom `Action` tetap tersembunyi di tabel sementara kolom `Date` tampil
35. Klik header `⋯`, lalu klik `[Setup Column]`
36. Ceklis kembali kolom `Action`, lalu klik `[Save]`

### TC-AC-SU-395: Drag reorder kolom lalu Save

37. Klik header `⋯`, lalu klik `[Setup Column]`
38. Drag `Modified By` ke posisi pertama
39. Drag `Date` ke posisi terakhir
40. Verifikasi Live Preview mengikuti urutan baru (Modified By pertama, Date terakhir)
41. Klik `[Save]`
42. Verifikasi tabel memakai urutan kolom baru
43. Muat ulang halaman dengan F5
44. Klik tab `Changelog`
45. Verifikasi tabel tetap memakai urutan kolom baru
46. Klik header `⋯`, klik `[Setup Column]`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Toggle kolom diulang per baris tabel 'Kolom toggle': langkah 25 sampai 28 (5 kolom).
- Muat ulang F5 diikuti klik tab `Changelog` adalah langkah penghubung; mengembalikan centang kolom `Action` dan Save memulihkan konfigurasi sebelum TC-395 (S-09). `[Save]` Setup Column adalah aksi sisi klien tanpa langkah 'Tunggu aksi selesai'.
- Temuan untuk QA:
  - Penyimpanan konfigurasi Setup Column Tab Changelog (spec ini dan 111) belum terdaftar di `suite.md` sebagai konfigurasi yang dipulihkan hook `after` (konvensi bagian 4); perlu ditambahkan oleh pemilik suite.
  - Asumsi bahwa setelah F5 halaman Detail tidak membuka tab yang sedang diuji (sehingga perlu klik tab) tidak dinyatakan di TC.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Langkah 46 adalah langkah penghubung (tanpa `Verifikasi`; S-03, S-09): memulihkan urutan kolom ke default sesudah TC-395.
- Spec ini melewati sekitar 35 langkah (46 langkah nominal, sekitar 62 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
