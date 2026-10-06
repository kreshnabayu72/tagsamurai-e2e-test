---
id: TC-GS-ROLE-E2E-003-empty-state-detail-role-dan-tab-read-only
title: "Tampilan Empty State pada Halaman Detail 0-User dan Tab Read Only 0-User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-355
coverage:
  web: automated
---

# Tampilan Empty State pada Halaman Detail 0-User dan Tab Read Only 0-User

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Mock respons endpoint access level list (Read Only) menghasilkan data kosong []
- Mock respons endpoint role users list untuk role Manage hardware menghasilkan data kosong []

## Test Steps

1. Buka menu Global Settings > Role & Permission
2. Klik tab 'Read Only' pada navigasi sub-tab
3. Verifikasi tabel Tab Read Only kosong menampilkan ilustrasi dengan Title: "No users assigned" dan Description: "Users with read only access will appear here."
4. Klik tab 'System' pada navigasi sub-tab
5. Buka halaman Detail pada role 'Manage hardware' yang memiliki 0 user
6. Verifikasi tabel Detail menampilkan ilustrasi kosong dengan Title: "No users assigned" dan Description: "Assign users to grant them access with this role."

## Notes

- Deskripsi empty state Tab Read Only berbeda dari halaman Detail meskipun judulnya sama (role.md §7.1).
