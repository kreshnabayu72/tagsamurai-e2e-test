---
id: TC-GS-ACTLOG-E2E-022-filter-tab-session-hapus-chip-hapus-centang-dan-overflow-chip
title: "Filter Tab Session: Hapus Chip, Hapus Centang, dan Overflow Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-83
  - TC-GS-ACTLOG-84
  - TC-GS-ACTLOG-85
coverage:
  web: automated
---

# Filter Tab Session: Hapus Chip, Hapus Centang, dan Overflow Chip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun subjek log: delapan user uji pada Data Dinamis dibuat lewat API di hook `before` dan memakai password uji `Spectra.env.ACTLOG_PASSWORD` (env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login dengan password salah (Budi Anwar) memakai `Spectra.env.LP_PASSWORD_WRONG`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (sufiks `{runId}-022`, `{runId}` hanya digit; nama opsi User di Filter Panel adalah nama lengkap):

  | Subjek | First Name | Last Name | Email | Position | Division |
  |---|---|---|---|---|---|
  | John Doe | `John` | `Doe {runId}-022` | `Fixture.activityLog.johnDoe022.email` (ditetapkan tim FE, fixture baru) | `Staff {runId}-022` | `Marketing {runId}-022` |
  | Budi Anwar | `Budi` | `Anwar {runId}-022` | `Fixture.activityLog.budi022.email` (ditetapkan tim FE, fixture baru) | `Supervisor {runId}-022` | `Finance {runId}-022` |
  | Chip 1 sampai Chip 6 (enam user, n = 1 sampai 6) | `Chip` | `Uji{n} {runId}-022` | `Fixture.activityLog.chip{n}022.email` (ditetapkan tim FE, fixture baru) | `Chip Posisi {n} {runId}-022` | `Chip Divisi {n} {runId}-022` |

- Data log subjek (entri Session; membentuk opsi filter yang dipakai):

  | Subjek | Activity | Status | Cara |
  |---|---|---|---|
  | John Doe | Login | Success | Aksi nyata: Login dengan password benar |
  | John Doe | Logout | `—` | Aksi nyata: Logout manual |
  | Budi Anwar | Login | Failed | Aksi nyata: Login dengan password salah |
  | Chip 1 sampai Chip 6 | Login | Success | Aksi nyata: Login dengan password benar (satu entri per user, agar keenam opsi User, Position, dan Division muncul di Filter Panel) |

- Data uji TC-GS-ACTLOG-83 dan 84 (dua opsi per field):

  | Field | Opsi pertama | Opsi kedua | Baris subjek yang tampil setelah [Apply] (hanya opsi kedua) | Baris subjek yang tidak tampil setelah [Apply] |
  |---|---|---|---|---|
  | User | `John Doe {runId}-022` | `Budi Anwar {runId}-022` | baris Login Failed milik Budi | semua baris milik John |
  | Position | `Staff {runId}-022` | `Supervisor {runId}-022` | baris Login Failed milik Budi | semua baris milik John |
  | Division | `Marketing {runId}-022` | `Finance {runId}-022` | baris Login Failed milik Budi | semua baris milik John |
  | Activity | `Login` | `Logout` | baris Logout milik John | baris Login milik John dan Budi |
  | Status | `Success` | `Failed` | baris Login Failed milik Budi | baris Login Success milik John |

- Data uji TC-GS-ACTLOG-85 (enam opsi per field):

  | Field | Kata kunci di kotak pencarian field | Enam opsi yang dipilih |
  |---|---|---|
  | User | `Chip` | `Chip Uji1 {runId}-022` sampai `Chip Uji6 {runId}-022` |
  | Position | `Chip Posisi` | `Chip Posisi 1 {runId}-022` sampai `Chip Posisi 6 {runId}-022` |
  | Division | `Chip Divisi` | `Chip Divisi 1 {runId}-022` sampai `Chip Divisi 6 {runId}-022` |

- Kemampuan teknis (disediakan tim FE/BE): menjalankan aksi Auth sebagai subjek lewat sesi API yang terpisah dari sesi UI aktor; membaca jumlah chip yang tampil pada field dan nilai `N` pada ringkasan `+N more`; mengukur bahwa field tidak melebar keluar Filter Panel; menelusuri semua halaman hasil bila baris subjek tidak berada di halaman pertama.
- State global: Filter tab Session dikosongkan di langkah 9, 18, 19, dan 25. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedelapan user subjek beserta Position dan Division bersuffix milik spec ini. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-83: Hapus chip lewat (X) menghapus centang opsi

2. Klik icon Filter
3. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-83 (langkah 3 sampai 8): pilih opsi pertama dan opsi kedua pada field
4. Klik icon `(X)` pada chip pertama tanpa membuka daftar opsi
5. Buka daftar opsi field
6. Verifikasi chip pertama hilang dari field
7. Verifikasi centang opsi pertama di daftar opsi hilang
8. Verifikasi chip kedua tetap ada di field

### Pemulihan state antar TC

9. Klik `[Clear Field]`

### TC-GS-ACTLOG-84: Hapus centang di dalam daftar opsi menghapus chip

10. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-84 (langkah 10 sampai 19): pilih opsi pertama dan opsi kedua pada field
11. Buka daftar opsi field, lalu hilangkan centang opsi pertama
12. Verifikasi chip opsi pertama langsung hilang dari field sebelum daftar ditutup
13. Verifikasi chip opsi kedua tetap ada di field
14. Tutup daftar opsi
15. Klik `[Apply]`
16. Verifikasi tabel menampilkan baris subjek pada kolom "Baris subjek yang tampil setelah [Apply]"
17. Verifikasi baris subjek pada kolom "Baris subjek yang tidak tampil setelah [Apply]" tidak tampil
18. Klik `[Clear Field]`
19. Klik `[Apply]`

### TC-GS-ACTLOG-85: Overflow chip banyak opsi terpilih

20. Untuk setiap baris tabel Data uji TC-GS-ACTLOG-85 (langkah 20 sampai 24): buka field, ketik kata kunci di kotak pencarian field, pilih keenam opsi, lalu tutup daftar opsi
21. Verifikasi sebagian chip tampil di dalam field
22. Verifikasi sisa chip diringkas dalam `+N more`
23. Verifikasi jumlah chip yang tampil ditambah N sama dengan 6
24. Verifikasi field tidak melebar keluar panel

### Pemulihan state akhir

25. Klik `[Clear Field]`

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Filter Panel Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-82 (prasyarat ketiga TC) ada di spec 021.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 (membersihkan pilihan field dari TC-GS-ACTLOG-83), langkah 18 dan 19 (membersihkan Filter di tiap iterasi TC-GS-ACTLOG-84 supaya hasil tabel tiap field tidak beririsan dengan field sebelumnya; TC hanya menulis `[Apply]` per field), langkah 14 (menutup daftar opsi sebelum `[Apply]`, sesuai TC-GS-ACTLOG-84 langkah 2), dan langkah 25 (membersihkan state di akhir spec; hook `after` sebagai cadangan). Kata kunci pada langkah 20 mempersempit daftar opsi ke enam opsi milik spec ini karena TC hanya menyebut "pilih 6 opsi".
- Langkah 3 sampai 8, 10 sampai 19, dan 20 sampai 24 berulang untuk setiap baris tabel Data uji di Prerequisites. Langkah 12 dijalankan sebelum langkah 14 (§8b butir 5: state sementara diasersi sebelum daftar ditutup).
- Spec memiliki 25 langkah nominal dan 99 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok memakai Filter Panel Tab Session, akun, dan dataset yang sama; tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna; ekspansi berasal dari tiga perulangan per field tanpa langkah bersyarat.
- Temuan untuk QA:
  - Email akun subjek (`Fixture.activityLog.<subjek>.email`) adalah fixture baru yang ditetapkan tim FE; spec tidak mengarang alamat email.
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 2 mengikuti TC-GS-ACTLOG-83.
  - TC-GS-ACTLOG-84 menulis hasil tabel "hanya mengikuti opsi kedua" tanpa langkah pembersihan antar field; tanpa pembersihan Filter field sebelumnya ikut beririsan (AND), sehingga spec menambah `[Clear Field]` dan `[Apply]` antar iterasi.
  - Perilaku `[Apply]` pada Filter Panel (panel menutup atau tetap terbuka) belum ditetapkan PRD; spec mengikuti urutan langkah TC dan membuka panel sekali di langkah 2.
  - TC-GS-ACTLOG-85 mensyaratkan minimal 6 opsi pada User, Position, dan Division; spec membuat enam user dengan Position dan Division masing-masing serta satu entri Login per user.
  - Entitas Client A memuat log dari spec dan run lain; asersi tabel dibatasi pada baris subjek spec ini (nama bersuffix, S-12). Nama literal TC (`John Doe`, `Budi Anwar`, `Staff`, `Supervisor`, `Marketing`, `Finance`) diganti nama bersuffix per run.
  - Env baru: `ACTLOG_PASSWORD` belum ada di `.env.example` dan perlu didaftarkan tim FE.
