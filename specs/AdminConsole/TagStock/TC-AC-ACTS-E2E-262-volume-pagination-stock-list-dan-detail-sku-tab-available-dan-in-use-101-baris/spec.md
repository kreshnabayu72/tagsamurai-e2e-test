---
id: TC-AC-ACTS-E2E-262-volume-pagination-stock-list-dan-detail-sku-tab-available-dan-in-use-101-baris
title: "Volume Pagination (101 Baris atau Lebih): Stock List, Detail SKU Tab Available, dan Detail SKU Tab In Use"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-66
  - TC-AC-ACTS-417
  - TC-AC-ACTS-463
coverage:
  web: automated
---

# Volume Pagination (101 Baris atau Lebih): Stock List, Detail SKU Tab Available, dan Detail SKU Tab In Use

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data Pre-setup (dibaca saja): Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS (Pre-setup #12 sampai #15 dan SKU pendukung); SKU `Fixture.tagStock.skuRfid` memiliki unit berstatus Available dan Damaged/Missing serta unit In Use milik beberapa Client.
- Data seed milik spec (volume kelas e; bersuffix `{runId}-262`, di-seed lewat API oleh fixture BE di hook `before`, dipulihkan atau dihapus di hook `after`): total sedikitnya 101 baris Stock List (TC-AC-ACTS-66); sedikitnya 101 unit berstatus Available dan Damaged/Missing pada SKU `Fixture.tagStock.skuRfid` untuk Tab Available (TC-AC-ACTS-417); sedikitnya 101 unit In Use milik beberapa Client dengan Status Available dan Damaged/Missing pada SKU yang sama untuk Tab In Use (TC-AC-ACTS-463).
- Tabel "Page size":

  | Ukuran |
  |---|
  | 25 |
  | 50 |
  | 100 |

- Kemampuan teknis: Fixture BE (seeding lewat API dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`); seed volume dipulihkan di hook `after` sehingga tidak dipakai spec lain.

## Test Steps

### TC-AC-ACTS-66: Pagination Stock List (volume 101 baris atau lebih)

1. Verifikasi footer pagination menampilkan default 10 baris per halaman
2. Verifikasi teks footer berformat `Showing [From]–[To] of [Total] entries`
3. Buka pilihan Rows per page
4. Verifikasi pilihan page size hanya 10, 25, 50, 100 (tanpa opsi All)
Langkah 5 sampai 6 diulang untuk setiap baris tabel "Page size" pada Prerequisites (3 iterasi).

5. Pilih page size `<Ukuran>`
6. Verifikasi jumlah baris yang tampil mengikuti page size `<Ukuran>`
7. Klik `[Next →]`
8. Verifikasi tabel berpindah ke halaman berikutnya
9. Klik `[← Prev]`
10. Verifikasi tabel kembali ke halaman sebelumnya
11. Isi input halaman dengan 2, tekan Enter
12. Verifikasi tabel berpindah ke halaman 2

13. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
14. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`; pastikan Tab `Available` aktif

### TC-AC-ACTS-417: Pagination Detail SKU Tab Available (volume 101 baris atau lebih)

15. Verifikasi footer pagination menampilkan default 10 baris per halaman
16. Verifikasi teks footer berformat `Showing [From]–[To] of [Total] entries`
17. Buka pilihan Rows per page
18. Verifikasi pilihan page size hanya 10, 25, 50, 100 (tanpa opsi All)
Langkah 19 sampai 20 diulang untuk setiap baris tabel "Page size" pada Prerequisites (3 iterasi).

19. Pilih page size `<Ukuran>`
20. Verifikasi jumlah baris yang tampil mengikuti page size `<Ukuran>`
21. Klik `[Next →]`
22. Verifikasi tabel berpindah ke halaman berikutnya
23. Klik `[← Prev]`
24. Verifikasi tabel kembali ke halaman sebelumnya
25. Isi input halaman dengan 2, tekan Enter
26. Verifikasi tabel berpindah ke halaman 2

27. Klik Tab `In Use`

### TC-AC-ACTS-463: Pagination Detail SKU Tab In Use (volume 101 baris atau lebih)

28. Verifikasi footer pagination menampilkan default 10 baris per halaman
29. Verifikasi teks footer berformat `Showing [From]–[To] of [Total] entries`
30. Buka pilihan Rows per page
31. Verifikasi pilihan page size hanya 10, 25, 50, 100 (tanpa opsi All)
Langkah 32 sampai 33 diulang untuk setiap baris tabel "Page size" pada Prerequisites (3 iterasi).

32. Pilih page size `<Ukuran>`
33. Verifikasi jumlah baris yang tampil mengikuti page size `<Ukuran>`
34. Klik `[Next →]`
35. Verifikasi tabel berpindah ke halaman berikutnya
36. Klik `[← Prev]`
37. Verifikasi tabel kembali ke halaman sebelumnya
38. Isi input halaman dengan 2, tekan Enter
39. Verifikasi tabel berpindah ke halaman 2

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah (39 langkah); alasan: semua blok satu kelas harness (kelas e, volume 101 baris atau lebih) dengan pola pagination yang sama pada tiga tabel yang berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah tiap blok dua belas dengan perulangan page size.
- Pagination volume pada permukaan lain: TC-AC-ACTS-509, 602, dan 646 ada di spec 263, TC-AC-ACTS-919 di spec 242.
- Perulangan bagian 8b butir 7: langkah 5 sampai 6, 19 sampai 20, dan 32 sampai 33 diulang untuk setiap baris tabel "Page size" (3 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Langkah penghubung (S-03): langkah 13 (Search SKU untuk menemukan baris target di Stock List berisi 101 baris atau lebih, R-16), langkah 14 (row action `Detail`), dan langkah 27 (berpindah ke Tab `In Use`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun perlu dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-66, 417, dan 463 langkah "Pilih 25 lalu 50 lalu 100" tidak menyebut Expected jumlah baris per pilihan; spec mengasersi jumlah baris mengikuti page size terpilih (Expected c). TC-AC-ACTS-66 Precondition b menyebut minimal 5 SKU sedangkan Test Data meminta minimal 101 baris; spec memakai 101 baris. TC-AC-ACTS-66 butir a menulis `Showing [From]–[To] of [Total] entries` sebagai pola; spec mengasersi pola tersebut.
