---
id: TC-AC-ACAL-E2E-017-state-tenant-entitas-suspended-baca-dan-aksi-tercatat
title: "State Tenant: Entitas Suspended Tetap Dapat Membaca dan Aksi Tercatat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-42
  - TC-AC-ACAL-157
coverage:
  web: automated
---

# State Tenant: Entitas Suspended Tetap Dapat Membaca dan Aksi Tercatat

## Prerequisites

- Mode: FE+BE.
- Kelas harness h (state tenant, bagian 3 prinsip 13): entitas aktor berstatus Suspended; dipisah dari verifikasi baca biasa.
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen halaman Activity Log untuk akun Total Control Distributor Alfa (kemampuan disediakan tim FE/BE); flag Total Control Principal disetel hook suite (lihat suite.md).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)):

| Akun | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |
| Total Control (Principal) | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 1) | `Spectra.env.AC_TC_PASSWORD` |

- Urutan hook `before` spec ini: sesi API Principal men-Suspend Distributor Alfa (precondition TC-AC-ACAL-42 dan 157), lalu login Total Control Distributor Alfa. Hook `after` memulihkan status Distributor Alfa ke Active lewat sesi API Principal bila masih Suspended (walau spec gagal di tengah), lalu mengembalikan sesi ke akun default suite (Total Control Principal). Halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite.
- State global yang diubah: status Distributor Alfa (Pre-setup No 8) menjadi Suspended sampai langkah 18 mengembalikannya ke Active; suite berjalan serial. Efek pada entitas Alfa: entri User Action Suspend dan Unsuspend Distributor Alfa bertambah di audit trail.
- Butir S-06 (Pre-setup yang diubah): status Distributor Alfa (Pre-setup No 8) diubah dari Active ke Suspended di hook `before`, lalu Unsuspend di langkah 18. Pemulihan ada di hook `before` (lebih dulu memulihkan status Active lewat sesi API Principal bila sisa run sebelumnya masih Suspended, baru men-Suspend) dan di hook `after` (memulihkan Active bila masih Suspended). Efek pada Last Updated: Suspend dan Unsuspend memperbarui Last Updated Distributor Alfa; spec ini tidak mengasersi Last Updated, dan nilainya tidak dapat dipulihkan.
- Fixture: `Fixture.activityLog.*` (namaTcAlfa, modifiedByPrincipalTc) memakai fixture activityLog baru, nilai ditetapkan tim FE.
- Data Pre-setup (tetap di environment): hierarki entitas No 8 dan entri User Action untuk `Distributor Alfa` dan `Distributor Gamma` (No 10). Nama tampil akun Total Control Distributor Alfa di kolom User Tab Session: `Fixture.activityLog.namaTcAlfa` (ditetapkan tim FE) dan nama tampil Principal di kolom Modified By: `Fixture.activityLog.modifiedByPrincipalTc` (ditetapkan tim FE).
- Data Dinamis: staf `Staf Gamma {runId}-017` (Distributor Gamma; password `Spectra.env.AC_DYN_PASSWORD`) yang membuka lalu menutup Admin Console lewat sesi API di hook `before`, sebagai pembanding scope. Dihapus lewat API di hook `after` bila masih ada.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Principal (Suspend dan Unsuspend Distributor, login, pembuatan staf); pembaruan real-time tabel (auto-wait, tidak ada batas waktu di TC); baseline jumlah (S-12): jumlah hasil dicatat dari footer sebelum aksi pemicu.

## Test Steps

### TC-AC-ACAL-42: Entitas aktor Suspended tetap bisa membuka dan melihat log

1. Ketik Search `Fixture.activityLog.namaTcAlfa`, tekan Enter
2. Verifikasi baris Note `Session started` milik akun Total Control Distributor Alfa tampil pada tab Session
3. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
4. Ketik Search `Staf Gamma {runId}-017`, tekan Enter
5. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris sesi staf Distributor Gamma
6. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
7. Klik tab "User Action"
8. Ketik Search `Distributor Alfa`, tekan Enter
9. Verifikasi baris Object `Distributor` Name `Distributor Alfa` tampil pada tab User Action
10. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
11. Ketik Search `Distributor Gamma`, tekan Enter
12. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris Name `Distributor Gamma`
13. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-157: Aksi yang diizinkan modul sumber pada entitas Suspended tetap tercatat

14. Ganti akun: logout, lalu login sebagai Total Control (Principal) dengan `Spectra.env.AC_TC_PASSWORD`
15. Klik menu Activity Log di sidebar Admin Console, lalu klik tab "User Action"
16. Klik icon Filter, pilih Action `Unsuspend`, klik [Apply]
17. Ketik Search `Distributor Alfa`, tekan Enter, lalu catat jumlah total hasil dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline
18. Pemicu API: Principal melakukan Unsuspend Distributor Alfa (aksi yang diizinkan modul Distributor pada entitas Suspended) hingga tersimpan
19. Tunggu aksi selesai: status Distributor Alfa kembali Active
20. Verifikasi jumlah total hasil pada footer bertambah satu dari baseline langkah 17 tanpa memuat ulang halaman
21. Verifikasi baris baru Action `Unsuspend` Object `Distributor` Name `Distributor Alfa` tampil dengan Modified By `Fixture.activityLog.modifiedByPrincipalTc`

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-42, 157).
- Urutan TC sama dengan sumber (42 lalu 157) karena TC-AC-ACAL-157 membutuhkan Distributor Alfa masih Suspended sampai aksi Unsuspend; Unsuspend ada di langkah 18 sebagai aksi TC-AC-ACAL-157.
- Pelaku kedua pada langkah 18 memakai sesi API (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`): bukan konteks kedua, tanpa butir `P-2`. Langkah 14 mengganti akun ke Principal sebagai pengamat tabel.
- Langkah penghubung (tanpa awalan `Verifikasi`): mengetik dan menutup Search (langkah 1, 3, 4, 6, 8, 10, 11, 13), membuka tab dan menu (langkah 7, 15), ganti akun (langkah 14), memasang Filter Action dan Search sebelum baseline (langkah 16, 17), serta "Tunggu aksi selesai" (langkah 19, bagian 8b butir 8).
- Asersi tambahan di luar Expected TC (S-03): langkah 4 sampai 6 dan 11 sampai 13 membuktikan scope Alfa dengan data Gamma yang tidak tampil, untuk menjalankan frasa "sesuai scope Alfa" di Expected a dan b TC-AC-ACAL-42 (anchor: empty state hasil Search, bagian 8b butir 2).
- Asersi tambahan di luar Expected TC (S-03): langkah 20 (jumlah total bertambah satu dari baseline langkah 17, tanpa memuat ulang halaman) membuktikan baris pada langkah 21 adalah entri aksi ini dan bukan entri Unsuspend lama (baseline S-12); frasa "tanpa memuat ulang halaman" mengandalkan pembaruan real-time tabel yang disediakan tim FE (Prerequisites). TC-AC-ACAL-157 Expected b hanya menyebut baris tercatat dengan Modified By Principal (langkah 21).
- Temuan untuk QA:
  - TC-AC-ACAL-42 Expected "Tab Session tampil sesuai scope Alfa" tidak menyebut baris yang harus tampil; spec memakai baris sesi akun Alfa sendiri (Note `Session started`) dan baris `Distributor Alfa` di User Action serta ketiadaan data Gamma.
  - TC-AC-ACAL-157 Post Condition "Distributor Alfa berstatus Active" tidak punya langkah observasi di TC; tidak diasersi di spec (hook `after` memastikan status Active).
  - TC-AC-ACAL-157 Expected a berisi `-`; hanya Expected b yang diasersi.
  - Akun yang melakukan Suspend Distributor Alfa untuk precondition tidak disebut TC; spec memakai sesi API Principal (disediakan tim FE/BE). `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_ALFA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di keduanya; email memakai placeholder `{namaCompany}`.
  - TC-AC-ACAL-42 tidak menyebut apakah login akun entitas Suspended diizinkan; spec mengikuti precondition TC (login Total Control Distributor Alfa saat Suspended).
