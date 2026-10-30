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
- Akun (Total Control pada tiap Client). Client A: `totalControl_automated_qaTeam1@qwertysystem.net`. Client B: `totalControl_automated_qaTeam2@qwertysystem.net`. Client S, P, N, D, dan X: email mengikuti pola Pre-setup TC `totalControl_automated_{namaClient}@qwertysystem.net`, nilai `{namaClient}` tidak tertulis di Pre-setup TC (lihat Temuan untuk QA):

| Client | Kondisi | Dipakai di | Env var password |
|---|---|---|---|
| Client A (Sari Dewi) | Plan Growth, toggle BYO aktif | TC-GS-HHR-399, TC-GS-HHR-390 | `Spectra.env.GS_TC_PASSWORD` |
| Client S | Plan Starter | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTS_TC_PASSWORD` |
| Client P | Plan Professional | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTP_TC_PASSWORD` |
| Client N | Plan Enterprise | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTN_TC_PASSWORD` |
| Client D | Suspended, memiliki sedikitnya dua reader Available | TC-GS-HHR-402, TC-GS-HHR-400, TC-GS-HHR-227 | `Spectra.env.GS_CLIENTD_TC_PASSWORD` |
| Client X | Expired, memiliki sedikitnya satu reader | TC-GS-HHR-401 | `Spectra.env.GS_CLIENTX_TC_PASSWORD` |
| Client B | Plan Growth, toggle BYO nonaktif, belum ada reader | TC-GS-HHR-391 | `Spectra.env.GS_CLIENTB_TC_PASSWORD` |

- Nama env var Client S, P, N, D, dan X baru dan belum terdaftar di `spectra.config.ts` dan `.env.example`; diusulkan ke owner (satu arti per nama). Password tidak ditulis di spec atau fixture. Login Client A dilakukan di hook `before`; ganti akun ke client lain dilakukan di langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data: Client A dengan Seed Reader A (DD-07 Available, Jalur B, `SN-HHR-00108`); stok `SN-HHR-00302` (Jalur B, tidak ada di stok Principal), katalog Device Name Client A dan Client B memuat DN-01 s.d. DN-07 (dibaca Client read-only). Data Dinamis: Alias Name `Reader Dock 07-{runId}-070` (Client A, DD-07), `Reader Dock 01-{runId}-070` (Client D, ditolak server).
- Kemampuan teknis (disediakan tim FE/BE):
  - Sesi API Principal untuk mematikan dan menyalakan toggle `Allow Self-Purchased Device Activation` (Client A dan Client B). Pelaku hanya memicu perubahan state lewat sesi API dan hasilnya tidak diasersi di sesi itu; endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini.
  - Simulator reader USB/driver lokal untuk Sync `SN-HHR-00302` (mekanisme tidak didefinisikan di TC, PRD, atau LLD; lihat Temuan untuk QA).
  - Pembaca file unduhan CSV untuk mengonfirmasi Download berhasil (blok TC-GS-HHR-402).
  - Pemulihan Seed Reader A, reader Client B yang dibuat TC-GS-HHR-391, dan kedua toggle BYO ke keadaan Tabel Data Uji TC.
- State global yang diubah: toggle BYO Client A (dimatikan lalu dinyalakan kembali dengan langkah eksplisit) dan Client B (dinyalakan, lalu dikembalikan nonaktif di hook `after`), alias DD-07, reader baru Client B. Pemulihan: hook `after` sebagai cadangan.
- Baseline: jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log dicatat sebelum aksi Bulk Mark as (TC-GS-HHR-227).

## Test Steps

### Plan gating Client A, S, P, N: TC-GS-HHR-399

Client A (sesi hook `before`) dikerjakan lebih dulu (langkah 1 sampai 8). Untuk setiap baris tabel "Client plan" (langkah 9 sampai 17):

| Iterasi | Client | Plan |
|---|---|---|
| 1 | Client S | Starter |
| 2 | Client P | Professional |
| 3 | Client N | Enterprise |

1. Buka Global Settings > Hardware > Handheld Reader
2. Verifikasi tombol `[+ Activate Reader]` tampil dan aktif
3. Verifikasi tombol `[+ Activate Reader]` tidak memakai ikon 🔒 dan tidak memunculkan tooltip upgrade
4. Klik `[+ Activate Reader]`
5. Verifikasi Overlay `Select Range Type` terbuka dengan pilihan `Short Range` dan `Long Range`
6. Tutup Overlay `Select Range Type` dengan `Esc`
7. Verifikasi row action reader tersedia
8. Verifikasi ikon Changelog tersedia
9. Ganti akun: logout lalu login sebagai Total Control `{Client}`
10. Buka Global Settings > Hardware > Handheld Reader
11. Verifikasi tombol `[+ Activate Reader]` tampil dan aktif
12. Verifikasi tombol `[+ Activate Reader]` tidak memakai ikon 🔒 dan tidak memunculkan tooltip upgrade
13. Klik `[+ Activate Reader]`
14. Verifikasi Overlay `Select Range Type` terbuka dengan pilihan `Short Range` dan `Long Range`
15. Tutup Overlay `Select Range Type` dengan `Esc`
16. Verifikasi row action reader tersedia
17. Verifikasi ikon Changelog tersedia
18. Verifikasi tampilan halaman pada keempat plan identik (hasil `Verifikasi` langkah 2 sampai 8 sama dengan hasil langkah 11 sampai 17 pada tiap client)

### Client D Suspended: aksi baca lalu aksi tulis ditolak: TC-GS-HHR-402, TC-GS-HHR-400, TC-GS-HHR-227

19. Ganti akun: logout lalu login sebagai Total Control Client D
20. Buka Global Settings > Hardware > Handheld Reader
21. Verifikasi daftar reader Client D tampil tanpa penolakan
22. Klik `Device Name` salah satu reader untuk membuka Popup Detail
23. Verifikasi Popup Detail terbuka dengan Tab Usage dan Tab Changelog tanpa penolakan
24. Tutup Popup Detail, klik ikon Changelog
25. Verifikasi Modal Changelog terbuka tanpa penolakan
26. Tutup Modal Changelog, klik ikon Download, pilih CSV
27. Verifikasi berkas CSV terunduh tanpa penolakan
28. Buka Overlay row action satu reader, klik `Edit Alias Name`, catat `Alias Name` reader tersebut sebagai nilai awal
29. Isi `Alias Name` dengan `Reader Dock 01-{runId}-070`, klik `[Save]`
30. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
31. Verifikasi UI di-refresh dan `Alias Name` reader sama dengan nilai awal
32. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log sebagai baseline
33. Centang checkbox dua reader Available
34. Klik tombol `Bulk Action`
35. Klik `Mark as Damaged`
36. Klik `[Mark as Damaged]` pada dialog
37. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
38. Verifikasi `Status` kedua reader tidak berubah (tetap Available)
39. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log
40. Verifikasi jumlah entri pada Changelog Handheld Reader, System Log aktor, dan Activity Log sama dengan baseline (tidak bertambah)

### Client X Expired: Delete ditolak: TC-GS-HHR-401

41. Ganti akun: logout lalu login sebagai Total Control Client X
42. Buka Global Settings > Hardware > Handheld Reader, catat jumlah reader di tabel
43. Buka Overlay row action satu reader, klik `Delete`
44. Klik `[Delete]` pada dialog
45. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
46. Verifikasi reader tetap ada di tabel (jumlah reader sama dengan yang dicatat)

### Toggle BYO: TC-GS-HHR-391 (Client B), TC-GS-HHR-390 (Client A)

47. Nyalakan toggle `Allow Self-Purchased Device Activation` untuk Client B lewat sesi API Principal hingga tersimpan
48. Tunggu aksi selesai
49. Ganti akun: logout lalu login sebagai Total Control Client B
50. Buka Global Settings > Hardware > Handheld Reader
51. Klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`
52. Klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
53. Pilih `Chainway C72` pada `Device Name`, isi `Brand` `Chainway`, isi `Model/Type` `C72`, klik `[Submit]`
54. Verifikasi aktivasi berhasil: baris `Chainway C72 - 1` dengan `Source` `Self-Purchased` dan `Status` `Available`
55. Ganti akun: logout lalu login sebagai Total Control Client A (Sari Dewi)
56. Buka Global Settings > Hardware > Handheld Reader, catat jumlah reader di tabel
57. Matikan toggle `Allow Self-Purchased Device Activation` untuk Client A lewat sesi API Principal hingga tersimpan
58. Tunggu aksi selesai
59. Muat ulang Handheld Reader
60. Buka Overlay row action DD-07, klik `Edit Alias Name`
61. Isi `Alias Name` dengan `Reader Dock 07-{runId}-070`, klik `[Save]`
62. Verifikasi Edit Alias DD-07 berhasil: `Alias Name` DD-07 menampilkan `Reader Dock 07-{runId}-070`
63. Klik `[+ Activate Reader]`, pilih `Long Range` pada Overlay `Select Range Type`, klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
64. Verifikasi Sync `SN-HHR-00302` ditolak dengan state `Ditolak server` berpesan `Self-purchased device activation is not enabled for your account.`
65. Klik `✕` untuk menutup Popup Activate
66. Verifikasi tidak ada record dibuat (jumlah reader di tabel sama dengan yang dicatat)
67. Nyalakan kembali toggle `Allow Self-Purchased Device Activation` untuk Client A lewat sesi API Principal hingga tersimpan

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 3 untuk TC-GS-HHR-227, Section 7c, 7e). Label Manual Only (b) ada pada TC-GS-HHR-390 dan TC-GS-HHR-391 (reader USB fisik); kebutuhannya ditulis di Prerequisites.
- Urutan: aksi baca/plan (tanpa efek tulis) di awal; kasus tolak server (Client D, X) tidak mengubah data; blok toggle BYO paling akhir karena mengubah state global (prinsip 3 butir 2, 3, 5).
- `P-7` (simulator USB bersama konteks lain, pengecualian atas pemisahan kelas d). Alasan per TC:
  - TC-GS-HHR-390: membutuhkan simulator USB untuk Sync `SN-HHR-00302` yang ditolak server (V-10) dan state tenant toggle BYO Client A yang dimatikan (kelas h) sebagai penentu penolakan.
  - TC-GS-HHR-391: membutuhkan simulator USB untuk Sync `SN-HHR-00302` dan Submit Jalur B, serta state tenant toggle BYO Client B yang dinyalakan (kelas h) sebagai penentu aktivasi diterima.
- Langkah 9 sampai 17 diulang untuk Client S, P, dan N (bagian 8b butir 7), parameter iterasi ada di tabel "Client plan"; Client A dikerjakan terpisah pada langkah 1 sampai 8. Langkah 18 membandingkan hasil keempat client.
- Spec melewati sekitar 35 langkah dengan ekspansi. Alasan: seluruh blok memverifikasi satu topik (state tenant) dan berdiri sendiri; tiap blok memakai client sendiri dan ganti akun eksplisit, sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (prinsip 3, pemisah "beda akun" pengecualian b).
- Langkah penghubung tanpa `Verifikasi` (S-03): ganti akun, buka halaman, tutup popup/modal, mencatat nilai awal dan baseline, muat ulang, mengubah toggle lewat sesi API. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi.
- Temuan untuk QA:
  - TC-GS-HHR-399 tidak menyebut data reader Client S, P, dan N, padahal expected menyebut row action dan Changelog; spec mengasumsikan ketiga client memiliki sedikitnya satu reader.
  - TC-GS-HHR-399 butir "tampilan identik" tidak menyebut cara membandingkan antar plan; spec membandingkan hasil `Verifikasi` tiap client.
  - TC-GS-HHR-390 tidak menyebut cara menutup Popup Activate sesudah Sync ditolak; spec menutup dengan `✕` dan, sesuai S-08, popup yang ditutup sesudah penolakan V-10 langsung tertutup tanpa dialog `Cancel Activation`.
  - TC-GS-HHR-390 butir a ("Edit Alias DD-07 berhasil") tidak menyebut toast; spec mengasersi `Alias Name` DD-07 pada baris.
  - TC-GS-HHR-391 precondition e menyebut katalog Device Name Client A, padahal aktornya Client B; spec mengasumsikan katalog yang sama tersedia di Client B.
  - TC-GS-HHR-402 tidak menyebut tab Popup Detail yang diamati dan cara membuktikan "berfungsi tanpa penolakan"; spec memakai tampilnya Tab Usage dan Tab Changelog dan berkas terunduh.
  - Mekanisme simulasi reader USB (Sync `SN-HHR-00302`) dan cara Principal mengubah toggle BYO tidak didefinisikan di TC, PRD, atau LLD; tidak ada endpoint yang dikarang.
  - Email dan nilai `{namaClient}` untuk akun Total Control Client S, P, N, D, dan X tidak tertulis di Pre-setup TC.
