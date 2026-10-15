---
id: TC-GS-USER-E2E-041-photo-management-user-detail-flow
title: "Photo Management: Upload, preview, dan hapus foto profil avatar dari User Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-335
  - TC-GS-USER-336
  - TC-GS-USER-337
  - TC-GS-USER-338
  - TC-GS-USER-339
  - TC-GS-USER-340
  - TC-GS-USER-341
  - TC-GS-USER-342
  - TC-GS-USER-343
  - TC-GS-USER-1017
  - TC-GS-USER-1041
coverage:
  web: automated
---

# Photo Management: Upload, preview, dan hapus foto profil avatar dari User Detail

## Prerequisites

- Login sebagai Role: Total Control
- Berada di User Detail John Doe

## Test Steps

### Upload dan Ganti Foto Profil

1. Hover area Avatar di User Detail John Doe
2. Klik ikon kamera/upload, pilih file gambar PNG/JPG valid (< 2MB)
3. Verifikasi gambar tampil pada dialog crop/preview
4. Simpan perubahan foto, verifikasi avatar terupdate dengan foto baru

### Hapus Foto Profil

5. Hover Avatar, klik opsi hapus foto
6. Verifikasi foto terhapus dan avatar kembali ke inisial nama

## Notes

- Menggabungkan 11 test case granular (TC-GS-USER-335 s.d. TC-GS-USER-1041).
