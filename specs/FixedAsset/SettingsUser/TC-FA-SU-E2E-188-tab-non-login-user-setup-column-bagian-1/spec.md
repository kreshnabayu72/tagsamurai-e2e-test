---
id: TC-FA-SU-E2E-188-tab-non-login-user-setup-column-bagian-1
title: "Tab Non-Login User: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-561
  - TC-FA-SU-562
coverage:
  web: automated
---

# Tab Non-Login User: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.
- Kolom `Last Update` tersisa sebagai satu-satunya kolom visible pada akhir langkah uncheck TC-FA-SU-561.
- Tabel parameter "Urutan drag Non-Login User" (urutan awal: `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`, `Last Update`):

| No | Kolom yang di-drag | Arah (satu posisi) | Urutan kolom sesudah drag |
|---|---|---|---|
| 1 | `Last Update` | atas | `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Last Update`, `Active` |
| 2 | `Division` | bawah | `Name`, `Email`, `Employee ID`, `Position`, `Last Update`, `Division`, `Active` |
| 3 | `Active` | atas | `Name`, `Email`, `Employee ID`, `Position`, `Last Update`, `Active`, `Division` |
| 4 | `Position` | bawah | `Name`, `Email`, `Employee ID`, `Last Update`, `Position`, `Active`, `Division` |
| 5 | `Employee ID` | bawah | `Name`, `Email`, `Last Update`, `Employee ID`, `Position`, `Active`, `Division` |
| 6 | `Email` | bawah | `Name`, `Last Update`, `Email`, `Employee ID`, `Position`, `Active`, `Division` |
| 7 | `Name` | bawah | `Last Update`, `Name`, `Email`, `Employee ID`, `Position`, `Active`, `Division` |

## Test Steps

1. Buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-561: Ceklis dan unceklis Setup Column kelas Hideable

2. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
3. Hilangkan centang kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active` pada daftar Setup Column (satu per satu)
4. Verifikasi Live Preview tidak lagi menampilkan kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active`
5. Hover checkbox kolom Last Update
6. Verifikasi checkbox kolom Last Update disabled sebagai satu-satunya kolom visible
7. Verifikasi tooltip `At least one column must remain visible.`
8. Klik `[Save]`
9. Verifikasi tabel tidak menampilkan kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active` dan hanya menampilkan kolom `Last Update`
10. Tekan F5
11. Verifikasi tabel tetap tidak menampilkan kolom `Name`, `Email`, `Employee ID`, `Position`, `Division`, `Active` setelah refresh dan hanya menampilkan kolom `Last Update`

### TC-FA-SU-562: Geser (drag reorder) Setup Column kelas Hideable

12. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
13. Untuk setiap baris tabel "Urutan drag Non-Login User" (langkah 13 sampai 14): drag kolom baris itu satu posisi sesuai kolom "Arah" baris itu
14. Verifikasi urutan Live Preview sama dengan kolom "Urutan kolom sesudah drag" baris itu
15. Klik `[Save]`
16. Verifikasi urutan kolom tabel sama dengan kolom "Urutan kolom sesudah drag" baris terakhir
17. Tekan F5
18. Verifikasi urutan kolom tabel tetap sama dengan baris terakhir tabel parameter setelah refresh

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso. Pemulihan preferensi kolom dilakukan hook `after` (Prerequisites).
- Urutan drag pada tabel parameter dipilih supaya tiap kolom bergeser tepat satu posisi pada gilirannya dan urutan akhir berbeda dari default; TC-FA-SU-562 hanya menyebut "satu posisi".
- Langkah berulang per baris tabel parameter: tabel "Urutan drag Non-Login User" pada langkah 13 sampai 14 (7 iterasi).
- Jumlah langkah: 18 tertulis, 30 dengan ekspansi iterasi.
- Temuan untuk QA:
  - TC-FA-SU-561 langkah 3 meminta mengubah centang ketujuh kolom sedangkan Expected h melarang meng-uncheck kolom terakhir yang visible; spec meng-uncheck enam kolom pertama dan mengasersi `Last Update` disabled dengan tooltip. Perubahan Live Preview, tabel, dan F5 kolom `Last Update` (Expected g) tidak dapat diasersi pada keadaan ini.
  - TC-FA-SU-562 tidak menyebut arah drag; arah per kolom ditetapkan di tabel parameter (S-15).
