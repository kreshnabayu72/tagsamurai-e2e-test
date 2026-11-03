---
id: TC-FA-SU-E2E-160-sub-tab-pending-approvals-screening-dan-search
title: "Sub-tab Pending Approvals: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-471
  - TC-FA-SU-472
  - TC-FA-SU-473
  - TC-FA-SU-474
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#25): Detail Budi Santoso dengan Sub-tab Pending Approvals 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #25 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC:

| Transaction ID | Transaction | Requester | Submission Date |
|---|---|---|---|
| `BRW-20260712-0341` | `Borrow` | `Ahmad D` | 12/07/26 |
| `TRF-20260714-0088` | `Transfer` | `Citra L` (Citra Lestari) | 14/07/26 |
| `DSP-20260715-0022` | `Disposal` | `Eka W` | 15/07/26 |
| `ASG-20260716-0015` | `Assignment` | `Budi S` | 16/07/26 |
| `BRW-20260718-0007` | `Borrow` | `Citra L` (Citra Lestari) | 18/07/26 |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-471: Screening Sub-tab Pending Approvals: Table Tools, kolom, dan default sort

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil
4. Verifikasi Table Tools rata kanan
5. Hover icon Search
6. Verifikasi tooltip `Search` tampil
7. Hover icon Filter
8. Verifikasi tooltip `Filter` tampil
9. Hover icon Download
10. Verifikasi tooltip `Download` tampil
11. Klik icon Search
12. Verifikasi placeholder Search `Search transaction ID, transaction, or requester...`
13. Klik `(←)` pada kotak Search
14. Verifikasi header kolom `Transaction ID (sortable)`, `Transaction (sortable)`, `Requester (sortable)`, `Submission Date (sortable)`, dan `Column Visibility (⋯)`
15. Verifikasi body tiap baris pada kolom Column Visibility (⋯) kosong tanpa row action
16. Klik header kolom Column Visibility (⋯)
17. Verifikasi overlay Column Visibility terbuka
18. Tekan Esc untuk menutup overlay Column Visibility
19. Verifikasi default sort Submission Date ascending: `BRW-20260712-0341`, `TRF-20260714-0088`, `DSP-20260715-0022`, `ASG-20260716-0015`, `BRW-20260718-0007`
20. Verifikasi footer pagination menampilkan 10 data per halaman
21. Klik dropdown page size
22. Verifikasi pilihan page size `10`, `25`, `50`, dan `100`
23. Tekan Esc untuk menutup pilihan page size

### TC-FA-SU-472: Search kelas teks dan badge: Transaction ID, Transaction

24. Ketik Search `TRF-2026`, tekan Enter
25. Verifikasi keyword `TRF-2026` menyisakan `TRF-20260714-0088` (1 baris)
26. Kosongkan isi kotak search, tekan Enter
27. Ketik Search `Disposal`, tekan Enter
28. Verifikasi keyword `Disposal` menyisakan `DSP-20260715-0022` (1 baris)
29. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-473: Search kelas user: Requester

30. Ketik Search `Lestari`, tekan Enter
31. Verifikasi keyword `Lestari` menyisakan `TRF-20260714-0088` dan `BRW-20260718-0007` (2 baris)
32. Klik `(←)` pada kotak Search

### TC-FA-SU-474: Siklus interaksi Search Sub-tab Pending Approvals: reveal, Enter, clear, collapse

33. Klik icon Search
34. Verifikasi input Search melebar
35. Verifikasi kursor fokus di input Search
36. Verifikasi placeholder Search `Search transaction ID, transaction, or requester...`
37. Hover icon Search
38. Verifikasi tooltip `Search` tampil
39. Ketik satu karakter `T` pada input Search
40. Verifikasi icon ✕ tampil di kanan input
41. Verifikasi tabel belum tersaring dan menampilkan sedikitnya satu baris
42. Ketik sisa `RF-2026` pada input Search, tekan Enter
43. Verifikasi tabel tersaring menjadi `TRF-20260714-0088`
44. Klik ✕
45. Verifikasi input Search kosong
46. Verifikasi search bar tetap terbuka
47. Verifikasi kursor fokus di input Search
48. Verifikasi tabel tetap menampilkan hasil search terakhir `TRF-20260714-0088`
49. Tekan Enter
50. Verifikasi tabel kembali menampilkan semua baris
51. Ketik Search `TRF-2026`, tekan Enter
52. Klik `(←)` pada kotak Search
53. Verifikasi search bar menutup
54. Verifikasi tabel langsung kembali menampilkan semua baris
55. Klik icon Search
56. Verifikasi keyword pada input Search dikosongkan
57. Ketik Search `  TRF-2026  `, tekan Enter
58. Verifikasi hasil sama dengan `TRF-2026` tanpa spasi, yaitu `TRF-20260714-0088`
59. Verifikasi isi input Search tetap `  TRF-2026  `
60. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah penghubung tambahan (S-03): klik header kolom Column Visibility (⋯) (langkah 16) memicu `Verifikasi` overlay (TC-FA-SU-471 Expected b), dan `Esc` (langkah 18) menutup overlay sebelum langkah berikutnya (S-09).
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (60 langkah, 60 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-475 sampai 479 ada di spec 161; TC-FA-SU-499 ada di spec 166.
- Temuan untuk QA (S-15):
  - Pre-setup #25 hanya menyebut "5 baris" Pending Approvals; Requester dan Transaction per baris diturunkan dari Expected TC (Requester `Citra L` untuk dua baris dari keyword `Lestari`).
  - TC-FA-SU-474 Expected b/f menyebut tabel "belum tersaring" dan "keyword dikosongkan" tanpa langkah observasi pasti; spec mengasersi lima baris tampil dan membuka kembali icon Search untuk memeriksa input kosong.
