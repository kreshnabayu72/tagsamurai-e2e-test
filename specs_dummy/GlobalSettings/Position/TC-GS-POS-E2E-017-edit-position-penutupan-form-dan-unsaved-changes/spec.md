---
id: TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes
title: "Penutupan form Edit via ✕, Esc, backdrop, in-app navigation, dan dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-93
  - TC-GS-POS-94
  - TC-GS-POS-95
  - TC-GS-POS-96
  - TC-GS-POS-97
  - TC-GS-POS-98
  - TC-GS-POS-99
  - TC-GS-POS-100
  - TC-GS-POS-101
  - TC-GS-POS-102
  - TC-GS-POS-103
coverage:
  web: automated
---

# Penutupan form Edit via ✕, Esc, backdrop, in-app navigation, dan dialog Unsaved Changes

## Prerequisites

- Login sebagai Role: Total Control
- Record Position tersedia

## Test Steps

### Tutup Form Tanpa Perubahan (Clean)

1. Buka modal Edit pada salah satu record
2. Klik tombol `[✕]` tanpa mengubah isi field
3. Verifikasi modal langsung tertutup tanpa dialog konfirmasi
4. Buka kembali modal Edit lalu tekan tombol Esc pada keyboard
5. Verifikasi modal langsung tertutup

### Unsaved Changes Saat Nilai Diubah

6. Buka kembali modal Edit dan ubah teks field
7. Klik tombol `[✕]`
8. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" muncul
9. Klik "[Cancel]" pada dialog
10. Verifikasi dialog tertutup dan modal Edit tetap terbuka dengan perubahan teks masih ada
11. Klik area backdrop di luar modal
12. Verifikasi modal tidak tertutup
13. Kembalikan nilai field persis sama seperti nilai aslinya, lalu tekan Esc
14. Verifikasi modal langsung tertutup (tidak dianggap dirty jika nilai dikembalikan identik)
15. Buka kembali modal Edit, klik "[Clear Field]", lalu klik `[✕]`
16. Verifikasi dialog Unsaved Changes muncul
17. Klik "[Leave]", verifikasi modal tertutup dan nilai record di tabel tidak berubah

## Notes

- Menggabungkan perilaku penutupan form Edit (TC-GS-POS-93 s.d. 103).
