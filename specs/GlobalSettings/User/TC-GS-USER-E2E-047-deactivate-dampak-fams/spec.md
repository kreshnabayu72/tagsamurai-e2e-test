---
id: TC-GS-USER-E2E-047-deactivate-dampak-fams
title: User yang dinonaktifkan hilang dari pilihan transaksi baru di Fixed Asset
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-388
  - TC-GS-USER-579
  - TC-GS-USER-580
coverage:
  web: automated
---

# User yang dinonaktifkan hilang dari pilihan transaksi baru di Fixed Asset

## Prerequisites

- Login sebagai Role: Total Control, dengan akses ke Global Settings dan Fixed Asset (FAMS)
- User "Wahyu Transaksi" Active, dan punya riwayat di FAMS: satu Assignment lama atas namanya (assignee), satu transaksi Borrow lama (peminjam), dan berperan sebagai approver aktif
- Spec ini menonaktifkan "Wahyu Transaksi", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Sebelum dinonaktifkan

1. Buka Fixed Asset > Assignment, mulai Request Assignment baru, dan buka Modal Select Assignee Picker
2. Verifikasi "Wahyu Transaksi" muncul di daftar, lalu tutup modal tanpa memilih
3. Buka Fixed Asset > Borrow, mulai Request Borrow baru, dan buka Modal Select User
4. Verifikasi "Wahyu Transaksi" muncul di daftar, lalu tutup modal tanpa memilih
5. Buka dropdown pemilihan approver pada transaksi baru dan verifikasi "Wahyu Transaksi" muncul

### Dinonaktifkan

6. Di Global Settings > User, klik Toggle Active [Global] pada baris "Wahyu Transaksi" untuk mematikannya, lalu klik `[Deactivate]` pada dialog
7. Verifikasi toast "Success, user has been deactivated." muncul

### Sesudah dinonaktifkan

8. Buka Fixed Asset > Assignment, mulai Request Assignment baru, buka Modal Select Assignee Picker, dan cari "Wahyu Transaksi"
9. Verifikasi "Wahyu Transaksi" tidak tampil, tanpa perlu memuat ulang halaman
10. Buka Fixed Asset > Borrow, mulai Request Borrow baru, buka Modal Select User, dan cari "Wahyu Transaksi"
11. Verifikasi "Wahyu Transaksi" tidak tampil sebagai calon peminjam
12. Buka dropdown pemilihan approver pada transaksi baru dan verifikasi "Wahyu Transaksi" tidak tampil
13. Buka daftar Assignment dan verifikasi kolom Assignee / Custodian pada assignment lama masih memuat nama "Wahyu Transaksi"
14. Buka Fixed Asset > Borrow, tab Borrowed (By Borrower), dan verifikasi transaksi Borrow lama masih menampilkan nama "Wahyu Transaksi"
15. Verifikasi approval dan aset lama milik "Wahyu Transaksi" tetap tersimpan tanpa berubah

## Notes

- Yang diuji adalah dampak ke pemilihan transaksi baru, bukan badge approval in-flight yang ikut disabled (itu dicakup `TC-GS-USER-91`, dan `TC-GS-USER-480` di `TC-GS-USER-E2E-008-toggle-active-user`).
- TC-388 adalah payung, dan TC-579 (Assignee Picker) serta TC-580 (Select User peminjam) adalah pecahannya. Ketiganya dicakup di langkah 8 sampai 15.
- Spec ini butuh akses ke dua aplikasi dan data riwayat FAMS. Kebutuhan itu ditulis di Prerequisites untuk tim FE.
