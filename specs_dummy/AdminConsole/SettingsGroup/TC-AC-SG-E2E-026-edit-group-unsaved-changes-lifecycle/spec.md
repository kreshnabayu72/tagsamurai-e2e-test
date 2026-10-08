---
id: TC-AC-SG-E2E-026-edit-group-unsaved-changes-lifecycle
title: "Siklus modal Edit Group: form pristine, form dirty dengan dialog Unsaved Changes, dan Clear Field"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-182
  - TC-AC-SG-183
  - TC-AC-SG-189
  - TC-AC-SG-190
coverage:
  web: automated
---

# Siklus modal Edit Group: form pristine, form dirty dengan dialog Unsaved Changes, dan Clear Field

## Prerequisites

- Login sebagai Role: Total Control
- Node target `"Region A"`

## Test Steps

### Tutup Modal Edit saat Pristine
1. Klik elipsis `[⋯]` pada `"Region A"` lalu pilih `[Edit]`
2. Verifikasi modal pre-filled dengan nama `"Region A"`
3. Tanpa mengubah teks apa pun, klik icon tutup `[✕]` (atau tekan Esc)
4. Verifikasi modal Edit langsung tertutup tanpa memunculkan dialog Unsaved Changes
### Tutup Modal Edit saat Dirty
5. Buka kembali modal `[Edit]` pada `"Region A"`
6. Ubah nama menjadi `"Region A Baru"`
7. Klik icon tutup `[✕]` di header modal
8. Verifikasi muncul dialog konfirmasi `"Unsaved Changes"` (`"You have unsaved changes. Are you sure you want to leave?"`)
9. Klik `[Cancel]` pada dialog, verifikasi modal tetap terbuka dan input tetap `"Region A Baru"`
10. Klik kembali `[✕]` lalu klik `[Leave]`, verifikasi modal tertutup dan nama di database tidak berubah
### Perilaku Tombol Clear Field & Ketiadaan Stay on Form
11. Buka kembali modal `[Edit]` pada `"Region A"`
12. Klik tombol `[Clear Field]`
13. Verifikasi field Group Name menjadi KOSONG (bukan revert ke nilai awal `"Region A"`) dan modal tetap terbuka
14. Verifikasi pada footer modal Edit TIDAK ADA checkbox `"Stay on this form after submitting"`

## Notes

- Tombol Clear Field selalu mengosongkan input field terlepas dari snapshot data awal.
