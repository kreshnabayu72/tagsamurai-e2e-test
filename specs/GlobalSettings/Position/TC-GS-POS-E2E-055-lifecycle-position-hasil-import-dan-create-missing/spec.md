---
id: TC-GS-POS-E2E-055-lifecycle-position-hasil-import-dan-create-missing
title: "Position Hasil Import: Edit, Delete In-Use Diblokir, Delete Bebas Relasi, dan Create Missing Positions Duplikat Ditolak"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-275
  - TC-GS-POS-276
  - TC-GS-POS-277
  - TC-GS-POS-295
coverage:
  web: automated
---

# Position Hasil Import: Edit, Delete In-Use Diblokir, Delete Bebas Relasi, dan Create Missing Positions Duplikat Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun Sesi A (aktor utama): Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; berada di Global Settings > User > Position.
- Akun Sesi B (Admin B, hanya memicu state pada TC-GS-POS-295): Admin B Total Control (Andi Wijaya) `superAdminGlobalSettingsB_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Konteks browser terpisah, login di hook `before`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Position `Sales Coordinator` (Pre-setup 16), dibuat via Import Type "Position" dan dipakai user `Hendra Gunawan` (Pre-setup 17, Login aktif). Pengecualian S-06 untuk Position Pre-setup in-use yang dirancang TC untuk blokir: hanya dibaca dan Delete selalu diblokir guard, sehingga tidak diubah dan Last Updated tidak berubah; tidak bersuffix.
- Data Dinamis (bersuffix per run):
  - `Import Probe Analyst {runId}-055` (Data Dinamis No. 35): Position milik spec dengan asal Import Type "Position", bebas relasi; seeding di hook `before` memakai jalur Import Type "Position" (kemampuan teknis disediakan tim FE/BE). Diganti nama menjadi `Import Probe Specialist {runId}-055` pada TC-GS-POS-275, lalu dihapus pada TC-GS-POS-277. Search dan asersi memakai nama lengkap bersuffix `{runId}-055`, bukan substring pendek, supaya Position spec lain tidak muncul di hasil.
  - `Lab Analyst {runId}-055`: Position yang dibuat Sesi B pada TC-GS-POS-295. Staging Import Type "User Login" (seeding di hook `before`, khusus spec ini dan hanya memuat Position belum terdaftar `Lab Analyst {runId}-055`) disiapkan sebelum Sesi B membuatnya.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` untuk akun aktor spec ini (Sesi A dan Sesi B) dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API `Import Probe Analyst {runId}-055`, `Import Probe Specialist {runId}-055`, dan `Lab Analyst {runId}-055` bila masih ada; bersihkan staging Import yang dibuat spec; tutup konteks Sesi B; kembalikan sesi ke akun default suite.
- Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Position; layar awal dibuka di hook ini sehingga `## Test Steps` tidak mengulang langkah buka pada TC-GS-POS-275 sampai 277.
- Kemampuan teknis: seeding Position dengan asal Import dan seeding staging Import Type "User Login" (disediakan tim FE/BE; mekanisme tidak didefinisikan di TC, PRD, atau LLD); dua konteks browser; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]` pada TC-GS-POS-295.
- State global: tidak ada yang diubah selain data milik spec.

## Test Steps

### TC-GS-POS-275: Position hasil Import Type "Position" bisa di-Edit identik record manual

1. Ketik `Import Probe Analyst {runId}-055` pada Search tabel lalu tekan Enter
2. Klik `⋯` pada baris `Import Probe Analyst {runId}-055`, pilih `Edit`
3. Ganti isi field Position Name menjadi `Import Probe Specialist {runId}-055`
4. Klik `[Save]`
5. Verifikasi toast sukses: "Success, position has been updated."
6. Klik ikon Changelog
7. Ketik `Import Probe Specialist {runId}-055` pada Search Popup Changelog lalu tekan Enter
8. Verifikasi Changelog mencatat entri Edit dengan Old Value `Import Probe Analyst {runId}-055` dan New Value `Import Probe Specialist {runId}-055`
9. Tutup Popup Changelog dengan klik `✕` di header

### TC-GS-POS-276: Position hasil Import yang dipakai user tetap diblokir saat Delete

10. Ganti isi kotak search tabel dengan `Sales Coordinator`, tekan Enter
11. Klik `⋯` pada baris `Sales Coordinator`, pilih `Delete`
12. Verifikasi dialog "Cannot Delete Data" tampil dengan `• Sales Coordinator`
13. Verifikasi dialog menampilkan tombol `[OK]`
14. Klik `[OK]`

### TC-GS-POS-277: Position hasil Import yang bebas relasi bisa dihapus

15. Ganti isi kotak search tabel dengan `Import Probe Specialist {runId}-055`, tekan Enter
16. Klik `⋯` pada baris `Import Probe Specialist {runId}-055`, pilih `Delete`
17. Verifikasi Dialog Delete Position tampil dengan bullet `• Import Probe Specialist {runId}-055`
18. Klik `[Delete]` pada Dialog Delete Position
19. Verifikasi toast sukses: "Success, position has been deleted."

### TC-GS-POS-295: [Create Missing Positions] untuk nama yang sudah ada ditolak sebagai duplikat

20. [Sesi B] Klik `[+ Position]`
21. [Sesi B] Ketik `Lab Analyst {runId}-055` pada field Position Name
22. [Sesi B] Klik `[Submit]`
23. [Sesi B] Tunggu hingga Create selesai (toast sukses tampil)
24. [Sesi A] Ganti isi kotak search tabel dengan `Lab Analyst {runId}-055`, tekan Enter
25. [Sesi A] Catat Last Updated baris `Lab Analyst {runId}-055` sebagai baseline
26. [Sesi A] Buka Global Settings > Import
27. [Sesi A] Klik `[Create Missing Positions]`
28. [Sesi A] Verifikasi toast error: "Error, failed to create position."
29. [Sesi A] Buka Global Settings > User > Position
30. [Sesi A] Ketik `Lab Analyst {runId}-055` pada Search tabel lalu tekan Enter
31. [Sesi A] Verifikasi tabel Position menampilkan tepat 1 baris `Lab Analyst {runId}-055`
32. [Sesi A] Verifikasi Last Updated baris `Lab Analyst {runId}-055` tidak berubah dibanding baseline pada langkah 25
33. [Sesi A] Klik ikon Changelog
34. [Sesi A] Ketik `Lab Analyst {runId}-055` pada Search Popup Changelog lalu tekan Enter
35. [Sesi A] Verifikasi Changelog menampilkan tepat 1 entri Create `Lab Analyst {runId}-055`
36. [Sesi A] Verifikasi kolom Modified By entri Create tersebut bernilai "Andi W"
37. [Sesi A] Tutup Popup Changelog dengan klik `✕` di header

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Kelas harness: fungsional lintas modul (Position dan Import).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 37 langkah (di atas smell sekitar 35 langkah). Alasan: seluruh blok satu topik (siklus hidup Position hasil Import) dengan satu kelas harness; blok TC-GS-POS-275 dan TC-GS-POS-277 berurutan karena TC-277 menghapus hasil rename TC-275 (Dependensi TC, dipenuhi di satu spec), sedangkan blok TC-GS-POS-276 dan TC-GS-POS-295 berdiri sendiri dengan data sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected, dan pemisahan hanya menambah login, hook, dan cleanup tanpa menambah cakupan.
- P-2 (pemicu bukan objek uji): Sesi B pada TC-GS-POS-295 (langkah 20 sampai 23) hanya membentuk state "Position sudah ada sebelum `[Create Missing Positions]` diklik"; objek asersi adalah hasil di Sesi A. Tidak ada asersi tentang perilaku Sesi B.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 dan 37 (menutup Popup Changelog); langkah 14 (menutup dialog `Cannot Delete Data` dengan `[OK]`); langkah 23 (menunggu Create Sesi B selesai); langkah 1, 10, 15, 24, dan 30 (Search untuk menemukan baris; langkah 10, 15, dan 24 mengganti isi kotak search yang sudah berisi); langkah 7 dan 34 (Search di Popup Changelog untuk menemukan entri milik spec, karena Changelog kumulatif); langkah 25 (mencatat Last Updated baris `Lab Analyst {runId}-055` sebagai baseline TC-GS-POS-295 butir b); langkah 26 dan 29 (berpindah modul).
- Butir Expected TC-GS-POS-295: butir a di langkah 28, butir b di langkah 31 (tepat 1 baris) dan langkah 32 (Last Updated tidak berubah), butir c di langkah 35 (tepat 1 entri Create) dan langkah 36 (Modified By).
- Asersi tentang entri log Position hasil Import (TC-GS-POS-249) ada di spec 046, yang memakai Position hasil Import miliknya bersuffix `{runId}-046`.
- Temuan untuk QA:
  - TC-GS-POS-295 berstatus Manual Only di TC tetapi tetap ditulis (konvensi bagian 2).
  - TC-GS-POS-295 Precondition c dan d tidak menyebut cara menyiapkan staging Import Type "User Login" dan memastikan `Lab Analyst` belum terdaftar saat staging dibuat; spec menuliskannya sebagai kemampuan tim FE/BE tanpa mengarang endpoint.
  - TC-GS-POS-275 dan 277 memakai Position Data Dinamis No. 35 (`Import Probe Analyst`, lalu `Import Probe Specialist`); spec memakai `Import Probe Analyst {runId}-055` bersuffix milik spec, yang membutuhkan seeding Position berasal Import yang disediakan tim FE/BE. TC-GS-POS-276 memakai Pre-setup 16 `Sales Coordinator` yang hanya dibaca.
  - TC-GS-POS-277 Dependensi TC-GS-POS-275 dipenuhi dengan langkah 1 sampai 5; tidak ada Post Condition tanpa observasi pada spec ini.
  - Sesi Admin B pada TC-GS-POS-295 (langkah 20 sampai 23) memakai sesi UI mengikuti TC, padahal hanya memicu state; konvensi P-2 meminta pelaku kedua semacam itu memakai sesi API. Perlu konfirmasi QA sebelum langkah itu dipindah ke sesi API yang disediakan tim FE/BE.
