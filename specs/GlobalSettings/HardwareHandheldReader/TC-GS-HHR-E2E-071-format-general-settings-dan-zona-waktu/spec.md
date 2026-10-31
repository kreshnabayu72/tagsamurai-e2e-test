---
id: TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu
title: "Format Tanggal, Jam, dan Zona Waktu General Settings Tercermin pada Semua Surface Tanggal Handheld Reader"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-392
  - TC-GS-HHR-393
  - TC-GS-HHR-394
  - TC-GS-HHR-395
  - TC-GS-HHR-396
coverage:
  web: automated
---

# Format Tanggal, Jam, dan Zona Waktu General Settings Tercermin pada Semua Surface Tanggal Handheld Reader

## Prerequisites

- Mode: FE+BE. Kelas harness: state global (format tanggal, format jam, dan zona waktu General Settings Client A). Suite `parallel: false`; spec ini mengubah state global dan memulihkannya (lihat Pemulihan).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun aktor: Total Control Sari Dewi (Client A) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE, format awal `dd/MM/yy` 24-hour, zona waktu Asia/Jakarta (UTC+07:00)): DD-01 (`Last Scanned` 21/06/26 10:15, `Activated At` 21/06/26 08:00); Seed Changelog Client A (entri teratas 23/06/26 08:50); Seed Event Log Client A (entri teratas EL-01 21/06/26 08:00); Seed Usage Event DD-01 (UE-01 21/06/26 10:15 teratas).
- Kemampuan teknis (disediakan tim FE/BE): mengubah General Settings Client A (format tanggal `MM/dd/yyyy`, format jam 12-hour, dan zona waktu Asia/Jayapura (UTC+09:00)) lewat sesi API aktor hingga tersimpan; endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini. Jam server dan jam browser disinkron (S-12); asersi tanggal membandingkan dengan nilai Seed.
- Pemulihan: langkah pemulihan eksplisit di akhir spec mengembalikan format `dd/MM/yy` 24-hour dan zona waktu Asia/Jakarta; kolom `Activated At` disembunyikan kembali; hook `after` memulihkan General Settings Client A sebagai cadangan.
- State global yang diubah: General Settings Client A (format tanggal, format jam, zona waktu) dan visibilitas kolom `Activated At`.

## Test Steps

### Format MM/dd/yyyy 12-hour: TC-GS-HHR-392, TC-GS-HHR-393, TC-GS-HHR-394, TC-GS-HHR-395

1. Ubah General Settings Client A: format tanggal `MM/dd/yyyy`, format jam 12-hour lewat sesi API hingga tersimpan
2. Tunggu aksi selesai
3. Muat ulang halaman Handheld Reader
4. Aktifkan kolom `Activated At` lewat panel Column Visibility
5. Amati kolom `Last Scanned` dan `Activated At` baris DD-01
6. Verifikasi `Last Scanned` DD-01 menampilkan bulan `06`, hari `21`, tahun `2026`, jam `10:15 AM` dalam urutan `MM/dd/yyyy`
7. Verifikasi `Activated At` DD-01 menampilkan bulan `06`, hari `21`, tahun `2026`, jam `08:00 AM` dalam urutan `MM/dd/yyyy`
8. Klik ikon Filter, pilih rentang tanggal pada `Last Scanned`
9. Verifikasi teks field date picker `Last Scanned` memakai format `MM/dd/yyyy`
10. Tutup Filter Panel tanpa menerapkan filter
11. Klik ikon Changelog
12. Verifikasi entri teratas kolom `Date` menampilkan bulan `06`, hari `23`, tahun `2026`, jam `08:50 AM` dalam urutan `MM/dd/yyyy`
13. Klik ikon Filter pada Modal Changelog, pilih rentang tanggal pada `Date`
14. Verifikasi teks field date picker `Date` Modal Changelog memakai format `MM/dd/yyyy`
15. Tutup Modal Changelog
16. Klik `Device Name` baris DD-01 untuk membuka Popup Detail
17. Amati info grid `Last Scanned` dan `Activated At`
18. Verifikasi `Last Scanned` DD-01 di info grid menampilkan bulan `06`, hari `21`, tahun `2026`, jam `10:15 AM` dalam urutan `MM/dd/yyyy`
19. Amati kolom `Date` Tab Usage
20. Verifikasi baris Tab Usage teratas `Date` menampilkan bulan `06`, hari `21`, tahun `2026`, jam `10:15 AM`
21. Tutup Popup Detail
22. Klik ikon Event Log, klik ikon Filter, pilih rentang tanggal pada `Date`
23. Verifikasi teks field date picker `Date` Event Log memakai format `MM/dd/yyyy`
24. Verifikasi kolom `Date` Event Log baris teratas menampilkan bulan `06`, hari `21`, tahun `2026`
25. Tutup Popup Event Log

### Zona waktu: TC-GS-HHR-396

26. Pulihkan General Settings Client A ke format tanggal `dd/MM/yy` dan format jam 24-hour, lalu ubah zona waktu Client A menjadi Asia/Jayapura (UTC+09:00) lewat sesi API hingga tersimpan
27. Tunggu aksi selesai
28. Muat ulang halaman Handheld Reader
29. Amati `Last Scanned` baris DD-01
30. Verifikasi `Last Scanned` DD-01 menjadi `21/06/26 12:15` (bergeser +2 jam dari `21/06/26 10:15`)

### Pemulihan

31. Pulihkan zona waktu Client A menjadi Asia/Jakarta (UTC+07:00) lewat sesi API hingga tersimpan
32. Sembunyikan kembali kolom `Activated At` lewat panel Column Visibility

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 7d). Semua TC berlabel Automatable.
- Urutan: seluruh TC format (392 sampai 395) memakai General Settings yang sama dan dijalankan berurutan dalam satu pengubahan state; TC-GS-HHR-396 terakhir karena memakai format default dan zona waktu berbeda (prinsip 3 butir 4).
- Langkah penghubung tanpa `Verifikasi` (S-03): mengubah General Settings lewat sesi API, muat ulang, mengaktifkan dan menyembunyikan kolom, membuka dan menutup Filter Panel, Modal Changelog, Popup Detail, dan Popup Event Log, memulihkan General Settings. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah ke muat ulang halaman setelah aksi API. Filter Panel (langkah 8 dan 22) tidak diterapkan.
- Pembukaan tiap surface adalah langkah observasi singkat (buka, amati format, tutup) sehingga kegagalan satu surface tidak membuat surface lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-HHR-392 langkah 2 ("Aktifkan kolom `Activated At`") tidak menyebut mekanismenya; spec memakai panel Column Visibility.
  - TC-GS-HHR-392 sampai TC-GS-HHR-396 menyatakan perubahan General Settings sebagai precondition oleh Total Control tanpa langkah UI; spec mengubahnya lewat sesi API yang disediakan tim FE tanpa mengarang endpoint.
  - TC-GS-HHR-394 langkah 2 mengamati `Activated At` pada info grid, tetapi Expected hanya menyebut `Last Scanned` dan `Date` Tab Usage; spec tidak mengasersi `Activated At` di Popup Detail.
  - TC-GS-HHR-393 dan TC-GS-HHR-395 tidak menyebut rentang tanggal yang dipilih pada date picker; spec memilih rentang apa pun yang memunculkan teks field.
  - TC-GS-HHR-396 menyatakan zona waktu tujuan Asia/Jayapura (UTC+09:00) dan tidak menyebut format jam yang berlaku; spec mengikuti format default `dd/MM/yy` 24-hour.
