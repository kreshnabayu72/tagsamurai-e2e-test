---
id: TC-GS-ACTLOG-E2E-011-isolasi-entitas-client-principal-distributor-partner-dan-realtime-lintas-entitas
title: "Isolasi Entitas: Client, Principal, Distributor, Partner, dan Realtime Lintas Entitas"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-35
  - TC-GS-ACTLOG-36
  - TC-GS-ACTLOG-198
coverage:
  web: automated
---

# Isolasi Entitas: Client, Principal, Distributor, Partner, dan Realtime Lintas Entitas

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Kelas harness c (multi-konteks: banyak tenant dalam satu alur). Pemicu di Client Beta dan di Client Alfa untuk TC-GS-ACTLOG-198 dijalankan lewat sesi API; tidak ada konteks browser kedua. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Akun yang diuji (Data Pre-setup, tetap di environment):

| No | Entitas | Role | Akun | Env var password | Nama tampil akun | Brand seed milik entitas |
|---|---|---|---|---|---|---|
| 1 | Client Alfa | Total Control | `Fixture.activityLog.clientAlfa` (email ditetapkan tim FE) | `Spectra.env.GS_CLIENTALFA_TC_PASSWORD` | disediakan tim FE | `Seed Client Alfa {runId}-011` |
| 2 | Client Beta | Total Control | `Fixture.activityLog.clientBeta` (email ditetapkan tim FE) | `Spectra.env.GS_CLIENTBETA_TC_PASSWORD` | `Rina Marlina` | `Seed Client Beta {runId}-011` |
| 3 | Principal Satu | Total Control | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` | disediakan tim FE | `Seed Principal Satu {runId}-011` |
| 4 | Distributor Dua | Total Control | `totalControlDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD` | disediakan tim FE | `Seed Distributor Dua {runId}-011` |
| 5 | Partner Tiga | Total Control | `Fixture.activityLog.partnerTiga` (email ditetapkan tim FE) | `Spectra.env.GS_PARTNER_TC_PASSWORD` (env baru) | disediakan tim FE | `Seed Partner Tiga {runId}-011` |

- Login akun 1 (Client Alfa) di hook `before`. Ganti akun ke baris 3, 4, dan 5 ditulis sebagai langkah eksplisit (perulangan langkah 44 sampai 55). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `GS_TC_PASSWORD`).
- Nama `Rina Marlina` adalah nama tampil akun Client Beta (baris 2) dan ditulis literal karena menjadi nilai Search dan opsi filter yang diasersi (TC-GS-ACTLOG-35 dan TC-GS-ACTLOG-198). Client Alfa tidak boleh punya user bernama `Rina`.
- Data Dinamis (suffix per run dan nomor spec), dibuat di hook `before` lewat aksi nyata via API:
  - Entri Session `Login` tiap entitas: login tiap akun baris 1 sampai 5 lewat API.
  - Entri User Action `Create` `Brand` tiap entitas: Create Brand pada kolom "Brand seed milik entitas" oleh akun entitas itu lewat API.
  - Aktivitas operasional FAMS dengan nama aset `Forklift FA {runId}-011` dan SAMS dengan nama `Supply SAMS {runId}-011` pada Client Alfa, dibuat lewat API modul FAMS dan SAMS oleh akun baris 1.
  - User `Realtime Alfa {runId}-011` (First Name `Realtime`, Last Name `Alfa {runId}-011`) pada Client Alfa, password `Spectra.env.ACTLOG_PASSWORD`, dipakai sebagai pelaku pembukti realtime pada TC-GS-ACTLOG-198.
  - Pemicu TC-GS-ACTLOG-198 (langkah 29, 30, 37, 38), dijalankan lewat sesi API pada saat langkah: login `Rina Marlina`, login `Realtime Alfa {runId}-011`, Create Brand `Beta Corp {runId}-011` oleh akun baris 2, dan Create Brand `Realtime Alfa {runId}-011` oleh akun baris 1.
- Kemampuan teknis (disediakan tim FE/BE): (a) sesi API tiap akun baris 1 sampai 5 untuk login dan Create Brand; (b) event realtime tabel Activity Log dikirim ke sesi Client Alfa (perilaku realtime TC-GS-ACTLOG-195 dan 196 berlaku).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Brand bersuffix `{runId}-011` di tiap entitas, user `Realtime Alfa {runId}-011`, serta aset `Forklift FA {runId}-011` dan `Supply SAMS {runId}-011`.

## Test Steps

### TC-GS-ACTLOG-35: Isolasi entitas, Client hanya melihat log miliknya pada kedua tab

1. Buka Global Settings > Activity Log > Session
2. Verifikasi baris Login milik akun Total Control Client Alfa (nama tampil pada tabel Prerequisites) tampil pada tabel Session
3. Ketik Search `Rina`, tekan Enter
4. Verifikasi tidak ada baris milik Client Beta pada tab Session
5. Ganti isi kotak search dengan `Forklift FA {runId}-011`, tekan Enter
6. Verifikasi log operasional FAMS `Forklift FA {runId}-011` tidak muncul pada tabel Session
7. Ganti isi kotak search dengan `Supply SAMS {runId}-011`, tekan Enter
8. Verifikasi log operasional SAMS `Supply SAMS {runId}-011` tidak muncul pada tabel Session
9. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
10. Klik icon Filter, buka daftar opsi User
11. Verifikasi opsi filter User memuat nama tampil akun Client Alfa
12. Verifikasi opsi filter User tidak memuat `Rina Marlina`
13. Tutup Filter Panel, klik Tab `User Action`
14. Ketik Search `Seed Client Alfa {runId}-011`, tekan Enter
15. Verifikasi baris `Create` `Brand` `Seed Client Alfa {runId}-011` tampil pada tab User Action
16. Ganti isi kotak search dengan `Rina`, tekan Enter
17. Verifikasi tidak ada baris milik Client Beta pada tab User Action
18. Ganti isi kotak search dengan `Seed Client Beta {runId}-011`, tekan Enter
19. Verifikasi baris `Create` `Brand` `Seed Client Beta {runId}-011` tidak tampil pada tab User Action
20. Ganti isi kotak search dengan `Forklift FA {runId}-011`, tekan Enter
21. Verifikasi log operasional FAMS `Forklift FA {runId}-011` tidak muncul pada tabel User Action
22. Ganti isi kotak search dengan `Supply SAMS {runId}-011`, tekan Enter
23. Verifikasi log operasional SAMS `Supply SAMS {runId}-011` tidak muncul pada tabel User Action
24. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
25. Klik icon Filter, buka daftar opsi Modified By
26. Verifikasi opsi filter Modified By memuat nama tampil akun Client Alfa
27. Verifikasi opsi filter Modified By tidak memuat `Rina Marlina`

### TC-GS-ACTLOG-198: Event entitas lain tidak muncul secara realtime, kedua tab

28. Tutup Filter Panel, klik Tab `Session`
29. Lewat sesi API, login sebagai `Rina Marlina` (Client Beta) dengan `Spectra.env.GS_CLIENTBETA_TC_PASSWORD`
30. Lewat sesi API, login sebagai `Realtime Alfa {runId}-011` (Client Alfa) dengan `Spectra.env.ACTLOG_PASSWORD`
31. Pada sesi Client Alfa tanpa memuat ulang halaman, Verifikasi baris Login `Realtime Alfa {runId}-011` tampil pada tab Session
32. Pada sesi Client Alfa tanpa memuat ulang halaman, Verifikasi baris Login `Rina Marlina` tidak tampil pada tab Session
33. Muat ulang tab Session
34. Verifikasi baris Login `Realtime Alfa {runId}-011` tampil pada tab Session setelah muat ulang
35. Verifikasi baris Login `Rina Marlina` tidak tampil pada tab Session setelah muat ulang
36. Klik Tab `User Action`
37. Lewat sesi API, buat Brand `Beta Corp {runId}-011` sebagai admin Client Beta
38. Lewat sesi API, buat Brand `Realtime Alfa {runId}-011` sebagai Total Control Client Alfa
39. Pada sesi Client Alfa tanpa memuat ulang halaman, Verifikasi baris `Create` `Brand` `Realtime Alfa {runId}-011` tampil pada tab User Action
40. Pada sesi Client Alfa tanpa memuat ulang halaman, Verifikasi baris `Create` `Brand` `Beta Corp {runId}-011` tidak tampil pada tab User Action
41. Muat ulang tab User Action
42. Verifikasi baris `Create` `Brand` `Realtime Alfa {runId}-011` tampil pada tab User Action setelah muat ulang
43. Verifikasi baris `Create` `Brand` `Beta Corp {runId}-011` tidak tampil pada tab User Action setelah muat ulang

### TC-GS-ACTLOG-36: Isolasi entitas, Principal, Distributor, dan Partner masing-masing hanya melihat log entitasnya

44. Untuk setiap baris 3 sampai 5 tabel Akun yang diuji (langkah 44 sampai 55): logout, lalu login sebagai Total Control entitas pada baris tabel dengan env var password pada baris itu
45. Buka Global Settings > Activity Log > Session
46. Klik icon Filter, buka daftar opsi User
47. Verifikasi opsi filter User memuat nama tampil akun entitas pada baris tabel
48. Verifikasi opsi filter User tidak memuat nama tampil akun entitas lain pada tabel Akun yang diuji (baris selain baris tabel)
49. Tutup Filter Panel, klik Tab `User Action`
50. Klik icon Filter, buka daftar opsi Modified By
51. Verifikasi opsi filter Modified By memuat nama tampil akun entitas pada baris tabel
52. Verifikasi opsi filter Modified By tidak memuat nama tampil akun entitas lain pada tabel Akun yang diuji (baris selain baris tabel)
53. Tutup Filter Panel, ketik Search `{runId}-011`, tekan Enter
54. Verifikasi baris `Create` `Brand` pada kolom "Brand seed milik entitas" baris tabel tampil pada tab User Action
55. Verifikasi baris `Create` `Brand` pada kolom "Brand seed milik entitas" baris selain baris tabel tidak tampil pada tab User Action

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-35, 36, 198).
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-ACTLOG-198 ditaruh sebelum TC-GS-ACTLOG-36 karena memakai akun Client Alfa yang sama dengan TC-GS-ACTLOG-35, sehingga ganti akun ke Principal, Distributor, dan Partner hanya terjadi di akhir spec.
- Pengulangan (K-9): langkah 44 sampai 55 diulang untuk baris 3, 4, dan 5 tabel Akun yang diuji (Principal Satu, Distributor Dua, Partner Tiga); parameter tiap iterasi ada di tabel Prerequisites.
- Spec memuat 55 langkah nominal (79 langkah setelah ekspansi: 43 langkah sebelum perulangan ditambah 12 langkah dikali 3 baris), di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (c, isolasi antar-tenant) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan langkah tiap entitas pada TC-GS-ACTLOG-36 identik sehingga ditulis sebagai perulangan, bukan dipecah menurut aksi.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup Filter Panel dan pindah tab (langkah 13, 28, 36, 49, 53), mereset Search lewat `(←)` (langkah 9 dan 24), memuat ulang tab (langkah 33 dan 41), serta ganti akun (langkah 44).
- Penanda yang menggantikan langkah "catat" pada TC-GS-ACTLOG-36 dan "tabel hanya memuat log milik entitas" pada TC-GS-ACTLOG-35 (S-03): opsi filter User dan Modified By (nama tampil akun tiap entitas), Search nama Brand seed bersuffix tiap entitas, dan Search nama aset FAMS dan SAMS bersuffix. Langkah anchor positif yang tidak ada di TC: langkah 2, 11, 15, 26, 47, 51, 54 (data entitas sendiri tampil pada surface yang sama sebelum asersi ketiadaan data entitas lain).
- Langkah 29, 30, 37, dan 38 (pemicu lewat sesi API): login `Realtime Alfa {runId}-011` dan Create Brand `Realtime Alfa {runId}-011` oleh Client Alfa ditambahkan sebagai pembukti bahwa realtime hidup (langkah 31, 39), dinilai sebelum asersi ketiadaan baris Client Beta; keduanya bukan langkah TC (S-03). Sesi API Client Beta dan Client Alfa hanya memicu perubahan state; tidak ada sesi UI kedua.
- Asersi kepemilikan log per entitas (langkah 4, 17, 19, 32, 35, 40, 43, 48, 52, 55) adalah asersi isolasi, bukan asersi absence kelas g (bagian 3 prinsip 13g).
- Temuan untuk QA:
  - TC-GS-ACTLOG-35 menyebut Client Alfa dan Client Beta tanpa mengaitkannya dengan Client A/B di `.env.example`; akun Client Alfa dan Client Beta adalah fixture disediakan tim FE (`GS_CLIENTALFA_TC_PASSWORD`, `GS_CLIENTBETA_TC_PASSWORD`). Bila Client Alfa = Client A, user `Rina Marlina` milik suite Brand membuat Search `Rina` menemukan baris sah; QA konfirmasi pemetaan.
  - TC-GS-ACTLOG-35 Expected c ("hanya memuat log milik Client Alfa") tidak punya pengenal lengkap; spec mengamatinya lewat penanda Client Beta (Search `Rina`, Brand seed Client Beta) dan opsi filter.
  - TC-GS-ACTLOG-36 tidak menyebut nama user tiap entitas dan memakai langkah "catat"; spec membaca nama tampil akun tiap entitas dari opsi filter dan nama tampil itu disediakan tim FE.
  - TC-GS-ACTLOG-198 tidak punya anchor bahwa realtime pada sesi Client Alfa bekerja; spec memakai aksi Client Alfa sendiri (langkah 30, 38) sebagai pembukti.
  - Hook suite Guided Tooltip menyetel flag untuk akun aktor suite; akun baris 2 sampai 5 perlu tercakup oleh hook yang sama (flag untuk akun itu ditetapkan tim FE/BE).
