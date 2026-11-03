---
id: TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search
title: "Sub-tab Pending Tasks: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-502
  - TC-FA-SU-503
  - TC-FA-SU-504
  - TC-FA-SU-505
  - TC-FA-SU-506
  - TC-FA-SU-507
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Responsibilities (#25): pengguna target Budi Santoso dengan 5 baris Sub-tab Pending Tasks (`BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`). Nilai kolom tiap baris mengikuti Pre-setup #25; asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11).
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Request Date ascending): `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`.
- Tabel parameter "Ikon Table Tools":

| Ikon | Tooltip |
|---|---|
| `Search` | `Search` |
| `Filter` | `Filter` |
| `Download` | `Download` |
- Tabel parameter "Search kelas teks dan badge":

| Kolom | Keyword | Hasil |
|---|---|---|
| Transaction ID | `ASG-2026` | `ASG-20260715-0045`, `ASG-20260718-0067` (2 baris) |
| Transaction | `Assignment` | `ASG-20260715-0045`, `ASG-20260718-0067` (2 baris) |

## Test Steps

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Pending Tasks

### TC-FA-SU-502: Screening Table Tools, kolom, dan default sort

2. Verifikasi header menampilkan Table Tools `Search`, `Filter`, `Download` rata kanan
3. Untuk setiap baris tabel "Ikon Table Tools" (langkah 3 sampai 4): hover ikon baris itu
4. Verifikasi tooltip sama dengan kolom "Tooltip" baris itu
5. Klik icon Search
6. Verifikasi placeholder Search `Search transaction ID, status, or group...`
7. Klik `←` pada kotak Search
8. Verifikasi kolom `Transaction ID (sortable)`, `Transaction (sortable)`, `Status (sortable)`, `Group (sortable)`, `PIC (sortable)`, `Total Asset (sortable)`, `Request Date (sortable)`, `Last Updated (sortable)`, dan `Column Visibility (⋯)`
9. Verifikasi sel kolom Column Visibility (⋯) pada tiap baris kosong tanpa row action
10. Klik header kolom Column Visibility (⋯)
11. Verifikasi overlay Column Visibility terbuka
12. Tekan Esc untuk menutup overlay Column Visibility
13. Verifikasi default sort Request Date ascending: `BRW-20260712-0346`, `BRW-20260713-0355`, `ASG-20260715-0045`, `BRW-20260716-0372`, `ASG-20260718-0067`
14. Klik dropdown page size
15. Verifikasi footer pagination 10 data per halaman dengan page size 10, 25, 50, 100
16. Tekan Esc untuk menutup pilihan page size

### TC-FA-SU-503: Search kelas teks dan badge

17. Untuk setiap baris tabel "Search kelas teks dan badge" (langkah 17 sampai 19): ketik Search keyword baris itu, tekan Enter
18. Verifikasi tabel menyisakan baris sesuai kolom "Hasil" baris itu
19. Klik `←` pada kotak Search

### TC-FA-SU-504: Search kelas enum (Status)

20. Ketik Search `Acceptance`, tekan Enter
21. Verifikasi keyword `Acceptance` menyisakan `ASG-20260715-0045`, `ASG-20260718-0067` (2 baris)
22. Klik `←` pada kotak Search

### TC-FA-SU-505: Search kelas badge (Group)

23. Ketik Search `Warehouse`, tekan Enter
24. Verifikasi keyword `Warehouse` menyisakan `BRW-20260716-0372` (1 baris)
25. Klik `←` pada kotak Search

### TC-FA-SU-506: Search kelas user (PIC)

26. Ketik Search `Santoso`, tekan Enter
27. Verifikasi keyword `Santoso` menyisakan `BRW-20260716-0372` (1 baris)
28. Klik `←` pada kotak Search

### TC-FA-SU-507: Search kelas num (Total Asset) dengan kolom Transaction ID disembunyikan

29. Klik header kolom Actions (⋯), lalu hilangkan centang Transaction ID
30. Ketik Search `3`, tekan Enter
31. Verifikasi dengan kolom Transaction ID disembunyikan, keyword `3` menyisakan satu baris Group `Logistics Warehouse` (Transaction ID `BRW-20260716-0372`, satu-satunya baris dengan Total Asset 3)
32. Klik `←` pada kotak Search
33. Klik header kolom Actions (⋯), lalu centang kembali Transaction ID

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Detail Budi Santoso, menutup kotak Search dengan `←` (S-09), dan memulihkan kolom Transaction ID (S-09).
- Langkah penghubung tambahan (S-03): klik header kolom Column Visibility (⋯) (langkah 10) dan `Esc` (langkah 12) memicu dan menutup overlay untuk `Verifikasi` overlay (TC-FA-SU-502 Expected b); klik dropdown page size (langkah 14) dan `Esc` (langkah 16) membuka dan menutup pilihan page size untuk `Verifikasi` pilihan page size (Expected d, S-14).
- Langkah berulang per baris tabel parameter: tabel "Ikon Table Tools" pada langkah 3 sampai 4 (3 iterasi); tabel "Search kelas teks dan badge" pada langkah 17 sampai 19 (2 iterasi).
- Jumlah langkah: 33 tertulis, 40 dengan ekspansi iterasi.
