---
id: TC-GS-HHR-E2E-074-konkurensi-delete-dan-cancel-request-dua-admin
title: "Konkurensi: Cancel Request Setelah Principal Memutuskan atau Admin Lain Membatalkan, dan Delete Reader yang Sudah Dihapus"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-429
  - TC-GS-HHR-432
  - TC-GS-HHR-433
  - TC-GS-HHR-475
coverage:
  web: automated
---

# Konkurensi: Cancel Request Setelah Principal Memutuskan atau Admin Lain Membatalkan, dan Delete Reader yang Sudah Dihapus

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, dua admin atau Principal memutuskan sementara dialog Client terbuka). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Peran | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Principal (API) | Principal, hanya memicu keputusan Approve atau Reject | Bambang Hartono | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | Sesi API (`Spectra.env.GS_PRINCIPAL_TC_PASSWORD`) |
| Admin B (API) | Admin B, Total Control Client A, hanya memicu perubahan state | Nadia Pratama | `totalControlSecond_automated_qaTeam1@qwertysystem.net` | Sesi API (`Spectra.env.GS_TC2_PASSWORD`) |

- Login Sesi A dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader. Principal dan Admin B memakai sesi API karena hanya memicu perubahan state dan hasil di sesi itu tidak diasersi; langkah pemicunya ditulis "hingga ... tersimpan". Hook `after` mengembalikan sesi ke akun default suite (Sesi A).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE): DD-01 (`Zebra RFID Reader - 1`, Available), DD-05 (`Chainway C72 - 1`, `Waiting for Approval`, permintaan collision di Admin Console > Approvals untuk `SN-HHR-00105`).
- Kemampuan teknis (disediakan tim FE/BE): sesi API Principal (Approve dan Reject permintaan DD-05), sesi API Admin B (Delete DD-01 dan konfirmasi Cancel Request DD-05); endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini; pemulihan Seed Reader A dan permintaan Approvals DD-05 antar blok (fixture BE; Catatan TC: tabel dipulihkan antar TC).
- Baseline: jumlah entri Changelog Handheld Reader, System Log aktor (Sari Dewi), dan Activity Log (Global Settings > Activity Log > tab `User Action`) dicatat sesudah aksi pemicu dan sebelum klik konfirmasi Sesi A (TC-GS-HHR-429, 432, 433, dan 475), karena aksi pemicu sendiri menambah entri (S-12); sesudah toast, ketiga surface dibuka kembali dan jumlahnya dibandingkan dengan baseline.
- State global yang diubah: Seed Reader A (DD-01 dan DD-05) dan permintaan Approvals DD-05. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Cancel Request setelah Principal Approve: TC-GS-HHR-432

1. Pulihkan Seed Reader A dan permintaan Approvals DD-05
2. Muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request` (dialog tetap terbuka)
3. Principal: Approve permintaan DD-05 lewat sesi API hingga tersimpan
4. Tunggu aksi selesai
5. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`) sebagai baseline
6. Klik `[Cancel Request]` pada dialog
7. Verifikasi muncul toast netral `This request is no longer available.`
8. Verifikasi daftar dimuat ulang
9. Verifikasi DD-05 berstatus `Available`
10. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`)
11. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline (tidak bertambah dari sesi A)
12. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak bertambah dari sesi A)
13. Verifikasi jumlah entri Activity Log (tab `User Action`) sama dengan baseline (tidak bertambah dari sesi A)

### Cancel Request setelah Principal Reject (menghapus data): TC-GS-HHR-433

14. Pulihkan Seed Reader A dan permintaan Approvals DD-05
15. Muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request` (dialog tetap terbuka)
16. Principal: Reject permintaan DD-05 lewat sesi API hingga tersimpan
17. Tunggu aksi selesai
18. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`) sebagai baseline
19. Klik `[Cancel Request]` pada dialog
20. Verifikasi muncul toast netral `This request is no longer available.`
21. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`)
22. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline (tidak bertambah dari sesi A; tidak ada efek tambahan)
23. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak bertambah dari sesi A; tidak ada efek tambahan)
24. Verifikasi jumlah entri Activity Log (tab `User Action`) sama dengan baseline (tidak bertambah dari sesi A; tidak ada efek tambahan)

### Cancel Request pada permintaan yang sudah dibatalkan admin lain (menghapus data): TC-GS-HHR-475

25. Pulihkan Seed Reader A dan permintaan Approvals DD-05
26. Muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request` (dialog tetap terbuka)
27. Admin B: konfirmasi Cancel Request DD-05 lewat sesi API hingga tersimpan
28. Tunggu aksi selesai
29. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`) sebagai baseline
30. Klik `[Cancel Request]` pada dialog
31. Verifikasi muncul toast netral `This device is no longer available.`
32. Verifikasi daftar dimuat ulang
33. Verifikasi baris DD-05 tidak ada (anchor: toast hasil server)
34. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`)
35. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline (tidak bertambah dari klik sesi A; tidak ada efek tambahan)
36. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak bertambah dari klik sesi A; tidak ada efek tambahan)
37. Verifikasi jumlah entri Activity Log (tab `User Action`) sama dengan baseline (tidak bertambah dari klik sesi A; tidak ada efek tambahan)

### Delete reader yang sudah dihapus admin lain (menghapus data, paling akhir): TC-GS-HHR-429

38. Pulihkan Seed Reader A
39. Muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Delete` (dialog tetap terbuka)
40. Admin B: Delete DD-01 lewat sesi API hingga tersimpan
41. Tunggu aksi selesai
42. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`) sebagai baseline
43. Klik `[Delete]` pada dialog
44. Verifikasi muncul toast netral `This device is no longer available.`
45. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log (Global Settings > Activity Log > tab `User Action`)
46. Verifikasi jumlah entri Changelog Handheld Reader sama dengan baseline (tidak bertambah oleh aksi kedua)
47. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak bertambah oleh aksi kedua)
48. Verifikasi jumlah entri Activity Log (tab `User Action`) sama dengan baseline (tidak bertambah oleh aksi kedua)

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 9). Semua TC berlabel Manual Only (d): butuh dua sesi atau pengguna paralel; kebutuhannya ditulis di Prerequisites.
- Urutan: Approve (mempertahankan DD-05) lebih dulu, lalu Reject dan Cancel (menghapus DD-05), Delete DD-01 paling akhir (prinsip 3 butir 5). Seed Reader A dan permintaan Approvals dipulihkan di awal tiap blok (langkah 1, 14, 25, 38).
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas harness (multi-konteks dua admin) dan berdiri sendiri; tiap blok memulihkan data di awal dan tidak bergantung pada hasil blok lain.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan, muat ulang, membuka dialog, mencatat baseline. Langkah "Tunggu aksi selesai" dipakai karena aksi sesi API diikuti pengamatan di Sesi A.
- Temuan untuk QA:
  - TC-GS-HHR-432 menyatakan nama tombol dialog sebagai `[Cancel Request]` dan kondisi "Principal sudah Approve" sebagai precondition; spec menaruh Approve sesudah dialog dibuka sesuai pernyataan "setelah sesi pertama membuka dialog" (S-04).
  - TC-GS-HHR-429 dan 432 membandingkan jumlah entri "dengan sebelum aksi" padahal aksi pemicu menambah entri; baseline dicatat sesudah aksi pemicu dan sebelum klik sesi A.
