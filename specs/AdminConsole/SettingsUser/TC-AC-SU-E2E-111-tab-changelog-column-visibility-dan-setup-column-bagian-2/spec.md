---
id: TC-AC-SU-E2E-111-tab-changelog-column-visibility-dan-setup-column-bagian-2
title: "Tab Changelog: Setup Column (Pin, Reset to Default, Tutup tanpa Save, Satu Kolom Tersisa)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-396
  - TC-AC-SU-397
  - TC-AC-SU-398
  - TC-AC-SU-399
coverage:
  web: automated
---

# Tab Changelog: Setup Column (Pin, Reset to Default, Tutup tanpa Save, Satu Kolom Tersisa)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-111` (email `janesmith+{runId}-111@qwertysystem.net`) dengan sedikitnya 1 entri Changelog (isi entri tidak diasersi, dipakai sebagai precondition TC).
- Konfigurasi kolom Tab Changelog saat spec mulai adalah default. Lebar viewport 1280px diatur spec pada TC-396 agar tabel dapat di-scroll horizontal dan dipulihkan di akhir spec. Pemulihan konfigurasi kolom yang disimpan spec: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan `[Reset to Default]`).
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-396: Pin dan unpin kolom

1. Cari `Jane Smith {runId}-111` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `Changelog`
3. Atur lebar viewport menjadi 1280px
4. Klik header `⋯`, lalu klik `[Setup Column]`
5. Klik icon Pin pada `Date`
6. Klik `[Save]`
7. Scroll tabel secara horizontal
8. Verifikasi kolom `Date` tetap terlihat (sticky) saat tabel di-scroll horizontal
9. Muat ulang halaman dengan F5
10. Klik tab `Changelog`
11. Scroll tabel secara horizontal
12. Verifikasi kolom `Date` tetap terlihat (sticky) setelah F5
13. Klik header `⋯`, lalu klik `[Setup Column]`
14. Klik icon Pin pada `Date` untuk melepas pin
15. Klik `[Save]`
16. Scroll tabel secara horizontal
17. Verifikasi kolom `Date` ikut ter-scroll

### TC-AC-SU-397: Reset to Default

18. Klik header `⋯`, lalu klik `[Setup Column]`
19. Unceklis kolom `Action`, drag `Modified By` ke posisi pertama, dan klik icon Pin pada `Date` (dipakai sebagai precondition TC, tidak diasersi)
20. Klik `[Save]`
21. Klik header `⋯`, lalu klik `[Setup Column]`
22. Klik `[Reset to Default]`
23. Verifikasi Live Preview kembali ke urutan default `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` dengan setiap kolom tampil
24. Verifikasi Live Preview tanpa pin
25. Klik `[Save]`
26. Verifikasi tabel memakai konfigurasi default
27. Muat ulang halaman dengan F5
28. Klik tab `Changelog`
29. Verifikasi tabel tetap memakai konfigurasi default

### TC-AC-SU-398: Tutup popup tanpa Save membuang perubahan

30. Klik header `⋯`, lalu klik `[Setup Column]`
31. Unceklis kolom `Action`, lalu drag `Modified By` ke posisi pertama
32. Klik icon `(X)` pada popup
33. Verifikasi popup tertutup tanpa dialog
34. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default)
35. Klik header `⋯`, lalu klik `[Setup Column]`
36. Unceklis kolom `Field`
37. Tekan `Esc`
38. Verifikasi popup tertutup tanpa dialog
39. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (default)

### TC-AC-SU-399: Satu kolom tersisa tidak bisa di-unceklis

40. Klik header `⋯`, lalu klik `[Setup Column]`
41. Unceklis kolom `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By`
42. Hover checkbox `Date`
43. Verifikasi checkbox `Date` tetap tampil dan checked
44. Verifikasi checkbox `Date` berstatus disabled
45. Verifikasi tooltip `At least one column must remain visible.` tampil
46. Klik icon `(X)` pada popup
47. Pulihkan lebar viewport ke ukuran semula

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Muat ulang F5 diikuti klik tab `Changelog` adalah langkah penghubung. Pada TC-397 langkah yang mengubah konfigurasi (Unceklis `Action`, drag, Pin) adalah precondition TC ('konfigurasi sudah diubah') dan tidak diasersi. `[Save]` Setup Column adalah aksi sisi klien tanpa langkah 'Tunggu aksi selesai'.
- Konfigurasi kembali ke default pada akhir TC-396 (unpin lalu Save), akhir TC-397 (Reset to Default), dan TC-398 (tanpa Save), sehingga tiap TC dimulai dari default (S-09).
- Temuan untuk QA:
  - TC-396 memakai lebar viewport 1280px sebagai precondition; ukuran viewport awal tidak dinyatakan sehingga langkah pemulihan ditulis 'ukuran semula'.
  - TC-396 tidak menyatakan cara unpin; spec mengasumsikan klik icon Pin yang sama.
  - Asumsi bahwa setelah F5 halaman Detail tidak membuka tab yang sedang diuji (sehingga perlu klik tab) tidak dinyatakan di TC.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (47 langkah nominal, sekitar 47 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
