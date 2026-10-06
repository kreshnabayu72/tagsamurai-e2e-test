---
id: TC-GS-DIV-E2E-028-delete-single-guard-blocked-in-use
title: "Pemblokiran Penghapusan Divisi yang Sedang Direferensikan Pengguna"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-43
coverage:
  web: automated
---

# Pemblokiran Penghapusan Divisi yang Sedang Direferensikan Pengguna

## Prerequisites

- Login sebagai Role: Total Control
- Divisi 'Human Resources' sedang direferensikan oleh pengguna aktif Budi Santoso

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik menu row action (⋯) pada baris 'Human Resources'
3. Klik menu 'Delete'
4. Verifikasi sistem memblokir penghapusan dengan memunculkan dialog blocker 'Cannot Delete Data' (severity warning)
5. Verifikasi body dialog memuat list bullet '• Human Resources — still in use' dan penjelasan 'These divisions are still in use. Remove the references before deleting.'
6. Verifikasi dialog menerapkan Single Dismiss Rule dengan tombol tunggal '[OK]' (tanpa tombol konfirmasi atau cancel)
7. Klik tombol '[OK]'
8. Verifikasi dialog tertutup dan baris 'Human Resources' tetap aman di tabel

## Notes

- Memvalidasi aturan kanonikal in-use delete guard DIV-LOGIC-02 dan division.md §4.2d Dialog 2.
