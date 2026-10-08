---
id: TC-GS-ROLE-E2E-030-assign-total-control-resilience-server-500-dan-double-submit
title: "Ketahanan Form Assign Total Control: Guard Double-Submit dan Penanganan Error Server 500"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-64
  - TC-GS-ROLE-65
coverage:
  web: automated
---

# Ketahanan Form Assign Total Control: Guard Double-Submit dan Penanganan Error Server 500

## Prerequisites

- Login sebagai Total Control; intercept respons 500
- Data Uji: Wawan Setiawan (Pre-setup #11)
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: openModalAssignTC()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Response Assign dibuat gagal 5xx
- Eko Prasetyo (Total Control) login di sesi B

## Test Steps

### Assign Total Control gagal 5xx (TC-GS-ROLE-64)

1. Klik [+ Assign]
2. Centang Wawan Setiawan
3. Klik [Assign]
4. Verifikasi Muncul toast error: "Error, failed to assign Total Control."
5. Verifikasi Popup tetap terbuka dengan Wawan Setiawan tetap tercentang dan [Assign] enabled untuk retry
6. Verifikasi Wawan Setiawan tidak muncul di Tab Total Control

### Assign Total Control saat user terpilih dihapus admin lain sebelum submit (TC-GS-ROLE-65)

7. Sesi A: [+ Assign] > centang Nina Kartika dan Wawan Setiawan
8. Sesi B: hapus user Wawan Setiawan di modul User
9. Sesi A: klik [Assign]
10. Verifikasi Alert inline (danger) di atas tombol footer, template "[User Name] no longer exists. Please select another.": "Wawan Setiawan no longer exists. Please select another."
11. Verifikasi Seluruh submit ditolak: Nina Kartika juga tidak menjadi Total Control
12. Verifikasi Popup tetap terbuka; hanya centangan Wawan Setiawan yang hilang, Nina Kartika tetap tercentang
13. Verifikasi Daftar picker di-refetch tanpa Wawan Setiawan
14. Verifikasi Klik [Assign] ulang: toast sukses "Success, Total Control has been assigned." untuk Nina Kartika

## Notes

- Memvalidasi alur skenario "Ketahanan Form Assign Total Control: Guard Double-Submit dan Penanganan Error Server 500".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 T-02; global-settings/role/PRD/role.md §9.6 Assign access level; global-settings/role/PRD/role.md §9.6 Delta modul ini; global-settings/role/PRD/role.md §6 V-10; global-settings/role/PRD/role.md ROLE-LOGIC-06c.
- Sumber pemetaan test case granular: TC-GS-ROLE-64, TC-GS-ROLE-65.
