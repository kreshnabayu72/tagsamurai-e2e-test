---
id: TC-GS-ACTLOG-E2E-008-ganti-bahasa-kolom-verbatim-dan-translatable
title: "Ganti Bahasa: Kolom Verbatim dan Translatable"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-27
coverage:
  web: automated
---

# Ganti Bahasa: Kolom Verbatim dan Translatable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Password user uji: `Spectra.env.ACTLOG_PASSWORD` untuk mengaktifkan user uji; password salah untuk login gagal: `Spectra.env.LP_PASSWORD_WRONG`.
- Data Pre-setup: tidak ada selain akun aktor.
- Data Dinamis (suffix `{runId}-008`, dibuat di hook `before` lewat API oleh Total Control Client A):
  - Position `Position Bahasa {runId}-008` dan Division `Division Bahasa {runId}-008`.
  - User `Uji Bahasa {runId}-008`, email `ujibahasa+{runId}-008@qwertysystem.net`, Employee ID `EMP-{runId}-008`, Position dan Division di atas, diaktivasi dengan `Spectra.env.ACTLOG_PASSWORD`.
  - Satu baris Session `Login` `Failed` milik user uji, dihasilkan di hook `before` lewat sesi API (percobaan login dengan password salah `Spectra.env.LP_PASSWORD_WRONG`).
  - Brand `Brand Bahasa {runId}-008` dibuat lalu di-rename menjadi `Brand Bahasa {runId}-008 Rename` oleh Total Control Client A lewat API; dari aksi rename ini terbentuk baris User Action `Edit` (Object `Brand`, Field `Name`, Modified By aktor).
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Brand, user uji, Position, dan Division milik spec ini lewat API. Baris log tidak dapat dihapus (append-only).
- Bahasa: Language picker akun penguji berisi bahasa non-Inggris yang tersedia; bahasa dipilih tim FE (TC tidak menyebut nama bahasa). Hook `before` menyetel bahasa akun penguji ke Inggris; hook `after` mengembalikan bahasa awal.
- State global yang diubah, dipulihkan di hook `after`: General Settings Date Format diset ke `DD/MM/YY` di hook `before` (kemampuan menyetel Date Format General Settings disediakan tim FE/BE tanpa endpoint yang dikarang di spec ini) dan bahasa akun penguji.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-27: Ganti bahasa, kolom verbatim tetap, kolom translatable ikut bahasa

1. Buka Global Settings > Activity Log > Session dalam bahasa Inggris
2. Ketik Search `EMP-{runId}-008`, tekan Enter
3. Catat nilai baris Login Failed milik user uji pada kolom Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device / Browser
4. Ganti bahasa lewat Language picker ke bahasa non-Inggris
5. Ganti isi kotak search dengan `EMP-{runId}-008`, tekan Enter, lalu amati baris yang sama
6. Verifikasi tab Session setelah ganti bahasa: nilai kolom Date, User, Employee ID, Position, Division, IP Address, Device / Browser identik dengan sebelum ganti bahasa
7. Verifikasi tab Session setelah ganti bahasa: format tanggal kolom Date tidak berubah (`DD/MM/YY`)
8. Verifikasi tab Session setelah ganti bahasa: nilai kolom Activity, Status, Note tampil dalam bahasa pilihan, bukan lagi teks Inggris asli
9. Kembalikan bahasa ke Inggris lewat Language picker
10. Klik tab "User Action"
11. Ketik Search `Brand Bahasa {runId}-008 Rename`, tekan Enter
12. Catat nilai baris Edit milik Brand tersebut pada kolom Date, Action, Object, Name, Field, Old Value, New Value, Modified By (bahasa Inggris)
13. Ganti bahasa lewat Language picker ke bahasa non-Inggris
14. Ganti isi kotak search dengan `Brand Bahasa {runId}-008 Rename`, tekan Enter, lalu amati baris yang sama
15. Verifikasi tab User Action setelah ganti bahasa: nilai kolom Date, Name, Old Value, New Value, Modified By identik dengan sebelum ganti bahasa
16. Verifikasi tab User Action setelah ganti bahasa: nilai kolom Action, Object, Field tampil dalam bahasa pilihan, bukan lagi teks Inggris asli
17. Kembalikan bahasa ke Inggris lewat Language picker

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-27). Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 2, 5, 11, dan 14 (Search dengan Employee ID atau Name bersuffix untuk menemukan baris milik run ini; pencarian diulang setelah ganti bahasa agar baris yang sama diamati; langkah 5 dan 14 mengasumsikan kotak Search tetap terbuka dan berisi keyword setelah ganti bahasa, sedangkan kotak Search tab User Action belum terbuka sebelum langkah 11), 9 dan 17 (mengembalikan bahasa ke Inggris; lihat Temuan untuk QA), 10 (pindah ke tab User Action).
- Langkah 7 mengasersi butir "format tanggal tidak berubah" yang ada di Expected a TC-27 sebagai klausa terpisah dari kesamaan nilai kolom (S-01).
- Temuan untuk QA:
  - TC-27 langkah 3 mencatat nilai tab User Action "(bahasa Inggris)" lalu "ganti bahasa lagi", padahal langkah 2 sudah memindahkan akun ke bahasa non-Inggris. Spec mengembalikan bahasa ke Inggris (langkah 9) sebelum mencatat nilai User Action, lalu mengganti ke bahasa non-Inggris (langkah 13).
  - TC-27 tidak menyebut bahasa non-Inggris yang dipilih dan teks terjemahan Activity, Status, Note, Action, Object, Field; asersi "bukan lagi teks Inggris asli" dibandingkan dengan nilai yang dicatat pada bahasa Inggris, bukan dengan teks terjemahan literal.
  - Cara menyetel General Settings Date Format `DD/MM/YY` untuk precondition tidak didefinisikan di TC; kemampuan itu diminta dari tim FE/BE.
  - TC-27 tidak menyebut keadaan kotak Search setelah ganti bahasa; spec mengasumsikan kotak tetap terbuka dan berisi keyword (langkah 5 dan 14).
  - `ACTLOG_PASSWORD` belum terdaftar di `.env.example`; didaftarkan tim FE.
