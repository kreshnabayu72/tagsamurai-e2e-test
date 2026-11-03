---
id: TC-GS-NLU-E2E-055-delete-single-screening-dialog-cancel-klik-ganda-dan-delete
title: "Delete Single: Screening Dialog, Cancel, Klik Ganda, dan Delete dari Row serta Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-187
  - TC-GS-NLU-188
  - TC-GS-NLU-189
  - TC-GS-NLU-191
  - TC-GS-NLU-196
coverage:
  web: automated
---

# Delete Single: Screening Dialog, Cancel, Klik Ganda, dan Delete dari Row serta Detail

## Prerequisites

- Mode: FE+BE (backend nyata). Spec menghapus tiga Non-Login User milik spec.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi, tanpa transaksi aset): `Tono Wijaya {runId}-055` (Position Field Technician), `Rani Lestari {runId}-055` (Position Driver, dipakai Delete dari Detail), `Hendra Wijaya {runId}-055` (klik ganda). Pengganti Tono Wijaya, Rani Lestari, dan Hendra Wijaya Pre-setup No. 11 agar record Pre-setup tidak terhapus (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: menghitung jumlah request yang dikirim browser untuk satu aksi Delete tanpa mengubah respons (pemantauan jaringan Spectra, tanpa mengarang endpoint); membuka Modal Changelog agregat (icon Changelog pada Table Tools).
- State global yang diubah: tidak ada. Entri Changelog bersifat permanen; asersi entri memakai nama bersuffix unik (baseline nol).

## Test Steps


### TC-GS-NLU-187: Screening dialog konfirmasi Delete

1. Ketik Search `Tono Wijaya {runId}-055`, tekan Enter
2. Klik `⋯` pada baris `Tono Wijaya {runId}-055` > `Delete`
3. Verifikasi dialog dengan Title `Delete Non-Login User`, body bullet `Tono Wijaya {runId}-055` lalu `All historical records (borrowed/assigned assets) will remain, but this identity cannot be restored. This action cannot be undone. Are you sure you want to delete it?`, dan tombol `[Cancel]` dan `[Delete]`

### TC-GS-NLU-188: Cancel pada dialog Delete

4. Klik area gelap di luar dialog
5. Verifikasi klik backdrop tidak menutup dialog
6. Klik `[Cancel]`
7. Verifikasi dialog tertutup
8. Verifikasi baris `Tono Wijaya {runId}-055` tetap ada di tabel
9. Verifikasi tidak ada toast

### TC-GS-NLU-189: Delete tanpa riwayat aset berhasil

10. Klik `⋯` pada baris `Tono Wijaya {runId}-055` > `Delete`
11. Klik `[Delete]`
12. Verifikasi dialog menutup
13. Verifikasi toast sukses: `Success, non-login user has been deleted.`
14. Verifikasi baris `Tono Wijaya {runId}-055` hilang dari tabel

### TC-GS-NLU-196: Klik ganda cepat pada Delete

15. Ketik Search `Hendra Wijaya {runId}-055`, tekan Enter
16. Klik `⋯` pada baris `Hendra Wijaya {runId}-055` > `Delete`
17. Klik ganda cepat `[Delete]`
18. Verifikasi hanya satu request Delete yang dikirim dan diproses
19. Verifikasi tepat satu toast sukses: `Success, non-login user has been deleted.`
20. Klik icon `Changelog` pada Table Tools untuk membuka Modal Changelog agregat
21. Verifikasi tepat satu entri dengan Action `Delete`, Field `Name`, dan Old Value `Hendra Wijaya {runId}-055`
22. Tutup Modal Changelog dengan `✕`

### TC-GS-NLU-191: Delete dari menu Detail

23. Ketik Search `Rani Lestari {runId}-055`, tekan Enter
24. Klik header kolom `Name` untuk mengurutkan agar state Sort aktif
25. Klik teks Name `Rani Lestari {runId}-055` untuk membuka Detail
26. Klik `⋯` di header > `Delete`
27. Verifikasi dialog dengan Title `Delete Non-Login User`, body bullet `Rani Lestari {runId}-055` lalu `All historical records (borrowed/assigned assets) will remain, but this identity cannot be restored. This action cannot be undone. Are you sure you want to delete it?`, dan tombol `[Cancel]` dan `[Delete]`
28. Klik `[Delete]`
29. Verifikasi toast sukses: `Success, non-login user has been deleted.`
30. Verifikasi halaman kembali ke List Non-Login User
31. Verifikasi Search `Rani Lestari {runId}-055` dan indikator Sort pada kolom `Name` dipertahankan

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 20, 22, 24.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 15, 23.
- Langkah 15 (TC-196) dan 23 (TC-191) memakai Search dan Sort hanya sebagai penghubung; TC-191 tidak menyebut Search, Filter, Sort, atau paginasi mana yang aktif.
- Urutan: screening dan Cancel (TC-187, TC-188) lebih dulu, Delete sukses TC-189 menyusul pada record yang sama (Dependensi TC-189 adalah TC-187), klik ganda TC-196, dan Delete dari Detail TC-191 paling akhir.
- Temuan untuk QA:
  - TC-189 Post Condition (Changelog, Activity Log, System Log aktor mencatat `Delete`; opsi Select User FAMS tidak memuat user) tanpa langkah observasi di TC; tidak diasersi.
  - TC-196 Expected b menyebut "satu entri log `Delete`" tanpa menyebut surface log; spec memakai Modal Changelog agregat karena Tab Changelog Detail tidak dapat dibuka untuk record yang sudah dihapus.
  - TC-191 Expected c menyebut Search, Filter, Sort, dan paginasi "dipertahankan" tanpa menyebut state awalnya; spec hanya mengatur Search dan Sort (Filter dan paginasi default tidak diasersi).
  - TC-196 "hanya satu request diproses" tidak menyebut cara mengamatinya; spec memakai pemantauan jaringan (disediakan tim FE/BE).
