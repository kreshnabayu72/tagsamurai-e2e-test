---
id: TC-GS-USER-E2E-092-tab-changelog-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Tab Changelog Detail: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-567
  - TC-GS-USER-568
  - TC-GS-USER-569
  - TC-GS-USER-570
  - TC-GS-USER-571
coverage:
  web: automated
---

# Tab Changelog Detail: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, tampil `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` spec ini; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role Full CRUD (Fajar Nugroho, tampil `Fajar N`) `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4; kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`). Dipakai hanya untuk membuat entri Changelog dengan Modified By kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Data Pre-setup yang dipakai (hanya dibaca, tidak diubah; S-06): Position `Staff`, `Supervisor`, `Finance Manager`, dan `Internal Auditor` (Tabel Data Uji Pre-setup No. 22) dan Client PT Maju Bersama dengan subscription Fixed Asset + Supply Asset (No. 26). John Doe (No. 18) yang disebut TC tidak dipakai: riwayat Changelog-nya tidak dijamin memuat sedikitnya dua nilai distinct pada kolom yang diuji (S-11) dan data Pre-setup tidak diubah (S-06), sehingga spec memakai user uji milik spec.
- Data Dinamis (user uji milik spec, seeding lewat API di hook `before`; kemampuan seeding user lewat API disediakan tim FE/BE, endpoint tidak disebut di TC dan PRD):
  - User uji: Name `Log User {runId}-092`, Email `loguser+{runId}-092@qwertysystem.net`, Position `Staff`, Employee ID `{empId1}`, Access `Fixed Asset`, Active. `{empId1}`, `{empId2}`, `{empId3}` adalah tiga Employee ID numerik murni, naik berurutan (`{empId1}` < `{empId2}` < `{empId3}`), unik per run, dibuat hook dari waktu run (tanpa suffix `{runId}` karena nilainya harus numerik murni).
  - Entri Changelog base (12 entri, urutan seeding = urutan waktu, dari terlama ke terbaru; Modified By tampil `[First Name] [Last Initial]`):
    - a. `Create` | `Name` | `—` | `Log User {runId}-092` | `Siti N`
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
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user uji `Log User {runId}-092` lewat API. Entri Changelog tidak bisa dihapus.
- Precondition TC-GS-USER-567, 568, 569, 570, 571: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tersedia; user uji punya riwayat Changelog.
- Suite serial (`parallel: false`) karena spec membaca dan mengubah konfigurasi kolom Tab Changelog di browser yang sama dengan spec lain.
- State global yang diubah dan dipulihkan: tidak ada yang bertahan; visibilitas kolom yang diubah di dalam spec dikembalikan lewat langkah, dan hook `after` memulihkan konfigurasi kolom Tab Changelog ke nilai awal sebagai cadangan.

## Test Steps

### TC-GS-USER-567: Search lalu Filter menghasilkan irisan

1. Klik icon Search di User List, ketik `Log User {runId}-092`, tekan Enter
2. Klik Name `Log User {runId}-092` di User List
3. Klik Tab `Changelog`
4. Klik icon Search, ketik `edit`, tekan Enter
5. Verifikasi baris Action `Edit` dengan Modified By `Siti N` (Field `Employee ID`) tampil
6. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, lalu klik `[Apply]`
7. Verifikasi tabel hanya memuat baris Action `Edit` dengan Modified By `Fajar N` (irisan Search dan Filter)
8. Verifikasi baris Action `Edit` dengan Modified By `Siti N` (Field `Employee ID`) tidak tampil
9. Verifikasi keyword tidak ter-reset (input Search berisi `edit`)
10. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
11. Klik icon ×, lalu tekan Enter pada input kosong

### TC-GS-USER-568: Filter lalu Search menghasilkan irisan

12. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, lalu klik `[Apply]`
13. Verifikasi baris Field `Employee ID` dengan Modified By `Fajar N` tampil
14. Isi Search dengan `position`, tekan Enter
15. Verifikasi tabel hanya memuat baris Field `Position` dengan Modified By `Fajar N` (irisan Filter dan Search)
16. Verifikasi baris Field `Employee ID` dengan Modified By `Fajar N` tidak tampil
17. Verifikasi filter tetap aktif (icon Filter berubah gelap)
18. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
19. Klik icon ×, lalu tekan Enter pada input kosong

### TC-GS-USER-569: Clear filter saat Search dan Sort aktif

20. Isi Search dengan `edit`, tekan Enter
21. Klik header Modified By sekali (A-Z)
22. Klik icon Filter, pilih opsi `Position` pada Field, lalu klik `[Apply]`
23. Verifikasi tabel hanya memuat baris Field `Position`
24. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
25. Verifikasi keyword tetap aktif (input Search berisi `edit`)
26. Verifikasi arah sort tetap aktif (Modified By A-Z: baris pertama Modified By `Fajar N`)
27. Verifikasi filter terlepas (baris Field `Employee ID` tampil kembali)
28. Klik header Modified By dua kali sampai sort kembali ke default
29. Klik icon ×, lalu tekan Enter pada input kosong

### TC-GS-USER-570: Filter tetap tersedia untuk kolom yang di-hide

30. Verifikasi baris Action `Add Access` tampil
31. Klik icon Filter, pilih opsi `Fajar N` pada Modified By, lalu klik `[Apply]`
32. Klik header kolom Column Visibility (⋯), hilangkan centang `Modified By`, lalu tutup overlay
33. Verifikasi kolom `Modified By` tidak tampil
34. Verifikasi filter tetap aktif menyaring (baris Action `Add Access` tidak tampil)
35. Klik icon Filter
36. Verifikasi field `Modified By` tetap ada di Filter Panel
37. Klik `[Clear Field]`, lalu klik `[Apply]`
38. Klik header kolom Column Visibility (⋯), centang kembali `Modified By`, lalu tutup overlay

### TC-GS-USER-571: Kombinasi Search + Filter menghasilkan 0 baris lalu pulih saat salah satu dilepas

39. Isi Search dengan `deactivate`, tekan Enter
40. Verifikasi baris Action `Deactivate` tampil
41. Klik icon Filter, pilih opsi `Create` pada Action, lalu klik `[Apply]`
42. Verifikasi empty filtered state tampil: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
43. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
44. Verifikasi baris hasil search tampil kembali (baris Action `Deactivate` tampil)
45. Klik icon ×, lalu tekan Enter pada input kosong

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (567, 568, 569, 570, 571). TC-GS-USER-570 mengubah visibilitas kolom dan dikembalikan di langkah terakhir blok itu sebelum TC-GS-USER-571. Detail user dan Tab `Changelog` dibuka sekali di langkah 1 sampai 3.
- Langkah 1 sampai 3 (mencari user uji lewat Search User List, lalu klik Name dan Tab `Changelog`) adalah langkah penghubung tanpa `Verifikasi`; TC menulis "Klik Name `John Doe`" tanpa cara menemukan baris, dan user uji milik spec menggantikan John Doe (lihat Prerequisites).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): "Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`" dan "Klik icon ×, lalu tekan Enter pada input kosong" di akhir TC-GS-USER-567 dan 568 serta "Klik icon ×, lalu tekan Enter pada input kosong" di akhir TC-GS-USER-569 dan 571 membersihkan filter dan Search antar-TC; klik header Modified By dua kali di TC-GS-USER-569 mengembalikan sort ke default; menyembunyikan (langkah 32) dan menampilkan kembali `Modified By` pada TC-GS-USER-570 lewat overlay Column Visibility tanpa Save. Pembersihan filter di langkah 24 adalah langkah TC-GS-USER-569 ("`[Clear Field]` + `[Apply]`").
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` baris pembanding sebelum dan sesudah penerapan (baris `Employee ID` oleh `Siti N`, baris `Employee ID` oleh `Fajar N`, baris `Add Access`, baris `Deactivate`) membuktikan irisan dan pelepasan nyata (bagian 8b butir 2). Entri yang dipakai berada di halaman 1 (10 entri terbaru) kecuali bila disebut lain.
- Pembagian TC Tab Changelog di User Detail: kombinasi Search dan Filter di spec 092; Search di spec 090; Filter Panel di spec 091; kombinasi dengan Sort dan Pagination (TC-GS-USER-590) di spec 093.
- Spec melewati sekitar 35 langkah (45 langkah) karena lima TC memakai Search dan Filter Tab Changelog pada dataset dan layar yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); semua blok satu kelas harness (kombinasi Search dan Filter Tab Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena Search dan filter dibersihkan di akhir tiap blok.
- Temuan untuk QA: (1) Cap waktu entri Changelog (entri `Create` H-2, jarak sedikitnya 1 menit antar entri) tidak punya cara di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE (S-13). (2) Label Field Changelog untuk perubahan Employee ID tidak disebut eksplisit (PRD user.md §8.3 hanya menulis `[Field]`); spec memakai `Employee ID`. (3) TC-GS-USER-567 sampai 571 menulis "Search keyword", "Terapkan filter", dan "Filter yang tidak beririsan" tanpa nilai; spec memakai `edit` dan Modified By `Fajar N` (567), Modified By `Fajar N` dan `position` (568), `edit` dan Field `Position` (569), Modified By `Fajar N` (570), `deactivate` dan Action `Create` (571). (4) TC-GS-USER-569 tidak menyebut kolom sort; spec memakai Modified By. (5) TC-GS-USER-570 "Hide kolom via Column Visibility" tidak menyebut apakah overlay menerapkan seketika; spec memakai overlay tanpa Save (prd-conventions.md §9.3). (6) TC-GS-USER-568 Expected b "Filter tetap aktif" tidak menyebut cara mengamati; spec mengasersi state aktif icon Filter. (7) TC-GS-USER-571 Expected a tidak menyebut teks empty filtered state; spec memakai teks dari TC-GS-USER-557.

