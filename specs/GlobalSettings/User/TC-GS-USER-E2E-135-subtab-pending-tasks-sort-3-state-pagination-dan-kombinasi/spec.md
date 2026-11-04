---
id: TC-GS-USER-E2E-135-subtab-pending-tasks-sort-3-state-pagination-dan-kombinasi
title: "Sub-tab Pending Tasks: Sort 3-state, Pagination, dan Kombinasi Search, Filter, Sort, dan Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-852
  - TC-GS-USER-853
  - TC-GS-USER-854
  - TC-GS-USER-869
  - TC-GS-USER-870
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Sort 3-state, Pagination, dan Kombinasi Search, Filter, Sort, dan Pagination

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data User; yang di-seed hanya task pending FAMS milik spec (Population PT-22).
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List (sub-tab Login User) dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat `B0` + 22 baris sesudah seeding, dengan `B0` = jumlah task pending Pre-setup Ahmad Fauzi yang dibaca lewat kemampuan baca BE tepat sebelum seeding; kemampuan itu disediakan tim FE/BE). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC task seed memakai Group dan user FAMS yang disediakan tim FE/BE dan bernama bersuffix `{runId}-135` (`{group-A}` = `Alfa {runId}-135`, `{group-B}` = `Beta {runId}-135`; PIC `{pic-A}` nama lengkap `Rina Pica {runId}-135`, `{pic-B}` nama lengkap `Sari Picb {runId}-135`; teks tampil sel PIC `[First Name] [Last Initial]`: `{pic-A-tampil}` = `Rina P`, `{pic-B-tampil}` = `Sari P`, dua nilai berbeda; asersi sel dan sort kolom PIC memakai nilai tampil, nama lengkap hanya untuk Search dan hover), sehingga tidak bentrok dengan task Pre-setup. Task Pre-setup Ahmad Fauzi (`B0` baris) tidak diubah dan isinya tidak diasumsikan: asersi jumlah per nilai Group atau PIC memakai nama bersuffix itu, sedangkan asersi per nilai Transaction, Status, Total Asset, Request Date, atau Last Updated menyebut baris seed (task milik spec ini). Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A-tampil}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B-tampil}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2a | 1 | `Borrowing` | `Waiting for Confirmation` | kosong (tampil `—`) | `{pic-B-tampil}` | `1` | `{rd-2}` | `{lu-1}` |
  | Q2b | 1 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | kosong (tampil `—`) | `2` | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A-tampil}` lebih kecil dari `{pic-B-tampil}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (`lfa {runId}-135`, potongan `{group-A}`) dan `{kw-pic}` (`Pica {runId}-135`, potongan nama lengkap `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan (baris seed): Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 9 baris, `{group-B}` 12 baris, dan kosong 1 baris; PIC `{pic-A-tampil}` 8 baris, `{pic-B-tampil}` 13 baris, dan kosong 1 baris (kosong dibutuhkan TC-GS-USER-852 butir d dan e); Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; total tabel `B0` + 22 baris sehingga page size 10 menghasilkan sedikitnya 3 halaman.
- Data uji per TC: TC-GS-USER-852 kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`; TC-GS-USER-853 kolom `Total Asset` (nilai `1`, `2`, `3`, `10` sehingga urutan natural dapat dibedakan dari urutan teks); TC-GS-USER-854 kolom `Request Date` dan `Last Updated`; TC-GS-USER-869 page size 25 dan 10, nomor halaman `2` (22 baris seed); TC-GS-USER-870 Search `{runId}-135`, Filter Transaction `Borrowing`, sort `Total Asset`, page size 25.
- Pembatas Search: baris Pre-setup (`B0`) tidak diasumsikan, sehingga seluruh asersi urutan dan jumlah memakai Search `{runId}-135` (cocok dengan Group atau PIC bersuffix; setiap baris seed memuat sedikitnya satu kolom bersuffix, termasuk Q2a dan Q2b) yang membatasi tabel pada 22 baris seed; Search itu adalah langkah penghubung (S-03), dan TC-GS-USER-870 memasang Search-nya sendiri sesudah Search penghubung ditutup.
- Default sort tabel: Request Date Oldest First (PRD `user.md` §4.1.3); klik ketiga pada tiap header mengembalikan urutan itu.
- Kemampuan teknis: membaca urutan nilai kolom pada halaman 1; mengubah page size dan mengisi input nomor halaman; seeding task pending FAMS dan pembersihannya (di atas).
- State yang diubah dan dipulihkan: sort dikembalikan ke default oleh klik ketiga tiap kolom; nomor halaman dikembalikan ke 1 di langkah 73; Search penghubung ditutup di langkah 74; page size dikembalikan ke 10 di langkah 87; Filter dan Search TC-GS-USER-870 dikosongkan di langkah 89 sampai 92; hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-852: Sort 3-state kolom kelas teks A-Z

1. Klik icon Search di User List, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Tasks`
5. Verifikasi footer pagination menampilkan sedikitnya 3 halaman (total `B0` + 22 baris)
6. Klik icon Search, ketik `{runId}-135`, tekan Enter
7. Verifikasi halaman 1 berisi 10 baris dan footer pagination menampilkan 3 halaman (22 baris seed)
8. Ubah page size ke 25
9. Verifikasi halaman 1 menampilkan 22 baris seed (pembanding sebelum sort)
10. Klik header `Transaction ID` (klik 1)
11. Verifikasi Transaction ID terurut A-Z: baris 1 sampai 8 berawalan `ASG-`, baris 9 sampai 22 berawalan `BRW-`
12. Klik header `Transaction ID` (klik 2)
13. Verifikasi Transaction ID terurut Z-A: baris 1 sampai 14 berawalan `BRW-`, baris 15 sampai 22 berawalan `ASG-`
14. Klik header `Transaction ID` (klik 3)
15. Verifikasi Transaction ID kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)
16. Klik header `Transaction` (klik 1)
17. Verifikasi Transaction terurut A-Z: baris 1 sampai 8 `Assignment`, baris 9 sampai 22 `Borrowing`
18. Klik header `Transaction` (klik 2)
19. Verifikasi Transaction terurut Z-A: baris 1 sampai 14 `Borrowing`, baris 15 sampai 22 `Assignment`
20. Klik header `Transaction` (klik 3)
21. Verifikasi Transaction kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)
22. Klik header `Status` (klik 1)
23. Verifikasi Status terurut A-Z: baris 1 sampai 8 `Waiting for Acceptance`, baris 9 sampai 22 `Waiting for Confirmation`
24. Klik header `Status` (klik 2)
25. Verifikasi Status terurut Z-A: baris 1 sampai 14 `Waiting for Confirmation`, baris 15 sampai 22 `Waiting for Acceptance`
26. Klik header `Status` (klik 3)
27. Verifikasi Status kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)
28. Klik header `Group` (klik 1)
29. Verifikasi Group terurut A-Z: baris 1 sampai 9 `{group-A}`, baris 10 sampai 21 `{group-B}`
30. Verifikasi Group klik 1: kosong di akhir (baris 22 bernilai `—`)
31. Klik header `Group` (klik 2)
32. Verifikasi Group terurut Z-A: baris 2 sampai 13 `{group-B}`, baris 14 sampai 22 `{group-A}`
33. Verifikasi Group klik 2: kosong di awal (baris 1 bernilai `—`)
34. Klik header `Group` (klik 3)
35. Verifikasi Group kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)
36. Klik header `PIC` (klik 1)
37. Verifikasi PIC terurut A-Z: baris 1 sampai 8 `{pic-A-tampil}`, baris 9 sampai 21 `{pic-B-tampil}`
38. Verifikasi PIC klik 1: kosong di akhir (baris 22 bernilai `—`)
39. Klik header `PIC` (klik 2)
40. Verifikasi PIC terurut Z-A: baris 2 sampai 14 `{pic-B-tampil}`, baris 15 sampai 22 `{pic-A-tampil}`
41. Verifikasi PIC klik 2: kosong di awal (baris 1 bernilai `—`)
42. Klik header `PIC` (klik 3)
43. Verifikasi PIC kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)

### TC-GS-USER-853: Sort 3-state kolom kelas numerik

44. Klik header `Total Asset` (klik 1)
45. Verifikasi Total Asset terurut kecil ke besar secara natural: baris 1 sampai 6 `1`, baris 7 sampai 10 `2`, baris 11 sampai 16 `3`, baris 17 sampai 22 `10`
46. Klik header `Total Asset` (klik 2)
47. Verifikasi Total Asset terurut besar ke kecil: baris 1 sampai 6 `10`, baris 7 sampai 12 `3`, baris 13 sampai 16 `2`, baris 17 sampai 22 `1`
48. Klik header `Total Asset` (klik 3)
49. Verifikasi Total Asset kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)

### TC-GS-USER-854: Sort 3-state kolom kelas tanggal

50. Klik header `Request Date` (klik 1)
51. Verifikasi Request Date Oldest First: baris 1 sampai 8 `{rd-1}`, baris 9 sampai 10 `{rd-2}`, baris 11 sampai 22 `{rd-3}`
52. Klik header `Request Date` (klik 2)
53. Verifikasi Request Date Newest First: baris 1 sampai 12 `{rd-3}`, baris 13 sampai 14 `{rd-2}`, baris 15 sampai 22 `{rd-1}`
54. Klik header `Request Date` (klik 3)
55. Verifikasi Request Date kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)
56. Klik header `Last Updated` (klik 1)
57. Verifikasi Last Updated Oldest First: baris 1 sampai 10 `{lu-1}`, baris 11 sampai 22 `{lu-2}`
58. Klik header `Last Updated` (klik 2)
59. Verifikasi Last Updated Newest First: baris 1 sampai 12 `{lu-2}`, baris 13 sampai 22 `{lu-1}`
60. Klik header `Last Updated` (klik 3)
61. Verifikasi Last Updated kembali ke default sort tabel: urutan default Request Date Oldest First (baris 1 sampai 8 Transaction `Assignment` dengan Request Date `{rd-1}`, baris 9 sampai 10 Transaction `Borrowing` dengan Request Date `{rd-2}`)

### TC-GS-USER-869: Pagination ubah page size dan input nomor halaman

62. Ubah page size ke 10
63. Verifikasi halaman 1 berisi 10 baris dan footer pagination menampilkan 3 halaman (page size 10)
64. Ubah page size ke 25
65. Verifikasi halaman 1 menampilkan 22 baris (maksimal 25 baris per halaman)
66. Ubah page size ke 10
67. Ketik `2` pada input nomor halaman, tekan Enter
68. Verifikasi halaman 2 langsung terbuka
69. Klik Next
70. Verifikasi tabel berpindah ke halaman 3 (2 baris)
71. Klik Previous
72. Verifikasi tabel berpindah kembali ke halaman 2
73. Ketik `1` pada input nomor halaman, tekan Enter
74. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-870: Kombinasi Search, Filter, Sort, dan Pagination berjalan bersamaan

75. Klik icon Search, ketik `{runId}-135`, tekan Enter
76. Klik icon Filter
77. Buka dropdown `Transaction`
78. Pilih opsi `Borrowing` pada dropdown `Transaction`
79. Klik `[Apply]`
80. Verifikasi tabel menampilkan 14 baris seed Transaction `Borrowing` (halaman 1 berisi 10 baris, 2 halaman)
81. Klik header `Total Asset` (sort ascending)
82. Ubah page size ke 25
83. Verifikasi keyword `{runId}-135` tetap aktif: kotak Search berisi `{runId}-135`
84. Verifikasi Filter Transaction `Borrowing` tetap aktif: tabel hanya memuat baris Transaction `Borrowing`
85. Verifikasi sort Total Asset ascending tetap aktif: baris 1 `1`, baris 2 `2`, baris 3 sampai 8 `3`, baris 9 sampai 14 `10`
86. Verifikasi page size 25 berlaku: seluruh 14 baris tampil pada satu halaman
87. Ubah page size ke 10
88. Klik header `Total Asset` dua kali sampai indikator sort netral
89. Klik icon Filter
90. Klik `[Clear Field]`
91. Klik `[Apply]`
92. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (852, 853, 854, 869, 870) dipertahankan.
- Langkah 1 sampai 4 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List agar Name dapat diklik, bagian 8b butir 12); langkah 6 (Search `{runId}-135` membatasi tabel pada 22 baris seed) dan 8 (page size 25 agar seluruh 22 baris teramati pada satu halaman untuk TC-GS-USER-852 sampai 854); langkah 73 (kembali ke halaman 1) dan 74 (menutup Search penghubung); rangkaian pembersihan di akhir spec (page size 10, sort netral, Filter dikosongkan, Search ditutup, S-09). Klik ketiga pada tiap header mengembalikan sort ke default, sehingga TC sort berikutnya dimulai dari state default.
- Asersi tambahan (S-03, dengan alasan): langkah 5 (total `B0` + 22 baris), 7, 9, dan `Verifikasi` keadaan awal TC-GS-USER-869 adalah pembanding sebelum asersi sesudahnya (S-14); posisi baris pada Expected sort adalah konkretisasi "A-Z / Z-A / kecil→besar / Oldest First" dari Population PT-22 (dua nilai distinct atau lebih pada tiap kolom, S-11) pada 22 baris seed. Nilai kosong Group dan PIC (Q2a dan Q2b) mengasersi butir "kosong di akhir" dan "kosong di awal" TC-GS-USER-852 butir d dan e.
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 ada di spec 132; TC-GS-USER-837 sampai 846 ada di spec 133; TC-GS-USER-847 sampai 851 ada di spec 134; TC-GS-USER-855 sampai 863 ada di spec 136; TC-GS-USER-398 dan 864 sampai 868 ada di spec 137. TC Sort dan Pagination sub-tab Pending Approvals ada di spec 129.
- Spec melewati sekitar 35 langkah (92 langkah) karena TC-GS-USER-852 sampai 854 menguji delapan kolom dengan blok identik (tiga klik header dengan satu `Verifikasi` tiap klik), ditambah dua TC Pagination dan kombinasi; semuanya satu layar, satu dataset (PT-22), dan satu kelas harness (fungsional). Tiap blok kolom berdiri sendiri dan state sort dikembalikan ke default oleh klik ketiga, sehingga satu kegagalan tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Sort PIC dan asersi sel memakai nilai tampil `{pic-A-tampil}` (`Rina P`) dan `{pic-B-tampil}` (`Sari P`); sort sebenarnya memakai nama lengkap (PRD `user.md` §4.1.3), urutannya sama dengan urutan teks tampil pada dua PIC ini. Format opsi dropdown PIC menunggu PRD §4.1.3.
  - TC-GS-USER-852 sampai 854: default sort tabel adalah Request Date Oldest First (TC-GS-USER-396), sehingga klik 1 dan klik 3 pada kolom `Request Date` menghasilkan komposisi halaman 1 yang sama; keduanya dibedakan lewat langkah klik bernomor, bukan lewat urutan baris. Urutan antar-baris bernilai sama (mis. 8 baris `Assignment`) tidak diasersi.
  - TC-GS-USER-852: sort kolom `PIC` memakai nama lengkap (PRD `user.md` §4.1.3) sedangkan sel menampilkan `[First Name] [Last Initial]`; spec memakai dua PIC yang urutan A-Z nama lengkapnya sama dengan urutan teks tampilnya.
  - TC-GS-USER-869: Data Uji menyebut tabel berisi 25 baris (fixture BE, Pre-setup No. 29) pada user `Volume Test User`; spec memakai Ahmad Fauzi dengan 22 baris seed milik spec (S-06) yang dibatasi Search `{runId}-135`. Asersi "maksimal 25 baris" diamati lewat 22 baris pada halaman 1; `Verifikasi` keadaan awal (10 baris, 3 halaman) ditambahkan sebagai pembanding. Hasil next dan prev diasersi lewat halaman 3 (2 baris) dan halaman 2.
  - TC-GS-USER-870: kontrol page size hanya tampil bila hasil lebih dari 10 baris (PRD `user.md` §4.1.3), sehingga kombinasi dibentuk dengan hasil 14 baris (Search `{runId}-135` dan Filter Transaction `Borrowing`).
  - Seeding task pending FAMS dengan nilai Group, PIC, Request Date, dan Last Updated tertentu tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE.
