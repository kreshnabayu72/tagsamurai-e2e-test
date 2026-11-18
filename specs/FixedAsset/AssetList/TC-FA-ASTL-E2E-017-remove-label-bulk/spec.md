---
id: TC-FA-ASTL-E2E-017-remove-label-bulk
title: "Bulk Remove Label tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-04d", "ASTL-LOGIC-04f", "ASTL-LOGIC-04h", "EC-04", "EB-FRM-1@remove-label", "EB-FB-1@remove-label"]
smoke: ["EB-FB-1@remove-label"]
dependsOn: []
trace:
  "ASTL-LOGIC-04d": 17
  "ASTL-LOGIC-04f": [7, 8, 23]
  "ASTL-LOGIC-04h": [18, 22, 23]
  "EC-04": 8
  "EB-FRM-1@remove-label": [21, 25]
  "EB-FB-1@remove-label": 21
anchor: [2]
coverage:
  web: automated
---
# Bulk Remove Label tersimpan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-017-1: aset Active, Asset Name `Monitor Dell {runId}`, tampil `Monitor Dell {runId} - 1`, Brand `Dell`, Model/Type `P2422H`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`, label manual `Aset Kritis {runId}` dan label bawaan template Asset Name `Wajib Audit {runId}`.
  - DU-017-2: aset Active, Asset Name `Keyboard Logitech {runId}`, tampil `Keyboard Logitech {runId} - 1`, Brand `Logitech`, Model/Type `K380`, Category `Peralatan IT`, Group `Kantor Pusat {runId}`, Status `Available`, label manual `Gedung A {runId}` dan label manual `Wajib Audit {runId}`.
  - DU-017-3: Group `Kantor Pusat {runId}`.

## Test Steps

### Label bawaan tidak ditawarkan
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Monitor Dell {runId} - 1` memuat label `Aset Kritis {runId}` dan `Wajib Audit {runId}`
3. Centang baris `Monitor Dell {runId} - 1`
4. Klik `Bulk Action`
5. Pilih `Remove Label`
6. Klik field `Select label`
7. Verifikasi opsi `Aset Kritis {runId}` tersedia
8. Verifikasi opsi `Wajib Audit {runId}` tidak tersedia karena label bawaan
9. Klik `[Cancel]`

### Union label manual dan pencabutan label bawaan sebagian
10. Centang baris `Keyboard Logitech {runId} - 1`
11. Klik ikon `Changelog` pada toolbar
12. Catat entri Changelog teratas
13. Tutup modal Changelog
14. Klik `Bulk Action`
15. Pilih `Remove Label`
16. Klik field `Select label`
17. Verifikasi opsi `Aset Kritis {runId}` dan `Gedung A {runId}` tersedia, masing-masing hanya dimiliki satu aset terpilih
18. Verifikasi opsi `Wajib Audit {runId}` tersedia karena manual pada `Keyboard Logitech {runId} - 1`
19. Pilih `Wajib Audit {runId}` dan `Gedung A {runId}`
20. Klik `[Apply]`
21. Verifikasi toast `Success, label has been removed.` tampil

### Hasil pencabutan terbaca ulang
22. Verifikasi baris `Keyboard Logitech {runId} - 1` tidak lagi memuat label `Wajib Audit {runId}` maupun `Gedung A {runId}`
23. Verifikasi baris `Monitor Dell {runId} - 1` tetap memuat label bawaan `Wajib Audit {runId}` dan label `Aset Kritis {runId}`
24. Klik ikon `Changelog` pada toolbar
25. Verifikasi Changelog memuat tepat satu entri baru `Remove Label` untuk `Keyboard Logitech {runId} - 1`
