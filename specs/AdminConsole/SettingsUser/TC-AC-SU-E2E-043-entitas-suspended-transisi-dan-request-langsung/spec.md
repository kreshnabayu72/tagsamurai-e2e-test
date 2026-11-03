---
id: TC-AC-SU-E2E-043-entitas-suspended-transisi-dan-request-langsung
title: "Entitas Suspended: Transisi Suspend/Unsuspend dan Request Tulis Langsung"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-165
  - TC-AC-SU-166
  - TC-AC-SU-167
  - TC-AC-SU-168
  - TC-AC-SU-169
coverage:
  web: automated
---

# Entitas Suspended: Transisi Suspend/Unsuspend dan Request Tulis Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user and role (Update) entitas Distributor Nusantara, Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, password `Spectra.env.AC_DIST_MUR_PASSWORD`.
- Akun kedua (ganti akun eksplisit di tengah spec): Total Control entitas Distributor Nusantara, Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, password `Spectra.env.AC_DIST_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (entitas Distributor Nusantara, seed lewat Fixture BE): `John Doe {runId}-043` (Activated, Active), `Jane Smith {runId}-043` (Activated, Inactive), `Mike Tan {runId}-043` (Pending Activation).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-043@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-043`.
- State tenant: status Suspended entitas Distributor Nusantara diubah dalam spec lewat Fixture BE yang setara aksi Admin Principal di modul Distributor (disediakan tim FE/BE); setiap langkah pemicu ditulis "... hingga status ... tersimpan". Hook `before` memastikan entitas berstatus Aktif; hook `after` meng-unsuspend entitas bila masih Suspended dan mengembalikan sesi ke Default User.
- Kemampuan teknis tambahan: klien HTTP untuk request langsung ke server dan perekaman request Deactivate `John Doe {runId}-043` yang dikirim sebelum suspend (TC-166); disediakan tim FE/BE.
- Akun aktor entitas Distributor Nusantara selain Default User tidak ada di Tabel Data Uji Pre-setup (hanya #7); email dan password `Spectra.env.AC_DIST_TC_PASSWORD` / `Spectra.env.AC_DIST_MUR_PASSWORD` perlu disediakan tim FE dan didaftarkan di `executionConfig.environmentVariables` serta `.env.example` oleh pemilik repo.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user) di-seed hook `before` dengan suffix `{runId}-043` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SU-165: Entitas suspended: login tetap boleh, sesi aktif tidak diputus

1. Rekam request Deactivate `John Doe {runId}-043` (klien HTTP) sebelum entitas disuspend, tanpa mengirimnya
2. Ketik Search `{runId}-043`, tekan Enter
3. Pemicu: suspend entitas Distributor Nusantara lewat Fixture BE hingga status Suspended tersimpan
4. Amati User List tanpa memuat ulang halaman
5. Verifikasi sesi tidak diputus: User List tetap tampil
6. Verifikasi switch Active baris `John Doe {runId}-043` berubah disabled tanpa memuat ulang
7. Verifikasi checkbox baris `John Doe {runId}-043` berubah disabled tanpa memuat ulang
8. Logout dari akun Manage user and role entitas Distributor
9. Login ulang sebagai Manage user and role entitas Distributor (`Spectra.env.AC_DIST_MUR_PASSWORD`)
10. Verifikasi login berhasil: Portal tampil

### TC-AC-SU-166: Entitas suspended: request tulis langsung ditolak server

11. Logout dari akun Manage user and role entitas Distributor
12. Login sebagai Total Control entitas Distributor (`Spectra.env.AC_DIST_TC_PASSWORD`)
13. Buka Settings > User lewat sidebar
14. Kirim ulang request Deactivate `John Doe {runId}-043` yang direkam sebelum suspend (klien HTTP, tanpa browser)
15. Verifikasi server menolak request (respons penolakan; kode status tidak dinyatakan TC)

### TC-AC-SU-167: Entitas di-unsuspend: akses tulis kembali normal tanpa reaktivasi per user

16. Ketik Search `{runId}-043`, tekan Enter
17. Pemicu: unsuspend entitas Distributor Nusantara lewat Fixture BE hingga status Aktif tersimpan
18. Amati User List tanpa memuat ulang halaman
19. Verifikasi switch Active baris `John Doe {runId}-043` kembali enabled
20. Verifikasi checkbox baris `John Doe {runId}-043` kembali enabled
21. Klik `(⋯)` baris `Mike Tan {runId}-043`
22. Verifikasi row action baris `Mike Tan {runId}-043` memuat kembali `Resend Activation Email`
23. Tutup menu `(⋯)` dengan Esc
24. Klik switch Active baris `John Doe {runId}-043`
25. Verifikasi dialog Deactivate User muncul
26. Tutup dialog Deactivate User tanpa mengonfirmasi (Esc)

### TC-AC-SU-168: Banner Dashboard hilang otomatis saat entitas di-unsuspend

27. Pemicu: suspend entitas Distributor Nusantara lewat Fixture BE hingga status Suspended tersimpan
28. Buka Admin Console > Dashboard lewat sidebar
29. Verifikasi banner suspended tampil: `"Your organization is currently suspended. Contact your administrator for more information."`
30. Admin Principal meng-unsuspend entitas (Fixture BE hingga status Aktif tersimpan)
31. Amati Dashboard tanpa memuat ulang halaman
32. Verifikasi banner suspended hilang otomatis

### TC-AC-SU-169: Suspend lalu unsuspend tidak mengubah nilai status Active user

33. Pemicu: suspend lalu unsuspend entitas Distributor Nusantara lewat Fixture BE hingga status Aktif tersimpan
34. Buka Settings > User lewat sidebar
35. Ketik Search `{runId}-043`, tekan Enter
36. Amati switch `John Doe {runId}-043` dan `Jane Smith {runId}-043`
37. Verifikasi switch `John Doe {runId}-043` ON
38. Verifikasi switch `Jane Smith {runId}-043` OFF

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 2, 3, 16, 17, 23, 26, 27, 33, 35 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Kelas harness h (state tenant). P-5 butir (b): TC-AC-SU-166 (request tulis langsung ke server saat Suspended) adalah satu-satunya TC objek-uji ringan kelas a di spec ini (tanpa harness eksternal dan tanpa state berat sendiri); TC-AC-SU-623 ada di spec 044.
- Pemecahan TC kelas h: TC-AC-SU-603, 604, 623 ada di spec 044 (`TC-AC-SU-E2E-044-entitas-suspended-transisi-dan-request-langsung-bagian-2`).
- Ganti akun eksplisit: TC-165 memakai akun Manage user and role entitas Distributor (pelaku "John Doe" pada TC); TC-166 sampai TC-169 memakai Total Control entitas Distributor. Alasan: kedua peran ada di entitas Distributor yang sama dan state Suspended dibangun berurutan oleh pemicu.
- Setelah TC-166 entitas masih Suspended; TC-167 meng-unsuspend, TC-168 menyuspend lalu meng-unsuspend lagi, TC-169 menyuspend lalu meng-unsuspend: pemicu tiap TC ditulis eksplisit di langkah penghubung.
- Anchor absence/transisi TC-168: banner Dashboard tampil lebih dulu sebelum asersi hilang.
- Langkah penghubung TC-168 mencakup langkah 30 (Admin Principal meng-unsuspend entitas lewat Fixture BE hingga status Aktif tersimpan); tanpa `Verifikasi`.
- Temuan untuk QA:
  - TC-165 menulis pelaku `John Doe` yang sedang login; tidak terpetakan ke akun Pre-setup. Spec memakai akun Manage user and role entitas Distributor sebagai sesi pelaku.
  - TC-166 mengharapkan toast "Changes can't be saved while this workspace is suspended or expired." dan rollback kontrol; untuk request langsung ke server perilaku FE itu tidak disalin (bagian 8b butir 1) dan hanya respons penolakan yang diasersi. Perilaku FE untuk respons yang sama belum punya spec jalur form. Post Condition ("Status `John Doe` tidak berubah") tidak punya langkah observasi dan tidak diasersi.
  - TC-167 dan TC-168 menyebut "Admin Principal" tanpa akun; spec memakai Fixture BE sebagai pemicu.
  - Nama dialog "Deactivate User" (TC-167) dipakai apa adanya; judul dan isi dialog tidak dinyatakan.
  - TC-169 tidak menyatakan siapa yang menyuspend; spec memakai Fixture BE.
- Alasan spec melewati sekitar 35 langkah: seluruh TC berada pada satu kelas harness (h, state tenant Distributor Nusantara) dan state Suspended dibangun berurutan oleh pemicu antar-TC; kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok membangun ulang state lewat pemicu eksplisit.
