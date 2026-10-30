---
id: TC-GS-UOM-E2E-060-konflik-delete-dua-admin
title: "Konflik Delete, Bulk Delete, dan Buka Detail pada Unit yang Dihapus Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UOM-103
  - TC-GS-UOM-344
  - TC-GS-UOM-345
  - TC-GS-UOM-357
  - TC-GS-UOM-413
coverage:
  web: automated
---

# Konflik Delete, Bulk Delete, dan Buka Detail pada Unit yang Dihapus Admin Lain

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama): Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Admin kedua (pelaku perubahan state): Total Control Client A kedua, `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Admin kedua hanya memicu Delete dan memakai sesi API; tidak ada sesi UI kedua. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); fixture disediakan tim FE.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data Pre-setup Client A (hanya dibaca, tidak diubah, Last Updated tidak berubah; dilewati oleh guard in-use, S-06): `Box` (in-use, FAMS 4 asset names), tanpa suffix `{runId}`.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), semuanya bebas relasi, di-seed lewat API di hook `before`, milik spec ini:
  - `Peck {runId}-060` / `pck` (D-19): dihapus admin kedua pada TC-GS-UOM-103.
  - `Ladle {runId}-060` / `ld` dan `Spool {runId}-060` / `sl` (D-32): Ladle dihapus Sesi A, Spool dihapus admin kedua, pada TC-GS-UOM-344.
  - `Bin {runId}-060` / `bn` (D-33): dihapus admin kedua pada TC-GS-UOM-345.
  - `Cask {runId}-060` / `ck` dan `Vat {runId}-060` / `vt` (D-37): keduanya dihapus admin kedua pada TC-GS-UOM-357.
  - `Reed {runId}-060` / `rd` (D-40): dihapus admin kedua pada TC-GS-UOM-413.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua unit dinamis di atas bila masih ada dan pulihkan page size tabel Measurement ke 10.
- Kemampuan teknis: sesi API aktor (lihat `suite.md`, bagian Hook suite) untuk Delete Measurement oleh admin kedua dengan menunggu hasil tersimpan; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Tidak ada state global yang diubah.
- Jeda nyata (bagian 6 konvensi, jeda pendek ±30 detik): langkah 7, 22, dan 30 menunggu toast sebelumnya hilang otomatis; lama hilang otomatis mengikuti perilaku aplikasi dan tidak ditetapkan TC.
- TC-GS-UOM-103, 344, 345, 357, 413: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-103: Delete unit yang sudah dihapus admin lain

1. [Sesi A] Ketik Search `Peck {runId}-060`, tekan Enter, klik `⋯` pada baris tersebut > Delete
2. [Sesi B, sesi API] Hapus `Peck {runId}-060` hingga tersimpan
3. [Sesi A] Klik [Delete] pada dialog
4. [Sesi A] Verifikasi toast: "This unit is no longer available."
5. [Sesi A] Verifikasi dialog Delete tertutup
6. [Sesi A] Verifikasi tabel me-refresh sehingga `Peck {runId}-060` tidak ada

### TC-GS-UOM-344: Bulk Delete berisi unit yang sudah dihapus admin lain

7. [Sesi A] Tunggu toast sebelumnya hilang otomatis, lalu ganti isi kotak search dengan `{runId}-060`, tekan Enter
8. [Sesi A] Centang baris `Ladle {runId}-060` dan `Spool {runId}-060`
9. [Sesi A] Klik `Bulk Action` > `Delete`
10. [Sesi B, sesi API] Hapus `Spool {runId}-060` hingga tersimpan
11. [Sesi A] Klik [Delete] pada dialog Bulk Delete homogen
12. [Sesi A] Verifikasi toast: "Success, unit has been deleted. Some items were skipped."
13. [Sesi A] Verifikasi tidak ada toast atau dialog lain selain toast pada langkah 12 (Spool dilewati tanpa pesan terpisah)
14. [Sesi A] Verifikasi `Ladle {runId}-060` terhapus
15. [Sesi A] Verifikasi tabel me-refresh sehingga `Ladle {runId}-060` dan `Spool {runId}-060` tidak ada

### TC-GS-UOM-345: Membuka Unit Detail untuk unit yang baru dihapus admin lain

16. [Sesi A] Klik `(←)` pada kotak Search, lalu ketik Search `Bin {runId}-060`, tekan Enter (baris Bin termuat di tabel Sesi A)
17. [Sesi B, sesi API] Hapus `Bin {runId}-060` hingga tersimpan (tabel Sesi A belum di-refresh)
18. [Sesi A] Klik teks `Bin {runId}-060`
19. [Sesi A] Verifikasi toast: "This unit is no longer available."
20. [Sesi A] Verifikasi modal Unit Detail tertutup otomatis
21. [Sesi A] Verifikasi tabel me-refresh sehingga `Bin {runId}-060` tidak ada

### TC-GS-UOM-357: Bulk Delete saat seluruh unit terpilih sudah dihapus admin lain

22. [Sesi A] Tunggu toast sebelumnya hilang otomatis, lalu klik `(←)` pada kotak Search dan ketik Search `{runId}-060`, tekan Enter
23. [Sesi A] Centang baris `Cask {runId}-060` dan `Vat {runId}-060`
24. [Sesi A] Klik `Bulk Action` > `Delete`
25. [Sesi B, sesi API] Hapus `Cask {runId}-060` dan `Vat {runId}-060` hingga tersimpan
26. [Sesi A] Klik [Delete] pada dialog Bulk Delete homogen
27. [Sesi A] Verifikasi toast: "This unit is no longer available."
28. [Sesi A] Verifikasi toast "Success, unit has been deleted. Some items were skipped." tidak tampil
29. [Sesi A] Verifikasi tabel me-refresh sehingga `Cask {runId}-060` dan `Vat {runId}-060` tidak ada

### TC-GS-UOM-413: Bulk Delete tanpa unit terhapus, D-02 hanya untuk unit in-use

30. [Sesi A] Tunggu toast sebelumnya hilang otomatis, klik `(←)` pada kotak Search, ubah page size tabel menjadi 50
31. [Sesi A] Centang baris `Box` dan `Reed {runId}-060`
32. [Sesi A] Klik `Bulk Action` > `Delete`
33. [Sesi B, sesi API] Hapus `Reed {runId}-060` hingga tersimpan
34. [Sesi A] Klik [Continue] pada dialog Bulk Delete campuran
35. [Sesi A] Verifikasi dialog `Cannot Delete Data` memuat bullet `Box` dengan sub-bullet `FAMS (4 asset names)`
36. [Sesi A] Verifikasi `Reed {runId}-060` tidak tampil di dialog `Cannot Delete Data`
37. [Sesi A] Verifikasi tidak ada toast "This unit is no longer available." maupun "Success, unit has been deleted. Some items were skipped."
38. [Sesi A] Klik [OK]
39. [Sesi A] Verifikasi `Box` tetap ada di tabel
40. [Sesi A] Verifikasi tabel me-refresh sehingga `Reed {runId}-060` tidak ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: fungsional (konflik data pada unit yang dihapus admin kedua). Admin kedua hanya pemicu state dan memakai sesi API; Sesi A satu-satunya sesi UI, sehingga spec ini bukan kelas multi-konteks.
- Urutan TC mengikuti nomor TC sumber; data tiap TC independen dan seluruhnya dihapus (prinsip 5 terpenuhi karena tidak ada kasus lain yang membutuhkan baris yang dihapus). TC-GS-UOM-413 terakhir karena memakai page size 50.
- TC-GS-UOM-91 (Edit unit yang dihapus admin lain) ada di spec `TC-GS-UOM-E2E-059-konflik-create-edit-dua-admin`; resilience cek referensi dan delete gagal (5xx, timeout) di spec 035; TC-GS-UOM-102 dan 123 (unit menjadi in-use setelah cek awal) di spec 061.
- Langkah penghubung: langkah 1, 16, 22 (Search baris target; tabel memuat lebih dari satu halaman), langkah 7, 22, 30 (menunggu toast sebelumnya hilang agar hitungan toast di langkah 13, 28, dan 37 hanya memuat toast blok ini), langkah 30 (ubah page size menjadi 50 agar `Box` dan `Reed` tampil bersama untuk dicentang; dipulihkan ke 10 di hook `after`), langkah 38 (menutup dialog `Cannot Delete Data`).
- TC-GS-UOM-357 Expected a ("Tidak ada unit yang benar-benar terhapus oleh aktor") tidak teramati terpisah di UI; kesimpulannya dicakup oleh langkah 28 (toast sukses dan skipped tidak tampil) dan langkah 27 sebagai anchor (S-03).
- TC-GS-UOM-413 menyebut `Box` Pre-setup (in-use, FAMS 4 asset names); `Box` hanya dibaca dan dilewati guard, tidak diubah (pengecualian S-06). Reed milik spec bersuffix.
- Sumber menulis nama literal (Peck, Ladle, Spool, Bin, Cask, Vat, Reed); spec memakai nama bersuffix `{runId}-060` (S-12) dan Search `{runId}-060` untuk memuat baris target.
- Spec memuat 40 langkah (melewati batas 35 langkah) karena lima TC konflik berdiri sendiri dengan data sendiri; seluruhnya satu pola (konflik Delete oleh admin kedua lewat sesi API), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Alasan spec ini terpisah dari `TC-GS-UOM-E2E-061-konflik-in-use-saat-confirm-delete`: pelaku pemicu dan dataset berbeda. Spec ini memakai admin kedua (`GS_TC2_PASSWORD`) yang menghapus unit lewat sesi API dan hanya men-seed unit bebas relasi; spec 061 memakai Admin FAMS (`FA_ADMIN_PASSWORD`) yang membuat Asset Name FAMS sehingga unit menjadi in-use, membutuhkan fixture `assetName.*`, dan membersihkan Asset Name sebelum unitnya. Gabungan kedua spec 55 langkah (40 + 15), sehingga kegagalan seeding atau fixture Asset Name FAMS di spec 061 tidak ikut menutupi hasil lima TC konflik Delete di spec ini.
- Temuan untuk QA:
  - Admin lain pada seluruh TC tidak ada di Tabel Data Uji Pre-setup; spec memakai akun Total Control Client A kedua yang disediakan tim FE (S-13).
  - TC-GS-UOM-344 dan 357 Post Condition ("Ladle dan Spool tidak ada", "Cask dan Vat tidak ada") dicakup oleh Expected d dan c yang sama; TC-GS-UOM-345 dan 413 Post Condition ("Bin terhapus", "Reed tidak ada") dicakup langkah 21 dan 40.
