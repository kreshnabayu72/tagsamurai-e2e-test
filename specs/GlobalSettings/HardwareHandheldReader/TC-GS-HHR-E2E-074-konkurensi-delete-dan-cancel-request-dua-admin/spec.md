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
| Principal (API) | Principal, hanya memicu keputusan Approve atau Reject | Bambang Hartono | `principal_automated_qaTeam1@qwertysystem.net` | Sesi API (`Spectra.env.GS_PRINCIPAL_TC_PASSWORD`) |
| Admin B (API) | Admin kedua Total Control Client A, hanya memicu perubahan state | Disediakan tim FE | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | Sesi API |

- Login Sesi A dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader. Principal dan Admin B memakai sesi API karena hanya memicu perubahan state dan hasil di sesi itu tidak diasersi (P-2 konvensi bagian 3); langkah pemicunya ditulis "hingga ... tersimpan". Hook `after` mengembalikan sesi ke akun default suite (Sesi A).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE): DD-01 (`Zebra RFID Reader - 1`, Available), DD-05 (`Chainway C72 - 1`, `Waiting for Approval`, permintaan collision di Admin Console > Approvals untuk `SN-HHR-00105`).
- Kemampuan teknis (disediakan tim FE/BE): sesi API Principal (Approve dan Reject permintaan DD-05), sesi API Admin B (Delete DD-01 dan konfirmasi Cancel Request DD-05); endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini; pemulihan Seed Reader A dan permintaan Approvals DD-05 antar blok (fixture BE; Catatan TC: tabel dipulihkan antar TC).
- Baseline: jumlah entri Changelog Handheld Reader, System Log aktor (Sari Dewi), dan Activity Log dicatat sesudah aksi pemicu dan sebelum klik konfirmasi Sesi A, karena aksi pemicu sendiri menambah entri (S-12).
- State global yang diubah: Seed Reader A (DD-01 dan DD-05) dan permintaan Approvals DD-05. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Cancel Request setelah Principal Approve: TC-GS-HHR-432

1. Pulihkan Seed Reader A dan permintaan Approvals DD-05
2. Muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request` (dialog tetap terbuka)
3. Principal: Approve permintaan DD-05 lewat sesi API hingga tersimpan
4. Tunggu aksi selesai
5. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log sebagai baseline
6. Klik `[Cancel Request]` pada dialog
7. Verifikasi muncul toast netral `This request is no longer available.`
8. Verifikasi daftar dimuat ulang dan DD-05 berstatus `Available`
9. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log
10. Verifikasi jumlah entri pada Changelog Handheld Reader, System Log aktor, dan Activity Log sama dengan baseline (tidak bertambah dari sesi A)

### Cancel Request setelah Principal Reject (menghapus data): TC-GS-HHR-433

11. Pulihkan Seed Reader A dan permintaan Approvals DD-05
12. Muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request` (dialog tetap terbuka)
13. Principal: Reject permintaan DD-05 lewat sesi API hingga tersimpan
14. Tunggu aksi selesai
15. Klik `[Cancel Request]` pada dialog
16. Verifikasi muncul toast netral `This request is no longer available.`
17. Verifikasi tidak ada efek tambahan: baris DD-05 tidak ada di daftar dan jumlah baris daftar sama dengan sebelum klik (anchor: toast hasil server)

### Cancel Request pada permintaan yang sudah dibatalkan admin lain (menghapus data): TC-GS-HHR-475

18. Pulihkan Seed Reader A dan permintaan Approvals DD-05
19. Muat ulang Handheld Reader, buka Overlay row action DD-05, klik `Cancel Request` (dialog tetap terbuka)
20. Admin B: konfirmasi Cancel Request DD-05 lewat sesi API hingga tersimpan
21. Tunggu aksi selesai
22. Klik `[Cancel Request]` pada dialog
23. Verifikasi muncul toast netral `This device is no longer available.`
24. Verifikasi daftar dimuat ulang dan baris DD-05 tidak ada (anchor: toast hasil server)
25. Verifikasi tidak ada efek tambahan: jumlah baris daftar sama dengan sebelum klik

### Delete reader yang sudah dihapus admin lain (menghapus data, paling akhir): TC-GS-HHR-429

26. Pulihkan Seed Reader A
27. Muat ulang Handheld Reader, buka Overlay row action DD-01, klik `Delete` (dialog tetap terbuka)
28. Admin B: Delete DD-01 lewat sesi API hingga tersimpan
29. Tunggu aksi selesai
30. Catat jumlah entri Changelog Handheld Reader, System Log aktor, dan Activity Log sebagai baseline
31. Klik `[Delete]` pada dialog
32. Verifikasi muncul toast netral `This device is no longer available.`
33. Buka kembali Changelog Handheld Reader, System Log aktor, dan Activity Log
34. Verifikasi tidak ada efek tambahan dan jumlah entri pada Changelog Handheld Reader, System Log aktor, dan Activity Log sama dengan baseline (tidak bertambah oleh aksi kedua)

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 9). Semua TC berlabel Manual Only (d): butuh dua sesi atau pengguna paralel; kebutuhannya ditulis di Prerequisites.
- Urutan: Approve (mempertahankan DD-05) lebih dulu, lalu Reject dan Cancel (menghapus DD-05), Delete DD-01 paling akhir (prinsip 3 butir 5). Seed Reader A dan permintaan Approvals dipulihkan di awal tiap blok (langkah 1, 11, 18, 26).
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan, muat ulang, membuka dialog, mencatat baseline. Langkah "Tunggu aksi selesai" dipakai karena aksi sesi API diikuti pengamatan di Sesi A.
- Temuan untuk QA:
  - TC-GS-HHR-429, 432, 433, dan 475 tidak menyebut akun Admin kedua; Admin B memakai sesi API yang disediakan tim FE, tanpa akun atau endpoint karangan.
  - TC-GS-HHR-433 butir ("tidak ada efek tambahan") tidak menyebut apa yang dibandingkan dan tidak punya langkah baseline; spec membandingkan jumlah baris daftar sebelum dan sesudah klik.
  - TC-GS-HHR-475 butir b ("tidak ada efek tambahan") demikian pula tidak menyebut pembanding; spec memakai jumlah baris daftar.
  - TC-GS-HHR-432 menyatakan nama tombol dialog sebagai `[Cancel Request]` dan kondisi "Principal sudah Approve" sebagai precondition; spec menaruh Approve sesudah dialog dibuka sesuai pernyataan "setelah sesi pertama membuka dialog" (S-04).
  - TC-GS-HHR-429 dan 432 membandingkan jumlah entri "dengan sebelum aksi" padahal aksi pemicu menambah entri; baseline dicatat sesudah aksi pemicu dan sebelum klik sesi A.
