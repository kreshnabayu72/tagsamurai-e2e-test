---
id: TC-GS-USER-E2E-167-dialog-deactivate-peringatan-aset-approval-single-bulk-dan-switch-pending
title: "Dialog Deactivate: Peringatan Aset Aktif dan Approval In-Flight untuk Single dan Bulk, serta Switch Active Tetap Enabled untuk User Pending Activation dan Pending Email Confirmation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1114
  - TC-GS-USER-1111
  - TC-GS-USER-1113
coverage:
  web: automated
---

# Dialog Deactivate: Peringatan Aset Aktif dan Approval In-Flight untuk Single dan Bulk, serta Switch Active Tetap Enabled untuk User Pending Activation dan Pending Email Confirmation

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tidak dipakai sebagai target aksi dan tidak diubah (S-06); spec memakai padanan seed bersuffix.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Division `Finance`, Access `Fixed Asset`, email `<nama tanpa spasi huruf kecil>+{runId}-167@qwertysystem.net`:
  - `Mike Tan {runId}-167`: Active (Global), Pending Activation (TC-GS-USER-1114).
  - `Rina Putri {runId}-167`: Activated dengan email pending `rinaputri.new+{runId}-167@qwertysystem.net`, sehingga berstatus Pending Email Confirmation (TC-GS-USER-1114).
  - `Joko Susilo {runId}-167`: Active, memegang aset Borrowed dan approver pada approval in-flight (TC-GS-USER-1111 dan TC-GS-USER-1113). Seeding aset Borrowed dan approval in-flight disediakan tim FE/BE.
  - `Dewi Lestari {runId}-167`: Active, tanpa aset aktif dan tanpa approval in-flight (TC-GS-USER-1113).
- Kemampuan teknis: hover pada switch Active untuk mengamati ada atau tidaknya tooltip; membaca isi dialog bulk per kelompok (kelompok pemegang aset dan kelompok approver in-flight).
- State global yang diubah: tidak ada. Dialog Deactivate tidak pernah dikonfirmasi (selalu `[Cancel]`), sehingga status keempat user tidak berubah. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus keempat user seed lewat API, bersihkan seleksi dan Search.

## Test Steps

### Persiapan

1. Ketik Search `{runId}-167`, tekan Enter

### TC-GS-USER-1114: Switch Active tetap Enabled untuk user Pending Activation dan Pending Email Confirmation

2. Hover switch Active baris `Mike Tan {runId}-167`
3. Verifikasi switch Active baris `Mike Tan {runId}-167` Enabled tanpa tooltip
4. Hover switch Active baris `Rina Putri {runId}-167`
5. Verifikasi switch Active baris `Rina Putri {runId}-167` Enabled tanpa tooltip
6. Ganti isi kotak search dengan `Mike Tan {runId}-167`, tekan Enter
7. Klik Name `Mike Tan {runId}-167` di User List
8. Verifikasi switch Active header Detail `Mike Tan {runId}-167` Enabled
9. Klik switch Active header Detail
10. Verifikasi dialog Deactivate tampil dengan Title `Deactivate User`
11. Klik `[Cancel]`

### TC-GS-USER-1111: Dialog Deactivate untuk target pemegang aset aktif menampilkan peringatan aset tanpa angka

12. Klik menu User di sidebar Global Settings
13. Ketik Search `{runId}-167`, tekan Enter
14. Klik switch Active baris `Joko Susilo {runId}-167`
15. Verifikasi dialog: Title `Deactivate User`; body `• Joko Susilo {runId}-167` dan `This will deactivate user across all products. This user will be immediately logged out.`
16. Verifikasi baris peringatan aset `Joko Susilo {runId}-167 is currently holding active assets (Borrowed / Assigned). Asset custody will remain recorded under this user until manually transferred or returned.`
17. Verifikasi baris peringatan aset tanpa angka jumlah aset
18. Verifikasi baris approval `Pending approvals of this user will be reassigned to other approvers.` tampil terpisah dari baris aset
19. Verifikasi dialog ditutup `Are you sure you want to deactivate it?` dengan tombol `[Cancel]` dan `[Deactivate]`
20. Verifikasi baris fallback `We couldn't check this user's active assets or pending approvals. You can still continue.` tidak tampil
21. Klik `[Cancel]`

### TC-GS-USER-1113: Dialog Bulk Deactivate memisahkan kelompok pemegang aset aktif dan approver in-flight

22. Centang baris `Dewi Lestari {runId}-167`
23. Centang baris `Joko Susilo {runId}-167`
24. Klik `Bulk Action` lalu opsi `Deactivate`
25. Verifikasi dialog `Deactivate Users`: bullet `• Dewi Lestari {runId}-167` dan `• Joko Susilo {runId}-167`, serta `These users will be immediately logged out.`
26. Verifikasi kelompok `The following users are currently holding active assets (Borrowed / Assigned). Asset custody will remain recorded under each user until manually transferred or returned:` tampil
27. Verifikasi kelompok pemegang aset memuat `• Joko Susilo {runId}-167`
28. Verifikasi kelompok pemegang aset tidak memuat `• Dewi Lestari {runId}-167`
29. Verifikasi kelompok approver in-flight memuat `• Joko Susilo {runId}-167`
30. Verifikasi kelompok approver in-flight tidak memuat `• Dewi Lestari {runId}-167`
31. Verifikasi kelompok approver in-flight tanpa angka jumlah
32. Verifikasi dialog ditutup `Are you sure you want to deactivate them?`
33. Klik `[Cancel]`
34. Klik icon `×` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec 34 langkah, di bawah ambang sekitar 35. Urutan TC sumber diubah: TC-GS-USER-1114 (baca saja) di awal, lalu TC-GS-USER-1111 (single) dan TC-GS-USER-1113 (bulk) pada user seed yang sama; tidak ada TC yang menghapus data atau mengubah status user.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1, 6, 13 (Search), 2, 4 (hover sebagai pemicu asersi tooltip, bagian 8b butir 5), 9 (klik switch header sebagai pemicu dialog), 11, 21, dan 33 (`[Cancel]` menutup dialog; aksi Deactivate tidak pernah dikonfirmasi), 12 (kembali ke User List lewat menu User), 22 dan 23 (centang baris), 24 (membuka dialog), dan 34 (membersihkan seleksi, S-09).
- Search `{runId}-167` pada langkah 1 dan 13 menampilkan keempat user seed dalam satu halaman, sehingga aksi pada baris `Joko Susilo`, `Dewi Lestari`, `Mike Tan`, dan `Rina Putri` tidak bergantung pada posisi halaman (bagian 8b butir 12). Langkah 7 (Klik Name pada tabel yang dapat memuat lebih dari satu halaman) didahului Search nama baris pada langkah 6 (R-16, R-23).
- Asersi absence (langkah 20, 28, dan 30) berada pada dialog yang sudah menampilkan pembandingnya pada langkah sebelumnya (langkah 15 sampai 19; langkah 25 sampai 27 dan 29).
- Pembagian TC lintas spec: dialog Deactivate dengan pemeriksaan aset atau approval gagal (TC-GS-USER-1112) diverifikasi di spec 169; dialog Deactivate dasar tanpa aset ada di spec 047; aksi Bulk Deactivate yang dikonfirmasi ada di spec 054.
- Temuan untuk QA:
  - TC-GS-USER-1113 Expected c tidak menuliskan teks heading kelompok approver in-flight; spec mengasersi keanggotaan kelompok (hanya Joko Susilo) dan ketiadaan angka, tanpa teks heading. Teks heading perlu dikonfirmasi QA (Need Confirmation).
  - TC-GS-USER-1114 langkah 3 ("Klik switch Active Mike Tan") tidak menyebut lokasi (List atau header Detail) setelah langkah 2 membuka Detail; spec mengklik switch header Detail. Parenthetical "Mike Tan berstatus Active Global" pada Expected c tidak diasersi terpisah (state seed).
  - TC-GS-USER-1111 Expected e ("Baris fallback tidak tampil") tidak menuliskan teks baris fallback; spec memakai teks dari TC-GS-USER-1112 Expected a.
  - TC-GS-USER-1111 dan TC-GS-USER-1113 memakai Joko Susilo dan Dewi Lestari Pre-setup (No. 19 dan No. 12); spec memakai seed bersuffix milik spec (S-06, S-12).
