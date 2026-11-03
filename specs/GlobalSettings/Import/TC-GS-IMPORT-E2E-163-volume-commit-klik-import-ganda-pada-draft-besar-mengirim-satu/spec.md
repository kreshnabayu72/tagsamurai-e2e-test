---
id: TC-GS-IMPORT-E2E-163-volume-commit-klik-import-ganda-pada-draft-besar-mengirim-satu
title: "Volume commit: klik Import ganda pada draft besar mengirim satu permintaan, dan baris diproses berurutan Row # lintas batch"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-364
  - TC-GS-IMPORT-368
coverage:
  web: automated
---

# Volume commit: klik Import ganda pada draft besar mengirim satu permintaan, dan baris diproses berurutan Row # lintas batch

## Prerequisites

- Mode: FE+BE (backend nyata) dengan pemantau jaringan browser (`Spectra.intercept` hanya mencatat permintaan, tanpa mengubah respons).
- Suite serial (`parallel: false`): spec melakukan commit nyata di Client E (250 dan 111 record Brand) yang dipakai bersama spec commit lain; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE):
  - Pemantau jaringan browser yang mencatat jumlah permintaan Import (TC-364) dan klik dua kali beruntun kurang dari 100 milidetik.
  - Kueri fixture daftar nama Brand Client E terurut menurut waktu pembuatan menaik (TC-368).
  - Skrip fixture reset Client E (D-47: hapus draft, hapus Brand hasil commit, reset hasil commit terakhir) dan seeding draft D-56 (250 baris) dan D-70 (111 baris, lintas Append dan Duplicate).
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job latar belakang selesai (bukan menunggu jam).
- Data Dinamis (milik spec ini; hasil commit dihapus oleh reset):
  - D-56 `brand-250-impor.csv`: `Brand Impor 001` sampai `Brand Impor 250`, semua valid dan unik (TC-364).
  - D-70 `brand-urut-111.csv` (TC-368): berkas asli `brand-urut-105.csv` (`Brand Urut 001` sampai `Brand Urut 105`), 5 baris hasil Append (`Brand Urut 106` sampai `Brand Urut 110`), dan 1 baris hasil Duplicate dari baris `Brand Urut 003` (Row #3) dengan Brand Name `Brand Urut Salinan` tepat di bawah baris sumber (Row #4); total 111 baris, batch commit 100 baris dan 11 baris. Draft disiapkan lewat skrip fixture.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus draft Client E, hapus Brand hasil commit (`Brand Impor nnn`, `Brand Urut nnn`, `Brand Urut Salinan`), reset hasil commit terakhir, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-364: Klik Import ganda lewat UI hanya mengirim satu permintaan

1. Reset Client E (D-47) dan seed draft Brand D-56 (250 baris `pending`) lewat skrip fixture
2. Muat ulang halaman Import > Brand
3. Pasang pemantau jaringan pada permintaan Import
4. Klik `[Import (250)]` dua kali beruntun dalam waktu kurang dari 100 milidetik
5. Verifikasi pemantau mencatat tepat satu permintaan Import
6. Verifikasi `[Import (250)]` Disabled
7. Verifikasi tidak ada dialog yang tampil
8. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
9. Buka halaman Master Reference > Brand
10. Ketik Search `Brand Impor`, tekan Enter
11. Verifikasi Pagination tabel Brand Client E menampilkan "Showing 1 - 10 of 250 items"

### TC-GS-IMPORT-368: Baris pending diproses berurutan Row # ascending lintas batch

12. Reset Client E (D-47) dan seed draft Brand D-70 (111 baris `pending`) lewat skrip fixture
13. Buka Global Settings > Import, pilih Sub-Tab Brand
14. Atur Rows per page 100
15. Catat urutan Brand Name menurut `Row #` pada halaman 1
16. Buka halaman 2
17. Catat urutan Brand Name menurut `Row #` pada halaman 2
18. Klik `[Import (111)]`
19. Tunggu aksi selesai (permintaan mendapat respons)
20. Tunggu commit selesai: muat ulang halaman Import > Brand setiap 5 detik sampai Dropzone tampil (batas tunggu 2 menit)
21. Baca urutan pembuatan 111 record Brand hasil commit melalui kueri fixture (daftar nama Brand terurut menurut waktu pembuatan menaik)
22. Verifikasi urutan pembuatan 111 record identik dengan urutan `Row #` yang dicatat pada langkah 15 dan langkah 17
23. Verifikasi record `Brand Urut 106` sampai `Brand Urut 110` (hasil Append) dibuat setelah `Brand Urut 105`
24. Verifikasi record `Brand Urut Salinan` dibuat pada urutan yang sama dengan posisi `Row #` barisnya yang dicatat pada langkah 15 (Row #4)
25. Verifikasi batas batch pertama 100 baris dan kedua 11 baris tidak mengubah urutan pembuatan

## Notes

- Mode: FE+BE dengan pemantau jaringan. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: volume data (e), seed dua draft besar (250 dan 111 baris) lewat skrip fixture; volume menjadi bagian objek uji karena batas batch 100 baris diuji pada urutan pemrosesan.
- Spec 25 langkah sehingga tidak melewati sekitar 35 langkah.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan blok: TC-364 lebih dulu, TC-368 kemudian; masing-masing mereset Client E sendiri.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 12), pemasangan pemantau (langkah 3), muat ulang halaman Import > Brand (langkah 2), pembukaan halaman dan Sub-Tab (langkah 13), pengaturan Rows per page (langkah 14), pencatatan urutan (langkah 15, 17), "Tunggu aksi selesai (permintaan mendapat respons)" persis sesudah klik `[Import (111)]` dan sebelum polling (langkah 19; bagian 8b butir 8), polling job (langkah 8, 20), dan pembacaan kueri fixture (langkah 21).
- Langkah 5 sampai 7 diasersi segera setelah klik ganda dan sebelum commit selesai (butir 5 dan 11 bagian 8b); langkah 7 (tidak ada dialog) didahului langkah 6 (tombol Disabled) sebagai anchor positif yang terhubung ke pemicu.
- Temuan untuk QA:
  - Penanda selesai untuk klik `[Import (111)]` (langkah 19) tidak disebut di TC atau PRD; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati.
  - TC-GS-IMPORT-364 menyebut klik dua kali beruntun dalam waktu kurang dari 100 milidetik tanpa menyebut cara mengaturnya pada automation; spec mengandalkan kemampuan klik berurutan cepat oleh tim FE.
  - TC-GS-IMPORT-368 Expected c menyebut posisi `Brand Urut Salinan` sebagai "Row #4" mengacu pada catatan Langkah 2; spec memakai catatan langkah 15.
  - Post Condition TC-GS-IMPORT-364 dan TC-GS-IMPORT-368 (draft dihapus, N record Brand tersimpan) tidak punya langkah observasi tersendiri selain Expected dan tidak diasersi tambahan (S-01); Post Condition b TC-GS-IMPORT-364 dikonfirmasi oleh Expected b.
