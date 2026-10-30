---
id: TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya
title: "Delete Position Tunggal: Dialog, Cancel, Esc, Sukses, Klik Ganda, dan Position Terakhir Entitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-111
  - TC-GS-POS-112
  - TC-GS-POS-113
  - TC-GS-POS-120
  - TC-GS-POS-122
  - TC-GS-POS-299
coverage:
  web: automated
---

# Delete Position Tunggal: Dialog, Cancel, Esc, Sukses, Klik Ganda, dan Position Terakhir Entitas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec 014, 020, dan 022 menulis ke entitas `Client Tulis` (Pre-setup 27) dan masing-masing mengembalikannya ke 0 Position; ketiganya tidak berjalan bersamaan.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; langkah 1 tidak mengulang pembukaan layar.
- Akun aktor:
  - Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client Tulis (Pre-setup 27) untuk TC-GS-POS-122: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTWRITE_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Email akun ini tidak tertulis di tabel Pre-setup TC (lihat Temuan untuk QA).
  - Hook `after` mengembalikan sesi ke akun Total Control default suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak dihapus atau diubah spec ini, tanpa suffix): Position 10 `IT Manager` (bebas relasi; dipakai TC-GS-POS-111, 112, dan 299 yang tidak menghapusnya) dan entitas `Client Tulis` (Pre-setup 27, Total Control) dengan 0 Position yang boleh ditulis. `IT Manager` hanya dibaca: aksi Delete atasnya dibatalkan (`[Cancel]` pada TC-GS-POS-112, `Esc` pada TC-GS-POS-299) atau hanya dibuka dialognya (TC-GS-POS-111), sehingga record dan Last Updated-nya tidak berubah (pengecualian S-06).
- Data Dinamis (di-seed lewat API di hook `before`; fixture baru `Fixture.position.deleteSingle020`):
  - Entitas Total Control: `Temporary Staff {runId}-020` (TC-GS-POS-113) dan `Brand Manager {runId}-020` (TC-GS-POS-120), keduanya tidak dipakai user dan dihapus oleh spec ini.
  - Entitas Client Tulis: `General Manager {runId}-020` (TC-GS-POS-122), tidak dipakai user. Seeding memakai sesi akun Client Tulis. Entitas hanya memiliki Position ini sehingga jumlahnya kembali 0 sesudah spec.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-020` yang masih ada di kedua entitas.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control dan Total Control `Client Tulis`) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: klik ganda cepat pada `[Delete]` (TC-GS-POS-120); penekanan tombol Tab dan Esc serta pembacaan elemen yang sedang fokus (TC-GS-POS-299); Search tabel; ganti akun (logout lalu login).
- State global: tidak ada yang diubah selain flag Guided Tooltip (diatur hook suite) dan sesi akun (dipulihkan seperti di atas).

## Test Steps

### TC-GS-POS-111: Screening Dialog Delete Position untuk jabatan bebas relasi

1. Ketik Search `IT Manager`, tekan Enter
2. Klik `⋯` pada baris `IT Manager`, pilih `Delete`
3. Verifikasi Header dialog menampilkan Title "Delete Position"
4. Verifikasi Header dialog berseverity danger
5. Verifikasi Body dialog menampilkan bullet `• IT Manager`
6. Verifikasi Body dialog menampilkan teks "Are you sure you want to delete it? This action cannot be undone." di bawah bullet
7. Verifikasi Footer dialog menampilkan `[Cancel]` bertipe text (contrast)
8. Verifikasi Footer dialog menampilkan `[Delete]` bertipe filled (danger)

### TC-GS-POS-112: Delete single, Cancel pada Dialog Delete Position

9. Klik `[Cancel]` pada Dialog Delete Position yang terbuka dari langkah 2
10. Verifikasi tidak ada toast
11. Verifikasi dialog tertutup
12. Verifikasi baris `IT Manager` tetap ada

### TC-GS-POS-299: Accessibility dialog Delete, focus trap dan Esc

13. Klik `⋯` pada baris `IT Manager`, pilih `Delete`
14. Tekan Tab 5 kali berturut-turut
15. Verifikasi fokus Tab hanya berputar di `[Cancel]` dan `[Delete]` di dalam Dialog Delete Position
16. Tekan Esc
17. Verifikasi tidak ada toast
18. Verifikasi dialog tertutup
19. Verifikasi baris `IT Manager` tetap ada
20. Klik `(←)` pada kotak Search

### TC-GS-POS-113: Delete single Position bebas relasi

21. Ketik Search `Temporary Staff {runId}-020`, tekan Enter
22. Klik `⋯` pada baris `Temporary Staff {runId}-020`, pilih `Delete`
23. Klik `[Delete]`
24. Verifikasi muncul toast sukses: "Success, position has been deleted."
25. Verifikasi dialog tertutup
26. Verifikasi baris `Temporary Staff {runId}-020` hilang dari tabel
27. Klik `(←)` pada kotak Search

### TC-GS-POS-120: Delete single, klik ganda Delete hanya diproses sekali

28. Tunggu toast dari langkah 24 hilang otomatis
29. Ketik Search `Brand Manager {runId}-020`, tekan Enter
30. Klik `⋯` pada baris `Brand Manager {runId}-020`, pilih `Delete`
31. Klik `[Delete]` 2× dengan cepat
32. Verifikasi hanya 1 toast sukses yang tampil: "Success, position has been deleted."
33. Verifikasi baris `Brand Manager {runId}-020` hilang dari tabel
34. Klik `(←)` pada kotak Search

### TC-GS-POS-122: Delete satu-satunya Position di entitas diizinkan

35. Ganti akun: logout dari akun Total Control
36. Login sebagai Total Control entitas `Client Tulis` dengan `Spectra.env.GS_CLIENTWRITE_TC_PASSWORD`
37. Buka Global Settings > User > Position
38. Klik `⋯` pada baris `General Manager {runId}-020`, pilih `Delete`
39. Klik `[Delete]`
40. Verifikasi muncul toast sukses: "Success, position has been deleted."
41. Verifikasi tidak ada dialog guard "item terakhir"
42. Verifikasi tabel berpindah ke empty state "No position yet"

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 111, 112, 299, 113, 120, 122. Dialog yang dibuka pada langkah 2 dipakai bersama TC-GS-POS-111 dan TC-GS-POS-112 (langkah 1 sampai 2 kedua TC identik), sehingga langkah 9 menutupnya dengan `[Cancel]`. TC-GS-POS-299 membuka dialog sendiri. Kasus yang menghapus data (113, 120, 122) berada sesudah semua kasus yang membutuhkan baris tetap ada, dan TC-GS-POS-122 paling akhir karena berganti akun. Urutan ini menyimpang dari urutan TC sumber (111, 112, 113, 120, 122, 299).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 21, 29 (Search agar baris target tampil di halaman aktif pada tabel 10 per halaman), langkah 20, 27, 34 (menutup input Search lewat `(←)`), langkah 28 (menunggu toast sukses dari langkah 24 hilang otomatis supaya hitungan toast pada langkah 32 hanya memuat toast hasil klik ganda), dan langkah ganti akun 35 sampai 37.
- Pada TC-GS-POS-112 dan 299, asersi tidak ada toast (langkah 10 dan 17) diletakkan segera sesudah `[Cancel]` atau `Esc` dan sebelum asersi dialog tertutup dan baris tetap ada, karena toast adalah state sementara; urutan ini menyimpang dari urutan Expected TC (bagian 8b butir 5 dan 11).
- Pencatatan Delete di Changelog dan Activity Log diasersi di spec 044 (TC-GS-POS-244) dan opsi Position yang hilang dari dropdown form User dan Non-Login User di spec 048 (TC-GS-POS-258).
- Spec melewati sekitar 35 langkah (42 langkah). Seluruhnya satu kelas (Delete single yang berhasil atau dibatalkan), satu dataset milik spec, tanpa kelas harness lain. Blok TC-GS-POS-113, 120, dan 122 memakai Position milik sendiri dan blok 111, 112, 299 hanya membaca Position Pre-setup, sehingga kegagalan satu blok tidak menghilangkan makna blok lain. Blok TC-GS-POS-122 memakai akun dan entitas berbeda lewat langkah ganti akun eksplisit (langkah 35 sampai 36) dan tetap bermakna bila blok sebelumnya gagal keras (konvensi bagian 3, kasus b: batas ukuran berarti bagian sesudah ganti akun tetap bermakna).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi: TC-GS-POS-112 (tidak ada entri Changelog), TC-GS-POS-113 (record terhapus permanen, entri Changelog, Activity Log, dropdown User dan Non-Login User), dan TC-GS-POS-120 (tepat 1 entri Delete di Changelog).
  - TC-GS-POS-120 memakai Position `Brand Manager` dan TC-GS-POS-122 memakai `General Manager` yang tidak ada di tabel Pre-setup maupun Data Uji Dinamis; spec men-seed keduanya dengan suffix `{runId}-020`.
  - TC-GS-POS-122: Pre-setup 27 mendefinisikan `Client Tulis` dengan 0 Position, sedangkan precondition TC mensyaratkan tepat 1 Position `General Manager`; spec men-seed 1 Position lalu menghapusnya, sehingga entitas kembali ke 0 Position. Delete menulis Changelog permanen di `Client Tulis` (Pre-setup 27 menyatakan entitas ini tidak dipakai TC baca-saja).
  - TC-GS-POS-122 Expected b ("Tidak ada dialog guard 'item terakhir'") tidak menyebut teks atau judul dialog guard; spec mengasersi tidak ada dialog guard "item terakhir" (langkah 41) tanpa mengasersi teks dialog tertentu.
  - TC-GS-POS-299 Expected a tidak menyebut jumlah penekanan Tab; spec memakai 5 kali (lebih banyak dari jumlah elemen fokus dialog).
  - Email akun Total Control `Client Tulis` tidak tertulis di Pre-setup 27 dan env var-nya belum terdaftar di `spectra.config.ts` maupun `.env.example`; spec memakai `GS_CLIENTWRITE_TC_PASSWORD` (env baru).
  - TC-GS-POS-120 dan 122 mencantumkan dependensi TC-GS-POS-54 dan 73 (pembuatan data); spec menggantinya dengan seeding API.
