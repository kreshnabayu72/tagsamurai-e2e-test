---
id: TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data
title: "Create Position sukses, trim whitespace, Stay on this form, 1 karakter, 120 karakter, dan refresh persistence"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-41
  - TC-GS-POS-51
  - TC-GS-POS-52
  - TC-GS-POS-53
  - TC-GS-POS-54
  - TC-GS-POS-73
  - TC-GS-POS-282
  - TC-GS-POS-286
coverage:
  web: automated
---

# Create Position sukses, trim whitespace, Stay on this form, 1 karakter, 120 karakter, dan refresh persistence

## Prerequisites

- Login sebagai Role: Total Control
- Buka tab Position

## Test Steps

### Create Single Position (Stay Tidak Dicentang)

1. Klik "[+ Position]"
2. Masukkan nama dengan spasi di awal dan akhir: "  Data Analyst  "
3. Pastikan checkbox "Stay on this form after submitting" tidak dicentang
4. Klik "[Submit]"
5. Verifikasi modal Create otomatis tertutup, toast sukses muncul, dan "Data Analyst" muncul di tabel dalam kondisi ter-trim (tanpa spasi depan/belakang)

### Input Berulang dengan "Stay on this form after submitting"

6. Klik "[+ Position]" lagi
7. Centang checkbox "[x] Stay on this form after submitting"
8. Masukkan nama batas 1 karakter "A" lalu klik "[Submit]"
9. Verifikasi toast sukses muncul, modal Create tetap terbuka, dan form ter-reset kosong
10. Masukkan nama batas tepat 120 karakter lalu klik "[Submit]"
11. Verifikasi toast sukses muncul dan form tetap terbuka dalam keadaan kosong
12. Masukkan berturut-turut nama populasi data: "iOS Developer", "Legal Counsel", "Marketing Executive" dengan menekan "[Submit]" pada masing-masing nama
13. Hapus centang "Stay on this form after submitting", masukkan nama "Quality Assurance Analyst", lalu klik "[Submit]"
14. Verifikasi modal tertutup dan seluruh record yang baru dibuat tampil di tabel Position
15. Tekan F5 (refresh browser) dan verifikasi seluruh data baru tetap persisten di database

## Notes

- Menggabungkan happy path, batas 1 dan 120 karakter, Stay on this form, trim whitespace, dan persistensi (TC-GS-POS-41, 51, 52, 53, 54, 73, 282, 286).
