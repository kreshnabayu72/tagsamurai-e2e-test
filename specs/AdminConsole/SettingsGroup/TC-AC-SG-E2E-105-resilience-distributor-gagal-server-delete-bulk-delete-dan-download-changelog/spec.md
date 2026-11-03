---
id: TC-AC-SG-E2E-105-resilience-distributor-gagal-server-delete-bulk-delete-dan-download-changelog
title: "Resilience Distributor: Gagal Server pada Delete, Bulk Delete, dan Download Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-147
  - TC-AC-SG-171
  - TC-AC-SG-270
coverage:
  web: automated
---

# Resilience Distributor: Gagal Server pada Delete, Bulk Delete, dan Download Changelog

## Prerequisites

- Mode: FE+BE. Kegagalan dipaksa dengan intercept parsial di atas backend nyata (bagian 6 konvensi); seluruh state lain nyata.
- Akun aktor pertama: Total Control entitas Distributor Hapus Utama, `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net` (Pre-setup #21), password `Spectra.env.AC_SG_HAPUS_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun di langkah 26): Total Control entitas Distributor Changelog, `totalControlChangelog_automated_{namaCompany}@qwertysystem.net` (Pre-setup #42), password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite untuk akun UI yang dipakai suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (seed lewat Fixture BE di hook `before` pada entitas Distributor Hapus Utama, dihapus atau dipulihkan hook `after`; setiap nama bersuffix `{runId}-105`; Pre-setup #21 tidak diubah): `Hapus Warn A {runId}-105` (tanpa entitas; Group Role `Manage partner` pada `Joko Susilo`, user Pre-setup #21) untuk TC-AC-SG-147; `Hapus Bulk 4 {runId}-105` dan `Hapus Bulk 5 {runId}-105` (tanpa entitas) untuk TC-AC-SG-171.
- Data Pre-setup: riwayat Changelog Group seed entitas Distributor Changelog (Pre-setup #42) dibaca saja oleh TC-AC-SG-270.
- Failure injection (Pre-setup #38; disediakan tim FE): respons 5xx pada Delete Group, respons 5xx pada Bulk Delete, dan Download gagal. Tiap injeksi dinyalakan sebelum aksi pemicu dan dimatikan segera sesudahnya (S-09); hook `after` memastikan semua injeksi mati.
- Kemampuan teknis: Fixture BE (seeding, pemulihan, dan pembacaan penugasan Group Role tanpa melalui UI; disediakan tim FE/BE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-147: Gagal server saat Delete: tidak ada yang terhapus dan toast error

1. Ketik Search `{runId}-105`, tekan Enter
2. Aktifkan failure injection: respons 5xx pada Delete Group
3. Klik ikon `⋯` pada baris `Hapus Warn A {runId}-105` lalu `Delete`
4. Klik `[Delete]` pada dialog Delete
5. Verifikasi dialog Delete tertutup
6. Verifikasi toast error: "Error, failed to delete group."
7. Verifikasi `Hapus Warn A {runId}-105` tetap ada di tabel
8. Verifikasi penugasan Group Role `Manage partner` pada `Joko Susilo` untuk `Hapus Warn A {runId}-105` tidak terlepas (lewat Fixture BE)
9. Klik ikon `⋯` pada baris `Hapus Warn A {runId}-105`
10. Verifikasi item `Delete` masih enabled (retry manual dapat dilakukan)
11. Tutup Overlay Row Action dengan `Esc`
12. Nonaktifkan failure injection

### TC-AC-SG-171: Gagal server pada Bulk Delete: tidak ada yang terhapus

13. Tunggu toast lama hilang otomatis
14. Centang kolom Checkbox pada baris `Hapus Bulk 4 {runId}-105` dan `Hapus Bulk 5 {runId}-105`
15. Aktifkan failure injection: respons 5xx pada Bulk Delete
16. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
17. Klik `[Delete]` pada dialog
18. Verifikasi toast error: "Error, failed to delete group."
19. Verifikasi `Hapus Bulk 4 {runId}-105` dan `Hapus Bulk 5 {runId}-105` tetap ada (tidak ada yang terhapus)
20. Klik `Bulk Action` pada Bulk Actions Bar
21. Verifikasi item `Delete` masih enabled (retry manual dapat dilakukan)
22. Tutup menu `Bulk Action` dengan `Esc`
23. Nonaktifkan failure injection
24. Klik `Unselect All` pada Bulk Actions Bar
25. Tunggu toast lama hilang otomatis

### TC-AC-SG-270: Download Changelog gagal menampilkan toast error

26. Ganti akun: Logout, lalu login sebagai Total Control `Distributor Changelog`
27. Aktifkan failure injection: Download gagal
28. Klik ikon Changelog pada toolbar
29. Klik Download pada Modal "Changelog: Group"
30. Klik "Download as CSV"
31. Verifikasi toast error: "Error, failed to download Changelog-Group."
32. Nonaktifkan failure injection
33. Tutup Modal Changelog dengan `✕`

## Notes

- Kelas b (fault injection). Pada seluruh blok, pemicu kegagalan adalah objek uji; tidak ada TC kelas lain dalam spec ini.
- Langkah penghubung (S-03, tanpa `Verifikasi`): menyalakan dan mematikan failure injection, Search `{runId}-105` untuk menemukan baris target (langkah 1; R-16), menutup Overlay Row Action dan memulihkan seleksi dengan `Unselect All` (langkah 11, 22, dan 24; S-09), serta menunggu toast lama hilang agar toast error yang sama diasersi sebagai toast baru (langkah 13 dan 25; R-12).
- Langkah 26 adalah ganti akun eksplisit (S-07); sesi dipulihkan ke akun default spec di hook `after`.
- Langkah 9 sampai 11 dan 20 sampai 22 menjalankan klausa "retry manual dapat dilakukan" dari Expected TC-AC-SG-147 dan TC-AC-SG-171 sebagai `Verifikasi` state kontrol; TC tidak merinci cara retry.
- Temuan untuk QA:
  - TC-AC-SG-147 menyebut `Hapus Warn A` dan TC-AC-SG-171 menyebut `Hapus Bulk 4` dan `Hapus Bulk 5` dari Pre-setup #21; spec memakai node milik spec (S-06).
  - TC-AC-SG-147 Expected "tidak ada penugasan role yang terlepas" tidak menyebut cara memeriksanya; spec membacanya lewat Fixture BE.
  - TC-AC-SG-270 Expected tidak menyebut apakah Modal Changelog tetap terbuka setelah gagal; spec menutup modal sebagai langkah penghubung.
