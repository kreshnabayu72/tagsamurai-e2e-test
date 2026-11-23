---
id: TC-FA-FAFM-E2E-021-delete-file-bulk
title: "Bulk Delete beberapa file dari tab Files"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-04c, ACT-04d, D-02, EC-03, S-20, T-02, TBL-05a, "§4.1a#p5"]
smoke: []
dependsOn: []
trace:
  ACT-04c: [35, 38]
  ACT-04d: 34
  D-02: [14, 15, 16, 17]
  EC-03: [38, 39, 40]
  S-20: 34
  T-02: 34
  TBL-05a: 12
  "§4.1a#p5": [34, 38]
anchor: [3, 19, 23]
coverage:
  web: automated
  android: automated
---

# Bulk Delete beberapa file dari tab Files

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-021-1: Aset `Toyota Avanza {runId}`, Group `Fleet`.
  - DU-021-2: Empat file Source `Damaged Photo`, Kategori `Damaged`, Asset `Toyota Avanza {runId}`, Group `Fleet`, Size `150.0 KB`, bernama `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` untuk n dari 1 sampai 4.
  - DU-021-3: Empat file Source `Repair Photo`, Kategori `Damaged`, Asset `Toyota Avanza {runId}`, Group `Fleet`, Size `120.0 KB`, bernama `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` untuk n dari 1 sampai 4.
  - Seluruh delapan file ada di tab `Damaged`.

## Test Steps

### Cancel pada dialog bulk Delete tidak menghapus file
1. Klik tab `Damaged`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi delapan file `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` dan `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` untuk n dari 1 sampai 4 tampil di tab `Damaged`
4. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-1-{runId}.jpg` untuk aksi bulk
5. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-2-{runId}.jpg` untuk aksi bulk
6. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-3-{runId}.jpg` untuk aksi bulk
7. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-4-{runId}.jpg` untuk aksi bulk
8. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-1-{runId}.jpg` untuk aksi bulk
9. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-2-{runId}.jpg` untuk aksi bulk
10. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-3-{runId}.jpg` untuk aksi bulk
11. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-4-{runId}.jpg` untuk aksi bulk
12. Verifikasi bar aksi bulk memuat aksi `Delete`
13. Klik `Delete` pada bar aksi bulk
14. Verifikasi dialog `Delete Files` memuat bullet nama untuk kedelapan file, yaitu `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` dan `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` untuk n dari 1 sampai 4
15. Verifikasi anotasi bullet keempat file `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` memuat Source `Damaged Photo`
16. Verifikasi anotasi bullet keempat file `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` memuat Source `Repair Photo`
17. Verifikasi anotasi bullet kedelapan file memuat nama aset `Toyota Avanza {runId}`
18. Tutup dialog konfirmasi dengan Cancel
19. Verifikasi kedelapan file masih tampil di tab `Damaged`

### Bulk Delete dikonfirmasi memproses semua file terpilih
20. Muat ulang halaman
21. Klik tab `Damaged`
22. Ganti isi kotak search dengan `{runId}`, tekan Enter
23. Verifikasi kedelapan file masih tampil di tab `Damaged`
24. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-1-{runId}.jpg` untuk aksi bulk
25. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-2-{runId}.jpg` untuk aksi bulk
26. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-3-{runId}.jpg` untuk aksi bulk
27. Pilih `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-4-{runId}.jpg` untuk aksi bulk
28. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-1-{runId}.jpg` untuk aksi bulk
29. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-2-{runId}.jpg` untuk aksi bulk
30. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-3-{runId}.jpg` untuk aksi bulk
31. Pilih `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-4-{runId}.jpg` untuk aksi bulk
32. Klik `Delete` pada bar aksi bulk
33. Klik `[Delete]` pada dialog `Delete Files`
34. Verifikasi toast `Success, file has been deleted.` tampil
35. Verifikasi tab `Damaged` tidak tampil satu pun file untuk Search `{runId}`

### Semua file terpilih masuk Recycle Bin
36. Klik `Recycle Bin` pada header kartu `Storage Usage`
37. Ketik Search `{runId}`, tekan Enter
38. Verifikasi kedelapan file `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` dan `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` untuk n dari 1 sampai 4 tampil di Recycle Bin
39. Verifikasi keempat file `foto-kerusakan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` memuat Source `Damaged Photo` di Recycle Bin
40. Verifikasi keempat file `foto-perbaikan-bumper-depan-kendaraan-operasional-cabang-surabaya-{n}-{runId}.jpg` memuat Source `Repair Photo` di Recycle Bin
41. Tutup modal `Recycle Bin`
