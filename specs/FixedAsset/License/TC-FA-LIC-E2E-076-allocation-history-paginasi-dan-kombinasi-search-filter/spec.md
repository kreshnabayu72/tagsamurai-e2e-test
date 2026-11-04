---
id: TC-FA-LIC-E2E-076-allocation-history-paginasi-dan-kombinasi-search-filter
title: "Allocation History: Paginasi dan Kombinasi Search, Filter, Sort, serta Paginasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-257
  - TC-FA-LIC-258
  - TC-FA-LIC-259
  - TC-FA-LIC-260
coverage:
  web: automated
---
# Allocation History: Paginasi dan Kombinasi Search, Filter, Sort, serta Paginasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): tujuh alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001, LALC-20241205-00001 (urutan default Last Updated terbaru lebih dulu; enam alokasi pertama ber-Plan Owner PT Maju Bersama (Distributor), LALC-20241205-00001 ber-Plan Owner PT ABC (Principal); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; LALC-20241205-00001 `Addon (Audit)` berstatus Expired, SUBS-20241201-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Data Pre-setup #39 (Allocation History 25 baris; dipakai TC-FA-LIC-257, 258, dan 259): 7 alokasi Pre-setup #13 ditambah 18 alokasi fixture berstatus Expired milik term SUBS-20250101-00001 (End Date 31/12/25 sama dengan End Date term itu, Plan Owner `PT Maju Bersama (Distributor)`, License Type `Asset License` atau `Addon (Audit)`; Allocation ID berformat `LALC-YYYYMMDD-XXXXX`), tanpa mengubah Total Asset License maupun ledger Add-on. Fixture BE (disediakan tim FE/BE; nama usulan `Fixture.fixedAssetLicense.riwayatPaginasi`) memasang 18 alokasi itu di hook `before`, memulihkan riwayat ke 7 alokasi Pre-setup #13 pada langkah 32 (TC-FA-LIC-260 memakai 7 alokasi Pre-setup #13; Pre-setup #39 hanya berlaku pada TC yang merujuknya), dan memulihkannya lagi di hook `after`.
- Test Data TC-FA-LIC-259 (nilai default Pre-setup #39): Search `Maju` (hasil 24 baris: 6 alokasi Pre-setup #13 ber-Plan Owner `PT Maju Bersama (Distributor)` ditambah 18 alokasi fixture, lebih dari 10 baris) dan Filter Status = `Expired`.
- State yang diubah dan dipulihkan: page size (dikembalikan ke 10 pada langkah 14, 23, dan 72), Sort `Allocation ID` (dinetralkan pada langkah 22) dan Sort `License Type` (pada langkah 71), Search dan Filter (dibersihkan pada langkah 30, 31, 66, dan 70), serta riwayat Allocation (fixture Pre-setup #39 dipulihkan ke Pre-setup #13 pada langkah 32 dan hook `after`).
- Kemampuan teknis (disediakan tim FE): mengirim tombol `Esc` ke browser (langkah 6).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-257: Default 10 per halaman, pilihan page size, dan input nomor halaman

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

### TC-FA-LIC-258: Nomor halaman tidak valid, ganti sort, dan ganti page size

15. Pindah ke halaman 2

Untuk setiap nilai pada daftar `0`, `99`, `abc` (langkah 16 sampai 17):

16. Ketik nilai pada input nomor halaman, tekan Enter
17. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 2

18. Klik header kolom `Allocation ID` untuk sort
19. Verifikasi mengganti sort tetap di halaman 2
20. Ganti page size menjadi `25`
21. Verifikasi mengganti page size kembali ke halaman 1
22. Klik header kolom `Allocation ID` dua kali lagi hingga netral
23. Buka pilihan page size, lalu pilih `10`

### TC-FA-LIC-259: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

24. Pindah ke halaman 2
25. Ketik Search `Maju`, tekan Enter
26. Verifikasi setelah Search tabel kembali ke halaman 1
27. Pindah ke halaman 2 lagi
28. Klik ikon Filter, pada field `Status` centang `Expired`, lalu klik `[Apply]`
29. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
30. Klik `[Clear Field]`, lalu klik `[Apply]`
31. Klik ikon Filter untuk menutup panel, lalu klik `(←)` pada kotak Search

### TC-FA-LIC-260: Kombinasi Search, Filter, Sort, dan paginasi

32. Pulihkan riwayat Allocation ke 7 alokasi Pre-setup #13 (hapus 18 alokasi fixture Pre-setup #39) lewat fixture BE hingga berhasil tersimpan
33. Muat ulang halaman (F5)
34. Klik sub-tab `Allocation History`
35. Verifikasi tabel menampilkan tujuh alokasi Pre-setup #13: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001, LALC-20241205-00001
36. Ketik Search `Asset License`, tekan Enter
37. Verifikasi tabel menampilkan: LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
38. Klik ikon Filter, pada field `Status` centang `Active`, lalu klik `[Apply]`
39. Verifikasi tabel menampilkan: LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001
40. Verifikasi Filter Panel tetap terbuka
41. Klik header kolom `Quantity` dua kali
42. Ubah page size menjadi `25`
43. Verifikasi tabel menampilkan: LALC-20260101-00001, LALC-20260312-00002, LALC-20260720-00003
44. Verifikasi indikator Descending pada `Quantity`
45. Verifikasi page size 25
46. Verifikasi Search `Asset License` tidak berubah
47. Verifikasi Filter Status `Active` tidak berubah
48. Klik header kolom `License Type` sekali
49. Verifikasi tabel menampilkan: LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001
50. Verifikasi `Quantity` kembali netral
51. Verifikasi indikator Ascending pada `License Type`
52. Verifikasi Search `Asset License` tidak berubah
53. Verifikasi Filter Status `Active` tidak berubah
54. Pada Filter Panel yang masih terbuka, klik `[Clear Field]`, lalu klik `[Apply]`
55. Verifikasi tabel menampilkan: LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
56. Verifikasi Search `Asset License` tetap aktif
57. Verifikasi Sort `License Type` tetap aktif
58. Pada field `Status` centang lagi `Active`, lalu klik `[Apply]`
59. Kosongkan isi kotak search, tekan Enter
60. Verifikasi tabel menampilkan: LALC-20260515-00002, LALC-20260801-00004, LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001
61. Verifikasi LALC-20250210-00001 dan LALC-20241205-00001 tidak tampil
62. Verifikasi Filter tetap aktif
63. Verifikasi Sort `License Type` Ascending tetap aktif
64. Ketik Search `Expired`, tekan Enter
65. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
66. Kosongkan isi kotak search, tekan Enter
67. Verifikasi tabel pulih otomatis menampilkan: LALC-20260515-00002, LALC-20260801-00004, LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001
68. Verifikasi Filter tetap aktif
69. Verifikasi Sort `License Type` Ascending tetap aktif
70. Klik `[Clear Field]`, lalu klik `[Apply]`
71. Klik header kolom `License Type` dua kali lagi hingga netral
72. Ubah page size menjadi `10`
73. Klik ikon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Urutan TC dalam spec: 257, 258, 259, 260 (sesuai `sourceTc`).
- Spec ini di atas 35 langkah (73 langkah nominal; 77 langkah setelah ekspansi). Alasan: seluruh blok satu topik (paginasi dan kontrol tabel Allocation History), satu klien dengan riwayat Pre-setup #13 (hanya dibaca; fixture Pre-setup #39 dipasang dan dipulihkan fixture BE), tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah 16 sampai 17 diulang untuk tiga nilai input nomor halaman dengan satu `Verifikasi` per iterasi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 14 dan 23 (mengembalikan page size ke 10; S-09), langkah 22 (menetralkan sort; S-09), langkah 30 (membersihkan Filter; S-09) dan 31 (menutup panel dan mengosongkan Search; S-09), langkah 32 sampai 34 (memulihkan riwayat ke Pre-setup #13 sebelum TC-FA-LIC-260, lalu membuka kembali sub-tab), serta langkah 70 sampai 73 (memulihkan Filter, Sort `License Type`, page size, dan panel; S-09). Filter Panel tetap terbuka sesudah `[Apply]` (prd-conventions.md §9.8), sehingga mengubah Filter dari panel itu tidak didahului membuka panel.
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-259 hasil Search `Maju` dan Filter Status = `Expired` dihitung lebih dari 10 baris dari Pre-setup #13 dan #39 (nilai Test Data TC); pada TC-FA-LIC-258 kolom sort `Allocation ID` dan page size `25` dipilih spec (TC menulis "klik header kolom untuk sort"); `Verifikasi` tujuh alokasi Pre-setup #13 sesudah pemulihan fixture (langkah 35) membuktikan precondition TC-FA-LIC-260.
- Temuan untuk QA:
  - TC-FA-LIC-260 memuat precondition 7 alokasi Pre-setup #13, sedangkan TC-FA-LIC-257, 258, dan 259 memuat 25 baris (Pre-setup #39); spec memulihkan riwayat ke 7 alokasi lewat fixture BE sebelum TC-FA-LIC-260. Pre-setup #39 menyebut License Type fixture `Asset License` atau `Addon (Audit)` tanpa komposisi pasti; hasil Search `Asset License` TC-FA-LIC-260 hanya cocok bila 18 alokasi itu tidak ikut tampil, sehingga pemulihan wajib.
  - TC-FA-LIC-260 mengasersi urutan Sort `Quantity` dan `License Type` tanpa menyebut nilai Quantity tiap baris dan tie-break; spec mengasersi urutan persis seperti Expected TC.
  - TC-FA-LIC-257, 258, 259, dan 260 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
