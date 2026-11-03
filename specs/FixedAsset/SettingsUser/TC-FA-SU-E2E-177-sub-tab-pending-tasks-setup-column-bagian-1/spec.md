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

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

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

### TC-FA-SU-527: Geser (drag reorder) Setup Column kelas Hideable

12. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
13. Untuk setiap baris tabel "Urutan drag Pending Tasks" (langkah 13 sampai 14): drag kolom baris itu satu posisi sesuai kolom "Arah" baris itu
14. Verifikasi urutan Live Preview sama dengan kolom "Urutan kolom sesudah drag" baris itu
15. Klik `[Save]`
16. Verifikasi urutan kolom tabel sama dengan kolom "Urutan kolom sesudah drag" baris terakhir
17. Tekan F5
18. Verifikasi urutan kolom tabel tetap sama dengan baris terakhir tabel parameter setelah refresh

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso. Pemulihan preferensi kolom dilakukan hook `after` (Prerequisites).
- Urutan drag pada tabel parameter dipilih supaya tiap kolom bergeser tepat satu posisi pada gilirannya dan urutan akhir berbeda dari default; TC-FA-SU-527 hanya menyebut "satu posisi".
- Langkah berulang per baris tabel parameter: tabel "Urutan drag Pending Tasks" pada langkah 13 sampai 14 (8 iterasi).
- Jumlah langkah: 18 tertulis, 32 dengan ekspansi iterasi.
- Temuan untuk QA:
  - TC-FA-SU-526 langkah 3 meminta mengubah centang kedelapan kolom sedangkan Expected i melarang meng-uncheck kolom terakhir yang visible; spec meng-uncheck tujuh kolom pertama dan mengasersi `Last Updated` (kolom terakhir) disabled dengan tooltip. Perubahan Live Preview, tabel, dan F5 kolom `Last Updated` (Expected h) tidak dapat diasersi pada keadaan ini.
  - TC-FA-SU-527 tidak menyebut arah drag; arah per kolom ditetapkan di tabel parameter (S-15).
  - TC-FA-SU-527 Expected a sampai h menulis "urutan Live Preview dan tabel berubah" tanpa menyebut urutan hasil; spec mengasersi urutan hasil drag kumulatif dari tabel parameter.
