---
id: TC-GS-DIV-E2E-024-create-division-batch-stay-checked-population
title: "Pembuatan Divisi Berurutan dengan Checkbox Stay on this Form Checked (Batch Population 26 Divisi)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-30
  - TC-GS-DIV-66
coverage:
  web: automated
---

# Pembuatan Divisi Berurutan dengan Checkbox Stay on this Form Checked (Batch Population 26 Divisi)

## Prerequisites

- Login sebagai Role: Total Control
- Hanya 6 Division Pre-setup yang ada di entitas
- Data: 26 Division Population D-02 (Accounting s.d. Warehouse)
- User berada di Global Settings > User > Division
- Hanya 6 Division Pre-setup yang ada (belum ada Division Data Uji Dinamis); jalankan sebelum TC Create lain

## Test Steps

### Population: Create 26 Division berurutan dengan Stay on this form dicentang (TC-GS-DIV-30)

1. Klik `[+ Division]`
2. Centang checkbox `Stay on this form after submitting`
3. Untuk tiap pasangan Name dan Code pada Data Uji: isi Division Name, isi Code, klik `[Submit]`
4. Setelah Submit terakhir tutup modal lewat icon `[✕]`
5. Verifikasi Tiap Submit memunculkan toast sukses: `Success, division has been created.`
6. Verifikasi Modal tetap terbuka, Division Name dan Code ter-reset kosong, fokus kembali ke Division Name, checkbox tetap tercentang
7. Verifikasi Setelah modal ditutup tabel menampilkan 32 Division dengan halaman 1 berisi 10 baris dan total 4 halaman
8. Verifikasi Tombol `[Submit]` tidak memunculkan dialog Unsaved Changes saat form kosong

### Submit Create dengan Stay checked mereset form dan tetap terbuka (TC-GS-DIV-66)

9. Klik `[+ Division]`
10. Centang `Stay on this form after submitting`
11. Isi Division Name `Investor Relations` dan Code `INV`
12. Klik `[Submit]`
13. Verifikasi Muncul toast sukses: `Success, division has been created.`
14. Verifikasi Modal tetap terbuka, Division Name dan Code kosong
15. Verifikasi Fokus kembali ke Division Name dan checkbox tetap tercentang

## Notes

- Memvalidasi perilaku checkbox Stay on this form after submitting: tiap submit memunculkan toast sukses, form di-reset, fokus kembali ke Name, dan modal tetap terbuka hingga ditutup manual (PRD §4.2c, §4.4 FI-12).
- Sumber pemetaan test case granular: TC-GS-DIV-30, TC-GS-DIV-66.
