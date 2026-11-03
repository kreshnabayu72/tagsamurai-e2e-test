---
id: TC-GS-USER-E2E-030-create-limit-master-data-count-stay-on-form-dan-slot-terakhir
title: "Create: Master Data Count Limit, kuota gabungan Login + Non-Login, dan slot terakhir"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-149
  - TC-GS-USER-150
  - TC-GS-USER-151
  - TC-GS-USER-986
coverage:
  web: automated
---

# Create: Master Data Count Limit, kuota gabungan Login + Non-Login, dan slot terakhir

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Kelas harness: e (volume data khusus: Master Data Count Limit). Spec berjalan serial dalam suite (`parallel: false`) dan mengubah state global entitas Client Limit.
- Entitas uji: Client Limit, entitas khusus untuk kuota yang disediakan tim FE (tidak ada di Tabel Data Uji Pre-setup No. 26). Entitas memuat Master Data Division `Finance` dan opsi Access `Fixed Asset`.
- Akun Sesi A (Admin A): Total Control pada entitas Client Limit, disediakan tim FE, kredensial `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login sekali di hook `before` (dibaca dari Prerequisites ini); hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`).
- Akun Sesi B (Admin B, hanya TC-GS-USER-986): Total Control admin kedua pada entitas Client Limit, disediakan tim FE, kredensial `Spectra.env.GS_LIMIT_TC2_PASSWORD`. Sesi B memakai konteks browser kedua (sesi UI) karena hasil di Sesi B (toast sukses atau dialog `Limit Reached`) diasersi; login di langkah eksplisit.
- Env var: `GS_LIMIT_TC_PASSWORD`, `GS_LIMIT_TC2_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` mengembalikan Sesi A ke Global Settings > User > User List, sub-tab Login User pada entitas Client Limit.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut mekanisme dan akunnya):
  - Mengatur Master Data Count Limit entitas Client Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits (lokasi dari TC-GS-USER-149); pelaku dan cara (UI atau API) disediakan tim FE. Nilai awal dicatat dan dipulihkan di hook `after`.
  - Membaca jumlah Login + Non-Login User entitas Client Limit lewat API (disebut `N` di langkah).
  - Membuat 1 Non-Login User lewat API (TC-GS-USER-150 tidak menyebut cara membuatnya).
  - Dua konteks browser dan klik `[Submit]` serentak di kedua sesi (TC-GS-USER-986).
  - Klien HTTP untuk pembacaan API.
- Data Dinamis, semua bersuffix `{runId}-030`, Division `Finance`, Access `Fixed Asset`, Emergency Phone (Required, No. 24) Country Code `🇮🇩 +62` dan Number `81234567890`:
  - NL-150: Non-Login User `Agus Limit {runId}-030` (nilai field wajib Non-Login User disediakan tim FE).
  - U-151a: First Name `Andi`, Last Name `Saputra {runId}-030`, Email `andisaputra+{runId}-030@qwertysystem.net`.
  - U-151b: First Name `Dina`, Last Name `Putri {runId}-030`, Email `dinaputri+{runId}-030@qwertysystem.net`.
  - U-986a (Sesi A): First Name `Candra`, Last Name `Pertama {runId}-030`, Email `candrapertama+{runId}-030@qwertysystem.net`.
  - U-986b (Sesi B): First Name `Dewa`, Last Name `Kedua {runId}-030`, Email `dewakedua+{runId}-030@qwertysystem.net`.
- Cleanup di hook `after` (tidak berasumsi alur berhasil penuh): hapus lewat API seluruh user dan Non-Login User bersuffix `{runId}-030`, pulihkan Master Data Count Limit entitas Client Limit ke nilai awal, tutup konteks browser Sesi B beserta sesi loginnya, kembalikan sesi ke akun default suite.
- Nilai `N` pada tiap blok dibaca ulang sebelum Master Data Count Limit diatur; limit tiap blok dihitung dari `N` blok itu.

## Test Steps

### TC-GS-USER-149: Klik [+ User] saat Master Data Count Limit tercapai memunculkan dialog Limit Reached

1. Baca jumlah Login + Non-Login User entitas Client Limit lewat API sebagai `N1`
2. Atur Master Data Count Limit = `N1`
3. Klik `[+ User]` di Table Tools
4. Verifikasi dialog Title `Limit Reached`
5. Verifikasi body dialog `You've reached the platform limit of {N1} users. Contact support if you need a higher limit.`
6. Verifikasi dialog hanya memiliki tombol tunggal `[OK]`
7. Klik `[OK]`
8. Verifikasi dialog tertutup
9. Verifikasi Popup Create tidak terbuka

### TC-GS-USER-150: Limit gabungan Login + Non-Login, Non-Login User ikut menghabiskan kuota

10. Baca jumlah Login + Non-Login User entitas Client Limit lewat API sebagai `N2`
11. Atur Master Data Count Limit = `N2` + 1
12. Klik sub-tab Non-Login User
13. Buat Non-Login User `Agus Limit {runId}-030` lewat API
14. Klik sub-tab Login User
15. Klik `[+ User]` di Table Tools
16. Verifikasi dialog `Limit Reached` muncul
17. Klik `[OK]`

### TC-GS-USER-151: Create beruntun dengan Stay on this form sampai limit tercapai

18. Baca jumlah Login + Non-Login User entitas Client Limit lewat API sebagai `N3`
19. Atur Master Data Count Limit = `N3` + 1
20. Klik `[+ User]` di Table Tools
21. Centang `Stay on this form after submitting`
22. Isi First Name `Andi`, Last Name `Saputra {runId}-030`, Division `Finance`, Email `andisaputra+{runId}-030@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
23. Klik `[Submit]`
24. Verifikasi toast sukses: "Success, user has been created."
25. Verifikasi form reset ke keadaan awal: First Name, Last Name, Division, Email kosong dan Access (multi dropdown) kosong dan menampilkan placeholder `Select access`
26. Isi First Name `Dina`, Last Name `Putri {runId}-030`, Division `Finance`, Email `dinaputri+{runId}-030@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
27. Klik `[Submit]`
28. Verifikasi dialog `Limit Reached` muncul
29. Klik `[OK]`
30. Verifikasi Popup Create tetap terbuka
31. Verifikasi input dipertahankan: First Name `Dina`, Last Name `Putri {runId}-030`, Division `Finance`, Email `dinaputri+{runId}-030@qwertysystem.net`, Access `Fixed Asset` terpilih
32. Klik `✕`
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`
35. Klik icon Search, ketik `{runId}-030`, tekan Enter
36. Verifikasi baris `Andi Saputra {runId}-030` tampil di User List
37. Verifikasi baris `Dina Putri {runId}-030` tidak ada di User List

### TC-GS-USER-986: Concurrent Create pada slot Master Data Limit terakhir

38. Baca jumlah Login + Non-Login User entitas Client Limit lewat API sebagai `N4`
39. Atur Master Data Count Limit = `N4` + 1
40. [Sesi B] Buka konteks browser kedua, login sebagai Admin B (`Spectra.env.GS_LIMIT_TC2_PASSWORD`)
41. [Sesi B] Klik menu User di sidebar Global Settings
42. [Sesi A] Klik `[+ User]` di Table Tools
43. [Sesi A] Isi First Name `Candra`, Last Name `Pertama {runId}-030`, Division `Finance`, Email `candrapertama+{runId}-030@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
44. [Sesi B] Klik `[+ User]` di Table Tools
45. [Sesi B] Isi First Name `Dewa`, Last Name `Kedua {runId}-030`, Division `Finance`, Email `dewakedua+{runId}-030@qwertysystem.net`, pilih Access `Fixed Asset`, isi Emergency Phone (Country Code `🇮🇩 +62`, Number `81234567890`)
46. [Sesi A] dan [Sesi B] Klik `[Submit]` serentak
47. Verifikasi hanya satu user dibuat: jumlah Login + Non-Login User entitas Client Limit lewat API = `N4` + 1
48. Verifikasi tepat satu sesi menampilkan toast sukses: "Success, user has been created."
49. Verifikasi sesi lainnya menampilkan dialog `Limit Reached`
50. [Sesi yang menampilkan dialog `Limit Reached`] Klik `[OK]`
51. [Sesi yang menampilkan dialog `Limit Reached`] Verifikasi Popup Create tetap terbuka
52. [Sesi yang menampilkan dialog `Limit Reached`] Verifikasi input dipertahankan: First Name, Last Name, Division, Email, dan Access sesuai yang diisi pada sesi itu
53. [Sesi yang menampilkan dialog `Limit Reached`] Klik `✕`
54. [Sesi yang menampilkan dialog `Limit Reached`] Verifikasi dialog `Unsaved Changes` tampil
55. [Sesi yang menampilkan dialog `Limit Reached`] Klik `[Leave]`
56. [Sesi B] Tutup konteks browser kedua dan hapus sesi loginnya

## Notes

- Mode: FE+BE. Kelas harness: e. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (56 langkah) karena seluruh TC berada di satu kelas (kuota Master Data Count Limit), satu layar (Popup Create dari User List), dan satu entitas uji. Tiap blok mengatur limit sendiri dari `N` yang dibaca ulang sehingga berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah pembacaan dan pengaturan limit (langkah 1 sampai 2, 10 sampai 11, 18 sampai 19, 38 sampai 39) adalah persiapan yang berulang.
- P-1 (state berat): TC-GS-USER-986 berada di spec ini walau memakai dua admin (kelas c), karena konteksnya bergantung pada state kuota berat entitas Client Limit (Master Data Count Limit = jumlah user + 1) yang dibangun langkah sebelumnya di spec ini dan dipulihkan di hook `after`; memisahkannya menuntut membangun ulang entitas dengan kuota di ambang batas di spec lain.
- Sesi UI kedua (Sesi B) dipakai karena hasil di Sesi B diasersi (bukan hanya pemicu state). TC-GS-USER-986 balapan: sesi mana yang diproses server lebih dulu tidak ditentukan (Sesi A atau Sesi B) dan spec tidak memaksanya. Karena itu langkah 48 dan 49 mengasersi hasil tanpa menamai sesi pemenang (tepat satu sesi dengan toast sukses, sesi lainnya dengan dialog `Limit Reached`), dan langkah 50 sampai 55 dijalankan pada sesi yang menampilkan dialog `Limit Reached`; tidak ada langkah bersyarat, karena Expected a menjamin tepat satu sesi seperti itu.
- Urutan TC sumber dipertahankan (149, 150, 151, 986); Create yang menghabiskan slot (151 dan 986) berada sesudah TC yang hanya memeriksa dialog.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 sampai 2, 10 sampai 11, 18 sampai 19, 38 sampai 39 (membaca `N` dan mengatur limit), 13 (pembuatan Non-Login User lewat API sebagai pengganti mekanisme yang tidak disebut TC), 17 dan 29 dan 51 (menutup dialog `Limit Reached`), 21 (centang Stay on this form), 32 sampai 34 (menutup form dirty, S-08), 35 (Search), 40 sampai 41 (membuka Sesi B), 53 sampai 55 (menutup form dirty sesi yang menampilkan dialog `Limit Reached`, S-08), 56 (menutup konteks Sesi B, S-09).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 33 dan 54 (dialog `Unsaved Changes`) memenuhi penutupan form dirty yang deterministik (S-08); langkah 36 menjadi anchor positif untuk absence `Dina Putri` pada langkah 37 (8b butir 2).
- Temuan untuk QA:
  - TC-GS-USER-149 precondition c menyebut lokasi System Limits di Admin Console tetapi tidak menyebut akun pelaku dan cara mengaturnya; disediakan tim FE (S-13).
  - TC-GS-USER-149, 150, 151, 986: precondition "System Limits ... jumlah user saat ini (+1)" tidak menyebut apakah Default User dan user Inactive dihitung; spec memakai jumlah Login + Non-Login User yang dibaca dari API.
  - TC-GS-USER-150 langkah 1 "buat 1 Non-Login User" tidak menyebut cara membuat Non-Login User dan nilai field wajibnya; spec membuatnya lewat API (disediakan tim FE/BE).
  - TC-GS-USER-150 Expected hanya dialog `Limit Reached`; judul dan body tidak disebut. Body dialog diasersi di TC-GS-USER-149.
  - TC-GS-USER-151 langkah 4 "Isi user `Dina Putri` (valid)" dan langkah 3 "Andi Saputra (valid)" tidak menyebut nilai field wajib; spec memakai Last Name pembeda bersuffix, Division `Finance`, Access `Fixed Asset`.
  - TC-GS-USER-151 Expected a "form reset" tidak mendaftar field; spec memverifikasi field yang diisi.
  - TC-GS-USER-986: TC tidak menyebut sesi mana yang menang, cara melakukan Submit serentak, dan akun Admin B; spec menetapkan peran dari hasil teramati dan Admin B disediakan tim FE.
  - TC-GS-USER-149 dan 151: TC tidak menyebut apakah halaman perlu dimuat ulang setelah limit diatur; spec tidak memuat ulang halaman.
  - TC-GS-USER-151 dan 986 mengisi Emergency Phone (Required, Pre-setup No. 24) dengan Country Code `🇮🇩 +62` dan Number `81234567890`; spec mengikuti TC. TC-GS-USER-149 dan 150 tidak membuat user.
  - Akun Admin B (Sesi B) memakai admin kedua Client Limit (`GS_LIMIT_TC2_PASSWORD`, `totalControlSecond_automated_qaTeam4@qwertysystem.net`), berbeda dari admin kedua Client A (`GS_TC2_PASSWORD`, spec 018); satu nama env satu arti (R-07).
