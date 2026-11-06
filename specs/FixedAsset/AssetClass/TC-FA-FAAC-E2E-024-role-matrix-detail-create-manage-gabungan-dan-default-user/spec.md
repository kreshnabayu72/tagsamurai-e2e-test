---
id: TC-FA-FAAC-E2E-024-role-matrix-detail-create-manage-gabungan-dan-default-user
title: "Role Matrix: Visibilitas Detail Mode Create, Akses Default User, dan Gabungan Elemen Manage Accounting (Read, Create, Update)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-68
  - TC-FA-FAAC-71
  - TC-FA-FAAC-672
coverage:
  web: automated
---

# Role Matrix: Visibilitas Detail Mode Create, Akses Default User, dan Gabungan Elemen Manage Accounting (Read, Create, Update)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Manage accounting (Read, Create)) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun lain memakai langkah ganti akun eksplisit di Test Steps. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Manage accounting (Read, Create) | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RC_PASSWORD` | TC-FA-FAAC-68 |
| Default User | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_DU_PASSWORD` | TC-FA-FAAC-71 |
| Manage accounting (Read, Create, Update) | `manageAccountingReadCreateUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RCU_PASSWORD` | TC-FA-FAAC-672 |

- Env var: `FA_AC_MA_RC_PASSWORD`, `FA_AC_DU_PASSWORD`, `FA_AC_MA_RCU_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: sembilan Asset Class contoh (Tabel Data Uji Pre-setup; nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC. HEAVY-EQ memiliki Asset Name Wheel Loader (4 aset aktif; seed Pre-setup). Dibaca, tidak diubah.
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Uji TC-FA-FAAC-672: huruf CRUD aktor Read, Create, Update.
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: ganti akun (logout lalu login), centang baris tabel, membuka dropdown Select akun.

## Test Steps

### TC-FA-FAAC-68

1. Klik [+ Asset Class]
2. Verifikasi Button [Submit] dan [Clear Field] (Create): Show
3. Verifikasi Button [Save] tidak ada pada mode Create
4. Klik tab Accounts, lalu klik Select akun Asset Cost
5. Verifikasi Select akun menampilkan shortcut "+ Create account": Show
6. Tutup dropdown Select akun (Esc), lalu kembali ke tabel Asset Class lewat Breadcrumb Asset Class (form tidak diubah)

### TC-FA-FAAC-71

7. Ganti akun: logout, lalu login sebagai Default User
8. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
9. Verifikasi Button [+ Asset Class]: Show
10. Ketik Search `VEHICLES`, tekan Enter
11. Centang baris VEHICLES
12. Verifikasi kolom Checkbox dan Bulk Action Bar: Show
13. Klik tombol ⋯ pada baris VEHICLES
14. Verifikasi menu ⋯ memuat Edit, Duplicate, dan Delete
15. Tutup menu ⋯ dan hapus centang baris VEHICLES
16. Verifikasi toggle kolom Active: Show dan Enabled

### TC-FA-FAAC-672

17. Ganti akun: logout, lalu login sebagai Manage accounting (Read, Create, Update)
18. Buka Fixed Asset > Settings > Accounting, lalu klik tab Asset Class
19. Verifikasi toolbar tabel Asset Class menampilkan Button [+ Asset Class]
20. Ketik Search `HEAVY-EQ`, tekan Enter
21. Klik ikon ⋯ pada baris HEAVY-EQ
22. Verifikasi menu ⋯ baris memuat Edit dan Duplicate
23. Verifikasi item Delete pada menu ⋯ baris tidak ada (Hidden)
24. Tutup menu ⋯ lalu centang baris HEAVY-EQ
25. Verifikasi kolom Checkbox dan Bulk Action Bar tampil dengan aksi Bulk Deactivate (seleksi Active)
26. Hapus centang baris HEAVY-EQ, lalu klik link Class Code HEAVY-EQ
27. Verifikasi Detail mode Edit: field Enabled, Button [Save] dan [Clear Field] tampil
28. Klik tab Asset Names
29. Verifikasi tab Asset Names: Button [+ Assign Asset Names] tampil
30. Klik ikon ⋯ pada baris Wheel Loader
31. Verifikasi menu ⋯ Wheel Loader memuat Move dan Unassign
32. Verifikasi item Unassign pada menu ⋯ Wheel Loader Disabled karena Wheel Loader memiliki aset aktif
33. Tutup menu ⋯ lalu kembali ke tabel Asset Class lewat Breadcrumb Asset Class (form tidak diubah)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi). Tiap role punya blok sendiri karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (menutup dropdown dan kembali ke tabel tanpa mengubah form), langkah 15, 24, 26, dan 33 (menutup menu, mengatur centang, membuka Detail HEAVY-EQ, dan kembali ke tabel, S-09), langkah 7 dan 17 (ganti akun), langkah 8 dan 18 (membuka tab Asset Class sesudah login ulang, S-07).
- Langkah 20: Search `HEAVY-EQ` untuk menemukan baris target karena baris itu tidak dijamin berada di halaman 1 (R-16); langkah 10 (Search `VEHICLES`) berasal dari TC-FA-FAAC-71.
- Langkah TC-FA-FAAC-71 "Perhatikan ... kolom Active" diasersi pada Expected d; Search dan "Klik tombol ⋯ pada baris VEHICLES" memakai baris VEHICLES sesuai TC; centang baris memakai VEHICLES juga, yaitu baris hasil Search (TC tidak menyebut baris centang).
- Asersi Delete Hidden pada menu ⋯ (TC-FA-FAAC-672) didahului asersi Edit dan Duplicate tampil pada menu yang sama sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-68 tidak menyebut cara kembali ke tabel; spec memakai Breadcrumb Asset Class pada form yang tidak diubah sehingga tidak ada dialog Unsaved Changes (bagian S-08 tidak berlaku).
  - TC-FA-FAAC-71 dan TC-FA-FAAC-672 mengasersi Bulk Action Bar yang baru muncul setelah seleksi; spec menambah langkah centang baris VEHICLES yang tidak ada di langkah TC-FA-FAAC-71.
  - TC-FA-FAAC-672 menyebut data "Huruf CRUD aktor: Read, Create, Update"; spec memakai akun Manage accounting (Read, Create, Update) dari Pre-setup.
