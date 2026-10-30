---
id: TC-GS-IMPORT-E2E-075-kunci-kedaluwarsa-save-pemegang-lama-diproses-normal-bila-belum-diambil
title: "Kunci Kedaluwarsa: Save Pemegang Lama Diproses Normal bila Belum Diambil, Ditolak 409 bila Sudah Diambil, dan Draft Tidak Ditemukan Setelah Discard Draft"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-253
  - TC-GS-IMPORT-254
  - TC-GS-IMPORT-257
coverage:
  web: automated
---

# Kunci Kedaluwarsa: Save Pemegang Lama Diproses Normal bila Belum Diambil, Ditolak 409 bila Sudah Diambil, dan Draft Tidak Ditemukan Setelah Discard Draft

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah jam server; lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > Brand Client A:
  - Sesi TC: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD` (TC-GS-IMPORT-254 dan 257; TC-GS-IMPORT-253 tidak memakai sesi kedua).
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua, memulihkan jam server, dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, #2 `Lenovo`). D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil pada TC-GS-IMPORT-257.
- Kemampuan teknis yang disediakan tim FE/BE (lingkungan non-produksi): fixture jam server dimajukan 11 menit (di atas TTL kunci 10 menit; hanya jam server karena TTL kunci dihitung murni di server dan tidak diamati lewat countdown UI). Jam dipulihkan lewat langkah eksplisit di akhir tiap blok.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft D-01 dan jam server dipulihkan antar TC.

## Test Steps

### TC-GS-IMPORT-253: Save pemegang lama setelah TTL habis diproses normal

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
4. Majukan jam server 11 menit tanpa admin lain mengambil kunci (fixture jam server)
5. [Sesi TC] Klik `[Save]`
6. [Sesi TC] Verifikasi toast sukses "Success, row has been updated."
7. [Sesi TC] Verifikasi baris #1 menampilkan `Acme Corporation` berstatus `pending`
8. [Sesi TC] Verifikasi footer `[Import (12)]` tampil kembali
9. Pulihkan jam server ke waktu nyata dan draft D-01
10. [Sesi TC] Muat ulang halaman Import > Brand
11. [Sesi Admin kedua] Muat ulang halaman Import > Brand

### TC-GS-IMPORT-254: Save pemegang lama ditolak 409 bila kunci kedaluwarsa sudah diambil

12. [Sesi TC] Klik `⋯` pada baris #1
13. [Sesi TC] Pilih Edit
14. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
15. Majukan jam server 11 menit (fixture jam server)
16. [Sesi Admin kedua] Klik `⋯` pada baris #2
17. [Sesi Admin kedua] Pilih Edit
18. [Sesi TC] Klik `[Save]`
19. [Sesi TC] Verifikasi dialog Title "Edit Session Taken Over" dengan Body "Another admin took over this edit session. Your unsaved changes were not saved." dan tombol `[OK]` saja
20. [Sesi TC] Klik `[OK]` pada dialog
21. [Sesi TC] Muat ulang halaman Import > Brand
22. [Sesi TC] Verifikasi baris #1 menampilkan `Acme Corp` (perubahan Total Control tidak tersimpan)
23. [Sesi Admin kedua] Verifikasi baris #2 tetap input aktif
24. [Sesi Admin kedua] Verifikasi footer tetap `[Cancel]` dan `[Save]`
25. [Sesi Admin kedua] Klik `[Cancel]` pada footer; pulihkan jam server ke waktu nyata dan draft D-01

### TC-GS-IMPORT-257: Save pemegang lama setelah Admin kedua melakukan Discard Draft

26. Siapkan draft D-01 berumur 25 jam (varian 1) dan muat ulang halaman Import > Brand pada kedua sesi
27. [Sesi TC] Klik `⋯` pada baris #1
28. [Sesi TC] Pilih Edit
29. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
30. Majukan jam server 11 menit (fixture jam server)
31. [Sesi Admin kedua] Klik `[Discard]` pada Unsaved Banner
32. [Sesi Admin kedua] Klik `[Discard Draft]` pada dialog
33. [Sesi Admin kedua] Tunggu aksi selesai (draft terhapus)
34. [Sesi TC] Klik `[Save]`
35. [Sesi TC] Verifikasi toast netral "This draft is no longer available."
36. [Sesi TC] Verifikasi halaman me-refresh ke state belum ada draft: Dropzone tampil
37. [Sesi TC] Verifikasi Unsaved Banner tidak tampil
38. Pulihkan jam server ke waktu nyata dan reset Client A ke draft D-01

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji perilaku Save setelah TTL kunci habis).
- Spec memuat 38 langkah, sedikit di atas smell 35 langkah. Alasan: semua blok satu kelas harness (TTL kunci dengan fixture jam server) dan tiap blok berdiri sendiri dengan draft dan jam yang dipulihkan, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Urutan TC-GS-IMPORT-257 terakhir karena Discard Draft menghapus draft.
- Konteks kedua beraksi: belum ada id pengecualian untuk Sesi Admin kedua yang beraksi (Edit pada TC-GS-IMPORT-254, Discard Draft pada TC-GS-IMPORT-257) di spec kelas d; `P-2` hanya untuk konteks yang bukan objek asersi dan `P-6` hanya untuk pengamat read-only tanpa interaksi. Spec tidak dipecah (satu kelas harness, blok berdiri sendiri); usulan aturan baru menunggu batch konvensi.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9, 25, 38 (pemulihan jam dan draft), langkah 10 dan 11 (muat ulang halaman kedua sesi sesudah draft dipulihkan), langkah 21 (muat ulang), langkah 26 (menyiapkan draft berumur 25 jam), langkah 33 (menunggu aksi selesai).
- Langkah 37 (absence Unsaved Banner) memakai Dropzone yang tampil di langkah 36 sebagai anchor positif.
- Jam server dipulihkan pada langkah 9, 25, 38 sebelum akun aktor membuka halaman atau log lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-253 mencantumkan Login hanya Total Control sedangkan seluruh langkah memakai satu sesi; spec tidak memakai Sesi Admin kedua pada blok ini.
  - TC-GS-IMPORT-257 Expected b menyebut halaman "me-refresh" tanpa menyebut cara pemicunya; spec mengasersi hasilnya (Dropzone tampil).
