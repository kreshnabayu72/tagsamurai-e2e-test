---
id: TC-GS-ROLE-E2E-043-assign-role-detail-dual-session-concurrency-stale-v10-v11
title: "Konkurensi Antar-Admin Assign Role Detail: Validasi Stale User V-10 Dihapus dan V-11 Sudah Di-Assign Admin Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-99
coverage:
  web: automated
---

# Konkurensi Antar-Admin Assign Role Detail: Validasi Stale User V-10 Dihapus dan V-11 Sudah Di-Assign Admin Lain

## Prerequisites

- Dual session context (Sesi A dan Sesi B Total Control)
- Data Uji: Yoga Pratama, Tari Anjani, Citra Dewanti (Pre-setup #18)
- Setup Hook: dualContext: sessionA, sessionB
- Login sbg Role: Total Control (Ahmad Fauzi)
- Eko Prasetyo login di sesi B

## Test Steps

### Assign Role saat user terpilih dihapus atau sudah di-assign admin lain sebelum submit (TC-GS-ROLE-99)

1. Sesi A: Detail "Manage hardware" > [+ Assign] > centang Yoga Pratama dan Tari Anjani
2. Sesi B: assign Yoga Pratama ke Manage hardware
3. Sesi A: klik [Assign]
4. Sesi A: centang Citra Dewanti (Tari Anjani masih tercentang)
5. Sesi B: hapus user Citra Dewanti
6. Sesi A: klik [Assign] lagi
7. Verifikasi Alert inline: "Yoga Pratama is no longer eligible. Please select another."
8. Verifikasi Tari Anjani tidak ditambahkan (submit atomik) dan tetap tercentang
9. Verifikasi Centangan Yoga Pratama hilang; picker di-refetch
10. Verifikasi Langkah 6 (V-10, user dihapus): alert inline "Citra Dewanti no longer exists. Please select another."; centangan Citra Dewanti hilang, Tari Anjani tetap tercentang; tidak ada baris baru yang dibuat (submit atomik)

## Notes

- Memvalidasi alur skenario "Konkurensi Antar-Admin Assign Role Detail: Validasi Stale User V-10 Dihapus dan V-11 Sudah Di-Assign Admin Lain".
- Aturan PRD terkait: global-settings/role/PRD/role.md §6 V-10; global-settings/role/PRD/role.md §6 V-11.
- Sumber pemetaan test case granular: TC-GS-ROLE-99.
