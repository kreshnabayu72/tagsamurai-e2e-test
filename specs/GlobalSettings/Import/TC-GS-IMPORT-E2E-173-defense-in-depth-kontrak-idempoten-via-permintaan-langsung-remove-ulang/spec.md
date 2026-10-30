---
id: TC-GS-IMPORT-E2E-173-defense-in-depth-kontrak-idempoten-via-permintaan-langsung-remove-ulang
title: "Defense-in-depth: kontrak idempoten via permintaan langsung (Remove ulang, AI Accept ulang, acquire kunci ditolak 409, AI Accept/Dismiss pada baris terhapus)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-545
  - TC-GS-IMPORT-546
  - TC-GS-IMPORT-548
  - TC-GS-IMPORT-841
coverage:
  web: automated
---

# Defense-in-depth: kontrak idempoten via permintaan langsung (Remove ulang, AI Accept ulang, acquire kunci ditolak 409, AI Accept/Dismiss pada baris terhapus)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): draft Client A dibagikan ke seluruh admin dan mode mock AI adalah state global; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach`.
- Pelaku kedua: Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC2_PASSWORD`, memakai sesi API (request langsung): pada TC-548 permintaan mulai sesi edit adalah objek uji (respons 409), pada TC-841 permintaan Remove hanya memicu state (P-2). Tidak ada sesi UI kedua karena tidak ada hasil yang diasersi di UI Admin kedua.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Klien HTTP yang mengirim request langsung ke server dengan token sesi akun aktor atau Admin kedua (Remove, AI Accept, AI Dismiss, mulai sesi edit, release kunci); pengenal baris diambil dari respons pembacaan Staging Table. Asersi request langsung hanya respons server dan state data (butir 1 bagian 8b).
  - Mock layanan AI deterministik mode normal D-40 (tabel D-41 dan D-42) yang mencatat jumlah permintaan.
  - Skrip fixture pemulihan draft dasar Client A (D-01 dan D-09, Kontrak Fixture R2).
- Data Dinamis (milik spec ini; Population Client A, nama literal karena asersi urutan baris; seeding idempotent dan dipulihkan sebelum tiap TC):
  - D-01 draft Brand 12 baris `pending`: `Acme Corp` (#1), `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus` (TC-545, 548).
  - D-09 draft Brand 13 baris: D-01 ditambah baris #13 `error` dengan Brand Name 121 karakter (nilai sumber Brand pertama tabel D-41), badge saran AI "AI suggestion: 'Samsung Electronics Indonesia'?" (TC-546, 841).
  - Tabel "Varian permintaan" TC-841 (langkah 42 sampai 52 diulang untuk setiap baris):

    | Varian | Permintaan langsung oleh Total Control |
    |---|---|
    | 1 | AI Accept |
    | 2 | AI Dismiss |

- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): batalkan sesi edit yang masih aktif, pulihkan draft dasar Client A, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-545: Remove idempoten

1. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
2. Ambil pengenal baris Row # 3 dari respons pembacaan Staging Table
3. Kirim permintaan Remove langsung ke server dengan token akun Total Control untuk pengenal baris itu
4. Verifikasi server membalas sukses pada permintaan Remove pertama
5. Kirim permintaan Remove yang sama sekali lagi
6. Verifikasi server membalas sukses pada permintaan Remove kedua tanpa efek samping
7. Buka Global Settings > Import, pilih Sub-Tab Brand, lalu muat ulang halaman
8. Verifikasi draft berisi 11 baris (kartu Total Rows 11)
9. Verifikasi baris yang semula Row # 4 (`Honeywell`) kini bernomor Row # 3

### TC-GS-IMPORT-546: AI Accept idempoten

10. Pulihkan draft dasar Client A D-09 (Brand 13 baris) lewat skrip fixture; pastikan mock AI mode normal
11. Muat ulang halaman Import > Brand
12. Klik halaman 2 pada Pagination
13. Ambil pengenal baris Row # 13 dari respons pembacaan Staging Table halaman 2
14. Kirim permintaan AI Accept langsung ke server dengan token akun Total Control untuk pengenal baris itu
15. Verifikasi server menjawab sukses pada permintaan AI Accept pertama
16. Muat ulang halaman Import > Brand
17. Klik halaman 2 pada Pagination
18. Verifikasi Row # 13 bernilai `Samsung Electronics Indonesia`
19. Verifikasi Row # 13 berstatus `pending`
20. Verifikasi Staging Metric Cards: Total Rows 13, Ready to Import 13, Errors 0
21. Kirim permintaan AI Accept yang sama sekali lagi dengan token akun Total Control
22. Verifikasi server menjawab sukses tanpa mengubah state
23. Muat ulang halaman Import > Brand
24. Klik halaman 2 pada Pagination
25. Verifikasi Row # 13 tetap bernilai `Samsung Electronics Indonesia` berstatus `pending`
26. Verifikasi Staging Metric Cards tetap Total Rows 13, Ready to Import 13, Errors 0 seperti setelah langkah 20

### TC-GS-IMPORT-548: Acquire kunci oleh Admin kedua ditolak 409 dan release kunci yang sudah lepas tidak berefek

27. Pulihkan draft dasar Client A D-01 (Brand 12 baris `pending`) lewat skrip fixture
28. Muat ulang halaman Import > Brand
29. Klik row action `⋯` pada Row # 1 lalu Edit (sesi edit dimulai)
30. Kirim permintaan mulai sesi edit langsung ke server dengan token akun Admin kedua Client A
31. Verifikasi server menolak permintaan dengan 409 Conflict
32. Kirim permintaan mulai sesi edit yang sama sekali lagi dengan token akun Admin kedua Client A
33. Verifikasi server menolak permintaan dengan 409 Conflict
34. Verifikasi sesi edit Total Control masih aktif (input sel masih dapat disunting)
35. Klik `[Cancel]` tanpa mengubah nilai
36. Kirim permintaan release kunci langsung ke server dengan token akun Total Control
37. Verifikasi server membalas tanpa error dan tanpa efek samping (kunci tetap bebas)
38. Klik row action `⋯` pada Row # 1 lalu Edit
39. Verifikasi sesi edit dimulai tanpa dialog Konflik Kunci Sesi
40. Klik `[Cancel]` tanpa mengubah nilai (pemulihan sesi edit)

### TC-GS-IMPORT-841: AI Accept dan AI Dismiss pada baris yang sudah dihapus admin lain

41. Untuk setiap baris tabel "Varian permintaan", lakukan langkah 42 sampai 52 (dua iterasi)
42. Pulihkan draft dasar Client A D-09 (Brand 13 baris) lewat skrip fixture; pastikan mock AI mode normal
43. Muat ulang halaman Import > Brand
44. Klik halaman 2 pada Pagination
45. Ambil pengenal baris Row # 13 dari respons pembacaan Staging Table halaman 2
46. Kirim permintaan Remove langsung ke server dengan token akun Admin kedua Client A untuk pengenal baris itu
47. Verifikasi server membalas sukses pada permintaan Remove Admin kedua
48. Kirim permintaan varian (AI Accept atau AI Dismiss sesuai baris tabel) langsung ke server dengan token akun Total Control untuk pengenal baris itu
49. Verifikasi server membalas sukses tanpa efek samping
50. Muat ulang halaman Import > Brand
51. Verifikasi Staging Metric Cards: Total Rows 12 (Active), Ready to Import 12, Errors 0 (Disabled), Duplicates 0 (Disabled)
52. Verifikasi Pagination "Showing 1 - 10 of 12 items"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: defense-in-depth (a); objek uji adalah kontrak idempoten pada request langsung. Admin kedua hanya memicu state lewat sesi API (P-2) kecuali pada TC-548 di mana permintaannya adalah objek uji.
- Alasan melewati sekitar 35 langkah (52 langkah nominal; ekspansi langkah 42 sampai 52 dikali dua iterasi memberi sekitar 61 langkah): empat blok homogen (request langsung dengan reset draft Client A di awal tiap blok), semua satu kelas dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah 42 sampai 52 diulang untuk setiap baris tabel "Varian permintaan" tanpa langkah bersyarat dan `Verifikasi` tetap satu per klausa.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok mengikuti TC.
- Langkah penghubung (tanpa `Verifikasi`): pemulihan draft (langkah 1, 10, 27, 42), pembukaan halaman dan Sub-Tab, pengambilan pengenal baris (langkah 2, 13, 45), pindah halaman (langkah 12, 17, 24, 44), dan membatalkan sesi edit (langkah 35, 40). Langkah 34 (sesi edit masih aktif) diasersi sebelum langkah 35 yang mengubah state (butir 5 bagian 8b).
- Asersi request langsung hanya respons server dan state data; langkah muat ulang dan pembacaan UI sesudahnya mengamati state data (nilai Row # 13, jumlah baris), bukan perilaku FE atas respons.
- Temuan untuk QA:
  - TC-GS-IMPORT-548 langkah 2 dan 3 memakai Admin kedua Client A sebagai pelaku request langsung yang ditolak 409; spec memakai sesi API Admin kedua karena yang diasersi hanya respons server. Langkah 1 TC memulai sesi edit lewat UI Total Control (dipertahankan).
  - TC-GS-IMPORT-841 menyebut dua varian dalam kolom Data dan satu Expected; spec mengulang langkah per varian dengan pemulihan D-09 di antaranya (Post Condition TC: "dibuat ulang ke D-09 sebelum varian berikutnya").
  - TC-GS-IMPORT-545 dan TC-GS-IMPORT-548 tidak menyebut cara memverifikasi bahwa permintaan kedua "tanpa efek samping" selain respons sukses dan state akhir; spec mengasersi respons dan state akhir.
  - TC-GS-IMPORT-546 dan TC-GS-IMPORT-841 mengasersi jumlah baris pada Staging Metric Cards sebagai state data, bukan perilaku FE atas respons.
  - Post Condition semua TC di spec ini "-" kecuali TC-GS-IMPORT-548 (sesi edit dibatalkan dengan `[Cancel]`, dikerjakan langkah 40) dan TC-GS-IMPORT-841 (draft 12 baris `pending`, dipulihkan langkah 42 pada iterasi berikutnya).
