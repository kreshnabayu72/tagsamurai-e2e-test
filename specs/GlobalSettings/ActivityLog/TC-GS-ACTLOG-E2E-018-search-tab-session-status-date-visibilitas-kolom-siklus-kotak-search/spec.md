---
id: TC-GS-ACTLOG-E2E-018-search-tab-session-status-date-visibilitas-kolom-siklus-kotak-search
title: "Search Tab Session: Status, Date, Visibilitas Kolom, Siklus Kotak Search"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-59
  - TC-GS-ACTLOG-61
  - TC-GS-ACTLOG-62
  - TC-GS-ACTLOG-65
coverage:
  web: automated
---

# Search Tab Session: Status, Date, Visibilitas Kolom, Siklus Kotak Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun subjek log: tiga user uji pada Data Dinamis dibuat lewat API di hook `before` dan memakai password uji `Spectra.env.ACTLOG_PASSWORD` (env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login dengan password salah memakai `Spectra.env.LP_PASSWORD_WRONG`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (sufiks `{runId}-018`, `{runId}` hanya digit sehingga kata kunci pendek `j` dan `john` tidak cocok dengan sufiks; hanya field yang diasersi dan field wajib pembuatan user yang di-seed):

  | Subjek | First Name | Last Name | Email | Employee ID | Position | Division | Tampil di kolom User |
  |---|---|---|---|---|---|---|---|
  | John | `John` | `Doe {runId}-018` | `Fixture.activityLog.john018.email` (ditetapkan tim FE, fixture baru) | `EMP001-{runId}-018` | `Staff {runId}-018` | `Marketing {runId}-018` | `John D` |
  | Budi | `Budi` | `Anwar {runId}-018` | `Fixture.activityLog.budi018.email` (ditetapkan tim FE, fixture baru) | `EMP002-{runId}-018` | `Supervisor {runId}-018` | `Finance {runId}-018` | `Budi A` |
  | Siti | `Siti` | `Nurbaya {runId}-018` | `Fixture.activityLog.siti018.email` (ditetapkan tim FE, fixture baru) | tanpa Employee ID | tanpa Position | `Operations {runId}-018` | `Siti N` |

- Data log subjek (entri Session):

  | Subjek | Activity | Status tampil | Status internal | Note | Cara |
  |---|---|---|---|---|---|
  | Budi | Login | `Failed` | Failed | `Incorrect password` | Aksi nyata: Login dengan password salah |
  | John | Login | `Success` | Success | `Login with password` | Aksi nyata: Login dengan password benar |
  | Budi | Reset Password | `Failed` | Failed | `Too many reset attempts` | Seed BE |
  | Siti | Reset Password | `Success` | Success | `Password reset requested` | Aksi nyata: permintaan Reset Password dari halaman Login |
  | Siti | Logout | `—` | Failed | `Logged out (new device login)` | Seed BE |
  | Siti | Session | `—` | Failed | `Session ended` | Seed BE |
  | John | Logout | `—` | Success | `Logged out` | Aksi nyata: Logout manual |
  | John | Session | `—` | Success | `Session started` | Aksi nyata: buka card Global Settings |
  | John | Session | `—` | Success | `Session ended` | Seed BE (stempel waktu tampil `14 Jul 26` pada Date Format `DD MMM YY`) |

- Setting General Settings: Date Format `DD MMM YY` (TC-GS-ACTLOG-61); kemampuan menyetel Date Format General Settings disediakan tim FE/BE tanpa endpoint yang dikarang. Hook `before` menyimpan nilai awal dan hook `after` memulihkannya.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dengan `status` internal Failed pada Logout dan Session, Note `Too many reset attempts`, dan stempel waktu `14 Jul 2026` (nilai itu tidak dapat dibentuk dari aksi penguji; tanpa mengarang endpoint); menyetel Date Format General Settings; menjalankan aksi Auth sebagai subjek lewat sesi API yang terpisah dari sesi UI aktor; menelusuri semua halaman hasil bila baris subjek tidak berada di halaman pertama.
- State global: Date Format General Settings dan visibilitas kolom Employee ID tab Session (dipulihkan di langkah 30 dan hook `after`). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan Date Format, tampilkan semua kolom tab Session, dan hapus lewat API ketiga user subjek beserta Position dan Division bersuffix milik spec ini. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-59: Search kolom Status mengikuti nilai tampil, baris Logout dan Session tidak cocok

2. Ketik Search `Failed`, tekan Enter
3. Verifikasi baris Login `Failed` milik Budi dan Reset Password `Failed` milik Budi tampil
4. Verifikasi baris Logout `Logged out (new device login)` dan Session `Session ended` milik Siti tidak tampil
5. Ganti isi kotak search dengan `Success`, tekan Enter
6. Verifikasi baris Login `Success` milik John dan Reset Password `Success` milik Siti tampil
7. Verifikasi baris Logout `Logged out` dan Session `Session started` milik John tidak tampil

### TC-GS-ACTLOG-61: Kolom Date tidak dapat dicari lewat Search

8. Ganti isi kotak search dengan `Session ended`, tekan Enter
9. Verifikasi baris Session `Session ended` milik John tampil dengan Date memuat `14 Jul 26`
10. Ganti isi kotak search dengan `14 Jul 26`, tekan Enter
11. Verifikasi tidak ada baris yang cocok berdasarkan tanggal
12. Verifikasi tampil `No results found`
13. Ganti isi kotak search dengan `14 Jul 2026`, tekan Enter
14. Verifikasi tidak ada baris yang cocok berdasarkan tanggal
15. Verifikasi tampil `No results found`

### TC-GS-ACTLOG-62: Search terikat visibilitas kolom

16. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
17. Ketik Search `EMP002`, tekan Enter
18. Verifikasi baris milik Budi dengan Employee ID `EMP002-{runId}-018` tampil
19. Verifikasi baris milik John dengan Employee ID `EMP001-{runId}-018` tidak tampil
20. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
21. Klik header `Column Visibility (⋯)`, hilangkan centang kolom Employee ID
22. Verifikasi kolom Employee ID hilang dari tabel
23. Tutup overlay `Column Visibility (⋯)` dengan menekan `Esc`
24. Ketik Search `EMP002`, tekan Enter
25. Verifikasi kata kunci `EMP002` tidak menampilkan baris
26. Verifikasi tampil `No results found`
27. Ganti isi kotak search dengan `Supervisor`, tekan Enter
28. Verifikasi baris milik Budi tampil (kolom Position tetap tampil)
29. Verifikasi baris milik John dengan Position `Staff {runId}-018` tidak tampil
30. Klik header `Column Visibility (⋯)`, centang kembali kolom Employee ID
31. Verifikasi kolom Employee ID tampil kembali
32. Tutup overlay `Column Visibility (⋯)` dengan menekan `Esc`
33. Ganti isi kotak search dengan `EMP002`, tekan Enter
34. Verifikasi baris milik Budi tampil
35. Verifikasi baris milik John dengan Employee ID `EMP001-{runId}-018` tidak tampil

### TC-GS-ACTLOG-65: Siklus interaksi kotak Search toolbar Tab Session

36. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
37. Arahkan kursor ke icon Search
38. Verifikasi tooltip `Search` tampil
39. Klik icon Search
40. Verifikasi kotak Search melebar
41. Verifikasi kursor otomatis fokus di kotak Search
42. Verifikasi placeholder `Search session log...`
43. Isi kotak Search dengan `j` (tanpa menekan Enter)
44. Verifikasi icon `(✕)` muncul di kanan dalam kotak
45. Verifikasi tabel belum tersaring (baris milik John, Budi, dan Siti masih tampil)
46. Tekan Enter
47. Verifikasi tabel tersaring sesuai `j`: baris milik John tampil
48. Verifikasi baris milik Budi dan Siti tidak tampil
49. Klik `(✕)` di dalam kotak Search
50. Verifikasi teks di kotak Search terhapus
51. Verifikasi kotak Search tetap terbuka dan fokus
52. Verifikasi tabel tetap menampilkan hasil `j` terakhir
53. Tekan Enter pada kotak kosong
54. Verifikasi tabel kembali menampilkan data tanpa saringan pencarian
55. Ketik Search `john`, tekan Enter
56. Klik icon `(←)`
57. Verifikasi kotak Search menutup menjadi icon Search
58. Verifikasi tabel langsung kembali tanpa saringan pencarian
59. Klik icon Search untuk membuka kembali kotak Search
60. Verifikasi isi kotak Search kosong

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Search Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-56, 57, 58, 60, 63, dan 64 ada di spec 017.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16 dan 36 (menutup Search dan mereset tabel sebelum TC berikutnya), langkah 23 dan 32 (menutup overlay `Column Visibility (⋯)` yang dibiarkan terbuka oleh langkah sebelumnya), serta langkah 59 (membuka kembali kotak Search untuk mengamati isinya). Langkah 30 menjalankan langkah TC-GS-ACTLOG-62 sekaligus memulihkan visibilitas kolom (hook `after` sebagai cadangan). "Ketik Search" membuka kotak Search bila tertutup (8b butir 9).
- Asersi tambahan yang tidak ada di Expected TC, dicatat sebagai anchor absence (8b butir 2): langkah 8 dan langkah sesudahnya membuktikan baris bertanggal `14 Jul 26` ada sebelum pencarian tanggal yang kosong; dua langkah sesudah langkah 16 membuktikan baris Budi dengan Employee ID tampil sebelum kolom disembunyikan; langkah 19, 29, dan 35 mengasersi baris John tidak tampil agar kolom Employee ID dan Position punya dua nilai terisi yang distinct (S-11).
- Spec memiliki 60 langkah, di atas smell 35 langkah. Alasan: keempat blok memakai Tab Session, akun, dan dataset yang sama, tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan sebagian besar langkah adalah `Verifikasi` hasil pemecahan klausa Expected (S-01), terutama TC-GS-ACTLOG-65.
- Temuan untuk QA:
  - TC-GS-ACTLOG-61 Expected butir b menyebut "penyaringan tanggal dilakukan lewat Filter Panel" tanpa langkah observasi; klausa itu tidak diasersi di spec ini (S-01).
  - TC-GS-ACTLOG-65 Expected butir f menyebut "isi dikosongkan" pada kotak yang sudah menutup menjadi icon Search, sehingga isinya tidak teramati; spec membuka kembali kotak lewat icon Search lalu mengasersi isinya kosong.
  - TC dan PRD tidak menentukan penutupan overlay `Column Visibility (⋯)` setelah centang kolom; spec menutupnya dengan `Esc`.
  - Tabel Tab Session entitas Client A memuat log dari spec dan run lain; asersi "tampil" dan "tidak tampil" dibatasi pada baris subjek spec ini (nama bersuffix). Nama subjek literal TC (`John Doe`, `Budi Anwar`, `Siti Nurbaya`) dan Employee ID `EMP002` diganti nama dan ID bersuffix per run (S-12); singkatan `John D`, `Budi A`, `Siti N` tetap sama.
  - Data Dinamis TC memuat Employee ID, Position, dan Division untuk `John Doe` dan `Siti Nurbaya`; spec men-seed field yang diasersi dan field wajib pembuatan user (seeding minimal, S-11), dengan pengecualian Employee ID dan Position John yang juga diisi (`EMP001-{runId}-018`, `Staff {runId}-018`) agar Search `EMP002`/`Supervisor` punya dua nilai terisi yang distinct (S-11).
  - Email akun subjek (`Fixture.activityLog.<subjek>.email`) adalah fixture baru yang ditetapkan tim FE; spec tidak mengarang alamat email.
  - TC-GS-ACTLOG-59 mensyaratkan entri Logout dan Session dengan `status` internal Failed serta Reset Password Failed `Too many reset attempts`, dan TC-GS-ACTLOG-61 entri bertanggal `14 Jul 2026` tanpa menyebut Time Zone dan jam; kondisi itu tidak dapat dibentuk dari aksi penguji sehingga dicatat sebagai seed BE.
  - TC-GS-ACTLOG-65 langkah 1 menyebut "klik icon Search, amati kotak Search" dan Expected a memuat hover icon; spec mengasersi tooltip `Search` sebelum icon diklik (urutan state, 8b butir 5).
  - Env baru: `ACTLOG_PASSWORD` belum ada di `.env.example` dan perlu didaftarkan tim FE.
