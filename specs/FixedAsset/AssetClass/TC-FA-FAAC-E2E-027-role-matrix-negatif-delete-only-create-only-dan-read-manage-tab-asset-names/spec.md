---
id: TC-FA-FAAC-E2E-027-role-matrix-negatif-delete-only-create-only-dan-read-manage-tab-asset-names
title: "Role Matrix Negatif: Deactivate Instead dan Tab Asset Names Tanpa Kontrol Tulis untuk Delete-Only, Create-Only, dan Read-Only (Manage Accounting, Huruf Read Saja)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-227
  - TC-FA-FAAC-615
  - TC-FA-FAAC-614
  - TC-FA-FAAC-616
coverage:
  web: automated
---

# Role Matrix Negatif: Deactivate Instead dan Tab Asset Names Tanpa Kontrol Tulis untuk Delete-Only, Create-Only, dan Read-Only (Manage Accounting, Huruf Read Saja)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Delete-Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Delete-Only | `deleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_DO_PASSWORD` | TC-FA-FAAC-227, TC-FA-FAAC-615 |
| Create-Only | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_CO_PASSWORD` | TC-FA-FAAC-614 |
| Read-Only (Manage accounting, huruf Read saja) | `readOnlyManageAccountingHurufReadSaja_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_MA_PASSWORD` | TC-FA-FAAC-616 |

- Env var: `FA_AC_DO_PASSWORD`, `FA_AC_CO_PASSWORD`, `FA_AC_RO_MA_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Asset Class B-USED dengan Last Posted Period Mar 2026 (seed Pre-setup; kondisi Last Posted Period disediakan lewat fixture BE, NC-16); HEAVY-EQ memiliki tiga Asset Name ter-assign Excavator PC200, Wheel Loader, dan Crane Rental Unit (seed Pre-setup). Dibaca, tidak diubah. Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: ganti akun (logout lalu login), membuka dialog Delete dan membaca tooltip tombol Disabled.

## Test Steps

### TC-FA-FAAC-227

1. Ketik Search `B-USED`, tekan Enter
2. Klik ikon ⋯ pada baris B-USED lalu pilih "Delete"
3. Arahkan kursor ke tombol "Deactivate instead"
4. Verifikasi tombol "Deactivate instead" Disabled
5. Verifikasi tooltip "You don't have permission to edit." tampil
6. Verifikasi tombol [Delete] pada dialog tetap dapat diakses (Enabled)
7. Klik [Cancel] pada dialog

### TC-FA-FAAC-615

8. Ganti isi kotak search dengan `HEAVY-EQ`, tekan Enter
9. Klik Class Code HEAVY-EQ untuk membuka Detail Asset Class Heavy Equipment
10. Klik tab Asset Names
11. Verifikasi tabel Asset Names tampil dengan baris Crane Rental Unit
12. Verifikasi tombol '+ Assign Asset Names', kolom checkbox, dan Bulk Action Bar: Hidden
13. Verifikasi row action 'Move' dan 'Unassign' Hidden

### TC-FA-FAAC-614

14. Ganti akun: logout, lalu login sebagai Create-Only
15. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
16. Ketik Search `HEAVY-EQ`, tekan Enter
17. Klik Class Code HEAVY-EQ untuk membuka Detail Asset Class Heavy Equipment
18. Klik tab Asset Names
19. Verifikasi tabel Asset Names tampil dengan baris Crane Rental Unit
20. Verifikasi tombol '+ Assign Asset Names', kolom checkbox, dan Bulk Action Bar: Hidden
21. Verifikasi row action 'Move' dan 'Unassign' Hidden

### TC-FA-FAAC-616

22. Ganti akun: logout, lalu login sebagai Read-Only (Manage accounting, huruf Read saja)
23. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
24. Ketik Search `HEAVY-EQ`, tekan Enter
25. Klik Class Code HEAVY-EQ untuk membuka Detail Asset Class Heavy Equipment
26. Klik tab Asset Names
27. Verifikasi tabel Asset Names tampil dengan baris Crane Rental Unit
28. Verifikasi tombol '+ Assign Asset Names', kolom checkbox, Bulk Action Bar, serta row action 'Move' dan 'Unassign': Hidden

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Spec Role Matrix negatif (bagian 3a): aksi atau kontrol yang tidak tersedia bagi role tanpa hak terkait; polaritas seragam negatif.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (menutup dialog Delete tanpa menghapus B-USED), langkah 14 dan 22 (ganti akun), langkah 15 dan 23 (membuka tab Asset Class sesudah login ulang, S-07), langkah 8, 16, dan 24 (Search `HEAVY-EQ` untuk menemukan baris target karena tidak dijamin berada di halaman 1; R-16). Langkah 1 (Search `B-USED`) berasal dari TC-FA-FAAC-227.
- Baris B-USED hanya dibaca: dialog Delete dibuka lalu dibatalkan, tidak ada data berubah (pengecualian S-06 untuk aksi yang dibatalkan).
- Asersi Hidden pada tab Asset Names didahului `Verifikasi` tabel Asset Names tampil dengan baris Crane Rental Unit sebagai anchor positif permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-227 menyebut Expected "Delete tetap dapat diakses" tanpa menyebut elemen yang dicek; spec mengasersi tombol [Delete] pada dialog Enabled.
  - TC-FA-FAAC-614 sampai 616 langkah 3 menyebut menu baris pada Crane Rental Unit, tetapi Expected hanya menyebut row action Hidden; spec mengasersi row action Hidden tanpa membuka menu.
