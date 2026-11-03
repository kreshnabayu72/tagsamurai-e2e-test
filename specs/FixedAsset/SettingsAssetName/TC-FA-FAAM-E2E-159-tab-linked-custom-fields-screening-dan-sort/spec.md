---
id: TC-FA-FAAM-E2E-159-tab-linked-custom-fields-screening-dan-sort
title: "Tab Linked Custom Fields: Screening dan Sort Kelas Field Name, Data Type, Global Value"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-546
  - TC-FA-FAAM-547
  - TC-FA-FAAM-548
  - TC-FA-FAAM-549
coverage:
  web: automated
---

# Tab Linked Custom Fields: Screening dan Sort Kelas Field Name, Data Type, Global Value

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`): `Dell Latitude` (Pre-setup #10) dengan custom field berscope (Pre-setup #27): `Cost Center` (Dropdown, Global `Finance`), `Operating System` (Dropdown, Specific), dan `Warranty Notes` (Text, Global kosong), sehingga label tab `Linked Custom Fields (3)`. Data memiliki dua nilai distinct pada kolom Field Name, Data Type, dan Global Value (S-11). Spec ini hanya membuka Popup Detail dan tidak mengubah data (S-06).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik nama `Dell Latitude`
3. Klik tab `Linked Custom Fields (3)`

### TC-FA-FAAM-546: Screening Tab Linked Custom Fields

4. Verifikasi tabel `Field Name | Data Type | Global Value` tampil
5. Verifikasi tabel Linked Custom Fields tanpa toolbar dan tanpa paginasi
6. Verifikasi default sort Field Name A-Z
7. Verifikasi Global Value Dropdown berupa badge `Finance`
8. Verifikasi Global Value Specific tampil `(per-asset)`
9. Verifikasi Global Value kosong tampil `—`
10. Verifikasi tautan `Open in Custom Fields ↗` tampil

### TC-FA-FAAM-547: Sort Tab Linked Custom Fields kelas Field Name

11. Klik header Field Name
12. Verifikasi Klik 1: A-Z tanpa membedakan huruf besar-kecil
13. Klik header Field Name
14. Verifikasi Klik 2: Z-A
15. Klik header Field Name
16. Verifikasi Klik 3: netral kembali Field Name A-Z

### TC-FA-FAAM-548: Sort Tab Linked Custom Fields kelas Data Type

17. Klik header Data Type
18. Verifikasi Klik 1: A-Z
19. Klik header Data Type
20. Verifikasi Klik 2: Z-A
21. Klik header Data Type
22. Verifikasi Klik 3: netral kembali Field Name A-Z

### TC-FA-FAAM-549: Sort Tab Linked Custom Fields kelas Global Value (kolom campuran)

23. Klik header Global Value
24. Verifikasi Klik 1: nilai teks A-Z dengan `(per-asset)` diperlakukan sebagai teks, dan `—` di akhir
25. Klik header Global Value
26. Verifikasi Klik 2: kebalikan penuh, `—` di awal
27. Klik header Global Value
28. Verifikasi Klik 3: netral kembali Field Name A-Z

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, R-16).
- Asersi tanpa toolbar dan paginasi (langkah 5) beranchor tabel yang tampil (langkah 4).
- Temuan untuk QA:
  - TC-FA-FAAM-549 Expected a menyebut urutan numerik naik lebih dulu dan multi-nilai menurut nilai pertama; data Pre-setup #27 tidak memuat nilai numerik maupun multi-nilai, sehingga klausa itu tidak dapat diasersi dengan data ini. Spec hanya mengasersi urutan teks dan posisi `—`.
  - TC-FA-FAAM-549 tidak menyebut apakah `(per-asset)` berada sebelum atau sesudah `Finance`; spec tidak mengasersi urutan keduanya.
