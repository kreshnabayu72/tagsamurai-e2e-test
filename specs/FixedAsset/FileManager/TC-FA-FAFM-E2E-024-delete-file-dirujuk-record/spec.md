---
id: TC-FA-FAFM-E2E-024-delete-file-dirujuk-record
title: "Delete file yang dirujuk record sumber tidak diblokir"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [ACT-02c, EC-02, FAFM-LOGIC-02a, FAFM-LOGIC-02b, "§9.4.3#b7", EB-EDG-3]
smoke: []
dependsOn: []
trace:
  ACT-02c: [4, 12, 20, 32, 36]
  EC-02: 27
  FAFM-LOGIC-02a: [4, 12, 20, 32, 42]
  FAFM-LOGIC-02b: [6, 14, 22, 34, 44]
  "§9.4.3#b7": [8, 16, 24, 46]
  EB-EDG-3: [8, 16, 24, 27, 46]
anchor: [3, 11, 19, 31, 39]
coverage:
  web: automated
---

# Delete file yang dirujuk record sumber tidak diblokir

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Data:
  - DU-024-1: Aset `Toyota Avanza {runId}`, Group `Fleet`, dengan record Damaged yang aktif dan mewajibkan Damaged Photo.
  - DU-024-2: File aktif `damage-bumper-{runId}.jpg`, Source `Damaged Photo`, Kategori `Damaged`, Size `400.0 KB`, Asset `Toyota Avanza {runId}`, Group `Fleet`, dirujuk field Damaged Photo pada record Damaged milik DU-024-1.
  - DU-024-3: Aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, dengan transaksi Borrow yang belum Return.
  - DU-024-4: File aktif `handover-borrow-{runId}.jpg`, Source `Handover Photo`, Kategori `Borrow`, Size `500.0 KB`, Asset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, dirujuk transaksi Borrow milik DU-024-3 yang belum Return.
  - DU-024-5: Aset `Printer HP M404 {runId}` berstatus `Disposed`, Group `Branch Bandung`.
  - DU-024-6: File aktif `dsp-auction-receipt-{runId}.pdf`, Source `Disposal Document`, Kategori `Disposal`, Size `600.0 KB`, Asset `Printer HP M404 {runId}`, Group `Branch Bandung`, dirujuk Disposal milik DU-024-5.
  - DU-024-7: Aset `Monitor LG 24 {runId}` berstatus Unmanaged, Group `Head Office`.
  - DU-024-8: File aktif `unmanaged-photo-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `250.0 KB`, Asset `Monitor LG 24 {runId}`, Group `Head Office`.
  - DU-024-9: Aset `Honda Vario {runId}`, Group `Fleet`, dengan record Damaged yang aktif dan mewajibkan Damaged Photo.
  - DU-024-10: File aktif `damage-spion-{runId}.jpg`, Source `Damaged Photo`, Kategori `Damaged`, Size `180.0 KB`, Asset `Honda Vario {runId}`, Group `Fleet`, dirujuk field Damaged Photo pada record Damaged milik DU-024-9.
  - DU-024-11: Aset `Suzuki Ertiga {runId}`, Group `Fleet`, dengan record Damaged yang aktif dan mewajibkan Damaged Photo.
  - DU-024-12: File aktif `damage-rem-{runId}.jpg`, Source `Damaged Photo`, Kategori `Damaged`, Size `220.0 KB`, Asset `Suzuki Ertiga {runId}`, Group `Fleet`, dirujuk field Damaged Photo pada record Damaged milik DU-024-11.

## Test Steps

### Delete file Damaged Photo yang dirujuk record Damaged
1. Klik tab `Damaged`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi file `damage-bumper-{runId}.jpg` tampil di tab `Damaged`
4. Verifikasi aksi `Delete` pada baris `damage-bumper-{runId}.jpg` tampil dan enabled
5. Klik `Delete` pada baris `damage-bumper-{runId}.jpg`
6. Verifikasi dialog konfirmasi `Delete File` tampil untuk file `damage-bumper-{runId}.jpg`
7. Klik `[Delete]` pada dialog `Delete File`
8. Verifikasi file `damage-bumper-{runId}.jpg` tidak tampil lagi di tab `Damaged`

### Delete file Handover Photo pada transaksi Borrow yang belum Return
9. Klik tab `Borrow`
10. Ketik Search `{runId}`, tekan Enter
11. Verifikasi file `handover-borrow-{runId}.jpg` tampil di tab `Borrow`
12. Verifikasi aksi `Delete` pada baris `handover-borrow-{runId}.jpg` tampil dan enabled
13. Klik `Delete` pada baris `handover-borrow-{runId}.jpg`
14. Verifikasi dialog konfirmasi `Delete File` tampil untuk file `handover-borrow-{runId}.jpg`
15. Klik `[Delete]` pada dialog `Delete File`
16. Verifikasi file `handover-borrow-{runId}.jpg` tidak tampil lagi di tab `Borrow`

### Delete file Disposal Document milik aset Disposed
17. Klik tab `Disposal`
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi file `dsp-auction-receipt-{runId}.pdf` tampil di tab `Disposal`
20. Verifikasi aksi `Delete` pada baris `dsp-auction-receipt-{runId}.pdf` tampil dan enabled
21. Klik `Delete` pada baris `dsp-auction-receipt-{runId}.pdf`
22. Verifikasi dialog konfirmasi `Delete File` tampil untuk file `dsp-auction-receipt-{runId}.pdf`
23. Klik `[Delete]` pada dialog `Delete File`
24. Verifikasi file `dsp-auction-receipt-{runId}.pdf` tidak tampil lagi di tab `Disposal`

### Ketiga file masuk Recycle Bin
25. Klik `Recycle Bin` pada header kartu `Storage Usage`
26. Ketik Search `{runId}`, tekan Enter
27. Verifikasi file `damage-bumper-{runId}.jpg`, `handover-borrow-{runId}.jpg`, dan `dsp-auction-receipt-{runId}.pdf` tampil di Recycle Bin
28. Tutup modal `Recycle Bin`

### Delete file milik aset Unmanaged
29. Klik tab `Asset Photo`
30. Ketik Search `{runId}`, tekan Enter
31. Verifikasi file `unmanaged-photo-{runId}.jpg` tampil di tab `Asset Photo`
32. Verifikasi aksi `Delete` pada baris `unmanaged-photo-{runId}.jpg` tampil dan enabled
33. Klik `Delete` pada baris `unmanaged-photo-{runId}.jpg`
34. Verifikasi dialog konfirmasi `Delete File` tampil untuk file `unmanaged-photo-{runId}.jpg`
35. Klik `[Delete]` pada dialog `Delete File`
36. Verifikasi file `unmanaged-photo-{runId}.jpg` tidak tampil lagi di tab `Asset Photo`

### Bulk Delete file Damaged Photo yang dirujuk record Damaged
37. Klik tab `Damaged`
38. Ketik Search `{runId}`, tekan Enter
39. Verifikasi file `damage-spion-{runId}.jpg` dan `damage-rem-{runId}.jpg` tampil di tab `Damaged`
40. Centang baris `damage-spion-{runId}.jpg`
41. Centang baris `damage-rem-{runId}.jpg`
42. Verifikasi aksi `Delete` pada bar aksi bulk tampil dan enabled
43. Klik `Delete` pada bar aksi bulk
44. Verifikasi dialog konfirmasi `Delete Files` tampil untuk file `damage-spion-{runId}.jpg` dan `damage-rem-{runId}.jpg`
45. Klik `[Delete]` pada dialog `Delete Files`
46. Verifikasi file `damage-spion-{runId}.jpg` dan `damage-rem-{runId}.jpg` tidak tampil lagi di tab `Damaged`
