---
id: TC-FA-RP-E2E-224-modal-changelog-sort-dan-setup-column-1
title: "Modal Changelog: Sort dan Setup Column (1/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-731
  - TC-FA-RP-732
  - TC-FA-RP-733
  - TC-FA-RP-734
coverage:
  web: automated
---

# Modal Changelog: Sort dan Setup Column (1/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Seeding enam entri seed #42 dijamin fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen yang tidak dipulihkan: entri lain dapat ada di antara entri seed, sehingga entri seed dikenali lewat kombinasi Action, User Name, Old Value, New Value, dan Modified By di atas, dan asersi memakai urutan relatif, selisih terhadap baseline, atau hanya entri seed yang cocok. Spec ini tidak mengubah data.
- Tabel Sort kelas teks (TC 733; kolom Urutan ascending memuat urutan relatif entri seed #42, entri lain dari audit trail permanen dapat berada di antaranya); kolom Modified By ditampilkan `[First Name] [Last Initial]`:

| Kolom | Urutan ascending |
|---|---|
| Action | Assign (Rina Wulandari, Ahmad Fauzi, Budi Santoso, Maya Anggraeni), Auto-Revert (Fitri Handayani), Remove (Budi Santoso) |
| User Name | Ahmad Fauzi, Budi Santoso (dua entri), Fitri Handayani, Maya Anggraeni, Rina Wulandari |
| Old Value | urutan A-Z nilai lama (urutan relatif entri seed) |
| New Value | urutan A-Z nilai baru (urutan relatif entri seed) |
| Modified By | `Prasetyo H`, `Rina W`, `Siti R` (urut menurut nama lengkap Prasetyo Hadi, Rina Wulandari, Siti Rahmawati) |

## Test Steps

### Sort default (TC 731)

1. Klik ikon Changelog pada toolbar.
2. Verifikasi entri terurut Date descending (terbaru lebih dulu) dengan urutan relatif entri seed Pre-setup #42 (entri lain dari audit trail permanen dapat berada di antaranya): Assign Maya Anggraeni, Auto-Revert Fitri Handayani, Remove Budi Santoso, Assign Budi Santoso, Assign Ahmad Fauzi, Assign Rina Wulandari.

### Sort siklus tiga state kelas tanggal (TC 732)

3. Klik header kolom Date sekali.
4. Verifikasi kolom Date ascending (Oldest First) dengan urutan relatif entri seed Pre-setup #42 (entri lain dapat berada di antaranya): Assign Rina Wulandari, Assign Ahmad Fauzi, Assign Budi Santoso, Remove Budi Santoso, Auto-Revert Fitri Handayani, Assign Maya Anggraeni.
5. Klik header kolom Date kedua kali.
6. Verifikasi kolom Date descending (Newest First), kebalikan urutan relatif langkah 4.
7. Klik header kolom Date ketiga kali.
8. Verifikasi urutan kembali ke default sort tabel (Date descending, urutan relatif langkah 2).

### Sort siklus tiga state kelas teks (TC 733)

9. Untuk setiap baris pada tabel Sort kelas teks, lakukan langkah 10 sampai 15.
10. Klik header kolom sekali.
11. Verifikasi kolom ascending dengan urutan relatif entri seed sesuai kolom Urutan ascending pada tabel.
12. Klik header kolom kedua kali.
13. Verifikasi kolom descending, kebalikan urutan relatif langkah 11.
14. Klik header kolom ketiga kali.
15. Verifikasi urutan kembali ke default sort tabel.

### Screening overlay Column Visibility (TC 734)

16. Klik header `(⋯)` kolom Column Visibility.
17. Verifikasi overlay memuat item `Setup Column...` di bagian bawah.
18. Verifikasi kolom bawaan tampil tercentang aktif: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
19. Verifikasi drag handle tersedia pada daftar.

## Notes

- Alasan di atas 35 langkah: langkah 10 sampai 15 adalah blok berulang dengan parameter pada tabel Prerequisites (lima iterasi); seluruh blok berkelas fungsional sama, dataset sama, dan tiap iterasi berdiri sendiri karena klik ketiga mengembalikan sort ke default. Langkah yang diulang: 10 sampai 15. Tanpa ekspansi, spec berisi 19 langkah.
- Langkah penghubung (S-03): langkah 9 (kepala perulangan).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 733 butir e menyebut urutan Modified By "berdasarkan nama lengkap" (Prasetyo Hadi, Rina Wulandari, Siti Rahmawati), sedangkan sel menampilkan `[First Name] [Last Initial]`; spec menulis nilai sel dan menyebut nama lengkap sebagai dasar urutan.
  - TC 733 butir c dan d tidak menyebut nilai Old Value dan New Value yang diurutkan ("urutan A-Z"); spec mengasersi urutan A-Z nilai yang tampil.
  - TC 732 dan TC 733 hanya mendefinisikan urutan ascending; urutan descending diasersi sebagai kebalikannya.
