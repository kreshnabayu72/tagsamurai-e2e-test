---
id: TC-GS-USER-E2E-031-create-referensi-position-division-custom-field-berubah-sesi-lain
title: "Create: Position/Division/Custom Field dihapus atau di-rename sesi lain sebelum Submit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-153
  - TC-GS-USER-154
  - TC-GS-USER-155
  - TC-GS-USER-156
  - TC-GS-USER-157
coverage:
  web: automated
---

# Create: Position/Division/Custom Field dihapus atau di-rename sesi lain sebelum Submit

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Layar awal: hook `beforeEach` mengembalikan layar ke Global Settings > User > User List, sub-tab Login User.
- Sesi pemicu: perubahan Master Data oleh "tab lain" (TC) dilakukan lewat sesi API akun Total Control yang sama (klien HTTP; token diperoleh dengan kredensial `GS_TC_PASSWORD`, cara disediakan tim FE), karena sesi itu hanya memicu perubahan state dan tidak ada hasil yang diasersi di sesi itu (P-2 butir b tidak diperlukan).
- Data Pre-setup (hanya dibaca): Division `Finance` (No. 23); Position `Staff` (No. 22); opsi Access `Fixed Asset` (No. 26); Custom Field `Blood Type` (Dropdown) dan `Skills` (Multi-Dropdown) dengan opsi `Excel` (No. 24).
- Data Dinamis, seeding lewat API di hook `before` (kemampuan seeding Master Data disediakan tim FE/BE; endpoint tidak disebut TC dan PRD), semua bersuffix `{runId}-031`:
  - Position `Internal Auditor {runId}-031` (TC-GS-USER-153; dihapus oleh sesi pemicu).
  - Division `Legal {runId}-031` (TC-GS-USER-154; dihapus oleh sesi pemicu).
  - Opsi `AB {runId}-031` pada Custom Field Pre-setup `Blood Type` (TC-GS-USER-155; dihapus oleh sesi pemicu).
  - Opsi `SQL {runId}-031` pada Custom Field Pre-setup `Skills` (TC-GS-USER-156; dihapus oleh sesi pemicu). Opsi `Excel` Pre-setup tidak diubah.
  - Position `Supervisor {runId}-031` (TC-GS-USER-157; di-rename oleh sesi pemicu menjadi `Team Supervisor {runId}-031`).
  - Penambahan dan penghapusan opsi pada Custom Field `Blood Type` dan `Skills` mengubah Last Updated kedua Custom Field Pre-setup itu; efek ini disengaja karena opsi Pre-setup `AB` dan `SQL` tidak boleh dihapus (S-06).
- Field form Create yang dipakai tiap TC: First Name `Budi`, Last Name `Santoso {runId}-031`, Email `budisantoso+{runId}-031@qwertysystem.net`, Division `Finance`, Access `Fixed Asset`; Position dan Custom Field sebagaimana disebut di langkah.
- Pesan inline error mengikuti TC dengan nilai bersuffix: `"This position no longer exists. Please select another."`, `"This division no longer exists. Please select another."`, `"This blood type no longer exists. Please select another."`, `"SQL {runId}-031 no longer exists. Please select another."`.
- Kemampuan teknis (disediakan tim FE/BE): sesi API pemicu (menghapus Position, Division, opsi Custom Field; me-rename Position); membaca jumlah user Login pada entitas lewat API (baseline).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API user bersuffix `{runId}-031`, Position `Internal Auditor`/`Supervisor`/`Team Supervisor` bersuffix, Division `Legal` bersuffix, dan opsi `AB {runId}-031` serta `SQL {runId}-031` bila masih ada.
- State global yang diubah: Last Updated Custom Field `Blood Type` dan `Skills` (lihat di atas). Spec membuat data dalam suite serial; form Create dibuka satu kali.

## Test Steps

### Persiapan

1. Catat baseline jumlah user Login pada entitas (lewat API)
2. Klik `[+ User]` di Table Tools
3. Isi First Name `Budi`, Last Name `Santoso {runId}-031`, Division `Finance`, Email `budisantoso+{runId}-031@qwertysystem.net`, centang Access `Fixed Asset`

### TC-GS-USER-153: Position dihapus sesi lain sebelum Submit ditolak di field

4. Pilih Position `Internal Auditor {runId}-031`
5. Hapus Position `Internal Auditor {runId}-031` dari Master Data lewat sesi API
6. Klik `[Submit]`
7. Verifikasi inline error di bawah dropdown Position: "This position no longer exists. Please select another."
8. Verifikasi field Position kosong
9. Klik dropdown Position
10. Verifikasi opsi `Staff` tampil di dropdown Position
11. Verifikasi opsi `Internal Auditor {runId}-031` tidak ada di dropdown Position
12. Klik kembali field Position untuk menutup dropdown
13. Verifikasi field lain tetap terisi: First Name `Budi`, Last Name `Santoso {runId}-031`, Division `Finance`, Email `budisantoso+{runId}-031@qwertysystem.net`, Access `Fixed Asset` tercentang
14. Verifikasi jumlah user Login pada entitas sama dengan baseline (user tidak dibuat)

### TC-GS-USER-154: Division dihapus sesi lain sebelum Submit ditolak di field

15. Pilih Division `Legal {runId}-031`
16. Hapus Division `Legal {runId}-031` dari Master Data lewat sesi API
17. Klik `[Submit]`
18. Verifikasi inline error di bawah dropdown Division: "This division no longer exists. Please select another."
19. Verifikasi field Division kosong
20. Klik dropdown Division
21. Verifikasi opsi `Finance` tampil di dropdown Division
22. Verifikasi opsi `Legal {runId}-031` tidak ada di dropdown Division
23. Klik kembali field Division untuk menutup dropdown
24. Verifikasi field lain tetap terisi: First Name `Budi`, Last Name `Santoso {runId}-031`, Email `budisantoso+{runId}-031@qwertysystem.net`, Access `Fixed Asset` tercentang
25. Verifikasi jumlah user Login pada entitas sama dengan baseline (user tidak dibuat)
26. Pilih Division `Finance`

### TC-GS-USER-155: Custom Field single-select stale ditolak di field

27. Pilih Blood Type `AB {runId}-031`
28. Hapus opsi `AB {runId}-031` pada Custom Field `Blood Type` lewat sesi API
29. Klik `[Submit]`
30. Verifikasi inline error Blood Type: "This blood type no longer exists. Please select another."
31. Verifikasi field Blood Type kosong
32. Verifikasi jumlah user Login pada entitas sama dengan baseline (user tidak dibuat)

### TC-GS-USER-156: Custom Field multi-select dengan satu value stale hanya menghapus chip stale

33. Pilih Skills `Excel` dan `SQL {runId}-031`
34. Hapus opsi `SQL {runId}-031` pada Custom Field `Skills` lewat sesi API
35. Klik `[Submit]`
36. Verifikasi inline error di field Skills: "SQL {runId}-031 no longer exists. Please select another."
37. Verifikasi chip `SQL {runId}-031` hilang dari field Skills
38. Verifikasi chip `Excel` tetap ada di field Skills
39. Verifikasi jumlah user Login pada entitas sama dengan baseline (user tidak dibuat)

### TC-GS-USER-157: Position di-rename sesi lain sebelum Submit tetap sukses

40. Pilih Position `Supervisor {runId}-031`
41. Rename Position `Supervisor {runId}-031` menjadi `Team Supervisor {runId}-031` lewat sesi API
42. Klik `[Submit]`
43. Verifikasi toast sukses: "Success, user has been created."
44. Klik icon Search, ketik `Budi Santoso {runId}-031`, tekan Enter
45. Verifikasi sel Position baris `Budi Santoso {runId}-031`: `Team Supervisor {runId}-031`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (45 langkah) karena seluruh TC berada di satu kelas (referensi Master Data berubah oleh sesi lain), satu layar (Popup Create), dan satu pembukaan form yang dipakai bersama. Tiap blok memakai Master Data seed sendiri bersuffix dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah Verifikasi atas Expected TC (Expected a sampai d pada empat TC pertama).
- Urutan TC sumber dipertahankan (153, 154, 155, 156, 157): empat TC diblokir (tidak ada data tercipta) sebelum TC-GS-USER-157 yang berakhir dengan Submit sukses dan menutup form (bagian 3 prinsip 3 dan 7). Form dibuka sekali dan dipakai berurutan (prinsip 8); tiap TC memilih field referensinya sendiri sesudah blok sebelumnya selesai.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline), 2 sampai 3 (membuka form dan mengisi field wajib bersama yang menjadi langkah 2 dan 3 tiap TC), 12 dan 23 (menutup dropdown dengan klik kembali field; `Esc` tidak dipakai karena `Esc` pada Popup Create memicu dialog Unsaved Changes), 26 (mengisi ulang Division `Finance` karena Division dikosongkan TC-GS-USER-154 dan wajib untuk Submit TC berikutnya), 44 (Search untuk melihat baris di List).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 10 dan 21 (opsi `Staff`/`Finance` tampil) menjadi anchor positif untuk absence opsi stale pada langkah 11 dan 22 (8b butir 2); langkah 14, 25, 32, dan 39 membuktikan "User tidak dibuat" lewat jumlah user terhadap baseline (Expected d TC-GS-USER-153 dan 154, Expected c TC-GS-USER-155 dan 156).
- Perubahan Master Data oleh "tab lain" dilakukan lewat sesi API akun yang sama; perilaku form Create di tab pemicu tidak diasersi.
- Temuan untuk QA:
  - TC-GS-USER-153 sampai 157 memakai Position `Internal Auditor`, `Supervisor`, Division `Legal`, opsi `AB` dan `SQL` Pre-setup sebagai target hapus atau rename. Spec memakai Master Data seed milik spec bersuffix agar data Pre-setup tidak diubah (S-06), sehingga pesan TC-GS-USER-156 memuat nama opsi bersuffix.
  - TC-GS-USER-156 Expected a menyebut pesan `"SQL no longer exists. Please select another."`; nama opsi pada pesan diasumsikan memuat nama opsi apa adanya (dengan suffix pada spec ini).
  - TC-GS-USER-153 sampai 157: Tabel Pre-setup No. 24 menandai Custom Field `Emergency Phone` sebagai Required; langkah TC tidak mengisinya. Spec mengikuti TC; bila field itu wajib, Submit ditolak validasi required sebelum pengecekan referensi stale. Konfigurasi entitas uji disediakan tim FE.
  - TC-GS-USER-153, 154, 155, 156: Expected "opsinya dimuat ulang" (153, 154) tidak menyebut kapan pemuatan ulang terjadi; spec mengasersi isi dropdown sesudah Submit ditolak.
  - TC-GS-USER-155 Expected a memakai nama field "blood type" huruf kecil; spec mengikuti teks TC.
  - TC-GS-USER-153 sampai 157 menyebut "tab lain" tanpa menyebut akun yang bertindak; spec memakai sesi API akun Total Control yang sama.
