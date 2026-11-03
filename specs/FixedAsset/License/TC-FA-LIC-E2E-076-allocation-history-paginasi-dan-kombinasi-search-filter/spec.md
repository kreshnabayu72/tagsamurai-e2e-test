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
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Data Dinamis (milik spec, dibuat di hook `before` oleh fixture BE yang disediakan tim FE/BE dan dihapus di hook `after`): 19 baris Allocation History tambahan sehingga total tabel 25 baris (6 alokasi Pre-setup #13 + 19; TC menulis "tabel berisi 25 baris (fixture)"). Seluruh baris tambahan berpola License Type `Addon (Audit)`, Status `Active`, dan Plan Owner `PT Uji Lain {runId}-076`. Pola ini dipilih spec agar Search `Addon` dan Filter Status `Active` menghasilkan lebih dari 10 baris (TC-FA-LIC-259) tanpa mengubah hasil Search `Asset License` dengan Filter Status `Active` (TC-FA-LIC-260).
- State yang diubah dan dipulihkan: page size (dikembalikan ke 10 pada langkah 11 dan 20), Sort `Allocation ID` dan `Plan Owner` (dinetralkan pada langkah 19 dan 51), Search dan Filter (dibersihkan pada langkah 27 dan sesudahnya).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-257: Default 10 per halaman, pilihan page size, dan input nomor halaman

2. Verifikasi tabel menampilkan 10 baris per halaman secara default
3. Buka pilihan page size
4. Verifikasi pilihan page size 10, 25, 50, 100 (tanpa opsi All)
5. Tutup pilihan page size dengan Esc
6. Ketik nomor halaman `2` pada input nomor halaman, tekan Enter
7. Verifikasi input nomor halaman 2 langsung membuka halaman 2
8. Buka pilihan page size, lalu pilih `25`
9. Verifikasi seluruh 25 baris tampil dalam satu halaman
10. Verifikasi tabel kembali ke halaman 1
11. Buka pilihan page size, lalu pilih `10`

### TC-FA-LIC-258: Nomor halaman tidak valid, ganti sort, dan ganti page size

12. Pindah ke halaman 2

Untuk setiap nilai pada daftar `0`, `99`, `abc` (langkah 13 sampai 14):

13. Ketik nilai pada input nomor halaman, tekan Enter
14. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 2

15. Klik header kolom `Allocation ID` untuk sort
16. Verifikasi mengganti sort tetap di halaman 2
17. Ganti page size menjadi `25`
18. Verifikasi mengganti page size kembali ke halaman 1
19. Klik header kolom `Allocation ID` dua kali lagi hingga netral
20. Buka pilihan page size, lalu pilih `10`

### TC-FA-LIC-259: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

21. Pindah ke halaman 2
22. Ketik Search `Addon`, tekan Enter
23. Verifikasi setelah Search tabel kembali ke halaman 1
24. Pindah ke halaman 2 lagi
25. Klik ikon Filter, pada field `Status` centang `Active`, lalu klik `[Apply]`
26. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
27. Klik `[Clear Field]`, lalu klik `[Apply]`
28. Klik ikon Filter untuk menutup panel, lalu klik `(←)` pada kotak Search

### TC-FA-LIC-260: Kombinasi Search, Filter, Sort, dan paginasi

29. Ketik Search `Asset License`, tekan Enter
30. Klik ikon Filter, pada field `Status` centang `Active`, lalu klik `[Apply]`
31. Klik header kolom `Allocation ID` sekali
32. Ubah page size menjadi `25`
33. Verifikasi Search, Filter, Sort, dan page size berlaku bersamaan: tabel menampilkan LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001
34. Klik header kolom `Plan Owner` sekali
35. Verifikasi mengganti kolom sort tidak mereset Search dan Filter: kata kunci `Asset License` tetap aktif dan tabel tetap menampilkan LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001
36. Klik `[Clear Field]`, lalu klik `[Apply]`
37. Verifikasi Clear Filter tidak mereset Search dan Sort: kata kunci `Asset License` dan Sort `Plan Owner` tetap aktif, tabel menampilkan LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
38. Pada field `Status` centang `Active`, lalu klik `[Apply]`
39. Klik `(←)` pada kotak Search
40. Verifikasi mengosongkan Search tidak mereset Filter dan Sort: Filter Status `Active` dan Sort `Plan Owner` tetap aktif, tabel menampilkan baris berstatus `Active` pada halaman 1
41. Klik `[Clear Field]`, lalu klik `[Apply]`
42. Ketik Search `Asset License`, tekan Enter
43. Pada field `Plan Owner` centang `PT Uji Lain {runId}-076`, lalu klik `[Apply]`
44. Verifikasi hasil kosong dari irisan Search dan Filter: tabel menampilkan empty state `No results found`
45. Klik `[Clear Field]`, lalu klik `[Apply]`
46. Verifikasi tabel pulih saat Filter dilepas: LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
47. Pada field `Plan Owner` centang `PT Uji Lain {runId}-076`, lalu klik `[Apply]`
48. Klik `(←)` pada kotak Search
49. Verifikasi tabel pulih saat Search dilepas: tabel menampilkan baris milik `PT Uji Lain {runId}-076` pada halaman 1
50. Klik `[Clear Field]`, lalu klik `[Apply]`
51. Klik header kolom `Plan Owner` dua kali lagi hingga netral
52. Klik ikon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Urutan TC dalam spec: 257, 258, 259, 260. Pada TC-FA-LIC-257 langkah memasukkan nomor halaman 2 dilakukan sebelum memilih page size 25 (TC menulis sebaliknya), karena halaman 2 hanya ada saat page size 10 (25 baris pada page size 25 menjadi satu halaman); page size dikembalikan ke 10 sesudahnya.
- Spec ini di atas 35 langkah (52 langkah nominal; 56 langkah setelah ekspansi). Alasan: seluruh blok satu topik (paginasi dan kontrol tabel Allocation History), satu dataset (enam alokasi Pre-setup #13 ditambah 19 baris milik spec), tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah 13 sampai 14 diulang untuk tiga nilai input nomor halaman dengan satu `Verifikasi` per iterasi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 11 dan 20 (mengembalikan page size ke 10; S-09), langkah 19 dan 51 (menetralkan sort; S-09), serta langkah pembersih Search dan Filter di akhir tiap blok (S-09).
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-259, kata kunci `Addon` dan Filter Status `Active` dipilih spec agar hasil melebihi 10 baris; pada TC-FA-LIC-260, kolom sort `Allocation ID`, kolom pengganti `Plan Owner`, page size 25, dan irisan kosong Search `Asset License` dengan Filter Plan Owner `PT Uji Lain {runId}-076` dipilih spec. Pengamatan Clear Filter dan pengosongan Search pada TC-FA-LIC-260 dilakukan dengan Filter dipasang ulang sebelum Search dikosongkan.
- Temuan untuk QA:
  - TC-FA-LIC-257 (langkah TC 5) meminta nomor halaman 2 setelah page size 25 dengan 25 baris (hanya satu halaman); Expected "bila tersedia" tidak deterministik. Spec menukar urutan seperti dijelaskan di atas.
  - TC-FA-LIC-260 menulis "Clear Filter; kemudian kosongkan Search" sehingga klausa "mengosongkan Search tidak mereset Filter" tidak teramati (Filter sudah dilepas); spec memasang ulang Filter sebelum mengosongkan Search.
  - TC-FA-LIC-260 menulis "Klik sort pada satu kolom; ubah page size" tanpa menyebut kolom dan nilai page size.
  - TC-FA-LIC-257, 258, 259, dan 260 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
