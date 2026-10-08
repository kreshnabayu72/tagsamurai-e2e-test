---
id: TC-GS-USER-E2E-085-bulk-dialog-satu-user-dan-daftar-panjang
title: 'Dialog bulk Activate dan Deactivate: satu user, daftar panjang, dan aksi yang disembunyikan'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-458
  - TC-GS-USER-459
  - TC-GS-USER-448
  - TC-GS-USER-398
coverage:
  web: automated
---

# Dialog bulk Activate dan Deactivate: satu user, daftar panjang, dan aksi yang disembunyikan

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Satu user Active "Budi Santoso" dan satu user Inactive "Irfan Nonaktif"
- Dua belas atau lebih user Active dan Inactive tambahan untuk seleksi banyak baris
- Spec ini hanya membuka dialog lalu membatalkan, jadi tidak mengubah data

## Test Steps

### Satu user terpilih

1. Pilih hanya baris "Budi Santoso" (Active) lalu klik bulk action `Deactivate`
2. Verifikasi dialog berjudul singular "Deactivate User" (bukan "Deactivate Users") dengan satu bullet "• Budi Santoso" dan teks "This will deactivate user across all products. Are you sure you want to deactivate it?", lalu klik `[Cancel]`
3. Pilih hanya baris "Irfan Nonaktif" (Inactive) lalu klik bulk action `Activate`
4. Verifikasi dialog berjudul singular "Activate User" dengan satu bullet dan teks "This will activate user across all products. Are you sure you want to activate it?", lalu klik `[Cancel]`

### Daftar panjang

5. Pilih 12 baris user Active lalu klik bulk action `Deactivate`
6. Verifikasi dialog menampilkan bullet nama untuk semua 12 baris (tidak diganti ringkasan "12 users are selected.") dan bodinya bisa di-scroll sehingga tiap nama tetap terbaca, lalu klik `[Cancel]`

### Aksi disembunyikan bila tidak berlaku

7. Pilih hanya baris yang semuanya Active
8. Verifikasi bulk action `Activate` tidak tampil (bukan disabled) dan `Deactivate` tetap tampil
9. Ganti seleksi ke baris yang semuanya Inactive
10. Verifikasi bulk action `Deactivate` tidak tampil dan `Activate` tetap tampil

## Notes

- Sumber `user.md` bagian 4.2, 4.4, dan `prd-conventions.md` bagian 7. Daftar bullet penuh untuk lebih dari 10 baris adalah deviasi dari kanon default dan sudah dicatat di TC sumber (`TC-GS-USER-448`).
- Bulk Activate/Deactivate yang mengubah data dicakup `TC-GS-USER-E2E-010` sampai `020` (role matrix) dan spec bulk lainnya.
