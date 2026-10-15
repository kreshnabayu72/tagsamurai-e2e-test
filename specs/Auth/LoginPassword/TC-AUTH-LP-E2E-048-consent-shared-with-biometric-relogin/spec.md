---
id: TC-AUTH-LP-E2E-048-consent-shared-with-biometric-relogin
title: "Persetujuan Privacy Policy dari Login with Password Berlaku pada Biometric Re-login"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-160
coverage:
  mobile: automated
---

# Persetujuan Privacy Policy dari Login with Password Berlaku pada Biometric Re-login

## Prerequisites

- Mode: FE+BE.
- Seeding: user dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: aplikasi native Android TAG Samurai Mobile terpasang di perangkat atau emulator; profil biometric re-login aktif untuk user di aplikasi dan verifikasi biometrik dapat disimulasikan (hardware atau emulasi biometrik); versi Privacy Policy aktif lebih baru dari versi yang disetujui user (fixture BE).
- TC-AUTH-LP-160: User `Citra Kirana` (`citrakirana+{runId}-048@qwertysystem.net`) berstatus Activated dan Active dengan profil biometric re-login aktif di aplikasi native Android TAG Samurai Mobile; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini; device terpercaya; bukan login pertama dan tidak idle; tidak memicu MFA; belum login di aplikasi
- TC-AUTH-LP-160 data: Email `citrakirana+{runId}-048@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-160: Persetujuan Privacy Policy dari Login with Password berlaku pada Biometric Re-login

1. Buka layar Login with Password di aplikasi
2. Ketik "citrakirana+{runId}-048@qwertysystem.net" di field Email
3. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
4. Ketuk [Log in] sampai layar Confirm to Continue tampil
5. Centang checkbox persetujuan
6. Ketuk [Continue ➔] sampai Portal — Product Hub tampil
7. Verifikasi aplikasi menuju Portal — Product Hub
8. Logout dari aplikasi
9. Buka aplikasi
10. Ketuk Biometric Re-login
11. Lakukan autentikasi biometrik
12. Verifikasi layar Confirm to Continue tidak tampil
13. Verifikasi aplikasi menuju Portal — Product Hub

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: harness eksternal (prinsip 13d, biometrik). Platform mobile (Android), sehingga hanya `coverage.mobile: automated`.
- Tidak ada langkah penghubung (S-03): logout (langkah spec 8), pembukaan aplikasi (langkah spec 9), dan ketuk Biometric Re-login (langkah spec 10) adalah langkah TC-AUTH-LP-160 sendiri (langkah TC 4).
- Temuan untuk QA:
  - TC-AUTH-LP-160 langkah TC 4 menyebut "ketuk Biometric Re-login" tanpa nama elemen UI yang pasti (tombol atau tautan) dan tanpa teks UI persis; spec memakai kata TC apa adanya.
  - TC-AUTH-LP-160 langkah TC 5 ("Verifikasi dengan biometrik") tidak menyebut cara menyimulasikan biometrik di lingkungan uji; dicatat sebagai kemampuan teknis di Prerequisites.
  - TC-AUTH-LP-160 Post Condition (persetujuan Privacy Policy tersimpan untuk versi aktif) tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition itu hanya terpenuhi lewat tindakan di langkah spec 5 dan 6 (centang checkbox persetujuan, ketuk [Continue ➔]) dan teramati tidak langsung lewat langkah spec 12 dan 13 (layar Confirm to Continue tidak tampil pada Biometric Re-login).
  - Precondition TC-AUTH-LP-160 tidak menyebut cara profil biometric re-login diaktifkan; dianggap fixture yang disiapkan tim BE atau FE.
