---
id: TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi
title: "Create Position Berhasil: Stay, 1 dan 120 Karakter, Trim, Populasi Data, Persistensi setelah Refresh, dan dari Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-41
  - TC-GS-POS-51
  - TC-GS-POS-52
  - TC-GS-POS-53
  - TC-GS-POS-54
  - TC-GS-POS-73
  - TC-GS-POS-282
  - TC-GS-POS-286
coverage:
  web: automated
---

# Create Position Berhasil: Stay, 1 dan 120 Karakter, Trim, Populasi Data, Persistensi setelah Refresh, dan dari Empty State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): TC-GS-POS-73 membuat satu Position di entitas `Client Tulis` (Pre-setup 27, entitas 0 Position yang boleh ditulis; dipakai juga spec 020 dan 022), sehingga spec ini tidak berjalan bersamaan dengan keduanya. Position tersebut dihapus di hook `after`.
- Layar awal Global Settings > User > Position dibuka hook `beforeEach`; langkah 1 langsung membuka popup Create.
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client Tulis (Pre-setup 27) untuk TC-GS-POS-73: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTWRITE_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA).
  - Hook `after` mengembalikan sesi ke akun Total Control default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: entitas `Client Tulis` (Pre-setup 27) dengan 0 Position (Precondition c TC-GS-POS-73).
- Kuota: Master Data Count Limit belum tercapai (Precondition c TC-GS-POS-51) dengan sisa kuota minimal 16 Position pada entitas Total Control default dan 1 Position pada `Client Tulis`; nilai limit tidak diubah spec ini.
- Data Dinamis (dibuat lewat UI oleh spec ini; nama bersuffix per run; fixture baru `Fixture.position.createSuccess014`):
  - D-14 (TC-GS-POS-41): nama 120 karakter yang diawali teks Data Uji TC-GS-POS-41 (`Senior Manager of Regional Supply Chain Planning, ...`) dan dipotong dari belakang sehingga panjang total termasuk suffix ` {runId}-014` tepat 120 karakter.
  - `IT Support Specialist {runId}-014` (TC-GS-POS-51 dan 286).
  - `HR Business Partner {runId}-014` dan `Temporary Staff {runId}-014` (TC-GS-POS-52).
  - 10 nama TC-GS-POS-53, masing-masing bersuffix ` {runId}-014`: `iOS Developer`, `Legal Counsel`, `Marketing Executive`, `Quality Assurance Analyst`, `Data Engineer`, `Office Administrator`, `Logistics Coordinator`, `Payroll Specialist`, `Security Officer`, `Training Coordinator`.
  - Input `  Brand Manager {runId}-014  ` (2 spasi depan dan belakang; tersimpan `Brand Manager {runId}-014`) (TC-GS-POS-54).
  - `Q` tanpa suffix (TC-GS-POS-282; nilai 1 karakter adalah objek uji). Prasyarat: tidak ada Position `Q` pada entitas Total Control default (spec 019 memakai `Y` dan `Z`, nama berbeda dari `Q`). Hook `before` mencatat apakah `Q` sudah ada; hook `after` hanya menghapus `Q` yang dibuat spec ini. Bila `Q` sudah ada pada entitas saat hook `before` dijalankan, Submit langkah 38 ditolak sebagai duplikat dan prasyarat spec ini tidak terpenuhi; entitas tanpa `Q` disediakan tim FE/BE. Suite serial.
  - `General Manager {runId}-014` pada entitas `Client Tulis` (TC-GS-POS-73).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-014` dan Position `Q` yang dibuat spec ini pada entitas Total Control default; hapus `General Manager {runId}-014` pada `Client Tulis` sehingga entitas kembali ke 0 Position.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Jam: jam server dan jam browser sinkron (untuk asersi Last Updated = waktu Submit pada TC-GS-POS-51; waktu dicatat sesudah `[Submit]`, toleransi satu menit karena Last Updated berketelitian menit).
- Kemampuan teknis: pembacaan waktu klien sesudah Submit; menunggu toast hilang otomatis (jeda nyata ±4 detik, TC-GS-POS-51); ganti akun (logout lalu login); penyetelan ukuran halaman tabel ke 25; F5 tanpa form terbuka.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite) dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-41: Position Name tepat 120 karakter diterima

1. Klik `[+ Position]`
2. Ketik nama 120 karakter D-14 (termasuk suffix) pada Position Name
3. Verifikasi tidak ada error "Max. 120 characters"
4. Klik `[Submit]`
5. Verifikasi toast sukses: "Success, position has been created."
6. Verifikasi popup tertutup

### TC-GS-POS-51: Create Position, Stay tidak dicentang

7. Klik `[+ Position]`
8. Ketik `IT Support Specialist {runId}-014` pada Position Name
9. Klik `[Submit]`
10. Catat waktu klien (sampai menit) sesudah `[Submit]` diklik
11. Verifikasi toast sukses: "Success, position has been created."
12. Verifikasi toast tampil di kanan bawah
13. Verifikasi toast hilang otomatis setelah 4 detik
14. Verifikasi popup tertutup

### TC-GS-POS-52: Create Position, Stay dicentang untuk input berulang

15. Klik `[+ Position]`
16. Centang `Stay on this form after submitting`
17. Ketik `HR Business Partner {runId}-014` pada Position Name
18. Klik `[Submit]`
19. Verifikasi toast sukses: "Success, position has been created."
20. Verifikasi popup tetap terbuka
21. Verifikasi Position Name kosong
22. Verifikasi fokus di Position Name
23. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
24. Ketik `Temporary Staff {runId}-014` pada Position Name
25. Klik `[Submit]`
26. Verifikasi toast sukses: "Success, position has been created."
27. Verifikasi popup tetap terbuka
28. Verifikasi Position Name kosong
29. Verifikasi fokus di Position Name
30. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang

### TC-GS-POS-53: Populasi data uji Position via Stay on this form

31. Untuk setiap dari 10 nama bersuffix pada Data Dinamis TC-GS-POS-53 secara berurutan (satu per satu): ketik nama pada Position Name lalu klik `[Submit]`
32. Verifikasi setelah tiap `[Submit]` pada langkah 31 muncul toast sukses: "Success, position has been created."

### TC-GS-POS-54: Spasi depan/belakang dibuang saat disimpan

33. Ketik `  Brand Manager {runId}-014  ` pada Position Name
34. Klik `[Submit]`
35. Verifikasi toast sukses: "Success, position has been created."

### TC-GS-POS-282: Position Name 1 karakter diterima

36. Ketik `Q` pada Position Name
37. Verifikasi tidak ada error validasi
38. Klik `[Submit]`
39. Verifikasi toast sukses: "Success, position has been created."

### TC-GS-POS-52 (lanjutan): menutup form Stay yang kosong

40. Klik `[✕]` pada form kosong
41. Verifikasi popup tertutup
42. Verifikasi dialog Unsaved Changes tidak muncul

### Verifikasi tabel setelah form ditutup (lanjutan TC-GS-POS-41, 51, 52, 53, 54)

43. Ketik Search `{runId}-014`, tekan Enter
44. Ubah ukuran halaman ke 25
45. Verifikasi baris D-14 (nama 120 karakter) tampil di tabel (TC-GS-POS-41)
46. Verifikasi baris `IT Support Specialist {runId}-014` tampil di tabel (TC-GS-POS-51)
47. Verifikasi baris `IT Support Specialist {runId}-014` berada pada urutan Name A-Z: di antara `iOS Developer {runId}-014` dan `Legal Counsel {runId}-014` (TC-GS-POS-51)
48. Verifikasi Last Updated baris `IT Support Specialist {runId}-014` sesuai waktu Submit yang dicatat pada langkah 10, dengan toleransi satu menit (TC-GS-POS-51)
49. Catat nilai Last Updated baris `IT Support Specialist {runId}-014`
50. Verifikasi baris `HR Business Partner {runId}-014` tampil di tabel (TC-GS-POS-52)
51. Verifikasi baris `Temporary Staff {runId}-014` tampil di tabel (TC-GS-POS-52)
52. Verifikasi ke-10 nama TC-GS-POS-53 tampil di tabel (TC-GS-POS-53)
53. Verifikasi ke-10 nama TC-GS-POS-53 terurut Name A-Z: `Data Engineer`, `iOS Developer`, `Legal Counsel`, `Logistics Coordinator`, `Marketing Executive`, `Office Administrator`, `Payroll Specialist`, `Quality Assurance Analyst`, `Security Officer`, `Training Coordinator` (TC-GS-POS-53)
54. Verifikasi teks sel Name baris `Brand Manager {runId}-014` sama persis tanpa spasi depan dan belakang (TC-GS-POS-54)
55. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)
56. Kembalikan ukuran halaman ke 10

### TC-GS-POS-286: Record tetap ada setelah refresh

57. Tekan F5
58. Ketik Search `IT Support`, tekan Enter
59. Verifikasi baris `IT Support Specialist {runId}-014` tetap tampil
60. Verifikasi Last Updated baris `IT Support Specialist {runId}-014` sama dengan nilai yang dicatat pada langkah 49
61. Klik `(←)` pada kotak Search (menutup input dan mereset tabel)

### TC-GS-POS-73: Create pertama dari empty state mengembalikan tabel

62. Ganti akun: logout dari akun Total Control
63. Login sebagai Total Control Client Tulis
64. Buka Global Settings > User > Position
65. Verifikasi tabel menampilkan empty state "No position yet"
66. Klik `[+ Position]`
67. Ketik `General Manager {runId}-014` pada Position Name
68. Klik `[Submit]`
69. Verifikasi toast sukses: "Success, position has been created."
70. Verifikasi empty state "No position yet" hilang
71. Verifikasi tabel menampilkan 1 baris `General Manager {runId}-014`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 41, 51, 52, 53, 54, 282, 286, 73. Menyimpang dari urutan TC sumber (41, 51, 52, 53, 54, 73, 282, 286) karena: TC-GS-POS-282 ikut satu sesi Stay yang sama dengan TC-GS-POS-52, 53, dan 54 (prinsip 8 konvensi); TC-GS-POS-286 butuh record dari TC-GS-POS-51 dan tidak butuh form; TC-GS-POS-73 berada di akun dan entitas lain sehingga ditaruh paling akhir.
- Pembukaan form (`[+ Position]`) dan kejadian menutup form: empat pembukaan (langkah 1, 7, 15, 66) dan empat penutupan: Submit sukses Stay tidak dicentang (langkah 4 dan 9), `[✕]` form Stay kosong (langkah 40), dan Submit sukses pada `Client Tulis` (langkah 68). Penutupan ✕ langkah 40 memenuhi Step 5 TC-GS-POS-52 dan Step 4 TC-GS-POS-53.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 (mencatat waktu klien sesudah `[Submit]` langkah 9; dibandingkan dengan Last Updated pada langkah 48, toleransi satu menit), langkah 16 (mengatur Stay untuk TC-GS-POS-52 sampai 282), langkah 31 (perulangan Submit TC-GS-POS-53: langkah 31 sampai 32 diulang untuk 10 nama, `Verifikasi` toast sesudah tiap `[Submit]`), langkah 43 dan 44 (Search bersuffix dan ukuran halaman 25 agar semua baris spec ini tampil dalam satu halaman), langkah 49 (mencatat Last Updated pembanding untuk TC-GS-POS-286), langkah 55 dan 56 (mengosongkan Search dan mengembalikan ukuran halaman sebelum F5), langkah 61 (mengosongkan Search), dan langkah ganti akun 62 sampai 63 (langkah 64 membuka Position pada akun baru).
- Langkah 65 adalah `Verifikasi` tambahan di luar Expected TC-GS-POS-73: empty state harus tampil lebih dulu (Dependensi TC-GS-POS-7) agar Expected b ("empty state hilang") bermakna.
- Posisi "urutan Name A-Z" pada Expected c TC-GS-POS-51 diamati terhadap baris lain milik spec ini (Search `{runId}-014`), karena tabel Position environment berisi data lain; urutan mengikuti collation en-US tidak peka huruf besar-kecil (`iOS Developer` berada setelah `Data Engineer` dan sebelum `IT Support Specialist`).
- Pembagian TC lintas spec: TC-GS-POS-47, 48, 49 ada di spec 012; TC-GS-POS-37 sampai 40, 42 sampai 45, 50, dan 284 ada di spec 011; TC-GS-POS-46 dan 84 ada di spec 049.
- Spec melewati sekitar 35 langkah (71 langkah nominal; 89 langkah dengan ekspansi langkah 31 sampai 32 untuk 10 nama). Seluruhnya satu kelas (Create sukses), satu dataset bersuffix; tiap Create memakai nama sendiri sehingga kegagalan satu Create tidak menghilangkan makna Create lain, dan blok TC-GS-POS-73 memakai akun dan entitas lain lewat langkah ganti akun eksplisit yang berdiri sendiri.
- Temuan untuk QA:
  - Post Condition TC-GS-POS-51 b dan c (Changelog 1 entri Create, Activity Log, opsi Position di dropdown form User dan Non-Login User), TC-GS-POS-52 (Changelog 2 entri Create), dan TC-GS-POS-54 (Changelog New Value `Brand Manager`), dan TC-GS-POS-282 ("Record `Q` tersimpan") tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini.
  - TC-GS-POS-282 memakai `Q` (1 karakter) yang tidak bisa diberi suffix; TC-GS-POS-283 (spec 019) memakai `Y` dan `Z`, nama berbeda dari `Q`, sehingga kedua spec tidak bentrok. Pengecualian nama 1 karakter literal berlaku dengan syarat seeding idempotent, cleanup hanya yang dibuat spec ini, dan suite serial (S-12).
  - TC-GS-POS-73 membuat Position di entitas `Client Tulis` (Pre-setup 27, 0 Position, boleh ditulis); spec ini memulihkan keadaan 0 Position di hook `after`. Email akun Total Control `Client Tulis` tidak tertulis di Pre-setup 27 dan env var `GS_CLIENTWRITE_TC_PASSWORD` baru didaftarkan tim FE.
  - TC-GS-POS-41 memakai nama 120 karakter literal tanpa suffix; spec memakai nama turunan dengan suffix `{runId}-014` yang total panjangnya 120 karakter, sehingga batas yang diuji tetap sama.
  - TC-GS-POS-286 Search `IT Support` dapat juga cocok dengan Position milik spec lain; asersi mengidentifikasi baris dari nama bersuffix.
  - Urutan `iOS Developer` terhadap nama berawalan huruf besar bergantung pada collation tabel; asersi langkah 53 mengikuti collation en-US tidak peka huruf besar-kecil yang juga dipakai spec 001.
