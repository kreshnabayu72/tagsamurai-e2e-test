---
id: TC-GS-USER-E2E-134-subtab-pending-tasks-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Sub-tab Pending Tasks: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-847
  - TC-GS-USER-848
  - TC-GS-USER-849
  - TC-GS-USER-850
  - TC-GS-USER-851
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris

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
- Data uji per TC: TC-GS-USER-847 Search `Borrowing` lalu Filter Group `{group-A}`; TC-GS-USER-848 Filter Group `{group-A}` lalu Search `Borrowing`; TC-GS-USER-849 Search `Borrowing`, sort kolom `Total Asset`, Filter Group `{group-A}`; TC-GS-USER-850 Filter Group `{group-A}` lalu kolom `Group` di-hide; TC-GS-USER-851 Search `Assignment` dan Filter Group `{group-B}` (tidak beririsan).
- Kemampuan teknis: memilih opsi pada dropdown multi-select searchable; membaca indikator sort pada header kolom; membaca warna icon Filter; seeding task pending FAMS dan pembersihannya (di atas).
- Preferensi kolom tabel Pending Tasks (visibilitas, urutan, pin) tersimpan per user di browser (cache `localStorage`, PRD `prd-conventions.md` §9.3); hook `after` menghapus preferensi itu sebagai cadangan. Nama key dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
- State yang diubah dan dipulihkan: kolom `Group` dicentang kembali di langkah 54; Filter dikosongkan di akhir tiap blok; sort `Total Asset` dikembalikan netral di langkah 39; kotak Search ditutup di akhir tiap blok dan di langkah 66; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-847: Search lalu Filter menghasilkan irisan

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Tasks`
4. Klik icon Search, ketik `Borrowing`, tekan Enter
5. Verifikasi tabel menampilkan 14 baris Transaction `Borrowing` (halaman 1 berisi 10 baris, 2 halaman)
6. Klik icon Filter
7. Pilih opsi `{group-A}` pada dropdown `Group`
8. Klik `[Apply]`
9. Verifikasi hasil adalah irisan Search dan Filter: tabel hanya menampilkan 2 baris Transaction `Borrowing` dengan Group `{group-A}`
10. Verifikasi baris Transaction `Assignment` dengan Group `{group-A}` tidak tampil (Filter Group `{group-A}` saja memuat baris itu)
11. Verifikasi keyword `Borrowing` tidak ter-reset: kotak Search tetap berisi `Borrowing`
12. Klik icon Filter
13. Klik `[Clear Field]`
14. Klik `[Apply]`
15. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-848: Filter lalu Search menghasilkan irisan

16. Klik icon Filter
17. Pilih opsi `{group-A}` pada dropdown `Group`
18. Klik `[Apply]`
19. Verifikasi tabel hanya menampilkan 10 baris Group `{group-A}`
20. Klik icon Search, ketik `Borrowing`, tekan Enter
21. Verifikasi hasil adalah irisan Filter dan Search: tabel hanya menampilkan 2 baris Transaction `Borrowing` dengan Group `{group-A}`
22. Verifikasi Filter tetap aktif: icon Filter berwarna gelap
23. Klik icon Filter
24. Klik `[Clear Field]`
25. Klik `[Apply]`
26. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-849: Clear filter saat Search dan Sort aktif

27. Klik icon Search, ketik `Borrowing`, tekan Enter
28. Klik header `Total Asset` (sort ascending)
29. Klik icon Filter
30. Pilih opsi `{group-A}` pada dropdown `Group`
31. Klik `[Apply]`
32. Verifikasi Filter menyaring: tabel hanya menampilkan 2 baris Transaction `Borrowing` dengan Group `{group-A}`
33. Klik icon Filter
34. Klik `[Clear Field]`
35. Klik `[Apply]`
36. Verifikasi keyword `Borrowing` tetap aktif: kotak Search berisi `Borrowing`
37. Verifikasi arah sort Total Asset ascending tetap aktif: halaman 1 berurutan Total Asset `1`, `2`, `3` (6 baris), lalu `10` (2 baris)
38. Verifikasi Filter terlepas: tabel menampilkan kembali baris Group `{group-B}` (14 baris Transaction `Borrowing`, halaman 1 berisi 10 baris)
39. Klik header `Total Asset` dua kali sampai indikator sort netral
40. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-850: Filter tetap tersedia untuk kolom yang di-hide

41. Klik icon Filter
42. Pilih opsi `{group-A}` pada dropdown `Group`
43. Klik `[Apply]`
44. Verifikasi tabel hanya menampilkan 10 baris Group `{group-A}` (8 baris Transaction `Assignment` dan 2 baris Transaction `Borrowing`)
45. Klik header kolom Column Visibility (⋯)
46. Hilangkan centang kolom `Group` pada Overlay Column Visibility
47. Verifikasi kolom `Group` tidak tampil di tabel
48. Klik icon Filter
49. Verifikasi Filter tetap aktif menyaring: tabel tetap menampilkan 10 baris (8 baris Transaction `Assignment` dan 2 baris Transaction `Borrowing`) dan icon Filter berwarna gelap
50. Verifikasi field `Group` tetap ada di Filter Panel dengan opsi `{group-A}` terpilih
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Klik header kolom Column Visibility (⋯)
54. Centang kembali kolom `Group` pada Overlay Column Visibility

### TC-GS-USER-851: Kombinasi Search + Filter menghasilkan 0 baris lalu pulih saat salah satu dilepas

55. Klik icon Search, ketik `Assignment`, tekan Enter
56. Verifikasi tabel menampilkan 8 baris Transaction `Assignment` (pembanding sebelum Filter yang tidak beririsan)
57. Klik icon Filter
58. Pilih opsi `{group-B}` pada dropdown `Group`
59. Klik `[Apply]`
60. Verifikasi empty filtered state tampil: teks `No results found`
61. Verifikasi empty filtered state tampil: teks `Try adjusting your search or filter.`
62. Klik icon Filter
63. Klik `[Clear Field]`
64. Klik `[Apply]`
65. Verifikasi baris hasil search tampil kembali: 8 baris Transaction `Assignment`
66. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (847, 848, 849, 850, 851) dipertahankan.
- Langkah 1 sampai 3 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama.
- Langkah penghubung (aksi tanpa `Verifikasi`): rangkaian "Klik icon Filter, `[Clear Field]`, `[Apply]`" dan klik `(←)` di akhir tiap blok (langkah 15, 26, 40, dan 66) mengosongkan Filter dan Search sebelum TC berikutnya (S-09); langkah 39 mengembalikan sort `Total Asset` ke netral; langkah 46 dan 54 menyembunyikan dan menampilkan kembali kolom `Group` untuk TC-GS-USER-850; langkah "Klik header `Total Asset`" (28) membentuk Sort aktif untuk TC-GS-USER-849.
- Asersi tambahan (S-03, dengan alasan): langkah 5, 19, 32, 44, dan 56 adalah `Verifikasi` hasil sebelum kontrol berikutnya dan menjadi anchor positif pembanding (bagian 8b butir 2) agar asersi irisan, pelepasan Filter, dan empty filtered state bermakna; langkah 47 memastikan kolom `Group` benar-benar hidden sebelum Filter Panel dibuka (S-14). Pada TC-GS-USER-847 `Verifikasi` baris Transaction `Assignment` dengan Group `{group-A}` tidak tampil memenuhi S-11 (dua nilai distinct pada kolom yang difilter).
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 (screening dan Search) ada di spec 132; TC-GS-USER-837 sampai 846 (Filter Panel) ada di spec 133; TC-GS-USER-852 sampai 854, 869, dan 870 (Sort, Pagination, kombinasi) ada di spec 135; TC-GS-USER-855 sampai 863 ada di spec 136; TC-GS-USER-398 dan 864 sampai 868 ada di spec 137. TC kombinasi sub-tab Pending Approvals ada di spec 128.
- Spec melewati sekitar 35 langkah (66 langkah) karena lima TC kombinasi kontrol tabel berbagi satu layar, satu dataset (PT-22), dan satu kelas harness (fungsional); tiap blok TC berdiri sendiri dan Filter, Search, serta Sort dikembalikan ke netral di antara blok, sehingga satu kegagalan tidak membuat blok lain kehilangan makna. Rangkaian pembukaan Filter Panel dan pembersihan merupakan prefix berulang.
- Temuan untuk QA:
  - TC-GS-USER-847 sampai 851: keyword, field filter, dan kolom sort tidak konkret di TC ("keyword", "terapkan filter", "salah satu kolom"); spec memakai Search `Borrowing`, Filter Group `{group-A}` atau `{group-B}`, dan kolom `Total Asset` dari Population PT-22.
  - TC-GS-USER-849: Expected b ("Filter terlepas") tidak menyatakan cara mengamati; spec mengasersi baris Group `{group-B}` tampil kembali. Expected a mengamati arah sort lewat urutan Total Asset pada halaman 1.
  - TC-GS-USER-850: "kolom tersebut" tidak menyebut kolom; spec memakai `Group`. TC mengasersi filter tetap menyaring walau kolom hidden; karena kolom `Group` hidden, hasil diamati lewat komposisi Transaction pada 10 baris.
  - TC-GS-USER-851: Expected a ("Empty filtered state tampil") tidak menyebut teks; spec memakai teks Expected TC-GS-USER-836 (`No results found` dan `Try adjusting your search or filter.`).
  - TC dan PRD tidak menyatakan apakah Filter Panel menutup setelah `[Apply]`; spec membuka kembali panel dengan klik icon Filter sebelum memakainya lagi. Seeding task pending FAMS tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE.
