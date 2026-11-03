---
id: TC-AC-ACAL-E2E-014-isolasi-scope-tab-user-action-principal-distributor-partner
title: "Isolasi Scope Tab User Action: Principal, Distributor, Partner"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-33
  - TC-AC-ACAL-34
  - TC-AC-ACAL-35
  - TC-AC-ACAL-36
  - TC-AC-ACAL-168
coverage:
  web: automated
---

# Isolasi Scope Tab User Action: Principal, Distributor, Partner

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); hook suite (flag Guided Tooltip akun Total Control Principal, kemampuan sesi API aktor) dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen untuk Total Control Principal (lihat suite.md). Untuk akun Distributor Alfa, Partner Beta, Partner Delta, dan Distributor Gamma, hook before/after spec ini menyetel dan memulihkan flag seen halaman Activity Log (kemampuan disediakan tim FE/BE).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)). Format email Pre-setup No 7: `<role><entitas>_automated_{namaCompany}@qwertysystem.net`.

| Akun | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Total Control (Principal) | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (No 1) | `Spectra.env.AC_TC_PASSWORD` |
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |
| Total Control (Partner Beta) | `totalControlAdminConsolePartnerBeta_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_BETA_TC_PASSWORD` |
| Total Control (Partner Delta) | `totalControlAdminConsolePartnerDelta_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_DELTA_TC_PASSWORD` |
| Total Control (Distributor Gamma) | `totalControlAdminConsoleDistributorGamma_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_GAMMA_TC_PASSWORD` |

- Login akun pertama (Total Control Principal) di hook `before` spec ini; halaman Admin Console > Activity Log dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): hierarki entitas No 8 (Distributor Alfa, Partner Beta, Client Karya, Client Sejahtera, Distributor Gamma, Client Omega, Partner Delta; Client Karya dipegang Partner Beta dan Partner Delta) dan entri User Action contoh No 10 dan No 13 (seed BE) untuk entitas tersebut dan Brand `Acme`, termasuk baris `Edit` / `Client` / `Client Karya` oleh Principal (precondition TC-AC-ACAL-168, hanya keberadaan barisnya yang diasersi) dan entri Object `Category`, `Language`, serta Object berawalan `Role & Permission >` (opsi UI `Role & Permission > Total Control`, `> Read Only`, `> Group Manager`, `> System Role`; precondition TC-AC-ACAL-36, dibuat Principal). Mekanisme seeding log tidak didefinisikan di TC, PRD, atau LLD: disediakan tim FE/BE.
- Entitas yang dicari (nama baris = nilai kolom Name di log; satu baris tabel = satu iterasi perulangan):

| Kode | Object | Name |
|---|---|---|
| E1 | `Distributor` | `Distributor Alfa` |
| E2 | `Client` | `Client Sejahtera` |
| E3 | `Partner` | `Partner Beta` |
| E4 | `Client` | `Client Karya` |
| E5 | `Distributor` | `Distributor Gamma` |
| E6 | `Client` | `Client Omega` |
| E7 | `Brand` | `Acme` |

- Object non-entitas TC-AC-ACAL-36 (satu baris tabel = satu iterasi; dicari lewat Search nama Object itu):

| Kode | Object (kata kunci Search) |
|---|---|
| N1 | `Category` |
| N2 | `Language` |
| N3 | `Role & Permission` (kata kunci pendek; Object di baris dan opsi filter berawalan `Role & Permission >`) |

- Pengamat TC-AC-ACAL-168 (satu baris tabel = satu iterasi):

| Kode | Pengamat | Env var password |
|---|---|---|
| P1 | Total Control (Partner Beta) | `Spectra.env.AC_BETA_TC_PASSWORD` |
| P2 | Total Control (Partner Delta) | `Spectra.env.AC_DELTA_TC_PASSWORD` |
| P3 | Total Control (Distributor Alfa) | `Spectra.env.AC_ALFA_TC_PASSWORD` |
| P4 | Total Control (Distributor Gamma) | `Spectra.env.AC_GAMMA_TC_PASSWORD` |

- Tidak ada Data Dinamis dan tidak ada state global yang diubah spec ini.

## Test Steps

### TC-AC-ACAL-33: Scope Tab User Action Principal, semua log termasuk objek non-entitas

1. Klik tab "User Action"
2. Untuk setiap baris tabel Entitas yang dicari E1 sampai E7 (langkah 2 sampai 4): ketik Search `Name` pada baris itu, tekan Enter
3. Verifikasi baris Object `Object` Name `Name` pada baris tabel itu tampil
4. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-34: Scope Tab User Action Distributor, diri, Client miliknya, Partner jaringan, dan Client Partner

5. Ganti akun: logout, lalu login sebagai Total Control (Distributor Alfa) dengan `Spectra.env.AC_ALFA_TC_PASSWORD`
6. Klik menu Activity Log di sidebar Admin Console, lalu klik tab "User Action"
7. Untuk setiap baris tabel Entitas yang dicari E1, E2, E3, dan E4 (langkah 7 sampai 9): ketik Search `Name` pada baris itu, tekan Enter
8. Verifikasi baris Object `Object` Name `Name` pada baris tabel itu tampil
9. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
10. Untuk setiap baris tabel Entitas yang dicari E5 dan E6 (langkah 10 sampai 12): ketik Search `Name` pada baris itu, tekan Enter
11. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris dengan Name pada baris tabel itu
12. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-36: Objek non-entitas tidak tampil untuk Distributor dan Partner

13. Ketik Search `Acme`, tekan Enter (Distributor Alfa)
14. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris Object `Brand` Name `Acme`
15. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
16. Untuk setiap Object `Category`, `Language`, dan `Role & Permission` (kata kunci Search; langkah 16 sampai 18): ketik Search nama Object itu, tekan Enter (Distributor Alfa)
17. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris dengan Object itu (N3: tanpa baris Object berawalan `Role & Permission >`)
18. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
19. Klik icon Filter, lalu buka dropdown Object
20. Verifikasi daftar opsi Object memuat sedikitnya satu opsi
21. Verifikasi daftar opsi Object tidak memuat opsi `Brand`, `Category`, `Language`, maupun opsi Object berawalan `Role & Permission >`
22. Tutup dropdown Object dan Filter Panel
23. Ganti akun: logout, lalu login sebagai Total Control (Partner Beta) dengan `Spectra.env.AC_BETA_TC_PASSWORD`
24. Klik menu Activity Log di sidebar Admin Console, lalu klik tab "User Action"
25. Ketik Search `Acme`, tekan Enter (Partner Beta)
26. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris Object `Brand` Name `Acme`
27. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
28. Untuk setiap Object `Category`, `Language`, dan `Role & Permission` (kata kunci Search; langkah 28 sampai 30): ketik Search nama Object itu, tekan Enter (Partner Beta)
29. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris dengan Object itu (N3: tanpa baris Object berawalan `Role & Permission >`)
30. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
31. Klik icon Filter, lalu buka dropdown Object
32. Verifikasi daftar opsi Object memuat sedikitnya satu opsi
33. Verifikasi daftar opsi Object tidak memuat opsi `Brand`, `Category`, `Language`, maupun opsi Object berawalan `Role & Permission >`
34. Tutup dropdown Object dan Filter Panel

### TC-AC-ACAL-35: Scope Tab User Action Partner, diri dan Client miliknya saja

35. Untuk setiap baris tabel Entitas yang dicari E3 dan E4 (langkah 35 sampai 37): ketik Search `Name` pada baris itu, tekan Enter
36. Verifikasi baris Object `Object` Name `Name` pada baris tabel itu tampil
37. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
38. Untuk setiap baris tabel Entitas yang dicari E1, E2, E5, dan E6 (langkah 38 sampai 40): ketik Search `Name` pada baris itu, tekan Enter
39. Verifikasi hasil Search kosong: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`, tanpa baris dengan Name pada baris tabel itu
40. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-168: Log Client yang dipegang lebih dari satu Partner tampil untuk setiap Partner pemegang

41. Untuk setiap baris tabel Pengamat TC-AC-ACAL-168 (langkah 41 sampai 44): ganti akun, yaitu logout lalu login sebagai pengamat baris itu dengan env var password baris itu
42. Klik menu Activity Log di sidebar Admin Console, lalu klik tab "User Action"
43. Ketik Search `Client Karya`, tekan Enter
44. Verifikasi baris Action `Edit` Object `Client` Name `Client Karya` tampil

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-33, 34, 35, 36, 168).
- Pengulangan (bagian 8b butir 7): langkah 2 sampai 4 (7 iterasi), 7 sampai 9 (4 iterasi), 10 sampai 12 (2 iterasi), 16 sampai 18 (3 iterasi), 28 sampai 30 (3 iterasi), 35 sampai 37 (2 iterasi), 38 sampai 40 (4 iterasi), dan 41 sampai 44 (4 iterasi). Parameter tiap iterasi ada di tabel Prerequisites: Entitas yang dicari E1 sampai E7 (langkah 2 sampai 4, 7 sampai 12, 35 sampai 40), Object non-entitas N1 sampai N3 (langkah 16 sampai 18 dan 28 sampai 30), dan Pengamat P1 sampai P4 (langkah 41 sampai 44); tidak ada langkah bersyarat; asersi tampil dan tidak tampil ditulis di perulangan terpisah.
- Urutan TC di spec berbeda dari urutan sumber: TC-AC-ACAL-36 (Alfa lalu Beta) ditaruh sebelum TC-AC-ACAL-35 supaya sesi Alfa dan Beta masing-masing dipakai berurutan dan jumlah ganti akun minimal; TC-AC-ACAL-168 terakhir karena memakai empat akun. Iterasi pertama langkah 41 (Partner Beta) mengulang login akun yang sedang aktif supaya perulangan tidak bersyarat.
- Spec 44 langkah nominal, 110 setelah ekspansi perulangan, di atas smell 35. Alasan: seluruh blok satu topik dan satu kelas (isolasi scope Tab User Action oleh query yang sama dengan pengamat berbeda), dataset sama, dan tiap blok akun berdiri sendiri setelah Step ganti akun sehingga kegagalan satu akun tidak membuat akun lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun (langkah 5, 23, 41), membuka menu dan tab (langkah 1, 6, 24, 42), mengetik Search (langkah 2, 7, 10, 13, 16, 25, 28, 35, 38, 43), menutup Search (langkah 4, 9, 12, 15, 18, 27, 30, 37, 40), dan membuka lalu menutup dropdown Object (langkah 19, 22, 31, 34).
- Asersi tambahan di luar Expected TC (S-03): langkah 20 dan 32 membuktikan daftar opsi Object memuat sedikitnya satu opsi sebelum asersi absence opsi (bagian 8b butir 2). Asersi absence baris memakai empty state `No results found` hasil Search sebagai anchor positif. Langkah 16 sampai 18 (Alfa) dan 28 sampai 30 (Beta) mengasersi baris Object `Category`, `Language`, dan Object berawalan `Role & Permission >` per TC-AC-ACAL-36 Expected a dan b; kata kunci Search mengikuti TC-AC-ACAL-36 Langkah 1: `Acme` (Name entri Brand), lalu `Category`, `Language`, dan `Role & Permission` (kata kunci pendek) satu per satu.
- Batas asersi "hanya" (TC-AC-ACAL-35 "diri dan Client miliknya saja", TC-AC-ACAL-36 "tidak tampil"): diperiksa dengan sampel, yaitu entitas E1, E2, E5, E6 (langkah 38 sampai 40), Object N1 sampai N3, dan opsi `Brand`, `Category`, `Language`, serta opsi berawalan `Role & Permission >` pada dropdown Object; bukan seluruh baris atau seluruh opsi tabel, sehingga entri lain di luar sampel tidak diasersi.
- Asersi "tampil" TC-AC-ACAL-33 sampai 35 memakai Search nama entitas (padanan kolom Name) agar baris ditemukan di antara banyak entri; TC menulis "Filter Object lalu amati baris" tanpa nilai filter.
- Temuan untuk QA:
  - Email Pre-setup memakai placeholder `{namaCompany}` (nilai ditetapkan tim FE); email akun Distributor Alfa, Partner Beta, Partner Delta, dan Distributor Gamma tidak ditulis utuh di Pre-setup No 7 ("format email sama"); `AC_TC_PASSWORD` terdaftar di `.env.example` dan `spectra.config.ts`; nama `AC_ALFA_TC_PASSWORD`, `AC_BETA_TC_PASSWORD`, `AC_DELTA_TC_PASSWORD`, `AC_GAMMA_TC_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
  - TC-AC-ACAL-33 menyebut "Filter Object lalu amati baris" tanpa menentukan nilai filter; spec memakai Search nama entitas.
  - TC-AC-ACAL-36 memberi kata kunci per Object (`Acme`, `Category`, `Language`, `Role & Permission`); spec memakainya persis pada langkah 13, 16 sampai 18, 25, dan 28 sampai 30, dan tetap mengasersi daftar opsi Object (langkah 21 dan 33). Karena entri non-entitas hanya diasersi lewat kata kunci itu, entri non-entitas yang tidak memuat kata kunci itu tidak tercakup.
  - TC-AC-ACAL-168 menyebut precondition "Principal mengedit Client Karya" tanpa menyebut field yang diubah; spec hanya mengasersi keberadaan baris `Edit` / `Client` / `Client Karya` dari seed BE.
  - TC-AC-ACAL-34 dan 35 memakai nama entitas literal sebagai kata kunci; QA konfirmasi bahwa nilai kolom Name log memakai nama entitas persis seperti di Pre-setup No 8.
  - Kata kunci Search `Role & Permission` adalah bentuk pendek; Object di baris dan opsi filter UI berawalan `Role & Permission >` (PRD Enum Object), sehingga asersi absence filter memakai awalan itu.
