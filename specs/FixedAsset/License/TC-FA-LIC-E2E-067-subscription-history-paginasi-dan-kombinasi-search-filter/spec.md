---
id: TC-FA-LIC-E2E-067-subscription-history-paginasi-dan-kombinasi-search-filter
title: "Subscription History: Paginasi dan Kombinasi Search, Filter, Sort, serta Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-214
  - TC-FA-LIC-215
  - TC-FA-LIC-216
  - TC-FA-LIC-217
coverage:
  web: automated
---
# Subscription History: Paginasi dan Kombinasi Search, Filter, Sort, serta Paginasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Data Pre-setup #38 (Subscription History 25 baris; dipakai TC-FA-LIC-214, 215, dan 216): 4 term Pre-setup #13 ditambah 21 term fixture berstatus non-live (Renewed; Plan Owner `PT Maju Bersama (Distributor)`, Type `Paid`; Subscription ID berformat `SUBS-YYYYMMDD-XXXXX`) yang tidak mengubah term live SUBS-20260101-00001, Total Asset License, maupun banner. Fixture BE (disediakan tim FE/BE; nama usulan `Fixture.fixedAssetLicense.riwayatPaginasi`) memasang 21 term itu di hook `before`, memulihkan riwayat ke 4 term Pre-setup #13 pada langkah 32 (TC-FA-LIC-217 memakai 4 term Pre-setup #13; Pre-setup #38 hanya berlaku pada TC yang merujuknya), dan memulihkannya lagi di hook `after`.
- Test Data TC-FA-LIC-216 (nilai default Pre-setup #38): Search `Maju` (hasil 24 baris: 3 term Pre-setup #13 ber-Plan Owner `PT Maju Bersama (Distributor)` ditambah 21 term fixture, lebih dari 10 baris) dan Filter Type = `Paid`.
- State yang diubah dan dipulihkan: page size (dikembalikan ke 10 pada langkah 14, 23, dan 72), Sort `Subscription ID` (dinetralkan pada langkah 22) dan Sort `Plan` (pada langkah 71), Search dan Filter (dibersihkan pada langkah 30, 31, 66, dan 70), serta riwayat Subscription (fixture Pre-setup #38 dipulihkan ke Pre-setup #13 pada langkah 32 dan hook `after`).
- Kemampuan teknis (disediakan tim FE): mengirim tombol `Esc` ke browser (langkah 6).

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-214: Default 10 per halaman, pilihan page size, dan input nomor halaman

2. Verifikasi footer menampilkan page size 10 secara default
3. Verifikasi halaman 1 menampilkan 10 baris
4. Buka pilihan page size
5. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
6. Tutup pilihan page size dengan Esc
7. Verifikasi page size tetap 10
8. Ketik nomor halaman `2` pada input nomor halaman, tekan Enter
9. Verifikasi input nomor halaman 2 langsung membuka halaman 2
10. Verifikasi halaman 2 menampilkan 10 baris (baris ke-11 sampai ke-20)
11. Buka pilihan page size, lalu pilih `25`
12. Verifikasi seluruh 25 baris tampil dalam satu halaman
13. Verifikasi tabel kembali ke halaman 1
14. Buka pilihan page size, lalu pilih `10`

### TC-FA-LIC-215: Nomor halaman tidak valid, ganti sort, dan ganti page size

15. Pindah ke halaman 2

Untuk setiap nilai pada daftar `0`, `99`, `abc` (langkah 16 sampai 17):

16. Ketik nilai pada input nomor halaman, tekan Enter
17. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 2

18. Klik header kolom `Subscription ID` untuk sort
19. Verifikasi mengganti sort tetap di halaman 2
20. Ganti page size menjadi `25`
21. Verifikasi mengganti page size kembali ke halaman 1
22. Klik header kolom `Subscription ID` dua kali lagi hingga netral
23. Buka pilihan page size, lalu pilih `10`

### TC-FA-LIC-216: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

24. Pindah ke halaman 2
25. Ketik Search `Maju`, tekan Enter
26. Verifikasi setelah Search tabel kembali ke halaman 1
27. Pindah ke halaman 2 lagi
28. Klik ikon Filter, pada field `Type` centang `Paid`, lalu klik `[Apply]`
29. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
30. Klik `[Clear Field]`, lalu klik `[Apply]`
31. Klik ikon Filter untuk menutup panel, lalu klik `(←)` pada kotak Search

### TC-FA-LIC-217: Kombinasi Search, Filter, Sort, dan paginasi

32. Pulihkan riwayat Subscription ke 4 term Pre-setup #13 (hapus 21 term fixture Pre-setup #38) lewat fixture BE hingga berhasil tersimpan
33. Muat ulang halaman (F5)
34. Klik sub-tab `Subscription History`
35. Verifikasi tabel menampilkan empat term Pre-setup #13: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001
36. Ketik Search `Professional`, tekan Enter
37. Verifikasi tabel menampilkan: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
38. Klik ikon Filter, pada field `Status` centang `Active`, `Pending`, dan `Converted`, lalu klik `[Apply]`
39. Verifikasi tabel menampilkan: SUBS-20270101-00001, SUBS-20260101-00001
40. Verifikasi Filter Panel tetap terbuka
41. Klik header kolom `Subscription ID` sekali
42. Ubah page size menjadi `25`
43. Verifikasi tabel menampilkan: SUBS-20260101-00001, SUBS-20270101-00001
44. Verifikasi indikator Ascending pada `Subscription ID`
45. Verifikasi page size 25
46. Verifikasi Search `Professional` tidak berubah
47. Verifikasi Filter Status `Active`, `Pending`, dan `Converted` tidak berubah
48. Klik header kolom `Plan` sekali
49. Verifikasi tabel menampilkan: SUBS-20270101-00001, SUBS-20260101-00001
50. Verifikasi `Subscription ID` kembali netral
51. Verifikasi indikator Ascending pada `Plan`
52. Verifikasi Search `Professional` tidak berubah
53. Verifikasi Filter Status `Active`, `Pending`, dan `Converted` tidak berubah
54. Pada Filter Panel yang masih terbuka, klik `[Clear Field]`, lalu klik `[Apply]`
55. Verifikasi tabel menampilkan: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
56. Verifikasi Search `Professional` tetap aktif
57. Verifikasi Sort `Plan` tetap aktif
58. Pada field `Status` centang lagi `Active`, `Pending`, dan `Converted`, lalu klik `[Apply]`
59. Kosongkan isi kotak search, tekan Enter
60. Verifikasi tabel menampilkan: SUBS-20241201-00001, SUBS-20270101-00001, SUBS-20260101-00001
61. Verifikasi SUBS-20250101-00001 tidak tampil
62. Verifikasi Filter tetap aktif
63. Verifikasi Sort `Plan` Ascending tetap aktif
64. Ketik Search `Renewed`, tekan Enter
65. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
66. Kosongkan isi kotak search, tekan Enter
67. Verifikasi tabel pulih otomatis menampilkan: SUBS-20241201-00001, SUBS-20270101-00001, SUBS-20260101-00001
68. Verifikasi Filter tetap aktif
69. Verifikasi Sort `Plan` Ascending tetap aktif
70. Klik `[Clear Field]`, lalu klik `[Apply]`
71. Klik header kolom `Plan` dua kali lagi hingga netral
72. Ubah page size menjadi `10`
73. Klik ikon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Urutan TC dalam spec: 214, 215, 216, 217 (sesuai `sourceTc`).
- Spec ini di atas 35 langkah (73 langkah nominal; 77 langkah setelah ekspansi). Alasan: seluruh blok satu topik (paginasi dan kontrol tabel Subscription History), satu klien dengan riwayat Pre-setup #13 (hanya dibaca; fixture Pre-setup #38 dipasang dan dipulihkan fixture BE), tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah 16 sampai 17 diulang untuk tiga nilai input nomor halaman dengan satu `Verifikasi` per iterasi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 14 dan 23 (mengembalikan page size ke 10; S-09), langkah 22 (menetralkan sort; S-09), langkah 30 (membersihkan Filter; S-09) dan 31 (menutup panel dan mengosongkan Search; S-09), langkah 32 sampai 34 (memulihkan riwayat ke Pre-setup #13 sebelum TC-FA-LIC-217, lalu membuka kembali sub-tab), serta langkah 70 sampai 73 (memulihkan Filter, Sort `Plan`, page size, dan panel; S-09). Filter Panel tetap terbuka sesudah `[Apply]` (prd-conventions.md §9.8), sehingga mengubah Filter dari panel itu tidak didahului membuka panel.
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-216 hasil Search `Maju` dan Filter Type = `Paid` dihitung lebih dari 10 baris dari Pre-setup #13 dan #38 (nilai Test Data TC); pada TC-FA-LIC-215 kolom sort `Subscription ID` dan page size `25` dipilih spec (TC menulis "klik header kolom untuk sort"); `Verifikasi` empat term Pre-setup #13 sesudah pemulihan fixture (langkah 35) membuktikan precondition TC-FA-LIC-217.
- Temuan untuk QA:
  - TC-FA-LIC-217 memuat precondition 4 term Pre-setup #13, sedangkan TC-FA-LIC-214, 215, dan 216 memuat 25 baris (Pre-setup #38); spec memulihkan riwayat ke 4 term lewat fixture BE sebelum TC-FA-LIC-217. Pre-setup #38 tidak menyebut Plan 21 term fixture; hasil Search `Professional` TC-FA-LIC-217 hanya cocok bila 21 term itu tidak ikut tampil, sehingga pemulihan wajib.
  - TC-FA-LIC-217 mengurutkan Sort `Plan` untuk baris ber-Plan sama (SUBS-20270101-00001 dan SUBS-20260101-00001 sama-sama `Professional`) tanpa menyebut tie-break; spec mengasersi urutan persis seperti Expected TC.
  - TC-FA-LIC-214, 215, 216, dan 217 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
