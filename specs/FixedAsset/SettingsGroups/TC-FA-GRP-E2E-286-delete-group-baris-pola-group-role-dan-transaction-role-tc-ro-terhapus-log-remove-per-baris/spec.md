---
id: TC-FA-GRP-E2E-286-delete-group-baris-pola-group-role-dan-transaction-role-tc-ro-terhapus-log-remove-per-baris
title: "Delete Group: Baris Pola Group Role dan Transaction Role Total Control/Read Only pada Node dan Descendant Terhapus dalam Satu Transaksi dengan Log Remove (Group Deleted) per Baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1290
coverage:
  web: automated
---

# Delete Group: Baris Pola Group Role dan Transaction Role Total Control/Read Only pada Node dan Descendant Terhapus dalam Satu Transaksi dengan Log Remove (Group Deleted) per Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): user Total Control No 1, Default User No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net`, dan Read Only No 3 `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`.
- Data Dinamis (Pre-setup tambahan, di-seed lewat sesi API aktor di hook `before` sebagai Create Group biasa sehingga baris pola Group Role dan Transaction Role untuk user Total Control dan Read Only terbentuk sendiri; dihapus di hook `after` bila masih ada): node `Del Pola {runId}-286` (level 1) dengan satu descendant `Del Pola Anak {runId}-286`. Pembentukan baris pola itu dipakai sebagai precondition TC-FA-GRP-1290; jumlahnya dibaca di langkah 1 untuk asersi log.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role dan tab Transaction Role (Settings > Role & Permission) per node dan per user termasuk node yang sudah dihapus, serta log Role & Permission (Action, Modified By, penanda nama node). Baseline entri log dibaca lewat kemampuan yang sama.

## Test Steps

1. Baca tab Group Role dan tab Transaction Role pada `Del Pola {runId}-286` dan `Del Pola Anak {runId}-286` untuk user Total Control (Pre-setup No 1 dan Default User) dan Read Only (Pre-setup No 3), lalu catat jumlah baris pola Group Role dan Transaction Role pada kedua node sebagai N
2. Verifikasi kedua node memuat baris pola Group Role dan Transaction Role untuk user Total Control dan Read Only (jumlah N lebih dari nol)
3. Baca log Role & Permission untuk entri `Remove (Group Deleted)` yang memuat nama `Del Pola {runId}-286` atau `Del Pola Anak {runId}-286`, lalu catat jumlahnya sebagai baseline
4. Ketik Search `Del Pola {runId}-286`, tekan Enter
5. Buka elipsis `Del Pola {runId}-286`, pilih Delete
6. Klik [Delete]
7. Verifikasi toast sukses `Success, group has been deleted.`
8. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Del Pola {runId}-286` (node terhapus)
9. Ganti isi kotak search dengan `Del Pola Anak {runId}-286`, tekan Enter
10. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Del Pola Anak {runId}-286` (descendant terhapus)
11. Baca tab Group Role pada kedua node untuk user Total Control dan Read Only
12. Verifikasi tidak ada sisa baris Group Role untuk user Total Control dan Read Only pada kedua node
13. Baca tab Transaction Role pada kedua node untuk user Total Control dan Read Only
14. Verifikasi tidak ada sisa baris Transaction Role (Asset Admin, Approver, Monitoring & Report) untuk user Total Control dan Read Only pada kedua node
15. Baca log Role & Permission untuk entri `Remove (Group Deleted)` yang memuat nama kedua node
16. Verifikasi jumlah entri `Remove (Group Deleted)` bertambah tepat N dibanding baseline langkah 3, yaitu satu entri per baris pola Group Role dan Transaction Role yang terhapus (bukan satu entri ringkas)
17. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 1 dan 3 (pembacaan precondition dan baseline), langkah 4 dan 9 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), langkah 11, 13, dan 15 (observasi lewat kemampuan baca), dan langkah 17 (menutup Search).
- Aksi hapus (langkah 6) diletakkan sesudah pembacaan precondition dan baseline karena menghapus data (S-10). Asersi "tidak ada sisa baris" (langkah 12 dan 14) memakai toast sukses Delete (langkah 7) dan empty state Search (langkah 8 dan 10) sebagai anchor.
- Temuan untuk QA:
  - TC-1290 Expected c menyebut "satu entri per baris pola yang terhapus" tanpa menyebut jumlah barisnya; spec membaca N dari precondition sebelum Delete (langkah 1) dan mengasersi selisih entri terhadap baseline (S-12).
  - TC-1290 langkah 2 dan 3 membaca Role & Permission dan log untuk node yang sudah terhapus; pembacaan node terhapus memakai kemampuan baca yang disediakan tim FE/BE karena UI tidak lagi menampilkan node itu.
  - Atomisitas "dalam satu transaksi" (judul TC) tidak teramati dari UI; spec mengasersi hasil akhirnya (tidak ada sisa baris pada node dan descendant).
