---
id: TC-AC-SG-E2E-045-popup-total-user-search-dan-eksekusi-filter
title: "Pencarian dan eksekusi filter granular pada popup drill-down Total User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-82
  - TC-AC-SG-168
  - TC-AC-SG-197
  - TC-AC-SG-198
  - TC-AC-SG-199
coverage:
  web: automated
---

# Pencarian dan eksekusi filter granular pada popup drill-down Total User

## Prerequisites

- Login sebagai Role: Total Control
- Popup drill-down Total User terbuka dengan populasi user beragam

## Test Steps

### Pencarian Toolbar Popup
1. Ketik nama salah satu user pada kotak Search toolbar popup
2. Verifikasi tabel popup tersaring hanya menampilkan user yang cocok
### Filter Berdasarkan Division
3. Buka Filter Panel, pilih Division `"IT"`, lalu klik `[Apply]`
4. Verifikasi tabel popup hanya memuat user yang berada di divisi IT
### Filter Berdasarkan Group Role (Group Manager)
5. Buka kembali Filter Panel, kosongkan Division, pilih Group Role `"Group Manager"`, lalu klik `[Apply]`
6. Verifikasi tabel popup hanya memuat user dengan peran Group Manager
### Filter by Nama Role Menangkap User Multi-Role
7. Pilih Group Role `"Manage group"` pada user yang memiliki 2 role (kolom tampil "2 roles")
8. Klik `[Apply]`
9. Verifikasi user tersebut tetap muncul di tabel hasil filter meskipun kolomnya bertuliskan agregat "2 roles"
### Filter Berdasarkan Activation Status (Kolom Curated)
10. Buka Filter Panel, pilih Activation Status `"Pending Activation"`, lalu klik `[Apply]`
11. Verifikasi tabel tersaring hanya menampilkan user berstatus Pending Activation

## Notes

- Filter mencocokkan membership aktual di database, bukan string yang ter-render di sel.
