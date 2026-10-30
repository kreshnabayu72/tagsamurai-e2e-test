---
id: TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda
title: "Konflik Antar Admin pada Remove Access Level: Target Sudah di-Remove atau Tier Berbeda dari Tab yang Dirender"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-275
  - TC-GS-ROLE-298
coverage:
  web: automated
---

# Konflik Antar Admin pada Remove Access Level: Target Sudah di-Remove atau Tier Berbeda dari Tab yang Dirender

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua admin), kelas c. Suite `parallel: false`.
- Akun Sesi A (UI): Ahmad Fauzi (Total Control, akun hook `before`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (pemicu): Eko Prasetyo (Total Control kedua, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Sesi B memakai sesi API (klien HTTP dengan kredensial Eko Prasetyo; cara memperoleh token disediakan tim FE) karena Sesi B hanya memicu perubahan state dan tidak ada asersi di Sesi B. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: satu konteks browser untuk Sesi A; klien HTTP untuk Sesi B; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Data Pre-setup #18 (kandidat fixture sekali pakai; Active, Access Global Settings dicentang, tanpa access level dan tanpa baris role) yang di-Given di hook `before` lewat sesi API Ahmad Fauzi: `Joko Prasetyo` di-assign Total Control (TC-275) dan `Rizal Hakim` di-assign Read Only (TC-298; Assign Read Only menulis baris role pada keenam role). Hook `after` mencabut access level dan menghapus baris role kedua user bila masih ada sehingga keduanya kembali ke Pre-setup #18.
- Data Pre-setup sebagai pembanding (hanya dibaca): `Ahmad Fauzi` di Tab Total Control dan `Rina Putri` di Tab Read Only.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-275: Remove access level saat target sudah di-Remove admin lain sejak render

1. [Sesi A] Klik Tab `Total Control`
2. [Sesi B] Remove Total Control `Joko Prasetyo` lewat sesi API
3. [Sesi A] Klik `(⋯)` pada baris `Joko Prasetyo`
4. [Sesi A] Klik `Remove`
5. [Sesi A] Klik `[Remove]` pada dialog
6. [Sesi A] Verifikasi toast netral `This access level is no longer available.` tampil
7. [Sesi A] Verifikasi tidak ada toast sukses
8. [Sesi A] Verifikasi tidak ada dialog
9. [Sesi A] Verifikasi baris `Ahmad Fauzi` tampil di Tab Total Control yang di-refresh
10. [Sesi A] Verifikasi baris `Joko Prasetyo` tidak ada di Tab Total Control
11. [Sesi A] Klik `Changelog`
12. [Sesi A] Ketik Search `Joko Prasetyo`, tekan Enter
13. [Sesi A] Verifikasi Changelog Tab Total Control memuat tepat 1 entri Remove untuk `Joko Prasetyo` (entri dari Sesi B; tidak ada entri Remove kedua)
14. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-298: Remove access level saat tier target berbeda dari tab yang dirender

15. [Sesi A] Klik Tab `Read Only`
16. [Sesi A] Verifikasi baris `Rizal Hakim` tampil di Tab Read Only
17. [Sesi B] Tetapkan Total Control ke `Rizal Hakim` lewat sesi API (upgrade Read Only ke Total Control)
18. [Sesi A] Klik `(⋯)` pada baris `Rizal Hakim`
19. [Sesi A] Klik `Remove`
20. [Sesi A] Klik `[Remove]` pada dialog `Remove Read Only`
21. [Sesi A] Verifikasi toast netral `This access level is no longer available.` tampil
22. [Sesi A] Verifikasi tidak ada toast sukses
23. [Sesi A] Verifikasi tidak ada dialog konflik
24. [Sesi A] Verifikasi baris `Rina Putri` tampil di Tab Read Only yang di-refresh
25. [Sesi A] Verifikasi baris `Rizal Hakim` tidak ada di Tab Read Only
26. [Sesi A] Klik Tab `Total Control`
27. [Sesi A] Verifikasi baris `Rizal Hakim` tampil di Tab Total Control (access level tidak dicabut)
28. [Sesi A] Buka Detail "Manage TAG"
29. [Sesi A] Verifikasi baris `Rizal Hakim` tampil di Detail "Manage TAG" (baris role tidak dihapus)
30. [Sesi A] Buka Tab `Total Control`
31. [Sesi A] Klik `Changelog`
32. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
33. [Sesi A] Verifikasi Changelog Tab Total Control memuat tepat 1 entri Assign untuk `Rizal Hakim` dengan Old `Read Only` dan New `Total Control` (entri upgrade dari Sesi B)
34. [Sesi A] Verifikasi Changelog Tab Total Control tidak memuat entri Remove untuk `Rizal Hakim`
35. [Sesi A] Tutup modal Changelog
36. [Sesi A] Klik Tab `Read Only`
37. [Sesi A] Klik `Changelog`
38. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
39. [Sesi A] Verifikasi Changelog Tab Read Only memuat entri Assign untuk `Rizal Hakim` (entri Given)
40. [Sesi A] Verifikasi Changelog Tab Read Only tidak memuat entri Remove untuk `Rizal Hakim`
41. [Sesi A] Tutup modal Changelog

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua admin), prinsip 13c bagian 3 konvensi; spec konflik antar admin lain ada di `TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus`, `TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control`, dan `TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil`.
- Sesi B memakai sesi API karena hanya memicu perubahan state dan tidak ada asersi di Sesi B (P-2, `[KEPUTUSAN 2026-10-21]`). Objek asersi adalah perilaku Sesi A sesudah perubahan Sesi B.
- Spec melewati sekitar 35 langkah (41 langkah) karena kedua blok satu kelas harness dan berdiri sendiri (user target, pemicu Sesi B, dan asersi sendiri) serta TC-298 memuat enam butir Expected yang masing-masing butuh surface berbeda (Tab Read Only, Tab Total Control, Detail, dan dua Changelog); kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah TC-298 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi`).
- Langkah penghubung (aksi tanpa `Verifikasi`): memilih tab dan membuka Detail dan Changelog (langkah 1, 11, 15, 26, 28, 30, 31, 36, 37), Search (langkah 12, 32, 38), dan menutup modal Changelog (langkah 14, 35, 41).
- Absence `Joko Prasetyo` dan `Rizal Hakim` di tab (langkah 10 dan 25) didahului baris pembanding pada tab yang sama (langkah 9 dan 24); absence entri Remove (langkah 34 dan 40) didahului `Verifikasi` entri Assign pada Changelog yang sama (langkah 33 dan 39; bagian 8b butir 2). Untuk Tab Total Control, "hanya memuat entry Assign upgrade" diasersi sebagai tepat 1 entri Assign untuk `Rizal Hakim`.
- TC-298 Expected c ("Rizal Hakim tetap Total Control") dan Expected d (baris role tetap ada) diasersi di langkah 27 dan 29 sebelum Changelog.
- Temuan untuk QA:
  - TC-275 dan TC-298 menyebut "tidak ada entry Remove kedua" dan "tidak ada entry Remove dari sesi A" tanpa metode pembacaan; spec memakai Search nama user di Changelog.
  - TC-298 Given menyebut Rizal Hakim memiliki "baris keenam role hasil bulk-write" sedangkan Pre-setup #18 menyatakan "tanpa baris role"; spec menganggap Assign Read Only (Given) menulis baris role.
  - TC-298 Expected f tidak menyebut apakah upgrade menambah entri di Changelog Tab Read Only; spec hanya mengasersi tidak ada entri Remove di Changelog Tab Read Only.
  - TC-298 Post Condition ("Rizal Hakim tetap Total Control") punya padanan di Expected c.
