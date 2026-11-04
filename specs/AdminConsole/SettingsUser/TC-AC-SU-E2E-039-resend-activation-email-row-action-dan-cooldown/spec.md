---
id: TC-AC-SU-E2E-039-resend-activation-email-row-action-dan-cooldown
title: "Resend Activation Email: Row Action dan Cooldown 60 Detik"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-142
  - TC-AC-SU-146
  - TC-AC-SU-147
  - TC-AC-SU-148
coverage:
  web: automated
---

# Resend Activation Email: Row Action dan Cooldown 60 Detik

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (Pending Activation, seed lewat Fixture BE): `Mike Tan {runId}-039`, `Sarah Lee {runId}-039` (belum di-resend).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-039@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-039`.
- Jam server dan jam browser/klien diatur bersama (bagian 6 konvensi); waktu terbit pengiriman (T0) dibaca lewat API seeding. Jam dipulihkan di langkah penghubung terakhir dan di hook `after`. Kemampuan atur jam server dan jam browser disediakan tim FE/BE.
- Mail-catcher tidak dipakai: tidak ada butir Expected TC tentang isi atau jumlah email.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user, group, role) di-seed hook `before` dengan suffix `{runId}-039` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-142: Resend Activation Email via row action: sukses dan cooldown dimulai

1. Ketik Search `{runId}-039`, tekan Enter
2. Klik `(⋯)` baris `Mike Tan {runId}-039` (Pending Activation)
3. Klik `Resend Activation Email`
4. Verifikasi muncul toast sukses: "Success, email has been sent."
5. Klik `(⋯)` baris `Mike Tan {runId}-039` lagi
6. Verifikasi opsi `Resend Activation Email` disabled dengan label tetap
7. Hover opsi `Resend Activation Email`
8. Verifikasi tooltip `"Please wait [Seconds] seconds before resending."`
9. Catat angka `[Seconds]` pada tooltip sebagai pembacaan pertama
10. Atur jam server dan jam browser maju 10 detik
11. Hover opsi `Resend Activation Email`
12. Verifikasi angka `[Seconds]` pada tooltip menurun dibanding angka yang dicatat pada langkah 9
13. Tutup menu `(⋯)` dengan Esc

### TC-AC-SU-146: Cooldown: 1 detik sebelum berakhir tombol masih disabled

14. Atur jam server dan jam browser ke T0 + 59 detik (T0 = waktu terbit pengiriman Resend `Mike Tan {runId}-039`)
15. Klik `(⋯)` baris `Mike Tan {runId}-039`
16. Hover opsi `Resend Activation Email`
17. Verifikasi opsi `Resend Activation Email` masih disabled
18. Verifikasi tooltip `"Please wait 1 seconds before resending."`

### TC-AC-SU-147: Cooldown berakhir tepat 60 detik: tombol kembali enabled dan bisa kirim lagi

19. Atur jam server dan jam browser ke T0 + 60 detik tanpa memuat ulang halaman
20. Hover opsi `Resend Activation Email`
21. Verifikasi opsi `Resend Activation Email` otomatis enabled
22. Verifikasi tooltip cooldown hilang
23. Klik `Resend Activation Email`
24. Verifikasi muncul toast sukses: "Success, email has been sent."
25. Klik `(⋯)` baris `Mike Tan {runId}-039`
26. Verifikasi cooldown baru dimulai: opsi `Resend Activation Email` disabled
27. Tutup menu `(⋯)` dengan Esc

### TC-AC-SU-148: Cooldown terpisah per user

28. Klik `(⋯)` baris `Sarah Lee {runId}-039` (Pending Activation, belum di-resend; `Mike Tan {runId}-039` dalam cooldown)
29. Verifikasi opsi `Resend Activation Email` baris `Sarah Lee {runId}-039` enabled
30. Klik `Resend Activation Email`
31. Verifikasi muncul toast sukses: "Success, email has been sent."
32. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 13, 14, 19, 27, 32 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- TC-146 dan TC-147 bergantung pada pengiriman TC-142 (Dependensi TC): TC-142 dijalankan lebih dulu, T0 adalah waktu terbit pengiriman itu. Waktu T0 + 59 dan T0 + 60 diset absolut (bagian 8b butir 3), bukan ditunggu.
- TC-148 berjalan sesudah TC-147: `Mike Tan {runId}-039` dalam cooldown seperti prasyarat TC.
- Pembagian TC: TC-AC-SU-149 (resend berulang tanpa batas harian) ada di spec 191 (`TC-AC-SU-E2E-191-resend-activation-email-tanpa-batas-harian`).
- Temuan untuk QA:
  - Teks tooltip TC-142 memakai placeholder `[Seconds]` ("X menghitung mundur"); spec mengasersi bentuk `"Please wait [Seconds] seconds before resending."` dengan angka menurun, nilai awal tidak dinyatakan TC.
  - Post Condition TC-142, 147 ("email terkirim", "entri log") tidak punya langkah observasi dan tidak diasersi.
  - TC-147 menulis "Tunggu 60 detik"; dipenuhi dengan mengatur jam (bagian 6), bukan menunggu nyata.
