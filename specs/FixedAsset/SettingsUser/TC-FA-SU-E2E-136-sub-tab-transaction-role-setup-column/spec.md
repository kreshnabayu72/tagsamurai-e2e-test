---
id: TC-FA-SU-E2E-136-sub-tab-transaction-role-setup-column
title: "Sub-tab Transaction Role: Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-401
  - TC-FA-SU-402
  - TC-FA-SU-403
  - TC-FA-SU-408
coverage:
  web: automated
---

# Sub-tab Transaction Role: Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Role (#39). Pengguna target: Yuda Pratama dengan 7 baris Transaction Role: `Borrowing & Assignment - Approver` pada IT Infrastructure; `Damaged - Monitoring & Report` pada Branch Surabaya; `Disposal - Approver` pada All Groups; `Disposal - Staff` pada Logistics Warehouse; `Missing - Approver` pada Branch Surabaya, General Affairs, dan Logistics Warehouse; `Transfer - Asset Admin` pada Finance & Accounting dan IT Infrastructure; `Transfer - Monitoring & Report` pada Branch Surabaya. Ketujuh baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- State yang diubah: preferensi kolom tabel tersimpan per perangkat setelah `[Save]`. Dipulihkan dengan menghapus preferensi kolom tabel ini di browser (kemampuan disediakan tim FE, bagian 4 konvensi), bukan `[Reset to Default]`; langkah pemulihan ada di akhir blok yang menyimpan, dan hook `after` mengulangnya sebagai cadangan. Spec tidak mengubah data backend.
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).

## Test Steps

### TC-FA-SU-408: Setup Column Sub-tab Transaction Role: Column Visibility tersedia untuk kolom Transaction, Role, dan Group

1. Ketik Search `Yuda Pratama`, tekan Enter
2. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
3. Klik header kolom Actions (⋯)
4. Verifikasi overlay Column Visibility memuat Transaction, Role, dan Group (Hideable)
5. Hapus centang Group
6. Centang kembali Group
7. Tutup overlay Column Visibility dengan Esc
8. Verifikasi header kolom Role tidak memiliki icon sort (tidak sortable)
9. Ketik Search `Approver`, tekan Enter
10. Verifikasi kolom Role searchable: keyword `Approver` menyisakan `Borrowing & Assignment - Approver`, `Disposal - Approver`, dan `Missing - Approver`
11. Klik `(←)` pada kotak Search
12. Klik icon Filter
13. Buka dropdown Role
14. Centang `Approver`
15. Klik `[Apply]`
16. Verifikasi kolom Role filterable: Filter Role `Approver` menyisakan `Borrowing & Assignment - Approver`, `Disposal - Approver`, dan `Missing - Approver`
17. Klik `[Clear Field]`
18. Klik `[Apply]`
19. Tutup panel Filter dengan klik icon Filter

### TC-FA-SU-401: Geser (drag reorder) Setup Column Sub-tab Transaction Role kelas Hideable (default tampil)

20. Klik header kolom Actions (⋯)
21. Klik `Setup Column...`
22. Drag kolom Transaction satu posisi ke bawah
23. Verifikasi urutan Live Preview berubah menjadi Role, Transaction, Group
24. Drag kolom Group satu posisi ke atas
25. Verifikasi urutan Live Preview berubah menjadi Role, Group, Transaction
26. Drag kolom Role satu posisi ke bawah
27. Verifikasi urutan Live Preview berubah menjadi Group, Role, Transaction
28. Klik `[Save]`
29. Verifikasi urutan kolom tabel berubah: Transaction berada di posisi ketiga
30. Verifikasi urutan kolom tabel berubah: Group berada di posisi pertama
31. Verifikasi urutan kolom tabel berubah: Role berada di posisi kedua
32. Tekan F5
33. Verifikasi urutan Transaction di posisi ketiga bertahan setelah F5
34. Verifikasi urutan Group di posisi pertama bertahan setelah F5
35. Verifikasi urutan Role di posisi kedua bertahan setelah F5
36. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

### TC-FA-SU-402: Pin dan unpin Setup Column Sub-tab Transaction Role kelas Hideable (default tampil)

37. Klik header kolom Actions (⋯)
38. Klik `Setup Column...`
39. Klik icon Pin pada kolom Transaction
40. Klik icon Pin pada kolom Role
41. Klik icon Pin pada kolom Group
42. Klik `[Save]`
43. Scroll tabel secara horizontal
44. Verifikasi kolom Transaction membeku di kiri saat tabel di-scroll horizontal
45. Verifikasi kolom Role membeku di kiri saat tabel di-scroll horizontal
46. Verifikasi kolom Group membeku di kiri saat tabel di-scroll horizontal
47. Tekan F5
48. Scroll tabel secara horizontal
49. Verifikasi kolom Transaction tetap membeku setelah F5
50. Verifikasi kolom Role tetap membeku setelah F5
51. Verifikasi kolom Group tetap membeku setelah F5
52. Klik header kolom Actions (⋯)
53. Klik `Setup Column...`
54. Klik icon Pin pada kolom Group untuk unpin
55. Klik icon Pin pada kolom Transaction untuk unpin
56. Klik icon Pin pada kolom Role untuk unpin
57. Klik `[Save]`
58. Scroll tabel secara horizontal
59. Verifikasi unpin melepaskan: kolom Group tidak lagi membeku
60. Verifikasi unpin melepaskan: kolom Transaction tidak lagi membeku
61. Verifikasi unpin melepaskan: kolom Role tidak lagi membeku
62. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

### TC-FA-SU-403: Reset to Default, Discard (✕ atau Esc), dan independensi cache Setup Column Sub-tab Transaction Role

63. Klik header kolom Actions (⋯)
64. Klik `Setup Column...`
65. Hapus centang kolom Role
66. Drag kolom Group satu posisi ke atas
67. Klik icon Pin pada kolom Transaction
68. Klik `[Reset to Default]`
69. Verifikasi `[Reset to Default]` mengembalikan visibility ke default pada preview: kolom Transaction, Role, dan Group tampil
70. Verifikasi `[Reset to Default]` mengembalikan urutan ke default pada preview: Transaction, Role, Group
71. Verifikasi `[Reset to Default]` mengembalikan pin ke default pada preview: tidak ada kolom ter-pin
72. Klik `[Save]`
73. Verifikasi konfigurasi default menjadi permanen setelah `[Save]`: tabel menampilkan Transaction, Role, Group tanpa kolom ter-pin
74. Klik header kolom Actions (⋯)
75. Klik `Setup Column...`
76. Hapus centang kolom Role
77. Tutup popup Setup Column dengan ✕
78. Verifikasi menutup lewat ✕ tanpa Save membuang perubahan preview: tabel tetap menampilkan Role
79. Klik header kolom Actions (⋯)
80. Klik `Setup Column...`
81. Hapus centang kolom Role
82. Tutup popup Setup Column dengan Esc
83. Verifikasi menutup lewat Esc tanpa Save membuang perubahan preview: tabel tetap menampilkan Role
84. Buka Detail Yuda Pratama > Tab Role > Sub-tab Group Role
85. Verifikasi konfigurasi kolom Sub-tab Group Role tidak terpengaruh oleh perubahan konfigurasi Sub-tab Transaction Role (cache per tabel)
86. Pulihkan konfigurasi kolom: hapus preferensi kolom tabel ini di browser lalu muat ulang halaman

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung Search (S-03, R-16): langkah 1 (Ketik Search `Yuda Pratama`, tekan Enter) untuk menemukan baris Yuda Pratama di User List 25 pengguna (3 halaman) sebelum membuka Detail.
- Pemulihan konfigurasi kolom: preferensi kolom yang disimpan spec dihapus di browser pada akhir blok dan di hook `after` (Prerequisites); `[Reset to Default]` tidak dipakai sebagai pemulihan.
- Alasan melewati sekitar 35 langkah (86 langkah tertulis, 86 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15):
  - TC-FA-SU-408 butir b: TC tidak menyebut cara memeriksa "searchable dan filterable"; spec memakai Search `Approver` dan Filter Role `Approver` (hasil sama dengan TC-FA-SU-384).
  - TC-FA-SU-401: arah dan urutan seret dipilih penulis (Transaction turun satu, Group naik satu, Role turun satu) karena TC hanya menyebut "satu posisi". Post Condition tidak punya langkah observasi dan tidak diasersi.
  - TC-FA-SU-402 butir d: tabel hanya memiliki tiga kolom Hideable, sehingga setelah ketiganya di-pin tidak ada "kolom lain" yang icon Pin-nya dapat diamati disabled; butir d tidak diasersi. Scroll horizontal pada tabel tiga kolom membutuhkan viewport sempit (Prerequisites). Post Condition tidak diasersi.
  - TC-FA-SU-403: "beberapa pengaturan" dan "tabel lain yang punya Setup Column" tidak dirinci; spec memilih sendiri (Role di-uncheck, Group digeser, Transaction di-pin; tabel lain = Sub-tab Group Role). Perubahan yang disimpan berupa konfigurasi default, sehingga independensi cache diasersi sebagai konfigurasi tabel lain tidak berubah. Post Condition tidak diasersi.
  - TC-FA-SU-402 langkah 5 hanya menyebut "Unpin satu kolom", sedangkan butir a sampai c masing-masing meminta unpin melepaskan kolomnya; spec meng-unpin ketiga kolom (Group, Transaction, Role) dan mengasersi tiap kolom terlepas.
