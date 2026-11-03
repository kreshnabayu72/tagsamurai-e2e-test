---
id: TC-FA-RP-E2E-139-tab-total-control-filter-1
title: "Tab Total Control: Filter (1/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-480
  - TC-FA-RP-481
  - TC-FA-RP-482
coverage:
  web: automated
---

# Tab Total Control: Filter (1/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris dengan Position, Division, Status, Activation Status, Modified By, Temporary User, Temporary Until, Cost Center, dan Joined Date), #37 (Tab Read Only empat baris), #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`. Rentang tanggal Last Updated dibentuk dari waktu Last Updated baris Fitri Handayani dan Rudi Hartono hasil seeding (kemampuan membaca waktu disediakan tim FE/BE) dan mencakup keduanya saja.
- Tabel Filter multi-select (TC 481):

| Field | Opsi | Baris yang tampil |
|---|---|---|
| Position | `Finance Officer` | Siti Rahmawati dan Fitri Handayani |
| Division | `Logistics` | Ahmad Fauzi dan Budi Santoso |
| Status | `Inactive` | hanya Siti Rahayu |
| Modified By | `Prasetyo Hadi` | Budi Santoso dan Fitri Handayani |
| Activation Status | `Pending Activation` | hanya Eka Saputra |
| Temporary User | `Yes` | hanya Rudi Hartono |
| Cost Center | `CC-100` | hanya Ahmad Fauzi |

- Tabel Filter date range (TC 482):

| Field | Rentang | Baris yang tampil |
|---|---|---|
| Last Updated | mencakup waktu Last Updated Fitri Handayani dan Rudi Hartono saja | Fitri Handayani dan Rudi Hartono |
| Temporary Until | mencakup tanggal Temporary Until Rudi Hartono | hanya Rudi Hartono |
| Joined Date | mencakup Joined Date Ahmad Fauzi (10/01/26) | hanya Ahmad Fauzi |

## Test Steps

### Screening Filter Panel (TC 480)

1. Klik ikon Filter.
2. Verifikasi Panel Filter muncul di bawah toolbar dengan field berurutan: `Position` (multi-select searchable, placeholder `All positions`), `Division` (multi-select searchable, `All divisions`), `Status` (multi-select searchable, `All statuses`), `Modified By` (multi-select searchable, `All users`), `Last Updated` (date range picker, `Select date`).
3. Verifikasi field kolom curated tersedia walau kolom disembunyikan: `Activation Status` (multi-select searchable, `All statuses`), `Temporary User` (multi-select searchable, `All options`), `Temporary Until` (date range picker, `Select date`), `Cost Center` (multi-select searchable), dan `Joined Date` (date range picker, `Select date`).
4. Verifikasi `Badge No` dan `Name` tidak punya field filter.
5. Verifikasi footer panel memuat `[Clear Field]` dan `[Apply]`.

### Filter per kelas multi-select searchable (TC 481)

6. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
7. Untuk setiap baris Tabel Filter multi-select, lakukan langkah 8 sampai 11.
8. Pilih opsi pada field sesuai tabel.
9. Klik `[Apply]`.
10. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel.
11. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Filter per kelas date range (TC 482)

12. Untuk setiap baris Tabel Filter date range, lakukan langkah 13 sampai 16.
13. Pilih rentang tanggal pada field sesuai tabel.
14. Klik `[Apply]`.
15. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel (field Last Updated: hanya baris dengan Last Updated di dalam rentang).
16. Klik `[Clear Field]`, lalu klik `[Apply]`.

## Notes

- Alasan di atas 35 langkah: langkah 8 sampai 11 (tujuh iterasi) dan langkah 13 sampai 16 (tiga iterasi) adalah blok berulang dengan parameter pada tabel Prerequisites; seluruh blok berkelas fungsional sama dan berdiri sendiri karena `[Clear Field]` dan `[Apply]` mengembalikan tabel ke keadaan penuh di akhir tiap iterasi. Langkah yang diulang: 8 sampai 11 dan 13 sampai 16.
- Langkah penghubung (S-03): langkah 1, 7, 8, 9, 11, 12, 13, 14, dan 16. Langkah 6 adalah pembanding positif untuk asersi universal langkah 10 dan 15 (8b butir 2). Langkah 4 adalah asersi absence field dengan anchor panel yang termuat (langkah 2 dan 3).
- Temuan untuk QA:
  - TC 482 menulis Data Uji rentang secara deskriptif ("rentang yang mencakup waktu Assign Fitri Handayani dan Rudi Hartono saja"); spec membentuk rentang dari waktu seeding, dan nilai tanggal eksak belum tertulis di Pre-setup #36.
