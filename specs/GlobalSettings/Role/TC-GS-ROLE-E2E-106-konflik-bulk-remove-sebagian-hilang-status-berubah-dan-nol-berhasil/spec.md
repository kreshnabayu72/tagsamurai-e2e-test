---
id: TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil
title: "Konflik Antar Admin pada Bulk Remove: Sebagian Baris Sudah Dihapus, Status Total Control Berubah, dan Nol Baris Berhasil"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-134
  - TC-GS-ROLE-296
  - TC-GS-ROLE-299
coverage:
  web: automated
---

# Konflik Antar Admin pada Bulk Remove: Sebagian Baris Sudah Dihapus, Status Total Control Berubah, dan Nol Baris Berhasil

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua admin), kelas c. Suite `parallel: false`.
- Akun Sesi A (UI):

| Aktor | TC | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-134 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Hendra Wijaya (Manage user and role C/R/U/D) | TC-296, TC-299 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

- Akun Sesi B (pemicu): Eko Prasetyo (Total Control kedua, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Sesi B memakai sesi API (klien HTTP dengan kredensial Eko Prasetyo; cara memperoleh token disediakan tim FE) karena Sesi B hanya memicu perubahan state dan tidak ada asersi di Sesi B.
- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: satu konteks browser untuk Sesi A (ganti akun Ahmad Fauzi ke Hendra Wijaya lewat logout dan login); klien HTTP untuk Sesi B; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Data milik spec (dibuat lewat sesi API Eko Prasetyo di hook `before`; kemampuan seeding user dan Assign Role disediakan tim FE; nilai field wajib lain user seed disediakan tim FE). Semua user Active, Access Global Settings dicentang, tanpa access level:
  - `Target Bulk A {runId}-106` dan `Target Bulk B {runId}-106`: baris Manage hardware (TC-134).
  - `Pembanding {runId}-106`: baris Manage hardware, dipakai sebagai baris pembanding absence pada TC-134.
  - `Target Bulk C {runId}-106` dan `Target Bulk D {runId}-106`: baris Manage TAG (TC-296; setara Wawan Setiawan dan Nina Kartika).
- Data Pre-setup #18: `Dimas Anggara` dan `Gita Permata` (Active, Access Global Settings dicentang, tanpa access level) dengan Given baris Manage hardware di-assign lewat sesi API Ahmad Fauzi di hook `before` (TC-299). Hook `after` mencabut Total Control dan menghapus baris role keduanya sehingga kembali ke Pre-setup #18.
- Efek pemulihan Pre-setup yang tidak terpulihkan (S-06): `Dimas Anggara` dan `Gita Permata` di-assign baris role, di-assign Total Control oleh Sesi B, lalu dibersihkan di hook `after`; Modified By dan Last Updated kedua user berubah dan tidak dapat dipulihkan ke nilai awal, serta entri Changelog (Assign, Remove), Activity Log, dan System Log bersifat immutable dan tidak dihapus. Karena itu asersi log atas kedua user tidak memakai nilai absolut: jumlah entri Remove memakai selisih terhadap baseline `B-DA-RM` dan `B-GP-RM` (S-12).
- Baseline (dicatat di hook `before` sesudah Given dan sebelum permintaan pertama Sesi B, S-12; jumlah entri dibaca dari UI Changelog Detail "Manage hardware" lewat Search nama user): jumlah entri Remove untuk `Dimas Anggara` sebagai `B-DA-RM` dan untuk `Gita Permata` sebagai `B-GP-RM`. Asersi memakai selisih terhadap baseline karena audit trail permanen dan nama Pre-setup literal dipakai ulang antar run.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): cabut Total Control `Target Bulk C {runId}-106` bila ada, hapus baris role semua user seed, lalu hapus semua user seed; pulihkan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data milik spec di atas.

## Test Steps

### TC-GS-ROLE-134: Bulk Remove saat sebagian baris sudah dihapus admin lain

1. [Sesi A] Buka Detail "Manage hardware"
2. [Sesi A] Ketik Search `{runId}-106`, tekan Enter
3. [Sesi A] Centang baris `Target Bulk A {runId}-106`
4. [Sesi A] Centang baris `Target Bulk B {runId}-106`
5. [Sesi B] Remove baris Manage hardware `Target Bulk A {runId}-106` lewat sesi API hingga perubahan tersimpan
6. [Sesi A] Klik `Bulk Action`
7. [Sesi A] Klik `Remove`
8. [Sesi A] Klik `[Remove]` pada dialog
9. [Sesi A] Verifikasi toast sukses `Success, user has been removed.` tampil
10. [Sesi A] Verifikasi toast tidak memuat `Some items were skipped.` (bukan toast parsial)
11. [Sesi A] Verifikasi baris `Pembanding {runId}-106` tampil di Detail "Manage hardware"
12. [Sesi A] Verifikasi baris `Target Bulk A {runId}-106` dan `Target Bulk B {runId}-106` tidak ada di Detail "Manage hardware"
13. [Sesi A] Klik `Changelog`
14. [Sesi A] Ketik Search `Target Bulk A {runId}-106`, tekan Enter
15. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Bulk A {runId}-106` (entri dari Sesi B)
16. [Sesi A] Verifikasi Modified By entri Remove `Target Bulk A {runId}-106` adalah `Eko P`
17. [Sesi A] Ganti isi kotak search dengan `Target Bulk B {runId}-106`, tekan Enter
18. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Bulk B {runId}-106` (entri dari Sesi A)
19. [Sesi A] Verifikasi Modified By entri Remove `Target Bulk B {runId}-106` adalah `Ahmad F`
20. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-296: Bulk Remove saat status Total Control target berubah antara render dan submit

21. [Sesi A] Ganti akun: logout, lalu login sebagai Hendra Wijaya
22. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage TAG"
23. [Sesi A] Ketik Search `{runId}-106`, tekan Enter
24. [Sesi A] Centang baris `Target Bulk C {runId}-106`
25. [Sesi A] Centang baris `Target Bulk D {runId}-106`
26. [Sesi B] Tetapkan Total Control ke `Target Bulk C {runId}-106` lewat sesi API hingga perubahan tersimpan
27. [Sesi A] Klik `Bulk Action`
28. [Sesi A] Klik `Remove`
29. [Sesi A] Klik `[Remove]` pada dialog
30. [Sesi A] Verifikasi toast sukses parsial `Success, user has been removed. Some items were skipped.` tampil
31. [Sesi A] Verifikasi baris `Target Bulk D {runId}-106` terhapus dari Detail "Manage TAG"
32. [Sesi A] Verifikasi baris `Target Bulk C {runId}-106` tetap ada di Detail "Manage TAG" (ditolak per baris, dihitung gagal)
33. [Sesi A] Verifikasi Bulk Action Bar tertutup
34. [Sesi A] Verifikasi seleksi di-reset ke 0 (tidak ada baris tercentang)
35. [Sesi A] Verifikasi tidak ada dialog konflik
36. [Sesi A] Klik `Changelog`
37. [Sesi A] Ketik Search `Target Bulk D {runId}-106`, tekan Enter
38. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Bulk D {runId}-106` (entri dari Sesi A)
39. [Sesi A] Ganti isi kotak search dengan `Target Bulk C {runId}-106`, tekan Enter
40. [Sesi A] Verifikasi Changelog memuat entri Assign untuk `Target Bulk C {runId}-106` (entri seeding)
41. [Sesi A] Verifikasi Changelog tidak memuat entri Remove untuk `Target Bulk C {runId}-106`
42. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-299: Bulk Remove saat semua baris ditolak per baris (0 berhasil)

43. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage hardware"
44. [Sesi A] Ketik Search `Dimas Anggara`, tekan Enter
45. [Sesi A] Centang baris `Dimas Anggara`
46. [Sesi A] Ganti isi kotak search dengan `Gita Permata`, tekan Enter
47. [Sesi A] Centang baris `Gita Permata`
48. [Sesi B] Tetapkan Total Control ke `Dimas Anggara` lewat sesi API hingga perubahan tersimpan
49. [Sesi B] Tetapkan Total Control ke `Gita Permata` lewat sesi API hingga perubahan tersimpan
50. [Sesi A] Klik `Bulk Action`
51. [Sesi A] Klik `Remove`
52. [Sesi A] Klik `[Remove]` pada dialog
53. [Sesi A] Verifikasi dialog konfirmasi tertutup
54. [Sesi A] Verifikasi toast error `Error, failed to remove user.` tampil
55. [Sesi A] Verifikasi tidak ada toast sukses
56. [Sesi A] Verifikasi tidak ada toast sukses parsial
57. [Sesi A] Verifikasi tidak ada dialog konflik
58. [Sesi A] Ganti isi kotak search dengan `Dimas Anggara`, tekan Enter
59. [Sesi A] Verifikasi baris `Dimas Anggara` tetap ada di Detail "Manage hardware"
60. [Sesi A] Verifikasi seleksi `Dimas Anggara` dipertahankan
61. [Sesi A] Ganti isi kotak search dengan `Gita Permata`, tekan Enter
62. [Sesi A] Verifikasi baris `Gita Permata` tetap ada di Detail "Manage hardware"
63. [Sesi A] Verifikasi seleksi `Gita Permata` dipertahankan
64. [Sesi A] Verifikasi Bulk Action Bar tetap tampil
65. [Sesi A] Klik `Changelog`
66. [Sesi A] Ketik Search `Dimas Anggara`, tekan Enter
67. [Sesi A] Verifikasi Changelog memuat entri Assign untuk `Dimas Anggara` (entri Given)
68. [Sesi A] Verifikasi jumlah entri Remove untuk `Dimas Anggara` di Changelog Detail "Manage hardware" sama dengan baseline `B-DA-RM` (selisih +0)
69. [Sesi A] Ganti isi kotak search dengan `Gita Permata`, tekan Enter
70. [Sesi A] Verifikasi Changelog memuat entri Assign untuk `Gita Permata` (entri Given)
71. [Sesi A] Verifikasi jumlah entri Remove untuk `Gita Permata` di Changelog Detail "Manage hardware" sama dengan baseline `B-GP-RM` (selisih +0)
72. [Sesi A] Tutup modal Changelog

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua admin), prinsip 13c bagian 3 konvensi; spec konflik antar admin lain ada di `TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus`, `TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control`, dan `TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda`.
- Sesi B adalah sesi API pemicu: hanya memicu perubahan state dan tidak ada asersi di Sesi B. Objek asersi adalah perilaku Sesi A sesudah perubahan Sesi B.
- Spec melewati sekitar 35 langkah (72 langkah) karena ketiga blok satu kelas harness dan berdiri sendiri: tiap blok punya user target, pemicu Sesi B, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah blok baca-log berpola (buka Changelog, cari entri, `Verifikasi`) dan pemecahan Expected per klausa.
- Urutan TC sumber (134, 296, 299) dipertahankan; akun Sesi A berganti dari Ahmad Fauzi ke Hendra Wijaya satu kali (langkah 21).
- Search target sebelum centang baris ditulis sebagai langkah penghubung (R-16) dan ditempatkan sebelum pemicu Sesi B supaya tampilan Sesi A tetap sebelum perubahan Sesi B; Search diperlukan karena daftar user bisa lebih dari satu halaman (langkah 2, 23, 44, 46, 58, dan 61). Langkah 2 dan 23 memakai `{runId}-106` yang memuat semua user seed pada surface itu, termasuk baris pembanding. Langkah 58 dan 61 mengganti isi Search per nama supaya baris `Dimas Anggara` (langkah 59) dan `Gita Permata` (langkah 62) tampil.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Detail, Changelog, dan Search (langkah 1, 13, 14, 17, 22, 36, 37, 39, 43, 65, 66, 69), menutup modal Changelog (langkah 20, 42, 72), dan ganti akun (langkah 21).
- Absence baris (langkah 12) didahului baris pembanding (langkah 11) dan toast sukses (langkah 9); absence entri Remove (langkah 41, 68, 71) didahului `Verifikasi` entri Assign untuk user yang sama pada Changelog yang sama (langkah 40, 67, 70; bagian 8b butir 2).
- TC-299 Expected c ("reset ke 0 hanya untuk sukses penuh atau parsial") adalah alasan seleksi dipertahankan; yang diasersi adalah seleksi dipertahankan (langkah 60 dan 63) dan Bulk Action Bar tetap tampil (langkah 64).
- Langkah penghubung (R-16, bukan dari TC sumber): pada TC-GS-ROLE-299 baris tetap ada dan seleksi diasersi per nama lewat Search `Dimas Anggara` (langkah 58) dan `Gita Permata` (langkah 61) karena daftar bisa lebih dari satu halaman; seleksi dipertahankan (Expected c) diasersi per user pada langkah 60 dan 63, mengandalkan seleksi yang bertahan saat isi Search berubah.
- Temuan untuk QA:
  - TC-134 tidak menyebut baris yang dipilih ("2 baris") dan akun Sesi A pada TC-134 hanya Ahmad Fauzi dengan Eko Prasetyo di Sesi B; spec memakai user seed milik spec.
  - TC-296 memakai Wawan Setiawan dan Nina Kartika dengan baris Manage TAG (Dinamis #5); spec memakai user seed milik spec supaya Pre-setup bersama tidak diubah (S-06).
  - TC-299 Post Condition ("Dimas Anggara dan Gita Permata tetap Total Control dan memiliki baris Manage hardware") untuk bagian "tetap Total Control" tidak punya langkah observasi di TC dan tidak diasersi; bagian baris Manage hardware punya padanan di Expected b.
  - TC-299 mencentang dua user yang berbeda nama; spec mencari tiap nama (langkah 44 dan 46) dan mengandalkan seleksi yang bertahan saat isi Search berubah (TC-GS-ROLE-136 hanya menyebut seleksi bertahan saat Search dikosongkan).
  - TC-134 Expected c tidak menyebut Modified By; spec mengasersi Modified By `Eko P` dan `Ahmad F` untuk membedakan entri sesi B dan sesi A (format `[First Name] [Last Initial]`).
  - TC-296 Expected e ("Changelog hanya memuat entry Remove Nina Kartika") tidak menyebut surface; spec memakai Changelog Detail "Manage TAG".
