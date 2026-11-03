---
id: TC-AC-ACAL-E2E-025-sort-tab-session-semua-kolom-dan-perpindahan-target
title: "Sort Tab Session: Semua Kolom dan Perpindahan Target"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-74
  - TC-AC-ACAL-75
  - TC-AC-ACAL-76
  - TC-AC-ACAL-77
  - TC-AC-ACAL-78
  - TC-AC-ACAL-79
coverage:
  web: automated
---

# Sort Tab Session: Semua Kolom dan Perpindahan Target

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; `{namaCompany}` ditetapkan tim FE), password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Activity Log (lihat suite.md).
- Data Pre-setup (Pre-setup No 12; nama literal menurut Lampiran A butir A-3, seeding idempotent, tidak dihapus): `Ani` (tanpa Employee ID), `Jane Smith` (tanpa Position), `John Dalton`, dan `John Davis` (keduanya tampil `John D`). Tidak ada Data Dinamis di Tab Session.
- Data log Tab Session (seed BE; Date berada pada satu hari yang ditetapkan tim FE, bukan 17 sampai 20 Jun 2026 yang dipakai data Filter Date). Dua nilai distinct atau lebih tiap kolom diasersi (S-11). Baris diidentifikasi lewat User, Note, dan IP Address:

  | Kode | Waktu | User | Employee ID | Position | Division | Note | IP Address | Device / Browser |
  |---|---|---|---|---|---|---|---|---|
  | s1 | `09:00` | `Ani` | `—` | `Staff` | `Finance` | `Session started` | `192.0.2.10` | `Chrome on Windows` |
  | s2 | `10:20` | `Jane Smith` | `EMP002` | `—` | `Finance` | `Session ended` | `2001:db8::1a` | `Safari on macOS` |
  | s3 | `11:00` | `John Dalton` | `EMP101` | `Manager` | `anggur` | `Session started` | `10.0.0.9` | `Edge on Windows` |
  | s4 | `12:00` | `John Davis` | `EMP102` | `Analyst` | `Apel` | `Session ended` | `10.0.0.10` | `Firefox on Linux` |

- Data log Tab User Action untuk TC-AC-ACAL-79 (seed BE, Date pada hari seed yang sama): dua entri Object `Partner` pada `12:30` dan `12:45` dengan Name `Partner Urut 1 {runId}-025` dan `Partner Urut 2 {runId}-025` (`{runId}` hanya digit).
- Urutan relatif baris s1 sampai s4 diasersi (bukan posisi mutlak) karena tabel audit trail memuat entri dari run dan spec lain. Urutan default (netral) baris seed adalah Date terbaru di atas: s4, s3, s2, s1.
- Data uji TC-AC-ACAL-75 (kolom `-` pada "Baris kosong" dilewati; nilai kosong tampil `—`, berada di akhir saat A-Z dan di awal saat Z-A; bagian 8b butir 7):

  | Kolom | Urutan ↑ (A-Z) | Baris kosong | Urutan ↓ (Z-A) |
  |---|---|---|---|
  | Employee ID | s2, s3, s4, s1 | s1 (`Ani`) | s1, s4, s3, s2 |
  | Position | s4, s3, s1, s2 | s2 (`Jane Smith`) | s2, s1, s3, s4 |
  | Division | s3, s4, s2, s1 (`anggur` sebelum `Apel`, lalu dua baris `Finance` mengikuti tie-break Date terbaru di atas) | - | s2, s1, s4, s3 |
  | Note | s4, s2, s3, s1 (`Session ended` sebelum `Session started`) | - | s3, s1, s4, s2 |
  | Device / Browser | s1, s3, s4, s2 | - | s2, s4, s3, s1 |

- Data uji TC-AC-ACAL-78 (nilai tampil kolom konstan pada baris seed):

  | Kolom | Nilai tampil |
  |---|---|
  | Activity | `Session` |
  | Status | `—` |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dan User Action dengan stempel waktu, IP Address, Device / Browser, dan nilai kolom seperti tabel di atas (mekanisme seeding entri log tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis dengan endpoint karangan); menelusuri halaman bila baris tidak berada di halaman pertama; hover sel User untuk membaca tooltip nama lengkap.
- State global: sort dan saringan direset hook `beforeEach` suite pada spec berikutnya; spec memulihkan sort ke netral di langkah 27, 30, 53, dan 55. Entri log tidak dapat dihapus dan tetap ada sebagai snapshot.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Buka Filter, pilih User `Ani`, `Jane Smith`, `John Dalton`, dan `John Davis`, klik `[Apply]`
2. Verifikasi baris s1, s2, s3, dan s4 tampil

### TC-AC-ACAL-74: Sort Date siklus tiga tahap

3. Klik ikon sort Date
4. Verifikasi ikon sort Date `↑`
5. Verifikasi baris s1, s2, s3, s4 berurutan Oldest First
6. Klik ikon sort Date lagi
7. Verifikasi ikon sort Date `↓`
8. Verifikasi baris s4, s3, s2, s1 berurutan Newest First
9. Klik ikon sort Date lagi
10. Verifikasi ikon sort Date netral
11. Verifikasi baris kembali ke default Date terbaru di atas (s4, s3, s2, s1)

### TC-AC-ACAL-75: Sort alfabetis Employee ID, Position, Division, Note, Device / Browser

12. Untuk setiap baris tabel Data uji TC-AC-ACAL-75 (langkah 12 sampai 20): klik ikon sort kolom
13. Verifikasi baris s1 sampai s4 berurutan A-Z sesuai kolom "Urutan ↑"
14. Verifikasi baris kosong pada kolom "Baris kosong" berada di akhir (kolom bertanda `-` dilewati)
15. Klik ikon sort kolom lagi
16. Verifikasi baris s1 sampai s4 berurutan Z-A sesuai kolom "Urutan ↓"
17. Verifikasi baris kosong pada kolom "Baris kosong" berada di awal (kolom bertanda `-` dilewati)
18. Klik ikon sort kolom lagi
19. Verifikasi sort netral
20. Verifikasi baris kembali ke default Date terbaru di atas (s4, s3, s2, s1)

### TC-AC-ACAL-76: Sort User berdasarkan nama lengkap

21. Klik ikon sort User (ascending)
22. Hover sel User baris s3
23. Verifikasi tooltip sel User baris s3 memuat `John Dalton`
24. Hover sel User baris s4
25. Verifikasi tooltip sel User baris s4 memuat `John Davis`
26. Verifikasi baris s3 (`John Dalton`) berada di atas baris s4 (`John Davis`)
27. Klik ikon sort User dua kali lagi hingga netral

### TC-AC-ACAL-77: Sort IP Address berbasis string

28. Klik ikon sort IP Address (ascending)
29. Verifikasi baris berurutan string: s4 (`10.0.0.10`), s3 (`10.0.0.9`), s1 (`192.0.2.10`), s2 (`2001:db8::1a`)
30. Klik ikon sort IP Address dua kali lagi hingga netral

### TC-AC-ACAL-78: Sort Activity dan Status, nilai konstan, urutan ikut tie-break

31. Untuk setiap baris tabel Data uji TC-AC-ACAL-78 (langkah 31 sampai 39): klik ikon sort kolom
32. Verifikasi ikon sort kolom `↑`
33. Verifikasi baris s4, s3, s2, s1 berurutan Date terbaru di atas karena semua bernilai sama (tie-break)
34. Klik ikon sort kolom lagi
35. Verifikasi ikon sort kolom `↓`
36. Verifikasi baris s4, s3, s2, s1 berurutan Date terbaru di atas
37. Klik ikon sort kolom lagi
38. Verifikasi ikon sort kolom netral
39. Verifikasi baris s4, s3, s2, s1 berurutan Date terbaru di atas

### TC-AC-ACAL-79: Pindah target sort dan tie-break Date terbaru di atas

40. Klik ikon sort Position (ascending)
41. Verifikasi ikon sort Position `↑` aktif
42. Klik ikon sort Division (ascending)
43. Verifikasi ikon sort Position kembali netral
44. Verifikasi ikon sort Division `↑` aktif
45. Verifikasi baris Division `Finance` pukul `10:20` (s2) berada di atas baris Division `Finance` pukul `09:00` (s1)
46. Klik tab User Action
47. Ketik Search `{runId}-025`, tekan Enter
48. Klik ikon sort Action (ascending)
49. Klik ikon sort Object (ascending)
50. Verifikasi ikon sort Action kembali netral
51. Verifikasi ikon sort Object `↑` aktif
52. Verifikasi baris Object `Partner` pukul `12:45` berada di atas baris Object `Partner` pukul `12:30`

### Pemulihan state

53. Klik ikon sort Object dua kali lagi hingga netral, lalu klik `←` pada kotak Search
54. Klik tab Session
55. Klik ikon sort Division dua kali lagi hingga netral

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (bagian 4a, Tab Session). Seluruh TC sumber spec ini dikerjakan di sini.
- Pembagian TC lintas tab: TC-AC-ACAL-79 menyentuh dua tab (Tab Session lalu Tab User Action, langkah 40 sampai 52); seluruh TC tetap di spec ini karena TC satu spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): saringan User pembatas ke subjek seed (langkah 1) dan Search `{runId}-025` pembatas ke baris seed User Action (langkah 47), supaya baris teramati berada di halaman yang sama (S-14); pemulihan sort (langkah 27, 30, 53, 55); dan pergantian tab (langkah 46 dan 54). Langkah 2 adalah pembanding generik sebelum asersi urutan.
- Langkah 12 sampai 20 berulang untuk setiap baris tabel Data uji TC-AC-ACAL-75 (lima iterasi) dan langkah 31 sampai 39 untuk setiap baris tabel Data uji TC-AC-ACAL-78 (dua iterasi), sesuai bagian 8b butir 7.
- Spec memiliki 55 langkah nominal dan 100 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Sort Tab Session pada akun dan dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari dua perulangan per kolom data tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD`, yang sudah terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding entri Session dan User Action (stempel waktu, IP Address, Device / Browser) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan "disediakan tim FE/BE".
  - TC-AC-ACAL-75 hanya menetapkan nilai `anggur` / `Apel`, `Ani`, dan `Jane Smith`; nilai Employee ID, Position, Note, dan Device / Browser lain adalah pilihan spec dengan sedikitnya dua nilai distinct tiap kolom (S-11). Urutan Z-A baris `Finance` memakai tie-break Date terbaru di atas sesuai TC-AC-ACAL-79.
  - TC-AC-ACAL-79 langkah 4 (Tab User Action) tidak menyebut Action entri `Partner`; nilai Action baris seed ditetapkan tim FE dan tidak diasersi.
