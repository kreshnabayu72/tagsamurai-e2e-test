---
id: TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes
title: "Penutupan form Create via ✕, Esc, backdrop, in-app navigation, dan dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-55
  - TC-GS-POS-56
  - TC-GS-POS-57
  - TC-GS-POS-58
  - TC-GS-POS-59
  - TC-GS-POS-60
  - TC-GS-POS-61
  - TC-GS-POS-62
  - TC-GS-POS-63
  - TC-GS-POS-64
coverage:
  web: automated
---

# Penutupan form Create via ✕, Esc, backdrop, in-app navigation, dan dialog Unsaved Changes

## Prerequisites

- Login sebagai Role: Total Control
- Buka tab Position

## Test Steps

### Penutupan Modal Bersih (Clean)

1. Klik "[+ Position]" untuk membuka form Create
2. Tekan tombol `[✕]` di header modal tanpa mengisi data
3. Verifikasi modal Create langsung tertutup tanpa ada dialog konfirmasi
4. Buka kembali "[+ Position]" dan tekan tombol Esc pada keyboard
5. Verifikasi modal langsung tertutup

### Unsaved Changes Saat Form Dirty

6. Buka kembali "[+ Position]" dan ketik "Senior Architect" ke input Position Name
7. Klik tombol `[✕]` di header
8. Verifikasi dialog konfirmasi "You have unsaved changes. Are you sure you want to leave?" muncul dengan tombol "[Leave]" dan "[Cancel]"
9. Klik "[Cancel]" pada dialog
10. Verifikasi dialog konfirmasi tertutup, modal Create tetap terbuka, dan teks "Senior Architect" masih utuh
11. Tekan tombol Esc pada keyboard
12. Verifikasi dialog "You have unsaved changes" kembali muncul
13. Klik area backdrop di luar modal Create
14. Verifikasi klik backdrop tidak menutup modal dan tidak membuang data
15. Klik tombol "[Leave]" pada dialog konfirmasi
16. Verifikasi modal Create tertutup dan tidak ada record baru yang terbuat di tabel

## Notes

- Menggabungkan alur penutupan form bersih vs dirty dari TC-GS-POS-55 s.d. 64.
