---
id: TC-GS-USER-E2E-113-changelog-modal-hover-truncate
title: 'Teks panjang di modal Changelog terpotong dan tooltip menampilkan teks lengkap'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-247
coverage:
  web: automated
---

# Teks panjang di modal Changelog terpotong dan tooltip menampilkan teks lengkap

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data Changelog mock dengan Name, Field, Old Value, dan New Value yang lebih panjang dari lebar kolom

## Test Steps

1. Buka modal Changelog User List
2. Hover teks yang terpotong di kolom Name, Field, Old Value, dan New Value
3. Verifikasi tooltip menampilkan teks lengkap untuk tiap kolom

## Notes

- Sumber `user.md` bagian 4.2a dan `prd-conventions.md` bagian 9.14.
