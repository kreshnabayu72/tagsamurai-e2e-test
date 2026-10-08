---
id: TC-AC-SG-E2E-020-create-level-1-happy-path-dan-stay-on-form
title: "Pembuatan group level 1 sukses dan perilaku checkbox Stay on this form after submitting"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-32
  - TC-AC-SG-39
coverage:
  web: automated
---

# Pembuatan group level 1 sukses dan perilaku checkbox Stay on this form after submitting

## Prerequisites

- Login sebagai Role: Total Control atau Manage group

## Test Steps

### Submit dengan Stay on this form Dicentang
1. Klik `[+ New Group]` di sidebar
2. Ketik Group Name `"Region C"`
3. Centang checkbox `"Stay on this form after submitting"`
4. Klik `[Submit]`
5. Verifikasi toast sukses `"Success, group has been created."` tampil
6. Verifikasi modal Create TETAP TERBUKA dan field Group Name direset menjadi kosong
7. Verifikasi baris `"Region C"` sudah terbentuk dan muncul di tabel utama dan sidebar tree
### Submit Normal (Modal Tertutup)
8. Ketik Group Name `"Region D"` pada modal yang masih terbuka
9. Hilangkan centang pada checkbox `"Stay on this form after submitting"`
10. Klik `[Submit]`
11. Verifikasi toast sukses `"Success, group has been created."` tampil
12. Verifikasi modal Create otomatis tertutup
13. Verifikasi baris `"Region D"` muncul di tabel utama dan tersusun alfabetis

## Notes

- Stay on this form memungkinkan pembuatan beruntun tanpa membuka ulang modal.
