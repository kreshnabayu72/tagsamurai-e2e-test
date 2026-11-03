---
id: TC-AC-ACHS-E2E-288-pagination-kombinasi-dan-hapus-baris-terakhir-tab-available
title: "Pagination Stock Detail Tab Available: Default, Navigasi, Input Halaman, Kombinasi Empat Kontrol, dan Hapus Baris Terakhir di Halaman Terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-305
  - TC-AC-ACHS-306
  - TC-AC-ACHS-307
  - TC-AC-ACHS-308
  - TC-AC-ACHS-309
  - TC-AC-ACHS-317
coverage:
  web: automated
---

# Pagination Stock Detail Tab Available: Default, Navigasi, Input Halaman, Kombinasi Empat Kontrol, dan Hapus Baris Terakhir di Halaman Terakhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `Fixture.hardwareStock.account.p01.totalControl.email` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen halaman Stock List; flag halaman Stock Detail disetel dengan cara yang sama (disediakan tim FE; lihat `suite.md`).
- Data Pre-setup (read-only, tidak diubah spec): SKU `Fixture.hardwareStock.p16.a[4].sku` (Long Range) dengan 18 unit Available dan 1 unit Waiting for Approval (#17, Tabel E: `Fixture.hardwareStock.p17.e[10].deviceName` sampai `Fixture.hardwareStock.p17.e[28].deviceName`; Tab Available 19 baris) dan General Settings #15 (Date Format `DD MMM YYYY`, Time Format 24-hour `HH:mm`). Tidak ada Data Dinamis.
- Baseline Pre-setup (S-06): spec ini membaca baseline unit SKU `Fixture.hardwareStock.p16.a[4].sku` (Pre-setup #17, Tabel E) tanpa mengubahnya, sedangkan nomor spec ini sesudah spec penulis (240 sampai 284). Syarat: baseline Pre-setup dipulihkan fixture environment automation ke keadaan awal sebelum spec ini dimulai (`suite.md`, bagian "Urutan jalan" dan "Seeding ulang Pre-setup"); fixture dan skrip pemulihannya disediakan tim FE/BE dan belum ada. Spec ini tidak menumpang hasil spec lain.
- Parameter Pre-setup: nilai populasi Pre-setup tidak ditulis di spec; langkah dan asersi merujuk kunci fixture `Fixture.hardwareStock.<path>` pada tabel berikut (identitas data, bukan rahasia; berkas `fixtures/hardwareStock.json` belum ada, dibuat tim FE/BE dari tabel Data Uji Pre-setup TC dan ditandai sebagai fixture yang belum ada). Spec tidak memerlukan pengecualian S-12 untuk nama literal.

| Parameter | Pre-setup | Peran dan atribut penentu | Kunci fixture |
|---|---|---|---|
| `kw_unit_name` | - | keyword Search turunan: `Fixture.hardwareStock.p17.e[20].deviceName` tanpa karakter terakhir (Device Name unit nomor 20 tanpa digit satuan); cocok dengan Device Name unit nomor 20 sampai 28 saja (`p17.e[20]` sampai `p17.e[28]`, 9 baris) | `Fixture.hardwareStock.derived.unitNameKeyword` |
| `kw_unit_name_prefix` | - | keyword Search turunan: bagian `Fixture.hardwareStock.p17.e[10].deviceName` sebelum pemisah ` - ` (nama dasar Device Name); cocok dengan seluruh unit Tabel E `p17.e[10]` sampai `p17.e[28]` (19 baris) | `Fixture.hardwareStock.derived.unitNamePrefix` |
| `model_a2` | #16 (Tabel A baris ke-2) | Model/Type baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].modelType` |
| `sku_a2` | #16 (Tabel A baris ke-2) | kode SKU baris 2 Tabel A (#16): Handheld Reader Short Range, 12 Available | `Fixture.hardwareStock.p16.a[2].sku` |
| `sku_a4` | #16 (Tabel A baris ke-4) | kode SKU baris 4 Tabel A (#16): Handheld Reader Long Range, 18 Available dan 7 In Use (#17, #18) | `Fixture.hardwareStock.p16.a[4].sku` |
| `brand_pad` | #16 (SKU padding nomor 01) | Brand semua baris padding (#16) | `Fixture.hardwareStock.p16.a[9].brand` |
| `unit_10` | #17 (Tabel E baris N = 10) | Device Name unit nomor 10, Tabel E (#17) | `Fixture.hardwareStock.p17.e[10].deviceName` |
| `unit_20` | #17 (Tabel E baris N = 20) | Device Name unit nomor 20, Tabel E (#17) | `Fixture.hardwareStock.p17.e[20].deviceName` |
| `unit_27` | #17 (Tabel E baris N = 27) | Device Name unit nomor 27, Tabel E (#17) | `Fixture.hardwareStock.p17.e[27].deviceName` |
| `unit_28` | #17 (Tabel E baris N = 28) | Device Name unit nomor 28, Tabel E (#17) | `Fixture.hardwareStock.p17.e[28].deviceName` |
| `akun totalControlPrincipal` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email` |

- Data Dinamis (hanya TC-AC-ACHS-317; data milik spec karena TC menghapus unit dan Pre-setup SKU `Fixture.hardwareStock.p16.a[2].sku` dipakai approval lain, S-06): satu SKU Smart Fixed Reader milik spec dengan Brand `Fixture.hardwareStock.p16.a[9].brand` dan Model/Type `E2E288-{runId}` (`{runId}` terdiri atas digit) yang memiliki 12 unit Available (setara 12 unit Available SKU EDA51 pada TC). Seeding SKU dan 12 unit disediakan tim BE/FE di hook `before` spec ini tanpa endpoint karangan; hook `after` menghapus SKU dan unit yang tersisa.
- Data uji TC-AC-ACHS-307 (input nomor halaman tidak valid pada halaman 1 dari 2 halaman):

  | No | Input | Keterangan |
  |---|---|---|
  | 1 | `0` | nol |
  | 2 | `6` | melebihi halaman terakhir (halaman terakhir adalah 2) |
  | 3 | `abc` | bukan angka |

- Pilihan spec: TC-AC-ACHS-308 memakai keyword Search `Fixture.hardwareStock.derived.unitNamePrefix` (19 baris, 2 halaman) karena keyword `Fixture.hardwareStock.derived.unitNameKeyword` hanya menghasilkan 9 baris sehingga halaman 2 tidak ada; TC-AC-ACHS-309 memakai Filter Status = `Available`, sort Registered At Ascending, dan rows per page 25; TC-AC-ACHS-317 mencari SKU milik spec lewat Model/Type `E2E288-{runId}` (TC memakai Search `Fixture.hardwareStock.p16.a[2].modelType`).
- State global yang diubah: seed SKU milik spec dan penghapusan dua unit (langkah 46 dan 49). Search, sort, dan rows per page dipulihkan pada akhir tiap TC.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

1. Klik row action `Detail` pada SKU `Fixture.hardwareStock.p16.a[4].sku`
2. Klik Tab `Available`

### TC-AC-ACHS-305: Default dan opsi rows per page

3. Verifikasi tabel menampilkan 10 baris per halaman
4. Verifikasi info `Showing 1–10 of 19 entries`
5. Buka dropdown rows per page
6. Verifikasi opsi rows per page 10, 25, 50, 100 (tanpa opsi All)
7. Tutup dropdown rows per page

### TC-AC-ACHS-306: Next, input nomor halaman, dan ganti page size

8. Klik `Next`
9. Verifikasi info `Showing 11–19 of 19 entries`
10. Isi input halaman `1`, tekan Enter
11. Verifikasi info `Showing 1–10 of 19 entries`
12. Klik `Next`
13. Pilih rows per page 25
14. Verifikasi tabel kembali ke halaman 1 (info `Showing 1–19 of 19 entries`)
15. Pilih rows per page 10

### TC-AC-ACHS-307: Input nomor halaman tidak valid diabaikan

16. Untuk setiap baris tabel Data uji TC-AC-ACHS-307 (langkah 16 sampai 17): isi input halaman dengan nilai, tekan Enter
17. Verifikasi tabel tetap di halaman sekarang (info `Showing 1–10 of 19 entries`)

### TC-AC-ACHS-308: Search kembali ke halaman 1, ganti sort tetap di halaman sekarang

18. Klik `Next`
19. Ketik Search `Fixture.hardwareStock.derived.unitNamePrefix`, tekan Enter
20. Verifikasi tabel kembali ke halaman 1 (info `Showing 1–10 of 19 entries`)
21. Klik `Next`
22. Klik header Serial Number sekali
23. Verifikasi nomor halaman tidak berubah (info `Showing 11–19 of 19 entries`)
24. Klik header Serial Number dua kali sampai netral, klik `✕` pada Search, tekan Enter

### TC-AC-ACHS-309: Kombinasi empat kontrol dan recovery dari 0 hasil

25. Ketik Search `Fixture.hardwareStock.derived.unitNameKeyword`, tekan Enter
26. Klik icon Filter, isi Status = `Available`, klik `[Apply]`
27. Klik header Registered At sekali (Ascending)
28. Pilih rows per page 25
29. Verifikasi keyword `Fixture.hardwareStock.derived.unitNameKeyword` tetap terisi di kotak Search
30. Verifikasi badge titik tampil pada ikon Filter
31. Verifikasi indikator sort Ascending aktif pada Registered At
32. Verifikasi rows per page 25 terpilih
33. Verifikasi tabel menampilkan irisan Search dan Filter: 8 baris (`Fixture.hardwareStock.p17.e[20].deviceName` sampai `Fixture.hardwareStock.p17.e[27].deviceName`)
34. Ganti isi kotak search dengan `zzqx-tidak-ada`, tekan Enter
35. Verifikasi tampil `No results found`
36. Klik `✕` pada Search, tekan Enter
37. Verifikasi tabel hanya memuat unit berstatus `Available` (18 baris)
38. Verifikasi indikator sort Ascending tetap aktif pada Registered At
39. Verifikasi rows per page 25 tetap terpilih
40. Klik `[Clear Field]`, klik `[Apply]`, klik icon Filter untuk menutup panel, klik header Registered At dua kali sampai netral, pilih rows per page 10

### TC-AC-ACHS-317: Hapus baris terakhir di halaman terakhir

41. Buka Hardware > Stock, ketik Search `E2E288-{runId}`, tekan Enter
42. Klik row action `Detail` pada SKU milik spec, lalu klik Tab `Available`
43. Verifikasi info `Showing 1–10 of 12 entries`
44. Klik `Next`
45. Verifikasi halaman 2 berisi 2 baris (info `Showing 11–12 of 12 entries`)
46. Klik `(⋯)` pada baris pertama halaman 2, klik `Delete`, klik `[Delete]` pada dialog
47. Tunggu aksi selesai (tabel dimuat ulang)
48. Verifikasi halaman 2 berisi 1 baris (info `Showing 11–11 of 11 entries`)
49. Klik `(⋯)` pada baris tersisa halaman 2, klik `Delete`, klik `[Delete]` pada dialog
50. Verifikasi tabel pindah ke halaman 1 (halaman terakhir yang masih ada) dengan info `Showing 1–10 of 10 entries`

## Notes

- Sumber TC: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md`. (bagian 4b, Stock Detail Tab Available). Seluruh TC sumber spec ini dikerjakan di sini.
- Konfirmasi keyword Search terhadap nilai penuh Pre-setup (#8): keyword Search `Fixture.hardwareStock.derived.unitNameKeyword` (turunan `Fixture.hardwareStock.p17.e[20].deviceName` tanpa karakter terakhir) cocok dengan 9 baris unit nomor 20 sampai 28 (Tabel E, Pre-setup #17), dan `Fixture.hardwareStock.derived.unitNamePrefix` (turunan: nama dasar `Fixture.hardwareStock.p17.e[10].deviceName` sebelum pemisah ` - `) cocok dengan seluruh 19 baris Tab Available, sesuai asersi langkah 4, 9, 20, 23, dan 33. Tidak ada perbedaan.
- Urutan TC: 305 sampai 309 pada Detail `Fixture.hardwareStock.p16.a[4].sku`, lalu TC-AC-ACHS-317 paling akhir karena menghapus data (prinsip 5 bagian 3) pada SKU milik spec.
- Langkah 16 sampai 17 berulang untuk setiap baris tabel Data uji (tiga iterasi; bagian 8b butir 7).
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik Tab` `Available` pada langkah 2 dan 42 (menggantikan langkah TC "Pastikan Tab Available aktif", `[KEPUTUSAN 2026-11-02]`), pemulihan rows per page 10, sort netral, pengosongan Search, `[Clear Field]` dan `[Apply]`, penutupan panel Filter, pencarian SKU milik spec (langkah pertama TC-AC-ACHS-317 menemukan baris target), serta "Tunggu aksi selesai" setelah `[Delete]` pertama. Toast sukses Delete tidak diasersi karena Expected TC-AC-ACHS-317 tidak memintanya.
- Spec memiliki 50 langkah nominal dan 50 langkah setelah ekspansi perulangan, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (Pagination Stock Detail Tab Available), tiap TC berdiri sendiri sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna, ekspansi hanya dari satu perulangan input, dan TC yang menghapus data berada di akhir pada data milik spec.
- Temuan untuk QA:
  - Nomor spec ini (288) sesudah spec penulis (240 sampai 284), padahal spec membaca baseline Pre-setup dan `suite.md` bagian "Urutan jalan" menempatkan spec baca di bawah nomor 240. Spec tidak direnumber; syarat pemulihan baseline ditulis di `## Prerequisites`, dan keputusan penomoran (folder baru di bawah 240) menunggu keputusan di luar spec ini.
  - TC, PRD, dan LLD yang dibaca tidak menyebut apakah halaman Stock Detail punya flag Guided Tooltip sendiri; spec menyetel flag halaman Stock Detail seperti flag Stock List dengan kemampuan yang disediakan tim FE.
  - TC-AC-ACHS-306 langkah 6 menulis "klik Next jika ada halaman berikutnya" dan langkah 7 "pada halaman 2 ganti rows per page ke 10"; pada 25 baris per halaman 19 unit hanya satu halaman. Spec mengubah urutan: ganti page size dari halaman 2 (10 baris per halaman) ke 25 untuk menguji kembali ke halaman 1.
  - TC-AC-ACHS-308 judul menyebut "Search dan Apply Filter kembali ke halaman 1" tetapi langkah dan Expected hanya menguji Search; keyword TC `Fixture.hardwareStock.derived.unitNameKeyword` hanya 9 baris sehingga halaman 2 tidak ada; spec memakai `Fixture.hardwareStock.derived.unitNamePrefix` (19 baris).
  - TC-AC-ACHS-309 tidak menyebut nilai Filter dan kolom sort; spec memilih Status = `Available` dan Registered At (pilihan spec).
  - TC-AC-ACHS-317 menghapus dua unit SKU Pre-setup `Fixture.hardwareStock.p16.a[2].sku` (12 unit Available) yang juga dirujuk Subject Approvals Pre-setup; spec memakai SKU milik spec dengan 12 unit Available (S-06), dan Search `Fixture.hardwareStock.p16.a[2].modelType` diganti Model/Type bersuffix. Mekanisme seeding SKU dan 12 unit tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan "disediakan tim BE/FE". TC tidak menyebut nama dua baris yang dihapus; spec menghapus dua baris di halaman 2.
