---
id: TC-GS-PROFILE-E2E-030-change-password-lock-batas-waktu-15-menit
title: "Change Password: Batas Waktu Boleh-Coba-Lagi (Satu Langkah Sebelum, Tepat, dan Setelah)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-PROFILE-123
  - TC-GS-PROFILE-124
  - TC-GS-PROFILE-125
coverage:
  web: automated
---

# Change Password: Batas Waktu Boleh-Coba-Lagi (Satu Langkah Sebelum, Tepat, dan Setelah)

## Prerequisites

- Mode: FE+BE (state lock, counter, dan jam server dari backend nyata).
- Suite serial (`parallel: false`): spec mengubah state global (jam server dan jam browser, counter dan lock Change Password akun #7).
- Akun aktor: Pre-setup #7 (Maya Anggraini, Total Control, `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif lewat `Spectra.env.GS_PROFILE_PWD_PASSWORD`, Time Format 24 jam, timezone Asia/Jakarta).
- Password baru Data Dinamis #3 memakai `Spectra.env.PROFILE_PASSWORD_NEW`. Current Password salah `Wr0ngPass!` ditulis literal karena submit selalu ditolak server.
- Login akun Pre-setup #1 (default suite) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal masing-masing (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; S-13): mengatur counter dan lock tier 15 menit akun #7 dengan waktu boleh-coba-lagi 09:15 pada tanggal fixture Pre-setup #7, dan mengatur jam server serta jam browser ke nilai absolut yang dibekukan (09:14:59, 09:15:00, 09:16:00) tanpa bergeser oleh detik nyata.
- Batas waktu (bagian 8b butir 3): waktu boleh-coba-lagi 09:15 ditetapkan fixture lock (bukan dihitung dari waktu nyata); jam server dan jam browser diset absolut dan dibekukan, margin satu detik terhadap batas disengaja karena itu yang diuji.
- Pemulihan di hook `after` spec: jam server dan jam browser ke waktu nyata, counter dan lock akun #7 ke 0.

## Test Steps

1. Atur counter Change Password akun #7 ke 3, kunci tier 15 menit sampai 09:15, dan bekukan jam server dan jam browser di 09:00
2. Klik [Change Password]

### TC-GS-PROFILE-123: Satu langkah sebelum waktu boleh-coba-lagi

3. Atur jam server dan jam browser ke 09:14:59 (dibekukan)
4. Verifikasi [Save] masih Disabled

### TC-GS-PROFILE-124: Tepat di waktu boleh-coba-lagi

5. Atur jam server dan jam browser ke 09:15:00 (dibekukan) tanpa memuat ulang halaman
6. Verifikasi [Save] Enabled otomatis tanpa memuat ulang halaman

### TC-GS-PROFILE-125: Setelah waktu boleh-coba-lagi

7. Atur jam server dan jam browser ke 09:16:00 (dibekukan)
8. Isi Current Password "Wr0ngPass!", New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
9. Klik [Save]
10. Verifikasi inline error "Current password is incorrect"
11. Verifikasi tidak ada toast terkunci
12. Verifikasi [Save] tetap Enabled
13. Klik [✕]
14. Verifikasi dialog Unsaved Changes tampil
15. Klik [Leave]

## Notes

- Kelas harness: d (batas eksak waktu). Satu pembukaan modal (langkah 2) dipakai untuk tiga kasus berurutan karena ketiganya hanya menggeser jam; TC-GS-PROFILE-125 memakai modal yang sama (langkah 1 TC identik dengan langkah 2 spec ini) dan mengisi form di langkah 8.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3, 5, 7 (mengatur state dan jam), 13 sampai 15 (menutup form dirty sesuai S-08).
- Anchor absence: langkah 10 (inline error tampil) mendahului langkah 11.
- Temuan untuk QA:
  - TC-GS-PROFILE-125 menulis Post Condition "Counter Change Password menjadi 4" tanpa langkah observasi; tidak diasersi.
  - TC-GS-PROFILE-123 dan TC-GS-PROFILE-124 tidak menyebut apakah jam browser ikut digeser; spec mengatur jam server dan jam browser bersama (bagian 6).
