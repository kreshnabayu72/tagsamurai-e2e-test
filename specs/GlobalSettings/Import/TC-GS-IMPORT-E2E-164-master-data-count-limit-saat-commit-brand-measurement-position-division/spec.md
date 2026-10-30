---
id: TC-GS-IMPORT-E2E-164-master-data-count-limit-saat-commit-brand-measurement-position-division
title: "Master Data Count Limit saat commit (Brand, Measurement, Position, Division): baris melampaui kuota jadi error; limit diubah lalu commit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-404
  - TC-GS-IMPORT-405
  - TC-GS-IMPORT-406
  - TC-GS-IMPORT-407
  - TC-GS-IMPORT-750
coverage:
  web: automated
---

# Master Data Count Limit saat commit (Brand, Measurement, Position, Division): baris melampaui kuota jadi error; limit diubah lalu commit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai kuota Master Data Count Limit Client Limit (seed 999 record per katalog) yang dibagikan dengan spec batas kuota lain, mengubah state global (System Limits Brand pada TC-750) dan draft Client Limit dibagikan ke seluruh admin; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client Limit (Bima Saputra) `totalControl_automated_qaTeam7@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTLIMIT_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client Limit dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Skrip seed R7/D-46: Client Limit memakai Master Data Count Limit minimum 1000 per katalog; 999 record per katalog tersimpan (nama `Seed [Entity] nnnn`, mis. `Seed Brand 0001`), sisa 1 slot; seed dan draft 2 baris dibuat ulang sebelum tiap TC dan dipulihkan sesudahnya.
  - Fixture Admin Console untuk mengubah System Limits (akun Total Control Client Limit tidak memiliki akses Admin Console): Master Data Count Limit Brand 1000 menjadi 1100 (TC-750) dan memulihkannya ke 1000. Akun administrator Admin Console disediakan tim FE.
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job commit latar belakang selesai (bukan menunggu jam).
- Data Dinamis (milik spec ini; nama sesuai Data Uji TC karena asersi Search mencocokkan nama persis; hook `before` membersihkan sisa nama itu dari run sebelumnya dan hook `after` menghapus yang dibuat spec): tabel "Berkas batas kuota" (langkah 2 sampai 15 diulang untuk TC-404 sampai TC-407):

  | TC | Sub-Tab | Berkas | Baris #1 | Baris #2 (melampaui kuota) | Halaman master | Pesan Callout |
  |---|---|---|---|---|---|---|
  | 404 | Brand | `brand-cap-2.csv` (Brand Name) | `Nikon` | `Pentax` | Master Reference > Brand | "You've reached the platform limit of 1000 brands. Contact support if you need a higher limit." |
  | 405 | Measurement | `measurement-cap-2.csv` (Unit Name, Symbol) | `Meter` (`m`) | `Liter` (`l`) | Master Reference > Measurement | "You've reached the platform limit of 1000 units. Contact support if you need a higher limit." |
  | 406 | Position | `position-cap-2.csv` (Position Name) | `Store Supervisor` | `Warehouse Staff` | User > Position | "You've reached the platform limit of 1000 positions. Contact support if you need a higher limit." |
  | 407 | Division | `division-cap-2.csv` (Division Name, Code) | `Finance & Accounting` (`FIN`) | `Legal` (`LGL`) | User > Division | "You've reached the platform limit of 1000 divisions. Contact support if you need a higher limit." |

- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan Master Data Count Limit Brand ke 1000, kembalikan seed tiap katalog Client Limit ke 999 (hapus `Nikon`, `Pentax`, `Meter`, `Store Supervisor`, `Finance & Accounting` dan record hasil commit lain), hapus draft Client Limit, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-404 sampai TC-GS-IMPORT-407: Commit melampaui kuota menjadi error (Brand, Measurement, Position, Division)

1. Untuk setiap baris tabel "Berkas batas kuota" pada Prerequisites (TC-404, 405, 406, 407), lakukan langkah 2 sampai 15 (empat iterasi)
2. Reset Client Limit lewat skrip fixture: Master Data Count Limit katalog sub-tab 1000 dengan 999 record tersimpan (sisa 1 slot), tanpa draft pada sub-tab itu; seed draft 2 baris `pending` dari berkas baris tabel
3. Buka Global Settings > Import, pilih Sub-Tab sesuai baris tabel
4. Klik `[Import (2)]`
5. Tunggu commit selesai: muat ulang halaman Import sub-tab itu setiap 5 detik sampai Banner Hasil Commit tampil (batas tunggu 2 menit)
6. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored. 1 error remains." tampil
7. Verifikasi Staging Table menampilkan 1 baris berstatus `error` yaitu baris #2 pada tabel
8. Verifikasi kolom # baris itu bernilai 1
9. Verifikasi Error Summary Callout memuat pesan Callout baris tabel dengan badge "1 row"
10. Buka halaman master sesuai baris tabel
11. Verifikasi Pagination tabel menampilkan "Showing 1 - 10 of 1000 items"
12. Ketik Search baris #1 tabel, tekan Enter
13. Verifikasi Search menampilkan baris bernama persis baris #1 tabel
14. Ganti isi kotak search dengan baris #2 tabel, tekan Enter
15. Verifikasi Search tidak menampilkan baris bernama persis baris #2 tabel

### TC-GS-IMPORT-750: Perubahan Master Data Count Limit Brand diikuti commit

16. Reset Client Limit lewat skrip fixture: Master Data Count Limit Brand 1000 dengan 999 Brand tersimpan (sisa 1 slot), tanpa draft Brand; seed draft Brand 2 baris `pending` dari `brand-cap-2.csv` (`Nikon`, `Pentax`)
17. Buka Global Settings > Import, pilih Sub-Tab Brand
18. Ubah Master Data Count Limit Brand dari 1000 menjadi 1100 di Admin Console > Plans & Licensing Lifecycle Settings > System Limits lewat fixture Admin Console (atas nama administrator Admin Console)
19. Klik `[Import (2)]`
20. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
21. Verifikasi Dropzone tampil
22. Verifikasi Banner Hasil Commit "Success, record has been imported. Duplicate records were ignored." tampil
23. Buka halaman Master Reference > Brand
24. Verifikasi Pagination tabel Brand Client Limit menampilkan "Showing 1 - 10 of 1001 items"
25. Ketik Search `Pentax`, tekan Enter
26. Verifikasi Search `Pentax` menampilkan baris bernama persis `Pentax`
27. Pulihkan Master Data Count Limit Brand ke 1000 lewat fixture Admin Console

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data (e); objek uji adalah batas Master Data Count Limit pada commit, dengan seed 999 record per katalog sebagai volume dan fixture Admin Console sebagai pemicu perubahan limit pada TC-750.
- Alasan melewati sekitar 35 langkah (27 langkah nominal; ekspansi langkah 2 sampai 15 dikali empat iterasi memberi sekitar 83 langkah): empat iterasi homogen yang berdiri sendiri (satu Sub-Tab per iterasi dengan reset Client Limit di awal), semua satu kelas dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna. Langkah 2 sampai 15 diulang tanpa langkah bersyarat; parameter tiap iterasi ada di tabel Prerequisites dan `Verifikasi` tetap satu per klausa. TC-GS-IMPORT-750 diletakkan terakhir karena mengubah System Limits.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 (instruksi iterasi), reset dan seeding (langkah 2, 16), pembukaan halaman dan Sub-Tab, polling job (langkah 5, 20), dan pemulihan limit pada langkah 27 (hook `after` sebagai cadangan). Langkah 12 dan 14 memakai Search atomik (butir 9 bagian 8b); langkah 13 menjadi anchor positif (Search menampilkan baris) sebelum asersi absence pada langkah 15, dan Pagination langkah 11 membuktikan tabel termuat.
- Pembagian TC lintas spec: batas Master Data Count Limit untuk User Login dan Create Missing ada di spec 165; race slot terakhir ada di spec 151.
- Temuan untuk QA:
  - TC-GS-IMPORT-404 sampai 407 mengasersi Pagination "of 1000 items" yang bergantung pada total record tepat 1000 di Client Limit sesudah commit; asersi hanya lolos bila tidak ada record lain yang dibuat spec lain pada Client Limit.
  - TC-GS-IMPORT-404 sampai 407 dan TC-GS-IMPORT-750 memakai nama literal (`Nikon`, `Pentax`, `Meter`, `Store Supervisor`, `Finance & Accounting`) tanpa suffix per run karena asersi Search mencocokkan nama persis; spec menjaga isolasi lewat reset seed dan cleanup di `after`.
  - TC-GS-IMPORT-750 mengubah System Limits lewat Admin Console tetapi akun Total Control Client Limit tidak memiliki akses Admin Console; akun administrator Admin Console tidak disebut di Pre-setup (ditulis disediakan tim FE).
  - TC-GS-IMPORT-750 Post Condition a menyebut seed dikembalikan ke 999; pemulihan seed dikerjakan hook `after` dan tidak diasersi (S-01).
  - Post Condition TC-GS-IMPORT-404 sampai 407 (draft berisi 1 baris `error`, 1 record baru tersimpan) dikonfirmasi oleh Expected tiap TC dan tidak diasersi tambahan.
