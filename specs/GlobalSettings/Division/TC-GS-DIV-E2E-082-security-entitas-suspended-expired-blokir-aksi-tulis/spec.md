---
id: TC-GS-DIV-E2E-082-security-entitas-suspended-expired-blokir-aksi-tulis
title: "Pemblokiran Seluruh Aksi Tulis (Create, Edit, Delete) Saat Status Entitas Workspace Suspended atau Expired"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-263
  - TC-GS-DIV-264
  - TC-GS-DIV-265
coverage:
  web: automated
---

# Pemblokiran Seluruh Aksi Tulis (Create, Edit, Delete) Saat Status Entitas Workspace Suspended atau Expired

## Prerequisites

- Login sebagai Role: Total Control pada Workspace Suspended/Expired
- Login sebagai Total Control pada entitas berstatus Suspended atau Expired
- Entitas berstatus Suspended
- Entitas berstatus Expired

## Test Steps

### Create saat entitas Suspended ditolak server (TC-GS-DIV-263)

1. Login sbg Total Control pada entitas yang di-Suspend
2. Klik `[+ Division]`, isi Name `Suspended Create` lalu `[Submit]`
3. Verifikasi Server menolak dengan `403 Forbidden`
4. Verifikasi Muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
5. Verifikasi Division tidak dibuat

### Edit saat entitas Expired ditolak server (TC-GS-DIV-264)

6. Login sbg Total Control pada entitas yang Expired
7. Edit Division `Finance` lalu klik `[Save]`
8. Verifikasi Server menolak dengan `403 Forbidden`
9. Verifikasi Muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
10. Verifikasi Name tidak berubah

### Delete saat entitas Suspended ditolak server (TC-GS-DIV-265)

11. Login sbg Total Control pada entitas yang di-Suspend
12. Hapus Division bebas relasi lalu konfirmasi
13. Verifikasi Server menolak dengan `403 Forbidden`
14. Verifikasi Muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
15. Verifikasi Division tetap ada

## Notes

- Memvalidasi penolakan server 403 dan umpan balik toast error kanonikal: "Changes can't be saved while this workspace is suspended or expired." saat Create, Edit, maupun Delete dieksekusi pada entitas non-aktif (PRD §9.4.1 D1, entity-isolation.md §18.8).
- Sumber pemetaan test case granular: TC-GS-DIV-263, TC-GS-DIV-264, TC-GS-DIV-265.
