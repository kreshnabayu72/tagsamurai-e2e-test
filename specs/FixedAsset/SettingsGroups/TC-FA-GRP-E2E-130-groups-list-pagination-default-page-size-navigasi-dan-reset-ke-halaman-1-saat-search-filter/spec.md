---
id: TC-FA-GRP-E2E-130-groups-list-pagination-default-page-size-navigasi-dan-reset-ke-halaman-1-saat-search-filter
title: "Groups List Pagination: Default dan Page Size, Navigasi Prev/Next dan Input Halaman, serta Reset ke Halaman 1 Saat Search/Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-416
  - TC-FA-GRP-417
  - TC-FA-GRP-1023
  - TC-FA-GRP-1024
coverage:
  web: automated
---

# Groups List Pagination: Default dan Page Size, Navigasi Prev/Next dan Input Halaman, serta Reset ke Halaman 1 Saat Search/Filter

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-130`, bagian 5), dibuat lewat API di `before` oleh akun aktor: group `Page Parent {runId}-130` (level 1, Function None) dengan 27 child Function None `Child 01 {runId}-130` sampai `Child 27 {runId}-130`. Dipakai sebagai pengganti Head Office (>= 11 child) dan tampilan >= 26 baris pada TC; tampil 10 baris per halaman: halaman 1 = Child 01 sampai Child 10, halaman 2 = Child 11 sampai Child 20, halaman 3 = Child 21 sampai Child 27.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Page Parent {runId}-130` beserta seluruh child.

## Test Steps

### TC-FA-GRP-416: Default dan pilihan page size

1. Klik `Page Parent {runId}-130` di sidebar Group Tree
2. Verifikasi footer pagination tampil
3. Verifikasi default 10 baris per halaman
4. Buka dropdown page size
5. Verifikasi pilihan page size 10, 25, 50, dan 100
6. Pilih page size 25
7. Verifikasi tabel menampilkan 25 baris
8. Pilih page size 50
9. Verifikasi tabel menampilkan 27 baris
10. Pilih page size 100
11. Verifikasi tabel menampilkan 27 baris
12. Pilih page size 10
13. Verifikasi tabel menampilkan 10 baris

### TC-FA-GRP-417: Navigasi prev/next dan input nomor halaman

14. Klik tombol next
15. Verifikasi tabel menampilkan halaman 2: baris pertama `Child 11 {runId}-130`
16. Klik tombol prev
17. Verifikasi tabel menampilkan halaman 1: baris pertama `Child 01 {runId}-130`
18. Ketik nomor halaman `3` pada input halaman, tekan Enter
19. Verifikasi tabel menampilkan halaman 3: baris pertama `Child 21 {runId}-130`

### TC-FA-GRP-1023: Search dari halaman 2 mereset ke halaman 1

20. Pindah ke halaman 2 lewat pagination
21. Klik icon Search
22. Ketik Search `Child`, tekan Enter
23. Verifikasi tabel menampilkan halaman 1 dari hasil search (baris pertama `Child 01 {runId}-130`), bukan halaman 2
24. Pindah ke halaman 2 lewat pagination
25. Klik `✕` pada kotak Search
26. Tekan Enter
27. Verifikasi tabel menampilkan seluruh data pada halaman 1 (baris pertama `Child 01 {runId}-130`), bukan halaman 2
28. Klik `(←)` pada kotak Search

### TC-FA-GRP-1024: Apply Filter dari halaman 2 mereset ke halaman 1

29. Pindah ke halaman 2 lewat pagination
30. Klik icon Filter
31. Pilih `None` pada dropdown Function
32. Klik [Apply]
33. Verifikasi tabel menampilkan halaman 1 dari hasil filter (baris pertama `Child 01 {runId}-130`), bukan halaman 2
34. Pindah ke halaman 2 lewat pagination
35. Klik icon Filter
36. Klik [Clear Field]
37. Klik [Apply]
38. Verifikasi tabel menampilkan seluruh data pada halaman 1 (baris pertama `Child 01 {runId}-130`), bukan halaman 2

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka node `Page Parent` di sidebar, berpindah halaman, serta `(←)` pada kotak Search di antara TC (S-03, S-09).
- Seluruh TC memakai `Page Parent` milik spec (27 child) sebagai pengganti Head Office dan tampilan >= 26 baris pada TC, supaya data Pre-setup tidak diubah (S-06).
- Halaman aktif diamati lewat baris pertama halaman (`Child 01`, `Child 11`, `Child 21`).
- Spec 38 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" dan "Head Office >= 11 child" pada TC-FA-GRP-1023/1024 memakai Pre-setup; spec memakai `Page Parent` milik spec dengan 27 child Function None (memenuhi syarat >= 11 child dan tampilan >= 26 baris).
  - Password akun aktor memakai env baru `FA_TC_PASSWORD`; perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Cara mengamati nomor halaman aktif tidak ditentukan TC; spec memakai baris pertama halaman.
