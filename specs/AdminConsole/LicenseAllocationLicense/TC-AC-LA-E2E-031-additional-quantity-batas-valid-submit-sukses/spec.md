---
id: TC-AC-LA-E2E-031-additional-quantity-batas-valid-submit-sukses
title: "Additional Quantity Batas Valid: Nilai 1 dan 15 Digit Submit Sukses"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-113
  - TC-AC-LA-509
coverage:
  web: automated
---

# Additional Quantity Batas Valid: Nilai 1 dan 15 Digit Submit Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, dan ID Subscription.
- Data Pre-setup: Client PT Sejahtera (#19, term `SUBS-20260101-A1B2C`); toggle Require Approval for Allocation OFF (#39), diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan ke keadaan awal di hook `after`.
- Data Dinamis: dua alokasi Concurrent User ke PT Sejahtera (Completed, Free): Quantity `1` dan Quantity `999999999999999` (Dinamis #5 TC). Alokasi tidak dapat dihapus (tanpa Delete); ledger kuota term `SUBS-20260101-A1B2C` dipulihkan oleh baseline automation dan fixture backend di hook `after`, wajib sebelum spec lain membaca Current Quota PT Sejahtera.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum tiap `[Submit]` (langkah 1 dan 9).
- Kemampuan teknis: mengisi 15 digit ke field Additional Quantity.
- State global: toggle Require Approval (lihat Data Pre-setup).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-113: Additional Quantity bernilai 1 lolos validasi batas bawah

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
4. Klik `[Submit]`
5. Verifikasi tidak ada pesan validasi pada Additional Quantity
6. Verifikasi toast sukses "Success, license has been allocated."
7. Verifikasi baris baru dengan Quantity `+1` tampil di tab Current (Allocation ID tidak ada pada baseline langkah 1)

### TC-AC-LA-509: Additional Quantity tepat 15 digit diterima untuk Principal tanpa batas saldo

8. Tunggu toast hilang otomatis
9. Catat baseline Allocation ID baris di halaman pertama tab Current
10. Klik `[+ Allocation]`
11. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `999999999999999`
12. Verifikasi tidak ada error `Max. 15 characters` pada Additional Quantity
13. Verifikasi tidak ada pesan validasi pada Additional Quantity
14. Verifikasi section Payment Method tidak dirender
15. Verifikasi tidak ada peringatan saldo
16. Klik `[Submit]`
17. Verifikasi toast sukses "Success, license has been allocated."
18. Verifikasi baris baru dengan Quantity `999999999999999` tanpa terpotong tampil di tab Current (Allocation ID tidak ada pada baseline langkah 9)
19. Verifikasi tidak ada toast galat server

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 2 kali, kejadian menutup 2 (modal tertutup oleh Submit sukses di langkah 4 dan 16).
- Langkah penghubung (S-03): langkah 1 dan 9 (baseline), langkah 8 (menunggu toast TC-AC-LA-113 hilang agar toast TC-AC-LA-509 dapat diasersi, R-12).
- Verifikasi langkah 13 dan 15 adalah klausa terpisah dari Expected a dan b TC-AC-LA-509 (S-01).
- Temuan untuk QA:
  - TC-AC-LA-113 menulis Quantity `+1`, sedangkan TC-AC-LA-509 Expected d menulis Quantity `999999999999999` tanpa tanda `+`; spec mengikuti masing-masing TC, perlu penegasan format Quantity pada baris Completed.
  - TC-AC-LA-509 Expected d ("tanpa galat server") tidak menyebut bentuk galat; spec mengasersi tidak ada toast galat (langkah 19).
  - Post Condition "Record Quantity +1 tercatat" (TC-AC-LA-113) dan "Record Quantity 15 digit tercatat" (TC-AC-LA-509) diwakili oleh baris baru pada langkah 7 dan 18; TC tidak memberi langkah observasi lain.
