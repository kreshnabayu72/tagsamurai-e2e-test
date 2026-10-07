---
id: TC-GS-DIV-E2E-033-edit-modal-clear-field-dan-unsaved-changes
title: "Interaksi Form Edit: Pengosongan Murni via Clear Field (Bukan Revert) dan Dialog Unsaved Changes pada Icon Close & Esc"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-105
  - TC-GS-DIV-107
  - TC-GS-DIV-108
coverage:
  web: automated
---

# Interaksi Form Edit: Pengosongan Murni via Clear Field (Bukan Revert) dan Dialog Unsaved Changes pada Icon Close & Esc

## Prerequisites

- Login sebagai Role: Total Control
- Buka Edit Division
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)

## Test Steps

### Clear Field pada Edit mengosongkan field tanpa me-revert nilai tersimpan (TC-GS-DIV-105)

1. Buka row action baris `Accounting` lalu klik `Edit`
2. Klik `[Clear Field]`
3. Verifikasi Division Name dan Code kosong (bukan kembali ke nilai tersimpan)
4. Verifikasi Tidak ada dialog Unsaved Changes
5. Verifikasi Modal tetap terbuka

### Close Edit saat dirty lalu Cancel mempertahankan form (TC-GS-DIV-107)

6. Buka row action baris `Accounting` lalu klik `Edit`
7. Ubah Division Name menjadi `Draft Edit`
8. Klik icon close `[✕]`
9. Klik `[Cancel]`
10. Verifikasi Dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]`, dan tombol `[Leave]`
11. Verifikasi Modal Edit tetap terbuka dan Division Name tetap `Draft Edit`

### Close Edit saat dirty lalu Leave membuang perubahan (TC-GS-DIV-108)

12. Buka row action baris `Accounting` lalu klik `Edit`
13. Ubah Division Name menjadi `Draft Edit`
14. Klik icon close `[✕]`
15. Klik `[Leave]`
16. Verifikasi Dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]`, dan tombol `[Leave]`
17. Verifikasi Modal Edit tertutup dan Name Accounting tidak berubah

## Notes

- Memvalidasi FI-06 (Clear Field pada Edit mengosongkan input murni, bukan me-revert ke nilai DB) dan kemunculan Dialog 5 Unsaved Changes saat form dirty ditutup lewat [✕] atau Esc (PRD §4.2d, §4.4).
- Sumber pemetaan test case granular: TC-GS-DIV-105, TC-GS-DIV-107, TC-GS-DIV-108.
