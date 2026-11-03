---
id: TC-FA-SU-E2E-166-sub-tab-pending-approvals-pagination-tooltip-icon-dan-state-per-sub-tab
title: "Sub-tab Pending Approvals: Pagination, Tooltip Icon, dan State per Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-494
  - TC-FA-SU-499
  - TC-FA-SU-501
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Pagination, Tooltip Icon, dan State per Sub-tab

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
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |

## Test Steps

### TC-FA-SU-494: Pagination Sub-tab Pending Approvals: page size, navigasi, dan kasus tepi

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
3. Verifikasi default 10 baris per halaman
4. Klik pilihan page size
5. Verifikasi pilihan page size `10`, `25`, `50`, dan `100` tanpa opsi All
6. Tekan Esc untuk menutup pilihan page size
7. Isi nomor halaman `0`, tekan Enter
8. Verifikasi tabel tetap di halaman 1
9. Isi nomor halaman `-1`, tekan Enter
10. Verifikasi tabel tetap di halaman 1
11. Isi nomor halaman `999`, tekan Enter
12. Verifikasi tabel tetap di halaman 1
13. Isi nomor halaman `abc`, tekan Enter
14. Verifikasi tabel tetap di halaman 1
15. Ganti page size ke 25
16. Verifikasi tabel menampilkan halaman 1
17. Ganti page size ke 10
18. Klik header Transaction ID
19. Verifikasi tabel menampilkan halaman 1
20. Klik header Transaction ID dua kali lagi untuk mengembalikan urutan default
21. Ketik Search `TRF-2026`, tekan Enter
22. Verifikasi tabel menampilkan halaman 1
23. Klik `(←)` pada kotak Search

### TC-FA-SU-499: Tooltip icon Table Tools dan header Actions Sub-tab Pending Approvals

24. Hover icon Search
25. Verifikasi tooltip `Search` tampil
26. Hover icon Filter
27. Verifikasi tooltip `Filter` tampil
28. Hover icon Download
29. Verifikasi tooltip `Download` tampil
30. Hover header kolom Actions (⋯)
31. Verifikasi tooltip `Column Visibility` tampil

### TC-FA-SU-501: State Sub-tab Pending Approvals dipertahankan per sub-tab

32. Ketik Search `TRF-2026`, tekan Enter
33. Klik icon Filter
34. Buka dropdown Transaction
35. Centang `Transfer`
36. Klik `[Apply]`
37. Klik header Transaction ID
38. Klik pilihan page size
39. Pilih page size 25
40. Klik Sub-tab Assigned Assets
41. Ketik Search `Printer`, tekan Enter
42. Klik icon Filter
43. Buka dropdown Brand
44. Centang `Canon`
45. Klik `[Apply]`
46. Klik header Model / Type
47. Klik Sub-tab Pending Approvals
48. Verifikasi Search `TRF-2026` dipulihkan pada Sub-tab Pending Approvals
49. Verifikasi Filter Transaction `Transfer` dipulihkan
50. Verifikasi Sort kolom Transaction ID dipulihkan
51. Verifikasi page size 25 dipulihkan
52. Klik Sub-tab Assigned Assets
53. Verifikasi Sub-tab Assigned Assets tetap memakai state-nya sendiri: Search `Printer`, Filter Brand `Canon`, dan Sort Model / Type
54. Klik Sub-tab Pending Approvals
55. Klik Back breadcrumb ke User List
56. Klik nama `Budi Santoso` di User List
57. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
58. Verifikasi state Sub-tab Pending Approvals dipulihkan: Search `TRF-2026`, Filter Transaction `Transfer`, Sort Transaction ID, page size 25
59. Tekan F5 pada halaman Detail
60. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
61. Verifikasi state Sub-tab Pending Approvals dipulihkan: Search `TRF-2026`, Filter Transaction `Transfer`, Sort Transaction ID, page size 25
62. Klik menu Settings > User pada sidebar
63. Klik nama `Budi Santoso` di User List
64. Klik tab Responsibilities, lalu klik Sub-tab Pending Approvals
65. Verifikasi state Sub-tab Pending Approvals kembali ke default: Search kosong, tanpa Filter, Sort default Submission Date ascending, page size 10

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Sub-tab Assigned Assets (Pre-setup #24) dipakai hanya sebagai sub-tab lain pada TC-FA-SU-501; nilai Search `Printer`, Filter Brand `Canon`, dan Sort Model / Type dipilih spec karena TC tidak menyebutnya.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (65 langkah, 65 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Pending Approvals, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-497, 498, dan 500 ada di spec 371, 366, dan 361.
- Temuan untuk QA (S-15):
  - TC-FA-SU-494 Expected e menyatakan perpindahan antar halaman tidak dapat dicapai (fixture satu halaman) dan merujuk TC-FA-SU-359 dan 1057; bukan asersi.
  - TC-FA-SU-501 tidak menyebut tab dan sub-tab aktif setelah F5; spec membuka kembali tab Responsibilities dan sub-tab sebelum mengasersi. Nomor halaman aktif tidak diuji (fixture satu halaman).
  - TC-FA-SU-499 berkolom Automation `UI Only` dan PIC BE `-`; spec tetap `Mode: FE+BE` karena berada pada halaman yang sama dengan backend nyata.
