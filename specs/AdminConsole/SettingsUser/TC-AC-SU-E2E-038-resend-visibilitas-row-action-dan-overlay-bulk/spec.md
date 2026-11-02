---
id: TC-AC-SU-E2E-038-resend-visibilitas-row-action-dan-overlay-bulk
title: "Resend Email: Visibilitas Row Action dan Overlay Bulk Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-138
  - TC-AC-SU-139
  - TC-AC-SU-141
  - TC-AC-SU-155
  - TC-AC-SU-159
coverage:
  web: automated
---

# Resend Email: Visibilitas Row Action dan Overlay Bulk Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control, `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data milik spec (status aktivasi seed lewat Fixture BE): `Mike Tan {runId}-038` (Pending Activation), `John Doe {runId}-038` (Activated, Active), `Rina Putri {runId}-038` (Pending Email Confirmation, Active), `Budi Santoso {runId}-038` (Pending Email Confirmation, Inactive).
- Email user seed: `<nama huruf kecil dipisah titik>+{runId}-038@qwertysystem.net`; user pada User List dikenali lewat nama bersuffix dan Search atas suffix `{runId}-038`.
- TC-AC-SU-141: Default User Principal diatur ke Pending Email Confirmation lewat Fixture BE di langkah penghubung dan dipulihkan ke Activated di hook `after` (lihat Temuan untuk QA).
- Data Pre-setup yang dipakai: Default User Principal (Pre-setup #1) `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, dicari lewat Search atas emailnya.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data; disediakan tim FE/BE).
- Data milik spec (user) di-seed hook `before` dengan suffix `{runId}-038` dan dihapus atau dipulihkan hook `after`; data Pre-setup tidak diubah.
- Suite berjalan serial (`parallel: false`).
- TC-AC-SU-141 (S-06): perubahan status Default User Principal lewat Fixture BE mengubah Last Updated dan Modified By akun itu menjadi `Default User`; efek pada kedua kolom itu diterima dan tidak ikut dipulihkan hook `after`.

## Test Steps

### TC-AC-SU-138: Row action Resend Activation Email tampil untuk user Pending Activation

1. Ketik Search `{runId}-038`, tekan Enter
2. Klik `(⋯)` baris `Mike Tan {runId}-038` (Pending Activation)
3. Verifikasi row action baris `Mike Tan {runId}-038`: `Detail` | `Resend Activation Email`
4. Tutup menu `(⋯)` dengan Esc
5. Klik `(⋯)` baris `John Doe {runId}-038` (Activated)
6. Verifikasi row action baris `John Doe {runId}-038`: hanya `Detail`
7. Tutup menu `(⋯)` dengan Esc

### TC-AC-SU-139: Row action Resend Confirmation Email tampil untuk user Pending Email Confirmation

8. Klik `(⋯)` baris `Rina Putri {runId}-038` (Pending Email Confirmation, Active)
9. Verifikasi row action baris `Rina Putri {runId}-038`: `Detail` | `Resend Confirmation Email`
10. Verifikasi row action baris `Rina Putri {runId}-038` tidak memuat `Resend Activation Email`
11. Tutup menu `(⋯)` dengan Esc
12. Klik `(⋯)` baris `Budi Santoso {runId}-038` (Pending Email Confirmation, Inactive)
13. Verifikasi row action baris `Budi Santoso {runId}-038`: `Detail` | `Resend Confirmation Email`
14. Verifikasi row action baris `Budi Santoso {runId}-038` tidak memuat `Resend Activation Email`
15. Tutup menu `(⋯)` dengan Esc

### TC-AC-SU-155: Bulk Resend Activation Email: seleksi campuran, aksi disembunyikan

16. Centang `Mike Tan {runId}-038` (Pending Activation) dan `John Doe {runId}-038` (Activated)
17. Klik `[Bulk Action ▾]`
18. Verifikasi overlay Bulk Action terbuka
19. Verifikasi opsi `Deactivate` tampil di overlay
20. Verifikasi overlay tidak menampilkan `Resend Activation Email`
21. Tutup overlay dengan Esc, lalu klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-SU-159: Opsi Resend Activation Email tidak ada di overlay bila seleksi tanpa Pending Activation

22. Centang `John Doe {runId}-038`, `Rina Putri {runId}-038` (bukan Pending Activation)
23. Klik `[Bulk Action ▾]`
24. Verifikasi opsi `Deactivate` tampil di overlay
25. Verifikasi opsi `Resend Activation Email` tidak tampil
26. Tutup overlay dengan Esc, lalu klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-SU-141: Baris Default User Pending Email Confirmation menampilkan Resend Confirmation Email

27. Atur Default User Principal ke Pending Email Confirmation lewat Fixture BE hingga status tersimpan
28. Klik `✕` pada Search, tekan Enter, lalu ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
29. Klik `(⋯)` baris Default User
30. Verifikasi opsi baris Default User: `Detail` | `Resend Confirmation Email`
31. Tutup menu `(⋯)` dengan Esc

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 4, 7, 11, 15, 21, 26, 27, 28, 31 (pencarian baris target lewat Search, penutupan menu atau dialog, pemulihan state, dan kembali ke User List); tanpa `Verifikasi` dan tanpa klaim keadaan.
- Mode: FE+BE. Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md`.
- Urutan TC di spec: 138, 139, 155, 159, 141. TC-141 memakai akun Pre-setup (Default User) sebagai target dan ditaruh terakhir supaya status akun itu hanya diubah di akhir.
- Di TC-155 overlay terbuka bukan anchor yang cukup bagi absence `Resend Activation Email` (bagian 8b butir 2); anchor-nya opsi `Deactivate` yang tampil di overlay untuk seleksi `John Doe {runId}-038` (Activated, Active). Langkah 19 mengikuti Expected TC-155 (opsi `Deactivate` tampil); TC-159 memakai `Deactivate` sebagai anchor menurut Expected TC.
- Temuan untuk QA:
  - TC-141 mensyaratkan Default User Pending Email Confirmation, sedangkan akun Default User Pre-setup #1 dipakai login suite; spec mengubah status akun itu lewat Fixture BE lalu memulihkannya (S-06; pengecualian untuk TC-140/141 sudah tertulis di suite.md). Perlu keputusan QA: user Default User terpisah atau pengecualian tertulis.
  - Post Condition TC-155 ("tidak ada email terkirim", "tidak ada entri log") tidak punya langkah observasi dan tidak diasersi.
