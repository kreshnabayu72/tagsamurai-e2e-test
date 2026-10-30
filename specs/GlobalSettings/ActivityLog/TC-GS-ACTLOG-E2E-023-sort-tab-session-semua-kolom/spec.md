---
id: TC-GS-ACTLOG-E2E-023-sort-tab-session-semua-kolom
title: "Sort Tab Session: Semua Kolom"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-86
  - TC-GS-ACTLOG-87
  - TC-GS-ACTLOG-88
  - TC-GS-ACTLOG-89
  - TC-GS-ACTLOG-90
  - TC-GS-ACTLOG-91
  - TC-GS-ACTLOG-92
coverage:
  web: automated
---

# Sort Tab Session: Semua Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun subjek log: tujuh user uji pada Data Dinamis dibuat lewat API di hook `before` dan memakai password uji `Spectra.env.ACTLOG_PASSWORD` (env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Password aksi subjek: Login dengan password salah (Budi Anwar) memakai `Spectra.env.LP_PASSWORD_WRONG`; Change Password Siti Nurbaya memakai password lama `Spectra.env.ACTLOG_PASSWORD` dan password baru `Spectra.env.ACTLOG_PASSWORD_NEW` (env baru, didaftarkan di tempat yang sama). Change Password Siti Nurbaya dijalankan paling akhir di hook `before` (password menjadi `ACTLOG_PASSWORD_NEW`); tidak ada login Siti Nurbaya sesudahnya.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (sufiks `{runId}-023`, `{runId}` hanya digit):

  | Subjek | First Name | Last Name | Email | Employee ID | Position | Division |
  |---|---|---|---|---|---|---|
  | Budi Anwar | `Budi` | `Anwar {runId}-023` | `Fixture.activityLog.budi023.email` (ditetapkan tim FE, fixture baru) | `EMP001-{runId}-023` | `Staff {runId}-023` | `Finance {runId}-023` |
  | John Dalton | `John` | `Dalton {runId}-023` | `Fixture.activityLog.johnDalton023.email` (ditetapkan tim FE, fixture baru) | `EMP002-{runId}-023` | `Supervisor {runId}-023` | `Marketing {runId}-023` |
  | John Davis | `John` | `Davis {runId}-023` | `Fixture.activityLog.johnDavis023.email` (ditetapkan tim FE, fixture baru) | tanpa Employee ID | tanpa Position | `Operations {runId}-023` |
  | Siti Nurbaya | `Siti` | `Nurbaya {runId}-023` | `Fixture.activityLog.siti023.email` (ditetapkan tim FE, fixture baru) | tanpa Employee ID | tanpa Position | `Operations {runId}-023` |
  | Posisi Satu | `Posisi` | `Satu {runId}-023` | `Fixture.activityLog.posisiSatu023.email` (ditetapkan tim FE, fixture baru) | tanpa Employee ID | `Accountant {runId}-023` | `Operations {runId}-023` |
  | Posisi Dua | `Posisi` | `Dua {runId}-023` | `Fixture.activityLog.posisiDua023.email` (ditetapkan tim FE, fixture baru) | tanpa Employee ID | `finance analyst {runId}-023` | `Operations {runId}-023` |
  | Posisi Tiga | `Posisi` | `Tiga {runId}-023` | `Fixture.activityLog.posisiTiga023.email` (ditetapkan tim FE, fixture baru) | tanpa Employee ID | `Finance Manager {runId}-023` | `Operations {runId}-023` |

- Data log subjek (entri Session):

  | Subjek | Activity | Status tampil | Note | Cara |
  |---|---|---|---|---|
  | Budi Anwar | Login | `Failed` | `Incorrect password` | Aksi nyata: Login dengan password salah |
  | John Dalton | Login | `Success` | `Login with password` | Aksi nyata: Login dengan password benar |
  | John Dalton | Reset Password | `Success` | `Password reset requested` | Aksi nyata: permintaan Reset Password dari halaman Login |
  | John Davis | Logout | `—` | `Logged out` | Aksi nyata: Logout manual |
  | John Davis | Session | `—` | `Session started` | Aksi nyata: buka card Global Settings |
  | Siti Nurbaya | Change Password | `Success` | `Password changed` | Aksi nyata: Change Password di My Profile dengan password lama benar |
  | Posisi Satu, Dua, Tiga | Login | `Success` | `Login with password` | Aksi nyata: Login dengan password benar (satu entri per user) |

- Data log subjek yang dibentuk seed BE (nilai tidak dapat dibentuk dari aksi penguji):

  | Dipakai TC | Subjek | Nilai |
  |---|---|---|
  | TC-GS-ACTLOG-86 | Siti Nurbaya | tiga entri Session bertanggal `14 Jul 2026, 08:02`, `14 Jul 2026, 09:30`, dan `14 Jul 2026, 17:00` (waktu tampil) |
  | TC-GS-ACTLOG-89 | Budi Anwar | satu entri dengan Device / Browser `Chrome on Windows` |
  | TC-GS-ACTLOG-89 | John Dalton | satu entri dengan Device / Browser `Safari on iOS` |
  | TC-GS-ACTLOG-89 | Siti Nurbaya | satu entri dengan Device / Browser kosong (tampil `—`) |
  | TC-GS-ACTLOG-92 | John Davis | empat entri dengan IP Address `10.0.0.9`, `192.0.2.10`, `2001:db8::1a`, dan `9.255.255.1` |

- Data uji TC-GS-ACTLOG-87 (urutan nilai subjek):

  | Kolom | Klik 1 `(↑)` | Klik 2 `(↓)` |
  |---|---|---|
  | Activity | `Change Password`, `Login`, `Logout`, `Reset Password`, `Session` | urutan terbalik dari klik 1 |
  | Division | `Finance {runId}-023`, `Marketing {runId}-023`, `Operations {runId}-023` | `Operations {runId}-023`, `Marketing {runId}-023`, `Finance {runId}-023` |
  | Note | `Incorrect password`, `Logged out`, `Login with password` | urutan terbalik dari klik 1 |

- Data uji TC-GS-ACTLOG-89 (baris subjek yang dibandingkan: Budi Anwar, John Dalton, Siti Nurbaya; untuk Device / Browser dipakai baris seed Device):

  | Kolom | Nilai terisi A-Z | Baris bernilai kosong (`—`) |
  |---|---|---|
  | Employee ID | `EMP001-{runId}-023` (Budi Anwar), `EMP002-{runId}-023` (John Dalton) | baris Siti Nurbaya |
  | Position | `Staff {runId}-023` (Budi Anwar), `Supervisor {runId}-023` (John Dalton) | baris Siti Nurbaya |
  | Device / Browser | `Chrome on Windows` (Budi Anwar), `Safari on iOS` (John Dalton) | baris seed Siti Nurbaya |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dengan stempel waktu, Device / Browser, dan IP Address pada tabel seed di atas (tanpa mengarang endpoint); menjalankan aksi Auth dan My Profile sebagai subjek lewat sesi API yang terpisah dari sesi UI aktor; membaca indikator sort `(↑)` dan `(↓)` pada header kolom; menelusuri semua halaman hasil bila baris subjek tidak berada di halaman pertama.
- State global: Sort dan Search tab Session dikembalikan ke default di langkah 58 dan 59. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketujuh user subjek beserta Position dan Division bersuffix milik spec ini. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.

## Test Steps

1. Buka Global Settings > Activity Log > Session
2. Ketik Search `{runId}-023`, tekan Enter
3. Catat urutan awal baris subjek sebagai baseline urutan default tabel

### TC-GS-ACTLOG-86: Sort 3 klik kolom Date

4. Klik header kolom Date
5. Verifikasi indikator `(↑)` aktif
6. Verifikasi urutan Oldest First: baris `14 Jul 2026, 08:02` di atas baris `14 Jul 2026, 09:30` dan `14 Jul 2026, 17:00`
7. Klik header kolom Date lagi
8. Verifikasi indikator `(↓)` aktif
9. Verifikasi urutan Newest First: baris `14 Jul 2026, 17:00` di atas baris `14 Jul 2026, 09:30` dan `14 Jul 2026, 08:02`
10. Klik header kolom Date untuk ketiga kali
11. Verifikasi indikator sort tidak aktif
12. Verifikasi urutan kembali ke urutan default tabel (sama dengan baseline langkah 3)

### TC-GS-ACTLOG-87: Sort 3 klik kolom Activity, Division, dan Note, alfabetis

13. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-87 (langkah 13 sampai 21): klik header kolom
14. Verifikasi indikator `(↑)` aktif
15. Verifikasi urutan baris subjek sesuai kolom "Klik 1 `(↑)`"
16. Klik header kolom lagi
17. Verifikasi indikator `(↓)` aktif
18. Verifikasi urutan baris subjek sesuai kolom "Klik 2 `(↓)`"
19. Klik header kolom untuk ketiga kali
20. Verifikasi indikator sort tidak aktif
21. Verifikasi urutan kembali ke urutan default tabel (sama dengan baseline langkah 3)

### TC-GS-ACTLOG-88: Sort alfabetis tidak membedakan huruf besar dan kecil, kolom Position

22. Klik header kolom Position
23. Verifikasi urutan baris subjek: `Accountant {runId}-023`, `finance analyst {runId}-023`, `Finance Manager {runId}-023`
24. Klik header kolom Position lagi
25. Verifikasi urutan baris subjek: `Finance Manager {runId}-023`, `finance analyst {runId}-023`, `Accountant {runId}-023`
26. Klik header kolom Position untuk ketiga kali

### TC-GS-ACTLOG-89: Sort alfabetis dengan nilai kosong, kolom Employee ID, Position, dan Device / Browser

27. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-89 (langkah 27 sampai 37): klik header kolom
28. Verifikasi indikator `(↑)` aktif
29. Verifikasi nilai terisi berurutan A-Z sesuai kolom "Nilai terisi A-Z"
30. Verifikasi baris bernilai kosong (`—`) berada di paling bawah, sesudah nilai terisi
31. Klik header kolom lagi
32. Verifikasi indikator `(↓)` aktif
33. Verifikasi baris bernilai kosong (`—`) berada di paling atas
34. Verifikasi nilai terisi berurutan Z-A sesudah baris `—`
35. Klik header kolom untuk ketiga kali
36. Verifikasi indikator sort tidak aktif
37. Verifikasi urutan kembali ke urutan default tabel (sama dengan baseline langkah 3)

### TC-GS-ACTLOG-90: Sort kolom User mengikuti nama lengkap, bukan teks singkat

38. Klik header kolom User
39. Verifikasi urutan nama lengkap baris subjek: `Budi Anwar {runId}-023`, `John Dalton {runId}-023`, `John Davis {runId}-023`, `Siti Nurbaya {runId}-023`
40. Klik header kolom User lagi
41. Verifikasi urutan nama lengkap baris subjek: `Siti Nurbaya {runId}-023`, `John Davis {runId}-023`, `John Dalton {runId}-023`, `Budi Anwar {runId}-023`
42. Klik header kolom User untuk ketiga kali
43. Verifikasi indikator sort tidak aktif
44. Verifikasi urutan kembali ke urutan default tabel (sama dengan baseline langkah 3)

### TC-GS-ACTLOG-91: Sort 3 klik kolom Status mengikuti nilai tampil

45. Klik header kolom Status
46. Verifikasi indikator `(↑)` aktif
47. Verifikasi urutan: baris Status `Failed`, lalu `Success`, lalu baris `—` (Logout dan Session) di paling bawah
48. Klik header kolom Status lagi
49. Verifikasi indikator `(↓)` aktif
50. Verifikasi urutan: baris `—` di paling atas, lalu `Success`, lalu `Failed`
51. Klik header kolom Status untuk ketiga kali
52. Verifikasi indikator sort tidak aktif
53. Verifikasi urutan kembali ke urutan default tabel (sama dengan baseline langkah 3)

### TC-GS-ACTLOG-92: Sort kolom IP Address berbasis string

54. Klik header kolom IP Address
55. Verifikasi urutan baris IP subjek: `10.0.0.9`, `192.0.2.10`, `2001:db8::1a`, `9.255.255.1` (perbandingan karakter, bukan angka per oktet)
56. Klik header kolom IP Address lagi
57. Verifikasi urutan baris IP subjek terbalik dari klik 1

### Pemulihan state akhir

58. Klik header kolom IP Address untuk ketiga kali
59. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Sort Tab Session). Semua TC sumber spec ini dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (mempersempit tabel ke baris subjek spec ini lewat Search sufiks `{runId}-023`, supaya baris subjek tidak tersebar lintas halaman akibat log spec dan run lain), langkah 3 (mencatat baseline urutan default untuk asersi "urutan default tabel"), langkah 26 (klik ketiga untuk mengembalikan sort Position sebelum TC-GS-ACTLOG-89; TC-GS-ACTLOG-88 hanya menulis dua klik), langkah 58 dan 59 (membersihkan state di akhir spec; hook `after` sebagai cadangan).
- Langkah 13 sampai 21 dan 27 sampai 37 berulang untuk setiap baris tabel Data uji di Prerequisites.
- Spec memiliki 59 langkah nominal dan 99 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (Sort Tab Session pada dataset dan akun yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan sebagian besar langkah adalah `Verifikasi` indikator dan urutan hasil pemecahan klausa Expected (S-01) dari pola tiga klik yang berulang pada tujuh TC.
- Temuan untuk QA:
  - Email akun subjek (`Fixture.activityLog.<subjek>.email`) adalah fixture baru yang ditetapkan tim FE; spec tidak mengarang alamat email.
  - Tabel Tab Session entitas Client A memuat log dari spec dan run lain, sedangkan Expected TC ("urutan ...") ditulis seolah hanya data TC yang ada. Asersi urutan dibatasi pada urutan relatif baris subjek spec ini (nama bersuffix, S-12), dan nama literal TC (`Budi Anwar`, `John Dalton`, `John Davis`, `Siti Nurbaya`, `Staff`, `Supervisor`, `EMP001`, `EMP002`) diganti nama bersuffix per run.
  - "Urutan default tabel" tidak didefinisikan di TC; spec membandingkan dengan urutan awal baris subjek yang dicatat di langkah 3.
  - TC-GS-ACTLOG-86 menulis entri bertanggal `14 Jul 2026` tanpa Activity, user, Time Zone, dan Date Format; entri dibentuk seed BE dan stempel waktu ditetapkan tim BE sehingga waktu tampil sesuai TC.
  - TC-GS-ACTLOG-89 mensyaratkan baris Device / Browser kosong dan nilai Device literal yang tidak dapat dibentuk dari aksi penguji (seed BE); TC-GS-ACTLOG-92 mensyaratkan empat IP Address literal (seed BE).
  - Env baru: `ACTLOG_PASSWORD` dan `ACTLOG_PASSWORD_NEW` belum ada di `.env.example` dan perlu didaftarkan tim FE.
