---
id: TC-FA-SU-E2E-183-tab-non-login-user-search-dan-sort
title: "Tab Non-Login User: Search dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-545
  - TC-FA-SU-546
  - TC-FA-SU-1033
coverage:
  web: automated
---

# Tab Non-Login User: Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Custom Field Shift (Pre-setup #31, `FaUserMain`): Gudang Cabang Bekasi `Morning`, Kendaraan Operasional B 1234 XY `Night`, Mesin Fotokopi Lt.3 `Morning`, Printer Lantai 5 `Night`, Ruang Meeting Anggrek `Morning`; kolom curated Shift muncul setelah ditampilkan lewat Setup Column.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Tabel parameter "Sort kelas teks":

| Kolom | Klik 1 (ascending ↑) | Klik 2 (descending ↓) | Klik 3 (netral, default) |
|---|---|---|---|
| Name | `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` | `Ruang Meeting Anggrek`, `Printer Lantai 5`, `Mesin Fotokopi Lt.3`, `Kendaraan Operasional B 1234 XY`, `Gudang Cabang Bekasi` | `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']`, `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']` |
| Email | `Mesin Fotokopi Lt.3`, `Kendaraan Operasional B 1234 XY`, `Ruang Meeting Anggrek`, `Printer Lantai 5`, `Gudang Cabang Bekasi` | `Gudang Cabang Bekasi`, `Printer Lantai 5`, `Ruang Meeting Anggrek`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3` | `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']`, `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']` |
| Division | `Ruang Meeting Anggrek`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Kendaraan Operasional B 1234 XY`, `Gudang Cabang Bekasi` | `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` | `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']`, `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']` |
- Tabel parameter "Sort kelas teks-e":

| Kolom | Klik 1 (ascending ↑) | Klik 2 (descending ↓) | Klik 3 (netral, default) |
|---|---|---|---|
| Employee ID | `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` | `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` | `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']`, `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']` |
| Position | `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` | `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek` | `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']`, `['Gudang Cabang Bekasi', 'Kendaraan Operasional B 1234 XY', 'Mesin Fotokopi Lt.3', 'Printer Lantai 5', 'Ruang Meeting Anggrek']` |

## Test Steps

1. Buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-545: Sort kelas teks (Name, Email, Division)

2. Untuk setiap baris tabel "Sort kelas teks" (langkah 2 sampai 7): klik header kolom baris itu satu kali
3. Verifikasi urutan ascending (↑) sama dengan kolom "Klik 1" baris itu
4. Klik header kolom baris itu kedua kali
5. Verifikasi urutan descending (↓) sama dengan kolom "Klik 2" baris itu
6. Klik header kolom baris itu ketiga kali
7. Verifikasi urutan netral kembali ke default sama dengan kolom "Klik 3" baris itu

### TC-FA-SU-546: Sort kelas teks-e (Employee ID, Position)

8. Untuk setiap baris tabel "Sort kelas teks-e" (langkah 8 sampai 13): klik header kolom baris itu satu kali
9. Verifikasi urutan ascending (↑) sama dengan kolom "Klik 1" baris itu
10. Klik header kolom baris itu kedua kali
11. Verifikasi urutan descending (↓) sama dengan kolom "Klik 2" baris itu
12. Klik header kolom baris itu ketiga kali
13. Verifikasi urutan netral kembali ke default sama dengan kolom "Klik 3" baris itu

### TC-FA-SU-1033: Search kelas cf (Shift)

14. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
15. Centang kolom Shift pada daftar Setup Column
16. Klik `[Save]`
17. Ketik Search `Night`, tekan Enter
18. Verifikasi keyword `Night` menyisakan `Kendaraan Operasional B 1234 XY`, `Printer Lantai 5` (2 baris)
19. Klik `←` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso; `←` pada kotak Search sesudah TC-FA-SU-1033 (S-09). TC-FA-SU-1033 ditaruh terakhir karena menambah kolom curated Shift.
- Langkah berulang per baris tabel parameter: tabel "Sort kelas teks" pada langkah 2 sampai 7 (3 iterasi); tabel "Sort kelas teks-e" pada langkah 8 sampai 13 (2 iterasi).
- Jumlah langkah: 19 tertulis, 37 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (37 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7).
- Temuan untuk QA:
  - TC-FA-SU-546: Employee ID dan Position tidak memiliki dua nilai distinct (seluruh nilai kosong), sehingga urutan asc, desc, dan netral identik; asersi ini tidak membuktikan fungsi sort kolom itu (S-11).
