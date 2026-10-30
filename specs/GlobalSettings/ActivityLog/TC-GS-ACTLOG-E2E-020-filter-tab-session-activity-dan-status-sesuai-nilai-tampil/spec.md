---
id: TC-GS-ACTLOG-E2E-020-filter-tab-session-activity-dan-status-sesuai-nilai-tampil
title: "Filter Tab Session: Activity dan Status Sesuai Nilai Tampil"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-68
  - TC-GS-ACTLOG-69
coverage:
  web: automated
---

# Filter Tab Session: Activity dan Status Sesuai Nilai Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before`, lalu halaman awal Global Settings > Activity Log > Session. Environment variable: `GS_TC_PASSWORD`.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun subjek log: dua user uji pada Data Dinamis dibuat lewat API di hook `before` dan memakai password uji `Spectra.env.ACTLOG_PASSWORD` (env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Password aksi subjek: Login dengan password salah dan password lama yang salah pada Change Password memakai `Spectra.env.LP_PASSWORD_WRONG`; Change Password Budi dengan password lama benar memakai `Spectra.env.ACTLOG_PASSWORD` dan password baru `Spectra.env.ACTLOG_PASSWORD_NEW` (env baru, didaftarkan di tempat yang sama). Urutan di hook `before` untuk Budi: Login password salah, Change Password dengan password lama salah (password tetap `ACTLOG_PASSWORD`), lalu Change Password dengan password lama benar (password menjadi `ACTLOG_PASSWORD_NEW`). Tidak ada login Budi sesudahnya.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (sufiks `{runId}-020`, `{runId}` hanya digit; hanya field wajib pembuatan user yang di-seed):

  | Subjek | First Name | Last Name | Email | Division | Tampil di kolom User |
  |---|---|---|---|---|---|
  | John | `John` | `Doe {runId}-020` | `Fixture.activityLog.john020.email` (ditetapkan tim FE, fixture baru) | `Marketing {runId}-020` | `John D` |
  | Budi | `Budi` | `Anwar {runId}-020` | `Fixture.activityLog.budi020.email` (ditetapkan tim FE, fixture baru) | `Finance {runId}-020` | `Budi A` |

- Data log subjek (entri Session):

  | Subjek | Activity | Status tampil | Status internal | Note | Cara |
  |---|---|---|---|---|---|
  | Budi | Change Password | `Success` | Success | `Password changed` | Aksi nyata: Change Password di My Profile dengan password lama benar |
  | Budi | Change Password | `Failed` | Failed | `Incorrect current password` | Aksi nyata: Change Password di My Profile dengan password lama salah |
  | Budi | Login | `Failed` | Failed | `Incorrect password` | Aksi nyata: Login dengan password salah |
  | John | Session | `—` | Success | `Session started` | Aksi nyata: buka card Global Settings |
  | John | Session | `—` | Failed | `Session ended` | Seed BE |
  | John | Logout | `—` | Failed | `Logged out (new device login)` | Seed BE |

- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dan Logout dengan `status` internal Failed (nilai itu tidak dapat dibentuk dari aksi penguji; tanpa mengarang endpoint); menjalankan aksi Auth dan My Profile sebagai subjek lewat sesi API yang terpisah dari sesi UI aktor; menelusuri semua halaman hasil bila baris subjek tidak berada di halaman pertama.
- State global: Filter tab Session dikosongkan di akhir spec (langkah 15 dan 16). Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedua user subjek beserta Division bersuffix milik spec ini. Entri Session tidak dapat dihapus dan tetap ada sebagai snapshot.

## Test Steps

1. Buka Global Settings > Activity Log > Session

### TC-GS-ACTLOG-68: Filter Activity Change Password dan Session menampilkan Status sesuai nilai tampil

2. Klik icon Filter, lalu pilih Activity `Change Password`
3. Klik `[Apply]`
4. Verifikasi hanya dua baris Change Password milik Budi yang tampil
5. Verifikasi Status kedua baris Change Password adalah `Success` dan `Failed` (bukan `—`)
6. Verifikasi Note kedua baris adalah `Password changed` dan `Incorrect current password`
7. Klik `[Clear Field]`, lalu pilih Activity `Session`
8. Klik `[Apply]`
9. Verifikasi hanya baris `Session started` dan `Session ended` milik John yang tampil
10. Verifikasi Status kedua baris Session adalah `—`

### TC-GS-ACTLOG-69: Filter Status mengikuti nilai yang tampil, Logout dan Session tidak cocok dengan Success maupun Failed

11. Klik `[Clear Field]`, lalu pilih Status `Failed`
12. Klik `[Apply]`
13. Verifikasi baris Login `Failed` milik Budi tampil
14. Verifikasi baris Logout `Logged out (new device login)` dan baris Session `Session ended` milik John tidak tampil

### Pemulihan state akhir

15. Klik `[Clear Field]`
16. Klik `[Apply]`

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (bagian Filter Panel Tab Session). Semua TC sumber spec ini dikerjakan di sini; TC-GS-ACTLOG-66 (prasyarat TC-GS-ACTLOG-68) ada di spec 019.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11 (membersihkan Activity `Session` dari TC-GS-ACTLOG-68 sebelum TC-GS-ACTLOG-69) serta langkah 15 dan 16 (membersihkan Filter di akhir spec; hook `after` sebagai cadangan). Langkah 7 mengikuti urutan TC-GS-ACTLOG-68 langkah 2.
- Temuan untuk QA:
  - Email akun subjek (`Fixture.activityLog.<subjek>.email`) adalah fixture baru yang ditetapkan tim FE; spec tidak mengarang alamat email.
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 2 mengikuti TC-GS-ACTLOG-68.
  - Tabel Tab Session entitas Client A memuat log dari spec dan run lain, sedangkan Expected TC ("hanya dua baris", "hanya baris ... tampil") ditulis seolah hanya data TC yang ada. Asersi dibatasi pada baris subjek spec ini (nama bersuffix, Note `Password changed` dan `Incorrect current password` milik Budi).
  - Nama subjek literal TC (`John Doe`, `Budi Anwar`) diganti nama bersuffix per run (S-12); singkatan `John D`, `Budi A` tetap sama.
  - TC-GS-ACTLOG-68 menulis entri `Session ended` tanpa `status` internal, sedangkan TC-GS-ACTLOG-69 menyebut `status` internalnya Failed; spec memakai satu entri `Session ended` dengan `status` internal Failed (seed BE) untuk kedua TC.
  - TC-GS-ACTLOG-68 butir c menyebut entri Login milik John; Login John terjadi sebagai bagian aksi nyata membuka card Global Settings dan tidak diasersi karena Expected TC-GS-ACTLOG-68 dan 69 tidak memintanya.
  - Perilaku `[Apply]` pada Filter Panel (panel menutup atau tetap terbuka) belum ditetapkan PRD: TC-GS-ACTLOG-68 menekan `[Clear Field]` tanpa membuka ulang Filter Panel sesudah `[Apply]` (langkah 7 dan 11). Spec mengikuti urutan langkah TC apa adanya.
  - Env baru: `ACTLOG_PASSWORD` dan `ACTLOG_PASSWORD_NEW` belum ada di `.env.example` dan perlu didaftarkan tim FE.
