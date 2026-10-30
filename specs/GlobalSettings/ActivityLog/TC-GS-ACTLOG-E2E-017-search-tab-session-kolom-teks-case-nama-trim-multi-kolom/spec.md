---
id: TC-GS-ACTLOG-E2E-017-search-tab-session-kolom-teks-case-nama-trim-multi-kolom
title: "Search Tab Session: Kolom Teks, Case, Nama, Trim, Multi-kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-56
  - TC-GS-ACTLOG-57
  - TC-GS-ACTLOG-58
  - TC-GS-ACTLOG-60
  - TC-GS-ACTLOG-63
  - TC-GS-ACTLOG-64
coverage:
  web: automated
---

# Search Tab Session: Kolom Teks, Case, Nama, Trim, Multi-kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun subjek log: tiga user uji pada Data Dinamis dibuat lewat API di hook `before` dan memakai password uji `Spectra.env.ACTLOG_PASSWORD` (env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Change Password Budi: password baru `Spectra.env.ACTLOG_PASSWORD_NEW` (env baru, didaftarkan di tempat yang sama) dan password lama yang salah `Spectra.env.LP_PASSWORD_WRONG`. Urutan di hook `before`: Change Password dengan password lama salah lebih dulu (password Budi tetap `ACTLOG_PASSWORD`), lalu Change Password dengan password lama benar (password Budi menjadi `ACTLOG_PASSWORD_NEW`). Tidak ada login Budi sesudahnya.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (sufiks `{runId}-017`, `{runId}` hanya digit; hanya field yang diasersi dan field wajib pembuatan user yang di-seed; singkatan tampil `John D`, `Budi A`, `Siti N` sama dengan TC karena huruf awal nama belakang dipertahankan):

  | Subjek | First Name | Last Name | Email | Employee ID | Position | Division | Tampil di kolom User |
  |---|---|---|---|---|---|---|---|
  | John | `John` | `Doe {runId}-017` | `Fixture.activityLog.john017.email` (ditetapkan tim FE, fixture baru) | `EMP001-{runId}-017` | `Staff {runId}-017` | `Marketing {runId}-017` | `John D` |
  | Budi | `Budi` | `Anwar {runId}-017` | `Fixture.activityLog.budi017.email` (ditetapkan tim FE, fixture baru) | `EMP002-{runId}-017` | `Supervisor {runId}-017` | `Finance {runId}-017` | `Budi A` |
  | Siti | `Siti` | `Nurbaya {runId}-017` | `Fixture.activityLog.siti017.email` (ditetapkan tim FE, fixture baru) | tanpa Employee ID | tanpa Position | `Operations {runId}-017` | `Siti N` |

- Data log subjek (entri Session):

  | Subjek | Activity | Status | Note | IP Address | Device / Browser | Cara |
  |---|---|---|---|---|---|---|
  | John | Login | Success | `Login with password` | dari klien uji | dari klien uji | Aksi nyata: Login dengan password benar |
  | John | Logout | `—` | `Logged out` | dari klien uji | dari klien uji | Aksi nyata: Logout manual |
  | John | Session | `—` | `Session started` | dari klien uji | dari klien uji | Aksi nyata: buka card Global Settings |
  | Budi | Login | Failed | `Incorrect password` | `198.51.100.24` | `Chrome on Windows` | Seed BE |
  | Budi | Reset Password | Failed | `Too many reset attempts` | dari seed | dari seed | Seed BE |
  | Budi | Change Password | Success | `Password changed` | dari klien uji | dari klien uji | Aksi nyata: Change Password di My Profile dengan password lama benar |
  | Budi | Change Password | Failed | `Incorrect current password` | dari klien uji | dari klien uji | Aksi nyata: Change Password di My Profile dengan password lama salah |
  | Siti | Reset Password | Success | `Password reset requested` | `2001:db8::1a` | `Safari on iOS` | Seed BE |

- Data uji TC-GS-ACTLOG-56 (kata kunci per kolom):

  | Kolom | Kata kunci | Baris subjek yang tampil | Baris subjek yang tidak tampil |
  |---|---|---|---|
  | Employee ID | `EMP002` | baris milik Budi | baris milik John (`EMP001-{runId}-017`) |
  | Position | `Supervisor` | baris milik Budi | baris milik John (`Staff {runId}-017`) |
  | Division | `Finance` | baris milik Budi | - |
  | Activity | `Reset Password` | baris Reset Password milik Siti dan Budi | - |
  | Status | `Failed` | baris Login Failed, Reset Password Failed, dan Change Password Failed milik Budi | baris dengan Status tampil `Success` (Login John, Change Password Success Budi, Reset Password Success Siti) |
  | Note | `Incorrect` | baris Note `Incorrect password` dan `Incorrect current password` | - |
  | IP Address | `198.51.100` | baris dengan IP `198.51.100.24` | - |
  | Device / Browser | `Safari` | baris `Safari on iOS` | - |

- Data uji TC-GS-ACTLOG-57 (kata kunci dengan kapitalisasi berbeda dari nilai tersimpan):

  | Kolom | Kata kunci | Baris subjek yang tampil |
  |---|---|---|
  | Employee ID | `emp002` | baris `EMP002-{runId}-017` milik Budi |
  | Position | `SUPERVISOR` | baris `Supervisor {runId}-017` milik Budi |
  | Division | `finance` | baris `Finance {runId}-017` milik Budi |
  | Activity | `RESET PASSWORD` | baris `Reset Password` milik Siti dan Budi |
  | Status | `failed` | baris dengan Status tampil `Failed` milik Budi |
  | Note | `incorrect` | baris Note `Incorrect password` dan `Incorrect current password` |
  | IP Address | `2001:DB8` | baris `2001:db8::1a` milik Siti |
  | Device / Browser | `safari` | baris `Safari on iOS` milik Siti |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dengan IP Address, Device / Browser, dan Note yang tertulis "Seed BE" pada tabel Data log (nilai itu tidak dapat dibentuk dari aksi penguji; tanpa mengarang endpoint); menjalankan aksi Auth dan My Profile sebagai subjek lewat sesi API yang terpisah dari sesi UI aktor; menelusuri semua halaman hasil bila baris subjek tidak berada di halaman pertama.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga user subjek beserta Position dan Division bersuffix milik spec ini. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-56: Search substring pada kolom teks Tab Session

2. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-56 (langkah 2 sampai 5): ketik Search kata kunci kolom, tekan Enter
3. Verifikasi tabel menampilkan baris subjek pada kolom "Baris subjek yang tampil"
4. Verifikasi baris subjek pada kolom "Baris subjek yang tidak tampil" tidak tampil (kolom bertanda `-` dilewati)
5. Kosongkan isi kotak Search (klik `(✕)`), lalu tekan Enter

### TC-GS-ACTLOG-57: Search tidak membedakan huruf besar dan kecil

6. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-57 (langkah 6 sampai 8): ketik Search kata kunci kolom, tekan Enter
7. Verifikasi tabel menampilkan baris subjek pada kolom "Baris subjek yang tampil"
8. Kosongkan isi kotak Search (klik `(✕)`), lalu tekan Enter

### TC-GS-ACTLOG-58: Search pada kolom User memakai kata dari nama depan

9. Ketik Search `john`, tekan Enter
10. Verifikasi baris User `John D` milik John tampil
11. Verifikasi baris User `Budi A` dan `Siti N` milik subjek tidak tampil
12. Ganti isi kotak search dengan `SITI`, tekan Enter
13. Verifikasi baris User `Siti N` milik Siti tampil
14. Verifikasi baris User `John D` dan `Budi A` milik subjek tidak tampil

### TC-GS-ACTLOG-60: Search pada kolom User memakai kata dari nama belakang

15. Ganti isi kotak search dengan `Doe`, tekan Enter
16. Verifikasi baris User `John D` milik John tampil
17. Verifikasi baris User `Budi A` milik Budi tidak tampil
18. Ganti isi kotak search dengan `anwar`, tekan Enter
19. Verifikasi baris User `Budi A` milik Budi tampil
20. Verifikasi baris User `John D` milik John tidak tampil

### TC-GS-ACTLOG-63: Search memangkas spasi di awal dan akhir kata kunci

21. Ganti isi kotak search dengan `  EMP002  ` (spasi di awal dan akhir), tekan Enter
22. Verifikasi hasil identik dengan kata kunci `EMP002` (baris milik Budi tampil)
23. Verifikasi isi kotak Search tetap `  EMP002  `
24. Ganti isi kotak search dengan tiga spasi saja, tekan Enter
25. Verifikasi tabel kembali menampilkan data tanpa saringan pencarian (baris milik John, Budi, dan Siti tampil)

### TC-GS-ACTLOG-64: Satu kata kunci cocok pada beberapa kolom sekaligus

26. Ganti isi kotak search dengan `password`, tekan Enter
27. Verifikasi dua baris Change Password milik Budi tampil
28. Verifikasi dua baris Reset Password (milik Budi dan Siti) tampil
29. Verifikasi baris Login Failed (Note `Incorrect password`) tampil
30. Verifikasi baris Login Success (Note `Login with password`) tampil
31. Verifikasi baris Session (`Session started`) dan baris Logout (`Logged out`) milik John tidak tampil

### Pemulihan state antar TC

32. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Search Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-72 (Search lalu Filter, bergantung pada TC-GS-ACTLOG-58) ada di spec 019.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 8 (kosongkan Search dan tekan Enter, sesuai TC-GS-ACTLOG-56 langkah 1; di TC-GS-ACTLOG-57 dipakai sebagai pemulihan antar baris) dan langkah 32 (menutup Search di akhir spec; hook `after` sebagai cadangan). "Ketik Search" membuka kotak Search bila tertutup (8b butir 9); kotak tetap terbuka dan fokus setelah `(✕)` sesuai TC-GS-ACTLOG-65 butir d.
- Langkah 2 sampai 5 dan 6 sampai 8 berulang untuk setiap baris tabel Data uji di Prerequisites.
- Spec memiliki 32 langkah nominal dan 81 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (Search Tab Session pada akun dan dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, dan ekspansi berasal dari dua perulangan per kolom data (TC-GS-ACTLOG-56 dan 57) tanpa langkah bersyarat.
- Temuan untuk QA:
  - Tabel Tab Session entitas Client A memuat log dari spec dan run lain, sedangkan Expected TC ditulis seolah hanya data TC yang ada. Semua asersi "tampil" dan "tidak tampil" dibatasi pada baris subjek spec ini (nama bersuffix).
  - TC-GS-ACTLOG-56 sampai 64 menulis nama subjek literal (`John Doe`, `Budi Anwar`, `Siti Nurbaya`) dan Employee ID `EMP002`; spec memakai nama dan ID bersuffix per run (S-12), dan asersi singkatan `John D`, `Budi A`, `Siti N` tetap berlaku karena huruf awal nama belakang dipertahankan.
  - Data Dinamis TC memuat Employee ID, Position, dan Division untuk `John Doe` serta Division untuk `Siti Nurbaya`; spec men-seed field yang diasersi dan field wajib pembuatan user (seeding minimal, S-11), dengan satu pengecualian: Employee ID dan Position John juga diisi (`EMP001-{runId}-017`, `Staff {runId}-017`) agar kolom itu punya dua nilai terisi yang distinct (S-11) dan Search `EMP002`/`Supervisor` membedakan Budi dari John. Asersi "baris John tidak tampil" pada TC-GS-ACTLOG-56 langkah 4 adalah asersi tambahan atas alasan itu (S-03).
  - Email akun subjek (`Fixture.activityLog.<subjek>.email`) adalah fixture baru yang ditetapkan tim FE; spec tidak mengarang alamat email.
  - TC-GS-ACTLOG-56 dan 64 mensyaratkan entri Reset Password `Failed` (`Too many reset attempts`) dan IP/Device literal yang tidak dapat dibentuk dari aksi penguji; dicatat sebagai seed BE di Prerequisites.
  - Env baru: `ACTLOG_PASSWORD` dan `ACTLOG_PASSWORD_NEW` belum ada di `.env.example` dan perlu didaftarkan tim FE.
