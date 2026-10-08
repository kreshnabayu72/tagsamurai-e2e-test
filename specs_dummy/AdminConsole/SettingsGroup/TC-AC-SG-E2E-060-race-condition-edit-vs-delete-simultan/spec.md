---
id: TC-AC-SG-E2E-060-race-condition-edit-vs-delete-simultan
title: "Konkurensi 2-Aktor: Cross-action race Edit vs Delete bersamaan pada node yang sama"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-149
coverage:
  web: automated
---

# Konkurensi 2-Aktor: Cross-action race Edit vs Delete bersamaan pada node yang sama

## Prerequisites

- Dua sesi browser independen (Aktor A dan Aktor B) login sebagai Total Control
- Node target X lolos guard Delete (Total Member = 0)

## Test Steps

### Eksekusi Balapan Edit vs Delete
1. Aktor A membuka modal Edit pada node X dan mengubah Group Name menjadi `"Nama Baru"`, belum menekan Save
2. Aktor B membuka dialog Delete pada node X yang sama dan menekan konfirmasi `[Delete]` lebih dulu hingga ter-commit
3. Verifikasi node X telah terhapus dari sistem oleh Aktor B
4. Aktor A menekan tombol `[Save]` pada modal Edit yang masih terbuka
5. Verifikasi submit Edit Aktor A DITOLAK oleh server dengan status HTTP 404/410 (`"This group no longer exists."`)
6. Verifikasi modal Edit Aktor A menampilkan error dan tertutup/auto-refresh
7. Verifikasi node X tidak "hidup kembali" akibat race condition ini
8. Buka Changelog, verifikasi hanya 1 entri Delete (oleh B) yang tercatat dan 0 entri Edit (oleh A)

## Notes

- Membutuhkan Dual Browser Context untuk mengeksekusi timing balapan 2 aktor.
