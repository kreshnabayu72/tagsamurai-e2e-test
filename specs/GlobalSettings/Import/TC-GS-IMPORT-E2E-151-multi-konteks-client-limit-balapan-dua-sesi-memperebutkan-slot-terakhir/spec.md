---
id: TC-GS-IMPORT-E2E-151-multi-konteks-client-limit-balapan-dua-sesi-memperebutkan-slot-terakhir
title: "Multi-konteks Client Limit: balapan dua sesi memperebutkan slot terakhir Master Data Count Limit (Division)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-410
  - TC-GS-IMPORT-720
coverage:
  web: automated
---

# Multi-konteks Client Limit: balapan dua sesi memperebutkan slot terakhir Master Data Count Limit (Division)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai kuota Master Data Count Limit Client Limit (seed 999 Division) yang dibagikan dengan spec batas kuota lain, dan draft Client Limit dibagikan ke seluruh admin; lihat `suite.md`.
- Dua konteks browser dalam satu spec, ditandai `[Sesi A]` dan `[Sesi B]` (keduanya mengasersi hasil di UI):
  - Sesi A (aktor utama): Total Control Client Limit (Bima Saputra) `totalControl_automated_qaTeam7@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTLIMIT_TC_PASSWORD`. Login di hook `before`; layar awal Global Settings > Import dibuka hook `beforeEach`.
  - Sesi B: Admin kedua Client Limit (Rasti Anggraeni) `totalControlSecond_automated_qaTeam7@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTLIMIT_TC2_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Password tidak ditulis di spec atau fixture.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE; tidak didefinisikan di TC, PRD, atau LLD selain nama kemampuannya):
  - Dua konteks browser paralel dan barrier: `Spectra.intercept` menahan dua permintaan (commit Tab Division dan Create Missing Divisions) lalu melepasnya pada saat yang sama (TC-410); aksi klik `[Create Missing Divisions]` oleh dua sesi pada waktu yang sama (TC-720). Pemenang slot tidak ditentukan.
  - Skrip seed R7/D-46: Master Data Count Limit Division Client Limit = 1000 (nilai minimum) dengan 999 Division tersimpan (nama `Seed Division nnnn`), sisa 1 slot; pemulihan sesudah TC.
  - Hook umur draft D-76 varian 1 (>=24 jam) untuk TC-410; skrip reset Client Limit (draft Tab Division dan User Login).
  - Jeda nyata: polling "muat ulang setiap 5 detik" menunggu job commit latar belakang selesai (bukan menunggu jam).
- Data Dinamis (milik spec ini; draft dibuang oleh reset sehingga nama baris berkas literal sesuai Data Uji TC):
  - TC-410: draft Tab Division 1 baris `pending` `Legal` Code `LGL` (`division-race-1.csv`, kolom Division Name dan Code) dan draft Tab User Login 1 baris `error` (`user-login-race-1.csv`: Putu Aditya, `putu.aditya@example.com`, Division `Logistik`, Access `Global Settings`).
  - TC-720: `user-login-division-cap.csv` (D-45): 2 baris Siti Rahmawati (Division `Pengadaan`) dan Budi Santoso (Division `Logistik`), Position kosong.
- Pemulihan (hook `after`, tetap jalan walau spec gagal): hapus Division hasil race (`Legal`, `Logistik`, `Pengadaan`) dan seed 999 Division sesuai D-46, hapus draft Client Limit, tutup konteks Sesi B, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-410: Commit Tab Division dan Create Missing Divisions bersamaan di slot terakhir

1. Reset Client Limit lewat skrip fixture: 999 Division tersimpan dan Master Data Count Limit Division 1000 (D-46); seed draft Tab Division 1 baris `Legal`/`LGL` dan draft Tab User Login 1 baris `error` (Division `Logistik`) dengan hook umur draft D-76 varian 1
2. [Sesi A] Muat ulang halaman Import > Division
3. [Sesi B] Buka Global Settings > Import, pilih Sub-Tab User Login
4. Pasang intercept yang menahan permintaan commit Tab Division dan permintaan Create Missing Divisions sampai dilepas
5. [Sesi A] Klik `[Import (1)]` di Tab Division
6. [Sesi B] Klik `[Create Missing Divisions]` pada baris pesan "Division not found" di Error Summary Callout
7. Lepaskan kedua permintaan yang ditahan intercept pada saat yang sama
8. [Sesi A] Tunggu commit selesai: muat ulang halaman Import > Division setiap 5 detik sampai `[Discard]` Enabled atau Dropzone tampil (batas tunggu 2 menit)
9. [Sesi A] Buka halaman Global Settings > User > Division
10. [Sesi A] Verifikasi Pagination tabel Division Client Limit menampilkan "Showing 1 - 10 of 1000 items"
11. [Sesi A] Ketik Search `Legal`, tekan Enter
12. [Sesi A] Catat jumlah baris hasil pencarian `Legal` yang bernama persis `Legal`
13. [Sesi A] Ganti isi kotak search dengan `Logistik`, tekan Enter
14. [Sesi A] Catat jumlah baris hasil pencarian `Logistik` yang bernama persis `Logistik`
15. [Sesi A] Verifikasi tepat satu dari Search `Legal` dan Search `Logistik` menampilkan baris bernama persis kata kunci itu (jumlah baris langkah 12 ditambah jumlah baris langkah 14 tepat 1)

### TC-GS-IMPORT-720: Dua Create Missing Divisions bersamaan di slot terakhir

16. Reset Client Limit lewat skrip fixture: tanpa draft Tab User Login, 999 Division tersimpan dan Master Data Count Limit Division 1000 (D-46); hapus Division `Legal`, `Logistik`, dan `Pengadaan` hasil TC-410 bila ada
17. [Sesi A] Buka Global Settings > Import, pilih Sub-Tab User Login
18. [Sesi A] Klik `[Upload File]` di Dropzone dan pilih berkas `user-login-division-cap.csv`
19. [Sesi A] Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
20. [Sesi A] Klik `⋯` pada baris #1 (`Pengadaan`)
21. [Sesi B] Buka Global Settings > Import, pilih Sub-Tab User Login
22. [Sesi B] Klik `⋯` pada baris #2 (`Logistik`)
23. [Sesi A] dan [Sesi B] Pilih `[Create Missing Divisions]` pada waktu yang sama
24. Verifikasi tepat satu dari kedua sesi menerima toast sukses "Success, division has been created."
25. Verifikasi sesi lainnya menerima toast error "Error, failed to create division."
26. Pada sesi yang menerima toast error, verifikasi baris miliknya berstatus `error`
27. Pada sesi yang menerima toast error, verifikasi Error Summary Callout memuat pesan "You've reached the platform limit of 1000 divisions. Contact support if you need a higher limit." dengan badge "1 row"
28. [Sesi A] Buka Global Settings > User > Division
29. [Sesi A] Ketik Search `Pengadaan`, tekan Enter
30. [Sesi A] Catat jumlah baris hasil pencarian `Pengadaan`
31. [Sesi A] Ganti isi kotak search dengan `Logistik`, tekan Enter
32. [Sesi A] Catat jumlah baris hasil pencarian `Logistik`
33. [Sesi A] Verifikasi jumlah baris langkah 30 ditambah jumlah baris langkah 32 tepat 1
34. [Sesi A] Buka halaman Import > User Login
35. [Sesi A] Verifikasi baris untuk nama yang tidak terbentuk berstatus `error`
36. [Sesi A] Verifikasi baris untuk nama yang terbentuk berstatus `pending`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (c) dengan race dua sesi sebagai objek uji. Kuota Master Data Count Limit adalah pemicu state (P-2: kuota boleh menjadi pemicu pada spec multi-konteks), spec tidak dipindah ke kelas volume. TC-GS-IMPORT-410 dan TC-GS-IMPORT-720 berstatus Manual di sumber; keduanya tetap spec dan kebutuhan teknisnya tercatat di Prerequisites.
- Spec berisi 36 langkah, hanya sedikit di atas 35 langkah. Alasan: satu skenario balapan dua sesi (kelas multi-konteks) yang tidak dapat dipecah tanpa kehilangan makna race; reset dan seeding hanya di langkah 1 dan 16. Langkah 16 juga menghapus Division `Legal`, `Logistik`, dan `Pengadaan` yang mungkin tersisa dari TC-410 (S-03), supaya baris #2 TC-720 tetap "Division not found" dan slot 1000 belum terpakai.
- Langkah penghubung (tanpa `Verifikasi`): reset dan seeding (langkah 1, 16), pembukaan halaman dan Sub-Tab, pencatatan jumlah baris (langkah 12, 14, 30, 32), polling job (langkah 8), dan ganti isi kotak search (langkah 13, 31). Langkah 34 membuka halaman Import > User Login pada Sesi A tanpa muat ulang paksa karena halaman dibuka dari halaman Division.
- Langkah 24 dan 25 tidak menentukan sesi mana yang menang karena Expected TC-GS-IMPORT-720 menyatakan "akun yang memperoleh slot tidak ditentukan"; langkah 26, 27, 35, dan 36 merujuk "sesi yang menerima toast error" dan "nama yang tidak terbentuk" yang ditentukan saat run.
- Langkah 15 dan 33 mengasersi penjumlahan dua pencarian sebagai pembanding: pencarian yang mengembalikan baris menjadi anchor positif bagi pencarian yang kosong.
- Temuan untuk QA:
  - TC-GS-IMPORT-410 dan TC-GS-IMPORT-720 tidak deterministik pada pemenang slot dan bertanda Manual (race); TC-GS-IMPORT-410 memakai flag clock, intercept, dua sesi, dan limit untuk satu asersi, sedangkan peran jam dan intercept tidak dijelaskan. Spec memakai barrier intercept (TC-410) dan klik bersamaan (TC-720).
  - TC-GS-IMPORT-410 Expected b mengasersi "baris bernama persis kata kunci" pada tabel Division tanpa menyebut cara memastikan nama persis (Search mencocokkan substring); spec menghitung baris yang bernama persis kata kunci.
  - TC-GS-IMPORT-410 Expected a (Pagination "of 1000 items") bergantung pada total Division tepat 1000 di Client Limit sesudah race; asersi ini hanya lolos bila tidak ada Division lain yang dibuat spec lain pada Client Limit.
  - Post Condition TC-GS-IMPORT-410 dan TC-GS-IMPORT-720 ("Total Division Client Limit = 1000", "Jumlah Division tepat 1000") dikonfirmasi oleh Expected TC-GS-IMPORT-410 a; pada TC-GS-IMPORT-720 dikonfirmasi oleh Expected c.
  - TC-GS-IMPORT-410 langkah 4 menyebut intercept menahan permintaan commit Tab Division dan Create Missing tanpa menyebut nama endpoint; diambil dari kontrak API modul oleh tim FE.
