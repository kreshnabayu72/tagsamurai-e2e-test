---
id: TC-GS-ROLE-E2E-034-assign-read-only-resilience-server-500
title: "Ketahanan Form Assign Read Only: Penanganan Kegagalan Jaringan Error Server 500"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-83
coverage:
  web: automated
---

# Ketahanan Form Assign Read Only: Penanganan Kegagalan Jaringan Error Server 500

## Prerequisites

- Login sebagai Total Control; intercept respons 500
- Data Uji: Nina Kartika (Pre-setup #11)
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: openModalAssignRO()
- Login sbg Role: Total Control (Ahmad Fauzi)
- Eko Prasetyo login di sesi B

## Test Steps

### Assign Read Only saat user terpilih dihapus atau menjadi tidak eligible sebelum submit (TC-GS-ROLE-83)

1. Sesi A: Tab Read Only > [+ Assign] > centang Wawan Setiawan dan Nina Kartika
2. Sesi B: assign Total Control ke Nina Kartika
3. Sesi A: klik [Assign]
4. Sesi B: hapus user Wawan Setiawan
5. Sesi A: klik [Assign] lagi (Wawan Setiawan masih tercentang)
6. Verifikasi Alert inline: "Nina Kartika is no longer eligible. Please select another."
7. Verifikasi Wawan Setiawan tidak menjadi Read Only (submit atomik)
8. Verifikasi Centangan Nina Kartika hilang, Wawan Setiawan tetap tercentang; picker di-refetch
9. Verifikasi Langkah 5 (V-10, user dihapus): alert inline "Wawan Setiawan no longer exists. Please select another."; centangan Wawan Setiawan hilang; tidak ada user yang menjadi Read Only (submit atomik); picker di-refetch

## Notes

- Memvalidasi alur skenario "Ketahanan Form Assign Read Only: Penanganan Kegagalan Jaringan Error Server 500".
- Aturan PRD terkait: global-settings/role/PRD/role.md §6 V-10; global-settings/role/PRD/role.md §6 V-11.
- Sumber pemetaan test case granular: TC-GS-ROLE-83.
