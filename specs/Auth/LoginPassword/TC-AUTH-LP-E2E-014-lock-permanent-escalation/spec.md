---
id: TC-AUTH-LP-E2E-014-lock-permanent-escalation
title: "Eskalasi Lock Permanent setelah 7 Hari Berturut-turut"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-58
  - TC-AUTH-LP-59
  - TC-AUTH-LP-60
coverage:
  web: automated
---

# Eskalasi Lock Permanent setelah 7 Hari Berturut-turut

## Prerequisites

- Mode: FE+BE.
- Seeding: satu user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_WRONG`.
- Kemampuan teknis: fixture BE yang menulis riwayat lock user (7 hari kalender berturut-turut mencapai lock 1 jam); reCAPTCHA mode uji; General Settings entitas memakai Time Zone dan Time Format default. Pemulihan: hook `after` menghapus user. Tidak ada langkah yang mengubah jam (riwayat lock di-seed bertanggal mundur oleh fixture BE).
- TC-AUTH-LP-58: Tanpa login (guest, browser web)
- TC-AUTH-LP-58: User `Eka Surya` (`ekasurya+{runId}-014@qwertysystem.net`) berstatus Activated dan Active, mencapai lock 1 jam pada 7 hari kalender berturut-turut; hari kalender sekarang adalah hari ke-8 dan belum ada percobaan hari itu (di-seed oleh fixture BE)
- TC-AUTH-LP-58 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-59: Tanpa login (guest); user yang sama berstatus Permanent di web (hasil TC-AUTH-LP-58 dalam spec ini) dengan password benar `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-60: Tanpa login (guest); user yang sama berstatus Permanent di web

## Test Steps

### TC-AUTH-LP-58: Salah password pertama di hari ke-8 setelah 7 hari berturut-turut lock 1 jam langsung Permanent

1. Buka halaman Login with Password
2. Isi Email `ekasurya+{runId}-014@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi Alert Danger di atas Button [Log in]: "For security reasons, your account has been locked. Please reset your password to regain access."
6. Verifikasi tautan [Reset password] tampil satu baris di bawah teks Alert
7. Verifikasi Alert lock 15 menit dan lock 1 jam tidak tampil

### TC-AUTH-LP-59: Submit password benar saat status Permanent tetap ditolak

8. Isi Password `Spectra.env.LP_PASSWORD`
9. Selesaikan reCAPTCHA
10. Klik [Log in]
11. Verifikasi Alert Danger "For security reasons, your account has been locked. Please reset your password to regain access." tampil
12. Verifikasi tautan [Reset password] tampil di bawah teks Alert
13. Verifikasi tidak ada sesi dibuat

### TC-AUTH-LP-60: Tautan [Reset password] pada Alert Permanent membuka halaman Reset Password

14. Klik tautan [Reset password] pada Alert
15. Verifikasi halaman Reset Password terbuka
16. Verifikasi field Email terisi "ekasurya+{runId}-014@qwertysystem.net"

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-LP-59 dan TC-AUTH-LP-60 bergantung pada TC-AUTH-LP-58 di TC sumber (kolom Dependensi); dependensi dipenuhi dengan menjalankan TC-AUTH-LP-58 terlebih dahulu pada user yang sama (S-04). Langkah 1–2 TC-AUTH-LP-60 (isi password benar lalu klik [Log in] agar Alert tampil) identik dengan TC-AUTH-LP-59 sehingga dijalankan sekali; navigasi ke halaman Reset Password ditaruh paling akhir.
- TC-AUTH-LP-163 ada di spec `TC-AUTH-LP-E2E-052-lock-daily-reset-keeps-consecutive-days`. User dan state seeding berbeda (riwayat 7 hari pada spec ini, hitungan hari berturut-turut 0 pada spec 052) dan tidak ada ketergantungan data antar-spec.
- Temuan untuk QA (TC-AUTH-LP-58): "hari ke-8" ditetapkan lewat seeding riwayat 7 hari kalender berturut-turut; TC tidak menyebut cara membentuk riwayat itu selain "waktu server uji sudah dimajukan".
