---
id: TC-AC-SG-E2E-019-create-level-1-unsaved-changes-lifecycle
title: "Siklus penutupan modal Create: form pristine, form dirty memicu dialog Unsaved Changes, dan Clear Field"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-180
  - TC-AC-SG-181
  - TC-AC-SG-188
coverage:
  web: automated
---

# Siklus penutupan modal Create: form pristine, form dirty memicu dialog Unsaved Changes, dan Clear Field

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

### Tutup Modal Saat Pristine (Bersih)
1. Klik tombol `[+ New Group]` di sidebar untuk membuka modal
2. Tanpa mengetik karakter apa pun, klik icon tutup `[✕]` di header modal (atau tekan Esc)
3. Verifikasi modal langsung tertutup tanpa memunculkan dialog Unsaved Changes
### Tutup Modal Saat Dirty (Tercemar)
4. Buka kembali modal `[+ New Group]`
5. Ketik teks `"Region Z"` pada field Group Name
6. Klik icon tutup `[✕]` di header modal
7. Verifikasi muncul dialog konfirmasi `"Unsaved Changes"` dengan pesan `"You have unsaved changes. Are you sure you want to leave?"`
8. Klik tombol `[Cancel]` pada dialog
9. Verifikasi dialog tertutup, modal Create tetap terbuka, dan teks `"Region Z"` tetap terisi
10. Klik kembali icon `[✕]` lalu klik tombol `[Leave]` pada dialog konfirmasi
11. Verifikasi modal tertutup penuh dan tidak ada data baru yang dibuat di sistem
### Siklus Tombol Clear Field
12. Buka kembali modal `[+ New Group]` dan ketik teks `"Region Z"`
13. Klik tombol `[Clear Field]` di footer modal
14. Verifikasi field Group Name kembali bersih/kosong
15. Verifikasi modal `[+ New Group]` TETAP TERBUKA (tombol Clear Field tidak menutup modal)

## Notes

- Modal form tidak memiliki tombol [Cancel]; tombol penutup adalah [✕] / Esc (prd-conventions.md §24.1).
