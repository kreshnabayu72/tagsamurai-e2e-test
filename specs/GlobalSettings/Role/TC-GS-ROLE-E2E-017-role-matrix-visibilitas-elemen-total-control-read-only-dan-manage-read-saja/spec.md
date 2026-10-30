---
id: TC-GS-ROLE-E2E-017-role-matrix-visibilitas-elemen-total-control-read-only-dan-manage-read-saja
title: "Role Matrix: Visibilitas Elemen Role & Permission untuk Total Control, Read Only, dan Manage user and role Read Saja"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-36
  - TC-GS-ROLE-37
  - TC-GS-ROLE-38
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Role & Permission untuk Total Control, Read Only, dan Manage user and role Read Saja

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel di bawah.
- Langkah TC-GS-ROLE-37 dan TC-GS-ROLE-38 identik (hanya akun yang berbeda) sehingga dijalankan sebagai perulangan "untuk setiap role"; TC-GS-ROLE-36 berbeda (aksi tulis tersedia) dan ditulis sebagai blok sendiri.

Role yang diuji (Tabel Data Uji Pre-setup #1, #4, #6):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-GS-ROLE-36 | Total Control | Penuh | Ahmad Fauzi | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-ROLE-37 | Read Only | Hanya baca | Siti Nurhaliza | disediakan tim FE | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-ROLE-38 | Manage user and role Read saja | Hanya baca | Fajar Nugroho | `manageUserAndRoleRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_READ_PASSWORD` (env baru) |

Kontrol tabel (parameter perulangan langkah "Untuk setiap baris tabel Kontrol tabel"):

| No | Kontrol |
|---|---|
| 1 | Search |
| 2 | Filter |
| 3 | Sort |
| 4 | Pagination |
| 5 | header Column Visibility |

- Login Total Control (role pertama) dilakukan di hook `before`; role berikutnya memakai langkah ganti akun eksplisit (logout lalu login). Karena spec berakhir di akun Manage user and role Read saja, hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; env baru `GS_ROLE_MANAGE_READ_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup yang dibaca: Dewi Lestari (Total Control, Inactive; Pre-setup #3), Siti Nurhaliza dan Rina Putri (Read Only; Pre-setup #4), Doni Pratama dengan baris role Manage TAG (Pre-setup #10), serta ≥ 11 user di Tab Total Control dan Tab Read Only (Pre-setup #17) agar Pagination tersedia. Spec tidak membuat, mengubah, atau menghapus data; menu row action dibuka lalu ditutup tanpa menjalankan Remove.
- Layar awal spec: Global Settings > Role & Permission (Tab Total Control) dibuka di hook `beforeEach`.
- Kemampuan teknis: hover pada checkbox disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-ROLE-36: Visibilitas elemen untuk aktor Total Control

1. Verifikasi Tombol `[+ Assign]` tampil pada Tab Total Control
2. Verifikasi Download tampil pada Tab Total Control
3. Verifikasi Changelog tampil pada Tab Total Control
4. Klik `⋯` pada baris Dewi Lestari
5. Verifikasi row action `Remove` tampil dan enabled
6. Tutup row action menu dengan Esc
7. Untuk setiap baris tabel Kontrol tabel (langkah 8):
8. Verifikasi kontrol tabel (baris tabel) aktif pada Tab Total Control
9. Klik Tab Read Only
10. Verifikasi Tombol `[+ Assign]` tampil pada Tab Read Only
11. Klik `⋯` pada baris Siti Nurhaliza
12. Verifikasi row action `Remove` tampil dan enabled
13. Tutup row action menu dengan Esc
14. Untuk setiap baris tabel Kontrol tabel (langkah 15):
15. Verifikasi kontrol tabel (baris tabel) aktif pada Tab Read Only
16. Klik Tab System
17. Klik Role Name "Manage TAG" untuk membuka Detail
18. Verifikasi Tombol `[+ Assign]` tampil pada Detail
19. Verifikasi kolom checkbox seleksi tampil pada Detail
20. Verifikasi checkbox Update baris Doni Pratama tampil dan enabled
21. Klik `⋯` pada baris Doni Pratama
22. Verifikasi row action `Remove` tampil dan enabled
23. Tutup row action menu dengan Esc
24. Untuk setiap baris tabel Kontrol tabel (langkah 25):
25. Verifikasi kontrol tabel (baris tabel) aktif pada Detail

### TC-GS-ROLE-37 dan TC-GS-ROLE-38: Visibilitas elemen untuk aktor Read Only dan aktor Manage user and role Read saja

26. Untuk setiap role pada tabel Role yang diuji dengan Kelompok "Hanya baca" (langkah 27 sampai 53):
27. Logout, lalu login sebagai role tersebut
28. Buka Global Settings > Role & Permission (Tab Total Control)
29. Verifikasi Download tampil pada Tab Total Control
30. Verifikasi Changelog tampil pada Tab Total Control
31. Verifikasi Tombol `[+ Assign]` Hidden pada Tab Total Control
32. Verifikasi row action `Remove` Hidden pada baris Dewi Lestari
33. Untuk setiap baris tabel Kontrol tabel (langkah 34):
34. Verifikasi kontrol tabel (baris tabel) aktif pada Tab Total Control
35. Klik Tab Read Only
36. Verifikasi Download tampil pada Tab Read Only
37. Verifikasi Changelog tampil pada Tab Read Only
38. Verifikasi Tombol `[+ Assign]` Hidden pada Tab Read Only
39. Verifikasi row action `Remove` Hidden pada baris Rina Putri
40. Klik Tab System
41. Verifikasi Role Name "Manage TAG" tampil dan dapat diklik
42. Klik `⋯` pada baris "Manage TAG"
43. Verifikasi row action `Detail` tampil
44. Tutup row action menu dengan Esc
45. Klik Role Name "Manage TAG" untuk membuka Detail
46. Verifikasi Tombol `[+ Assign]` Hidden pada Detail
47. Verifikasi kolom checkbox seleksi Hidden pada Detail
48. Verifikasi row action `Remove` Hidden pada baris Doni Pratama
49. Verifikasi checkbox Create, Update, dan Delete baris Doni Pratama tampil namun disabled
50. Hover checkbox Update baris Doni Pratama
51. Verifikasi tooltip "Read Only access cannot modify data."
52. Untuk setiap baris tabel Kontrol tabel (langkah 53):
53. Verifikasi kontrol tabel (baris tabel) aktif pada Detail

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Pada blok TC-GS-ROLE-37 dan TC-GS-ROLE-38, iterasi pertama (Read Only) memetakan ke TC-GS-ROLE-37 dan iterasi kedua (Manage user and role Read saja) ke TC-GS-ROLE-38, sesuai kolom TC pada tabel Role yang diuji.
- Spec Role Matrix (bagian 3a konvensi) berupa matriks visibilitas elemen per role yang memuat polaritas tampil dan Hidden/disabled; `caseType` Negative mengikuti alur dominan (dua dari tiga TC menguji elemen tidak tersedia, bagian 8).
- Spec melewati sekitar 35 langkah: 53 langkah nominal, sekitar 108 langkah dengan ekspansi perulangan (langkah 7 sampai 8, 14 sampai 15, 24 sampai 25 masing-masing lima iterasi; blok langkah 27 sampai 53 dua iterasi dengan langkah 33 sampai 34 dan 52 sampai 53 lima iterasi di dalamnya). Semua langkah berada di satu kelas harness (Role Matrix, hanya baca dan tanpa data tulis); tiap blok role berdiri sendiri (login ulang di awal blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan perulangan kontrol tabel dipakai supaya tiap kontrol punya `Verifikasi` sendiri (S-01).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup row action menu dengan Esc (langkah 6, 13, 23, 44), klik Tab Read Only dan Tab System (langkah 9, 16, 35, 40), membuka Detail lewat Role Name (langkah 17, 45), serta logout lalu login ke role berikutnya (langkah 27).
- Asersi Hidden pada langkah 31, 32, 38, 39, 46, 47, dan 48 memakai Download dan Changelog yang sudah tampil (langkah 29, 30, 36, 37) atau halaman Detail yang sudah termuat sebagai anchor permukaan (bagian 8b butir 2).
- Pada Tab Total Control dan Tab Read Only untuk role hanya baca, `Remove` diasersi Hidden pada baris tanpa membuka menu `⋯` (TC menyebut "overlay (⋯) baris tidak memuat Remove"); menu `⋯` baris tanpa aksi tidak tersedia.
- Asersi kontrol tabel aktif untuk TC-GS-ROLE-37 dan TC-GS-ROLE-38 (Expected e) dijalankan pada Tab Total Control dan Detail; TC-GS-ROLE-36 Expected d menyebut ketiga surface.
- Pada TC-GS-ROLE-37 dan TC-GS-ROLE-38 langkah 41 sampai 44 menjalankan Expected b ("Detail tetap tersedia via Role Name dan row action").
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-GS-ROLE-37 dan TC-GS-ROLE-38 Expected d menyebut checkbox Create/Update/Delete pada Detail "Manage TAG", sedangkan Detail Manage TAG hanya memiliki toggle Read dan Update (TC-GS-ROLE-32 dan TC-GS-ROLE-311); asersi langkah 49 mengikuti TC dan akan gagal pada Create dan Delete bila kolomnya memang tidak ada.
  - TC-GS-ROLE-37 dan TC-GS-ROLE-38 Expected e tidak menyebut surface untuk "aktif"; spec memakai Tab Total Control dan Detail.
  - TC-GS-ROLE-36 Expected d: Pagination "aktif" di Detail "Manage TAG" mensyaratkan lebih dari 10 baris; Pre-setup TC tidak menyebut jumlah baris Manage TAG.
  - TC-GS-ROLE-36 sampai TC-GS-ROLE-38 tidak menyebut halaman tempat baris Dewi Lestari, Siti Nurhaliza, Rina Putri, dan Doni Pratama berada; spec mengasumsikan halaman 1 pada urutan default.
