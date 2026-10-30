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
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): cabut Total Control `Target Bulk C {runId}-106` bila ada, hapus baris role semua user seed, lalu hapus semua user seed; pulihkan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data milik spec di atas.

## Test Steps

### TC-GS-ROLE-134: Bulk Remove saat sebagian baris sudah dihapus admin lain

1. [Sesi A] Buka Detail "Manage hardware"
2. [Sesi A] Centang baris `Target Bulk A {runId}-106`
3. [Sesi A] Centang baris `Target Bulk B {runId}-106`
4. [Sesi B] Remove baris Manage hardware `Target Bulk A {runId}-106` lewat sesi API
5. [Sesi A] Klik `Bulk Action`
6. [Sesi A] Klik `Remove`
7. [Sesi A] Klik `[Remove]` pada dialog
8. [Sesi A] Verifikasi toast sukses `Success, user has been removed.` tampil
9. [Sesi A] Verifikasi toast tidak memuat `Some items were skipped.` (bukan toast parsial)
10. [Sesi A] Verifikasi baris `Pembanding {runId}-106` tampil di Detail "Manage hardware"
11. [Sesi A] Verifikasi baris `Target Bulk A {runId}-106` dan `Target Bulk B {runId}-106` tidak ada di Detail "Manage hardware"
12. [Sesi A] Klik `Changelog`
13. [Sesi A] Ketik Search `Target Bulk A {runId}-106`, tekan Enter
14. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Bulk A {runId}-106` dengan Modified By `Eko P` (entri dari Sesi B)
15. [Sesi A] Ganti isi kotak search dengan `Target Bulk B {runId}-106`, tekan Enter
16. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Bulk B {runId}-106` dengan Modified By `Ahmad F` (entri dari Sesi A)
17. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-296: Bulk Remove saat status Total Control target berubah antara render dan submit

18. [Sesi A] Ganti akun: logout, lalu login sebagai Hendra Wijaya
19. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage TAG"
20. [Sesi A] Centang baris `Target Bulk C {runId}-106`
21. [Sesi A] Centang baris `Target Bulk D {runId}-106`
22. [Sesi B] Tetapkan Total Control ke `Target Bulk C {runId}-106` lewat sesi API
23. [Sesi A] Klik `Bulk Action`
24. [Sesi A] Klik `Remove`
25. [Sesi A] Klik `[Remove]` pada dialog
26. [Sesi A] Verifikasi toast sukses parsial `Success, user has been removed. Some items were skipped.` tampil
27. [Sesi A] Verifikasi baris `Target Bulk D {runId}-106` terhapus dari Detail "Manage TAG"
28. [Sesi A] Verifikasi baris `Target Bulk C {runId}-106` tetap ada di Detail "Manage TAG" (ditolak per baris, dihitung gagal)
29. [Sesi A] Verifikasi Bulk Action Bar tertutup
30. [Sesi A] Verifikasi seleksi di-reset ke 0 (tidak ada baris tercentang)
31. [Sesi A] Verifikasi tidak ada dialog konflik
32. [Sesi A] Klik `Changelog`
33. [Sesi A] Ketik Search `Target Bulk D {runId}-106`, tekan Enter
34. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Bulk D {runId}-106` (entri dari Sesi A)
35. [Sesi A] Ganti isi kotak search dengan `Target Bulk C {runId}-106`, tekan Enter
36. [Sesi A] Verifikasi Changelog memuat entri Assign untuk `Target Bulk C {runId}-106` (entri seeding)
37. [Sesi A] Verifikasi Changelog tidak memuat entri Remove untuk `Target Bulk C {runId}-106`
38. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-299: Bulk Remove saat semua baris ditolak per baris (0 berhasil)

39. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage hardware"
40. [Sesi A] Centang baris `Dimas Anggara`
41. [Sesi A] Centang baris `Gita Permata`
42. [Sesi B] Tetapkan Total Control ke `Dimas Anggara` lewat sesi API
43. [Sesi B] Tetapkan Total Control ke `Gita Permata` lewat sesi API
44. [Sesi A] Klik `Bulk Action`
45. [Sesi A] Klik `Remove`
46. [Sesi A] Klik `[Remove]` pada dialog
47. [Sesi A] Verifikasi dialog konfirmasi tertutup
48. [Sesi A] Verifikasi toast error `Error, failed to remove user.` tampil
49. [Sesi A] Verifikasi tidak ada toast sukses
50. [Sesi A] Verifikasi tidak ada toast sukses parsial
51. [Sesi A] Verifikasi tidak ada dialog konflik
52. [Sesi A] Verifikasi baris `Dimas Anggara` dan `Gita Permata` tetap ada di Detail "Manage hardware"
53. [Sesi A] Verifikasi Bulk Action Bar tetap tampil
54. [Sesi A] Verifikasi seleksi `Dimas Anggara` dan `Gita Permata` dipertahankan
55. [Sesi A] Klik `Changelog`
56. [Sesi A] Ketik Search `Dimas Anggara`, tekan Enter
57. [Sesi A] Verifikasi Changelog memuat entri Assign untuk `Dimas Anggara` (entri Given)
58. [Sesi A] Verifikasi Changelog tidak memuat entri Remove untuk `Dimas Anggara`
59. [Sesi A] Ganti isi kotak search dengan `Gita Permata`, tekan Enter
60. [Sesi A] Verifikasi Changelog memuat entri Assign untuk `Gita Permata` (entri Given)
61. [Sesi A] Verifikasi Changelog tidak memuat entri Remove untuk `Gita Permata`
62. [Sesi A] Tutup modal Changelog

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua admin), prinsip 13c bagian 3 konvensi; spec konflik antar admin lain ada di `TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus`, `TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control`, dan `TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda`.
- Sesi B memakai sesi API karena hanya memicu perubahan state dan tidak ada asersi di Sesi B (P-2, `[KEPUTUSAN 2026-10-21]`). Objek asersi adalah perilaku Sesi A sesudah perubahan Sesi B.
- Spec melewati sekitar 35 langkah (62 langkah) karena ketiga blok satu kelas harness dan berdiri sendiri: tiap blok punya user target, pemicu Sesi B, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah blok baca-log berpola (buka Changelog, cari entri, `Verifikasi`) dan pemecahan Expected per klausa.
- Urutan TC sumber (134, 296, 299) dipertahankan; akun Sesi A berganti dari Ahmad Fauzi ke Hendra Wijaya satu kali (langkah 18).
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Detail, Changelog, dan Search (langkah 1, 12, 13, 15, 19, 32, 33, 35, 39, 55, 56, 59), menutup modal Changelog (langkah 17, 38, 62), dan ganti akun (langkah 18).
- Absence baris (langkah 11) didahului baris pembanding (langkah 10) dan toast sukses (langkah 8); absence entri Remove (langkah 37, 58, 61) didahului `Verifikasi` entri Assign untuk user yang sama pada Changelog yang sama (langkah 36, 57, 60; bagian 8b butir 2).
- TC-299 Expected c ("reset ke 0 hanya untuk sukses penuh atau parsial") adalah alasan seleksi dipertahankan; yang diasersi adalah seleksi dipertahankan (langkah 54) dan Bulk Action Bar tetap tampil (langkah 53).
- Temuan untuk QA:
  - TC-134 tidak menyebut baris yang dipilih ("2 baris") dan akun Sesi A pada TC-134 hanya Ahmad Fauzi dengan Eko Prasetyo di Sesi B; spec memakai user seed milik spec.
  - TC-296 memakai Wawan Setiawan dan Nina Kartika dengan baris Manage TAG (Dinamis #5); spec memakai user seed milik spec supaya Pre-setup bersama tidak diubah (S-06).
  - TC-299 Post Condition ("Dimas Anggara dan Gita Permata tetap Total Control dan memiliki baris Manage hardware") untuk bagian "tetap Total Control" tidak punya langkah observasi di TC dan tidak diasersi; bagian baris Manage hardware punya padanan di Expected b.
  - TC-134 Expected c tidak menyebut Modified By; spec mengasersi Modified By `Eko P` dan `Ahmad F` untuk membedakan entri sesi B dan sesi A (format `[First Name] [Last Initial]`).
  - TC-296 Expected e ("Changelog hanya memuat entry Remove Nina Kartika") tidak menyebut surface; spec memakai Changelog Detail "Manage TAG".
