---
id: TC-GS-USER-E2E-055-bulk-delete-homogen-campuran-dan-cancel
title: "Bulk Delete: Cancel Tidak Menghapus, Dialog Gabungan Aset dan Approval, NLU Terdampak, dan Semua Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-299
  - TC-GS-USER-300
  - TC-GS-USER-301
  - TC-GS-USER-1028
coverage:
  web: automated
---

# Bulk Delete: Cancel Tidak Menghapus, Dialog Gabungan Aset dan Approval, NLU Terdampak, dan Semua Berhasil

## Prerequisites

- Mode: FE+BE. Spec menghapus data (Bulk Delete, aksi destruktif) sehingga dijalankan terakhir dan serial, sesudah spec lain selesai (suite `parallel: false`).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22) tidak dipakai sebagai target aksi dan tidak diubah.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Semua user Activated, Active, Division `Finance`, Access `Fixed Asset`, email `<name tanpa spasi huruf kecil>+{runId}-055@qwertysystem.net`:
  - T-1: Name `Tono Wijaya {runId}-055`, tanpa aset dan approval (Data Dinamis No. 4).
  - R-1: Name `Rani Lestari {runId}-055`, tanpa aset dan approval (Data Dinamis No. 4).
  - J-1: Name `Joko Susilo {runId}-055`, punya borrowed asset (HK8; seeding aset disediakan tim FE/BE).
  - A-1: Name `Ahmad Fauzi {runId}-055`, mewakili Non-Login User N-1 `Agus Prasetyo {runId}-055` (Represented By A-1; HK8).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus T-1, R-1, J-1, A-1, dan N-1 lewat API bila masih ada, bersihkan seleksi, dan kosongkan Search.
- State global yang diubah: tidak ada. Spec hanya menghapus T-1 dan R-1 (langkah 27); J-1 dan A-1 hanya muncul di dialog dan dibatalkan.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-055`, tekan Enter

### TC-GS-USER-1028: Bulk Delete dialog [Cancel] tidak menghapus dan tidak mereset seleksi

2. Centang baris `Tono Wijaya {runId}-055` dan `Rani Lestari {runId}-055`
3. Klik `Bulk Action` lalu opsi `Delete`
4. Klik `[Cancel]`
5. Verifikasi dialog tertutup
6. Verifikasi tidak ada toast
7. Verifikasi kedua baris tetap ada
8. Verifikasi kedua baris tetap tercentang
9. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-300: Bulk Delete campuran user dengan aset, satu dialog gabungan tanpa angka

10. Centang baris `Joko Susilo {runId}-055` (punya aset) dan `Tono Wijaya {runId}-055`
11. Klik `Bulk Action` lalu opsi `Delete`
12. Verifikasi satu daftar bullet nama `Joko Susilo {runId}-055` dan `Tono Wijaya {runId}-055`
13. Verifikasi daftar tanpa angka jumlah aset atau approval
14. Verifikasi dialog tanpa kelompok skipped
15. Verifikasi tombol `[Cancel]` dan `[Delete]`
16. Klik `[Cancel]`
17. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-301: Bulk Delete dengan user yang mewakili NLU menyebut semua NLU terdampak

18. Centang baris `Ahmad Fauzi {runId}-055` dan `Tono Wijaya {runId}-055`
19. Klik `Bulk Action` lalu opsi `Delete`
20. Verifikasi dialog menambah `Represented By will be cleared for the following non-login user(s):`
21. Verifikasi dialog memuat bullet `• Agus Prasetyo {runId}-055`
22. Klik `[Cancel]`
23. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-299: Bulk Delete, semua berhasil

24. Centang baris `Tono Wijaya {runId}-055` dan `Rani Lestari {runId}-055`
25. Klik `Bulk Action` lalu opsi `Delete`
26. Verifikasi dialog memuat bullet `Tono Wijaya {runId}-055` dan `Rani Lestari {runId}-055`
27. Klik `[Delete]`
28. Verifikasi toast sukses "Success, user has been deleted."
29. Verifikasi baris `Joko Susilo {runId}-055` dan `Ahmad Fauzi {runId}-055` tampil di tabel (pembanding)
30. Verifikasi baris `Tono Wijaya {runId}-055` hilang
31. Verifikasi baris `Rani Lestari {runId}-055` hilang
32. Verifikasi bar hilang

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-GS-USER-1028 (Cancel) dan TC-GS-USER-300 dan 301 (dialog saja, ditutup dengan `[Cancel]`) mendahului TC-GS-USER-299 karena memakai `Tono Wijaya {runId}-055` yang dihapus TC-GS-USER-299; aksi yang menghapus data paling akhir (bagian 3 prinsip 5). Spec ini berjalan terakhir dan serial dalam suite karena Bulk Delete adalah aksi destruktif.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (Search), 4, 16, dan 22 (menutup dialog dengan `[Cancel]`), 9, 17, dan 23 (membersihkan seleksi dengan icon `×`, S-09).
- Asersi tambahan: langkah 29 (baris pembanding sebelum asersi baris hilang, bagian 8b butir 2); langkah 13 dan 14 memecah Expected TC-GS-USER-300 ("tanpa angka", "tanpa kelompok skipped") dan didahului langkah 12 yang menampilkan daftar bullet pada dialog yang sama.
- Pembagian TC: Bulk Delete dengan kegagalan sebagian dan partial (toast T-13) serta Bulk Delete gagal 5xx diverifikasi di spec resilience; log Bulk Delete diverifikasi di spec pencatatan log.
- Temuan untuk QA:
  - TC-GS-USER-300 dan TC-GS-USER-301 hanya menyebut dialog dan tidak menyebut apakah `[Delete]` dikonfirmasi; spec membatalkan dialog dengan `[Cancel]` supaya data seed tetap ada untuk TC berikutnya (konfirmasi Delete user dengan aset dan NLU dicakup spec 050).
  - TC-GS-USER-301 tidak menyebut Title dialog; spec tidak mengasersi Title.
  - TC-GS-USER-300 butir ("tanpa angka jumlah", "tanpa kelompok skipped") adalah asersi absence tanpa pembanding spesifik di TC; spec mengasersinya sesudah daftar bullet tampil pada dialog yang sama.
  - TC-GS-USER-299 dan TC-GS-USER-1028 mensyaratkan `Tono Wijaya` dan `Rani Lestari` "disiapkan sebelum eksekusi" (Data Dinamis No. 4) tanpa menyebut cara; spec men-seed lewat API dengan suffix `{runId}-055`.
  - TC-GS-USER-299, 300, 301, dan 1028 tanpa Post Condition.
