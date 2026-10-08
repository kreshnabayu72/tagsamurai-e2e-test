---
id: TC-GS-DIV-E2E-022-create-modal-unsaved-changes-protection
title: "Proteksi Perubahan Belum Disimpan pada Create: Dialog Unsaved Changes pada Icon Close & Esc, Serta Blokir Klik Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-68
  - TC-GS-DIV-69
  - TC-GS-DIV-70
  - TC-GS-DIV-71
coverage:
  web: automated
---

# Proteksi Perubahan Belum Disimpan pada Create: Dialog Unsaved Changes pada Icon Close & Esc, Serta Blokir Klik Backdrop

## Prerequisites

- Login sebagai Role: Total Control
- Form Create Division terisi sebagian (dirty state)
- User berada di Global Settings > User > Division

## Test Steps

### Close via icon X saat form dirty lalu Cancel mempertahankan form (TC-GS-DIV-68)

1. Klik `[+ Division]`
2. Isi Division Name `Draft Division`
3. Klik icon close `[✕]`
4. Klik `[Cancel]`
5. Verifikasi Dialog `Unsaved Changes` tampil (severity warning)
6. Verifikasi Body: `You have unsaved changes. Are you sure you want to leave?`
7. Verifikasi Tombol `[Cancel]` dan `[Leave]`
8. Verifikasi Setelah `[Cancel]` dialog tertutup, modal Create tetap terbuka dan Division Name tetap `Draft Division`

### Close via icon X saat form dirty lalu Leave membuang input (TC-GS-DIV-69)

9. Klik `[+ Division]`
10. Isi Division Name `Draft Division`
11. Klik icon close `[✕]`
12. Klik `[Leave]`
13. Verifikasi Dialog `Unsaved Changes` tampil (severity warning)
14. Verifikasi Body: `You have unsaved changes. Are you sure you want to leave?`
15. Verifikasi Tombol `[Cancel]` dan `[Leave]`
16. Verifikasi Setelah `[Leave]` modal Create tertutup dan Division `Draft Division` tidak dibuat

### Close via tombol Escape saat form dirty menampilkan dialog (TC-GS-DIV-70)

17. Klik `[+ Division]`
18. Isi Division Name `Draft Division`
19. Tekan Escape
20. Klik `[Cancel]`
21. Verifikasi Dialog `Unsaved Changes` tampil (severity warning)
22. Verifikasi Body: `You have unsaved changes. Are you sure you want to leave?`
23. Verifikasi Tombol `[Cancel]` dan `[Leave]`
24. Verifikasi Setelah `[Cancel]` modal Create tetap terbuka dengan input dipertahankan

### Klik backdrop saat form dirty tidak menutup form (TC-GS-DIV-71)

25. Klik `[+ Division]`
26. Isi Division Name `Draft Division`
27. Klik area backdrop di luar modal
28. Verifikasi Modal Create tetap terbuka dan Division Name tetap `Draft Division`
29. Verifikasi Dialog `Unsaved Changes` tidak muncul

## Notes

- Memvalidasi proteksi kehilangan data pada form Create yang sudah dimodifikasi (dirty state): kemunculan Dialog 5 Unsaved Changes saat klik icon [✕] atau tekan Esc, aksi [Cancel] mempertahankan modal, aksi [Leave] membuang perubahan dan menutup modal, penutupan tanpa dialog saat form clean, dan proteksi klik backdrop di luar modal (PRD §4.2d D-05, §4.4).
- Sumber pemetaan test case granular: TC-GS-DIV-68, TC-GS-DIV-69, TC-GS-DIV-70, TC-GS-DIV-71.
