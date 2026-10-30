---
id: TC-GS-ROLE-E2E-061-download-tab-system-dan-detail-isi-file
title: "Download Tab System dan Detail: Nama File dan Isi File"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-185
  - TC-GS-ROLE-194
  - TC-GS-ROLE-303
coverage:
  web: automated
---

# Download Tab System dan Detail: Nama File dan Isi File

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; berkas dibuat dari backend nyata.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > System dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data (hanya dibaca): Tab System memuat enam Role Name berurutan fixed (`Import data`, `Manage files`, `Manage hardware`, `Manage master reference`, `Manage TAG`, `Manage user and role`) dengan kolom `Users` berisi angka; Detail "Manage TAG" berisi sedikitnya 4 user dengan Position dan Division berbeda (precondition TC) dan kolom CRUD `Read` dan `Update`; Detail "Manage user and role" tersedia.
- Tabel "Format Download" untuk TC-GS-ROLE-194:

  | Format | Item overlay | Nama berkas |
  |---|---|---|
  | CSV | `Download as CSV` | `Role-Permission-Manage-TAG.csv` |
  | XLSX | `Download as XLSX` | `Role-Permission-Manage-TAG.xlsx` |

- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (jumlah baris, urutan baris, nilai sel, jenis nilai angka atau teks sel). Berkas unduhan dihapus di hook `after`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission, Tab System.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-185: Download Tab System sebagai CSV dan XLSX

1. Catat urutan baris tabel Tab System
2. Klik icon Download
3. Klik `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi file `Role-Permission-System.csv` terunduh
6. Buka isi file CSV yang diunduh
7. Verifikasi file memuat enam baris data sesuai urutan fixed yang dicatat
8. Klik icon Download
9. Klik `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `Role-Permission-System.xlsx` terunduh
12. Buka isi file XLSX yang diunduh
13. Verifikasi kolom `Users` bertipe angka di file XLSX
14. Verifikasi file memuat enam baris data sesuai urutan fixed yang dicatat

### TC-GS-ROLE-194: Download Detail sebagai CSV dan XLSX

15. Klik Role Name `Manage TAG`
Untuk setiap baris tabel "Format Download" (langkah 16 sampai 23):
16. Klik icon Download
17. Klik item overlay sesuai baris tabel
18. Verifikasi tidak ada toast sukses
19. Verifikasi file dengan nama berkas sesuai baris tabel terunduh
20. Buka isi file yang diunduh
21. Verifikasi file memuat sedikitnya satu baris data
22. Verifikasi kolom `Read` pada setiap baris data bernilai `Yes` atau `No`
23. Verifikasi kolom `Update` pada setiap baris data bernilai `Yes` atau `No`

### TC-GS-ROLE-303: Download Detail "Manage user and role" memakai nama file Title-Case-hyphen

24. Klik tombol Back browser
25. Klik Role Name `Manage user and role`
26. Klik icon Download
27. Klik `Download as CSV`
28. Verifikasi tidak ada toast sukses
29. Verifikasi file `Role-Permission-Manage-User-And-Role.csv` terunduh
30. Klik icon Download
31. Klik `Download as XLSX`
32. Verifikasi tidak ada toast sukses
33. Verifikasi file `Role-Permission-Manage-User-And-Role.xlsx` terunduh

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor (spec 069).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC dalam spec: 185, 194, 303 (urutan di `tc-role.md`: 185, 194, 303).
- Asersi absence atas state sementara (toast sukses) diletakkan segera sesudah klik pilihan format dan sebelum asersi berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh. Asersi "setiap baris data bernilai `Yes` atau `No`" didahului `Verifikasi` file memuat sedikitnya satu baris data.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah "Catat urutan baris tabel Tab System" (pembanding urutan fixed), langkah "Buka isi file ...", langkah "Klik Role Name `Manage TAG`" (membuka Detail), dan langkah "Klik tombol Back browser" (kembali ke Tab System sebelum membuka Detail "Manage user and role").
- Langkah 16 sampai 23 diulang untuk dua format pada tabel "Format Download" (8 langkah, 16 setelah ekspansi). Spec melewati sekitar 35 langkah (33 langkah nominal, 41 setelah ekspansi) karena tiga TC Download memakai tabel Tab System dan Detail yang sama dan satu kelas harness (binary buffer); tiap blok mengunduh berkas sendiri dan tidak bergantung pada berkas blok lain.
- TC-GS-ROLE-303 hanya mengasersi nama berkas dan tidak membuka isi berkas karena Expected-nya tidak menyebut isi.
- Pembagian TC lintas spec: TC-GS-ROLE-174 sampai 178 (Download Tab Total Control dan Read Only) di spec 058; TC-GS-ROLE-180 di spec 059; TC-GS-ROLE-179 dan 205 (Download gagal) di spec 069.
- Temuan untuk QA:
  - TC-GS-ROLE-185 Expected c: "Enam baris sesuai urutan fixed" tidak menyebut urutan konkret; spec membandingkan dengan urutan tabel Tab System yang dicatat sebelum Download.
  - TC-GS-ROLE-185 Expected a dan c berlaku untuk CSV dan XLSX; spec mengasersi isi berkas pada keduanya, sedangkan tipe angka `Users` hanya pada XLSX sesuai Expected b.
  - TC-GS-ROLE-194 Expected c: nilai `Yes` atau `No` tidak dipetakan ke checkbox user tertentu; spec hanya mengasersi nilai yang valid.
  - TC-GS-ROLE-185, 194, 303: TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan tersebut disediakan tim FE (Prerequisites).
