---
id: TC-FA-SU-E2E-177-sub-tab-pending-tasks-setup-column-bagian-1
title: "Sub-tab Pending Tasks: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-526
  - TC-FA-SU-527
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec menyimpan konfigurasi kolom lewat `[Save]` pada Setup Column. Hook `after` menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi); tidak ada data backend yang berubah. Perubahan Column Visibility dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.
- Kolom `Last Updated` tersisa sebagai satu-satunya kolom visible pada akhir langkah uncheck TC-FA-SU-526.
- Tabel parameter "Urutan drag Pending Tasks" (urutan awal: `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`, `Last Updated`):

| No | Kolom yang di-drag | Arah (satu posisi) | Urutan kolom sesudah drag |
|---|---|---|---|
| 1 | `Last Updated` | atas | `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Last Updated`, `Request Date` |
| 2 | `Total Asset` | bawah | `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Last Updated`, `Total Asset`, `Request Date` |
| 3 | `Request Date` | atas | `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Last Updated`, `Request Date`, `Total Asset` |
| 4 | `PIC` | bawah | `Transaction ID`, `Transaction`, `Status`, `Group`, `Last Updated`, `PIC`, `Request Date`, `Total Asset` |
| 5 | `Group` | bawah | `Transaction ID`, `Transaction`, `Status`, `Last Updated`, `Group`, `PIC`, `Request Date`, `Total Asset` |
| 6 | `Status` | bawah | `Transaction ID`, `Transaction`, `Last Updated`, `Status`, `Group`, `PIC`, `Request Date`, `Total Asset` |
| 7 | `Transaction` | bawah | `Transaction ID`, `Last Updated`, `Transaction`, `Status`, `Group`, `PIC`, `Request Date`, `Total Asset` |
| 8 | `Transaction ID` | bawah | `Last Updated`, `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Request Date`, `Total Asset` |

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-526: Ceklis dan unceklis Setup Column kelas Hideable

2. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
3. Hilangkan centang kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date` pada daftar Setup Column (satu per satu)
4. Verifikasi Live Preview tidak lagi menampilkan kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date`
5. Hover checkbox kolom Last Updated
6. Verifikasi checkbox kolom Last Updated disabled sebagai satu-satunya kolom visible
7. Verifikasi tooltip `At least one column must remain visible.`
8. Klik `[Save]`
9. Verifikasi tabel tidak menampilkan kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date` dan hanya menampilkan kolom `Last Updated`
10. Tekan F5
11. Verifikasi tabel tetap tidak menampilkan kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date` setelah refresh dan hanya menampilkan kolom `Last Updated`
12. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
13. Centang kembali kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`, `Total Asset`, `Request Date` pada daftar Setup Column (satu per satu)
14. Klik `[Save]`

### TC-FA-SU-527: Geser (drag reorder) Setup Column kelas Hideable

15. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
16. Untuk setiap baris tabel "Urutan drag Pending Tasks" (langkah 16 sampai 17): drag kolom baris itu satu posisi sesuai kolom "Arah" baris itu
17. Verifikasi urutan Live Preview sama dengan kolom "Urutan kolom sesudah drag" baris itu
18. Klik `[Save]`
19. Verifikasi urutan kolom tabel sama dengan kolom "Urutan kolom sesudah drag" baris terakhir
20. Tekan F5
21. Verifikasi urutan kolom tabel tetap sama dengan baris terakhir tabel parameter setelah refresh
22. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
23. Klik `[Reset to Default]`
24. Klik `[Save]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` (Enter) lalu membuka Detail Budi Santoso, karena User List memuat lebih dari satu halaman (R-16, 8b butir 13). Pemulihan konfigurasi kolom: centang kembali tujuh kolom dan `[Save]` (langkah 12 sampai 14) sebelum TC-FA-SU-527, `[Reset to Default]` dan `[Save]` (langkah 22 sampai 24) di akhir (S-09, 8b butir 14); hook `after` hanya cadangan (Prerequisites).
- Urutan drag pada tabel parameter dipilih supaya tiap kolom bergeser tepat satu posisi pada gilirannya dan urutan akhir berbeda dari default; TC-FA-SU-527 hanya menyebut "satu posisi".
- Langkah berulang per baris tabel parameter: tabel "Urutan drag Pending Tasks" pada langkah 16 sampai 17 (8 iterasi).
- Jumlah langkah: 24 tertulis, 38 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (24 tertulis, 38 ekspansi). Seluruh blok berada pada satu surface (satu sub-tab atau tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian angka di atas ambang berasal dari ekspansi iterasi tabel parameter (8b butir 7); di atas smell 35 langkah.
- Temuan untuk QA:
  - TC-FA-SU-526 langkah 3 meminta mengubah centang kedelapan kolom sedangkan Expected i melarang meng-uncheck kolom terakhir yang visible; spec meng-uncheck tujuh kolom pertama dan mengasersi `Last Updated` (kolom terakhir) disabled dengan tooltip. Perubahan Live Preview, tabel, dan F5 kolom `Last Updated` (Expected h) tidak dapat diasersi pada keadaan ini.
  - TC-FA-SU-527 tidak menyebut arah drag; arah per kolom ditetapkan di tabel parameter (S-15).
  - TC-FA-SU-527 Expected a sampai h menulis "urutan Live Preview dan tabel berubah" tanpa menyebut urutan hasil; spec mengasersi urutan hasil drag kumulatif dari tabel parameter.
