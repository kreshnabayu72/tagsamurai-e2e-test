---
id: TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi
title: "Opsi Bulk Action per Kombinasi Status Seleksi: Activate, Deactivate, Delete, dan Resend Activation Email"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-285
  - TC-GS-USER-286
  - TC-GS-USER-287
  - TC-GS-USER-288
  - TC-GS-USER-289
  - TC-GS-USER-290
  - TC-GS-USER-1045
coverage:
  web: automated
---

# Opsi Bulk Action per Kombinasi Status Seleksi: Activate, Deactivate, Delete, dan Resend Activation Email

## Prerequisites

- Mode: FE+BE. Spec hanya memilih baris dan membuka dropdown `Bulk Action`; tidak ada aksi yang dikonfirmasi dan tidak ada data diubah atau dihapus.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22) tidak dipakai dan tidak diubah (S-06).
- Data Dinamis, 7 user milik spec, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Division `Finance`, Access `Fixed Asset`, email `<name tanpa spasi huruf kecil>+{runId}-052@qwertysystem.net`:
  - `Dewi Lestari {runId}-052`: Activated, Active.
  - `Ahmad Fauzi {runId}-052`: Activated, Active.
  - `Jane Smith {runId}-052`: Activated, Inactive (dinonaktifkan manual).
  - `Budi Hartono {runId}-052`: Activated, Inactive, Temporary-expired (cara membuat Temporary Until yang sudah terlewati lewat seeding disediakan tim FE/BE).
  - `Mike Tan {runId}-052`: Pending Activation.
  - `Andre Kurniawan {runId}-052`: Pending Activation.
  - `Rina Putri {runId}-052`: Activated, dengan email pending `rinaputri.new+{runId}-052@qwertysystem.net` (seeding Pending Email Change disediakan tim FE/BE).
  - Dengan Search `{runId}-052`, tabel menampilkan 7 baris pada satu halaman.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus 7 user seed lewat API, bersihkan seleksi, tutup dropdown, kosongkan Search.
- Kemampuan teknis: membaca ikon dan severity opsi pada dropdown `Bulk Action` (CheckLine, CloseLine, DeleteBin6Line, MailSendLine); menutup dropdown dengan Esc.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-052`, tekan Enter

### TC-GS-USER-285: Opsi Bulk Action untuk seleksi Dewi Lestari (Active) dan Jane Smith (Inactive)

2. Centang baris `Dewi Lestari {runId}-052` (Active)
3. Centang baris `Jane Smith {runId}-052` (Inactive)
4. Klik `Bulk Action`
5. Verifikasi opsi `Activate` (CheckLine), `Deactivate` (CloseLine), dan `Delete` (DeleteBin6Line, danger, paling akhir)
6. Verifikasi opsi `Resend Activation Email` tidak tampil
7. Tutup dropdown `Bulk Action` dengan Esc
8. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-286: Opsi Bulk Action untuk seleksi Dewi Lestari dan Ahmad Fauzi (semua Active)

9. Centang baris `Dewi Lestari {runId}-052` dan `Ahmad Fauzi {runId}-052`
10. Klik `Bulk Action`
11. Verifikasi opsi `Deactivate` dan `Delete`
12. Verifikasi opsi `Activate` Hidden
13. Tutup dropdown `Bulk Action` dengan Esc
14. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-287: Opsi Bulk Action untuk seleksi Jane Smith dan Budi Hartono (semua Inactive)

15. Centang baris `Jane Smith {runId}-052` dan `Budi Hartono {runId}-052`
16. Klik `Bulk Action`
17. Verifikasi opsi `Activate` dan `Delete`
18. Verifikasi opsi `Deactivate` Hidden
19. Tutup dropdown `Bulk Action` dengan Esc
20. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-288: Opsi Bulk Action untuk seleksi Mike Tan dan user Pending Activation lain Andre Kurniawan

21. Centang baris `Mike Tan {runId}-052` dan `Andre Kurniawan {runId}-052`
22. Klik `Bulk Action`
23. Verifikasi opsi `Resend Activation Email` (MailSendLine) tampil
24. Tutup dropdown `Bulk Action` dengan Esc
25. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-289: Opsi Bulk Action untuk seleksi Mike Tan (Pending) dan Dewi Lestari (Activated)

26. Centang baris `Mike Tan {runId}-052` (Pending Activation) dan `Dewi Lestari {runId}-052` (Activated)
27. Klik `Bulk Action`
28. Verifikasi opsi `Delete` tampil (pembanding)
29. Verifikasi opsi `Resend Activation Email` Hidden
30. Tutup dropdown `Bulk Action` dengan Esc
31. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-290: Opsi Bulk Action untuk seleksi Rina Putri (email pending) dan Dewi Lestari

32. Centang baris `Rina Putri {runId}-052` (email pending) dan `Dewi Lestari {runId}-052`
33. Klik `Bulk Action`
34. Verifikasi opsi `Delete` tampil (pembanding)
35. Verifikasi opsi `Resend Confirmation Email` tidak tampil
36. Tutup dropdown `Bulk Action` dengan Esc
37. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-1045: Opsi Bulk Action untuk seleksi Active dan Temporary-expired saja

38. Centang baris `Dewi Lestari {runId}-052` (Active) dan `Budi Hartono {runId}-052` (Temporary-expired, Inactive)
39. Klik `Bulk Action`
40. Verifikasi opsi `Deactivate` (CloseLine) tampil
41. Verifikasi opsi `Activate` tidak tampil
42. Verifikasi opsi `Resend Activation Email` tidak tampil
43. Tutup dropdown `Bulk Action` dengan Esc
44. Klik icon `×` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Seluruh TC adalah tampilan opsi dropdown yang ditentukan status baris di backend.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (44 langkah) karena tujuh TC opsi Bulk Action berada di satu kelas harness (fungsional), satu layar, dan satu dataset 7 user seed milik spec. Tiap blok berdiri sendiri pada kombinasi seleksi sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan memisahkannya mengulang login, seeding, dan Search yang sama.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (Search), 7, 13, 19, 24, 30, 36, 43 (menutup dropdown dengan Esc), 8, 14, 20, 25, 31, 37, 44 (membersihkan seleksi dengan icon `×`, S-09).
- Asersi tambahan: langkah 28 dan 34 (opsi `Delete` tampil) adalah pembanding sebelum asersi opsi yang tidak tampil (bagian 8b butir 2); pada TC lain pembanding adalah opsi yang diasersi tampil lebih dulu pada dropdown yang sama. TC-GS-USER-1045 mengasersi `Deactivate` tampil sebelum `Activate` tidak tampil supaya pembanding tampil lebih dulu.
- Pembagian TC: dialog dan hasil aksi Bulk Activate, Deactivate, dan Delete diverifikasi di spec 054 dan 055; Bulk Resend Activation Email diverifikasi di spec 056.
- Temuan untuk QA:
  - TC-GS-USER-285 sampai 290 dan TC-GS-USER-1045 memakai user Pre-setup (Dewi Lestari, Jane Smith, Ahmad Fauzi, Budi Hartono, Mike Tan, Rina Putri) dan `Andre Kurniawan` (Data Dinamis No. 2, dibuat TC-GS-USER-138, bukan Pre-setup); spec memakai seed milik spec bersuffix `{runId}-052`. TC tidak menyebut cara seeding user Pending Activation, Temporary-expired, dan email pending.
  - TC-GS-USER-285 menyebut `Delete` "paling akhir" tanpa menyebut urutan `Activate` dan `Deactivate`; spec mengasersi urutan sesuai Expected.
  - TC-GS-USER-290 menyebut `Resend Confirmation Email` "tidak pernah tampil" tanpa alasan; spec hanya mengasersi ketiadaannya pada seleksi itu.
  - TC-GS-USER-285 sampai 290 dan TC-GS-USER-1045 tanpa Post Condition.
