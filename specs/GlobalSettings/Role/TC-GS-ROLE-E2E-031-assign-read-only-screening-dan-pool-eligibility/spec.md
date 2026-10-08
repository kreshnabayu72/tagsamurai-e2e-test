---
id: TC-GS-ROLE-E2E-031-assign-read-only-screening-dan-pool-eligibility
title: "Screening Modal Assign Read Only, Validasi Kelayakan Pool, dan Validasi Seleksi Kosong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-78
  - TC-GS-ROLE-79
  - TC-GS-ROLE-82
coverage:
  web: automated
---

# Screening Modal Assign Read Only, Validasi Kelayakan Pool, dan Validasi Seleksi Kosong

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup #1, #4, #11
- Setup Hook: beforeEach: openModalAssignRO()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Read Only

## Test Steps

### Screening Popup Assign Read Only dan pool-nya (TC-GS-ROLE-78)

1. Klik [+ Assign]
2. Screening popup dan daftar user
3. Verifikasi Title "Assign Read Only"; toolbar, kolom, footer sama dengan Popup Assign Total Control
4. Verifikasi Tidak tampil: semua user Total Control (Ahmad Fauzi, Budi Santoso, Dewi Lestari) dan Read Only (Rina Putri)
5. Verifikasi Tampil: Rahmat Hidayat, Wawan Setiawan, Hendra Wijaya

### Submit Assign Read Only tanpa memilih user (TC-GS-ROLE-79)

6. Klik [+ Assign]
7. Klik [Assign]
8. Verifikasi Teks error inline "You must pick a user" (danger) di atas tombol footer
9. Verifikasi Popup tetap terbuka, tidak ada toast

### Klik ganda [Assign] Popup Assign Read Only (TC-GS-ROLE-82)

10. Klik [+ Assign]
11. Centang Wawan Setiawan
12. Klik [Assign] dua kali cepat
13. Verifikasi Satu toast sukses: "Success, Read Only has been assigned."
14. Verifikasi Changelog Tab Read Only memuat tepat 1 entry Assign untuk Wawan Setiawan

## Notes

- Memvalidasi alur skenario "Screening Modal Assign Read Only, Validasi Kelayakan Pool, dan Validasi Seleksi Kosong".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Tab: Read Only; global-settings/role/PRD/role.md ROLE-LOGIC-06b; global-settings/role/PRD/role.md §6 V-09; global-settings/role/PRD/role.md §9.4.2 klik ganda.
- Sumber pemetaan test case granular: TC-GS-ROLE-78, TC-GS-ROLE-79, TC-GS-ROLE-82.
