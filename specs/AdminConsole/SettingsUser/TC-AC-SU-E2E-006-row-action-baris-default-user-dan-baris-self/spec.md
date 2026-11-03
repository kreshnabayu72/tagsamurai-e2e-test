---
id: TC-AC-SU-E2E-006-row-action-baris-default-user-dan-baris-self
title: "User List: Row Action Baris Default User dan Baris Aktor Sendiri per Varian Status"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-11
  - TC-AC-SU-12
coverage:
  web: automated
---

# User List: Row Action Baris Default User dan Baris Aktor Sendiri per Varian Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup yang diubah (S-06, pengecualian data yang tidak dapat dimiliki spec): baris Default User entitas Principal (Pre-setup #1) dan akun aktor Total Control (Pre-setup #2, baris self) karena TC-AC-SU-11 dan TC-AC-SU-12 hanya bermakna pada baris itu. Fixture BE (disediakan tim FE/BE) mengatur status aktivasi Default User dan status email aktor (Activated tanpa email pending, Pending Activation, Pending Email Confirmation) per varian, dan memulihkan keduanya ke keadaan awal di hook `before`, di antara varian, dan di hook `after`. Efek pada Last Updated dan Modified By kedua baris dicatat sebagai efek spec ini. `suite.md` belum menyatakan pengecualian ini (lihat Temuan untuk QA).
- Kedua baris dicari lewat Search atas email Pre-setup #1 dan #2.
- Tidak ada data dinamis yang dibuat spec.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-11: Row action baris Default User

1. Atur status Default User menjadi Pending Activation lewat Fixture BE (varian A)
2. Muat ulang halaman dengan F5
3. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
4. Klik (⋯) baris Default User
5. Verifikasi varian A: row action menu `Detail | Resend Activation Email`
6. Tutup menu row action dengan Esc
7. Atur status Default User menjadi Pending Email Confirmation lewat Fixture BE (varian B)
8. Muat ulang halaman dengan F5
9. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
10. Klik (⋯) baris Default User
11. Verifikasi varian B: row action menu `Detail | Resend Confirmation Email`
12. Tutup menu row action dengan Esc
13. Atur status Default User menjadi Activated lewat Fixture BE (varian C)
14. Muat ulang halaman dengan F5
15. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
16. Klik (⋯) baris Default User
17. Verifikasi varian C: row action menu `Detail`
18. Tutup menu row action dengan Esc

### TC-AC-SU-12: Row action baris self

19. Atur akun aktor Activated tanpa email pending lewat Fixture BE (varian A)
20. Muat ulang halaman dengan F5
21. Ketik Search `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
22. Klik (⋯) baris aktor sendiri
23. Verifikasi varian A: row action menu `Detail`
24. Verifikasi varian A: checkbox baris self tampil namun disabled
25. Verifikasi varian A: switch ON baris self tampil namun disabled
26. Tutup menu row action dengan Esc
27. Atur akun aktor Pending Email Confirmation lewat Fixture BE (varian B)
28. Muat ulang halaman dengan F5
29. Ketik Search `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
30. Klik (⋯) baris aktor sendiri
31. Verifikasi varian B: row action menu `Detail | Resend Confirmation Email`
32. Verifikasi varian B: checkbox baris self tampil namun disabled
33. Verifikasi varian B: switch ON baris self tampil namun disabled
34. Tutup menu row action dengan Esc
35. Pulihkan status Default User dan akun aktor ke keadaan awal lewat Fixture BE, muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): langkah 3 dan Search sesudahnya (menemukan baris target lewat email, R-16), semua langkah "Tutup menu row action dengan Esc" (termasuk 34), serta langkah 35 (pemulihan state, S-09). Langkah pengaturan status varian (langkah 1 dan 19 dan padanannya) adalah precondition TC yang dijalankan lewat Fixture BE.
- Temuan untuk QA:
  - TC-AC-SU-11 dan TC-AC-SU-12 mensyaratkan status Default User dan akun aktor yang berbeda per varian; keduanya data Pre-setup, sehingga S-06 pengecualian 2026-10-30 (data tidak dapat dimiliki spec) dipakai dan `suite.md` belum memuat pernyataannya. Perlu keputusan pemilik: tambahkan pernyataan di `suite.md` atau sediakan Default User/aktor alternatif.
  - TC-AC-SU-12 memakai nama aktor `Hendra Wijaya` yang tidak ada di Tabel Pre-setup; spec memakai akun Total Control Pre-setup #2 (baris self dicari lewat emailnya).
  - Cara membuat Pending Email Confirmation pada aktor ("Email aktor diubah di Global Settings") dijalankan lewat Fixture BE, bukan lewat UI Global Settings.
