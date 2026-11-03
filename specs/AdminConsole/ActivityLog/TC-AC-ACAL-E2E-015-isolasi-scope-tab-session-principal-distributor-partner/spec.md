---
id: TC-AC-ACAL-E2E-015-isolasi-scope-tab-session-principal-distributor-partner
title: "Isolasi Scope Tab Session: Principal, Distributor, Partner"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-37
  - TC-AC-ACAL-38
  - TC-AC-ACAL-39
coverage:
  web: automated
---

# Isolasi Scope Tab Session: Principal, Distributor, Partner

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); hook suite (flag Guided Tooltip akun Total Control Principal, kemampuan sesi API aktor) dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen untuk Total Control Principal (lihat suite.md). Untuk akun Distributor Alfa dan Partner Beta, hook before/after spec ini menyetel dan memulihkan flag seen halaman Activity Log (kemampuan disediakan tim FE/BE).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)):

| Akun | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Total Control (Principal) | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 1) | `Spectra.env.AC_TC_PASSWORD` |
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |
| Total Control (Partner Beta) | `totalControlAdminConsolePartnerBeta_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_BETA_TC_PASSWORD` |

- Login akun pertama (Total Control Principal) di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (tetap di environment, tidak diubah): hierarki entitas No 8 (Distributor Alfa, Partner Beta di jaringan Alfa, Distributor Gamma).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`; password staf `Spectra.env.AC_DYN_PASSWORD` (password uji yang dipasang ke user dinamis modul Activity Log):
  - Staf per entitas. Satu baris tabel = satu iterasi perulangan. Nama bersuffix dipakai sebagai pengganti sesi staf Pre-setup No 9 agar baris tidak bercampur dengan spec lain; singkatan User mengikuti `[First Name] [Last Initial]`:

| Kode | Staf (nama lengkap) | Entitas | User tampil |
|---|---|---|---|
| S1 | `Staf Principal {runId}-015` | Principal | `Staf P` |
| S2 | `Staf Alfa {runId}-015` | Distributor Alfa | `Staf A` |
| S3 | `Staf Beta {runId}-015` | Partner Beta | `Staf B` |
| S4 | `Staf Gamma {runId}-015` | Distributor Gamma | `Staf G` |

  - Tiap staf membuka lalu menutup Admin Console lewat sesi API di hook `before`, sehingga masing-masing punya baris Note `Session started` dan `Session ended`.
  - Client `Klien Uji {runId}-015` milik Partner Beta (jaringan Distributor Alfa), dibuat lewat sesi API; staf Principal `Staf Principal {runId}-015` mengubah PIC Name client itu lewat sesi API setelah membuka Admin Console (precondition TC-AC-ACAL-38 "mengubah data Partner Beta", tidak diasersi).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Client `Klien Uji {runId}-015` dan keempat staf bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run sehingga run berikutnya tidak bentrok.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor yang membuat baris Session `Session started` dan `Session ended` untuk staf dinamis; pembuatan staf per entitas (Principal, Alfa, Beta, Gamma) dan Client milik Partner Beta lewat API.
- Tidak ada state global yang diubah.

## Test Steps

### TC-AC-ACAL-37: Scope Tab Session Principal, semua sesi staf AC

1. Untuk setiap baris tabel Staf per entitas S1 sampai S4 (langkah 1 sampai 3): ketik Search nama lengkap staf pada baris itu, tekan Enter
2. Verifikasi baris User pada kolom User tampil untuk staf baris tabel itu dengan Note `Session started`
3. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-38: Scope Tab Session Distributor, staf sendiri dan staf Partner jaringan, berbasis pemilik akun

4. Ganti akun: logout, lalu login sebagai Total Control (Distributor Alfa) dengan `Spectra.env.AC_ALFA_TC_PASSWORD`
5. Klik menu Activity Log di sidebar Admin Console
6. Untuk setiap baris tabel Staf per entitas S2 dan S3 (langkah 6 sampai 8): ketik Search nama lengkap staf pada baris itu, tekan Enter
7. Verifikasi baris User tampil untuk staf baris tabel itu dengan Note `Session started`
8. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
9. Untuk setiap baris tabel Staf per entitas S1 dan S4 (langkah 9 sampai 11): ketik Search nama lengkap staf pada baris itu, tekan Enter
10. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris sesi staf baris tabel itu
11. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-39: Scope Tab Session Partner, staf sendiri saja

12. Ganti akun: logout, lalu login sebagai Total Control (Partner Beta) dengan `Spectra.env.AC_BETA_TC_PASSWORD`
13. Klik menu Activity Log di sidebar Admin Console
14. Untuk setiap baris tabel Staf per entitas S3 (langkah 14 sampai 16): ketik Search nama lengkap staf pada baris itu, tekan Enter
15. Verifikasi baris User tampil untuk staf baris tabel itu dengan Note `Session started`
16. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
17. Untuk setiap baris tabel Staf per entitas S2, S1, dan S4 (langkah 17 sampai 19): ketik Search nama lengkap staf pada baris itu, tekan Enter
18. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris sesi staf baris tabel itu
19. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-37, 38, 39).
- Pengulangan (bagian 8b butir 7): langkah 1 sampai 3 (4 iterasi), 6 sampai 8 (2), 9 sampai 11 (2), 14 sampai 16 (1), dan 17 sampai 19 (3). Parameter tiap iterasi ada di tabel S1 sampai S4; asersi tampil dan tidak tampil ditulis di perulangan terpisah, tanpa langkah bersyarat.
- Jumlah langkah (bagian 8b butir 7): 19 langkah nominal, 40 setelah ekspansi perulangan, di atas sekitar 35. Alasan: seluruh TC satu topik dan satu permukaan (isolasi scope Tab Session), dataset staf S1 sampai S4 sama, dan tiga blok akun berdiri sendiri setelah ganti akun; ekspansi berasal dari perulangan per staf, bukan dari langkah yang berbeda.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun (langkah 4 dan 12), membuka menu (langkah 5 dan 13), mengetik Search nama lengkap staf (langkah 1, 6, 9, 14, 17) dan menutup Search (langkah 3, 8, 11, 16, 19).
- Asersi absence (langkah 10 dan 18) memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2). Baris `Session started` hasil Search sama pada langkah 7 dan 15 memastikan Tab Session sudah termuat.
- Staf dinamis bersuffix menggantikan sesi staf Pre-setup No 9 yang tidak ditulis namanya di TC (S-06, S-12); precondition TC-AC-ACAL-38 "mengubah data Partner Beta" dipenuhi dengan mengubah PIC Name Client milik Partner Beta (aksi pada target jaringan Alfa) supaya data Pre-setup Partner Beta tidak diubah.
- Temuan untuk QA:
  - Pre-setup No 9 ("sesi staf Principal, Alfa, Beta, Gamma") tidak menyebut nama atau email staf; spec memakai staf dinamis bersuffix yang disediakan tim FE/BE. Email akun Alfa dan Beta memakai placeholder `{namaCompany}`; password: `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_ALFA_TC_PASSWORD`, `AC_BETA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
  - TC-AC-ACAL-38 precondition b menyebut staf Principal "mengubah data Partner Beta" tanpa menyebut objek dan field; spec memakai PIC Name Client milik Partner Beta.
  - TC-AC-ACAL-37 sampai 39 tidak menyebut kolom Note atau Activity untuk baris sesi; spec mengasersi Note `Session started` (nilai Note sesi AC pada TC-AC-ACAL-48).
