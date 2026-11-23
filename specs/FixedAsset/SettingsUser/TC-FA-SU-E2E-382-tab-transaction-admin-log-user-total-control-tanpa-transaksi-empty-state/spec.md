---
id: TC-FA-SU-E2E-382-tab-transaction-admin-log-user-total-control-tanpa-transaksi-empty-state
title: "Tab Transaction Admin Log User Total Control Tanpa Transaksi: Empty State"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1075
coverage:
  web: automated
---

# Tab Transaction Admin Log User Total Control Tanpa Transaksi: Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan penugasan (Pre-setup #23).
- Pengguna target: Lina Marlina, Total Control (Pre-setup #1 dan #23) dengan baris pola Asset Admin pada setiap Jenis Transaksi x Group, yang belum memproses transaksi apa pun sebagai PIC (tanpa seed log transaksi).
- Data uji: tidak ada log transaksi untuk Lina Marlina sebagai PIC; spec tidak membuat atau mengubah data.
- Kemampuan teknis (disediakan tim FE/BE): pembacaan state BE untuk memastikan Lina Marlina belum memiliki log transaksi sebagai PIC sebelum aksi (kondisi data sendiri, prinsip 12).
- State global yang diubah: tidak ada; tidak butuh pemulihan.
- Fixture: nama pengguna dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1075: Tab Transaction Admin Log user Total Control dengan baris pola Transaction Role yang belum memproses transaksi: baris pola tidak membuat user dianggap PIC, empty state S-27a

1. Verifikasi Lina Marlina belum memiliki log transaksi sebagai PIC lewat kemampuan baca BE
2. Ketik Search `Lina Marlina`, tekan Enter, lalu klik Name `Lina Marlina`
3. Klik Tab Transaction Admin Log
4. Verifikasi Sub-tab Borrow, Assignment, Transfer, dan Disposal tampil
5. Verifikasi Sub-tab Borrow menampilkan ilustrasi empty state dengan Title `No transaction log yet`
6. Verifikasi Description `Transactions this user has processed as PIC will appear here.`
7. Verifikasi empty state bukan `No results found`
8. Klik Sub-tab Assignment
9. Verifikasi Sub-tab Assignment menampilkan empty state dengan Title `No transaction log yet` dan Description `Transactions this user has processed as PIC will appear here.`
10. Klik Sub-tab Transfer
11. Verifikasi Sub-tab Transfer menampilkan empty state dengan Title `No transaction log yet` dan Description `Transactions this user has processed as PIC will appear here.`
12. Klik Sub-tab Disposal
13. Verifikasi Sub-tab Disposal menampilkan empty state dengan Title `No transaction log yet` dan Description `Transactions this user has processed as PIC will appear here.`
14. Verifikasi tidak ada baris log yang muncul akibat baris pola Asset Admin pada keempat sub-tab
15. Klik Tab Role lalu Sub-tab Transaction Role
16. Verifikasi Sub-tab Transaction Role Lina Marlina menampilkan baris pola tier

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 2. Search `Lina Marlina` pada langkah 2 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Langkah 1 memenuhi precondition (d) TC lewat kemampuan baca BE.
- Asersi "tidak ada baris log" (langkah 14) didahului `Verifikasi` empty state `No transaction log yet` yang tampil pada tiap sub-tab (langkah 5, 9, 11 dan 13) serta Sub-tab Transaction Role yang masih memuat baris pola pada akhir alur (langkah 16); spec fungsional ini mengasersi empty state, bukan absence log kelas g.
- Temuan untuk QA:
  - TC-FA-SU-1075 ACC menyebut `#20` (id Client `FaUserMain`, bukan nomor akun); aktor diambil dari Pre-setup #2 (Default User) pada precondition (a). Mohon dikonfirmasi.
  - TC-FA-SU-1075 precondition (d) mensyaratkan Lina Marlina belum memproses transaksi sebagai PIC tetapi tidak menyebut cara memastikannya; spec memakai kemampuan baca BE yang disediakan tim FE/BE dan mengandaikan tidak ada seed log transaksi.
