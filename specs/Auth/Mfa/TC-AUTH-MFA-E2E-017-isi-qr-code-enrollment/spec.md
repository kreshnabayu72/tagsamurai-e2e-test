---
id: TC-AUTH-MFA-E2E-017-isi-qr-code-enrollment
title: "Isi QR Code Enrollment Authenticator"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-109
coverage:
  web: automated
---

# Isi QR Code Enrollment Authenticator

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-109: `Dinda Ayu` (`dindaayu+{runId}-017@qwertysystem.net`)
- Seeding state BE per user: hanya profil FIRST (Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar) yang dibentuk lewat pembuatan user oleh akun aktor; tidak ada state BE lain yang di-seed. Secret pending dibentuk oleh alur UI spec ini sendiri.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam aplikasi authenticator uji; hook `after` memulihkan jam aplikasi authenticator uji ke jam semula.
- Hook `after`: hapus user tersebut dan pulihkan jam aplikasi authenticator uji ke jam semula. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness eksternal, prinsip 13 butir d):
  - Dekode QR code: mengambil gambar QR code dari elemen canvas atau gambar di halaman Enrollment lalu mendekodenya menjadi URI `otpauth://` untuk dibaca skema, label, dan parameternya.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) yang dapat mendaftarkan akun dari QR code atau URI `otpauth://` hasil dekode, menampilkan penerbit dan identitas akun, menghasilkan kode TOTP, dan jam aplikasinya dapat dimajukan 30 detik lalu dipulihkan (langkah 21 dan 23).
  - Yang diatur hanya jam klien (jam aplikasi authenticator uji); jam server dan jam browser tidak diubah. Spec ini tidak menunggu waktu nyata.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-109: QR code mendaftarkan akun TAG Samurai dengan kode 6 digit berperiode 30 detik

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `dindaayu+{runId}-017@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
9. Ambil gambar QR code dari halaman Enrollment lalu dekode menjadi URI `otpauth://`
10. Verifikasi URI hasil dekode berskema `otpauth://totp/`
11. Verifikasi URI hasil dekode memuat penerbit "TAG Samurai"
12. Verifikasi URI hasil dekode memuat identitas `dindaayu+{runId}-017@qwertysystem.net`
13. Verifikasi URI hasil dekode memuat parameter 6 digit (`digits=6`)
14. Verifikasi URI hasil dekode memuat parameter periode 30 detik (`period=30`)
15. Verifikasi URI hasil dekode memuat parameter algoritma SHA-1 (`algorithm=SHA1`)
16. Pindai QR code dengan aplikasi authenticator uji
17. Amati entri akun pada aplikasi dan catat kode yang tampil
18. Verifikasi Aplikasi authenticator uji menambahkan akun dengan penerbit "TAG Samurai"
19. Verifikasi Aplikasi authenticator uji menambahkan akun dengan identitas `dindaayu+{runId}-017@qwertysystem.net`
20. Verifikasi Kode yang tampil terdiri atas 6 digit
21. Majukan jam aplikasi authenticator uji 30 detik lalu amati kode yang tampil
22. Verifikasi Kode yang tampil berbeda dari kode yang dicatat pada langkah 17 (kode berganti setiap 30 detik)
23. Pulihkan jam aplikasi authenticator uji ke jam semula
24. Ketik 6 digit kode yang sedang tampil di aplikasi authenticator uji pada kotak digit
25. Klik button [Verify]
26. Verifikasi Kode dari aplikasi diterima oleh button [Verify] pada halaman Enrollment (SHA-1): browser dialihkan ke Portal — Product Hub

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Satu TC (kelas harness eksternal: dekode QR dan pengamatan TOTP) sehingga spec ini terpisah dari spec Enrollment lain (prinsip 13 butir d).
- Asersi parameter URI hasil dekode (langkah 10 sampai 15) menurunkan butir Expected a, b, dan c yang menyebut penerbit, identitas, 6 digit, periode 30 detik, dan SHA-1 dari sisi isi QR code; pengamatan perilaku aplikasi (langkah 18 sampai 22, 26) tetap mengikuti TC. Dicatat sebagai asersi tambahan di bawah dasar Expected TC (S-03).
- Expected b "berganti setiap 30 detik" diamati lewat satu pergantian kode setelah jam aplikasi authenticator uji dimajukan 30 detik (Langkah Uji 10 TC), bukan lewat menunggu waktu nyata.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 9 (dekode QR), langkah 23 (memulihkan jam aplikasi authenticator uji sebelum kode diketik, supaya kode yang diterima server sesuai jam server), dan langkah 24, 25 (mengetik kode lalu [Verify]) yang dibutuhkan agar butir c "kode diterima oleh [Verify]" dapat dicek (S-14).
- Pencatatan: TC ini tidak memuat asersi pencatatan.
- Temuan untuk QA: (1) TC-AUTH-MFA-109 berlabel Manual Only, tetapi spec ini memasukkannya dengan kemampuan dekode QR dan pengaturan jam aplikasi authenticator uji di Prerequisites. (2) Butir c Expected "diterima oleh button [Verify]" tidak punya langkah mengetik kode dan klik [Verify] di Langkah Uji; ditambahkan sebagai langkah 24–25 dan "diterima" diartikan sebagai pengalihan ke Portal — Product Hub. (3) Post Condition "Enrollment belum aktif sampai [Verify] diklik" tidak punya Expected padanan maupun langkah observasi di TC; tidak diasersi di spec ini (S-01). QA dapat menambah Expected atau langkah observasi di TC. (4) Mekanisme seeding user profil FIRST mengikuti Pre-setup #3 (Create User); tidak ada state BE tambahan yang butuh mekanisme seeding di spec ini.
