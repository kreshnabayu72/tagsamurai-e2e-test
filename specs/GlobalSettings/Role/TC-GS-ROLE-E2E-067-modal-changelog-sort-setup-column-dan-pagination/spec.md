---
id: TC-GS-ROLE-E2E-067-modal-changelog-sort-setup-column-dan-pagination
title: "Modal Changelog: Sort per Kolom, Setup Column, dan Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-202
  - TC-GS-ROLE-203
  - TC-GS-ROLE-206
coverage:
  web: automated
---

# Modal Changelog: Sort per Kolom, Setup Column, dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Akun pemicu seeding (sesi API, bukan sesi UI): Manage user and role C/R/U/D, Hendra Wijaya (`Hendra W`), `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 5), kredensial `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD`, dipakai hanya agar Changelog memuat nilai Modified By kedua (`Hendra W`) untuk asersi sort Modified By.
- Environment variable: `GS_TC_PASSWORD`; env baru yang perlu didaftarkan di `spectra.config.ts` dan `.env.example` oleh tim FE: `GS_ROLE_MANAGE_CRUD_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > System.
- Seeding (lewat API di hook `before`, urutan sebagai berikut; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level`, POST/PATCH/DELETE `/v2/iam/products/{product}/roles/capabilities/users`; asumsi seeding lewat API mencatat entri Changelog sama seperti aksi UI). Jumlah entri seed ditentukan dari seeding, bukan dibaca dari tabel (bagian 8b butir 10):
  - Changelog Tab System dan Detail "Manage TAG" (15 entri seed): Citra Dewanti (Pre-setup #18) oleh Ahmad Fauzi di-assign Role Manage TAG (satu entri `Assign`, Field `Access`, Old Value `—`, New Value `Assigned`); Edit CRUD Update baris Manage TAG Citra Dewanti oleh Ahmad Fauzi sebanyak 10 kali berselang-seling (centang lalu hapus centang, lima pasang; sepuluh entri `Edit`, Field `Update`, Old Value dan New Value `Active` dan `Inactive`); Edit CRUD Update oleh Hendra Wijaya satu kali (satu entri `Edit`, Modified By `Hendra W`); Remove baris Manage TAG Citra Dewanti oleh Ahmad Fauzi (satu entri `Remove`, Old Value `Assigned`, New Value `—`). Doni Pratama (Pre-setup #10): Edit CRUD Delete baris Manage files diubah dari checked ke unchecked lalu dikembalikan oleh Ahmad Fauzi (dua entri `Edit`, Field `Delete`, Role — User `Manage files — Doni Pratama`). Dengan demikian Changelog Tab System memuat sedikitnya 11 entri, sedikitnya dua nilai berbeda pada kolom Action, Role — User, Field, dan Modified By, serta nilai `—` pada Old Value dan New Value (S-11).
  - Changelog Tab Total Control (empat entri seed): Sari Wulandari (Pre-setup #11) dan Fikri Ramadhan (Pre-setup #18) masing-masing di-assign Total Control lalu di-Remove Total Control oleh Ahmad Fauzi, sehingga kolom User Name memuat dua nilai berbeda.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Sari Wulandari, Fikri Ramadhan, dan Citra Dewanti dikembalikan ke kondisi kandidat Pre-setup #11 dan #18 (Active, Access Global Settings dicentang, tanpa access level, tanpa baris role) lewat API; nilai CRUD baris Manage files Doni Pratama kembali ke nilai Pre-setup (Delete checked); konfigurasi kolom Modal Changelog Tab Total Control, Tab System, dan Detail "Manage TAG" dikembalikan ke default; Modal Changelog ditutup. Entri Changelog tidak bisa dihapus. Pengubahan baris Pre-setup Doni Pratama dipulihkan dalam spec yang sama (S-06).
- Sort Modal Changelog (tiga klik berurutan; "default" = urutan awal Date terbaru dulu):

| Kolom | Varian | Klik 1 | Klik 2 | Klik 3 | Nilai kosong |
|---|---|---|---|---|---|
| Date | Tab System | Oldest First | Newest First | default (Newest First) | tidak ada |
| Action | Tab System | A-Z | Z-A | default | tidak ada |
| Role — User | Tab System | A-Z | Z-A | default | tidak ada |
| Field | Tab System | A-Z | Z-A | default | tidak ada |
| Modified By | Tab System | A-Z | Z-A | default | tidak ada |
| Old Value | Tab System | A-Z | Z-A | default | baris `—` (Assign) di akhir pada klik 1, di awal pada klik 2 |
| New Value | Tab System | A-Z | Z-A | default | baris `—` (Remove) di akhir pada klik 1, di awal pada klik 2 |
| User Name | Tab Total Control | A-Z | Z-A | default | tidak ada |

- Konfigurasi kolom tabel utama Tab Total Control berada pada default (`Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`) saat spec dimulai.
- Kemampuan teknis: membaca urutan baris tabel Modal Changelog; membaca jumlah baris yang tampil dan halaman aktif pagination.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-202: Sort Modal Changelog

1. Klik icon Changelog di Table Tools
2. Untuk setiap kolom `Date`, `Action`, `Role — User`, `Field`, `Modified By` (langkah 2 sampai 7, parameter di tabel Sort Modal Changelog): klik header kolom
3. Verifikasi urutan baris sesuai kolom "Klik 1" pada tabel
4. Klik header kolom
5. Verifikasi urutan baris sesuai kolom "Klik 2" pada tabel
6. Klik header kolom
7. Verifikasi urutan baris kembali ke default (Date terbaru dulu)
8. Untuk setiap kolom `Old Value` lalu `New Value` (langkah 8 sampai 15, parameter di tabel Sort Modal Changelog): klik header kolom
9. Verifikasi urutan baris sesuai kolom "Klik 1" pada tabel
10. Verifikasi baris bernilai kosong (`—`) berada di akhir
11. Klik header kolom
12. Verifikasi urutan baris sesuai kolom "Klik 2" pada tabel
13. Verifikasi baris bernilai kosong (`—`) berada di awal
14. Klik header kolom
15. Verifikasi urutan baris kembali ke default (Date terbaru dulu)
16. Tutup Modal Changelog lewat `[✕]`
17. Klik Tab `Total Control`
18. Klik icon Changelog di Table Tools
19. Klik header `User Name`
20. Verifikasi urutan baris kolom `User Name` A-Z
21. Klik header `User Name`
22. Verifikasi urutan baris kolom `User Name` Z-A
23. Klik header `User Name`
24. Verifikasi urutan baris kembali ke default (Date terbaru dulu)

### TC-GS-ROLE-203: Setup Column Modal Changelog

25. Klik header (⋯) di modal
26. Verifikasi overlay Column Visibility mendaftar `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
27. Verifikasi ketujuh kolom tercentang
28. Verifikasi checkbox ketujuh kolom enabled
29. Klik `[Setup Column]`
30. Hapus centang `Field`
31. Klik `[Save]`
32. Verifikasi kolom `Field` tersembunyi di Modal Changelog
33. Tutup Modal Changelog lewat `[✕]`
34. Klik icon Changelog di Table Tools
35. Verifikasi kolom `Field` tetap tersembunyi
36. Klik header (⋯) di modal
37. Klik `[Setup Column]`
38. Klik `[Reset to Default]`
39. Klik `[Save]`
40. Verifikasi ketujuh kolom `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil kembali
41. Tutup Modal Changelog lewat `[✕]`
42. Verifikasi kolom tabel utama Tab Total Control tetap `Name`, `Position`, `Division`, `Status`, `Modified By`, dan `Last Updated`
43. Klik Tab `System`
44. Klik icon Changelog di Table Tools
45. Klik header (⋯) di modal
46. Verifikasi overlay Column Visibility mendaftar `Date`, `Action`, `Role — User`, `Field`, `Old Value`, `New Value`, dan `Modified By` (Role — User menggantikan User Name)
47. Verifikasi ketujuh kolom tercentang
48. Verifikasi checkbox ketujuh kolom enabled
49. Tutup overlay Column Visibility dengan Esc
50. Tutup Modal Changelog lewat `[✕]`
51. Klik Role Name `Manage TAG`
52. Klik icon Changelog di Table Tools
53. Klik header (⋯) di modal
54. Verifikasi overlay Column Visibility mendaftar `Date`, `Action`, `Role — User`, `Field`, `Old Value`, `New Value`, dan `Modified By` (Role — User menggantikan User Name)
55. Verifikasi ketujuh kolom tercentang
56. Verifikasi checkbox ketujuh kolom enabled
57. Tutup overlay Column Visibility dengan Esc
58. Tutup Modal Changelog lewat `[✕]`

### TC-GS-ROLE-206: Pagination Modal Changelog

59. Klik breadcrumb `System`
60. Klik icon Changelog di Table Tools
61. Verifikasi pagination default 10 baris per halaman
62. Buka dropdown page size
63. Verifikasi opsi page size `10`, `25`, `50`, dan `100`
64. Tutup dropdown page size dengan Esc
65. Klik halaman 2
66. Verifikasi halaman 2 aktif dan menampilkan sedikitnya satu baris
67. Klik halaman 1
68. Verifikasi halaman 1 aktif dan menampilkan 10 baris
69. Buka dropdown page size
70. Pilih `25`
71. Verifikasi page size 25 aktif
72. Verifikasi tabel menampilkan lebih dari 10 baris
73. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (202, 203, 206) dipertahankan.
- Urutan kolom pada TC-GS-ROLE-202 diubah dari urutan TC sumber (Date, Action, Old Value, Role — User, Field, New Value, Modified By, User Name) menjadi kolom tanpa nilai kosong lebih dulu (langkah 2 sampai 7), kolom bernilai kosong (langkah 8 sampai 15), lalu User Name di Tab Total Control (langkah 19 sampai 24), supaya tiap kelompok memakai satu blok ulang dengan parameter di tabel Sort Modal Changelog tanpa langkah bersyarat.
- Urutan langkah TC-GS-ROLE-206 diubah dari TC sumber (default, ubah page size 25, navigasi halaman): navigasi halaman 2 dilakukan pada page size 10 (langkah 65 sampai 68) sebelum page size diubah ke 25 (langkah 69 sampai 72), karena seeding menghasilkan sedikitnya 11 entri tetapi tidak menjamin lebih dari 25 entri, sehingga navigasi antar-halaman hanya bermakna pada page size 10.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 16, 33, 41, 50, 58, dan 73 (menutup Modal Changelog), langkah 17 dan 43 (pindah tab), langkah 49 dan 57 (menutup overlay), langkah 51 dan 59 (masuk ke Detail "Manage TAG" lalu kembali ke Tab System lewat breadcrumb), langkah 64 (menutup dropdown), langkah 36 sampai 39 (`[Reset to Default]` lalu `[Save]` untuk memulihkan konfigurasi kolom), dan langkah 34 (membuka modal lagi, sesuai Langkah Uji 3 TC-GS-ROLE-203).
- Verifikasi varian System dan Detail "Manage TAG" pada langkah 43 sampai 58 berasal dari klausa "varian System/Detail: Role — User menggantikan User Name" di Expected a TC-GS-ROLE-203.
- Spec melewati sekitar 35 langkah (73 langkah nominal, sekitar 100 dengan ekspansi dua blok ulang) karena TC-GS-ROLE-202 mengurutkan delapan kolom dengan tiga klik tiap kolom dan tiap klausa Expected dipecah menjadi satu `Verifikasi` (S-01). Semuanya satu kelas harness (kontrol tabel Modal Changelog), satu akun, dan satu dataset seeding; tiap blok TC berdiri sendiri (membuka modalnya sendiri), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-202 Expected a: kolom Date berketelitian menit dan entri seed dibuat dalam rentang menit yang sama, sehingga urutan Oldest First dan Newest First hanya teramati pada entri dengan Date berbeda yang sudah ada di environment.
  - TC-GS-ROLE-202 Expected c dan f menyebut posisi nilai kosong untuk Old Value dan New Value tetapi tidak menyebut "default" kolom-kolom lain; spec memakai urutan default Date terbaru dulu.
  - TC-GS-ROLE-206 Langkah Uji 3 ("Navigasi halaman") tidak menyebut halaman tujuan; spec memakai halaman 2 lalu halaman 1 pada page size 10.
  - TC-GS-ROLE-206 Expected a ("Default 10") tidak menyebut jumlah baris yang tampil; spec mengasersi pagination default 10 baris per halaman.
  - TC-GS-ROLE-202 dan 206 menyebut precondition "≥3 entry" dan ">10 entry" tanpa menyebut cara menyediakannya; spec men-seed lewat API (Prerequisites).
