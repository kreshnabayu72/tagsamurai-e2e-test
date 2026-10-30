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

- Mode: FE+BE. Kelas harness: state tenant (kelas h, write-lockdown Suspended/Expired, plan tier, toggle BYO). TC-GS-HHR-390 dan TC-GS-HHR-391 juga memakai simulator reader USB (kelas d) sebagai bagian pemicu. Suite `parallel: false` karena spec mengubah state global (toggle BYO Client A dan Client B).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk setiap akun pada tabel di bawah (lihat `suite.md`, Hook suite).
- Akun (Total Control pada tiap Client; email mengikuti pola Pre-setup TC `totalControl_automated_{namaClient}@qwertysystem.net`, nilai `{namaClient}` tidak tertulis di Pre-setup TC, lihat Temuan untuk QA):

| Client | Kondisi | Dipakai di | Env var password |
|---|---|---|---|
| Client A (Sari Dewi) | Plan Growth, toggle BYO aktif | TC-GS-HHR-399, TC-GS-HHR-390 | `Spectra.env.GS_TC_PASSWORD` |
| Client S | Plan Starter | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTS_TC_PASSWORD` |
| Client P | Plan Professional | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTP_TC_PASSWORD` |
| Client N | Plan Enterprise | TC-GS-HHR-399 | `Spectra.env.GS_CLIENTN_TC_PASSWORD` |
| Client D | Suspended, memiliki sedikitnya dua reader Available | TC-GS-HHR-402, TC-GS-HHR-400, TC-GS-HHR-227 | `Spectra.env.GS_CLIENTD_TC_PASSWORD` |
| Client X | Expired, memiliki sedikitnya satu reader | TC-GS-HHR-401 | `Spectra.env.GS_CLIENTX_TC_PASSWORD` |
| Client B | Plan Growth, toggle BYO nonaktif, belum ada reader | TC-GS-HHR-391 | `Spectra.env.GS_CLIENTB_TC_PASSWORD` |

- Nama env var Client S, P, N, D, X, dan B baru dan belum terdaftar di `spectra.config.ts` dan `.env.example`; diusulkan ke owner (satu arti per nama). Password tidak ditulis di spec atau fixture. Login Client A dilakukan di hook `before`; ganti akun ke client lain dilakukan di langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite (Client A).
- Data: Client A dengan Seed Reader A (DD-07 Available, Jalur B, `SN-HHR-00108`); stok `SN-HHR-00302` (Jalur B, tidak ada di stok Principal), katalog Device Name Client A dan Client B memuat DN-01 s.d. DN-07 (dibaca Client read-only). Data Dinamis: Alias Name `Reader Dock 07-{runId}-070` (Client A, DD-07), `Reader Dock 01-{runId}-070` (Client D, ditolak server).
- Kemampuan teknis (disediakan tim FE/BE):
  - Sesi API Principal untuk mematikan dan menyalakan toggle `Allow Self-Purchased Device Activation` (Client A dan Client B). Pelaku hanya memicu perubahan state, hasilnya tidak diasersi di sesi Principal (P-2 konvensi bagian 3); endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini.
  - Simulator reader USB/driver lokal untuk Sync `SN-HHR-00302` (mekanisme tidak didefinisikan di TC, PRD, atau LLD; lihat Temuan untuk QA).
  - Pembaca file unduhan CSV untuk mengonfirmasi Download berhasil (blok TC-GS-HHR-402).
  - Pemulihan Seed Reader A, reader Client B yang dibuat TC-GS-HHR-391, dan kedua toggle BYO ke keadaan Tabel Data Uji TC.
- State global yang diubah: toggle BYO Client A (dimatikan lalu dinyalakan kembali dengan langkah eksplisit) dan Client B (dinyalakan, lalu dikembalikan nonaktif di hook `after`), alias DD-07, reader baru Client B. Pemulihan: hook `after` sebagai cadangan.
- Baseline: jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log dicatat sebelum aksi Bulk Mark as (TC-GS-HHR-227).

## Test Steps

### Plan gating Client A, S, P, N: TC-GS-HHR-399

Untuk setiap baris tabel "Client plan" (langkah 1 sampai 8):

| Iterasi | Client | Plan | Ganti akun (langkah 1) |
|---|---|---|---|
| 1 | Client A | Growth | dilewati (sesi hook `before`) |
| 2 | Client S | Starter | login Total Control Client S |
| 3 | Client P | Professional | login Total Control Client P |
| 4 | Client N | Enterprise | login Total Control Client N |

1. Ganti akun: untuk Client S, P, dan N logout lalu login sebagai Total Control client tersebut; untuk Client A lewati langkah ini (sesi dari hook `before`)
2. Buka Global Settings > Hardware > Handheld Reader
3. Verifikasi tombol `[+ Activate Reader]` tampil dan aktif
4. Verifikasi tombol `[+ Activate Reader]` tidak memakai ikon 🔒 dan tidak memunculkan tooltip upgrade
5. Klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`
6. Verifikasi Popup Activate terbuka
7. Klik `✕` untuk menutup Popup Activate
8. Verifikasi row action reader dan ikon Changelog tersedia, dan kartu kuota tampil

9. Verifikasi tampilan halaman pada keempat plan identik (hasil `Verifikasi` langkah 3 sampai 8 sama pada tiap client)

### Client D Suspended: aksi baca lalu aksi tulis ditolak: TC-GS-HHR-402, TC-GS-HHR-400, TC-GS-HHR-227

10. Ganti akun: logout lalu login sebagai Total Control Client D
11. Buka Global Settings > Hardware > Handheld Reader
12. Verifikasi daftar reader Client D tampil tanpa penolakan
13. Klik `Device Name` salah satu reader untuk membuka Popup Detail
14. Verifikasi Popup Detail terbuka dengan Tab Usage dan Tab Changelog tanpa penolakan
15. Tutup Popup Detail, klik ikon Changelog
16. Verifikasi Modal Changelog terbuka tanpa penolakan
17. Tutup Modal Changelog, klik ikon Download, pilih CSV
18. Verifikasi berkas CSV terunduh tanpa penolakan
19. Buka Overlay row action satu reader, klik `Edit Alias Name`, catat `Alias Name` reader tersebut sebagai nilai awal
20. Isi `Alias Name` dengan `Reader Dock 01-{runId}-070`, klik `[Save]`
21. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
22. Verifikasi UI di-refresh dan `Alias Name` reader sama dengan nilai awal
23. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log sebagai baseline
24. Centang checkbox dua reader Available
25. Klik tombol `Bulk Action`
26. Klik `Mark as Damaged`
27. Klik `[Mark as Damaged]` pada dialog
28. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
29. Verifikasi `Status` kedua reader tidak berubah (tetap Available)
30. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log
31. Verifikasi jumlah entri pada Changelog Handheld Reader, System Log aktor, dan Activity Log sama dengan baseline (tidak bertambah)

### Client X Expired: Delete ditolak: TC-GS-HHR-401

32. Ganti akun: logout lalu login sebagai Total Control Client X
33. Buka Global Settings > Hardware > Handheld Reader, catat jumlah reader di tabel
34. Buka Overlay row action satu reader, klik `Delete`
35. Klik `[Delete]` pada dialog
36. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
37. Verifikasi reader tetap ada di tabel (jumlah reader sama dengan yang dicatat)

### Toggle BYO: TC-GS-HHR-391 (Client B), TC-GS-HHR-390 (Client A)

38. Nyalakan toggle `Allow Self-Purchased Device Activation` untuk Client B lewat sesi API Principal hingga tersimpan
39. Tunggu aksi selesai
40. Ganti akun: logout lalu login sebagai Total Control Client B
41. Buka Global Settings > Hardware > Handheld Reader
42. Klik `[+ Activate Reader]`, klik `Long Range` pada Overlay `Select Range Type`
43. Klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
44. Pilih `Chainway C72` pada `Device Name`, isi `Brand` `Chainway`, isi `Model/Type` `C72`, klik `[Submit]`
45. Verifikasi aktivasi berhasil: baris `Chainway C72 - 1` dengan `Source` `Self-Purchased` dan `Status` `Available`
46. Ganti akun: logout lalu login sebagai Total Control Client A (Sari Dewi)
47. Buka Global Settings > Hardware > Handheld Reader, catat jumlah reader di tabel
48. Matikan toggle `Allow Self-Purchased Device Activation` untuk Client A lewat sesi API Principal hingga tersimpan
49. Tunggu aksi selesai
50. Muat ulang Handheld Reader
51. Buka Overlay row action DD-07, klik `Edit Alias Name`
52. Isi `Alias Name` dengan `Reader Dock 07-{runId}-070`, klik `[Save]`
53. Verifikasi Edit Alias DD-07 berhasil: `Alias Name` DD-07 menampilkan `Reader Dock 07-{runId}-070`
54. Klik `[+ Activate Reader]`, pilih `Long Range` pada Overlay `Select Range Type`, klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
55. Verifikasi Sync `SN-HHR-00302` ditolak dengan state `Ditolak server` berpesan `Self-purchased device activation is not enabled for your account.`
56. Klik `✕` untuk menutup Popup Activate
57. Verifikasi tidak ada record dibuat (jumlah reader di tabel sama dengan yang dicatat)
58. Nyalakan kembali toggle `Allow Self-Purchased Device Activation` untuk Client A lewat sesi API Principal hingga tersimpan

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 3 untuk TC-GS-HHR-227, Section 7c, 7e). Label Manual Only (b) ada pada TC-GS-HHR-390 dan TC-GS-HHR-391 (reader USB fisik); kebutuhannya ditulis di Prerequisites.
- Urutan: aksi baca/plan (tanpa efek tulis) di awal; kasus tolak server (Client D, X) tidak mengubah data; blok toggle BYO paling akhir karena mengubah state global (prinsip 3 butir 2, 3, 5). Spec ini memakai satu alur per kelas h; dua langkah USB (TC-GS-HHR-390 dan TC-GS-HHR-391) adalah pemicu state yang diuji oleh toggle, bukan objek uji harness.
- Langkah 1 sampai 8 diulang untuk empat client (bagian 8b butir 7); langkah 9 membandingkan hasil keempatnya.
- Spec melewati sekitar 35 langkah dengan ekspansi. Alasan: seluruh blok memverifikasi satu topik (state tenant) dan berdiri sendiri; tiap blok memakai client sendiri dan ganti akun eksplisit, sehingga bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (prinsip 3, pemisah "beda akun" pengecualian b).
- Langkah penghubung tanpa `Verifikasi` (S-03): ganti akun, buka halaman, tutup popup/modal, mencatat nilai awal dan baseline, muat ulang, mengubah toggle lewat sesi API. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi.
- Temuan untuk QA:
  - TC-GS-HHR-399 tidak menyebut data reader Client S, P, dan N, padahal expected menyebut row action, Changelog, dan kartu; spec mengasumsikan ketiga client memiliki sedikitnya satu reader.
  - TC-GS-HHR-399 butir a menyebut "Popup Activate terbuka" setelah klik `[+ Activate Reader]`, sedangkan alur Activate melewati Overlay `Select Range Type`; spec memilih `Long Range` agar Popup Activate terbuka.
  - TC-GS-HHR-399 butir "tampilan identik" tidak menyebut cara membandingkan antar plan; spec membandingkan hasil `Verifikasi` tiap client.
  - TC-GS-HHR-390 tidak menyebut apakah dialog `Cancel Activation` tampil saat Popup Activate ditutup sesudah Sync ditolak; spec menutup dengan `✕` saja.
  - TC-GS-HHR-390 butir a ("Edit Alias DD-07 berhasil") tidak menyebut toast; spec mengasersi `Alias Name` DD-07 pada baris.
  - TC-GS-HHR-391 precondition e menyebut katalog Device Name Client A, padahal aktornya Client B; spec mengasumsikan katalog yang sama tersedia di Client B.
  - TC-GS-HHR-402 tidak menyebut tab Popup Detail yang diamati dan cara membuktikan "berfungsi tanpa penolakan"; spec memakai tampilnya Tab Usage dan Tab Changelog dan berkas terunduh.
  - Mekanisme simulasi reader USB (Sync `SN-HHR-00302`) dan cara Principal mengubah toggle BYO tidak didefinisikan di TC, PRD, atau LLD; tidak ada endpoint yang dikarang.
  - Email dan nilai `{namaClient}` untuk akun Total Control Client S, P, N, D, X, dan B tidak tertulis di Pre-setup TC.
