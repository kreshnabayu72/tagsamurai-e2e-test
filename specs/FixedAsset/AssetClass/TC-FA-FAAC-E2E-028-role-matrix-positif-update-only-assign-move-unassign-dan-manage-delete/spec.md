---
id: TC-FA-FAAC-E2E-028-role-matrix-positif-update-only-assign-move-unassign-dan-manage-delete
title: "Role Matrix Positif: Update-Only Melihat Kontrol Assign, Move, Unassign dan Menjalankan Assign, serta Manage Accounting (Read, Delete) Menjalankan Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-613
  - TC-FA-FAAC-617
  - TC-FA-FAAC-86
coverage:
  web: automated
---

# Role Matrix Positif: Update-Only Melihat Kontrol Assign, Move, Unassign dan Menjalankan Assign, serta Manage Accounting (Read, Delete) Menjalankan Delete

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Update-Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_UO_PASSWORD` | TC-FA-FAAC-613, TC-FA-FAAC-617 |
| Manage accounting (Read, Delete) | `manageAccountingReadDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RD_PASSWORD` | TC-FA-FAAC-86 |

- Env var: `FA_AC_UO_PASSWORD`, `FA_AC_MA_RD_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: HEAVY-EQ memiliki tiga Asset Name ter-assign Excavator PC200 (8 aset aktif), Wheel Loader (4 aset aktif), dan Crane Rental Unit (0 aset aktif); Asset Class B-ANCHOR (Anchor Heavy Equipment, Active, tanpa Asset Name); Asset Name tanpa Asset Class 'Hand Truck' (0 aset aktif); Asset Class TEMP-EQ – Temporary Equipment tanpa Asset Name dan tanpa Last Posted Period (seed Pre-setup, NC-16). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data yang diubah spec: 'Hand Truck' ter-assign ke B-ANCHOR dan TEMP-EQ terhapus. Target aksi tulis memakai baris seed literal sesuai TC (nama seed dipakai apa adanya, pengecualian beralasan atas S-06 dan S-12 untuk modul ini); fixture BE (disediakan tim FE/BE) menyiapkan baris itu di hook `before` dan memulihkannya ke keadaan awal di hook `after`, termasuk bila spec gagal di tengah.
- State global: bulan berjalan menurut zona waktu General Settings (NC-11) dan kondisi periode akuntansi, Last Posted Period, dan Last Exported Period disediakan lewat fixture BE (NC-16); seluruhnya dipulihkan di hook `after`.
- Data Dinamis: tidak ada data bersuffix `{runId}`; target aksi tulis adalah baris seed literal di atas (pengecualian beralasan, lihat butir sebelumnya).
- Kemampuan teknis: ganti akun (logout lalu login), centang baris tabel, fixture BE untuk seed dan pemulihan.

## Test Steps

### TC-FA-FAAC-613

1. Ketik Search `HEAVY-EQ`, tekan Enter
2. Klik Class Code HEAVY-EQ untuk membuka Detail Asset Class Heavy Equipment
3. Klik tab Asset Names
4. Centang baris Excavator PC200
5. Verifikasi tombol '+ Assign Asset Names' tampil dan Enabled
6. Verifikasi kolom checkbox dan Bulk Action Bar tampil
7. Klik tombol ⋯ pada baris Crane Rental Unit
8. Verifikasi menu baris memuat 'Move' dan 'Unassign'
9. Verifikasi 'Unassign' Enabled untuk 'Crane Rental Unit'
10. Tutup menu baris, hapus centang baris Excavator PC200, lalu kembali ke tabel Asset Class lewat Breadcrumb Asset Class (form tidak diubah)

### TC-FA-FAAC-617

11. Ganti isi kotak search dengan `B-ANCHOR`, tekan Enter
12. Klik Class Code B-ANCHOR untuk membuka Detail Asset Class anchor
13. Klik tab 'Asset Names'
14. Klik tombol '+ Assign Asset Names'
15. Centang 'Hand Truck'
16. Klik [Assign]
17. Verifikasi dialog menutup
18. Verifikasi toast sukses: "Success, asset name has been assigned."
19. Verifikasi 'Hand Truck' tampil di tab Asset Names

### TC-FA-FAAC-86

20. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Delete)
21. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
22. Ketik Search `TEMP-EQ`, tekan Enter
23. Klik tombol ⋯ pada baris TEMP-EQ lalu klik Delete
24. Verifikasi dialog Konfirmasi tampil dengan title "Delete Asset Class", bullet "TEMP-EQ – Temporary Equipment", teks "This action cannot be undone. Are you sure you want to delete it?", tombol [Cancel] dan [Delete]
25. Klik [Delete] pada dialog
26. Verifikasi toast "Success, asset class has been deleted." tampil
27. Verifikasi baris TEMP-EQ hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Spec Role Matrix positif (bagian 3a): aksi berhasil bagi role yang berhak; urutan mengikuti prinsip bagian 3 (asersi kontrol dulu, Assign berhasil, Delete di akhir).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 (menutup menu, menghapus centang, dan kembali ke tabel tanpa mengubah form, S-09), langkah 20 (ganti akun), langkah 21 (membuka tab Asset Class sesudah login ulang, S-07), langkah 1 dan 11 (Search untuk menemukan baris target karena tidak dijamin berada di halaman 1; R-16). Langkah 22 (Search `TEMP-EQ`) berasal dari TC-FA-FAAC-86.
- Dependensi TC-FA-FAAC-87 pada TC-FA-FAAC-617 (Asset Class anchor Active tanpa Asset Name) dijalankan lewat seeding API di hook `before` (S-04): B-ANCHOR di-seed lewat fixture BE, tidak dibuat lewat UI.
- Asersi baris TEMP-EQ hilang memakai toast sukses Delete yang sudah diasersi sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-613 langkah 2 dan 3 menyebut toolbar dan menu baris, sedangkan Bulk Action Bar baru tampil setelah seleksi; spec menambah langkah centang baris Excavator PC200 yang tidak ada di langkah TC.
  - TC-FA-FAAC-86 menyebut TEMP-EQ tanpa Last Posted Period dan Post Condition "terhapus" tanpa langkah observasi tambahan; Post Condition tidak diasersi.
  - TC-FA-FAAC-617 menyebut Asset Name 'Hand Truck' tanpa Asset Class sebagai seed Pre-setup; pemulihan ke keadaan tanpa Asset Class dijamin fixture BE di hook `after`.
