---
id: TC-AUTH-MFA-E2E-056-aksesibilitas-screen-reader-validasi-kode
title: "Aksesibilitas Screen Reader pada Pesan Validasi Kode Authenticator"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-12
coverage:
  web: automated
---

# Aksesibilitas Screen Reader pada Pesan Validasi Kode Authenticator

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (device dikenali), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-12: `Maya Kusuma` (`mayakusuma+{runId}-056@qwertysystem.net`)
- Hook `after`: hapus user seeding dan nonaktifkan screen reader uji bila masih aktif. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser). TC ini berjalan di browser awal tanpa ID device tersimpan, dikenali sebagai browser uji B (ID device belum dikenali), dan login dari IP uji Jakarta (ID) hanya memicu MFA karena device baru. User berprofil NEWDEVE, jadi login Password melewati Choose Verification Method tanpa layar Confirm to Continue.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture. Kode salah `000000` adalah input uji yang ditolak server, ditulis literal.
- Kemampuan teknis: reCAPTCHA mode uji di environment; screen reader uji yang dapat diaktifkan dan dinonaktifkan oleh automation, dengan keluaran pengumumannya dapat dibaca oleh automation; kemampuan membaca atribut ARIA pada region pesan error.
- Kemampuan teknis, seeding state BE per user: status Activated dan Active ON, trusted device ber-ID device browser uji A (device dikenali), lokasi dan waktu login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, consent sudah disetujui sehingga tanpa layar Confirm to Continue, dan Authenticator terdaftar. Mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-12: Accessibility — pesan validasi kode salah diumumkan seketika ke screen reader (ARIA live)

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `mayakusuma+{runId}-056@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
8. Aktifkan screen reader uji
9. Ketik 6 digit kode salah `000000` pada kotak digit
10. Klik button [Login]
11. Verifikasi Pesan "Invalid code" muncul pada slot error
12. Verifikasi Pesan "Invalid code" diumumkan seketika oleh screen reader tanpa perpindahan fokus manual
13. Verifikasi Region pesan error memiliki atribut ARIA live
14. Nonaktifkan screen reader uji

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini berkelas d karena objek ujinya keluaran teknologi bantu (screen reader dan atribut ARIA live), bukan perilaku fungsional validasi kode; validasi fungsional kode Authenticator ada di spec TC-AUTH-MFA-E2E-010.
- Langkah penghubung tanpa awalan `Verifikasi` (langkah 8 mengaktifkan dan langkah 14 menonaktifkan screen reader supaya tidak memengaruhi spec berikutnya) bukan asersi tambahan (S-03, S-09). Langkah 11 dan 12 memisahkan dua klausa Expected a TC-AUTH-MFA-12 (pesan muncul; pesan diumumkan) menjadi satu `Verifikasi` per klausa (S-01).
- Pencatatan pada Post Condition TC-AUTH-MFA-12 (Failed `Incorrect OTP`) tidak diasersikan di spec ini; asersi pencatatan berada di spec pencatatan.
- Temuan untuk QA: (1) TC-AUTH-MFA-12 tidak menyebut cara membaca keluaran screen reader dan ditandai Manual Only; spec mengasumsikan keluaran pengumuman dapat dibaca automation (Prerequisites). (2) Pre-setup TC (#20/#21) belum memuat mekanisme seeding state BE per user (trusted device ber-ID device browser A, lokasi dan waktu login terakhir, consent, logout web terakhir, Authenticator terdaftar); mekanisme seed disediakan tim FE/BE.
