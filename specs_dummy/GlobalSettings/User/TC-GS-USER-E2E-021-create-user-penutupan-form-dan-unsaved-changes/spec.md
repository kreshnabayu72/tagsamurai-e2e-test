---
id: TC-GS-USER-E2E-021-create-user-penutupan-form-dan-unsaved-changes
title: "Create User: Penutupan modal via Esc, ikon close, klik backdrop, dan unsaved changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-125
  - TC-GS-USER-126
  - TC-GS-USER-127
  - TC-GS-USER-1005
coverage:
  web: automated
---

# Create User: Penutupan modal via Esc, ikon close, klik backdrop, dan unsaved changes

## Prerequisites

- Login sebagai Role: Total Control
- Berada di halaman User List

## Test Steps

### Penutupan Form Bersih

1. Klik '[+ User]', verifikasi modal terbuka
2. Tekan tombol Esc pada keyboard tanpa mengisi form, verifikasi modal langsung tertutup tanpa dialog
3. Buka kembali modal '[+ User]', klik tombol [✕] di header, verifikasi modal tertutup

### Penutupan Form Dirty dan Backdrop No-op

4. Buka kembali modal '[+ User]', ketik teks pada First Name
5. Klik area backdrop luar modal, verifikasi modal tetap terbuka (klik backdrop bersifat no-op)
6. Klik tombol [✕] di header saat form dirty, verifikasi dialog konfirmasi Unsaved Changes muncul dengan tombol '[Keep Editing]' dan '[Discard]'
7. Klik '[Keep Editing]', verifikasi modal Create tetap terbuka dengan isi input utuh
8. Klik [✕] lalu klik '[Discard]', verifikasi modal Create tertutup dan input dibuang

## Notes

- Menggabungkan 4 test case granular (TC-GS-USER-125 s.d. TC-GS-USER-1005).
