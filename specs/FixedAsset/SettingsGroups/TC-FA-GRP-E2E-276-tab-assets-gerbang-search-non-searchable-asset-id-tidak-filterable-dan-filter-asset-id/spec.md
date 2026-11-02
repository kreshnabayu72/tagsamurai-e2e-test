---
id: TC-FA-GRP-E2E-276-tab-assets-gerbang-search-non-searchable-asset-id-tidak-filterable-dan-filter-asset-id
title: "Tab Assets: Kolom Non-Searchable Warranty Expiry dan Last Scanned Tidak Match, Asset ID Tidak Filterable, dan Filter Asset Name Satu/Dua Opsi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1248
  - TC-FA-GRP-1263
  - TC-FA-GRP-1264
coverage:
  web: automated
---

# Tab Assets: Kolom Non-Searchable Warranty Expiry dan Last Scanned Tidak Match, Asset ID Tidak Filterable, dan Filter Asset Name Satu/Dua Opsi

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor pertama: allValueAccess (Pre-setup No 17: Group Role Manage purchase pada Value Gate Node A, Global Role Manage accounting, lisensi FA-7 aktif) `allValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit, untuk TC-1263 dan TC-1264): Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Data Pre-setup tambahan (hanya dibaca): Value Gate Node A (Tabel Dinamis No 10, aset G1-G6) dengan audit scan (No 15: pemindaian terbaru G3 01/09/2026, G1 10/10/2026, G5 20/10/2026). Node di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-276` (mekanisme seeding disediakan tim FE/BE). Langkah dan asersi memakai nama bersuffix itu. Warranty Expiry G1 15/03/2027. Asset ID G1 dibaca dari tabel; data filter Asset Name: Laptop Dell (G1 dan G6: Laptop Dell - 1, Laptop Dell - 2) dan Forklift Toyota (G4); potongan Asset ID G1 untuk Search diketik dengan kapitalisasi berbeda dari aslinya (case-insensitive) dan hanya cocok dengan baris G1.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (kondisi awal client uji; spec tidak mengubahnya).
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah.

## Test Steps

### TC-1248: Search kolom non-searchable Warranty Expiry dan Last Scanned tidak menghasilkan match
1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column, centang kolom Warranty Expiry dan Last Scanned, klik [Save]
3. Ketik Search `15/03/2027`, tekan Enter
4. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
5. Ganti isi kotak search dengan `10/10/2026`, tekan Enter
6. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
7. Klik icon Filter
8. Verifikasi Filter Panel memuat field Warranty Expiry dan Last Scanned
9. Tutup Filter Panel; klik `(←)` pada kotak Search
### TC-1263: Screening kolom Asset ID Tab Assets tidak Filterable (Asset ID unik)
10. Ganti akun: Logout, login sebagai Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`), buka Fixed Asset > Settings > Groups
11. Buka Detail Value Gate Node A (Tab Assets)
12. Klik icon Filter
13. Amati daftar field
14. Verifikasi Filter Panel memuat field lain (Status)
15. Verifikasi Filter Panel tidak memuat field `Asset ID`
16. Tutup Filter Panel; ketik Search potongan Asset ID G1 (kapitalisasi berbeda dari aslinya), tekan Enter
17. Verifikasi baris G1 tampil
18. Verifikasi baris lain tidak tampil
19. Klik `(←)` pada kotak Search
### TC-1264: Filter Tab Assets by Asset Name: satu opsi dan dua opsi (logika OR)
20. Klik icon Filter; pada field Asset Name pilih Laptop Dell, klik [Apply]
21. Verifikasi hanya G1 dan G6 (Laptop Dell - 1, Laptop Dell - 2) tampil
22. Verifikasi indikator filter aktif tampil pada icon Filter
23. Verifikasi Filter Panel tertutup setelah [Apply]
24. Klik icon Filter, klik [Clear Field]; pilih Asset Name Laptop Dell dan Forklift Toyota, klik [Apply]
25. Verifikasi G1, G6, dan G4 tampil (OR di dalam field)
26. Verifikasi G2, G3, dan G5 tidak tampil
27. Klik icon Filter, klik [Clear Field]

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Tutup Filter Panel; klik `(←)` pada kotak Search" di akhir TC-1248 dan TC-1263; satu langkah Ganti akun sebelum TC-1263 (aktor berbeda); [Clear Field] terakhir TC-1264 (langkah 27).
- Asersi tambahan (S-03): `Verifikasi` Filter Panel memuat field Warranty Expiry dan Last Scanned pada TC-1248 menerjemahkan Expected b "hanya tersedia lewat Filter Panel", yang tidak punya langkah observasi di TC; `Verifikasi` field lain (Status) pada TC-1263 adalah anchor positif untuk absence field `Asset ID`.
- Temuan untuk QA:
  - TC-1263 Langkah 5 tidak menyebut potongan Asset ID konkret; spec memakai potongan Asset ID G1.
