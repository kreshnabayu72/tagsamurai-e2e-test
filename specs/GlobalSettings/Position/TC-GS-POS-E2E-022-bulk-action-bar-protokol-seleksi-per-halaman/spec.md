---
id: TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman
title: "Bulk Action Bar Position: Populasi 15 Position, Screening, Counter, Icon ✕, Checkbox Header, Indeterminate, dan Seleksi Manual hingga 100%"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-123
  - TC-GS-POS-124
  - TC-GS-POS-125
  - TC-GS-POS-126
  - TC-GS-POS-127
  - TC-GS-POS-128
  - TC-GS-POS-130
coverage:
  web: automated
---

# Bulk Action Bar Position: Populasi 15 Position, Screening, Counter, Icon ✕, Checkbox Header, Indeterminate, dan Seleksi Manual hingga 100%

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec 014, 020, dan 022 menulis ke entitas `Client Tulis` (Pre-setup 27) dan masing-masing mengembalikannya ke 0 Position; ketiganya tidak berjalan bersamaan.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; langkah 1 langsung membuka form Create.
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client Tulis (Pre-setup 27) untuk TC-GS-POS-130: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTWRITE_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA).
  - Hook `after` mengembalikan sesi ke akun Total Control default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 sampai 16 (7 record) pada entitas Total Control, yang ikut terhitung dalam jumlah total baris tabel N; entitas `Client Tulis` (Pre-setup 27, Total Control) dengan 0 Position yang boleh ditulis.
- Data Dinamis:
  - Dibuat lewat UI oleh TC-GS-POS-123 (Stay on this form) pada entitas Total Control, 15 Position bersuffix `{runId}-022`: `Account Executive`, `Business Analyst`, `Content Writer`, `Customer Support Agent`, `Facility Manager`, `Graphic Designer`, `Network Engineer`, `Product Designer`, `Project Coordinator`, `Research Analyst`, `Sales Representative`, `Software Tester`, `System Administrator`, `Technical Writer`, dan `UX Researcher`, masing-masing diikuti ` {runId}-022`. Dengan 7 record Pre-setup, jumlah baris tabel N = 22 (lebih dari 10, sehingga ada halaman 2). N diturunkan dari seeding (7 Pre-setup + 15 hasil langkah 3 = 22) dan ditetapkan pada langkah 13, bukan dibaca dari tabel yang hanya menampilkan satu halaman.
  - Di-seed hook `before` pada entitas `Client Tulis` (fixture baru `Fixture.position.bulkBar022`): 3 Position `Area Manager {runId}-022`, `Shift Leader {runId}-022`, `Store Clerk {runId}-022`, tidak dipakai user, sehingga entitas memiliki tepat 3 Position (TC-GS-POS-130 mensyaratkan tepat 3). Kemampuan seeding pada entitas `Client Tulis` disediakan tim FE/BE.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-022` yang masih ada di kedua entitas.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control dan Total Control `Client Tulis`) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: Search tabel; pembacaan state checkbox (checked, unchecked, indeterminate), background baris terpilih, dan teks Bulk Action Bar; ganti akun (logout lalu login).
- State global: Selection Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits berada pada nilai default (lebih besar dari 10) dan tidak diubah spec ini. Flag Guided Tooltip diatur hook suite; sesi akun dipulihkan seperti di atas.

## Test Steps

### TC-GS-POS-123: Populasi data uji Bulk Delete via Stay on this form

1. Klik `[+ Position]`
2. Centang checkbox `Stay on this form after submitting`
3. Untuk setiap nama berikut (urut): `Account Executive {runId}-022`, `Business Analyst {runId}-022`, `Content Writer {runId}-022`, `Customer Support Agent {runId}-022`, `Facility Manager {runId}-022`, `Graphic Designer {runId}-022`, `Network Engineer {runId}-022`, `Product Designer {runId}-022`, `Project Coordinator {runId}-022`, `Research Analyst {runId}-022`, `Sales Representative {runId}-022`, `Software Tester {runId}-022`, `System Administrator {runId}-022`, `Technical Writer {runId}-022`, `UX Researcher {runId}-022`, ulangi langkah 4 sampai 6
4. Ketik nama pada field Position Name
5. Klik `[Submit]`
6. Verifikasi muncul toast sukses: "Success, position has been created."
7. Klik `✕` pada header form
8. Ketik Search `{runId}-022`, tekan Enter
9. Verifikasi halaman 1 menampilkan 10 nama urut A-Z: `Account Executive`, `Business Analyst`, `Content Writer`, `Customer Support Agent`, `Facility Manager`, `Graphic Designer`, `Network Engineer`, `Product Designer`, `Project Coordinator`, `Research Analyst` (masing-masing bersuffix ` {runId}-022`)
10. Pindah ke halaman 2
11. Verifikasi halaman 2 menampilkan 5 nama sisanya: `Sales Representative`, `Software Tester`, `System Administrator`, `Technical Writer`, `UX Researcher` (masing-masing bersuffix ` {runId}-022`)
12. Klik `(←)` pada kotak Search

### TC-GS-POS-124: Screening Bulk Action Bar saat 1 baris dicentang

13. Tetapkan N = 22 (7 Position Pre-setup ditambah 15 Position hasil langkah 3)
14. Centang checkbox baris `Account Executive {runId}-022`
15. Verifikasi Bulk Action Bar muncul rata kiri sejajar Table Tools
16. Verifikasi urutan elemen Bulk Action Bar: tombol `Bulk Action`, teks "1 Position selected", tombol "Select All (N records)", icon `✕`
17. Verifikasi baris `Account Executive {runId}-022` ber-background selected
18. Klik `Bulk Action`
19. Verifikasi overlay `Bulk Action` berisi aksi `Delete`
20. Verifikasi aksi `Delete` ber-icon DeleteBin6Line
21. Verifikasi aksi `Delete` berseverity danger
22. Klik `Bulk Action` sekali lagi untuk menutup overlay

### TC-GS-POS-125: Counter Bulk Action Bar singular/plural realtime

23. Hapus centang baris `Account Executive {runId}-022`
24. Centang baris `Account Executive {runId}-022`
25. Verifikasi counter "1 Position selected"
26. Centang baris `Business Analyst {runId}-022`
27. Verifikasi counter "2 Positions selected"
28. Hapus centang baris `Business Analyst {runId}-022`
29. Verifikasi counter kembali "1 Position selected"

### TC-GS-POS-126: Icon ✕ pada Bulk Action Bar membatalkan seluruh seleksi

30. Hapus centang baris `Account Executive {runId}-022`
31. Centang baris `Account Executive {runId}-022`
32. Centang baris `Business Analyst {runId}-022`
33. Klik icon `✕` pada Bulk Action Bar
34. Verifikasi seluruh checkbox baris ter-uncheck
35. Verifikasi Bulk Action Bar hilang

### TC-GS-POS-127: Checkbox header memilih dan membatalkan seluruh baris halaman aktif

36. Klik checkbox header
37. Verifikasi seluruh 10 baris halaman 1 tercentang
38. Verifikasi checkbox header checked
39. Verifikasi counter "10 Positions selected"
40. Pindah ke halaman 2
41. Verifikasi baris halaman 2 tidak tercentang
42. Kembali ke halaman 1
43. Klik checkbox header lagi
44. Verifikasi seluruh baris halaman 1 unchecked
45. Verifikasi Bulk Action Bar hilang

### TC-GS-POS-128: Checkbox header indeterminate saat sebagian baris dicentang

46. Centang 1 baris di halaman 1 (`Account Executive {runId}-022`)
47. Verifikasi checkbox header menampilkan state indeterminate `[-]`
48. Verifikasi counter "1 Position selected"
49. Klik icon `✕` pada Bulk Action Bar

### TC-GS-POS-130: Centang manual seluruh baris hingga 100% mengubah tombol menjadi Unselect All

50. Ganti akun: logout dari akun Total Control
51. Login sebagai Total Control entitas `Client Tulis` dengan `Spectra.env.GS_CLIENTWRITE_TC_PASSWORD`
52. Buka Global Settings > User > Position
53. Centang baris `Area Manager {runId}-022`
54. Centang baris `Shift Leader {runId}-022`
55. Centang baris `Store Clerk {runId}-022`
56. Verifikasi counter "3 Positions selected"
57. Verifikasi tombol "Select All (3 records)" berubah menjadi "Unselect All"
58. Klik icon `✕` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: 123, 124, 125, 126, 127, 128, 130. TC-GS-POS-123 membuat data yang dipakai TC-GS-POS-124 sampai 128 dalam spec yang sama; TC-GS-POS-130 paling akhir karena berganti akun ke entitas Client Tulis. Pembukaan form `[+ Position]` satu kali ditutup dengan `✕` pada langkah 7.
- Langkah 3 sampai 6 memakai pola "untuk setiap nama": langkah 4 sampai 6 diulang untuk 15 nama (15 toast sukses diverifikasi satu per Submit).
- Langkah 9 dan 11 memverifikasi ke-15 nama pada tabel yang disaring Search `{runId}-022` (10 nama di halaman 1 dan 5 nama di halaman 2); Search dipakai agar hanya data spec ini yang diperiksa. Asersi dilakukan sesudah form ditutup karena tabel berada di belakang modal selama Stay tercentang.
- Asersi tambahan di luar Expected TC-GS-POS-123 b ("Ke-15 nama tampil di tabel"): urutan A-Z pada langkah 9 dan 11, serta pembagian 10 nama di halaman 1 dan 5 nama di halaman 2. Alasannya, langkah 14 sampai 49 mengandalkan baris `Account Executive` dan `Business Analyst` berada di halaman 1 pada urutan default Name A-Z, dan langkah 36 sampai 45 mengandalkan halaman 1 berisi 10 baris, sehingga urutan dan pembagian halaman itu diperiksa lebih dulu.
- Pada langkah 14 sampai 49 baris dicari di halaman 1 tanpa Search karena pada urutan default Name A-Z `Account Executive` dan `Business Analyst` berada di halaman 1. Search tidak dipakai supaya "Select All (N records)" dan counter mengacu ke seluruh tabel.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 (Search agar baris target tampil), langkah 10 (pindah ke halaman 2 untuk memeriksa sisa nama), langkah 12 (menutup input Search lewat `(←)`), langkah 13 (menetapkan N dari seeding), langkah 22 (menutup overlay), langkah 23 dan 30 (menghapus centang agar kasus berikutnya mulai dari seleksi bersih), langkah 49 dan 58 (menutup seleksi dengan `✕`), serta langkah ganti akun 50 sampai 52. Langkah 2 (centang Stay) mengatur mode sesi form, bukan asersi TC.
- Spec melewati sekitar 35 langkah (58 langkah nominal; sekitar 100 langkah dengan ekspansi langkah 4 sampai 6 sebanyak 15 kali). Seluruhnya satu kelas (Bulk Action Bar dan protokol seleksi per halaman) dengan satu akun utama dan satu dataset; TC-GS-POS-124 sampai 128 membaca data yang dibuat TC-GS-POS-123 pada spec yang sama, sehingga bagian sesudah TC-GS-POS-123 kehilangan makna bila populasi gagal. Blok TC-GS-POS-130 berdiri sendiri (akun dan entitas `Client Tulis` sendiri lewat langkah ganti akun eksplisit, langkah 50 sampai 51) dan tetap bermakna bila blok sebelumnya gagal keras (konvensi bagian 3, kasus b: batas ukuran berarti bagian sesudah ganti akun tetap bermakna).
- Temuan untuk QA:
  - TC-GS-POS-124 sampai 128 mencantumkan dependensi TC-GS-POS-123; spec menjalankan TC-GS-POS-123 (populasi lewat UI) di dalam spec yang sama. Asersi tabel TC-GS-POS-123 Expected b ("Ke-15 nama tampil di tabel") diperiksa lewat Search `{runId}-022` pada dua halaman.
  - TC-GS-POS-124 dan 127 mensyaratkan total baris lebih dari 10 (halaman 2 ada) tanpa menyebutnya di precondition; terpenuhi oleh 7 record Pre-setup ditambah 15 record Data Dinamis.
  - TC-GS-POS-126 Expected a ("Seluruh checkbox ter-uncheck") tidak menyebut cakupan halaman; spec mengasersi checkbox baris di halaman aktif.
  - TC-GS-POS-130: Pre-setup 27 mendefinisikan `Client Tulis` dengan 0 Position, sedangkan precondition TC mensyaratkan tepat 3 Position `Area Manager`, `Shift Leader`, `Store Clerk`; spec men-seed 3 Position bersuffix dan menghapusnya di `after` sehingga entitas kembali ke 0 Position.
  - Email akun Total Control `Client Tulis` tidak tertulis di Pre-setup 27 dan env var-nya belum terdaftar di `spectra.config.ts` maupun `.env.example`; spec memakai `GS_CLIENTWRITE_TC_PASSWORD` (env baru).
  - Post Condition TC-GS-POS-123 ("Record Data Dinamis No. 20 sampai 34 tersimpan") tidak punya langkah observasi terpisah selain Expected b yang sudah diasersi.
