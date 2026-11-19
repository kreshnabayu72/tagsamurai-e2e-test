---
id: TC-FA-ASTL-E2E-016-add-label-bulk
title: "Bulk Add Label tersimpan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-04c", "§9.7#r11", "EB-FRM-1@add-label", "EB-FB-1@add-label"]
smoke: ["EB-FB-1@add-label"]
dependsOn: []
trace:
  "ASTL-LOGIC-04c": [10, 21]
  "§9.7#r11": [2, 14, 15, 17, 23]
  "EB-FRM-1@add-label": [13, 17]
  "EB-FB-1@add-label": 13
anchor: []
coverage:
  web: automated
---
# Bulk Add Label tersimpan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Data:
  - DU-016-1: aset Active, Asset Name `Printer Warna {runId}`, tampil `Printer Warna {runId} - 1`, Brand `Epson`, Model/Type `L3250`, Category `Peralatan Kantor`, Group `Kantor Pusat {runId}`, Status `Available`, Label manual `Gedung A {runId}`.
  - DU-016-2: aset Active, Asset Name `Scanner Dokumen {runId}`, tampil `Scanner Dokumen {runId} - 1`, Brand `Canon`, Model/Type `DR-C225`, Category `Peralatan Kantor`, Group `Kantor Pusat {runId}`, Status `Available`, tanpa label.
  - DU-016-3: katalog label manual `Gedung A {runId}` dan `Aset Kritis {runId}`.
  - DU-016-4: Group `Kantor Pusat {runId}`.
  - Sesi pengamat: sesi browser kedua dengan aktor Total Control membuka All Assets dengan Search yang memuat DU-016-1 dan DU-016-2 sebelum langkah 1, dan tidak dimuat ulang sesudahnya.

## Test Steps

### Katalog label ditawarkan penuh
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `Printer Warna {runId} - 1` memuat label `Gedung A {runId}`
3. Klik ikon `Changelog` pada toolbar
4. Catat entri Changelog teratas
5. Tutup modal Changelog
6. Centang baris `Printer Warna {runId} - 1` dan baris `Scanner Dokumen {runId} - 1`
7. Klik `Bulk Action`
8. Pilih `Add Label`
9. Klik field `Select label`
10. Verifikasi opsi `Gedung A {runId}` dan `Aset Kritis {runId}` tersedia, termasuk label yang sudah dimiliki `Printer Warna {runId} - 1`

### Add Label tersimpan dan tercatat
11. Pilih `Aset Kritis {runId}` dan `Gedung A {runId}`
12. Klik `[Apply]`
13. Verifikasi toast `Success, label has been added.` tampil
14. Verifikasi baris `Scanner Dokumen {runId} - 1` memuat label `Aset Kritis {runId}` dan `Gedung A {runId}`
15. Verifikasi baris `Printer Warna {runId} - 1` memuat label `Gedung A {runId}` satu kali dan label `Aset Kritis {runId}`
16. Klik ikon `Changelog` pada toolbar
17. Verifikasi Changelog memuat tepat satu entri baru `Add Label` untuk `Printer Warna {runId} - 1` dan tepat satu entri baru `Add Label` untuk `Scanner Dokumen {runId} - 1`

### Label yang dimiliki seluruh aset terpilih tetap ditawarkan
18. Klik `Bulk Action`
19. Pilih `Add Label`
20. Klik field `Select label`
21. Verifikasi opsi `Gedung A {runId}` dan `Aset Kritis {runId}` tetap tersedia walaupun keduanya kini dimiliki kedua aset terpilih
22. Klik `[Cancel]`

### Sesi lain melihat label berubah tanpa muat ulang
23. Verifikasi pada sesi pengamat, tanpa memuat ulang halaman, baris `Scanner Dokumen {runId} - 1` memuat label `Aset Kritis {runId}` dan `Gedung A {runId}`, dan baris `Printer Warna {runId} - 1` memuat label `Aset Kritis {runId}`
