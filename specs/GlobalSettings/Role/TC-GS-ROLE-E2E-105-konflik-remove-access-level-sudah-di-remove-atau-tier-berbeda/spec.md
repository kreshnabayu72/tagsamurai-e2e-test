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
- Efek pemulihan Pre-setup yang tidak terpulihkan (S-06): `Joko Prasetyo` dan `Rizal Hakim` di-assign access level, di-remove atau di-upgrade oleh Sesi B, lalu dibersihkan di hook `after`; Modified By dan Last Updated kedua user berubah dan tidak dapat dipulihkan ke nilai awal, serta entri Changelog (Assign, Remove), Activity Log, dan System Log bersifat immutable dan tidak dihapus. Karena itu asersi log atas kedua user tidak memakai nilai absolut: semua jumlah entri memakai selisih terhadap baseline `B-JP-RM`, `B-RH-AS`, `B-RH-RM-TC`, dan `B-RH-RM-RO` (S-12).
- Baseline (dicatat di hook `before` sesudah Given dan sebelum permintaan pertama Sesi B, S-12; jumlah entri dibaca dari UI Changelog lewat Search nama user): jumlah entri Remove untuk `Joko Prasetyo` di Changelog Tab Total Control sebagai `B-JP-RM`; jumlah entri Assign untuk `Rizal Hakim` di Changelog Tab Total Control sebagai `B-RH-AS`; jumlah entri Remove untuk `Rizal Hakim` di Changelog Tab Total Control sebagai `B-RH-RM-TC`; jumlah entri Remove untuk `Rizal Hakim` di Changelog Tab Read Only sebagai `B-RH-RM-RO`. Asersi memakai selisih terhadap baseline karena audit trail permanen dan nama Pre-setup literal dipakai ulang antar run.
- Data Pre-setup sebagai pembanding (hanya dibaca): `Ahmad Fauzi` di Tab Total Control dan `Rina Putri` di Tab Read Only.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-275: Remove access level saat target sudah di-Remove admin lain sejak render

1. [Sesi A] Klik Tab `Total Control`
2. [Sesi A] Ketik Search `Joko Prasetyo`, tekan Enter
3. [Sesi B] Remove Total Control `Joko Prasetyo` lewat sesi API hingga perubahan tersimpan
4. [Sesi A] Klik `(⋯)` pada baris `Joko Prasetyo`
5. [Sesi A] Klik `Remove`
6. [Sesi A] Klik `[Remove]` pada dialog
7. [Sesi A] Verifikasi toast netral `This access level is no longer available.` tampil
8. [Sesi A] Verifikasi tidak ada toast sukses
9. [Sesi A] Verifikasi tidak ada dialog
10. [Sesi A] Ketik Search `Ahmad Fauzi`, tekan Enter
11. [Sesi A] Verifikasi baris `Ahmad Fauzi` tampil di Tab Total Control yang di-refresh
12. [Sesi A] Ketik Search `Joko Prasetyo`, tekan Enter
13. [Sesi A] Verifikasi baris `Joko Prasetyo` tidak ada di Tab Total Control
14. [Sesi A] Klik `Changelog`
15. [Sesi A] Ketik Search `Joko Prasetyo`, tekan Enter
16. [Sesi A] Verifikasi jumlah entri Remove untuk `Joko Prasetyo` di Changelog Tab Total Control bertambah tepat 1 dari baseline `B-JP-RM` (selisih +1; entri dari Sesi B, tidak ada entri Remove kedua)
17. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-298: Remove access level saat tier target berbeda dari tab yang dirender

18. [Sesi A] Klik Tab `Read Only`
19. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
20. [Sesi A] Verifikasi baris `Rizal Hakim` tampil di Tab Read Only
21. [Sesi B] Tetapkan Total Control ke `Rizal Hakim` (upgrade Read Only ke Total Control) lewat sesi API hingga perubahan tersimpan
22. [Sesi A] Klik `(⋯)` pada baris `Rizal Hakim`
23. [Sesi A] Klik `Remove`
24. [Sesi A] Klik `[Remove]` pada dialog `Remove Read Only`
25. [Sesi A] Verifikasi toast netral `This access level is no longer available.` tampil
26. [Sesi A] Verifikasi tidak ada toast sukses
27. [Sesi A] Verifikasi tidak ada dialog konflik
28. [Sesi A] Ketik Search `Rina Putri`, tekan Enter
29. [Sesi A] Verifikasi baris `Rina Putri` tampil di Tab Read Only yang di-refresh
30. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
31. [Sesi A] Verifikasi baris `Rizal Hakim` tidak ada di Tab Read Only
32. [Sesi A] Klik Tab `Total Control`
33. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
34. [Sesi A] Verifikasi baris `Rizal Hakim` tampil di Tab Total Control (access level tidak dicabut)
35. [Sesi A] Buka Detail "Manage TAG"
36. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
37. [Sesi A] Verifikasi baris `Rizal Hakim` tampil di Detail "Manage TAG" (baris role tidak dihapus)
38. [Sesi A] Buka Tab `Total Control`
39. [Sesi A] Klik `Changelog`
40. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
41. [Sesi A] Verifikasi jumlah entri Assign untuk `Rizal Hakim` di Changelog Tab Total Control bertambah tepat 1 dari baseline `B-RH-AS` (selisih +1; entri upgrade dari Sesi B)
42. [Sesi A] Verifikasi entri Assign baru untuk `Rizal Hakim` di Changelog Tab Total Control memiliki Old `Read Only` dan New `Total Control` (entri upgrade dari Sesi B)
43. [Sesi A] Verifikasi jumlah entri Remove untuk `Rizal Hakim` di Changelog Tab Total Control sama dengan baseline `B-RH-RM-TC` (selisih +0)
44. [Sesi A] Tutup modal Changelog
45. [Sesi A] Klik Tab `Read Only`
46. [Sesi A] Klik `Changelog`
47. [Sesi A] Ketik Search `Rizal Hakim`, tekan Enter
48. [Sesi A] Verifikasi Changelog Tab Read Only memuat entri Assign untuk `Rizal Hakim` (entri Given)
49. [Sesi A] Verifikasi jumlah entri Remove untuk `Rizal Hakim` di Changelog Tab Read Only sama dengan baseline `B-RH-RM-RO` (selisih +0)
50. [Sesi A] Tutup modal Changelog

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua admin), prinsip 13c bagian 3 konvensi; spec konflik antar admin lain ada di `TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus`, `TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control`, dan `TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil`.
- Sesi B adalah sesi API pemicu: hanya memicu perubahan state dan tidak ada asersi di Sesi B. Objek asersi adalah perilaku Sesi A sesudah perubahan Sesi B.
- Spec melewati sekitar 35 langkah (50 langkah) karena kedua blok satu kelas harness dan berdiri sendiri (user target, pemicu Sesi B, dan asersi sendiri) serta TC-298 memuat enam butir Expected yang masing-masing butuh surface berbeda (Tab Read Only, Tab Total Control, Detail, dan dua Changelog); kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah TC-298 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi`).
- Search target sebelum aksi baris ditulis sebagai langkah penghubung (R-16) dan ditempatkan sebelum pemicu Sesi B supaya tampilan Sesi A tetap sebelum perubahan Sesi B; Search diperlukan karena daftar user bisa lebih dari satu halaman. Langkah 2 dan 19; langkah 10 dan 28 mengganti isi Search dengan nama pembanding (menggantikan `(←)`) supaya baris pembanding `Ahmad Fauzi` (langkah 11) dan `Rina Putri` (langkah 29) tampil.
- Langkah penghubung (aksi tanpa `Verifikasi`): memilih tab dan membuka Detail dan Changelog (langkah 1, 14, 18, 32, 35, 38, 39, 45, 46), Search (langkah 15, 40, 47), dan menutup modal Changelog (langkah 17, 44, 50).
- Absence `Joko Prasetyo` dan `Rizal Hakim` di tab (langkah 13 dan 31) didahului baris pembanding pada tab yang sama (langkah 11 dan 29); absence entri Remove (langkah 43 dan 49) didahului `Verifikasi` entri Assign pada Changelog yang sama (langkah 41 dan 48; bagian 8b butir 2). Untuk Tab Total Control, "hanya memuat entry Assign upgrade" diasersi sebagai selisih +1 entri Assign untuk `Rizal Hakim` terhadap baseline `B-RH-AS` (langkah 41).
- TC-298 Expected c ("Rizal Hakim tetap Total Control") dan Expected d (baris role tetap ada) diasersi di langkah 34 dan 37 sebelum Changelog.
- Langkah penghubung (R-16, bukan dari TC sumber): Search `Rizal Hakim` (langkah 33 dan 36) sebelum `Verifikasi` baris tampil di Tab Total Control dan Detail "Manage TAG" karena daftar user bisa lebih dari satu halaman.
- Langkah penghubung (R-16, bukan dari TC sumber): Search `Ahmad Fauzi` (langkah 10) dan `Rina Putri` (langkah 28) menggantikan `(←)` sebelum `Verifikasi` baris pembanding, karena tab berpagination; Search `Joko Prasetyo` (langkah 12) dan `Rizal Hakim` (langkah 30) mengganti isi Search sebelum absence. Absence tetap bermakna karena baris pembanding pada tab yang sama sudah terverifikasi pada langkah sebelumnya (langkah 11 dan 29).
- Temuan untuk QA:
  - TC-275 dan TC-298 menyebut "tidak ada entry Remove kedua" dan "tidak ada entry Remove dari sesi A" tanpa metode pembacaan; spec memakai Search nama user di Changelog.
  - TC-298 Given menyebut Rizal Hakim memiliki "baris keenam role hasil bulk-write" sedangkan Pre-setup #18 menyatakan "tanpa baris role"; spec menganggap Assign Read Only (Given) menulis baris role.
  - TC-298 Expected f tidak menyebut apakah upgrade menambah entri di Changelog Tab Read Only; spec hanya mengasersi tidak ada entri Remove di Changelog Tab Read Only.
  - TC-298 Post Condition ("Rizal Hakim tetap Total Control") punya padanan di Expected c.
