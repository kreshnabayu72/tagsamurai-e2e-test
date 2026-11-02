---
id: TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo
title: "State Tenant: Plan Starter sampai Enterprise, Client Suspended dan Expired Menolak Tulis, dan Toggle Self-Purchased Device Activation"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-HHR-227
  - TC-GS-HHR-390
  - TC-GS-HHR-391
  - TC-GS-HHR-399
  - TC-GS-HHR-400
  - TC-GS-HHR-401
  - TC-GS-HHR-402
coverage:
  web: automated
---

# State Tenant: Plan Starter sampai Enterprise, Client Suspended dan Expired Menolak Tulis, dan Toggle Self-Purchased Device Activation

## Prerequisites

- Mode: FE+BE. Kelas harness: state tenant (kelas h, write-lockdown Suspended/Expired, plan tier, toggle BYO). TC-GS-HHR-390 dan TC-GS-HHR-391 juga membutuhkan simulator reader USB (kelas d) bersama state tenant toggle BYO sesuai pengecualian `P-7` (lihat Notes). Suite `parallel: false` karena spec mengubah state global (toggle BYO Client A dan Client B).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun pada tabel di bawah (lihat `suite.md`, Hook suite).
- Akun (Total Control pada tiap Client). Client A: `totalControl_automated_qaTeam1@qwertysystem.net`. Client B: `totalControl_automated_qaTeam2@qwertysystem.net`. Client P: `totalControl_automated_qaTeam12@qwertysystem.net`. Client N: `totalControl_automated_qaTeam13@qwertysystem.net`. Client D: `totalControl_automated_qaTeam9@qwertysystem.net`. Client X: `totalControl_automated_qaTeam11@qwertysystem.net`. Client S: email disediakan tim FE (tidak tertulis di Pre-setup TC; lihat Temuan untuk QA):

| Client | Kondisi | Dipakai di | Env var password |
|---|---|---|---|
| Client A (Sari Dewi) | Plan Growth, toggle BYO aktif | TC-GS-HHR-399, TC-GS-HHR-390 | `Spectra.env.GS_TC_PASSWORD` |
| Client S | Plan Starter, memiliki sedikitnya satu reader | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTS_TC_PASSWORD` |
| Client P | Plan Professional, memiliki sedikitnya satu reader | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTP_TC_PASSWORD` |
| Client N | Plan Enterprise, memiliki sedikitnya satu reader | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTN_TC_PASSWORD` |
| Client D | Suspended, memiliki sedikitnya dua reader Available | TC-GS-HHR-402, TC-GS-HHR-400, TC-GS-HHR-227 | `Spectra.env.GS_CLIENTD_TC_PASSWORD` |
| Client X | Expired, memiliki sedikitnya satu reader | TC-GS-HHR-401 | `Spectra.env.GS_CLIENTX_TC_PASSWORD` |
| Client B | Plan Growth, toggle BYO nonaktif, belum ada reader | TC-GS-HHR-391 | `Spectra.env.GS_CLIENTB_TC_PASSWORD` |

- Nama env var Client S, P, N, D, dan X baru dan belum terdaftar di `spectra.config.ts` dan `.env.example`; diusulkan ke owner (satu arti per nama). Password tidak ditulis di spec atau fixture. Login Client A dilakukan di hook `before`; ganti akun ke client lain dilakukan di langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data: Client A dengan Seed Reader A (DD-07 Available, Jalur B, `SN-HHR-00108`); stok `SN-HHR-00302` (Jalur B, tidak ada di stok Principal), katalog Device Name Client A dan Client B memuat DN-01 s.d. DN-07 (dibaca Client read-only). Client S, P, dan N masing-masing memiliki sedikitnya satu reader (dibutuhkan untuk asersi row action dan ikon Changelog TC-GS-HHR-399; disediakan tim FE/BE). Data Dinamis: Alias Name `Reader Dock 07-{runId}-070` (Client A, DD-07), `Reader Dock 01-{runId}-070` (Client D, ditolak server).
- Kemampuan teknis (disediakan tim FE/BE):
  - Sesi API Principal untuk mematikan dan menyalakan toggle `Allow Self-Purchased Device Activation` (Client A dan Client B). Pelaku hanya memicu perubahan state lewat sesi API dan hasilnya tidak diasersi di sesi itu; endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini.
  - Simulator reader USB/driver lokal untuk Sync `SN-HHR-00302` (mekanisme tidak didefinisikan di TC, PRD, atau LLD; lihat Temuan untuk QA).
  - Pembaca file unduhan CSV untuk mengonfirmasi Download berhasil (blok TC-GS-HHR-402).
  - Pemulihan Seed Reader A, reader Client B yang dibuat TC-GS-HHR-391 beserta stok `SN-HHR-00302` ke bebas (fixture BE yang dinyatakan di `suite.md`; dijalankan juga sebagai langkah penghubung 60 antara TC-GS-HHR-391 dan TC-GS-HHR-390), dan kedua toggle BYO ke keadaan Tabel Data Uji TC.
- State global yang diubah: toggle BYO Client A (dimatikan lalu dinyalakan kembali dengan langkah eksplisit) dan Client B (dinyalakan, lalu dikembalikan nonaktif di hook `after`), alias DD-07, reader baru Client B, dan stok `SN-HHR-00302` (dipulihkan pada langkah 60). Pemulihan: hook `after` sebagai cadangan.
- Baseline: jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`) dicatat sebelum aksi Bulk Mark as (TC-GS-HHR-227).

## Test Steps

### Plan gating Client A, S, P, N: TC-GS-HHR-399

Client A (sesi hook `before`) dikerjakan lebih dulu (langkah 1 sampai 9). Untuk setiap baris tabel "Client plan" (langkah 10 sampai 19):

| Iterasi | Client | Plan |
|---|---|---|
| 1 | Client S | Starter |
| 2 | Client P | Professional |
| 3 | Client N | Enterprise |

1. Buka Global Settings > Hardware > Handheld Reader
2. Verifikasi tombol `[+ Activate Reader]` tampil dan aktif
3. Arahkan kursor ke `[+ Activate Reader]`
4. Verifikasi tombol `[+ Activate Reader]` tidak memakai ikon 🔒 dan tidak memunculkan tooltip upgrade
5. Klik `[+ Activate Reader]`
6. Verifikasi Overlay `Select Range Type` terbuka dengan pilihan `Short Range` dan `Long Range`
7. Tutup Overlay `Select Range Type` dengan `Esc`
8. Verifikasi row action reader tersedia
9. Verifikasi ikon Changelog tersedia
10. Ganti akun: logout lalu login sebagai Total Control `{Client}`
11. Buka Global Settings > Hardware > Handheld Reader
12. Verifikasi tombol `[+ Activate Reader]` tampil dan aktif
13. Arahkan kursor ke `[+ Activate Reader]`
14. Verifikasi tombol `[+ Activate Reader]` tidak memakai ikon 🔒 dan tidak memunculkan tooltip upgrade
15. Klik `[+ Activate Reader]`
16. Verifikasi Overlay `Select Range Type` terbuka dengan pilihan `Short Range` dan `Long Range`
17. Tutup Overlay `Select Range Type` dengan `Esc`
18. Verifikasi row action reader tersedia
19. Verifikasi ikon Changelog tersedia
20. Verifikasi tampilan halaman pada keempat plan identik (hasil `Verifikasi` langkah 2 sampai 9 sama dengan hasil langkah 12 sampai 19 pada tiap client)

### Client D Suspended: aksi baca lalu aksi tulis ditolak: TC-GS-HHR-402, TC-GS-HHR-400, TC-GS-HHR-227

21. Ganti akun: logout lalu login sebagai Total Control Client D
22. Buka Global Settings > Hardware > Handheld Reader
23. Verifikasi daftar reader Client D tampil tanpa penolakan
24. Klik `Device Name` salah satu reader untuk membuka Popup Detail
25. Verifikasi Popup Detail terbuka dengan Tab Usage dan Tab Changelog tanpa penolakan
26. Tutup Popup Detail, klik ikon Changelog
27. Verifikasi Modal Changelog terbuka tanpa penolakan
28. Tutup Modal Changelog, klik ikon Download, pilih CSV
29. Verifikasi berkas CSV terunduh tanpa penolakan
30. Buka Overlay row action satu reader, klik `Edit Alias Name`, catat `Alias Name` reader tersebut sebagai nilai awal
31. Isi `Alias Name` dengan `Reader Dock 01-{runId}-070`, klik `[Save]`
32. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
33. Verifikasi dialog Edit Alias Name tertutup
34. Verifikasi UI di-refresh dan `Alias Name` reader sama dengan nilai awal
35. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`) sebagai baseline
36. Centang checkbox dua reader Available
37. Klik tombol `Bulk Action`
38. Klik `Mark as Damaged`
39. Klik `[Mark as Damaged]` pada dialog
40. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
41. Verifikasi `Status` kedua reader tidak berubah (tetap Available)
42. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`)
43. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline (tidak bertambah)
44. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak bertambah)
45. Verifikasi jumlah entri Activity Log (tab `User Action`) sama dengan baseline (tidak bertambah)

### Client X Expired: Delete ditolak: TC-GS-HHR-401

46. Ganti akun: logout lalu login sebagai Total Control Client X
47. Buka Global Settings > Hardware > Handheld Reader, catat jumlah reader di tabel
48. Buka Overlay row action satu reader, klik `Delete`
49. Klik `[Delete]` pada dialog
50. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
51. Verifikasi reader tetap ada di tabel (jumlah reader sama dengan yang dicatat)

### Toggle BYO: TC-GS-HHR-391 (Client B), TC-GS-HHR-390 (Client A)

52. Nyalakan toggle `Allow Self-Purchased Device Activation` untuk Client B lewat sesi API Principal hingga tersimpan
53. Tunggu aksi selesai
54. Ganti akun: logout lalu login sebagai Total Control Client B
55. Buka Global Settings > Hardware > Handheld Reader
56. Klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`
57. Klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
58. Pilih `Chainway C72` pada `Device Name`, isi `Brand` `Chainway`, isi `Model/Type` `C72`, klik `[Submit]`
59. Verifikasi aktivasi berhasil: baris `Chainway C72 - 1` dengan `Source` `Self-Purchased` dan `Status` `Available`
60. Pulihkan reader Client B yang dibuat TC-GS-HHR-391 dan stok `SN-HHR-00302` ke bebas, sebelum TC-GS-HHR-390 memakai serial yang sama
61. Ganti akun: logout lalu login sebagai Total Control Client A (Sari Dewi)
62. Buka Global Settings > Hardware > Handheld Reader, catat jumlah reader di tabel
63. Matikan toggle `Allow Self-Purchased Device Activation` untuk Client A lewat sesi API Principal hingga tersimpan
64. Tunggu aksi selesai
65. Muat ulang Handheld Reader
66. Buka Overlay row action DD-07, klik `Edit Alias Name`
67. Isi `Alias Name` dengan `Reader Dock 07-{runId}-070`, klik `[Save]`
68. Verifikasi Edit Alias DD-07 berhasil: `Alias Name` DD-07 menampilkan `Reader Dock 07-{runId}-070`
69. Klik `[+ Activate Reader]`, pilih `Long Range` pada Overlay `Select Range Type`, klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
70. Verifikasi Sync `SN-HHR-00302` ditolak dengan state `Ditolak server` berpesan `Self-purchased device activation is not enabled for your account.`
71. Klik `✕` untuk menutup Popup Activate
72. Verifikasi tidak ada record dibuat (jumlah reader di tabel sama dengan yang dicatat)
73. Nyalakan kembali toggle `Allow Self-Purchased Device Activation` untuk Client A lewat sesi API Principal hingga tersimpan

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 3 untuk TC-GS-HHR-227, Section 7c, 7e). Label Manual Only (b) ada pada TC-GS-HHR-390 dan TC-GS-HHR-391 (reader USB fisik); kebutuhannya ditulis di Prerequisites.
- Urutan: aksi baca/plan (tanpa efek tulis) di awal; kasus tolak server (Client D, X) tidak mengubah data; blok toggle BYO paling akhir karena mengubah state global (prinsip 3 butir 2, 3, 5).
- `P-7` (simulator USB bersama konteks lain, pengecualian atas pemisahan kelas d). Alasan per TC:
  - TC-GS-HHR-390: membutuhkan simulator USB untuk Sync `SN-HHR-00302` yang ditolak server (V-10) dan state tenant toggle BYO Client A yang dimatikan (kelas h) sebagai penentu penolakan.
  - TC-GS-HHR-391: membutuhkan simulator USB untuk Sync `SN-HHR-00302` dan Submit Jalur B, serta state tenant toggle BYO Client B yang dinyalakan (kelas h) sebagai penentu aktivasi diterima.
  - TC-GS-HHR-399, TC-GS-HHR-400, TC-GS-HHR-401, TC-GS-HHR-402, dan TC-GS-HHR-227 tidak membutuhkan USB, tetapi sejenis kelas h (state tenant: plan, Suspended, Expired) dengan TC-GS-HHR-390 dan TC-GS-HHR-391; sesuai kalimat akhir `P-7`, hanya blok yang tidak membutuhkan USB dan bukan kelas c atau h sejenis yang dipisah ke spec sendiri, sehingga kelima TC itu tetap di spec ini.
- Langkah 10 sampai 19 diulang untuk Client S, P, dan N (bagian 8b butir 7), parameter iterasi ada di tabel "Client plan"; Client A dikerjakan terpisah pada langkah 1 sampai 9. Langkah 20 membandingkan hasil keempat client.
- Spec melewati sekitar 35 langkah dengan ekspansi. Alasan: seluruh blok memverifikasi satu topik (state tenant) dan berdiri sendiri; tiap blok memakai client sendiri dan ganti akun eksplisit, sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (prinsip 3, pemisah "beda akun" pengecualian b).
- Langkah penghubung tanpa `Verifikasi` (S-03): ganti akun, buka halaman, tutup popup/modal, mencatat nilai awal dan baseline, muat ulang, mengubah toggle lewat sesi API, mengarahkan kursor ke `[+ Activate Reader]` sebelum asersi absence tooltip (langkah 3 dan 13), memulihkan reader Client B dan stok `SN-HHR-00302` (langkah 60). Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi.
- Temuan untuk QA:
  - TC-GS-HHR-399 tidak menyebut data reader Client S, P, dan N, padahal expected menyebut row action dan Changelog; spec menuliskan di Prerequisites bahwa ketiga client memiliki sedikitnya satu reader (disediakan tim FE/BE).
  - TC-GS-HHR-399 butir "tampilan identik" tidak menyebut cara membandingkan antar plan; spec membandingkan hasil `Verifikasi` tiap client.
  - TC-GS-HHR-390 dan TC-GS-HHR-391 memakai serial `SN-HHR-00302` tanpa urutan atau pemulihan di antaranya; spec menjalankan TC-GS-HHR-391 lebih dulu dan memulihkan reader Client B beserta stok `SN-HHR-00302` lewat fixture BE (langkah 60) sebelum TC-GS-HHR-390.
  - TC-GS-HHR-390 tidak menyebut cara menutup Popup Activate sesudah Sync ditolak; spec menutup dengan `✕` dan, sesuai S-08, popup yang ditutup sesudah penolakan V-10 langsung tertutup tanpa dialog `Cancel Activation`.
  - TC-GS-HHR-390 butir a ("Edit Alias DD-07 berhasil") tidak menyebut toast; spec mengasersi `Alias Name` DD-07 pada baris.
  - TC-GS-HHR-391 precondition e menyebut katalog Device Name Client A, padahal aktornya Client B; spec mengasumsikan katalog yang sama tersedia di Client B.
  - TC-GS-HHR-402 tidak menyebut tab Popup Detail yang diamati dan cara membuktikan "berfungsi tanpa penolakan"; spec memakai tampilnya Tab Usage dan Tab Changelog dan berkas terunduh.
  - Mekanisme simulasi reader USB (Sync `SN-HHR-00302`) dan cara Principal mengubah toggle BYO tidak didefinisikan di TC, PRD, atau LLD; tidak ada endpoint yang dikarang.
  - Email akun Total Control Client S tidak tertulis di Pre-setup TC.
