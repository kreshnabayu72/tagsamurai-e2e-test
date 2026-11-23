---
id: TC-AUTH-LP-E2E-056-mobile-agreement-tautan-dokumen
title: "Tautan Dokumen Privacy Policy pada Layar Confirm to Continue di Aplikasi Mobile"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-165
coverage:
  mobile: automated
---

# Tautan Dokumen Privacy Policy pada Layar Confirm to Continue di Aplikasi Mobile

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh. Hook `after` juga menutup paksa aplikasi sehingga perangkat kembali tanpa sesi pra-auth.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: aplikasi native Android TAG Samurai Mobile (perangkat atau emulator) dengan driver otomasi yang dapat membedakan layar dalam aplikasi dari browser eksternal; seeding user subjek dengan versi Privacy Policy yang disetujui lebih lama dari versi aktif (relatif, lihat aturan State global Privacy Policy); fixture BE untuk device terpercaya di mobile (tidak memicu MFA).
- State global Privacy Policy: publish bersifat append-only dan immutable tanpa restore (`ACPP-LOGIC-01`), sehingga versi aktif tidak dipulihkan dan naik pada setiap run; suite berjalan serial. Seeding user Agreement selalu relatif terhadap versi aktif saat hook `before` (versi yang disetujui user = versi sebelum versi aktif), tanpa nomor versi absolut.
- State global: perangkat Android uji bersama; suite berjalan serial (`parallel: false`).
- TC-AUTH-LP-165: User `Tono Kurniawan` (`tonokurniawan+{runId}-056@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini; device terpercaya di mobile (tidak memicu MFA)
- TC-AUTH-LP-165: User belum login (guest); aplikasi native Android TAG Samurai Mobile
- TC-AUTH-LP-165 data: Email `tonokurniawan+{runId}-056@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`
- Layar Confirm to Continue ditinggalkan tanpa Continue, sehingga persetujuan user tidak pernah tersimpan di spec ini.

## Test Steps

### TC-AUTH-LP-165: Tautan baca dokumen penuh di aplikasi mobile membuka layar dalam app dan kembali tanpa me-reset centang

1. Buka layar Login with Password di aplikasi
2. Ketik email `tonokurniawan+{runId}-056@qwertysystem.net` di field Email
3. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
4. Ketuk [Log in] sampai layar Confirm to Continue tampil
5. Centang checkbox "I have read and agree to the Privacy Policy *"
6. Ketuk tautan "Read the full Privacy Policy" pada Content Box
7. Verifikasi dokumen Privacy Policy versi aktif tampil di layar dalam aplikasi (bukan browser eksternal)
8. Verifikasi layar dokumen menampilkan tombol kembali
9. Ketuk tombol kembali pada layar dokumen
10. Verifikasi layar Confirm to Continue tampil lagi
11. Verifikasi checkbox "I have read and agree to the Privacy Policy *" tetap tercentang
12. Verifikasi teks "Privacy Policy" pada label checkbox bukan tautan
13. Ketuk teks "Privacy Policy" pada label checkbox
14. Verifikasi dokumen Privacy Policy tidak terbuka: layar Confirm to Continue tetap tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`. Padanan web (tautan membuka tab baru, TC-AUTH-LP-91) ada di spec `TC-AUTH-LP-E2E-020-agreement-screening`; TC-AUTH-LP-165 berplatform mobile sehingga ditaruh di spec mobile tersendiri dengan `coverage.mobile: automated`, seperti spec mobile lain di suite ini (017, 018, 048).
- Layar dokumen terbuka di dalam aplikasi yang sama; tidak ada konteks kedua.
- Langkah 13 dan 14 memecah Expected c TC ("bukan tautan; mengetuknya tidak membuka dokumen"); asersi checkbox tercentang (langkah 11) ditaruh sebelum ketukan label karena ketukan label dapat mengubah centang.
- Temuan untuk QA:
  - TC-AUTH-LP-165 tidak menyebut judul layar dokumen atau penanda versi aktif yang diharapkan; asersi langkah 7 memakai "dokumen Privacy Policy versi aktif tampil di layar dalam aplikasi" sesuai Expected TC.
  - TC-AUTH-LP-165 Expected c tidak menyebut apakah mengetuk teks "Privacy Policy" pada label checkbox mengubah status centang; spec hanya mengasersi dokumen tidak terbuka.
  - TC-AUTH-LP-165 tidak menyebut perilaku tombol kembali bawaan Android (system back) pada layar dokumen; spec memakai tombol kembali pada layar dokumen sesuai langkah TC.
