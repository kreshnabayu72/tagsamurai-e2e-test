---
id: TC-AUTH-MFA-E2E-045-enrollment-dua-device-bersamaan
title: "Enrollment Authenticator dari Dua Device Bersamaan (Web dan Android)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-119
coverage:
  web: automated
  mobile: automated
---

# Enrollment Authenticator dari Dua Device Bersamaan (Web dan Android)

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`:
  - TC-AUTH-MFA-119: `Nadia Pratiwi` (`nadiapratiwi+{runId}-045@qwertysystem.net`)
- Hook `after`: hapus user dan pastikan aplikasi mobile tidak menyimpan sesi. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik di browser dan di aplikasi) untuk TC-AUTH-MFA-119. Dua konteks aktif bersamaan: browser uji A (web, belum pernah login) dan perangkat uji Android B (aplikasi mobile TAG Samurai, platform berbeda dari browser uji A).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Driver otomasi web untuk browser uji A dan driver otomasi Android untuk perangkat uji B, keduanya aktif dalam satu run.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) yang dapat memindai dua QR code berbeda (secret halaman A dan secret halaman B) dan menghasilkan kode untuk masing-masing entri.
  - reCAPTCHA mode uji di environment (halaman web).
- Pemulihan state global: tidak ada (spec tidak mengubah jam server, geo-IP, email service, atau counter rate limit).

## Test Steps

### TC-AUTH-MFA-119: Enrollment dari dua device bersamaan: hanya satu yang berhasil

1. Di browser uji A, buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Ketik `nadiapratiwi+{runId}-045@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
9. Pindai QR code halaman Enrollment di browser uji A dengan aplikasi authenticator uji (entri secret halaman A)
10. Pindah ke perangkat uji Android B: buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
11. Ketik `nadiapratiwi+{runId}-045@qwertysystem.net` pada field Email
12. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
13. Klik button [Log in] → layar Confirm to Continue tampil
14. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
15. Pilih opsi "Authenticator app"
16. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
17. Pindai QR code halaman Enrollment di perangkat uji Android B dengan aplikasi authenticator uji (entri secret halaman B)
18. Ketik 6 digit kode dari aplikasi authenticator uji untuk entri secret halaman B pada kotak digit di perangkat uji Android B
19. Klik button [Verify] di perangkat uji Android B (enrollment aktif lebih dulu)
20. Verifikasi Perangkat uji Android B: login selesai dan Portal — Product Hub tampil
21. Pindah ke browser uji A, ketik 6 digit kode dari aplikasi authenticator uji untuk entri secret halaman A pada kotak digit
22. Klik button [Verify] di browser uji A
23. Verifikasi Browser uji A gagal verify: caption "Invalid code" tampil
24. Verifikasi Browser uji A tetap di halaman Enrollment Authenticator (enrollment yang aktif lebih dulu menang)
25. Verifikasi Tidak ada sesi yang dibuat di browser uji A

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi` (memindai QR code halaman A pada aplikasi authenticator uji sebelum berpindah ke perangkat Android, pindah antar konteks browser uji A dan perangkat uji Android B) bukan asersi tambahan (S-03).
- Temuan untuk QA: (1) TC-AUTH-MFA-119 Langkah 10 mengetik kode "secret halaman A" tetapi Langkah Uji tidak memindai QR halaman A pada aplikasi authenticator uji; spec menambah langkah pemindaian itu (S-14, S-15). (2) TC-AUTH-MFA-119 Langkah 8 menyebut login mobile "sampai halaman Enrollment Authenticator tampil" tanpa merinci Confirm to Continue dan pemilihan metode pada aplikasi mobile; spec memakai urutan yang sama dengan web karena user berprofil FIRST (login pertama di platform mana pun) dan tanpa reCAPTCHA pada aplikasi mobile, mengikuti spec mobile lain di suite ini. (3) TC-AUTH-MFA-119 Post Condition "Enrollment Authenticator `Nadia Pratiwi` aktif sekali dari perangkat uji Android B" tidak punya cara pengecekan terpisah di Langkah Uji dan tidak diasersi di luar butir a dan b. (4) TC-AUTH-MFA-119 Precondition mencantumkan mail-catcher, tetapi Langkah Uji tidak membaca email.
