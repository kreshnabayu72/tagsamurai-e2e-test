---
id: TC-FA-FAFM-E2E-026-permanently-delete-bulk
title: "Bulk Permanently Delete beberapa file dari Recycle Bin"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-06c, ACT-06d, D-04, F-FAFM-03d, S-22, T-07]
smoke: []
dependsOn: []
trace:
  ACT-06c: [31, 41, 42]
  ACT-06d: 30
  D-04: 13
  F-FAFM-03d: 31
  S-22: 30
  T-07: 30
anchor: [3, 15, 19, 35]
coverage:
  web: automated
  android: automated
---

# Bulk Permanently Delete beberapa file dari Recycle Bin

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-026-1: Aset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-026-2: Empat file di Recycle Bin, Source `Damaged Photo`, Size `150.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`, bernama `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` untuk n dari 1 sampai 4.
  - DU-026-3: Empat file di Recycle Bin, Source `Repair Photo`, Size `120.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`, bernama `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` untuk n dari 1 sampai 4.
  - DU-026-4: File pembanding di Recycle Bin `foto-sisa-kendaraan-cabang-medan-{runId}.jpg`, Source `Damaged Photo`, Size `100.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`, tidak dipilih pada aksi bulk.
  - DU-026-5: File di Recycle Bin `foto-perbaikan-satu-{runId}.jpg`, Source `Repair Photo`, Size `110.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`, yang tetap terpilih pada aksi bulk terakhir.
  - DU-026-6: File di Recycle Bin `foto-perbaikan-dua-{runId}.jpg`, Source `Repair Photo`, Size `115.0 KB`, Deleted By `System`, Asset `Toyota Avanza {runId}`, Group `Fleet`, yang pilihannya dibatalkan pada aksi bulk terakhir.

## Test Steps

### Cancel pada dialog bulk Permanently Delete tidak menghapus file
1. Buka Recycle Bin
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi kedelapan file `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` dan `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` untuk n dari 1 sampai 4 tampil di Recycle Bin
4. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-1-{runId}.jpg` untuk aksi bulk
5. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-2-{runId}.jpg` untuk aksi bulk
6. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-3-{runId}.jpg` untuk aksi bulk
7. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-4-{runId}.jpg` untuk aksi bulk
8. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-1-{runId}.jpg` untuk aksi bulk
9. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-2-{runId}.jpg` untuk aksi bulk
10. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-3-{runId}.jpg` untuk aksi bulk
11. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-4-{runId}.jpg` untuk aksi bulk
12. Klik `Permanently Delete` pada bar aksi bulk
13. Verifikasi dialog `Permanently Delete Files` memuat bullet nama untuk kedelapan file, yaitu `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` dan `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-{n}-{runId}.jpg` untuk n dari 1 sampai 4
14. Tutup dialog konfirmasi dengan Cancel
15. Verifikasi kedelapan file masih tampil di Recycle Bin

### Bulk Permanently Delete dikonfirmasi menghapus semua file terpilih
16. Muat ulang halaman
17. Buka Recycle Bin
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi file pembanding `foto-sisa-kendaraan-cabang-medan-{runId}.jpg` tampil di Recycle Bin
20. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-1-{runId}.jpg` untuk aksi bulk
21. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-2-{runId}.jpg` untuk aksi bulk
22. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-3-{runId}.jpg` untuk aksi bulk
23. Pilih `foto-kerusakan-bumper-belakang-kendaraan-operasional-cabang-medan-4-{runId}.jpg` untuk aksi bulk
24. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-1-{runId}.jpg` untuk aksi bulk
25. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-2-{runId}.jpg` untuk aksi bulk
26. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-3-{runId}.jpg` untuk aksi bulk
27. Pilih `foto-perbaikan-bumper-belakang-kendaraan-operasional-cabang-medan-4-{runId}.jpg` untuk aksi bulk
28. Klik `Permanently Delete` pada bar aksi bulk
29. Klik `[Permanently Delete]` pada dialog `Permanently Delete Files`
30. Verifikasi toast `Success, file has been permanently deleted.` tampil
31. Verifikasi kedelapan file terpilih tidak tampil lagi di Recycle Bin
32. Tutup modal `Recycle Bin`

### Hanya file yang tetap terpilih yang dihapus permanen
33. Buka Recycle Bin
34. Ketik Search `{runId}`, tekan Enter
35. Verifikasi file `foto-perbaikan-satu-{runId}.jpg` dan `foto-perbaikan-dua-{runId}.jpg` tampil di Recycle Bin
36. Pilih `foto-perbaikan-satu-{runId}.jpg` untuk aksi bulk
37. Pilih `foto-perbaikan-dua-{runId}.jpg` untuk aksi bulk
38. Batalkan pilihan `foto-perbaikan-dua-{runId}.jpg`
39. Klik `Permanently Delete` pada bar aksi bulk
40. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
41. Verifikasi file `foto-perbaikan-satu-{runId}.jpg` tidak tampil lagi di Recycle Bin
42. Verifikasi file `foto-perbaikan-dua-{runId}.jpg` masih tampil di Recycle Bin
43. Tutup modal `Recycle Bin`
