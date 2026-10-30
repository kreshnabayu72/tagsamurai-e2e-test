---
id: TC-GS-HHR-E2E-073-konkurensi-edit-dan-status-dua-admin
title: "Konkurensi Dua Admin: Edit Alias Name, Edit Reader Power, Mark as Damaged, dan Edit pada Reader yang Dihapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-427
  - TC-GS-HHR-428
  - TC-GS-HHR-430
  - TC-GS-HHR-431
  - TC-GS-HHR-452
coverage:
  web: automated
---

# Konkurensi Dua Admin: Edit Alias Name, Edit Reader Power, Mark as Damaged, dan Edit pada Reader yang Dihapus

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, dua admin Client A pada reader yang sama). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini dan akun Admin B (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Peran | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| B (UI) | Admin B, Total Control (Client A) | Nadia Pratama | `totalControlSecond_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC2_PASSWORD` |
| B (API) | Admin B yang sama, hanya memicu perubahan state | Nadia Pratama | Sesi API akun yang sama | Sesi API |

- Login Sesi A dilakukan di hook `before`; Sesi B (UI) dibuka dengan langkah ganti akun eksplisit (langkah 1) hanya untuk TC-GS-HHR-427 dan TC-GS-HHR-452 karena hasil di sesi B diasersi (tanpa dialog konflik). Untuk TC-GS-HHR-428, TC-GS-HHR-430, dan TC-GS-HHR-431 Admin B memakai sesi API karena hanya memicu perubahan state; langkah pemicunya ditulis "hingga ... tersimpan". Hook `after` menutup Sesi B dan mengembalikan sesi ke akun default suite (Sesi A).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE): DD-01 (`Zebra RFID Reader - 1`, Available, Long Range, `Reader Power` 30 dBm, `Alias Name` `—`), DD-02 (`Gudang Reader - 1`, Available). Data Dinamis: Alias Name `Dock A-{runId}-073`, `Dock B-{runId}-073`.
- Kemampuan teknis (disediakan tim FE/BE): konteks browser kedua untuk Sesi B (UI); sesi API Admin B untuk Mark as Damaged, Mark as Missing, dan Delete (endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini); pemulihan Seed Reader A ke keadaan Tabel Data Uji Dinamis TC antar blok (fixture BE; Catatan TC: tabel dipulihkan antar TC).
- Baseline: jumlah entri Changelog Handheld Reader, System Log aktor (Sari Dewi), dan Activity Log dicatat sesudah aksi Admin B dan sebelum aksi Sesi A (TC-GS-HHR-430, TC-GS-HHR-431), karena aksi Admin B sendiri menambah entri (S-12).
- State global yang diubah: Seed Reader A (DD-01, DD-02). Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Persiapan sesi

1. Ganti akun: buka konteks browser kedua (Sesi B) dan login sebagai Admin kedua Total Control Client A

### Last-write-wins Edit Alias Name dan Edit Reader Power: TC-GS-HHR-427, TC-GS-HHR-452

2. Pulihkan Seed Reader A
3. Sesi A: muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Edit Alias Name`
4. Sesi B: muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Edit Alias Name`
5. Sesi A: isi `Alias Name` dengan `Dock A-{runId}-073`, klik `[Save]`
6. Verifikasi Save Sesi A berhasil: `Alias Name` DD-01 di Sesi A menampilkan `Dock A-{runId}-073`
7. Sesi B: isi `Alias Name` dengan `Dock B-{runId}-073`, klik `[Save]`
8. Verifikasi Save Sesi B berhasil tanpa dialog konflik
9. Sesi B: muat ulang Handheld Reader
10. Verifikasi `Alias Name` DD-01 akhir `Dock B-{runId}-073`
11. Sesi A: klik ikon Changelog
12. Verifikasi Changelog memuat entri `Alias Name` DD-01 dari `—` ke `Dock A-{runId}-073`
13. Verifikasi Changelog memuat entri `Alias Name` DD-01 dari `Dock A-{runId}-073` ke `Dock B-{runId}-073`
14. Sesi A: tutup Modal Changelog
15. Pulihkan Seed Reader A
16. Sesi A: muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Edit Reader Power`
17. Sesi B: muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Edit Reader Power`
18. Sesi A: geser slider `Reader Power` ke 20 dBm, klik `[Save]`
19. Verifikasi Save Sesi A berhasil: `Reader Power` DD-01 di Sesi A menampilkan `20 dBm`
20. Sesi B: geser slider `Reader Power` ke 25 dBm, klik `[Save]`
21. Verifikasi Save Sesi B berhasil tanpa dialog konflik
22. Sesi B: muat ulang Handheld Reader
23. Verifikasi `Reader Power` DD-01 akhir `25 dBm`
24. Sesi A: klik ikon Changelog
25. Verifikasi Changelog memuat entri `Reader Power` DD-01 dari `30 dBm` ke `20 dBm`
26. Verifikasi Changelog memuat entri `Reader Power` DD-01 dari `20 dBm` ke `25 dBm`
27. Sesi A: tutup Modal Changelog

### Mark as Damaged saat reader sudah Damaged atau Missing: TC-GS-HHR-430, TC-GS-HHR-431

28. Pulihkan Seed Reader A
29. Sesi A: muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Mark as Damaged` (dialog tetap terbuka)
30. Admin B: Mark as Damaged DD-01 lewat sesi API hingga tersimpan
31. Tunggu aksi selesai
32. Sesi A: catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log sebagai baseline
33. Sesi A: klik `[Mark as Damaged]` pada dialog
34. Verifikasi dialog `Device Changed` dengan body "This device was changed by someone else. Please review." dan tombol `[OK]` tampil
35. Sesi A: klik `[OK]`
36. Verifikasi dialog tertutup
37. Verifikasi daftar dimuat ulang dan `Status` DD-01 tetap `Damaged`
38. Sesi A: buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log
39. Verifikasi jumlah entri pada Changelog Handheld Reader, System Log aktor, dan Activity Log sama dengan baseline (tidak ada efek tambahan dari aksi kedua)
40. Pulihkan Seed Reader A
41. Sesi A: muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Mark as Damaged` (dialog tetap terbuka)
42. Admin B: Mark as Missing DD-01 lewat sesi API hingga tersimpan
43. Tunggu aksi selesai
44. Sesi A: catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log sebagai baseline
45. Sesi A: klik `[Mark as Damaged]` pada dialog
46. Verifikasi dialog `Device Changed` dengan body "This device was changed by someone else. Please review." dan tombol `[OK]` tampil
47. Sesi A: klik `[OK]`
48. Verifikasi dialog tertutup
49. Verifikasi daftar dimuat ulang dan `Status` DD-01 tetap `Missing`
50. Sesi A: buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log
51. Verifikasi jumlah entri pada Changelog Handheld Reader, System Log aktor, dan Activity Log sama dengan baseline (tidak bertambah dari sesi A)

### Edit Alias saat reader sudah dihapus admin lain (menghapus data, paling akhir): TC-GS-HHR-428

52. Pulihkan Seed Reader A
53. Sesi A: muat ulang Handheld Reader, buka Overlay row action DD-02, klik `Edit Alias Name` (dialog tetap terbuka)
54. Admin B: Delete DD-02 lewat sesi API hingga tersimpan
55. Tunggu aksi selesai
56. Sesi A: isi `Alias Name` dengan `Dock A-{runId}-073`, klik `[Save]`
57. Verifikasi muncul toast netral `This device is no longer available.`
58. Verifikasi daftar di-refresh dan baris DD-02 tidak ada (anchor: toast hasil server)

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 9). Semua TC berlabel Manual Only (d): butuh dua sesi atau pengguna paralel; kebutuhannya ditulis di Prerequisites.
- Urutan: edit last-write-wins (tidak mengubah Status) lebih dulu, perubahan status berikutnya, Delete oleh Admin B paling akhir (prinsip 3 butir 5). Seed Reader A dipulihkan di awal tiap blok (langkah 2, 15, 28, 40, 52) supaya kegagalan satu blok tidak menutupi hasil blok lain.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan Seed Reader A, muat ulang, membuka dialog, menutup Modal Changelog, mencatat baseline. Langkah "Tunggu aksi selesai" dipakai karena aksi Admin B lewat sesi API diikuti pengamatan di Sesi A.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas harness (multi-konteks dua admin) dan berdiri sendiri; tiap blok memulihkan data dan tidak bergantung pada hasil blok lain.
- Perilaku Admin B yang sama (TC-GS-HHR-430, TC-GS-HHR-431) dibaca di Sesi A saja; Sesi UI kedua hanya dipakai pada TC-GS-HHR-427 dan TC-GS-HHR-452 karena hasil di sesi B diasersi.
- Temuan untuk QA:
  - TC-GS-HHR-427 dan TC-GS-HHR-452 mengharapkan "tanpa dialog konflik" pada Save sesi kedua; TC tidak menyebut apakah Save sesi pertama diverifikasi di sesi A, sehingga spec mengasersi hasil Save sesi A hanya lewat nilai pada baris DD-01 (butir tambahan yang dicatat sebagai asersi pendukung).
  - TC-GS-HHR-430 dan TC-GS-HHR-431 menyatakan "Tidak ada efek tambahan" dan membandingkan jumlah entri "dengan sebelum aksi"; karena aksi Admin B sendiri menambah entri, baseline spec dicatat sesudah aksi Admin B dan sebelum klik sesi A.
  - TC-GS-HHR-428 menyebut Save tanpa menyebut nilai `Alias Name` yang valid; spec memakai `Dock A-{runId}-073`.
  - TC-GS-HHR-452 mengharapkan `Reader Power` DD-01 awal 30 dBm ("`30 dBm` ke `20 dBm`") sesuai Seed Reader A.
