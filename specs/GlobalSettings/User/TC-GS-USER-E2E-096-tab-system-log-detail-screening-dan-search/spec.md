---
id: TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search
title: "Tab System Log Detail: Screening, Empty State, dan Search pada Kolom Searchable, Kolom Date, Kolom Hidden, serta No Results"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-407
  - TC-GS-USER-1042
  - TC-GS-USER-591
  - TC-GS-USER-592
  - TC-GS-USER-593
  - TC-GS-USER-594
  - TC-GS-USER-595
  - TC-GS-USER-596
  - TC-GS-USER-597
coverage:
  web: automated
---

# Tab System Log Detail: Screening, Empty State, dan Search pada Kolom Searchable, Kolom Date, Kolom Hidden, serta No Results

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor UI: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 23, 26): hanya dibaca (Position, Division, dan Access dipakai sebagai nilai field user seed). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). System Log memuat aksi yang dilakukan user sebagai aktor (PRD user.md §8.3), sehingga isi log ditentukan oleh aksi milik spec, bukan oleh user Pre-setup. Tiap user diberi Division `Finance` dan Access `Fixed Asset`:
  - Pemilik log `Aktor Log {runId}-096`, email `aktorlog+{runId}-096@qwertysystem.net`, tier Total Control, status Activated, password `Spectra.env.USER_PASSWORD`. Aktivasi akun seed dan sesi API Aktor Log disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut mekanismenya). Seluruh aksi seed di bawah dijalankan lewat sesi API Aktor Log.
  - Target aksi `Target Alfa {runId}-096` (email `targetalfa+{runId}-096@qwertysystem.net`, Position `Staff`) dan `Target Beta {runId}-096` (email `targetbeta+{runId}-096@qwertysystem.net`).
  - Pengguna tanpa aksi `Lukman Hakim {runId}-096` (email `lukmanhakim+{runId}-096@qwertysystem.net`), dibuat oleh akun Siti dan tidak pernah menjalankan aksi (System Log sisi aktor kosong; TC-GS-USER-1042).
  - Aksi seed oleh Aktor Log, berurutan (hanya data yang dipakai `Verifikasi`, S-11): (1) Create `Target Alfa` (Field `Name`, Old Value `—`); (2) Create `Target Beta`; (3) Edit Position `Target Alfa` dari `Staff` menjadi `Supervisor`; (4) Deactivate `Target Alfa` (Field `Status (Global)`, `Active` menjadi `Inactive`); (5) Activate `Target Alfa` (`Inactive` menjadi `Active`); (6) Delete `Target Beta` (Field `Name`, New Value `—`); (7) Assign Total Control ke `Target Alfa` (Object `Total Control`, Field `Access Level`, New Value `Total Control`). Entri ke-7 menjadi entri terbaru. Hasil: kolom Action memuat `Create`, `Edit`, `Deactivate`, `Activate`, `Delete`, `Assign`; kolom Object memuat `User` dan `Total Control`; kolom Name memuat `Target Alfa` dan `Target Beta`; kolom Field memuat `Name`, `Position`, `Status (Global)`, `Access Level` (sedikitnya dua nilai distinct per kolom, S-11).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa` (cabut tier Total Control lebih dulu bila diperlukan), `Target Beta` bila masih ada, `Lukman Hakim`, dan `Aktor Log`; hapus sisa user bersuffix `-096` dari run lama. Entri log tidak bisa dihapus.
- Kemampuan teknis: mengetik di kotak Search; membuka dan menutup overlay Download; menyalin teks sel kolom Date (format yang tampil); mengamati posisi kursor/fokus input.
- State global yang diubah dan dipulihkan: visibilitas kolom `Field` pada tabel System Log (di-hide lalu dicentang kembali pada langkah 82); hook `before` mengosongkan preferensi Setup Column tab ini (tempat penyimpanan preferensi tidak disebut TC User; disediakan tim FE) dan hook `after` memulihkannya sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-407, 1042, 591, 592, 593, 594, 595, 596, 597: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-407: Screening Tab System Log di User Detail

1. Klik icon Search di User List, ketik `Aktor Log {runId}-096`, tekan Enter
2. Klik Name `Aktor Log {runId}-096`
3. Klik Tab `System Log`
4. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`
5. Klik icon Search
6. Verifikasi placeholder Search `Search action, field, or value...`
7. Klik icon panah `(←)` untuk menutup Search
8. Verifikasi toolbar tidak memuat icon Changelog
9. Klik icon Download
10. Verifikasi overlay Download memuat opsi `Download as CSV` dan `Download as XLSX`
11. Tekan Esc untuk menutup overlay Download
12. Verifikasi kolom tabel berurutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, dan Column Visibility (⋯)
13. Verifikasi kolom `Date` berurutan Newest First secara default (baris teratas Action `Assign`, Object `Total Control`)
14. Verifikasi tabel tanpa row action
15. Verifikasi pagination default 10 baris per halaman

### TC-GS-USER-1042: Empty state Tab System Log (user tanpa aksi apa pun)

16. Kembali ke Global Settings > User > User List (sub-tab Login User)
17. Klik icon Search, ketik `Lukman Hakim {runId}-096`, tekan Enter
18. Klik Name `Lukman Hakim {runId}-096`
19. Klik Tab `System Log`
20. Verifikasi empty state tampil: ilustrasi, `No system logs recorded`, dan `Security and audit trail records will appear here.`

### TC-GS-USER-591: Siklus Search: reveal, Enter, clear (✕), collapse ←

21. Kembali ke Global Settings > User > User List (sub-tab Login User)
22. Klik icon Search, ketik `Aktor Log {runId}-096`, tekan Enter
23. Klik Name `Aktor Log {runId}-096`
24. Klik Tab `System Log`
25. Klik icon Search
26. Verifikasi search bar melebar
27. Verifikasi kursor auto-focus pada input Search
28. Ketik `edit` pada input Search
29. Verifikasi tabel belum tersaring (baris Action `Create` masih tampil)
30. Verifikasi icon `(✕)` muncul
31. Tekan Enter
32. Verifikasi baris Action `Edit` tampil
33. Verifikasi tabel tersaring (baris Action `Create` tidak tampil)
34. Klik icon `(✕)`
35. Verifikasi input Search kosong
36. Verifikasi baris Action `Edit` tetap tampil (tabel tetap hasil terakhir)
37. Verifikasi baris Action `Create` tetap tidak tampil (tabel tidak di-reset)
38. Tekan Enter pada input kosong
39. Verifikasi tabel kembali menampilkan semua data (baris Action `Create` tampil kembali)
40. Isi Search dengan `edit`, tekan Enter
41. Klik icon `←`
42. Verifikasi search bar collapse
43. Verifikasi tabel langsung reset (baris Action `Create` tampil)
44. Klik icon Search
45. Verifikasi input Search kosong (keyword tidak tersimpan)

### TC-GS-USER-592: Query Search di-trim dan tidak case-sensitive

46. Isi Search dengan `  EDIT  `, tekan Enter
47. Verifikasi baris Action `Edit` tampil (spasi di awal dan akhir diabaikan, huruf besar/kecil tidak dibedakan)
48. Verifikasi isi search box tetap `  EDIT  ` seperti yang diketik

### TC-GS-USER-593: Search menemukan substring pada kolom kelas teks

49. Ganti isi kotak search dengan `eat`, tekan Enter
50. Verifikasi Action: baris Action `Create` (memuat `eat`) tampil
51. Klik icon `(✕)`
52. Tekan Enter pada input kosong
53. Isi Search dengan `otal`, tekan Enter
54. Verifikasi Object: baris Object `Total Control` (memuat `otal`) tampil
55. Klik icon `(✕)`
56. Tekan Enter pada input kosong
57. Isi Search dengan `lfa`, tekan Enter
58. Verifikasi Name: baris Name `Target Alfa {runId}-096` (memuat `lfa`) tampil
59. Klik icon `(✕)`
60. Tekan Enter pada input kosong
61. Isi Search dengan `osit`, tekan Enter
62. Verifikasi Field: baris Field `Position` (memuat `osit`) tampil
63. Klik icon `(✕)`
64. Tekan Enter pada input kosong

### TC-GS-USER-594: Search menemukan substring pada kolom kelas nilai campuran

65. Isi Search dengan `Staf`, tekan Enter
66. Verifikasi Old Value: baris Old Value `Staff` (memuat `Staf`) tampil
67. Klik icon `(✕)`
68. Tekan Enter pada input kosong
69. Isi Search dengan `Super`, tekan Enter
70. Verifikasi New Value: baris New Value `Supervisor` (memuat `Super`) tampil
71. Klik icon `(✕)`
72. Tekan Enter pada input kosong

### TC-GS-USER-595: Kolom non-searchable tidak tercakup Search

73. Salin teks tanggal pada kolom Date salah satu baris yang tampil (format yang tampil di kolom itu)
74. Isi Search dengan teks tanggal yang disalin, tekan Enter
75. Verifikasi pesan `No results found`
76. Klik icon `(✕)`
77. Tekan Enter pada input kosong

### TC-GS-USER-596: Search tidak mencocokkan kolom yang di-hide, cocok kembali setelah unhide

78. Klik header Column Visibility (⋯), hilangkan centang kolom `Field`
79. Verifikasi kolom `Field` tidak tampil di tabel
80. Isi Search dengan `Position`, tekan Enter
81. Verifikasi pesan `No results found` (kolom `Field` hidden)
82. Klik header Column Visibility (⋯), centang kembali kolom `Field`
83. Verifikasi kolom `Field` tampil kembali di tabel
84. Tekan Enter pada input Search yang masih berisi `Position`
85. Verifikasi baris Field `Position` kembali cocok (tampil)
86. Klik icon `(✕)`
87. Tekan Enter pada input kosong

### TC-GS-USER-597: Empty filtered state

88. Isi Search dengan `zzzqqq`, tekan Enter
89. Verifikasi empty filtered state tampil: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (TC-GS-USER-407) dan `Siti Nurhaliza` (TC-GS-USER-591 sampai 597). System Log menampilkan aksi yang dilakukan user sebagai aktor, sehingga isi log kedua user itu bergantung pada aksi spec lain. Spec memakai user milik spec (`Aktor Log`) dengan aksi seed yang diketahui (S-06, S-11).
- Urutan TC dalam spec: TC-GS-USER-407, 1042, 591, 592, 593, 594, 595, 596, 597 (urutan `sourceTc`). Dua TC screening (407 dan 1042) di awal sesuai bagian 3 konvensi; TC-GS-USER-1042 membuka user lain sehingga membutuhkan satu pembukaan ulang User Detail `Aktor Log` (langkah 21 sampai 24). TC-GS-USER-596 di tengah memakai Column Visibility dan dipulihkan di langkah 82.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1, 17, 22 (mencari user di User List agar Name dapat diklik; daftar dimuat ulang tanpa Search sesudah kembali), langkah 16 dan 21 (kembali ke User List), langkah 51 sampai 52, 55 sampai 56, 59 sampai 60, 63 sampai 64, 67 sampai 68, 71 sampai 72, 76 sampai 77, dan 81 sampai 82 (mengosongkan Search sebagai bagian "lalu clear" TC atau pembersihan sebelum kasus berikutnya). Langkah 44 sampai 45 (membuka Search kembali dan memastikan kosong) adalah observasi tambahan untuk Expected f "keyword kosong" pada TC-GS-USER-591 (S-14).
- Langkah baru di TC-GS-USER-407 (S-03 dan S-09): membuka Search lalu menutupnya dengan `(←)`, membuka overlay Download lalu menutupnya dengan Esc, adalah langkah penghubung tanpa `Verifikasi` untuk mengamati placeholder Search dan opsi Download (Expected a); `Verifikasi toolbar tidak memuat icon Changelog` didahului `Verifikasi` toolbar `Search`, `Filter`, dan `Download` (langkah 4) sebagai anchor (bagian 8b butir 2).
- Langkah 29, 33, 36, 37, 39: TC-GS-USER-591 tidak menyebut cara mengamati "tabel belum tersaring" atau "tabel tersaring"; spec memakai ada atau tidaknya baris Action `Create`. Langkah 32 (baris `Edit` tampil) adalah anchor positif untuk asersi ketiadaan baris `Create` (8b butir 2).
- Asersi memakai pola baris (bukan jumlah baris), sehingga entri log dari run atau spec lain tidak memengaruhi hasil. Kata kunci pada TC-GS-USER-593 dan 594 memakai potongan nilai yang hanya muncul pada kolom yang diuji: `eat` (Action `Create`), `otal` (Object `Total Control`), `lfa` (Name `Target Alfa`), `osit` (Field `Position`), `Staf` (Old Value `Staff`), `Super` (New Value `Supervisor`).
- Spec melewati sekitar 35 langkah (89 langkah) karena sembilan TC memakai permukaan tab yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01), termasuk tujuh kolom searchable dengan satu kata kunci masing-masing. Semua blok satu kelas (screening dan Search pada Tab System Log), satu akun, satu dataset, dan tiap blok berdiri sendiri karena Search dikosongkan di akhir tiap blok.
- Pembagian TC lintas spec: Filter Panel TC-GS-USER-598 sampai 606 diverifikasi di spec 097; kombinasi Search dan Filter TC-GS-USER-607 sampai 611 di spec 098; Sort, Pagination, dan kombinasi TC-GS-USER-612 sampai 614, 629, 630 di spec 099; Setup Column TC-GS-USER-615 sampai 623 di spec 100; Download TC-GS-USER-408 dan 624 sampai 628 di spec 101.
- Temuan untuk QA: (1) TC-GS-USER-407 dan 591 sampai 597 memakai user Pre-setup sebagai pemilik log padahal isi System Log bergantung pada aksi yang dijalankan user itu; spec memakai user milik spec. (2) TC-GS-USER-593 dan 594 menyebut "potongan nilai" tanpa nilai; spec memakai potongan yang tercantum di Notes. (3) TC-GS-USER-595 Data Uji "Nilai tanggal/status sesuai data" menyebut status padahal tabel tidak punya kolom status; spec memakai teks tanggal kolom Date. (4) TC-GS-USER-596 tidak menyebut nilai yang hanya ada di kolom Field; spec memakai `Position`. (5) TC-GS-USER-591 Expected f "keyword kosong" tidak punya langkah observasi di TC; spec mengamatinya lewat membuka Search kembali (langkah 44 sampai 45). (6) TC-GS-USER-1042 menyebut `Lukman Hakim` tanpa suffix; spec memakai nama bersuffix per run. (7) TC-GS-USER-407 Expected a menyebut Download CSV/XLSX tanpa teks opsi; spec memakai `Download as CSV` dan `Download as XLSX` seperti TC-GS-USER-584. (8) TC-GS-USER-1042 dan 597: ilustrasi dan teks empty state adalah satu butir Expected, sehingga masing-masing ditulis satu `Verifikasi` (S-01).
