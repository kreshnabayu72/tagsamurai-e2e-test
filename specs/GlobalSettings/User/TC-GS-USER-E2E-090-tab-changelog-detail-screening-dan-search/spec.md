---
id: TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search
title: "Tab Changelog Detail: Screening, State Kosong, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-405
  - TC-GS-USER-551
  - TC-GS-USER-552
  - TC-GS-USER-553
  - TC-GS-USER-554
  - TC-GS-USER-555
  - TC-GS-USER-557
  - TC-GS-USER-556
coverage:
  web: automated
---

# Tab Changelog Detail: Screening, State Kosong, dan Search

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, tampil `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` spec ini; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role Full CRUD (Fajar Nugroho, tampil `Fajar N`) `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4; kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`). Dipakai hanya untuk membuat entri Changelog dengan Modified By kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Data Pre-setup yang dipakai (hanya dibaca, tidak diubah; S-06): Position `Staff`, `Supervisor`, `Finance Manager`, dan `Internal Auditor` (Tabel Data Uji Pre-setup No. 22) dan Client PT Maju Bersama dengan subscription Fixed Asset + Supply Asset (No. 26). John Doe (No. 18) yang disebut TC tidak dipakai: riwayat Changelog-nya tidak dijamin memuat sedikitnya dua nilai distinct pada kolom yang diuji (S-11) dan data Pre-setup tidak diubah (S-06), sehingga spec memakai user uji milik spec.
- Data Dinamis (user uji milik spec, seeding lewat API di hook `before`; kemampuan seeding user lewat API disediakan tim FE/BE, endpoint tidak disebut di TC dan PRD):
  - User uji: Name `Log User {runId}-090`, Email `loguser+{runId}-090@qwertysystem.net`, Position `Staff`, Employee ID `{empId1}`, Access `Fixed Asset`, Active. `{empId1}`, `{empId2}`, `{empId3}` adalah tiga Employee ID numerik murni, naik berurutan (`{empId1}` < `{empId2}` < `{empId3}`), unik per run, dibuat hook dari waktu run (tanpa suffix `{runId}` karena nilainya harus numerik murni).
  - Entri Changelog base (12 entri, urutan seeding = urutan waktu, dari terlama ke terbaru; Modified By tampil `[First Name] [Last Initial]`):
    - a. `Create` | `Name` | `—` | `Log User {runId}-090` | `Siti N`
    - b. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - c. `Edit` | `Employee ID` | `{empId1}` | `{empId2}` | `Siti N`
    - d. `Deactivate` | `Status (Global)` | `Active` | `Inactive` | `Siti N`
    - e. `Activate` | `Status (Global)` | `Inactive` | `Active` | `Siti N`
    - f. `Add Access` | `App Access` | `—` | `Supply Asset` | `Siti N`
    - g. `Remove Access` | `App Access` | `Supply Asset` | `—` | `Siti N`
    - h. `Edit` | `Position` | `Supervisor` | `Finance Manager` | `Fajar N`
    - i. `Edit` | `Position` | `Finance Manager` | `Staff` | `Fajar N`
    - j. `Edit` | `Employee ID` | `{empId2}` | `{empId3}` | `Fajar N`
    - k. `Edit` | `Position` | `Staff` | `Internal Auditor` | `Fajar N`
    - l. `Edit` | `Position` | `Internal Auditor` | `Supervisor` | `Fajar N`
  - Pelaku entri: `Siti N` lewat sesi API Total Control, `Fajar N` lewat sesi API Fajar Nugroho. Dengan demikian kolom Modified By memuat dua nilai distinct (`Siti N`, `Fajar N`); kolom Action, Field, Old Value, dan New Value memuat sedikitnya dua nilai distinct (S-11).
- Kemampuan teknis yang disediakan tim FE/BE (TC, PRD, dan LLD tidak memberi cara): memberi cap waktu pada entri seed sehingga setiap entri berjarak sedikitnya 1 menit dari entri sebelumnya mengikuti urutan huruf di atas, dan entri a (`Create`) bercap tanggal hari uji dikurangi 2 hari (H-2) sedangkan entri lain bercap hari uji. Cap waktu ini membuat urutan Date deterministik (entri terbaru di atas) dan memberi dua nilai distinct pada kolom Date.
- Kemampuan teknis: klik header kolom dan icon di toolbar tabel; mengetik di kotak Search dan dropdown Filter; menyalin teks sel.
- Konfigurasi kolom Tab Changelog akun Total Control dalam keadaan default (6 kolom tampil, tanpa pin) saat spec dimulai; hook `before` mengosongkan konfigurasi kolom Tab Changelog bila perlu (mekanisme disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user uji `Log User {runId}-090` lewat API. Entri Changelog tidak bisa dihapus.
- Precondition TC-GS-USER-405, 551, 552, 553, 554, 555, 556, 557: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tersedia; user uji punya riwayat Changelog.
- Suite serial (`parallel: false`) karena spec membaca dan mengubah konfigurasi kolom Tab Changelog di browser yang sama dengan spec lain.
- State global yang diubah dan dipulihkan: tidak ada yang bertahan; visibilitas kolom yang diubah di dalam spec dikembalikan lewat langkah, dan hook `after` memulihkan konfigurasi kolom Tab Changelog ke nilai awal sebagai cadangan.

## Test Steps

### TC-GS-USER-405: Screening Tab Changelog di User Detail

1. Klik icon Search di User List, ketik `Log User {runId}-090`, tekan Enter
2. Klik Name `Log User {runId}-090` di User List
3. Klik Tab `Changelog`
4. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`
5. Verifikasi kolom tabel berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`, dan Column Visibility (⋯)
6. Verifikasi tabel tidak memiliki kolom `Name` dan `Object`
7. Verifikasi Date default Newest First: baris pertama adalah entri terbaru (Action `Edit`, Field `Position`, Old Value `Internal Auditor`, New Value `Supervisor`, Modified By `Fajar N`)
8. Verifikasi baris tabel tidak memiliki row action
9. Verifikasi pagination default 10 baris per halaman (halaman 1 memuat 10 baris)

### TC-GS-USER-551: Siklus Search: reveal, Enter, clear ×, collapse ←

10. Klik icon Search
11. Verifikasi input Search melebar
12. Verifikasi kursor auto-focus pada input Search
13. Ketik `deactivate` pada input Search
14. Verifikasi tabel belum tersaring (baris Action `Add Access` masih tampil)
15. Verifikasi icon × muncul
16. Tekan Enter
17. Verifikasi baris Action `Deactivate` tampil
18. Verifikasi tabel tersaring (baris Action `Add Access` tidak tampil)
19. Klik icon ×
20. Verifikasi input Search kosong
21. Verifikasi tabel tetap hasil terakhir (baris Action `Deactivate` tampil)
22. Verifikasi tabel tetap hasil terakhir (baris Action `Add Access` tidak tampil)
23. Tekan Enter pada input kosong
24. Verifikasi tabel kembali menampilkan semua data (baris Action `Add Access` tampil kembali)
25. Isi Search dengan `deactivate`, tekan Enter
26. Klik icon ←
27. Verifikasi search collapse
28. Verifikasi tabel langsung reset (baris Action `Add Access` tampil kembali)
29. Klik icon Search
30. Verifikasi keyword kosong (input Search tidak berisi `deactivate`)

### TC-GS-USER-552: Query Search di-trim dan tidak case-sensitive

31. Isi Search dengan `  EDIT  ` (dua spasi di awal dan akhir), tekan Enter
32. Verifikasi baris Action `Edit` tampil
33. Verifikasi baris Action `Add Access` tidak tampil
34. Verifikasi isi search box tetap `  EDIT  ` apa adanya

### TC-GS-USER-553: Search menemukan substring pada kolom kelas teks

35. Ganti isi kotak search dengan `deact`, tekan Enter
36. Verifikasi kolom Action: baris dengan Action `Deactivate` tampil
37. Verifikasi baris Action `Add Access` tidak tampil
38. Klik icon ×, lalu tekan Enter pada input kosong
39. Isi Search dengan `emplo`, tekan Enter
40. Verifikasi kolom Field: baris dengan Field `Employee ID` tampil
41. Verifikasi baris Action `Add Access` tidak tampil
42. Klik icon ×, lalu tekan Enter pada input kosong
43. Isi Search dengan `fajar`, tekan Enter
44. Verifikasi kolom Modified By: baris dengan Modified By `Fajar N` tampil
45. Verifikasi baris Action `Add Access` (Modified By `Siti N`) tidak tampil
46. Klik icon ×, lalu tekan Enter pada input kosong

### TC-GS-USER-554: Search menemukan substring pada kolom kelas nilai campuran

47. Isi Search dengan `Staff`, tekan Enter
48. Verifikasi kolom Old Value: baris dengan Old Value `Staff` tampil
49. Verifikasi baris Action `Add Access` tidak tampil
50. Klik icon ×, lalu tekan Enter pada input kosong
51. Isi Search dengan `Supply`, tekan Enter
52. Verifikasi kolom New Value: baris dengan New Value `Supply Asset` tampil
53. Verifikasi baris Action `Activate` tidak tampil
54. Klik icon ×, lalu tekan Enter pada input kosong

### TC-GS-USER-555: Kolom non-searchable tidak tercakup Search

55. Verifikasi baris tabel tampil (baris Action `Add Access` tampil)
56. Salin teks tanggal pada kolom Date baris pertama (format yang tampil di kolom itu)
57. Isi Search dengan teks tanggal yang disalin, tekan Enter
58. Verifikasi kolom Date: keyword tidak mencocokkan baris (no result state: `No results found`)

### TC-GS-USER-557: Empty filtered state

59. Ganti isi kotak search dengan `zzzqqq`, tekan Enter
60. Verifikasi empty filtered state tampil: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
61. Klik icon ×, lalu tekan Enter pada input kosong

### TC-GS-USER-556: Search tidak mencocokkan kolom yang di-hide, kembali cocok setelah unhide

62. Klik header kolom Column Visibility (⋯), hilangkan centang `Modified By`, lalu tutup overlay
63. Verifikasi kolom `Modified By` tidak tampil
64. Verifikasi baris Action `Add Access` tampil
65. Isi Search dengan `fajar`, tekan Enter
66. Verifikasi saat kolom hidden: no result state (`No results found`)
67. Klik header kolom Column Visibility (⋯), centang kembali `Modified By`, lalu tutup overlay
68. Verifikasi kolom `Modified By` tampil kembali
69. Tekan Enter lagi pada input Search
70. Verifikasi setelah unhide: baris dengan Modified By `Fajar N` tampil
71. Klik icon ×, lalu tekan Enter pada input kosong

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-405, 551, 552, 553, 554, 555, 557, 556. Alasan: TC-GS-USER-405 hanya mengamati (screening di awal, bagian 3 konvensi); TC-GS-USER-557 sebelum TC-GS-USER-556 karena TC-GS-USER-556 mengubah visibilitas kolom dan ditaruh paling akhir supaya TC lain memakai 6 kolom tampil. Detail user dan Tab `Changelog` dibuka sekali di langkah 1 sampai 3 untuk kedelapan TC.
- Langkah 1 sampai 3 (mencari user uji lewat Search User List, lalu klik Name dan Tab `Changelog`) adalah langkah penghubung tanpa `Verifikasi`; TC menulis "Klik Name `John Doe`" tanpa cara menemukan baris, dan user uji milik spec menggantikan John Doe (lihat Prerequisites).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): membersihkan Search (Klik icon ×, lalu Enter pada input kosong) setelah tiap kata kunci TC-GS-USER-553, 554, 557, dan 556 supaya kata kunci berikutnya mulai dari tabel penuh; langkah 29 membuka kembali Search yang ditutup ← di TC-GS-USER-551 (langkah berikutnya memeriksa keyword kosong); langkah 62 dan 67 menyembunyikan lalu menampilkan kembali `Modified By` lewat overlay Column Visibility tanpa Save.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` baris Action `Add Access` tampil/tidak tampil adalah anchor untuk "belum tersaring" dan "tersaring" (bagian 8b butir 2); pada TC-GS-USER-553 dan 554 satu `Verifikasi` ketiadaan baris `Add Access` atau `Activate` membuktikan penyaringan nyata, bukan sekadar baris cocok tampil. Baris `Add Access` (entri f) berada di halaman 1 (10 entri terbaru) sehingga dapat diamati tanpa pindah halaman; entri `Create` (entri a) berada di halaman 2.
- Pembagian TC Tab Changelog di User Detail: Search di spec 090; Filter Panel di spec 091; kombinasi Search dan Filter di spec 092; Sort dan Pagination di spec 093; Setup Column di spec 094; Download di spec 095. TC-GS-USER-405 diverifikasi di spec 090.
- Spec melewati sekitar 35 langkah (71 langkah) karena delapan TC memakai Search Tab Changelog pada dataset dan layar yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); semua blok satu kelas harness (screening dan Search Tab Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena Search dibersihkan di akhir tiap blok.
- Temuan untuk QA: (1) Cap waktu entri Changelog (entri `Create` H-2, jarak sedikitnya 1 menit antar entri) tidak punya cara di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE (S-13). (2) Label Field Changelog untuk perubahan Employee ID tidak disebut eksplisit (PRD user.md §8.3 hanya menulis `[Field]`); spec memakai `Employee ID`. (3) TC-GS-USER-551 Expected b dan d tidak menyebut cara mengamati "tabel belum tersaring" dan "tabel tetap hasil terakhir"; spec memakai ada atau tidaknya baris Action `Add Access`. (4) TC-GS-USER-552 Expected a "baris yang memuat `Edit`" tidak menyebut kolom; spec mengasersi baris Action `Edit`. (5) TC-GS-USER-555 Data Uji menyebut "tanggal/status" padahal Tab Changelog tidak punya kolom status; spec memakai teks kolom Date. (6) TC-GS-USER-556 "Hide kolom via Column Visibility" tidak menyebut apakah overlay menerapkan seketika; spec memakai overlay Column Visibility tanpa Save (prd-conventions.md §9.3). (7) TC-GS-USER-551 Expected f "keyword kosong" tidak menyebut cara mengamati; spec membuka kembali Search dan memeriksa input kosong.

