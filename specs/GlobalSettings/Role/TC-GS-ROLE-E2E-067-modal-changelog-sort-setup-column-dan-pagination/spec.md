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
- Data Dinamis milik spec (dibuat lewat seeding API di hook `before`, pola spec 051; nama endpoint tidak disebut di TC dan PRD, tidak dikarang di spec): tiga user target seed bersuffix run, yaitu `Citra Dewanti {runId}-067` (`citradewanti+{runId}-067@qwertysystem.net`), `Sari Wulandari {runId}-067` (`sariwulandari+{runId}-067@qwertysystem.net`), dan `Fikri Ramadhan {runId}-067` (`fikriramadhan+{runId}-067@qwertysystem.net`), masing-masing Active, Access Global Settings dicentang, tanpa access level, dan tanpa baris role (setara kandidat Pre-setup #18 dan #11). Karena nama target milik spec dan unik per run, entri audit trail permanen dari run lain atau spec lain tidak masuk ke hasil Search dan Filter di bawah.
- Seeding aksi (lewat API di hook `before`, urutan sebagai berikut; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level`, POST/PATCH/DELETE `/v2/iam/products/{product}/roles/capabilities/users`; asumsi seeding lewat API mencatat entri Changelog sama seperti aksi UI). Jumlah entri seed ditentukan dari seeding, bukan dibaca dari tabel (bagian 8b butir 10):
  - Changelog Tab System dan Detail "Manage TAG" (13 entri seed). Kelompok seed pertama: Citra Dewanti {runId}-067 oleh Ahmad Fauzi di-assign Role Manage TAG (satu entri `Assign`, Field `Access`, Old Value `—`, New Value `Assigned`); Edit CRUD Update baris Manage TAG Citra Dewanti {runId}-067 oleh Ahmad Fauzi sebanyak 4 kali berselang-seling (centang lalu hapus centang, dua pasang; empat entri `Edit`, Field `Update`, Old Value dan New Value `Active` dan `Inactive`). Hook `before` lalu menunggu sampai menit berganti (maksimum 60 detik; kolom Date berketelitian menit), memisahkan dua kelompok seed. Kelompok seed kedua: Edit CRUD Update oleh Hendra Wijaya satu kali pada baris Manage TAG Citra Dewanti {runId}-067 (satu entri `Edit`, Modified By `Hendra W`); Citra Dewanti {runId}-067 di-assign Role Manage files oleh Ahmad Fauzi (satu entri `Assign`, Role — User `Manage files — Citra Dewanti {runId}-067`, Field `Access`, Old Value `—`, New Value `Assigned`); Remove baris Manage TAG dan baris Manage files Citra Dewanti {runId}-067 oleh Ahmad Fauzi (dua entri `Remove`, Old Value `Assigned`, New Value `—`). Doni Pratama (Pre-setup #10): Edit CRUD Delete baris Manage files diubah dari checked ke unchecked lalu dikembalikan oleh Ahmad Fauzi sebanyak dua kali (empat entri `Edit`, Field `Delete`, Role — User `Manage files — Doni Pratama`), sebagai entri tambahan agar Changelog Tab System memuat lebih dari 10 entri (TC-GS-ROLE-206).
  - Pembatas dataset sort Tab System (S-14): audit trail permanen tumbuh dan halaman 1 tanpa pembatas didominasi entri spec lain, sehingga langkah sort memakai Search `Citra Dewanti {runId}-067` (Role — User); nama target bersuffix milik spec, sehingga hasil Search hanya memuat entri seed run ini dan 9 entri berada dalam satu halaman di setiap run. Hasil Search memuat 9 entri seed Citra Dewanti {runId}-067 dalam satu halaman, dengan dua nilai berbeda pada kolom Action (`Assign`, `Edit`, `Remove`), Role — User (`Manage TAG — Citra Dewanti {runId}-067`, `Manage files — Citra Dewanti {runId}-067`), Field (`Access`, `Update`), Modified By (`Ahmad F`, `Hendra W`), Old Value, dan New Value (termasuk `—`) serta Date berbeda menit (dua kelompok seed). Asersi sort Date dibatasi pada pasangan entri yang berbeda menit (kelompok seed pertama lawan kedua); urutan entri se-menit tidak diasersi (S-12; konvensi bagian 6, `[KEPUTUSAN 2026-11-02]`).
  - Changelog Tab Total Control (empat entri seed): Sari Wulandari {runId}-067 dan Fikri Ramadhan {runId}-067 masing-masing di-assign Total Control lalu di-Remove Total Control oleh Ahmad Fauzi (Sari Wulandari {runId}-067 pada kelompok seed pertama, Fikri Ramadhan {runId}-067 pada kelompok kedua sesudah jeda menit), sehingga kolom User Name memuat dua nilai berbeda. Langkah sort Tab Total Control memakai Filter User Name `Sari Wulandari {runId}-067` dan `Fikri Ramadhan {runId}-067` sebagai pembatas dataset (S-14); hasil Filter memuat empat entri dalam satu halaman. Batas yang sama berlaku untuk Tab Total Control: asersi urutan Date (kembali ke default, langkah 33) hanya pada pasangan entri berbeda menit, yaitu entri Fikri Ramadhan {runId}-067 di atas entri Sari Wulandari {runId}-067; urutan dua entri se-menit milik user yang sama tidak diasersi.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah, tidak berasumsi seeding berhasil penuh): ketiga user seed bersuffix (`Citra Dewanti {runId}-067`, `Sari Wulandari {runId}-067`, `Fikri Ramadhan {runId}-067`) dihapus lewat API (tanpa menyentuh data Pre-setup #11 dan #18); nilai CRUD baris Manage files Doni Pratama kembali ke nilai Pre-setup (Delete checked); konfigurasi kolom Modal Changelog Tab Total Control, Tab System, dan Detail "Manage TAG" dikembalikan ke default lewat penghapusan preferensi kolom di browser (bagian 4 konvensi; langkah 48 sampai 51 memulihkannya lewat UI di dalam spec); Modal Changelog ditutup. Entri Changelog tidak bisa dihapus. Pengubahan baris Pre-setup Doni Pratama dipulihkan dalam spec yang sama (S-06).
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
- Kemampuan teknis: membaca urutan baris tabel Modal Changelog; menghapus preferensi kolom (Setup Column) tabel Modal Changelog di penyimpanan browser (disediakan tim FE); membaca jumlah baris yang tampil dan halaman aktif pagination.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-202: Sort Modal Changelog

1. Klik icon Changelog di Table Tools
2. Ketik Search `Citra Dewanti {runId}-067`, tekan Enter
3. Verifikasi tabel memuat sedikitnya dua baris hasil
4. Untuk setiap kolom `Date`, `Action`, `Role — User`, `Field`, `Modified By` (langkah 4 sampai 9, parameter di tabel Sort Modal Changelog): klik header kolom
5. Verifikasi urutan baris sesuai kolom "Klik 1" pada tabel
6. Klik header kolom
7. Verifikasi urutan baris sesuai kolom "Klik 2" pada tabel
8. Klik header kolom
9. Verifikasi urutan baris kembali ke default (Date terbaru dulu; hanya pada pasangan entri berbeda menit)
10. Untuk setiap kolom `Old Value` lalu `New Value` (langkah 10 sampai 19, parameter di tabel Sort Modal Changelog): klik header kolom
11. Verifikasi urutan baris sesuai kolom "Klik 1" pada tabel
12. Klik halaman terakhir pada pagination
13. Verifikasi baris bernilai kosong (`—`) berada di akhir
14. Klik header kolom
15. Verifikasi urutan baris sesuai kolom "Klik 2" pada tabel
16. Klik halaman pertama pada pagination
17. Verifikasi baris bernilai kosong (`—`) berada di awal
18. Klik header kolom
19. Verifikasi urutan baris kembali ke default (Date terbaru dulu; hanya pada pasangan entri berbeda menit)
20. Klik `(←)` pada kotak Search
21. Tutup Modal Changelog lewat `[✕]`
22. Klik Tab `Total Control`
23. Klik icon Changelog di Table Tools
24. Klik Filter
25. Pilih User Name `Sari Wulandari {runId}-067` dan `Fikri Ramadhan {runId}-067`
26. Klik `[Apply]`
27. Verifikasi tabel memuat sedikitnya dua baris hasil
28. Klik header `User Name`
29. Verifikasi urutan baris kolom `User Name` A-Z
30. Klik header `User Name`
31. Verifikasi urutan baris kolom `User Name` Z-A
32. Klik header `User Name`
33. Verifikasi urutan baris kembali ke default (Date terbaru dulu; hanya pada pasangan entri berbeda menit, entri Fikri Ramadhan {runId}-067 di atas entri Sari Wulandari {runId}-067)
34. Klik Filter
35. Klik `[Clear Field]`
36. Klik `[Apply]`

### TC-GS-ROLE-203: Setup Column Modal Changelog

37. Klik header (⋯) di modal
38. Verifikasi overlay Column Visibility mendaftar `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`
39. Verifikasi ketujuh kolom tercentang
40. Verifikasi checkbox ketujuh kolom enabled
41. Klik `[Setup Column]`
42. Hapus centang `Field`
43. Klik `[Save]`
44. Verifikasi kolom `Field` tersembunyi di Modal Changelog
45. Tutup Modal Changelog lewat `[✕]`
46. Klik icon Changelog di Table Tools
47. Verifikasi kolom `Field` tetap tersembunyi
48. Klik header (⋯) di modal
49. Klik `[Setup Column]`
50. Klik `[Reset to Default]`
51. Klik `[Save]`
52. Verifikasi ketujuh kolom `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil kembali
53. Tutup Modal Changelog lewat `[✕]`
54. Verifikasi kolom tabel utama Tab Total Control tetap `Name`, `Position`, `Division`, `Status`, `Modified By`, dan `Last Updated`
55. Klik Tab `System`
56. Klik icon Changelog di Table Tools
57. Klik header (⋯) di modal
58. Verifikasi overlay Column Visibility mendaftar `Date`, `Action`, `Role — User`, `Field`, `Old Value`, `New Value`, dan `Modified By` (Role — User menggantikan User Name)
59. Verifikasi ketujuh kolom tercentang
60. Verifikasi checkbox ketujuh kolom enabled
61. Tutup overlay Column Visibility dengan Esc
62. Tutup Modal Changelog lewat `[✕]`
63. Klik Role Name `Manage TAG`
64. Klik icon Changelog di Table Tools
65. Klik header (⋯) di modal
66. Verifikasi overlay Column Visibility mendaftar `Date`, `Action`, `Role — User`, `Field`, `Old Value`, `New Value`, dan `Modified By` (Role — User menggantikan User Name)
67. Verifikasi ketujuh kolom tercentang
68. Verifikasi checkbox ketujuh kolom enabled
69. Tutup overlay Column Visibility dengan Esc
70. Tutup Modal Changelog lewat `[✕]`

### TC-GS-ROLE-206: Pagination Modal Changelog

71. Klik breadcrumb `System`
72. Klik icon Changelog di Table Tools
73. Verifikasi pagination default 10 baris per halaman
74. Buka dropdown page size
75. Verifikasi opsi page size `10`, `25`, `50`, dan `100`
76. Tutup dropdown page size dengan Esc
77. Klik halaman 2
78. Verifikasi halaman 2 aktif dan menampilkan sedikitnya satu baris
79. Klik halaman 1
80. Verifikasi halaman 1 aktif dan menampilkan 10 baris
81. Buka dropdown page size
82. Pilih `25`
83. Verifikasi page size 25 aktif
84. Verifikasi tabel menampilkan lebih dari 10 baris
85. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (202, 203, 206) dipertahankan.
- Urutan kolom pada TC-GS-ROLE-202 diubah dari urutan TC sumber (Date, Action, Old Value, Role — User, Field, New Value, Modified By, User Name) menjadi kolom tanpa nilai kosong lebih dulu (langkah 4 sampai 9), kolom bernilai kosong (langkah 10 sampai 19), lalu User Name di Tab Total Control (langkah 28 sampai 33), supaya tiap kelompok memakai satu blok ulang dengan parameter di tabel Sort Modal Changelog tanpa langkah bersyarat.
- Urutan langkah TC-GS-ROLE-206 diubah dari TC sumber (default, ubah page size 25, navigasi halaman): navigasi halaman 2 dilakukan pada page size 10 (langkah 77 sampai 80) sebelum page size diubah ke 25 (langkah 81 sampai 84), karena seeding menghasilkan sedikitnya 11 entri tetapi tidak menjamin lebih dari 25 entri, sehingga navigasi antar-halaman hanya bermakna pada page size 10.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 21, 45, 53, 62, 70, dan 85 (menutup Modal Changelog), langkah 22 dan 55 (pindah tab), langkah 61 dan 69 (menutup overlay), langkah 63 dan 71 (masuk ke Detail "Manage TAG" lalu kembali ke Tab System lewat breadcrumb), langkah 76 (menutup dropdown), langkah 48 sampai 51 (`[Reset to Default]` lalu `[Save]` untuk memulihkan konfigurasi kolom), dan langkah 46 (membuka modal lagi, sesuai Langkah Uji 3 TC-GS-ROLE-203). Pembatas dataset sort (S-14, R-16): langkah 2 (Search `Citra Dewanti {runId}-067`) dan 20 (mengosongkan Search sebelum modal ditutup); langkah 24 sampai 26 (Filter User Name) dan 34 sampai 36 (mengosongkan Filter). Langkah 12 dan 16 (pindah ke halaman terakhir lalu halaman pertama pagination) mendahului asersi `—` di akhir dan di awal (S-14); hasil Search memuat satu halaman, sehingga halaman terakhir sama dengan halaman pertama.
- Asersi tambahan (bukan dari Expected TC, alasannya S-14 dan bagian 8b butir 2): langkah 3 dan 27 (tabel hasil Search atau Filter memuat sedikitnya dua baris, pembanding sebelum asersi urutan).
- Verifikasi varian System dan Detail "Manage TAG" pada langkah 55 sampai 70 berasal dari klausa "varian System/Detail: Role — User menggantikan User Name" di Expected a TC-GS-ROLE-203.
- Spec melewati sekitar 35 langkah (85 langkah nominal, sekitar 120 dengan ekspansi dua blok ulang) karena TC-GS-ROLE-202 mengurutkan delapan kolom dengan tiga klik tiap kolom dan tiap klausa Expected dipecah menjadi satu `Verifikasi` (S-01). Semuanya satu kelas harness (kontrol tabel Modal Changelog), satu akun, dan satu dataset seeding; tiap blok TC berdiri sendiri (membuka modalnya sendiri), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-202 Expected a: kolom Date berketelitian menit; hook `before` menunggu sampai menit berganti di antara dua kelompok seed supaya hasil Search memuat Date berbeda menit, dan urutan entri se-menit tidak diasersi.
  - TC-GS-ROLE-202 Expected c dan f menyebut posisi nilai kosong untuk Old Value dan New Value tetapi tidak menyebut "default" kolom-kolom lain; spec memakai urutan default Date terbaru dulu.
  - TC-GS-ROLE-206 Langkah Uji 3 ("Navigasi halaman") tidak menyebut halaman tujuan; spec memakai halaman 2 lalu halaman 1 pada page size 10.
  - TC-GS-ROLE-206 Expected a ("Default 10") tidak menyebut jumlah baris yang tampil; spec mengasersi pagination default 10 baris per halaman.
  - TC-GS-ROLE-202 dan 206 menyebut precondition "≥3 entry" dan ">10 entry" tanpa menyebut cara menyediakannya; spec men-seed lewat API (Prerequisites).
