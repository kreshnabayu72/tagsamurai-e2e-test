---
id: TC-GS-HHR-E2E-028-resilience-download-daftar-usage-dan-changelog
title: "Resilience Download: Kegagalan Unduh Daftar Reader, Tab Usage, Modal Changelog, dan Popup Event Log Activate"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-184
  - TC-GS-HHR-315
  - TC-GS-HHR-339
coverage:
  web: automated
---

# Resilience Download: Kegagalan Unduh Daftar Reader, Tab Usage, Modal Changelog, dan Popup Event Log Activate

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata). Respons yang dipaksa lewat `Spectra.intercept()` pada request unduh (endpoint ekspor tidak disebut di TC, PRD, atau LLD yang dirujuk spec ini, sehingga tidak dituliskan): respons 500 pada request unduh Daftar Reader (langkah 1), request unduh Tab Usage (langkah 8), request unduh Modal Changelog dan request unduh Popup Event Log Activate (langkah 20). Setiap intercept dilepas segera setelah pemicunya selesai (S-09).
- Suite serial (`parallel: false`). Spec ini tidak mengubah state global dan tidak membuat data. Hook `after` melepas intercept yang tersisa dan menutup popup atau modal yang masih terbuka.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-handheld-reader` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.
- Akun aktor (login di hook `before`, bukan di langkah): Total Control Sari Dewi, Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (Client A): Seed Reader A (DD-01 sampai DD-10), plan Growth, General Settings `dd/MM/yy` 24-hour Asia/Jakarta. DD-01 (Serial Number `SN-HHR-00101`) dipakai sebagai reader yang Popup Detail-nya dibuka; Device Name DD-01 sama dengan DD-06 (`Zebra RFID Reader - 1`), sehingga DD-01 ditemukan lewat Serial Number. Fixture baru `Fixture.hardwareHandheldReader.resilienceDownload028`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500; membaca toast beserta ketahanannya (toast error tidak hilang otomatis; `foundation/functions/toast-copy.md`) dan men-dismiss toast; mengamati bahwa tidak ada berkas yang terunduh (pembaca daftar unduhan browser).

## Test Steps

### TC-GS-HHR-315: Download Daftar Reader gagal menampilkan toast error

1. Pasang intercept pada request unduh: respons 500
2. Klik ikon Download
3. Pilih `Download as CSV`
4. Verifikasi toast error "Error, failed to download Handheld-Reader-List." tampil
5. Verifikasi tidak ada berkas yang terunduh
6. Dismiss toast error
7. Lepas intercept pada request unduh

### TC-GS-HHR-184: Download Tab Usage gagal menampilkan toast error

8. Pasang intercept pada request unduh: respons 500
9. Ketik Search `SN-HHR-00101`, tekan Enter
10. Klik `Device Name` baris DD-01
11. Pastikan Tab `Usage` aktif
12. Klik ikon Download
13. Pilih `Download as CSV`
14. Verifikasi toast error "Error, failed to download Handheld-Reader-Usage." tampil
15. Verifikasi tidak ada berkas yang terunduh
16. Dismiss toast error
17. Lepas intercept pada request unduh
18. Tutup Popup Detail lewat `✕`
19. Klik `(←)` pada kotak Search

### TC-GS-HHR-339: Download Modal Changelog dan Popup Event Log Activate gagal menampilkan toast error

20. Pasang intercept pada request unduh: respons 500
21. Klik ikon Changelog
22. Klik ikon Download pada Modal Changelog
23. Pilih `Download as CSV`
24. Verifikasi toast error "Error, failed to download Changelog-Handheld-Reader." tampil
25. Dismiss toast error
26. Tutup Modal Changelog lewat `✕`
27. Klik ikon Event Log
28. Klik ikon Download pada Popup Event Log Activate
29. Pilih `Download as CSV`
30. Verifikasi toast error "Error, failed to download Handheld-Reader-Activate-Log." tampil
31. Dismiss toast error
32. Lepas intercept pada request unduh
33. Tutup Popup Event Log lewat `✕`

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec singkat (33 langkah), di bawah ambang sekitar 35 langkah. Seluruhnya satu kelas harness (kelas b: fault injection 5xx pada unduhan), satu akun aktor, dan tanpa data baru. Tidak ada aksi yang menghabisi atau mengubah data.
- Spec 026, 027, dan 028 menguji kelas b (fault injection 5xx) pada permukaan berbeda dan sengaja dipisah: gabungannya 244 langkah (122, 89, dan 33), jauh di atas sekitar 35 langkah. Spec 026 membutuhkan simulator USB dan membuat reader, spec 027 memicu 5xx pada aksi tulis, dan spec ini hanya memicu 5xx pada unduhan tanpa mengubah data, sehingga kegagalan keras satu spec tidak menghilangkan makna spec lain.
- Pengecualian S-12 Population Seed Reader A HHR (A-5) berlaku untuk Seed Reader A (nama dan Serial Number literal tanpa suffix `{runId}`); spec ini tidak mengubah reader, dan pemulihan Seed Reader A dijamin fixture backend serta dinyatakan di `suite.md`.
- Urutan: Daftar Reader (TC-GS-HHR-315), Popup Detail Tab Usage (TC-GS-HHR-184), lalu Modal Changelog dan Popup Event Log Activate (TC-GS-HHR-339). Urutan menyimpang dari nomor TC (184 sebelum 315) supaya surface dari layar utama ke popup dan modal berurutan dan Popup Detail tidak perlu dibuka sebelum daftar.
- Langkah penghubung (aksi tanpa `Verifikasi`): pemasangan dan pelepasan intercept; dismiss toast error agar toast error berikutnya tidak lulus karena toast lama (S-09); Search untuk menemukan baris DD-01 dan `(←)` untuk mengosongkan Search; menutup Popup Detail, Modal Changelog, dan Popup Event Log lewat `✕`.
- Pembagian TC lintas spec: TC-GS-HHR-306 sampai 314 dan 316 (unduh sukses CSV/XLSX, isi berkas, dan volume besar) ada di spec 057, 058, dan 059; pengunduhan Tab Usage sukses (TC-GS-HHR-183) ada di spec 058.
- Temuan untuk QA:
  - TC-GS-HHR-184 dan 315 meminta "tidak ada file terunduh", sedangkan TC-GS-HHR-339 tidak menyebut berkas; spec tidak mengasersi berkas pada TC-GS-HHR-339 karena Expected TC hanya meminta toast. Kemampuan mengamati unduhan disediakan tim FE.
  - TC-GS-HHR-339 langkah 2 menulis "Buka Modal Changelog, Download as CSV" tanpa menyebut ikon Download dan pilihan format secara terpisah; spec memakai pola ikon Download lalu `Download as CSV` sesuai TC-GS-HHR-184 dan 315.
  - TC-GS-HHR-339 langkah 3 menutup Modal Changelog tanpa menyebut cara; spec memakai `✕`.
  - Request unduh tidak diidentifikasi (nama endpoint, pembeda antar surface) di TC; spec memasang satu intercept untuk request unduh per blok dan tidak mengarang endpoint.
