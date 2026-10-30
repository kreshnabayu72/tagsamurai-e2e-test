---
id: TC-GS-ACTLOG-E2E-021-filter-tab-session-opsi-dari-data-pencarian-opsi-dan-chip-muncul
title: "Filter Tab Session: Opsi dari Data, Pencarian Opsi, dan Chip Muncul"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-78
  - TC-GS-ACTLOG-81
  - TC-GS-ACTLOG-82
coverage:
  web: automated
---

# Filter Tab Session: Opsi dari Data, Pencarian Opsi, dan Chip Muncul

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (TC-GS-ACTLOG-78): Total Control entitas log-terbatas segar milik spec ini, `Fixture.activityLog.entitasLog021` (fixture baru; entitas dan akun Total Control-nya disediakan tim FE/BE), password `Spectra.env.GS_LIMITLOG_TC_PASSWORD` (env baru; satu password bersama untuk semua akun Total Control entitas log-terbatas, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login dilakukan di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Password tidak ditulis di spec atau fixture.
- Akun aktor kedua (TC-GS-ACTLOG-81 dan 82): Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login lewat langkah Ganti akun eksplisit di `## Test Steps` (langkah 8). Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen untuk akun Client A (lihat suite.md). Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control `entitasLog021` dan halaman Global Settings > Activity Log (kemampuan disediakan tim FE/BE).
- Akun subjek log (Client A): tiga user uji pada Data Dinamis dibuat lewat API di hook `before` dan memakai password uji `Spectra.env.ACTLOG_PASSWORD` (env baru; didaftarkan di tempat yang sama). Login dengan password salah memakai `Spectra.env.LP_PASSWORD_WRONG`. `{runId}` hanya digit.
- Data entitas log-terbatas `entitasLog021` (di-seed di hook `before`, bukan di Test Steps; nama literal karena entitas segar milik spec ini): log Session hanya milik User `John Doe` dan `Budi Anwar` (master User juga memuat `Siti Nurbaya` yang belum pernah login); Position `Staff` dan `Supervisor` (master memuat `Finance Manager` yang belum dipakai); Division `Marketing` dan `Finance`; Activity `Login` dan `Logout` milik kedua user tersebut, tanpa `Reset Password` dan `Change Password`; Status hanya `Success` pada entri `Login` dan `Logout`. Akun Total Control penguji entitas ini adalah salah satu dari `John Doe` atau `Budi Anwar` (ditetapkan tim FE) sehingga baris Login dan Session penguji tidak menambah nama User baru.
- Efek pada `entitasLog021`: login akun penguji di hook `before`, pembukaan halaman, dan Logout di langkah 7 menambah baris Login, Session, dan Logout pada entitas itu. Baris log tidak dapat dihapus; entitas milik spec ini sehingga tidak memengaruhi spec lain. Opsi Activity yang diasersi (`Login`, `Logout`) tercakup oleh baris itu, dan `Session` tidak diasersi.
- Data Dinamis Client A (sufiks `{runId}-021`; nama opsi User di Filter Panel adalah nama lengkap):

  | Subjek | First Name | Last Name | Email | Position | Division |
  |---|---|---|---|---|---|
  | John Doe | `John` | `Doe {runId}-021` | `Fixture.activityLog.johnDoe021.email` (ditetapkan tim FE, fixture baru) | `Staff {runId}-021` | `Marketing {runId}-021` |
  | John Dalton | `John` | `Dalton {runId}-021` | `Fixture.activityLog.johnDalton021.email` (ditetapkan tim FE, fixture baru) | `Staff {runId}-021` | `Marketing {runId}-021` |
  | Budi Anwar | `Budi` | `Anwar {runId}-021` | `Fixture.activityLog.budi021.email` (ditetapkan tim FE, fixture baru) | `Supervisor {runId}-021` | `Finance {runId}-021` |

- Data log subjek Client A (entri Session; membentuk opsi Activity `Login`, `Logout`, `Reset Password` dan opsi Status `Success`, `Failed`):

  | Subjek | Activity | Status | Cara |
  |---|---|---|---|
  | John Doe | Login | Success | Aksi nyata: Login dengan password benar |
  | John Doe | Logout | `—` | Aksi nyata: Logout manual |
  | John Dalton | Login | Success | Aksi nyata: Login dengan password benar |
  | Budi Anwar | Login | Failed | Aksi nyata: Login dengan password salah |
  | Budi Anwar | Reset Password | Success | Aksi nyata: permintaan Reset Password dari halaman Login |

- Data uji TC-GS-ACTLOG-78 (entitas log-terbatas):

  | Field | Opsi yang tampil | Opsi yang tidak tampil |
  |---|---|---|
  | User | `John Doe`, `Budi Anwar` | `Siti Nurbaya` |
  | Position | `Staff`, `Supervisor` | `Finance Manager` |
  | Division | `Marketing`, `Finance` | Division master lain |
  | Activity | `Login`, `Logout` | `Reset Password`, `Change Password` |
  | Status | `Success` | `Failed` |

- Data uji TC-GS-ACTLOG-81 (Client A):

  | Field | Kata kunci | Opsi yang tampil | Opsi yang tidak tampil |
  |---|---|---|---|
  | User | `jo` | `John Doe {runId}-021`, `John Dalton {runId}-021` | `Budi Anwar {runId}-021` |
  | Position | `sup` | `Supervisor {runId}-021` | `Staff {runId}-021` |
  | Division | `fin` | `Finance {runId}-021` | `Marketing {runId}-021` |
  | Activity | `log` | `Login`, `Logout` | `Reset Password` |
  | Status | `fail` | `Failed` | `Success` |

- Data uji TC-GS-ACTLOG-82 (Client A):

  | Field | Opsi pertama | Opsi kedua |
  |---|---|---|
  | User | `John Doe {runId}-021` | `Budi Anwar {runId}-021` |
  | Position | `Staff {runId}-021` | `Supervisor {runId}-021` |
  | Division | `Marketing {runId}-021` | `Finance {runId}-021` |
  | Activity | `Login` | `Logout` |
  | Status | `Success` | `Failed` |

- Kemampuan teknis (disediakan tim FE/BE): entitas log-terbatas `entitasLog021` dengan log Session sesuai Data entitas di atas, di-seed di hook `before`; menjalankan aksi Auth sebagai subjek Client A lewat sesi API yang terpisah dari sesi UI aktor; mengganti akun aktor di tengah spec.
- State global: hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Filter tab Session dikosongkan di langkah 22. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga user subjek Client A beserta Position dan Division bersuffix milik spec ini. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-78: Isi opsi filter Tab Session bersumber dari data tabel

2. Klik icon Filter
3. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-78 (langkah 3 sampai 6): buka daftar opsi field
4. Verifikasi opsi pada kolom "Opsi yang tampil" tampil di daftar opsi
5. Verifikasi opsi pada kolom "Opsi yang tidak tampil" tidak tampil di daftar opsi
6. Verifikasi tidak ada opsi `None` pada daftar opsi field

### Ganti akun

7. Klik icon Filter untuk menutup Filter Panel, lalu Logout dari akun entitas log-terbatas
8. Login sebagai Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, lalu buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-81: Pencarian di dalam field multi-select Tab Session

9. Klik icon Filter
10. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-81 (langkah 10 sampai 16): buka field, ketik kata kunci di kotak pencarian field
11. Verifikasi opsi pada kolom "Opsi yang tampil" tampil di daftar opsi
12. Verifikasi opsi pada kolom "Opsi yang tidak tampil" tidak tampil di daftar opsi
13. Ganti kata kunci di kotak pencarian field dengan `zzz`
14. Verifikasi tidak ada opsi yang tampil
15. Verifikasi tidak ada pesan error
16. Kosongkan isi kotak pencarian field (hapus teks), lalu tutup daftar opsi

### TC-GS-ACTLOG-82: Chip opsi terpilih muncul di dalam field multi-select Tab Session

17. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-82 (langkah 17 sampai 21): buka field, centang opsi pertama, lalu tutup daftar opsi
18. Verifikasi satu chip berlabel opsi pertama muncul di dalam field
19. Buka field, centang opsi kedua, lalu tutup daftar opsi
20. Verifikasi chip kedua muncul di samping chip pertama
21. Verifikasi chip pertama tidak digantikan oleh chip kedua

### Pemulihan state akhir

22. Klik `[Clear Field]`

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Filter Panel Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-83, 84, dan 85 (bergantung pada TC-GS-ACTLOG-82) ada di spec 022.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menutup Filter Panel), langkah 16 (mengosongkan pencarian field dan menutup daftar opsi sebelum TC-GS-ACTLOG-82), dan langkah 22 (membersihkan state di akhir spec; hook `after` sebagai cadangan). Langkah 17 dan langkah sesudah centang opsi kedua menutup daftar opsi karena TC-GS-ACTLOG-82 mengamati field dalam keadaan tertutup.
- Langkah 7 dan 8 adalah Ganti akun eksplisit (S-07). Penggabungan TC-GS-ACTLOG-78 dengan TC-GS-ACTLOG-81 dan 82 dalam satu spec: bagian sesudah Ganti akun (TC-GS-ACTLOG-81 dan 82) tetap bermakna walau TC-GS-ACTLOG-78 gagal karena hanya memakai data Client A milik spec ini, sedangkan TC-GS-ACTLOG-78 tidak membuat data. Kegagalan keras hook `before` untuk seeding Client A menutupi hasil TC-GS-ACTLOG-78.
- Langkah 3 sampai 6, 10 sampai 16, dan 17 sampai 21 berulang untuk setiap baris tabel Data uji di Prerequisites.
- Spec memiliki 22 langkah nominal dan 86 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: TC-GS-ACTLOG-78 berakun entitas log-terbatas, TC-GS-ACTLOG-81 dan 82 berakun Client A dan dipisahkan Step Ganti akun eksplisit; ketiga blok memakai Filter Panel Tab Session dan ekspansi berasal dari tiga perulangan per field tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun subjek (`Fixture.activityLog.<subjek>.email`) adalah fixture baru yang ditetapkan tim FE; spec tidak mengarang alamat email.
  - TC-GS-ACTLOG-78 mensyaratkan entitas dengan log Session terbatas (Tabel Data Uji Pre-setup baris 13) yang berbeda dari entitas TC-GS-ACTLOG-81 dan 82; `Fixture.activityLog.entitasLog021` dan env `GS_LIMITLOG_TC_PASSWORD` belum ada di `.env.example` dan perlu disediakan tim FE/BE (env baru, bersama untuk semua akun Total Control entitas log-terbatas). Spec memakai Ganti akun untuk berpindah entitas.
  - TC-GS-ACTLOG-78 tidak menyebut identitas akun penguji entitas; baris Login, Session, dan Logout akun penguji tercatat di entitas yang sama. Spec mensyaratkan akun penguji salah satu pemilik log (`John Doe` atau `Budi Anwar`).
  - TC-GS-ACTLOG-78 Expected butir c menyebut "Division master lain tidak tampil" tanpa nama; spec memakai kalimat itu apa adanya.
  - Entitas Client A memuat opsi dari log spec dan run lain; asersi opsi pada TC-GS-ACTLOG-81 dibatasi pada opsi subjek spec ini (nama bersuffix, S-12). Nama literal TC (`John Doe`, `John Dalton`, `Budi Anwar`, `Supervisor`, `Staff`, `Finance`, `Marketing`) diganti nama bersuffix per run.
  - TC-GS-ACTLOG-81 Expected butir f menyebut "tidak ada opsi yang tampil dan tidak ada pesan error"; PRD (prd-conventions.md §9.8) mendefinisikan teks `No results found` untuk pencarian dropdown tanpa kecocokan, sehingga teks itu tidak diasersi di spec.
  - Env baru: `ACTLOG_PASSWORD` belum ada di `.env.example` dan perlu didaftarkan tim FE.
