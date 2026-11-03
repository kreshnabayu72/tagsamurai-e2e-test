---
id: TC-AC-ACAL-E2E-043-realtime-baris-baru-saringan-aktif-opsi-filter-bertambah-dan-halaman-lebih-dari-satu
title: "Real-time: Baris Baru, Saringan Aktif, Opsi Filter Bertambah, dan Halaman Lebih dari Satu"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-137
  - TC-AC-ACAL-138
  - TC-AC-ACAL-139
  - TC-AC-ACAL-148
  - TC-AC-ACAL-166
  - TC-AC-ACAL-177
coverage:
  web: automated
---

# Real-time: Baris Baru, Saringan Aktif, Opsi Filter Bertambah, dan Halaman Lebih dari Satu

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md).
- Akun pengamat (satu sesi UI pada satu waktu): Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`), disebut "Principal" pada langkah dan menjadi pengamat langkah 1 sampai 35 dan 46 sampai 56. Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Satu-satunya pergantian akun adalah blok TC-AC-ACAL-166: langkah 36 login sebagai Principal segar (di bawah) dan langkah 45 login kembali sebagai Principal Pre-setup No 1; hook `after` memulihkan sesi ke akun default suite.
- Pelaku kedua ("tab lain", "admin lain", "staf lain" pada TC) hanya memicu perubahan state dan tidak diasersi, sehingga dijalankan lewat sesi API aktor (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`); tidak ada sesi UI kedua dan tidak memakai `P-2`. Langkah pemicu diberi awalan "Pemicu API".
- Jendela pengamatan absence: "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bagian 6 konvensi, jendela amat SSE); TC tidak menyatakan durasinya.
- Rows per page tab User Action: `10` (nilai default).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`; password staf `Spectra.env.AC_DYN_PASSWORD`:
  - Client `Sejahtera {runId}-043` dan Client `Karya {runId}-043` (milik Principal), dipakai sebagai target ubah PIC Name pada TC-AC-ACAL-137, 138, dan 177; Partner `Partner Uji {runId}-043` berstatus Active sebagai target Suspend TC-AC-ACAL-138. Semuanya pengganti Client Sejahtera, Client Karya, dan Partner Beta Pre-setup supaya data Pre-setup tidak diubah (S-06).
  - Staf `Staf Realtime {runId}-043` (Principal) yang membuka Admin Console pada TC-AC-ACAL-139.
  - Dua entri User Action seed (TC-AC-ACAL-148): `{runId}-043 Urut A` bercap `10:10` dan `{runId}-043 Urut B` bercap `10:05` pada tanggal `Fixture.activityLog.tanggalUrutan` (ditetapkan tim FE/BE; TC hanya menyebut jam), ditulis dengan entri `10:05` setelah entri `10:10`. Mekanisme seeding bercap waktu tidak didefinisikan di TC, PRD, atau LLD: disediakan tim FE/BE.
  - Volume: sedikitnya 35 entri User Action (Pre-setup No 11, seed BE) agar halaman 3 tersedia pada TC-AC-ACAL-177.
  - Principal segar per run (Data Dinamis, TC-AC-ACAL-166): entitas `Principal Segar {runId}-043` dan akun Total Control Principal `principalsegar{runId}-043@qwertysystem.net` (placeholder; suffix `{runId}-043`), password `Spectra.env.AC_PRINCIPAL_SEGAR_PASSWORD` (nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`). Entitas dan akun disediakan tim FE/BE di hook `before`, belum memiliki log Object `Wallet` tetapi memiliki sedikitnya satu log User Action Object lain (syarat langkah 38). Guided Tooltip akun ini disetel dan dipulihkan hook `before`/`after` seperti akun Pre-setup No 1. Akun ini hanya mengamati langkah 36 sampai 44 (blok TC-AC-ACAL-166) dan menjadi aktor sesi API pada langkah 41 saja ("Principal segar"); log Object `Wallet` baru ada setelah langkah 41 (Top-up Wallet). Semua pemicu lain (langkah 3, 14, 21, 22, 29, 30, 50) memakai Principal Pre-setup No 1. Field wajib Top-up Wallet (nominal dan lain-lain) disediakan tim FE/BE (TC tidak menyebutnya).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Client, Partner, dan staf dinamis di atas bila masih ada; entitas dan akun Principal segar dihapus bila API menyediakannya. Entri log tidak dapat dihapus; nama bersuffix run sehingga run berikutnya tidak bentrok.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Principal Pre-setup No 1 (ubah PIC Name Client, Suspend Partner) dan sesi API aktor Principal segar (Top-up Wallet) dan sesi API staf dinamis (membuka Admin Console); mengamati tabel tanpa memuat ulang halaman sampai pembaruan real-time tampil (auto-wait, TC tidak menyebut batas waktu); membaca posisi scroll dan halaman; baseline jumlah (S-12): jumlah total dibaca dari footer `Showing X–Y of Z entries` sebelum aksi pemicu dan asersi memakai selisih, bukan angka absolut (TC-AC-ACAL-177 menulis total `36`).
- Tidak ada state global yang diubah selain data milik spec.

## Test Steps

### TC-AC-ACAL-139: Real-time Tab Session, sesi baru muncul tanpa reload

1. Catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline S0
2. Gulir tabel ke bagian bawah halaman 1 dan catat posisi scroll
3. Pemicu API: `Staf Realtime {runId}-043` membuka Admin Console hingga baris `Session started` tersimpan
4. Verifikasi jumlah total entri bertambah satu dari baseline S0 tanpa memuat ulang halaman
5. Verifikasi tidak ada dialog yang tampil
6. Verifikasi posisi scroll dan halaman tetap sama dengan langkah 2
7. Gulir tabel ke atas
8. Verifikasi baris `Session started` milik `Staf Realtime {runId}-043` muncul di baris teratas

### TC-AC-ACAL-148: Entri yang tiba tidak berurutan tampil terurut Date

9. Klik tab "User Action"
10. Ketik Search `{runId}-043 Urut`, tekan Enter
11. Verifikasi baris `{runId}-043 Urut A` (`10:10`) berada di atas baris `{runId}-043 Urut B` (`10:05`), mengikuti urutan Date dan bukan urutan kedatangan
12. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-137: Real-time Tab User Action, baris baru muncul diam-diam

13. Catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline U0, lalu gulir tabel ke bagian bawah halaman 1 dan catat posisi scroll
14. Pemicu API: Principal mengubah PIC Name Client `Sejahtera {runId}-043` menjadi `PIC 137 {runId}-043` hingga tersimpan
15. Verifikasi jumlah total entri bertambah satu dari baseline U0 tanpa memuat ulang halaman
16. Verifikasi tidak ada dialog yang tampil
17. Verifikasi posisi scroll dan halaman tetap sama dengan langkah 13
18. Gulir tabel ke atas
19. Verifikasi baris `Edit` `Client` `Sejahtera {runId}-043` Field `PIC Name` New Value `PIC 137 {runId}-043` muncul di baris teratas

### TC-AC-ACAL-138: Real-time Tab User Action, baris yang tidak cocok saringan aktif tidak muncul

20. Klik icon Filter, pilih Object `Partner`, klik [Apply]
21. Pemicu API: Principal mengubah PIC Name Client `Sejahtera {runId}-043` menjadi `PIC 138a {runId}-043` hingga tersimpan
22. Pemicu API: Principal men-Suspend Partner `Partner Uji {runId}-043` hingga tersimpan
23. Verifikasi baris `Suspend` `Partner` `Partner Uji {runId}-043` muncul tanpa memuat ulang halaman
24. Verifikasi filter Object `Partner` tetap aktif
25. Tunggu 5 detik tanpa memuat ulang halaman
26. Verifikasi tabel tidak memuat baris Object `Client`
27. Klik icon Filter, klik [Clear Field], lalu klik [Apply]
28. Ketik Search `Karya {runId}-043`, tekan Enter
29. Pemicu API: Principal mengubah PIC Name Client `Sejahtera {runId}-043` menjadi `PIC 138b {runId}-043` hingga tersimpan
30. Pemicu API: Principal mengubah PIC Name Client `Karya {runId}-043` menjadi `PIC 138c {runId}-043` hingga tersimpan
31. Verifikasi baris `Edit` `Client` `Karya {runId}-043` Field `PIC Name` New Value `PIC 138c {runId}-043` muncul tanpa memuat ulang halaman
32. Verifikasi Search tetap `Karya {runId}-043`
33. Tunggu 5 detik tanpa memuat ulang halaman
34. Verifikasi tabel tidak memuat baris Name `Sejahtera {runId}-043`
35. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-166: Opsi dropdown filter bertambah tanpa reload saat ada log baru

36. Ganti akun: keluar dari sesi UI, login sebagai Principal segar `principalsegar{runId}-043@qwertysystem.net` (`Spectra.env.AC_PRINCIPAL_SEGAR_PASSWORD`), lalu buka Admin Console > Activity Log tab "User Action"
37. Klik icon Filter, lalu buka dropdown Object
38. Verifikasi daftar opsi Object memuat sedikitnya satu opsi
39. Verifikasi daftar opsi Object tidak memuat `Wallet`
40. Tutup dropdown Object
41. Pemicu API: Principal segar melakukan Top-up Wallet hingga tersimpan
42. Tanpa memuat ulang halaman, buka lagi dropdown Object
43. Verifikasi opsi `Wallet` muncul di daftar opsi Object
44. Tutup dropdown Object dan Filter Panel

### TC-AC-ACAL-177: Pembaruan real-time saat di halaman lebih dari satu tidak memindahkan halaman

45. Ganti akun: keluar dari sesi UI, login kembali sebagai Total Control (Principal) Pre-setup No 1, lalu buka Admin Console > Activity Log tab "User Action"
46. Catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline V0
47. Klik [Next →]
48. Klik [Next →]
49. Verifikasi tabel berada di halaman 3: footer `Showing 21–30 of V0 entries`
50. Pemicu API: Principal mengubah PIC Name Client `Sejahtera {runId}-043` menjadi `PIC 177 {runId}-043` hingga tersimpan
51. Verifikasi jumlah total pada footer bertambah satu menjadi V0 ditambah satu tanpa memuat ulang halaman
52. Verifikasi tabel tetap di halaman 3 tanpa pindah halaman otomatis
53. Verifikasi tidak ada dialog yang tampil
54. Klik [← Prev]
55. Klik [← Prev]
56. Verifikasi baris `Edit` `Client` `Sejahtera {runId}-043` Field `PIC Name` New Value `PIC 177 {runId}-043` terlihat di halaman 1

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-137, 138, 139, 148, 166, 177).
- Urutan TC di spec berbeda dari urutan sumber: TC-AC-ACAL-139 (Tab Session, tab awal) lebih dulu, lalu TC-AC-ACAL-148 (muat tabel User Action dengan seed tidak berurutan) sebelum TC-AC-ACAL-137 dan seterusnya, sehingga perpindahan tab minimal dan tiap TC mulai dari kondisi Search dan Filter kosong.
- Spec 56 langkah, di atas smell 35. Alasan: seluruh TC satu topik (pembaruan real-time Tab Session dan User Action) dan satu permukaan; tiap blok TC berdiri sendiri dengan data pemicu bersuffix sendiri dan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): baseline dan scroll (langkah 1, 2, 13, 46), pemicu lewat sesi API (langkah 3, 14, 21, 22, 29, 30, 41, 50), menggulir tabel (langkah 7, 18), membuka tab, Filter, dan dropdown (langkah 9, 20, 27, 37, 40, 42, 44), mengetik dan menutup Search (langkah 10, 12, 28, 35), ganti akun ke Principal segar dan kembali (langkah 36 dan 45; S-03, pengamat TC-AC-ACAL-166 adalah scope Principal segar, bukan Pre-setup No 1), "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 25 dan 33), serta pindah halaman (langkah 47, 48, 54, 55).
- Asersi tambahan di luar Expected TC (S-03): langkah 38 membuktikan opsi pembanding pada dropdown yang sama sudah tampil sebelum asersi absence opsi `Wallet` (bagian 8b butir 2). Absence pada langkah 26 dan 34 didahului anchor positif pada surface yang sama (langkah 23 dan 31).
- Urutan asersi TC-AC-ACAL-138 mengikuti keadaan: baris Suspend/Partner (Expected b) diasersi sebelum absence baris Client (Expected a) supaya anchor positif lebih dulu (bagian 8b butir 2 dan 5). Dua pemicu Client dan Partner pada langkah 21 dan 22 tetap berurutan seperti Langkah Uji.
- Data bersuffix `Sejahtera {runId}-043` dan `Karya {runId}-043` menggantikan Client Sejahtera dan Client Karya pada TC; Search `Karya {runId}-043` menggantikan Search `Karya` (S-12).
- Total entri tidak diasersi absolut: TC-AC-ACAL-177 menulis Z `36`; spec memakai baseline V0 dan V0 ditambah satu (S-12).
- Temuan untuk QA:
  - TC-AC-ACAL-166 mensyaratkan "belum ada log Object `Wallet`" dan log tidak dapat dihapus, sedangkan TC-AC-ACAL-96 mensyaratkan opsi `Wallet` sudah ada. Spec ini memenuhi TC-AC-ACAL-166 dengan Principal segar per run yang disediakan tim FE/BE sebagai Data Dinamis dan diamati lewat langkah ganti akun 36 (login) dan 45 (kembali ke Principal No 1); TC-AC-ACAL-96 memakai scope lain yang sudah memuat log Wallet. Entitas dan akun Principal segar (placeholder email, entitas, dan nama env) disediakan tim FE/BE.
  - TC-AC-ACAL-148 bertanda Automation `Manual Only`; spec memakai seed log bercap waktu (kemampuan tim FE/BE) dan `coverage.web: automated`. TC hanya menyebut jam `10:05` dan `10:10` tanpa tanggal.
  - TC-AC-ACAL-137, 138, 177 tidak menyebut field PIC Name tujuan dan akun admin pelaku; spec memakai Principal lewat sesi API dan nilai bersuffix.
  - TC-AC-ACAL-137 "tabel di-scroll ke bawah" tidak menyebut posisi scroll yang diharapkan; spec mencatat dan membandingkan posisi.
  - TC-AC-ACAL-138 Expected c menulis "Hanya baris Client Karya"; spec mengasersi baris Karya muncul dan baris Sejahtera tidak ada pada hasil Search.
  - TC-AC-ACAL-139 tidak menyebut staf yang membuka Admin Console; spec memakai staf dinamis Principal.
  - TC-AC-ACAL-166 tidak menyebut field wajib Top-up Wallet; disediakan tim FE/BE.
  - Email Pre-setup memakai placeholder `{namaCompany}`; password: `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_DYN_PASSWORD` dan `AC_PRINCIPAL_SEGAR_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
