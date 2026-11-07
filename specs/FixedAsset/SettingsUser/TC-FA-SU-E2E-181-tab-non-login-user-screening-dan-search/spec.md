---
id: TC-FA-SU-E2E-181-tab-non-login-user-screening-dan-search
title: "Tab Non-Login User: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-538
  - TC-FA-SU-539
  - TC-FA-SU-540
  - TC-FA-SU-541
coverage:
  web: automated
---

# Tab Non-Login User: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Tabel parameter "Ikon Table Tools":

| Ikon | Tooltip |
|---|---|
| `Search` | `Search` |
| `Filter` | `Filter` |
| `Download` | `Download` |
- Tabel parameter "Search kelas teks":

| Kolom | Keyword | Hasil |
|---|---|---|
| Name | `Printer` | `Printer Lantai 5` (1 baris) |
| Email | `copier` | `Mesin Fotokopi Lt.3` (1 baris) |
| Employee ID | `EMP-` | tidak ada baris (0 baris) |
| Position | `Manager` | tidak ada baris (0 baris) |
| Division | `Facility` | `Ruang Meeting Anggrek` (1 baris) |

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-538: Screening Table Tools, kolom, dan default sort

2. Verifikasi header menampilkan Table Tools `Search`, `Filter`, `Download` rata kanan
3. Untuk setiap baris tabel "Ikon Table Tools" (langkah 3 sampai 4): hover ikon baris itu
4. Verifikasi tooltip sama dengan kolom "Tooltip" baris itu
5. Klik icon Search
6. Verifikasi placeholder Search `Search name, email, or employee ID...`
7. Klik `←` pada kotak Search
8. Verifikasi kolom `Name (sortable)`, `Email (sortable)`, `Employee ID (sortable)`, `Position (sortable)`, `Division (sortable)`, `Active (sortable)`, `Last Update (sortable)`, dan `Column Visibility (⋯)`
9. Verifikasi sel kolom Column Visibility (⋯) pada tiap baris kosong tanpa row action
10. Klik header kolom Column Visibility (⋯)
11. Verifikasi overlay Column Visibility terbuka
12. Tekan Esc untuk menutup overlay Column Visibility
13. Verifikasi default sort Name ascending: `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`
14. Klik dropdown page size
15. Verifikasi footer pagination 10 data per halaman dengan page size 10, 25, 50, 100
16. Tekan Esc untuk menutup pilihan page size

### TC-FA-SU-539: Search kelas teks

17. Untuk setiap baris tabel "Search kelas teks" (langkah 17 sampai 19): ketik Search keyword baris itu, tekan Enter
18. Verifikasi tabel menyisakan baris sesuai kolom "Hasil" baris itu
19. Klik `←` pada kotak Search

### TC-FA-SU-540: Search kelas exact (Active)

20. Ketik Search `inactive`, tekan Enter
21. Verifikasi keyword `inactive` menyisakan `Printer Lantai 5` (1 baris)
22. Klik `←` pada kotak Search

### TC-FA-SU-541: Search kelas enum (Temporary User)

23. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
24. Centang kolom Temporary User pada daftar Setup Column
25. Klik `[Save]`
26. Ketik Search `No`, tekan Enter
27. Verifikasi keyword `No` menyisakan `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` (5 baris)
28. Klik `←` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` di User List supaya baris target tidak bergantung posisi halaman (langkah 1, 8b butir 13, R-16) lalu membuka Detail Budi Santoso; `←` pada kotak Search sesudah tiap keyword (S-09).
- Langkah penghubung tambahan (S-03): klik header kolom Column Visibility (⋯) (langkah 10) dan `Esc` (langkah 12) memicu dan menutup overlay untuk `Verifikasi` overlay (TC-FA-SU-538 Expected b); klik dropdown page size (langkah 14) dan `Esc` (langkah 16) membuka dan menutup pilihan page size untuk `Verifikasi` pilihan page size (Expected d, S-14).
- Langkah berulang per baris tabel parameter: tabel "Ikon Table Tools" pada langkah 3 sampai 4 (3 iterasi); tabel "Search kelas teks" pada langkah 17 sampai 19 (5 iterasi).
- Jumlah langkah: 28 tertulis, 44 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (44 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-539 Expected c dan d: keyword `EMP-` (Employee ID) dan `Manager` (Position) menghasilkan 0 baris karena nilai kolom itu kosong pada seluruh Non-Login User (TC-FA-SU-552); asersi 0 baris tidak membuktikan pencarian kolom tersebut. Anchor positif adalah hasil baris sebelumnya pada surface yang sama.
