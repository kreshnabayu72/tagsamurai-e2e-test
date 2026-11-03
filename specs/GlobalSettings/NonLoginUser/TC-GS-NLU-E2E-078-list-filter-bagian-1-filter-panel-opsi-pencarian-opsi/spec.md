---
id: TC-GS-NLU-E2E-078-list-filter-bagian-1-filter-panel-opsi-pencarian-opsi
title: "List Filter bagian 1: Filter Panel, isi opsi dropdown, pencarian di dalam dropdown, dan screening kontrol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-267
  - TC-GS-NLU-268
  - TC-GS-NLU-272
coverage:
  web: automated
---

# List Filter bagian 1: Filter Panel, isi opsi dropdown, pencarian di dalam dropdown, dan screening kontrol

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12; hanya dibaca, tidak diubah, tanpa suffix): Position yang dipakai baris tabel `Field Technician`, `Driver`, `Contractor` (Position master data lain, mis. `Warehouse Supervisor`, belum dipakai baris mana pun). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengamatan ikon Filter (gelap) dan placeholder field di Filter Panel.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-267: Screening Filter Panel

1. Klik icon Filter
2. Verifikasi Filter Panel terbuka di bawah toolbar
3. Verifikasi ikon Filter menjadi gelap
4. Verifikasi field berurutan: `Active` (placeholder `All statuses`), `Position` (`All positions`), `Division` (`All divisions`), `Represented By` (`All users`), `Last Update` date range (`Select date`)
5. Verifikasi tombol `[Clear Field]` (kiri) dan `[Apply]` (kanan)
6. Verifikasi field curated (Temporary User, Temporary Until, Custom Field `Filterable ✅`) sudah tersedia walau kolomnya belum diaktifkan

### TC-GS-NLU-268: Screening isi opsi dropdown Filter hanya nilai yang ada di tabel

7. Buka dropdown Position
8. Verifikasi opsi Position memuat `Field Technician`, `Driver`, `Contractor`
9. Verifikasi opsi Position tidak memuat seluruh master data (`Warehouse Supervisor` tidak ada)
10. Buka dropdown Division
11. Verifikasi opsi Division mengikuti nilai Division yang dipakai baris tabel
12. Buka dropdown Represented By
13. Verifikasi opsi Represented By mengikuti nama Login User yang dipakai baris tabel
14. Buka dropdown Active
15. Verifikasi opsi Active memuat `Active` dan `Inactive`

### TC-GS-NLU-272: Pencarian di dalam dropdown filter mempersempit opsi

16. Buka dropdown Position
17. Ketik `driv` pada kotak pencarian di dalam dropdown
18. Verifikasi daftar opsi menyempit ke yang mengandung `driv` (`Driver` tampil, `Field Technician` dan `Contractor` tidak; tidak membedakan huruf besar kecil)
19. Ganti isi kotak pencarian di dalam dropdown dengan `zzzxxx`
20. Verifikasi pencarian tak cocok menampilkan tanpa opsi
21. Klik ikon Filter untuk menutup Filter Panel

## Notes

- Langkah penghubung (S-03): langkah terakhir menutup Filter Panel tanpa Apply.
- Asersi tambahan (S-03): `Warehouse Supervisor` tidak ada di opsi Position (TC-GS-NLU-268) menerjemahkan "bukan seluruh master data" ke Position master data yang belum dipakai baris mana pun (Pre-setup No. 9; TC-GS-NLU-490 precondition d).
- Pembagian TC lintas spec: TC Filter lain ada di spec 079, 080, 081, 134.
- Temuan untuk QA:
  - TC-GS-NLU-268 Expected b tidak merinci opsi Division dan Represented By yang dipakai tabel; spec mengasersi bahwa opsi mengikuti nilai di tabel tanpa daftar tetap.
  - TC-GS-NLU-272 langkah hanya mengetik `driv`, tetapi Expected b ("pencarian tak cocok menampilkan tanpa opsi") butuh input tak cocok; spec menambah langkah mengetik `zzzxxx` dan tidak menyebut teks pesan karena TC tidak menyebutnya.
