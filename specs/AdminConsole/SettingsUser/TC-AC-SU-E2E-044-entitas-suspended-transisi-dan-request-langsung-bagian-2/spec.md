---
id: TC-AC-SU-E2E-044-entitas-suspended-transisi-dan-request-langsung-bagian-2
title: "Entitas Suspended: Sesi Aktor MUR Distributor, Pemulihan Otomatis, dan Request Activate Langsung"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-603
  - TC-AC-SU-604
  - TC-AC-SU-623
coverage:
  web: automated
---

# Entitas Suspended: Sesi Aktor MUR Distributor, Pemulihan Otomatis, dan Request Activate Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user and role (Update) entitas Distributor Nusantara, Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, password `Spectra.env.AC_DIST_MUR_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (entitas Distributor Nusantara, seed lewat Fixture BE): `Jane Smith {runId}-044` (Activated, Inactive).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-044@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-044`.
- State tenant: status Suspended entitas Distributor Nusantara diubah dalam spec lewat Fixture BE yang setara aksi Principal di modul Distributor (disediakan tim FE/BE); setiap pemicu ditulis "... hingga status ... tersimpan". Hook `before` memastikan entitas Aktif; hook `after` meng-unsuspend entitas bila masih Suspended.
- Kemampuan teknis tambahan: klien HTTP untuk request langsung ke server (TC-623); disediakan tim FE/BE.
- Akun aktor entitas Distributor Nusantara selain Default User tidak ada di Tabel Data Uji Pre-setup (hanya #7); email dan password `Spectra.env.AC_DIST_MUR_PASSWORD` perlu disediakan tim FE dan didaftarkan di `executionConfig.environmentVariables` serta `.env.example` oleh pemilik repo.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user) di-seed hook `before` dengan suffix `{runId}-044` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-603: Entitas disuspend membuat seluruh kontrol tulis read-only tanpa memutus sesi

1. Ketik Search `{runId}-044`, tekan Enter
2. Pemicu: Principal suspend Distributor Nusantara lewat Fixture BE hingga status Suspended tersimpan
3. Amati Settings > User aktor Distributor tanpa memuat ulang halaman
4. Verifikasi sesi tidak diputus: User List tetap tampil
5. Hover switch Active baris `Jane Smith {runId}-044`
6. Verifikasi switch Active baris `Jane Smith {runId}-044` disabled
7. Verifikasi tooltip `"Entity is suspended."` pada switch Active
8. Verifikasi checkbox seluruh baris disabled
9. Hover checkbox baris `Jane Smith {runId}-044`
10. Verifikasi tooltip `"Entity is suspended."` pada checkbox
11. Verifikasi Bulk Action Bar tidak tampil
12. Klik `(⋯)` baris `Jane Smith {runId}-044`
13. Verifikasi `Detail` tampil pada row action baris `Jane Smith {runId}-044`
14. Verifikasi Resend tidak tampil pada row action baris `Jane Smith {runId}-044`
15. Tutup menu `(⋯)` dengan Esc
16. Klik nama `Jane Smith {runId}-044`, Detail terbuka, buka Tab Role, lalu Sub-tab [Group Role]
17. Verifikasi `[Detail]` tampil pada kolom Actions Group Role
18. Verifikasi `[Assign Group]` tidak tampil
19. Buka Dashboard lewat sidebar
20. Verifikasi banner Dashboard: `"Your organization is currently suspended. Contact your administrator for more information."`

### TC-AC-SU-604: Entitas di-unsuspend memulihkan akses normal otomatis

21. Pemicu: Principal unsuspend Distributor Nusantara lewat Fixture BE hingga status Aktif tersimpan
22. Amati Dashboard tanpa memuat ulang halaman
23. Verifikasi banner Dashboard hilang
24. Buka Settings > User lewat sidebar
25. Ketik Search `{runId}-044`, tekan Enter
26. Verifikasi switch Active baris `Jane Smith {runId}-044` (baris non-protected) enabled
27. Verifikasi baris `Jane Smith {runId}-044` dapat dioperasikan tanpa aktivasi ulang per user

### TC-AC-SU-623: Aksi tulis saat entitas suspended via bypass ditolak

28. Pemicu: suspend Distributor Nusantara lewat Fixture BE hingga status Suspended tersimpan
29. Injeksi request Activate `Jane Smith {runId}-044` (klien HTTP, tanpa browser)
30. Verifikasi server menolak request (respons penolakan; kode status tidak dinyatakan TC)
31. Amati Settings > User dan Popup Changelog: User

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 2, 15, 21, 25, 28 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Langkah 13 (`Detail` tampil pada row action) adalah anchor positif tambahan (S-03, dasar 8b.2) bagi absence Resend pada langkah 14.
- Kelas harness h (state tenant). P-5 butir (b): TC-AC-SU-623 (request tulis langsung saat Suspended) adalah satu-satunya TC objek-uji ringan kelas a di spec ini; TC-AC-SU-166 ada di spec 043.
- Pembagian TC: TC-AC-SU-165 sampai 169 ada di spec 043 (`TC-AC-SU-E2E-043-entitas-suspended-transisi-dan-request-langsung`).
- Satu sesi aktor MUR Distributor dipakai sepanjang spec (login di hook `before`); status Suspended dibangun berurutan oleh pemicu: TC-603 menyuspend, TC-604 meng-unsuspend, TC-623 menyuspend lagi.
- Temuan untuk QA:
  - TC-603 menulis "Bulk Action Bar, Resend, dan [Assign Group] tidak tampil" tanpa anchor positif per elemen; spec memakai `[Detail]` sebagai anchor untuk `[Assign Group]` dan hasil hover sebagai anchor lainnya.
  - Hover checkbox pada langkah 9 mengikuti langkah TC-603 dan tooltip yang sama dengan switch menurut TC-161.
  - TC-604 butir c ("Tidak perlu aktivasi ulang per user") tidak punya langkah observasi sendiri; spec memakai satu `Verifikasi` yang bergantung pada butir a.
  - TC-623 mengharapkan toast "Changes can't be saved while this workspace is suspended or expired." dan langkah "Amati Settings > User dan Popup Changelog: User" tanpa Expected sendiri. Perilaku FE (toast) pada request langsung tidak disalin (bagian 8b butir 1); langkah Amati ditulis tanpa `Verifikasi`.
  - Aktor TC-603, 604, 623 ditulis "Manage user and role (Update) (entitas Distributor Nusantara)" tanpa akun; spec memakai akun yang disediakan tim FE.
