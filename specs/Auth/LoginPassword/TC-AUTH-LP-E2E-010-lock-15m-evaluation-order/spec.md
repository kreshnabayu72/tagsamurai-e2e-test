---
id: TC-AUTH-LP-E2E-010-lock-15m-evaluation-order
title: "Urutan Evaluasi Lock 15 Menit terhadap Password Kosong dan reCAPTCHA"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-LP-42
  - TC-AUTH-LP-43
coverage:
  web: automated
---

# Urutan Evaluasi Lock 15 Menit terhadap Password Kosong dan reCAPTCHA

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`.
- Kemampuan teknis: fixture BE yang menaruh user pada status terkunci 15 menit di web dengan waktu berakhirnya lock masih berlaku selama seluruh spec (tanpa melalui tiga kegagalan password); reCAPTCHA mode uji di environment; General Settings entitas memakai Time Zone dan Time Format default.
- TC-AUTH-LP-42: Tanpa login (guest, browser web)
- TC-AUTH-LP-42: User `Rina Putri` (`rinaputri+{runId}-010@qwertysystem.net`) berstatus Activated dan Active, sedang terkunci 15 menit di web (di-seed oleh fixture BE di hook `before`)
- TC-AUTH-LP-42 data: Password kosong
- TC-AUTH-LP-43: Tanpa login (guest, browser web)
- TC-AUTH-LP-43: User yang sama (`rinaputri+{runId}-010@qwertysystem.net`) masih terkunci 15 menit di web
- TC-AUTH-LP-43 data: Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-42: Submit Password kosong selama lock 15 menit aktif

1. Buka halaman Login with Password
2. Isi Email `rinaputri+{runId}-010@qwertysystem.net` dan kosongkan field Password
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil ({time} = jam berakhirnya lock dalam Time Format General Settings dan Time Zone entitas, hanya jam tanpa tanggal; cek lock didahulukan dari Password kosong)
6. Verifikasi caption "Password must not be empty" tidak tampil

### TC-AUTH-LP-43: Submit tanpa reCAPTCHA selama lock 15 menit aktif

7. Muat ulang halaman Login with Password
8. Isi Email `rinaputri+{runId}-010@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD`
9. Tanpa menyelesaikan reCAPTCHA, klik [Log in]
10. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil ({time} = jam berakhirnya lock dalam Time Format General Settings dan Time Zone entitas, hanya jam tanpa tanggal; cek lock didahulukan dari reCAPTCHA)
11. Verifikasi caption "Please verify that you are not a robot" tidak tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AUTH-LP-42 dan TC-AUTH-LP-43 bergantung pada TC-AUTH-LP-38 di TC sumber (kolom Dependensi). Di spec ini state terkunci 15 menit disiapkan lewat seeding fixture BE (S-04 membolehkan seeding API sebagai pengganti penyalinan langkah); progresi lock yang membangun state itu diuji di spec `TC-AUTH-LP-E2E-009-lock-15m-progression`.
- Langkah penghubung (S-03): langkah 7 (muat ulang halaman Login with Password) mengembalikan form ke keadaan awal sebelum TC-AUTH-LP-43 dijalankan; tidak ada asersi tambahan.
- Spec ini hanya berjalan beberapa menit setelah seeding, sehingga lock 15 menit tidak berakhir di tengah spec.
- Temuan untuk QA: TC sumber tidak menyebut cara memicu state "terkunci 15 menit" tanpa tiga kegagalan nyata; spec ini mengandalkan fixture BE tanpa menyebut endpoint (S-13).
