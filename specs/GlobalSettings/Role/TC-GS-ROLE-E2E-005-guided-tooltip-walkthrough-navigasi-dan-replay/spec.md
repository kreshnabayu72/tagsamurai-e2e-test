---
id: TC-GS-ROLE-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay
title: "Guided Tooltip 4-Step Walkthrough, Siklus Navigasi, Trigger First-Visit, dan Replay"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-121
  - TC-GS-ROLE-122
  - TC-GS-ROLE-123
  - TC-GS-ROLE-124
  - TC-GS-ROLE-125
coverage:
  web: automated
---

# Guided Tooltip 4-Step Walkthrough, Siklus Navigasi, Trigger First-Visit, dan Replay

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Flag penyimpanan guided_tooltip_seen_gs-role-permission belum bernilai true

## Test Steps

1. Buka menu Global Settings > Role & Permission pertama kali
2. Verifikasi walkthrough otomatis muncul menunjuk ke Step 1
3. Verifikasi Step 1 menargetkan sub-tab navigation dengan Title: "Access Level Navigation"
4. Verifikasi tombol [Back] tersembunyi pada Step 1 dan tombol [Next] aktif
5. Klik tombol [Next] untuk berpindah ke Step 2
6. Verifikasi Step 2 menargetkan Toolbar Search & Filter dengan Title: "Search & Filters"
7. Klik tombol [Next] untuk berpindah ke Step 3
8. Verifikasi Step 3 menargetkan tombol [+ Assign] dengan Title: "Assign Users"
9. Klik tombol [Next] untuk berpindah ke Step 4
10. Verifikasi Step 4 menargetkan kolom Row Action [⋯] dengan Title: "Assignment Actions"
11. Verifikasi tombol [Next] berubah menjadi tombol [Done] pada Step 4
12. Klik tombol [Done] untuk menyelesaikan walkthrough
13. Verifikasi walkthrough tertutup dan flag seen tersimpan sebagai true
14. Refresh halaman dan verifikasi walkthrough tidak muncul otomatis lagi
15. Klik icon bantuan [?] pada header halaman
16. Verifikasi walkthrough manual replay mulai kembali dari Step 1 tanpa mereset flag seen

## Notes

- Guided Tooltip modul Role & Permission terdiri dari 4 langkah kanonikal (role.md §4.7).
