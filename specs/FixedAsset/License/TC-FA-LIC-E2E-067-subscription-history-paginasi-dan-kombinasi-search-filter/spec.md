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
- Data Dinamis (milik spec, dibuat di hook `before` oleh fixture BE yang disediakan tim FE/BE dan dihapus di hook `after`): 21 baris Subscription History tambahan sehingga total tabel 25 baris (4 term Pre-setup #13 + 21; TC menulis "tabel berisi 25 baris (fixture)"). Seluruh baris tambahan berpola Plan `Enterprise`, Type `Paid`, Status `Converted`, Plan Owner `PT Uji Lain {runId}-067`, dan Start Date lebih baru dari 01/01/27. Pola ini dipilih spec agar Search `Enterprise` dan Filter Status `Converted` menghasilkan lebih dari 10 baris (TC-FA-LIC-216) tanpa mengubah hasil Search `Professional` dan Filter Status `Active` atau `Pending` (TC-FA-LIC-217).
- State yang diubah dan dipulihkan: page size (dikembalikan ke 10 pada langkah 11 dan 20), Sort `Subscription ID` (dinetralkan pada langkah 19), Search dan Filter (dibersihkan pada langkah 27 dan 36).

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-214: Default 10 per halaman, pilihan page size, dan input nomor halaman

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

### TC-FA-LIC-215: Nomor halaman tidak valid, ganti sort, dan ganti page size

12. Pindah ke halaman 2

Untuk setiap nilai pada daftar `0`, `99`, `abc` (langkah 13 sampai 14):

13. Ketik nilai pada input nomor halaman, tekan Enter
14. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 2

15. Klik header kolom `Subscription ID` untuk sort
16. Verifikasi mengganti sort tetap di halaman 2
17. Ganti page size menjadi `25`
18. Verifikasi mengganti page size kembali ke halaman 1
19. Klik header kolom `Subscription ID` dua kali lagi hingga netral
20. Buka pilihan page size, lalu pilih `10`

### TC-FA-LIC-216: Search dan Apply Filter di halaman lebih dari 1 mereset ke halaman 1

21. Pindah ke halaman 2
22. Ketik Search `Enterprise`, tekan Enter
23. Verifikasi setelah Search tabel kembali ke halaman 1
24. Pindah ke halaman 2 lagi
25. Klik ikon Filter, pada field `Status` centang `Converted`, lalu klik `[Apply]`
26. Verifikasi setelah Apply Filter tabel kembali ke halaman 1
27. Klik `[Clear Field]`, lalu klik `[Apply]`
28. Klik ikon Filter untuk menutup panel, lalu klik `(←)` pada kotak Search

### TC-FA-LIC-217: Kombinasi Search, Filter, Sort, dan paginasi

29. Ketik Search `Professional`, tekan Enter
30. Klik ikon Filter, pada field `Status` centang `Active` dan `Pending`, lalu klik `[Apply]`
31. Klik header kolom `Subscription ID` sekali
32. Ubah page size menjadi `25`
33. Verifikasi Search, Filter, Sort, dan page size berlaku bersamaan: tabel menampilkan SUBS-20260101-00001 dan SUBS-20270101-00001
34. Klik header kolom `Plan Owner` sekali
35. Verifikasi mengganti kolom sort tidak mereset Search dan Filter: kata kunci `Professional` tetap aktif dan tabel tetap menampilkan SUBS-20260101-00001 dan SUBS-20270101-00001
36. Klik `[Clear Field]`, lalu klik `[Apply]`
37. Verifikasi Clear Filter tidak mereset Search dan Sort: kata kunci `Professional` dan Sort `Plan Owner` tetap aktif, tabel menampilkan SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
38. Pada field `Status` centang `Active`, lalu klik `[Apply]`
39. Klik `(←)` pada kotak Search
40. Verifikasi mengosongkan Search tidak mereset Filter dan Sort: Filter Status `Active` dan Sort `Plan Owner` tetap aktif, tabel menampilkan SUBS-20260101-00001
41. Klik `[Clear Field]`, lalu klik `[Apply]`
42. Ketik Search `Professional`, tekan Enter
43. Pada field `Status` centang `Converted`, lalu klik `[Apply]`
44. Verifikasi hasil kosong dari irisan Search dan Filter: tabel menampilkan empty state `No results found`
45. Klik `[Clear Field]`, lalu klik `[Apply]`
46. Verifikasi tabel pulih saat Filter dilepas: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
47. Pada field `Status` centang `Converted`, lalu klik `[Apply]`
48. Klik `(←)` pada kotak Search
49. Verifikasi tabel pulih saat Search dilepas: tabel menampilkan baris berstatus `Converted` pada halaman 1
50. Klik `[Clear Field]`, lalu klik `[Apply]`
51. Klik header kolom `Plan Owner` dua kali lagi hingga netral
52. Klik ikon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Urutan TC dalam spec: 214, 215, 216, 217. Pada TC-FA-LIC-214 langkah memasukkan nomor halaman 2 dilakukan sebelum memilih page size 25 (TC menulis sebaliknya), karena halaman 2 hanya ada saat page size 10 (25 baris pada page size 25 menjadi satu halaman); page size dikembalikan ke 10 sesudahnya.
- Spec ini di atas 35 langkah (52 langkah nominal; 56 langkah setelah ekspansi). Alasan: seluruh blok satu topik (paginasi dan kontrol tabel Subscription History), satu dataset (empat term Pre-setup #13 ditambah 21 baris milik spec), tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah 13 sampai 14 diulang untuk tiga nilai input nomor halaman dengan satu `Verifikasi` per iterasi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 11 dan 20 (mengembalikan page size ke 10; S-09), langkah 19 (menetralkan sort; S-09), langkah 27, 28, dan 36 serta langkah pembersih sesudahnya (pemulihan Search dan Filter; S-09).
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-216, kata kunci `Enterprise` dan Filter Status `Converted` dipilih spec agar hasil melebihi 10 baris; pada TC-FA-LIC-217, kolom sort `Subscription ID`, kolom pengganti `Plan Owner`, page size 25, dan irisan kosong Search `Professional` dengan Filter Status `Converted` dipilih spec. Pengamatan Clear Filter dan pengosongan Search pada TC-FA-LIC-217 dilakukan dengan Filter dipasang ulang sebelum Search dikosongkan.
- Temuan untuk QA:
  - TC-FA-LIC-214 (butir TC 5) meminta nomor halaman 2 setelah page size 25 dengan 25 baris (hanya satu halaman); Expected "bila tersedia" tidak deterministik. Spec menukar urutan seperti dijelaskan di atas.
  - TC-FA-LIC-217 menulis "Clear Filter; kemudian kosongkan Search" sehingga klausa "mengosongkan Search tidak mereset Filter" tidak teramati (Filter sudah dilepas); spec memasang ulang Filter sebelum mengosongkan Search.
  - TC-FA-LIC-217 menulis "Klik sort pada satu kolom; ubah page size" tanpa menyebut kolom dan nilai page size.
  - TC-FA-LIC-214, 215, 216, dan 217 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
