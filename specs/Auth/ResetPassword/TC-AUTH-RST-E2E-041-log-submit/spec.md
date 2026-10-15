---
id: TC-AUTH-RST-E2E-041-log-submit
title: "Pencatatan Submit: Policy Gagal, Sama dengan Password Lama, dan Sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-98
  - TC-AUTH-RST-101
  - TC-AUTH-RST-99
coverage:
  web: automated
---

# Pencatatan Submit: Policy Gagal, Sama dengan Password Lama, dan Sukses

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-041@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`; satu token reset aktif diterbitkan di hook `before` lewat API Request, tautan dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`.
- Kemampuan teknis: mail-catcher; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Global Settings > Activity Log > Session dan Global Settings > User > Detail > User Log).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-98, 101, 99: aksi submit oleh guest (browser web) pada satu token; admin pengamat log pada jendela terpisah.
- TC-AUTH-RST-98 data: Password dan Confirm Password `abc` (literal; submit diblokir server).
- TC-AUTH-RST-101 data: Password dan Confirm Password `Spectra.env.RST_PASSWORD` (sama dengan password lama).
- TC-AUTH-RST-99 data: Password dan Confirm Password `Spectra.env.RST_PASSWORD_NEW`.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA)

### TC-AUTH-RST-98: Submit yang melanggar kebijakan tercatat Failed / Password does not meet requirements

2. Pindah ke jendela admin, buka Global Settings > Activity Log > Session lalu terapkan Filter Activity = "Reset Password"
3. Buka Global Settings > User > Detail > User Log untuk user "Budi Santoso" lalu catat jumlah baris dan entri teratas kedua surface sebagai baseline B1
4. Pindah ke jendela guest lalu buka tautan reset milik `budisantoso+{runId}-041@qwertysystem.net` dari mail-catcher
5. Ketik "abc" pada field Password dan field Confirm Password lalu klik Button [Reset Password]
6. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Budi Santoso"
7. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B1
8. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Failed, Note `Password does not meet requirements`

### TC-AUTH-RST-101: Submit dengan password sama dengan password lama

9. Catat jumlah baris dan entri teratas Activity Log Session dan User Log user "Budi Santoso" sebagai baseline B2 (sudah memuat entri dari langkah 5)
10. Pindah ke jendela guest, kosongkan field Password dan Confirm Password lalu ketik `Spectra.env.RST_PASSWORD` pada kedua field dan klik Button [Reset Password]
11. Pindah ke jendela admin, muat ulang Activity Log Session dengan Filter Activity = "Reset Password", dan muat ulang User Log user "Budi Santoso"
12. Verifikasi jumlah baris pada kedua surface bertambah tepat satu dibanding baseline B2
13. Verifikasi entri baru pada kedua surface: Activity `Reset Password`, Status Failed, Note `Password does not meet requirements`

### TC-AUTH-RST-99: Submit sukses tercatat Success / Password updated successfully

14. Catat jumlah baris dan entri teratas Activity Log Session dan User Log user "Budi Santoso" sebagai baseline B3
15. Pindah ke jendela guest, kosongkan field Password dan Confirm Password lalu ketik `Spectra.env.RST_PASSWORD_NEW` pada kedua field dan klik Button [Reset Password]
16. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Budi Santoso"
17. Verifikasi ada entri baru di atas baseline B3 pada kedua surface: Activity `Reset Password`, Status Success, Note `Password updated successfully`

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Submit sukses paling akhir karena mengonsumsi token; dua penolakan memakai token yang sama.
- Entri logout per sesi yang berakhir (`Logout`, `Logged out (password changed)`) ditulis oleh Session Management dan tidak diasersi di sini (sesuai Expected TC-AUTH-RST-99 butir b). Langkah 17 tidak menyatakan "tepat satu" karena sesi yang berakhir dapat menambah entri milik modul lain di log yang sama.
- Aksi penolakan policy dan sama-dengan-lama juga dipicu di spec `TC-AUTH-RST-E2E-027-server-rejection-then-success` (dengan asersi log langsung); spec ini mengulang aksi tersebut untuk TC log (TC-AUTH-RST-98 dan 101) sesuai dependensi TC sumber.
- Temuan untuk QA: TC-AUTH-RST-101 hanya memuat langkah untuk Activity Log Session (Steps 1) tetapi Expected menyebut kedua surface, dan langkah memuat ulang User Log tidak ada di TC. Spec mengikuti Expected: User Log user "Budi Santoso" dimuat ulang pada langkah 11 sebelum diasersi; usulan: tambah langkah 2 (User Log) di TC-AUTH-RST-101 (S-15).
- Temuan untuk QA: TC-AUTH-RST-98 dan 101 tidak punya Post Condition; entri identik (Failed / `Password does not meet requirements`) muncul dua kali, sehingga baseline B1 dan B2 diperlukan agar entri TC-AUTH-RST-101 tidak lulus karena entri TC-AUTH-RST-98 (S-12).
- Langkah penghubung (S-03): langkah 1 (persiapan jendela), pindah antar jendela admin dan guest, serta pengosongan field Password dan Confirm Password sebelum mengetik ulang.
