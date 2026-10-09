---
id: TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas
title: "Defense Gate Direct API: PUT/GET ditolak sesuai RBAC, entitas suspended ditolak, GET Read Only berhasil, dan isolasi record entitas"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-124
  - TC-GS-GSET-125
  - TC-GS-GSET-126
  - TC-GS-GSET-127
  - TC-GS-GSET-128
  - TC-GS-GSET-129
  - TC-GS-GSET-130
  - TC-GS-GSET-144
coverage:
  web: automated
---

# Defense Gate Direct API: PUT/GET ditolak sesuai RBAC, entitas suspended ditolak, GET Read Only berhasil, dan isolasi record entitas

## Prerequisites

- Token sesi aktor tersedia untuk request API langsung ke `/v2/enterprise-management/general-settings`
- Akun Role Read Only, Role System Role, Capability Individual, dan Total Control
- Staff `Client Suspended` (entitas suspended) dan staff `Client A` (entitas `Client Lain` memakai `USD`)
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Payload valid untuk PUT: currencyCode `IDR`, timezone `Asia/Jakarta`, dateFormat `dd/MM/yy`, timeFormat `HH:mm`, sessionIdleTimeout `60`

## Test Steps

### PUT Ditolak per Role

1. Dengan token Read Only, kirim PUT `/v2/enterprise-management/general-settings` dengan payload valid (sessionIdleTimeout `60`, field lain sama dengan nilai tersimpan)
2. Verifikasi Response 403 `Forbidden`
3. Buka General Settings dan verifikasi Session Idle Timeout tetap `30 minutes` (tidak berubah)
4. Ulangi langkah 1 dengan token System Role dan verifikasi Response 403 `Forbidden` serta nilai tersimpan tetap `30 minutes`
5. Ulangi langkah 1 dengan token Capability Individual dan verifikasi Response 403 `Forbidden` serta nilai tersimpan tetap `30 minutes`

### GET Ditolak/Diterima per Role

6. Dengan token System Role, kirim GET `/v2/enterprise-management/general-settings`
7. Verifikasi Response 403 `Forbidden` tanpa nilai General Settings yang dikembalikan
8. Ulangi GET dengan token Capability Individual dan verifikasi Response 403 `Forbidden` tanpa nilai yang dikembalikan
9. Ulangi GET dengan token Read Only
10. Verifikasi Response 200 memuat nilai tersimpan: currencyCode `IDR`, timezone `Asia/Jakarta`, dateFormat `dd/MM/yy`, timeFormat `HH:mm`, sessionIdleTimeout `30`

### PUT Ditolak saat Entitas Suspended

11. Dengan token Total Control staff `Client Suspended`, kirim PUT dengan payload valid (sessionIdleTimeout `60`)
12. Verifikasi Response 403 `Forbidden`
13. Buka General Settings dan verifikasi sessionIdleTimeout tetap `30 minutes`

### Isolasi Record Entitas

14. Buka Global Settings > General Settings sebagai staff `Client A`
15. Verifikasi form menampilkan nilai `Client A` (`IDR`) dan tidak memuat nilai `Client Lain` (`USD`)

## Notes

- Spec FE+BE yang hanya mengasersi respons server dan state data (tanpa UI). Menggabungkan TC-GS-GSET-124, 125, 126, 127, 128, 129, 130, dan 144.
