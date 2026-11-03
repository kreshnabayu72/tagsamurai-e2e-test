---
id: TC-AC-LCS-E2E-123-changelog-parsial-berulang-dan-modified-by
title: "Isi Entri Changelog: Save Parsial Client Lifecycle, Save Berulang pada Field Sama, dan Format Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-474
  - TC-AC-LCS-475
  - TC-AC-LCS-476
coverage:
  web: automated
---

# Isi Entri Changelog: Save Parsial Client Lifecycle, Save Berulang pada Field Sama, dan Format Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: pembacaan total entri pada footer modal Changelog sebagai baseline N0 sebelum aksi (audit trail permanen; N tidak dapat diturunkan dari seeding, bagian 8b butir 10; baseline dicatat per tab). Precondition TC "Changelog tab kosong" tidak diasersi sebagai angka absolut: spec mengasersi selisih terhadap baseline N0 (S-12). Konfigurasi tab yang diubah spec dipulihkan ke default oleh hook `beforeEach` dan `after` suite.
- Kemampuan teknis: Fixture BE memulihkan ketujuh tab ke default antara TC-AC-LCS-475 dan TC-AC-LCS-476 (precondition TC-AC-LCS-476 meminta Free Plan Duration `365`).
- Data uji: Grace Period Duration `20`, Post-Purge Retention `800`; Free Plan Duration `365` ke `400` ke `500` (TC-AC-LCS-475) dan `365` ke `400` (TC-AC-LCS-476). Nama user aktor `Andi Wijaya`, tampil `Andi W`.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini).
- Data uji mengacu ke `Fixture.lifecycleSettings.<kunci>` dari `fixtures/lifecycle-settings.json` (nilai default tiap tab dan dataset Changelog).
- Konfigurasi Lifecycle Settings bersifat platform-wide dan Changelog bersifat permanen; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-474: Save dua dari sembilan field tab Client Lifecycle hanya mencatat dua entri

1. Klik tab Client Lifecycle
2. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
3. Catat total entri pada footer modal sebagai baseline N0 (tab Client Lifecycle)
4. Tutup modal dengan `[✕]`
5. Ubah Grace Period Duration dari `30` menjadi `20`
6. Ubah Post-Purge Retention dari `730` menjadi `800`
7. Klik `[Save]` dan tunggu toast sukses
8. Klik icon Changelog di pojok kanan atas panel tab Client Lifecycle
9. Verifikasi footer menunjukkan total entri baseline N0 ditambah 2 (tepat 2 entri baru)
10. Verifikasi entri baru tampil: Field `Grace Period Duration`, Old Value `30`, New Value `20`
11. Verifikasi entri baru tampil: Field `Post-Purge Retention`, Old Value `730`, New Value `800`
12. Verifikasi tidak ada entri baru untuk tujuh field Client Lifecycle yang lain
13. Tutup modal dengan `[✕]`

### TC-AC-LCS-475: Save kedua pada field yang sama tidak mengubah nilai entri log pertama

14. Klik tab Free Plan Settings
15. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
16. Catat total entri pada footer modal sebagai baseline N0 (tab Free Plan Settings)
17. Tutup modal dengan `[✕]`
18. Ubah Free Plan Duration dari `365` menjadi `400`
19. Klik `[Save]` dan tunggu toast sukses
20. Ubah Free Plan Duration dari `400` menjadi `500`
21. Klik `[Save]` dan tunggu toast sukses
22. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
23. Verifikasi footer menunjukkan total entri baseline N0 ditambah 2 (tepat 2 entri baru)
24. Verifikasi salah satu dari dua baris teratas: Field `Free Plan Duration`, Old Value `400`, New Value `500`
25. Verifikasi baris lainnya dari dua baris teratas: Field `Free Plan Duration`, Old Value `365`, New Value `400` (tidak ter-overwrite oleh Save kedua)

### TC-AC-LCS-476: Modified By pada Changelog menampilkan format singkat dan tooltip nama lengkap saat hover

26. Pulihkan ketujuh tab ke nilai default lewat Fixture BE
27. Muat ulang halaman dengan F5
28. Klik tab Free Plan Settings
29. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
30. Catat total entri pada footer modal sebagai baseline N0 (tab Free Plan Settings)
31. Tutup modal dengan `[✕]`
32. Ubah Free Plan Duration dari `365` menjadi `400`
33. Klik `[Save]` dan tunggu toast sukses
34. Klik icon Changelog di pojok kanan atas panel tab Free Plan Settings
35. Verifikasi footer menunjukkan total entri baseline N0 ditambah 1 (tepat 1 entri baru)
36. Verifikasi Modified By pada baris 1 tampil `Andi W` sebagai plain text (bukan badge)
37. Hover nilai Modified By pada baris 1
38. Verifikasi tooltip `Andi Wijaya` tampil

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: membaca baseline N0 lalu menutup modal (S-12) pada langkah 1 sampai 4, 14 sampai 17, dan 28 sampai 31 (baseline TC-AC-LCS-476 dibaca sesudah pemulihan dan muat ulang), menutup modal sebelum pindah tab, serta pemulihan ketujuh tab dan muat ulang halaman antara TC-AC-LCS-475 dan TC-AC-LCS-476 (S-09).
- Entri baru dicari di antara baris teratas urutan Newest First. Pada TC-AC-LCS-475 dua baris teratas dinilai sebagai himpunan tanpa urutan karena kedua Save dapat berada pada menit yang sama (S-14); pada TC-AC-LCS-474 dan TC-AC-LCS-476 urutan antar entri dengan cap waktu menit yang sama tidak diasersi karena TC tidak menyebutnya.
- Temuan untuk QA:
  - Expected TC (footer `1–N of N` dengan N sama dengan jumlah entri baru) mengandaikan Changelog tab kosong; Changelog bersifat permanen sehingga spec mengasersi total entri sebagai baseline N0 ditambah jumlah entri baru (S-12) dan memeriksa entri baru di baris teratas urutan Newest First.
  - Post Condition TC berupa nilai field tersimpan tidak punya langkah observasi sendiri di TC dan tidak diasersi; entri Changelog yang tercatat diasersi lewat Expected.
- Alasan di atas sekitar 35 langkah: ketiga blok TC (474, 475, 476) memakai modal Changelog yang sama pada tab Client Lifecycle, tiap blok membaca baseline N0 sendiri sesudah pemulihan, dan sebagian langkahnya adalah langkah penghubung baseline serta penutupan modal; memecahnya hanya mengulang pemulihan ketujuh tab dan muat ulang yang sama tanpa isolasi lebih, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
