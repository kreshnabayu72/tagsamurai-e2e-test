---
id: TC-GS-DIV-E2E-015-create-modal-validasi-field-name-keunikan-dan-scope
title: "Validasi Keunikan Name pada Create: Debounce ~500ms, Trim Spasi Depan/Belakang, dan Izin Duplikasi Lintas Entitas"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-40
  - TC-GS-DIV-41
  - TC-GS-DIV-42
coverage:
  web: automated
---

# Validasi Keunikan Name pada Create: Debounce ~500ms, Trim Spasi Depan/Belakang, dan Izin Duplikasi Lintas Entitas

## Prerequisites

- Login sebagai Role: Total Control
- Division "Finance" sudah ada di entitas uji aktif
- Entitas B memiliki Division dengan nama yang sama
- User berada di Global Settings > User > Division
- Division `Finance` sudah ada

## Test Steps

### Division Name duplikat tanpa membedakan huruf besar kecil menampilkan error setelah debounce (TC-GS-DIV-40)

1. Klik `[+ Division]`
2. Ketik `FINANCE` pada Division Name lalu berhenti mengetik ~500ms
3. Verifikasi Tidak ada error saat masih mengetik; setelah debounce ~500ms muncul error inline `Division Name already exists`
4. Verifikasi Error tidak menunggu kursor keluar dari field

### Division Name duplikat dengan spasi depan dan belakang tetap terdeteksi (TC-GS-DIV-41)

5. Klik `[+ Division]`
6. Ketik `  finance  ` pada Division Name lalu berhenti mengetik ~500ms
7. Verifikasi Muncul error inline `Division Name already exists`

### Submit langsung dengan Division Name duplikat sebelum debounce selesai ditolak (TC-GS-DIV-42)

8. Klik `[+ Division]`
9. Ketik `Finance` dan segera klik `[Submit]` sebelum 500ms berlalu
10. Verifikasi Record tidak dibuat
11. Verifikasi Error inline `Division Name already exists` tampil dan modal tetap terbuka dengan input dipertahankan

## Notes

- Memvalidasi error V-04 ("Division Name already exists" muncul saat debounce ~500ms), auto-trim spasi, dan isolasi entitas (PRD §6, §9.9, §9.11).
- Sumber pemetaan test case granular: TC-GS-DIV-40, TC-GS-DIV-41, TC-GS-DIV-42.
