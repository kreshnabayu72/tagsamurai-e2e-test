---
id: TC-AC-SG-E2E-055-modal-changelog-screening-search-dan-filter
title: "Modal Changelog: pencatatan audit trail Create/Edit/Delete, empty state, search, dan filter Action & Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-99
  - TC-AC-SG-100
  - TC-AC-SG-101
  - TC-AC-SG-102
  - TC-AC-SG-107
  - TC-AC-SG-108
  - TC-AC-SG-186
coverage:
  web: automated
---

# Modal Changelog: pencatatan audit trail Create/Edit/Delete, empty state, search, dan filter Action & Modified By

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat mutasi riwayat Create, Edit, dan Delete di entitas; akun entitas baru tanpa mutasi

## Test Steps

### Empty State Modal Changelog
1. Buka Modal Changelog pada group yang baru dibuat tanpa mutasi lanjutan
2. Verifikasi modal menampilkan empty state dengan teks `"No changelog yet"` dan subtitle `"Activities and changes will appear here."` (§7.1)
### Struktur Kolom & Audit Trail
3. Buka Modal Changelog entitas via toolbar tabel utama
4. Verifikasi modal memuat 7 kolom: `Date`, `Action`, `Group Name`, `Field`, `Old Value`, `New Value`, `Modified By`
5. Verifikasi mutasi Create level 1 mencatat 1 entri: Field `Group Name`, Old `—`, New `[Nama]`
6. Verifikasi mutasi Create subgroup mencatat 1 entri: Field `Group Name`, Old `—`, New `[Nama]`
7. Verifikasi mutasi Edit rename mencatat entri dengan nilai Old dan New yang sesuai
8. Verifikasi mutasi Delete mencatat 1 entri per group di subtree: Field `Group Name`, Old `[Nama]`, New `—`
### Search & Filter Panel Changelog
9. Ketik nama group pada kotak Search modal Changelog lalu tekan Enter
10. Verifikasi hasil tersaring mencakup kolom Group Name
11. Buka Filter Panel Changelog, pilih Action `"Edit"` dan salah satu user Modified By, lalu klik `[Apply]`
12. Verifikasi tabel Changelog hanya menampilkan entri Edit oleh user tersebut (logika AND)

## Notes

- TC-AC-SG-103 s/d 106 (pencatatan DB sinkron dan transaksi atomik) diuji di level backend.
