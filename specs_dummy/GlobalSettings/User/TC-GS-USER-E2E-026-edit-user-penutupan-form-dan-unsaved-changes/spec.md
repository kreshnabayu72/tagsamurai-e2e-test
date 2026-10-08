---
id: TC-GS-USER-E2E-026-edit-user-penutupan-form-dan-unsaved-changes
title: "Edit User: Penutupan modal via Esc, ikon close, unsaved changes, dan no-op save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-185
  - TC-GS-USER-186
  - TC-GS-USER-187
  - TC-GS-USER-188
  - TC-GS-USER-189
  - TC-GS-USER-190
coverage:
  web: automated
---

# Edit User: Penutupan modal via Esc, ikon close, unsaved changes, dan no-op save

## Prerequisites

- Login sebagai Role: Total Control
- Berada di halaman User List

## Test Steps

### Unsaved Changes pada Edit

1. Buka modal Edit user Dewi Lestari, ubah teks Last Name
2. Klik tombol [✕], verifikasi dialog Unsaved Changes muncul
3. Klik '[Discard]', verifikasi modal tertutup dan perubahan dibatalkan

### No-Op Save

4. Buka kembali modal Edit Dewi Lestari tanpa mengubah data apa pun, klik '[Save]'
5. Verifikasi modal tertutup dan tidak ada mutasi data yang sia-sia

## Notes

- Menggabungkan 6 test case granular (TC-GS-USER-185 s.d. TC-GS-USER-190).
