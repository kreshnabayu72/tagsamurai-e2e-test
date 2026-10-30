---
id: TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed
title: "Edit Position Sukses: Rename, Kapitalisasi, No-Op (Last Updated Tetap), Nama 1 dan 120 Karakter, dan Record Seed"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-79
  - TC-GS-POS-89
  - TC-GS-POS-90
  - TC-GS-POS-91
  - TC-GS-POS-92
  - TC-GS-POS-110
  - TC-GS-POS-283
  - TC-GS-POS-287
coverage:
  web: automated
---

# Edit Position Sukses: Rename, Kapitalisasi, No-Op (Last Updated Tetap), Nama 1 dan 120 Karakter, dan Record Seed

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec mengubah nama record seed `Head of Operations` di entitas `Client Seed` (dipulihkan di hook `after`) dan men-seed Position bernama 1 karakter literal (`Y`) tanpa suffix, sehingga tidak berjalan bersamaan dengan spec lain pada entitas yang sama.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; langkah 1 tidak mengulang pembukaan layar.
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) untuk TC-GS-POS-91, 92, 79, 89, 90, dan 283. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control entitas `Client Seed` (Pre-setup 21) untuk TC-GS-POS-287 dan 110: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTSEED_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA).
  - Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite.
- Data Pre-setup (tanpa suffix):
  - Entitas `Client Seed` (Pre-setup 21) diprovisioning dengan Position Default User `Head of Operations` dan memiliki record manual non-seed `Shift Leader`. `Shift Leader` hanya dibaca oleh TC-GS-POS-287 (overlay Row Action dibuka lalu ditutup) dan tidak diubah spec ini.
  - Record `Head of Operations` diubah namanya oleh TC-GS-POS-110 (target tidak bisa diganti dengan data milik spec, karena objek uji adalah record hasil seed provisioning) dan dipulihkan di hook `after` (lihat Cleanup). Efek yang tidak bisa dipulihkan: Last Updated record dan entri Changelog/Activity Log Client Seed bertambah.
- Data Dinamis (di-seed lewat API di hook `before`; fixture baru `Fixture.position.editSeed019`):
  - Entitas utama: `iOS Developer {runId}-019` (diubah menjadi nama 120 karakter), `IT Support Specialist {runId}-019` (diubah menjadi `IT Operations Lead {runId}-019`), `Data Engineer {runId}-019` (diubah menjadi `Data engineer {runId}-019`), dan `Legal Counsel {runId}-019` (No-Op, nama tidak berubah).
  - Nama 120 karakter TC-GS-POS-79: diawali teks Data Uji TC-GS-POS-79 (`Senior Manager of Regional Supply Chain Planning, Procurement Strategy, Vendor Performance and Logistics Cost Programss...`) dan dipotong dari belakang sehingga panjang total termasuk suffix ` {runId}-019` tepat 120 karakter (fixture `editSeed019` menghitung potongan dari panjang `{runId}` aktual).
  - `Y` (diubah menjadi `Z`) untuk TC-GS-POS-283. Nama 1 karakter ditulis literal (nilai TC `Q` dan `R` diganti `Y` dan `Z`, lihat Notes) tanpa suffix karena suffix mengubah objek uji (batas 1 karakter); di-seed idempotent di `before` (dilewati bila sudah ada).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh), dua butir terpisah per entitas:
  - Entitas `Client Seed`: bila `Operations Director {runId}-019` ada, kembalikan namanya menjadi `Head of Operations` (record seed dipulihkan, tidak dihapus).
  - Entitas Total Control: hapus lewat API semua Position bersuffix `{runId}-019` yang masih ada (`Legal Counsel`, `iOS Developer` atau nama 120 karakter, `IT Support Specialist` atau `IT Operations Lead`, `Data Engineer` atau `Data engineer`), serta `Y` dan `Z` bila dibuat spec ini.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control dan Total Control `Client Seed`) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: membaca kolom Last Updated tabel; membaca jam klien sesudah `[Save]` diklik, dengan jam server dan jam browser sinkron; jeda debounce ±500 ms (jeda pendek, ditunggu nyata); ganti akun (logout lalu login); membaca opsi Overlay Row Action.
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite), nama record seed `Head of Operations` (dipulihkan, lihat Cleanup), dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### Persiapan tabel

1. Ketik Search `{runId}-019`, tekan Enter

### TC-GS-POS-91: Save tanpa perubahan nilai (No-Op)

2. Catat nilai Last Updated baris `Legal Counsel {runId}-019`
3. Klik `⋯` pada baris `Legal Counsel {runId}-019`, pilih `Edit`
4. Verifikasi Popup Edit Position terbuka
5. Tanpa mengubah apa pun, klik `[Save]`
6. Verifikasi tidak ada error "Position Name already exists"
7. Verifikasi tidak ada dialog Unsaved Changes
8. Verifikasi tidak ada toast "Success, position has been updated."
9. Verifikasi toast "No changes to save."
10. Verifikasi toast tersebut bersifat netral (info)
11. Verifikasi Popup Edit tertutup otomatis
12. Verifikasi spinner berhenti
13. Verifikasi Last Updated baris `Legal Counsel {runId}-019` sama dengan nilai yang dicatat pada langkah 2

### TC-GS-POS-92: Hanya menambah spasi depan dan belakang dihitung No-Op

14. Klik `⋯` pada baris `Legal Counsel {runId}-019`, pilih `Edit`
15. Verifikasi Popup Edit Position terbuka
16. Ganti nilai Position Name dengan `  Legal Counsel {runId}-019  `
17. Klik `[Save]`
18. Verifikasi toast netral "No changes to save."
19. Verifikasi Popup Edit tertutup
20. Verifikasi baris tetap `Legal Counsel {runId}-019`

### TC-GS-POS-79: Position Name tepat 120 karakter diterima

21. Klik `⋯` pada baris `iOS Developer {runId}-019`, pilih `Edit`
22. Verifikasi Popup Edit Position terbuka
23. Ganti nilai Position Name dengan nama 120 karakter (diakhiri ` {runId}-019`)
24. Verifikasi tidak ada error "Max. 120 characters"
25. Klik `[Save]`
26. Verifikasi toast sukses "Success, position has been updated."

### TC-GS-POS-89: Ganti nama

27. Klik `⋯` pada baris `IT Support Specialist {runId}-019`, pilih `Edit`
28. Verifikasi Popup Edit Position terbuka
29. Ganti nilai Position Name menjadi `IT Operations Lead {runId}-019`
30. Klik `[Save]`
31. Catat waktu sesudah `[Save]` diklik (jam klien)
32. Verifikasi toast sukses "Success, position has been updated."
33. Verifikasi Popup Edit tertutup
34. Verifikasi baris tampil sebagai `IT Operations Lead {runId}-019`
35. Verifikasi baris `IT Operations Lead {runId}-019` berada pada posisi urutan baru sesuai urutan A-Z di tabel tersaring
36. Verifikasi Last Updated baris `IT Operations Lead {runId}-019` sama dengan waktu yang dicatat pada langkah 31 (toleransi satu menit)

### TC-GS-POS-90: Perubahan kapitalisasi saja dihitung perubahan

37. Klik `⋯` pada baris `Data Engineer {runId}-019`, pilih `Edit`
38. Verifikasi Popup Edit Position terbuka
39. Ganti nilai Position Name menjadi `Data engineer {runId}-019`, tunggu ±500 ms
40. Verifikasi tidak ada error "Position Name already exists"
41. Klik `[Save]`
42. Verifikasi tidak ada toast "No changes to save."
43. Verifikasi toast sukses "Success, position has been updated."
44. Verifikasi baris tampil sebagai `Data engineer {runId}-019`

### TC-GS-POS-283: Position Name 1 karakter diterima

45. Ganti isi kotak search dengan `Y`, tekan Enter
46. Klik `⋯` pada baris `Y`, pilih `Edit`
47. Verifikasi Popup Edit Position terbuka
48. Ganti nilai Position Name menjadi `Z`
49. Klik `[Save]`
50. Verifikasi toast sukses "Success, position has been updated."
51. Ganti isi kotak search dengan `Z`, tekan Enter
52. Verifikasi baris tampil `Z`
53. Klik `(←)` pada kotak Search

### Ganti akun ke Client Seed

54. Logout dari akun Total Control
55. Login sebagai Total Control entitas `Client Seed` dengan `Spectra.env.GS_CLIENTSEED_TC_PASSWORD`

### TC-GS-POS-287: Row action Edit dan Delete sama untuk record seed dan record biasa

56. Buka Global Settings > User > Position
57. Ketik Search `Head of Operations`, tekan Enter
58. Klik `⋯` pada baris `Head of Operations`
59. Verifikasi Overlay Row Action berisi opsi `Edit` dan `Delete`
60. Verifikasi tidak ada opsi yang disembunyikan untuk record seed
61. Tutup Overlay Row Action
62. Ganti isi kotak search dengan `Shift Leader`, tekan Enter
63. Klik `⋯` pada baris `Shift Leader`
64. Verifikasi Overlay Row Action berisi opsi `Edit` dan `Delete`
65. Verifikasi opsi pada overlay `Shift Leader` sama dengan opsi pada overlay `Head of Operations`
66. Tutup Overlay Row Action

### TC-GS-POS-110: Edit record Position hasil seed provisioning

67. Ganti isi kotak search dengan `Head of Operations`, tekan Enter
68. Klik `⋯` pada baris `Head of Operations`, pilih `Edit`
69. Verifikasi Popup Edit Position terbuka
70. Ganti nilai Position Name menjadi `Operations Director {runId}-019`
71. Klik `[Save]`
72. Verifikasi toast sukses "Success, position has been updated."
73. Ganti isi kotak search dengan `Operations Director {runId}-019`, tekan Enter
74. Verifikasi baris tampil sebagai `Operations Director {runId}-019`
75. Verifikasi tidak ada penanda record terkunci pada baris tersebut
76. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 91, 92, 79, 89, 90, 283, 287, 110. No-Op (TC-GS-POS-91 dan 92) tidak mengubah data sehingga ditaruh pertama; kasus sukses mengubah data milik spec; bagian Client Seed (setelah ganti akun) memakai TC-GS-POS-287 sebelum TC-GS-POS-110 karena TC-GS-POS-110 mengubah nama record `Head of Operations`. Urutan menyimpang dari urutan TC sumber.
- Pada TC-GS-POS-91, langkah 6 dan 7 (tidak ada error dan tidak ada dialog Unsaved Changes) diasersi segera sesudah `[Save]` (langkah 5) dan sebelum asersi toast, karena error inline dan dialog adalah state sementara; urutan ini menyimpang dari urutan Expected TC (bagian 8b butir 5 dan 11).
- Asersi absence toast diletakkan segera sesudah pemicu `[Save]` dan sebelum asersi toast hasil: langkah 8 (tidak ada toast "Success, position has been updated.", pemicu langkah 5, TC-GS-POS-91) sebelum langkah 9 sampai 10, dan langkah 42 (tidak ada toast "No changes to save.", pemicu langkah 41, TC-GS-POS-90) sebelum langkah 43. Urutan ini menyimpang dari urutan Expected TC (bagian 8b butir 5 dan 11); toast hasil yang menyusul menjadi anchor positif bagi pemicu.
- Pembagian TC lintas spec: TC-GS-POS-91 dan 92 hanya mengasersi yang ada di Expected pada tabel dan form; asersi "tidak ada entri log" untuk TC-GS-POS-246 dan 308 ada di spec 046, dan spec ini tidak mengklaim absence log.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 45, 51, 57, 62, 67, 73 (Search agar baris target tampil pada halaman aktif), langkah 2 dan 31 (mencatat Last Updated dan waktu sesudah `[Save]` sebagai pembanding), langkah 39 (jeda ±500 ms agar validasi duplikat selesai sebelum asersi tidak ada error; TC-GS-POS-90 tidak menyebut jeda), langkah 53 dan 76 (menutup input Search lewat `(←)`), langkah 61 dan 66 (menutup overlay), dan langkah 54 sampai 56 (ganti akun eksplisit dan membuka layar Position pada sesi Client Seed).
- Penutupan Popup Edit pada TC sukses terjadi otomatis lewat Save. Jumlah pembukaan Popup Edit: 7 (langkah 3, 14, 21, 27, 37, 46, 68); jumlah penutupan: 7 (semua lewat Save atau penutupan otomatis).
- Langkah 4, 15, 22, 28, 38, 47, dan 69 adalah `Verifikasi` dari anotasi "→ Popup Edit Position terbuka" pada Langkah 1 TC.
- Spec melewati sekitar 35 langkah (76 langkah). Tiap blok TC memakai record sendiri dan berdiri sendiri; semuanya satu kelas (Edit sukses dan No-Op). Bagian Client Seed memakai akun dan entitas berbeda lewat langkah ganti akun eksplisit (langkah 54 sampai 55), sehingga bagian itu tetap bermakna bila bagian Client A gagal keras (konvensi bagian 3, "Pisahkan spec hanya jika ada pemisah nyata", kasus b: batas ukuran berarti bagian sesudah ganti akun tetap bermakna, bukan jumlah langkah).
- Nama 1 karakter literal `Y` dan `Z` memakai pengecualian S-12 (nama 1 karakter literal tanpa suffix): seeding idempotent (dilewati bila sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite berjalan serial, dan nama berbeda dengan spec 014 (`Q`) pada entitas yang sama.
- Expected `Last Updated = waktu Save` (langkah 36) dibandingkan dengan waktu jam klien yang dicatat pada langkah 31 (sesudah `[Save]` pada langkah 30), dalam format tanggal General Settings aktif, dengan toleransi satu menit; jam server dan jam browser sinkron (Prerequisites).
- Seeding `Legal Counsel`, `iOS Developer`, `IT Support Specialist`, dan `Data Engineer` dipakai sebagai target aksi TC yang diasersi.
- Temuan untuk QA:
  - TC-GS-POS-110 dan 287: email akun Total Control entitas `Client Seed` tidak tertulis di Pre-setup 21, dan env var-nya belum ada di daftar Pre-setup; spec memakai `GS_CLIENTSEED_TC_PASSWORD` (env baru). TC-GS-POS-110 mengubah record seed `Head of Operations`; spec memakai nama hasil `Operations Director {runId}-019` dan memulihkannya di hook `after`.
  - TC-GS-POS-283 menulis record `Q` diubah menjadi `R`, dan record `Q` berasal dari TC-GS-POS-282 (spec 014). Spec ini men-seed record 1 karakter sendiri bernama `Y` (diubah menjadi `Z`), tanpa suffix karena batas 1 karakter, supaya tidak bentrok dengan `Q` milik spec 014 pada entitas yang sama. Nilai uji 1 karakter pada TC-GS-POS-283 tidak mengubah objek uji (batas 1 karakter). Seeding dilewati bila `Y` sudah ada dan cleanup hanya menghapus yang dibuat spec ini.
  - TC-GS-POS-79: nama 120 karakter versi Edit di TC berakhir `ProgramssE`; spec memakai nama dengan suffix `{runId}-019` yang panjang totalnya tetap 120 karakter, sehingga bagian akhir nama berbeda dari TC.
  - TC-GS-POS-91 Expected a ("spinner berhenti") dan TC-GS-POS-89 Expected c ("posisi urutan baru") tidak menyebut cara pengamatan; spec mengasersi tidak ada spinner tersisa dan urutan A-Z di tabel tersaring.
  - TC-GS-POS-91 Expected a meminta asersi "spinner berhenti" bersama "Popup tertutup otomatis"; spinner tombol adalah state sementara yang hanya bermakna selama Popup Edit terbuka, sedangkan langkah 12 mengasersinya sesudah Popup tertutup (langkah 11). Asersi dipertahankan sesuai TC; bentuk Expected yang dapat diamati secara bermakna perlu ditentukan pemilik TC.
  - TC-GS-POS-110 dan 287 berstatus Manual Only di kolom Automation; tetap dimasukkan sesuai konvensi bagian 2.
  - Post Condition tanpa langkah observasi di TC dan tidak diasersi: TC-GS-POS-79 ("Record bernama 120 karakter"), TC-GS-POS-90 dan 110 ("Changelog mencatat entri Edit"), TC-GS-POS-89 (Changelog, Activity Log Global Settings, dan dropdown Position form User dan Non-Login User), TC-GS-POS-283 ("Record bernama `Z`"), serta TC-GS-POS-91 dan 92 ("tidak ada entri baru di Changelog dan Activity Log").
