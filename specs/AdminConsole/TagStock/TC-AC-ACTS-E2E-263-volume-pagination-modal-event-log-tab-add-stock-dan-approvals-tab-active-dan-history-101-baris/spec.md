---
id: TC-AC-ACTS-E2E-263-volume-pagination-modal-event-log-tab-add-stock-dan-approvals-tab-active-dan-history-101-baris
title: "Volume Pagination (101 Baris atau Lebih): Modal Event Log Tab Add Stock serta Approvals Tab Active dan Tab History"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-509
  - TC-AC-ACTS-602
  - TC-AC-ACTS-646
coverage:
  web: automated
---

# Volume Pagination (101 Baris atau Lebih): Modal Event Log Tab Add Stock serta Approvals Tab Active dan Tab History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed milik spec (volume kelas e; bersuffix `{runId}-263`, di-seed lewat API oleh fixture BE di hook `before`, dipulihkan atau dihapus di hook `after`): sedikitnya 101 sesi Add Stock dan Delete Stock di Event Log SKU `Fixture.tagStock.skuRfid` (TC-AC-ACTS-509); sedikitnya 101 baris Subject Register Duplicate dan Activation Collision di Approvals > TAG Stock > Tab Active (TC-AC-ACTS-602); sedikitnya 101 baris Subject Approved, Rejected, dan Canceled di Tab History (TC-AC-ACTS-646).
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

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-509: Pagination modal Event Log (Tab Add Stock) (volume 101 baris atau lebih)

4. Verifikasi footer pagination menampilkan default 10 baris per halaman
5. Verifikasi teks footer berformat `Showing [From]–[To] of [Total] entries`
6. Buka pilihan Rows per page
7. Verifikasi pilihan page size hanya 10, 25, 50, 100 (tanpa opsi All)
Langkah 8 sampai 9 diulang untuk setiap baris tabel "Page size" pada Prerequisites (3 iterasi).

8. Pilih page size `<Ukuran>`
9. Verifikasi jumlah baris yang tampil mengikuti page size `<Ukuran>`
10. Klik `[Next →]`
11. Verifikasi tabel berpindah ke halaman berikutnya
12. Klik `[← Prev]`
13. Verifikasi tabel kembali ke halaman sebelumnya
14. Isi input halaman dengan 2, tekan Enter
15. Verifikasi tabel berpindah ke halaman 2

16. Tutup modal Event Log dengan klik (X)
17. Buka Approvals > TAG Stock lewat sidebar
18. Klik Tab `Active`

### TC-AC-ACTS-602: Pagination Approvals > TAG Stock > Tab Active (volume 101 baris atau lebih)

19. Verifikasi footer pagination menampilkan default 10 baris per halaman
20. Verifikasi teks footer berformat `Showing [From]–[To] of [Total] entries`
21. Buka pilihan Rows per page
22. Verifikasi pilihan page size hanya 10, 25, 50, 100 (tanpa opsi All)
Langkah 23 sampai 24 diulang untuk setiap baris tabel "Page size" pada Prerequisites (3 iterasi).

23. Pilih page size `<Ukuran>`
24. Verifikasi jumlah baris yang tampil mengikuti page size `<Ukuran>`
25. Klik `[Next →]`
26. Verifikasi tabel berpindah ke halaman berikutnya
27. Klik `[← Prev]`
28. Verifikasi tabel kembali ke halaman sebelumnya
29. Isi input halaman dengan 2, tekan Enter
30. Verifikasi tabel berpindah ke halaman 2

31. Klik Tab `History`

### TC-AC-ACTS-646: Pagination Approvals > TAG Stock > Tab History (volume 101 baris atau lebih)

32. Verifikasi footer pagination menampilkan default 10 baris per halaman
33. Verifikasi teks footer berformat `Showing [From]–[To] of [Total] entries`
34. Buka pilihan Rows per page
35. Verifikasi pilihan page size hanya 10, 25, 50, 100 (tanpa opsi All)
Langkah 36 sampai 37 diulang untuk setiap baris tabel "Page size" pada Prerequisites (3 iterasi).

36. Pilih page size `<Ukuran>`
37. Verifikasi jumlah baris yang tampil mengikuti page size `<Ukuran>`
38. Klik `[Next →]`
39. Verifikasi tabel berpindah ke halaman berikutnya
40. Klik `[← Prev]`
41. Verifikasi tabel kembali ke halaman sebelumnya
42. Isi input halaman dengan 2, tekan Enter
43. Verifikasi tabel berpindah ke halaman 2

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah (43 langkah); alasan: semua blok satu kelas harness (kelas e, volume 101 baris atau lebih) dengan pola pagination yang sama pada tiga tabel yang berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; jumlah langkah tiap blok dua belas dengan perulangan page size.
- Pagination volume pada permukaan lain: TC-AC-ACTS-66, 417, dan 463 ada di spec 262, TC-AC-ACTS-919 di spec 242.
- Perulangan bagian 8b butir 7: langkah 8 sampai 9, 23 sampai 24, dan 36 sampai 37 diulang untuk setiap baris tabel "Page size" (3 iterasi); parameter tiap iterasi ada di tabel itu pada Prerequisites, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa.
- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), langkah 16 (menutup modal Event Log sebelum pindah surface, S-09), langkah 17 dan 18 (membuka Approvals > TAG Stock dan Tab `Active`), dan langkah 31 (Tab `History`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-509, 602, dan 646 langkah "Pilih 25 lalu 50 lalu 100" tidak menyebut Expected jumlah baris per pilihan; spec mengasersi jumlah baris mengikuti page size terpilih (Expected c).
