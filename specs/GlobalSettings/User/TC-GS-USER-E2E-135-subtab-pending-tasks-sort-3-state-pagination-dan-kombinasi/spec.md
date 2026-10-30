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
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat tepat 22 baris saat spec mulai). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC memakai Group dan user FAMS yang disediakan tim FE/BE. Bila Ahmad Fauzi sudah memiliki task pending Pre-setup, task itu dihitung ke dalam komposisi di bawah. Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A}` lebih kecil dari `{pic-B}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (kata pertama `{group-A}`) dan `{kw-pic}` (nama depan `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan: Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris dan `{group-B}` 12 baris; PIC `{pic-A}` 8 baris dan `{pic-B}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; page size 10 menghasilkan 3 halaman (10, 10, 2 baris).
- Data uji per TC: TC-GS-USER-852 kolom `Transaction ID`, `Transaction`, `Status`, `Group`, `PIC`; TC-GS-USER-853 kolom `Total Asset` (nilai `1`, `2`, `3`, `10` sehingga urutan natural dapat dibedakan dari urutan teks); TC-GS-USER-854 kolom `Request Date` dan `Last Updated`; TC-GS-USER-869 page size 25 dan 10, nomor halaman `2` (data 22 baris, memenuhi Data Uji TC ≥21 baris); TC-GS-USER-870 Search `Borrowing`, Filter Group `{group-B}`, sort `Total Asset`, page size 25.
- Default sort tabel: Request Date Oldest First (PRD `user.md` §4.1.3); klik ketiga pada tiap header mengembalikan urutan itu.
- Kemampuan teknis: membaca urutan nilai kolom pada halaman 1; mengubah page size dan mengisi input nomor halaman; seeding task pending FAMS dan pembersihannya (di atas).
- State yang diubah dan dipulihkan: sort dikembalikan ke default oleh klik ketiga tiap kolom; nomor halaman dikembalikan ke 1 di langkah 62; page size dikembalikan ke 10 di langkah 74; Filter dan Search dikosongkan di langkah 79; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-852: Sort 3-state kolom kelas teks A-Z

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Tasks`
4. Klik header `Transaction ID` (klik 1)
5. Verifikasi Transaction ID terurut A-Z pada halaman 1: 8 baris berawalan `ASG-` lalu 2 baris berawalan `BRW-`
6. Klik header `Transaction ID` (klik 2)
7. Verifikasi Transaction ID terurut Z-A pada halaman 1: 10 baris berawalan `BRW-`
8. Klik header `Transaction ID` (klik 3)
9. Verifikasi Transaction ID kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)
10. Klik header `Transaction` (klik 1)
11. Verifikasi Transaction terurut A-Z pada halaman 1: 8 baris `Assignment` lalu 2 baris `Borrowing`
12. Klik header `Transaction` (klik 2)
13. Verifikasi Transaction terurut Z-A pada halaman 1: 10 baris `Borrowing`
14. Klik header `Transaction` (klik 3)
15. Verifikasi Transaction kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)
16. Klik header `Status` (klik 1)
17. Verifikasi Status terurut A-Z pada halaman 1: 8 baris `Waiting for Acceptance` lalu 2 baris `Waiting for Confirmation`
18. Klik header `Status` (klik 2)
19. Verifikasi Status terurut Z-A pada halaman 1: 10 baris `Waiting for Confirmation`
20. Klik header `Status` (klik 3)
21. Verifikasi Status kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)
22. Klik header `Group` (klik 1)
23. Verifikasi Group terurut A-Z pada halaman 1: 10 baris `{group-A}`
24. Klik header `Group` (klik 2)
25. Verifikasi Group terurut Z-A pada halaman 1: 10 baris `{group-B}`
26. Klik header `Group` (klik 3)
27. Verifikasi Group kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)
28. Klik header `PIC` (klik 1)
29. Verifikasi PIC terurut A-Z pada halaman 1: 8 baris `{pic-A}` lalu 2 baris `{pic-B}`
30. Klik header `PIC` (klik 2)
31. Verifikasi PIC terurut Z-A pada halaman 1: 10 baris `{pic-B}`
32. Klik header `PIC` (klik 3)
33. Verifikasi PIC kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)

### TC-GS-USER-853: Sort 3-state kolom kelas numerik

34. Klik header `Total Asset` (klik 1)
35. Verifikasi Total Asset terurut kecil ke besar secara natural pada halaman 1: 6 baris `1` lalu 4 baris `2`
36. Klik header `Total Asset` (klik 2)
37. Verifikasi Total Asset terurut besar ke kecil pada halaman 1: 6 baris `10` lalu 4 baris `3`
38. Klik header `Total Asset` (klik 3)
39. Verifikasi Total Asset kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)

### TC-GS-USER-854: Sort 3-state kolom kelas tanggal

40. Klik header `Request Date` (klik 1)
41. Verifikasi Request Date Oldest First pada halaman 1: 8 baris `{rd-1}` lalu 2 baris `{rd-2}`
42. Klik header `Request Date` (klik 2)
43. Verifikasi Request Date Newest First pada halaman 1: 10 baris `{rd-3}`
44. Klik header `Request Date` (klik 3)
45. Verifikasi Request Date kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)
46. Klik header `Last Updated` (klik 1)
47. Verifikasi Last Updated Oldest First pada halaman 1: 10 baris `{lu-1}`
48. Klik header `Last Updated` (klik 2)
49. Verifikasi Last Updated Newest First pada halaman 1: 10 baris `{lu-2}`
50. Klik header `Last Updated` (klik 3)
51. Verifikasi Last Updated kembali ke default sort tabel: urutan default Request Date Oldest First (halaman 1: 8 baris Transaction `Assignment` dengan Request Date `{rd-1}`, lalu 2 baris Transaction `Borrowing` dengan Request Date `{rd-2}`)

### TC-GS-USER-869: Pagination ubah page size dan input nomor halaman

52. Verifikasi halaman 1 berisi 10 baris dan footer pagination menampilkan 3 halaman (page size 10)
53. Ubah page size ke 25
54. Verifikasi halaman 1 menampilkan 22 baris (maksimal 25 baris per halaman)
55. Ubah page size ke 10
56. Ketik `2` pada input nomor halaman, tekan Enter
57. Verifikasi halaman 2 langsung terbuka
58. Klik Next
59. Verifikasi tabel berpindah ke halaman 3 (2 baris)
60. Klik Previous
61. Verifikasi tabel berpindah kembali ke halaman 2
62. Ketik `1` pada input nomor halaman, tekan Enter

### TC-GS-USER-870: Kombinasi Search, Filter, Sort, dan Pagination berjalan bersamaan

63. Klik icon Search, ketik `Borrowing`, tekan Enter
64. Klik icon Filter
65. Pilih opsi `{group-B}` pada dropdown `Group`
66. Klik `[Apply]`
67. Verifikasi tabel menampilkan 12 baris Transaction `Borrowing` dengan Group `{group-B}` (halaman 1 berisi 10 baris, 2 halaman)
68. Klik header `Total Asset` (sort ascending)
69. Ubah page size ke 25
70. Verifikasi keyword `Borrowing` tetap aktif: kotak Search berisi `Borrowing`
71. Verifikasi Filter Group `{group-B}` tetap aktif: icon Filter berwarna gelap dan tabel hanya memuat baris Group `{group-B}`
72. Verifikasi sort Total Asset ascending tetap aktif: baris berurutan Total Asset `3` (6 baris) lalu `10` (6 baris)
73. Verifikasi page size 25 berlaku: seluruh 12 baris tampil pada satu halaman
74. Ubah page size ke 10
75. Klik header `Total Asset` dua kali sampai indikator sort netral
76. Klik icon Filter
77. Klik `[Clear Field]`
78. Klik `[Apply]`
79. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (852, 853, 854, 869, 870) dipertahankan.
- Langkah 1 sampai 3 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 62 (kembali ke halaman 1), serta rangkaian pembersihan di akhir spec (langkah 74 sampai 79: page size 10, sort netral, Filter dikosongkan, Search ditutup, S-09). Klik ketiga pada tiap header mengembalikan sort ke default, sehingga TC sort berikutnya dimulai dari state default; langkah 68 membentuk Sort aktif untuk TC-GS-USER-870.
- Asersi tambahan (S-03, dengan alasan): langkah 52 dan 67 adalah `Verifikasi` keadaan awal sebelum page size diubah (S-14) dan menjadi pembanding asersi sesudahnya; komposisi halaman 1 pada Expected sort adalah konkretisasi "A-Z / Z-A / kecil→besar / Oldest First" dari Population PT-22 (dua nilai distinct atau lebih pada tiap kolom, S-11).
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 ada di spec 132; TC-GS-USER-837 sampai 846 ada di spec 133; TC-GS-USER-847 sampai 851 ada di spec 134; TC-GS-USER-855 sampai 863 ada di spec 136; TC-GS-USER-398 dan 864 sampai 868 ada di spec 137. TC Sort dan Pagination sub-tab Pending Approvals ada di spec 129.
- Spec melewati sekitar 35 langkah (79 langkah) karena TC-GS-USER-852 sampai 854 menguji delapan kolom dengan blok identik (tiga klik header dengan satu `Verifikasi` tiap klik), ditambah dua TC Pagination dan kombinasi; semuanya satu layar, satu dataset (PT-22), dan satu kelas harness (fungsional). Tiap blok kolom berdiri sendiri dan state sort dikembalikan ke default oleh klik ketiga, sehingga satu kegagalan tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-USER-852 sampai 854: default sort tabel adalah Request Date Oldest First (TC-GS-USER-396), sehingga klik 1 dan klik 3 pada kolom `Request Date` menghasilkan komposisi halaman 1 yang sama; keduanya dibedakan lewat langkah klik bernomor, bukan lewat urutan baris. Urutan antar-baris bernilai sama (mis. 8 baris `Assignment`) tidak diasersi.
  - TC-GS-USER-852: sort kolom `PIC` memakai nama lengkap (PRD `user.md` §4.1.3) sedangkan sel menampilkan `[First Name] [Last Initial]`; spec memakai dua PIC yang urutan A-Z nama lengkapnya sama dengan urutan teks tampilnya.
  - TC-GS-USER-869: Data Uji "≥21 baris" dipenuhi Population PT-22 (22 baris). Asersi "maksimal 25 baris" diamati lewat 22 baris pada halaman 1; `Verifikasi` keadaan awal (10 baris, 3 halaman) ditambahkan sebagai pembanding. Hasil next dan prev diasersi lewat halaman 3 (2 baris) dan halaman 2.
  - TC-GS-USER-870: "Terapkan filter bila tersedia" bersyarat; Filter Panel tersedia pada sub-tab ini sehingga spec menerapkan Filter Group `{group-B}` tanpa kondisi. Kontrol page size hanya tampil bila hasil lebih dari 10 baris (PRD `user.md` §4.1.3), sehingga kombinasi dibentuk dengan hasil 12 baris.
  - Seeding task pending FAMS dengan nilai Group, PIC, Request Date, dan Last Updated tertentu tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE.
