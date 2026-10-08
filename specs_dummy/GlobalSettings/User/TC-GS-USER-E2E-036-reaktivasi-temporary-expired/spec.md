---
id: TC-GS-USER-E2E-036-reaktivasi-temporary-expired
title: Reaktivasi Temporary User yang sudah expired dan Bulk Activate yang melewatinya
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-89
  - TC-GS-USER-333
  - TC-GS-USER-335
  - TC-GS-USER-90
  - TC-GS-USER-354
  - TC-GS-USER-332
  - TC-GS-USER-334
  - TC-GS-USER-337
coverage:
  web: automated
---

# Reaktivasi Temporary User yang sudah expired dan Bulk Activate yang melewatinya

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User Temporary yang sudah expired (Temporary Until sudah lewat) dan berstatus Inactive, hasil seeding:
  - "Dewi Kedaluwarsa" untuk uji dialog, validasi tanggal, dan bulk. Tidak dikonsumsi oleh langkah reaktivasi
  - "Eko Kedaluwarsa" untuk uji Extend period
  - "Fitri Kedaluwarsa" untuk uji Make permanent
  - "Gani Kedaluwarsa" dan "Hana Kedaluwarsa" untuk uji Bulk Activate saat semua baris expired
- User "Irfan Nonaktif" berstatus Inactive biasa (bukan Temporary)
- Spec ini mengaktifkan "Eko Kedaluwarsa" dan "Fitri Kedaluwarsa", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Dialog reaktivasi

1. Klik toggle Active ON pada baris "Dewi Kedaluwarsa" di User List
2. Verifikasi dialog "Reactivate Temporary User" muncul dengan teks "This user's active period has ended. Choose how to reactivate:", opsi "Extend period" dengan date picker, opsi "Make permanent", serta tombol `[Cancel]` dan `[Reactivate]`
3. Verifikasi `[Reactivate]` disabled selama belum ada opsi yang dipilih
4. Klik `[Cancel]`
5. Verifikasi dialog tertutup dan "Dewi Kedaluwarsa" tetap Inactive

### Validasi tanggal Extend period

6. Klik toggle Active ON pada "Dewi Kedaluwarsa" lagi lalu pilih opsi "Extend period"
7. Isi tanggal kemarin lalu klik `[Reactivate]`
8. Verifikasi inline error "Please select a future date." muncul, dialog tetap terbuka, dan "Dewi Kedaluwarsa" tetap Inactive, lalu ulangi dengan tanggal hari ini dan verifikasi hasil yang sama
9. Klik `[Cancel]`

### Tiga titik masuk

10. Buka User Detail "Dewi Kedaluwarsa" dan klik toggle Active ON pada Header
11. Verifikasi dialog "Reactivate Temporary User" yang identik muncul, lalu klik `[Cancel]`
12. Buka Modal Edit "Dewi Kedaluwarsa" dan set toggle Active ON dari dalam form
13. Verifikasi dialog "Reactivate Temporary User" yang identik muncul, lalu klik `[Cancel]` dan tutup Modal Edit
14. Verifikasi tidak ada dari ketiga titik masuk yang langsung mengaktifkan user tanpa dialog

### Bulk Activate

15. Pilih baris "Irfan Nonaktif" dan "Dewi Kedaluwarsa", lalu klik bulk action `Activate`
16. Verifikasi dialog "Activate Users" muncul tanpa dialog Extend/Make Permanent, lalu konfirmasi
17. Verifikasi "Irfan Nonaktif" menjadi Active, sedangkan "Dewi Kedaluwarsa" dilewati dan tetap Inactive
18. Verifikasi toast "Success, user has been activated. Some users were skipped (temporary period expired)." muncul
19. Pilih baris "Gani Kedaluwarsa" dan "Hana Kedaluwarsa" (semuanya expired), lalu klik bulk action `Activate` dan konfirmasi
20. Verifikasi tidak ada user yang teraktivasi, tidak ada dialog Extend/Make Permanent, dan keduanya tetap Inactive
21. Verifikasi toast "Success, user has been activated. Some users were skipped (temporary period expired)." muncul (seluruhnya dilewati, bukan error)

### Reaktivasi yang mengubah data

22. Klik toggle Active ON pada "Eko Kedaluwarsa", pilih "Extend period", isi tanggal 14 hari dari hari ini, lalu klik `[Reactivate]`
23. Verifikasi "Eko Kedaluwarsa" menjadi Active, badge "Temporary" tetap tampil, dan Temporary Until menampilkan tanggal baru
24. Klik toggle Active ON pada "Fitri Kedaluwarsa", pilih "Make permanent", lalu klik `[Reactivate]`
25. Verifikasi "Fitri Kedaluwarsa" menjadi Active, badge "Temporary" hilang, dan Temporary Until kosong
26. Klik toggle Active OFF pada "Fitri Kedaluwarsa"
27. Verifikasi dialog konfirmasi "Deactivate User" biasa muncul (bukan dialog Extend/Make Permanent), lalu klik `[Cancel]`
28. Buka Changelog "Fitri Kedaluwarsa"
29. Verifikasi ada baris Action "Remove Temporary User", Field "Temporary Until", Old tanggal lama, New "—", dan Modified By admin yang login (bukan "System")

## Notes

- Spec ini dipisah dari alur Temporary User biasa karena butuh user yang sudah expired (prinsip 12 di `docs/e2e-conventions.md` bagian 3). Kebutuhan seeding-nya ditulis di Prerequisites untuk tim FE.
- Aksi yang mengubah data (langkah 22 sampai 29) ditaruh paling akhir.
- Dialog reaktivasi mengikuti PRD `user.md` bagian 4.2: judul "Reactivate Temporary User", tombol `[Cancel]` dan `[Reactivate]`. Sumber TC menyebut tombol ini "Confirm".
- Expected `TC-GS-USER-354` menyebut toast "atau setara" untuk kasus semua baris dilewati. Langkah 21 memakai toast partial dari PRD `user.md` bagian 7. Bila implementasi memakai copy lain, ini akan terlihat saat run.
- Nonaktif otomatis saat expiry dicakup `TC-GS-USER-E2E-035-temporary-auto-deactivate`.
