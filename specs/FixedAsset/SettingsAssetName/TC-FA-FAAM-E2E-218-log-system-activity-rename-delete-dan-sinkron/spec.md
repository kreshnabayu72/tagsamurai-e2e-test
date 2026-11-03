---
id: TC-FA-FAAM-E2E-218-log-system-activity-rename-delete-dan-sinkron
title: "Log Multi-Surface: Name Sama, Tiga Surface Tersinkron, Delete, dan Bulk Delete"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-581
  - TC-FA-FAAM-582
  - TC-FA-FAAM-735
  - TC-FA-FAAM-736
coverage:
  web: automated
---

# Log Multi-Surface: Name Sama, Tiga Surface Tersinkron, Delete, dan Bulk Delete

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category `IT Equipment`), No. 23 (Brand `Dell`), No. 24 (UoM `Unit`).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-218`, Code literal Tabel Dinamis (batas panjang Code; hook `before` menghapus sisa Code yang sama dari run lama):
  - `Edit Target Item 581 {runId}-218` (Code `ETI581`) dan `Edit Target Item 582 {runId}-218` (Code `ETI582`): salinan fixture 13d (Tabel Dinamis No. 49, 50), Total Asset 0.
  - `Warehouse Pallet 735 {runId}-218` (Code `PLT-WH735`): salinan fixture 13 (Tabel Dinamis No. 99), Total Asset 0.
  - `Bulk Clean A 736 {runId}-218` dan `Bulk Clean B 736 {runId}-218`: salinan fixture 13c (Tabel Dinamis No. 102), Total Asset 0.
  - Nama hasil rename TC-FA-FAAM-581: `Name After {runId}-218` dengan Code `NAF`; Code hasil edit TC-FA-FAAM-582: `SYN1`.
- Kemampuan teknis: membuka Modal Changelog, Detail User aktor > tab System Log, dan Activity Log FAMS beserta Search di dalamnya. Ketiganya audit trail permanen sehingga entri dicari lewat Search atas nama bersuffix unik (baseline nol) dan total entri tidak diasersi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus sisa seed milik spec ini lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-581, 582, 735, 736: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### Pembukaan

1. Ketik Search `{runId}-218`, tekan Enter

### TC-FA-FAAM-581: Rename, Name sama untuk semua baris satu penyimpanan

2. Klik `⋯` baris `Edit Target Item 581 {runId}-218` lalu `Edit`
3. Ubah Asset Name menjadi `Name After {runId}-218`
4. Ubah Code menjadi `NAF`
5. Klik `[Save]`
6. Buka Detail User aktor lalu tab System Log
7. Ketik Search `Name After {runId}-218`, tekan Enter
8. Verifikasi kedua baris (Field `Asset Name` dan Field `Code`) memuat Name `Name After {runId}-218`
9. Verifikasi baris Field `Asset Name` Old `Edit Target Item 581 {runId}-218`, New `Name After {runId}-218`
10. Buka Activity Log FAMS
11. Ketik Search `Name After {runId}-218`, tekan Enter
12. Verifikasi kedua baris (Field `Asset Name` dan Field `Code`) memuat Name `Name After {runId}-218`
13. Verifikasi baris Field `Asset Name` Old `Edit Target Item 581 {runId}-218`, New `Name After {runId}-218`

### TC-FA-FAAM-582: Tiga surface log tersinkron untuk satu aksi

14. Buka Fixed Asset > Settings > Asset Master > Asset Name
15. Ketik Search `Edit Target Item 582 {runId}-218`, tekan Enter
16. Klik `⋯` baris `Edit Target Item 582 {runId}-218` lalu `Edit`
17. Ubah Code menjadi `SYN1`
18. Klik `[Save]`
19. Klik icon Changelog
20. Ketik Search `Edit Target Item 582 {runId}-218`, tekan Enter
21. Verifikasi Changelog memuat satu entri Edit Field `Code`, Old `ETI582`, New `SYN1`
22. Tutup Modal Changelog
23. Buka Detail User aktor lalu tab System Log
24. Ketik Search `Edit Target Item 582 {runId}-218`, tekan Enter
25. Verifikasi System Log memuat satu entri Edit Field `Code`, Old `ETI582`, New `SYN1`
26. Buka Activity Log FAMS
27. Ketik Search `Edit Target Item 582 {runId}-218`, tekan Enter
28. Verifikasi Activity Log FAMS memuat satu entri Edit Field `Code`, Old `ETI582`, New `SYN1`
29. Verifikasi Date entri pada Changelog, System Log, dan Activity Log FAMS sama

### TC-FA-FAAM-735: Delete menulis satu baris Delete di System Log aktor dan Activity Log FAMS

30. Buka Fixed Asset > Settings > Asset Master > Asset Name
31. Ketik Search `Warehouse Pallet 735 {runId}-218`, tekan Enter
32. Klik `⋯` baris `Warehouse Pallet 735 {runId}-218` lalu `Delete`
33. Klik `[Delete]`
34. Buka Detail User aktor lalu tab System Log
35. Ketik Search `Warehouse Pallet 735 {runId}-218`, tekan Enter
36. Verifikasi satu baris Action `Delete`, Object `Asset Name`, Name `Warehouse Pallet 735 {runId}-218` (nama yang dihapus), Field `Asset Name`, Old `Warehouse Pallet 735 {runId}-218`, New `—`
37. Buka Activity Log FAMS
38. Ketik Search `Warehouse Pallet 735 {runId}-218`, tekan Enter
39. Verifikasi baris Delete yang sama dengan Modified By `[First Name] [Last Initial]` aktor

### TC-FA-FAAM-736: Bulk Delete menulis satu baris Delete per item

40. Buka Fixed Asset > Settings > Asset Master > Asset Name
41. Ketik Search `736 {runId}-218`, tekan Enter
42. Centang `Bulk Clean A 736 {runId}-218` dan `Bulk Clean B 736 {runId}-218`
43. Klik `Bulk Action` lalu `Delete`
44. Klik `[Delete]`
45. Buka Detail User aktor lalu tab System Log
46. Ketik Search `736 {runId}-218`, tekan Enter
47. Verifikasi dua baris Action `Delete`, Object `Asset Name`, Field `Asset Name`, Name dan Old Value `Bulk Clean A 736 {runId}-218` serta `Bulk Clean B 736 {runId}-218`, New `—`
48. Verifikasi pada System Log hanya ada dua baris untuk pencarian `736 {runId}-218` (tidak ada baris untuk item selain keduanya)
49. Buka Activity Log FAMS
50. Ketik Search `736 {runId}-218`, tekan Enter
51. Verifikasi dua baris Delete yang sama dengan Modified By aktor
52. Verifikasi pada Activity Log hanya ada dua baris untuk pencarian `736 {runId}-218`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 15, 31, 41 (Search tabel utama), langkah 7, 11, 20, 24, 27, 35, 38, 46, 50 (Search nama bersuffix pada audit trail permanen; S-12, S-14), langkah 6, 10, 14, 19, 23, 26, 30, 34, 37, 40, 45, 49 (navigasi antar surface), dan langkah 22 (menutup Modal Changelog).
- Di atas smell 35 langkah. Spec berisi 52 langkah. Alasan di atas ~35: sebagian besar adalah blok baca-log berpola (buka surface, cari entri, Verifikasi kolom log) yang tidak dihitung menurut bagian 3 konvensi; langkah di luar blok itu sekitar 17. Keempat TC berdiri sendiri dengan seed sendiri dan satu kelas harness.
- Tidak ada pelaku kedua; Total Control satu sesi.
- Temuan untuk QA:
  - TC-FA-FAAM-735 dan 736 meminta "entri acuan" teratas; pada audit trail permanen spec memakai Search atas nama bersuffix unik (baseline nol) sebagai pengganti, sesuai S-12.
  - TC-FA-FAAM-582 menyebut "Date sama" tanpa toleransi; kolom Date log berketelitian menit.
  - TC-FA-FAAM-736 butir c ("tidak ada baris untuk item selain keduanya") diasersi sebagai jumlah baris hasil Search `736 {runId}-218`, bukan absence.
