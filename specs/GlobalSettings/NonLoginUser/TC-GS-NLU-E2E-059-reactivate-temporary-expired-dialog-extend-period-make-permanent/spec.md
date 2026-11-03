---
id: TC-GS-NLU-E2E-059-reactivate-temporary-expired-dialog-extend-period-make-permanent
title: "Reactivate Temporary-expired: Dialog, Extend Period, dan Make Permanent"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-204
  - TC-GS-NLU-205
  - TC-GS-NLU-206
  - TC-GS-NLU-207
coverage:
  web: automated
---

# Reactivate Temporary-expired: Dialog, Extend Period, dan Make Permanent

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Inactive, Temporary-expired, Division Operations, Represented By Ahmad Fauzi): `Agus Salim {runId}-059` (Position Contractor; dialog dan error inline), `Reaktif Satu {runId}-059` (Extend period), `Reaktif Dua {runId}-059` (Make permanent). Pengganti Agus Salim, Reaktif Satu, dan Reaktif Dua Pre-setup No. 11 karena spec mengubah statusnya (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Tanggal besok dihitung dari tanggal hari ini pada zona waktu client (Timezone `Asia/Jakarta`, Pre-setup No. 16); format tampil Temporary until mengikuti Date Format General Settings client.
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-204: Dialog Reactivate Temporary User

1. Ketik Search `Agus Salim {runId}-059`, tekan Enter
2. Klik switch Active pada baris `Agus Salim {runId}-059` (OFF, Temporary-expired)
3. Verifikasi dialog dengan Title `Reactivate Temporary User` menggantikan dialog Activate
4. Verifikasi body dialog: bullet `Agus Salim {runId}-059` dan `This user's active period has ended. Choose how to reactivate:`
5. Verifikasi opsi A `Extend period` dengan date picker tanggal mendatang
6. Verifikasi opsi B `Make permanent`
7. Verifikasi `[Reactivate]` Disabled sampai satu opsi dipilih
8. Verifikasi tombol `[Cancel]` tampil

### TC-GS-NLU-206: Extend period tanpa tanggal

9. Pilih opsi `Extend period` tanpa memilih tanggal
10. Klik `[Reactivate]`
11. Verifikasi pesan inline di bawah field tanggal: `Please select a future date.`
12. Verifikasi dialog tetap terbuka
13. Verifikasi user tetap Inactive (switch baris OFF)
14. Klik `[Cancel]` untuk menutup dialog

### TC-GS-NLU-205: Reactivate dengan Extend period

15. Ganti isi kotak search dengan `Reaktif Satu {runId}-059`, tekan Enter
16. Klik switch Active pada baris `Reaktif Satu {runId}-059`
17. Pilih opsi `Extend period`, pilih tanggal besok
18. Klik `[Reactivate]`
19. Verifikasi dialog menutup
20. Verifikasi toast sukses: `Success, non-login user has been activated.`
21. Verifikasi switch baris menjadi ON
22. Klik teks Name `Reaktif Satu {runId}-059` untuk membuka Detail
23. Verifikasi Temporary until pada Detail menjadi tanggal besok (format Date Format General Settings)
24. Verifikasi user tetap Temporary User (teks `Temporary until` tampil di bawah Represented By)
25. Kembali ke list Non-Login User

### TC-GS-NLU-207: Reactivate dengan Make permanent

26. Ganti isi kotak search dengan `Reaktif Dua {runId}-059`, tekan Enter
27. Klik switch Active pada baris `Reaktif Dua {runId}-059`
28. Pilih opsi `Make permanent`
29. Klik `[Reactivate]`
30. Verifikasi toast sukses: `Success, non-login user has been activated.`
31. Verifikasi switch baris menjadi ON
32. Klik teks Name `Reaktif Dua {runId}-059` untuk membuka Detail
33. Verifikasi General Information Detail tampil (anchor)
34. Verifikasi teks `Temporary until` tidak tampil di bawah Represented By (Temporary Until kosong dan user bukan Temporary User)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 14, 22, 25, 32.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 15, 26.
- TC-205 dan TC-207 Expected tentang Temporary Until dan status Temporary User diamati di Detail (teks `Temporary until` di bawah Represented By, TC-251) karena kolom Temporary Until tidak tampil secara default di List.
- Urutan: TC-206 diletakkan sebelum TC-205 karena error inline dan penutupan dialog dengan `[Cancel]` terjadi pada record `Agus Salim` yang sama dengan TC-204; validasi diblokir lebih dulu daripada aksi sukses (S-10).
- Pembagian TC lintas spec: Cancel pada dialog Reactivate (TC-208) dan tanggal ditolak (TC-209, TC-467) ada di spec 060.
- Temuan untuk QA:
  - TC-205 dan TC-207 tidak menyebut tempat mengamati Temporary Until dan status Temporary User; spec memakai Detail.
  - TC-204 Expected c: "date picker tanggal mendatang" tidak menyebut tanggal pertama yang dapat dipilih; spec hanya memverifikasi keberadaan opsi dan date picker.
