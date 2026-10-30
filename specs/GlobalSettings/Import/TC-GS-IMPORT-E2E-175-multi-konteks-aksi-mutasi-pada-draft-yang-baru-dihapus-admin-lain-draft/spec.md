---
id: TC-GS-IMPORT-E2E-175-multi-konteks-aksi-mutasi-pada-draft-yang-baru-dihapus-admin-lain-draft
title: "Multi-konteks: aksi mutasi pada draft yang baru dihapus admin lain (Draft Tidak Ditemukan), tujuh tab, dan Delete All Rows kategori yang sudah dihapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-542
  - TC-GS-IMPORT-543
  - TC-GS-IMPORT-544
coverage:
  web: automated
---

# Multi-konteks: aksi mutasi pada draft yang baru dihapus admin lain (Draft Tidak Ditemukan), tujuh tab, dan Delete All Rows kategori yang sudah dihapus

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Import dibagikan ke seluruh admin satu client dan spec mengubah state global (mode mock AI, jam server untuk umur draft dan kunci sesi edit); lihat `suite.md`.
- Konteks browser (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite). Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach` untuk Sesi A:
  - Sesi A (aktor): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`. Pada TC-542 Sesi A membuka tujuh tab peramban dalam sesi login yang sama, ditandai `[Tab 1]` sampai `[Tab 7]`.
  - Sesi B (administrator lain, sesi UI kedua yang hasilnya diasersi pada TC-543 dan TC-544): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC2_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Pada TC-542 Admin kedua hanya memicu Discard Draft lewat sesi API (hasil di sesi itu tidak diasersi; P-2).
  - Pada blok Client D (TC-543), kedua sesi ganti akun eksplisit: Total Control Client D (Wulan Sari) `totalControl_automated_qaTeam4@qwertysystem.net`, `Spectra.env.GS_CLIENTD_TC_PASSWORD` (Sesi A) dan Admin kedua Client D (Putra Mahendra) `totalControlSecond_automated_qaTeam4@qwertysystem.net`, `Spectra.env.GS_CLIENTD_TC2_PASSWORD` (Sesi B).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk setiap akun UI spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Banyak tab peramban dalam satu sesi login (tujuh tab pada TC-542) dan dua konteks browser paralel.
  - Fixture timestamp kunci sesi edit: mengatur kedaluwarsa kunci sesi edit Total Control ke waktu yang sudah lewat (TC-542 langkah 11).
  - Hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam) agar Unsaved Banner dan `[Discard]` tampil (TC-542).
  - Sesi API Admin kedua Client A untuk Discard Draft (TC-542).
  - Mock layanan AI deterministik mode normal D-40 (tabel D-41 dan D-42).
  - Skrip fixture pemulihan draft dasar (D-09 Client A, D-65 Client D, Kontrak Fixture R2).
- Data Dinamis (milik spec ini; Population Client A, nama literal karena asersi urutan baris; seeding idempotent dan dipulihkan sebelum tiap TC): D-09 draft Brand 13 baris Client A (12 `pending` dari D-01 dan Row # 13 `error` dengan badge saran AI "AI suggestion: 'Samsung Electronics Indonesia'?") untuk TC-542 dan TC-544; D-65 draft Brand 2 baris `pending` Client D (Row # 1 `Nikon`, Row # 2 `Ricoh`) untuk TC-543.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan jam server dan kedaluwarsa kunci, kembalikan mock AI ke normal, hapus draft Client A dan Client D, tutup tab dan konteks tambahan, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-542: Aksi mutasi pada draft yang baru dihapus admin lain di tujuh tab

1. Pulihkan draft dasar Client A D-09 (13 baris) dengan hook umur draft D-76 varian 1 lewat skrip fixture; pastikan mock AI mode normal
2. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab Brand pada tujuh tab peramban ([Tab 1] sampai [Tab 7])
3. [Sesi A] Verifikasi draft tampil di setiap tab
4. [Tab 3] Klik row action `⋯` pada Row # 2 lalu Remove (Dialog Delete Row terbuka)
5. [Tab 4] Centang checkbox Row # 3
6. [Tab 4] Centang checkbox Row # 4
7. [Tab 4] Klik `[Delete]` pada Bulk Action Bar (Dialog Delete Rows terbuka)
8. [Tab 6] Klik kartu Errors
9. [Tab 6] Verifikasi Row # 13 tampil dengan badge saran AI
10. [Tab 7] Klik kartu Errors
11. [Tab 7] Verifikasi Row # 13 tampil dengan badge saran AI
12. [Tab 1] Klik row action `⋯` pada Row # 1 lalu Edit (sesi edit dimulai)
13. [Tab 1] Ubah Brand Name Row # 1 menjadi `Acme Corp 2` tanpa menyimpan
14. Atur kedaluwarsa kunci sesi edit Sesi A ke waktu yang sudah lewat lewat fixture timestamp
15. Discard Draft atas nama Admin kedua Client A lewat sesi API (setara klik `[Discard]` pada Unsaved Banner lalu `[Discard Draft]`)
16. [Tab 1] Klik `[Save]`
17. [Tab 1] Verifikasi toast netral "This draft is no longer available."
18. [Tab 1] Verifikasi Dropzone tampil (kembali ke state belum ada draft)
19. [Tab 1] Tutup toast
20. [Tab 2] Klik `[Import (12)]`
21. [Tab 2] Verifikasi toast netral "This draft is no longer available."
22. [Tab 2] Verifikasi Dropzone tampil
23. [Tab 2] Tutup toast
24. [Tab 3] Klik `[Delete]` pada Dialog Delete Row
25. [Tab 3] Verifikasi toast netral "This draft is no longer available."
26. [Tab 3] Verifikasi Dropzone tampil
27. [Tab 3] Tutup toast
28. [Tab 4] Klik `[Delete]` pada Dialog Delete Rows
29. [Tab 4] Verifikasi toast netral "This draft is no longer available."
30. [Tab 4] Verifikasi Dropzone tampil
31. [Tab 4] Tutup toast
32. [Tab 5] Klik `[Delete All Rows]` pada baris pesan `Brand Name: Max. 120 characters`
33. [Tab 5] Verifikasi toast netral "This draft is no longer available."
34. [Tab 5] Verifikasi Dropzone tampil
35. [Tab 5] Tutup toast
36. [Tab 6] Klik `[Accept]` pada badge saran AI Row # 13
37. [Tab 6] Verifikasi toast netral "This draft is no longer available."
38. [Tab 6] Verifikasi Dropzone tampil
39. [Tab 6] Tutup toast
40. [Tab 7] Klik `[Dismiss]` pada badge saran AI Row # 13
41. [Tab 7] Verifikasi toast netral "This draft is no longer available."
42. [Tab 7] Verifikasi Dropzone tampil

### TC-GS-IMPORT-544: Delete All Rows pada kategori yang sudah dihapus admin lain

43. Pulihkan draft dasar Client A D-09 (13 baris dengan 1 baris `error`) lewat skrip fixture; pastikan mock AI mode normal
44. [Sesi A] Tutup tab tambahan dan muat ulang halaman Import > Brand
45. [Sesi B] Buka Global Settings > Import, pilih Sub-Tab Brand (halaman dibiarkan terbuka dengan Callout memuat baris pesan `Brand Name: Max. 120 characters`)
46. [Sesi A] Klik `[Delete All Rows]` pada baris pesan `Brand Name: Max. 120 characters`
47. [Sesi A] Verifikasi toast sukses "Success, row has been deleted."
48. [Sesi A] Verifikasi baris error terhapus
49. [Sesi A] Verifikasi Staging Metric Cards Total Rows 12
50. [Sesi A] Verifikasi Staging Metric Cards Ready to Import 12
51. [Sesi A] Verifikasi Staging Metric Cards Errors 0
52. [Sesi A] Tutup toast
53. [Sesi B] Klik `[Delete All Rows]` pada baris pesan yang sama di halaman yang dibiarkan terbuka
54. [Sesi B] Verifikasi tidak muncul toast error "Error, failed to delete row."
55. [Sesi B] Verifikasi tidak muncul dialog
56. [Sesi B] Muat ulang halaman Import > Brand
57. [Sesi B] Verifikasi draft berisi 12 baris `pending` dengan Staging Metric Cards Total Rows 12
58. [Sesi B] Verifikasi Staging Metric Cards Errors 0 sama seperti langkah 51

### TC-GS-IMPORT-543: Hapus baris terakhir lalu admin kedua mengulang Bulk Delete

59. [Sesi A] Ganti akun: logout, lalu login sebagai Total Control Client D (Wulan Sari)
60. [Sesi B] Ganti akun: logout, lalu login sebagai Admin kedua Client D (Putra Mahendra)
61. Reset Client D lewat skrip fixture dan seed draft Brand D-65 (2 baris `pending`: `Nikon`, `Ricoh`)
62. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab Brand
63. [Sesi A] Centang checkbox Row # 1
64. [Sesi A] Centang checkbox Row # 2
65. [Sesi B] Buka Global Settings > Import, pilih Sub-Tab Brand (halaman dibiarkan terbuka)
66. [Sesi B] Centang checkbox Row # 1
67. [Sesi B] Centang checkbox Row # 2
68. [Sesi A] Klik `[Delete]` pada Bulk Action Bar
69. [Sesi A] Klik `[Delete]` pada Dialog Delete Rows
70. [Sesi A] Verifikasi toast sukses "Success, row has been deleted."
71. [Sesi A] Verifikasi Dropzone tampil
72. [Sesi B] Klik `[Delete]` pada Bulk Action Bar di halaman yang dibiarkan terbuka
73. [Sesi B] Klik `[Delete]` pada Dialog Delete Rows
74. [Sesi B] Verifikasi toast netral "This draft is no longer available."
75. [Sesi B] Verifikasi Dropzone tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (c); objek uji adalah halaman terbuka yang basi sesudah draft dihapus admin lain. Discard Draft Admin kedua pada TC-542 hanya pemicu lewat sesi API (P-2); jam server dan fixture kunci hanya pemicu.
- Alasan melewati sekitar 35 langkah (75 langkah nominal): tiga blok satu kelas multi-konteks yang berdiri sendiri; TC-542 memakai tujuh tab (tujuh aksi homogen yang masing-masing mengasersi toast dan Dropzone, 28 langkah di antaranya satu tab satu aksi). Blok Client D (TC-543) memakai ganti akun eksplisit di dua sesi (langkah 59 dan 60), sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok: TC-542, TC-544 (Client A), lalu TC-543 (Client D). Tiap blok memulihkan draft sendiri.
- Langkah penghubung (tanpa `Verifikasi`): pemulihan draft (langkah 1, 43, 61), pembukaan halaman dan Sub-Tab, centang dan klik pemicu (langkah 4 sampai 8, 10, 12, 13), fixture kedaluwarsa kunci (langkah 14), Discard Draft Admin kedua (langkah 15), menutup toast antar-asersi (S-09; langkah 19, 23, 27, 31, 35, 39, 52), serta ganti akun (langkah 59 dan 60). Langkah 3, 9, 11 adalah `Verifikasi` tambahan di luar Expected TC-542 yang membuktikan prasyarat (draft tampil di tiap tab; badge saran AI tampil di tab 6 dan 7).
- Langkah 54 dan 55 adalah asersi absence state sementara (toast error dan dialog) segera setelah pemicu langkah 53; langkah 57 dan 58 membuktikan draft akhir pada surface yang sama.
- Temuan untuk QA:
  - TC-GS-IMPORT-542 Expected a sampai g menyebut "ditolak server 404" tetapi Langkah TC melakukan aksi lewat UI sehingga status 404 tidak teramati tanpa intercept; spec hanya mengasersi toast netral "This draft is no longer available." dan Dropzone, yaitu akibat yang teramati di UI.
  - TC-GS-IMPORT-542 menyebut Admin kedua membuka halaman dan mengklik `[Discard]` serta `[Discard Draft]` lewat UI; spec memakai sesi API (P-2) karena hasil di sesi itu tidak diasersi. Menunggu konfirmasi QA.
  - TC-GS-IMPORT-542 memakai tujuh tab dalam satu sesi login; aturan "satu sesi per tab" tidak dinyatakan, sehingga spec mengasumsikan sesi login dibagikan antar-tab.
  - TC-GS-IMPORT-542 tidak menyebut apa yang terjadi pada sesi edit Tab 1 selain Save ditolak; spec hanya mengasersi toast dan Dropzone sesuai Expected a.
  - Post Condition semua TC di spec ini "-" dan tidak ada keadaan yang perlu dipulihkan selain yang dikerjakan hook `after`.
