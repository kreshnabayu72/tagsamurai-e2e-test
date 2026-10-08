---
id: TC-GS-DIV-E2E-086-concurrency-race-slot-limit-edit-vs-delete-dan-idempotent-delete
title: "Konkurensi Tingkat Lanjut: Rebutan Slot Terakhir Master Data Limit, Race Edit pada Divisi yang Dihapus, dan Hapus Idempotent Bersamaan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-274
  - TC-GS-DIV-275
  - TC-GS-DIV-276
coverage:
  web: automated
---

# Konkurensi Tingkat Lanjut: Rebutan Slot Terakhir Master Data Limit, Race Edit pada Divisi yang Dihapus, dan Hapus Idempotent Bersamaan

## Prerequisites

- Login sebagai Role: Total Control Admin A dan Admin B
- Dua sesi browser aktif (Admin A dan Admin B)
- Jumlah divisi berada pada 1 slot di bawah Master Data Count Limit
- User berada di Global Settings > User > Division
- Jumlah Division satu di bawah Master Data Count Limit
- Division `Temp Unit` (Code `TMP`) ada
- Division `Rapid Unit` dan `Spare Unit` bebas relasi ada

## Test Steps

### Dua admin membuat Division pada slot terakhir: hanya satu yang berhasil (TC-GS-DIV-274)

1. Admin A dan Admin B membuka Create Division dan mengisi Name berbeda
2. Admin A dan Admin B klik `[Submit]` bersamaan
3. Verifikasi Satu Create sukses dengan toast `Success, division has been created.`
4. Verifikasi Create lainnya ditolak dengan Dialog `Limit Reached` (bukan pesan duplicate) dan form tetap terbuka dengan input dipertahankan

### Edit-vs-Delete: Admin A menyimpan Edit pada Division yang baru dihapus Admin B (TC-GS-DIV-275)

5. Admin A membuka Edit Division `Temp Unit`
6. Admin B menghapus Division `Temp Unit`
7. Admin A mengubah Name menjadi `Temp Unit 2` lalu klik `[Save]`
8. Verifikasi Muncul toast netral: `This division is no longer available.`
9. Verifikasi Daftar di-refresh dan baris `Temp Unit` tidak ada
10. Verifikasi Tidak ada Division `Temp Unit 2` yang dibuat

### Edit-vs-Bulk Delete: Admin A menyimpan Edit pada Division yang baru dihapus lewat Bulk Delete Admin B (TC-GS-DIV-276)

11. Admin A membuka Edit Division `Rapid Unit`
12. Admin B memilih `Rapid Unit` dan `Spare Unit` lalu Bulk Delete dan konfirmasi
13. Admin A mengubah Name menjadi `Rapid Unit 2` lalu klik `[Save]`
14. Verifikasi Bulk Delete Admin B sukses untuk kedua Division
15. Verifikasi Save Admin A menampilkan toast netral: `This division is no longer available.` dan daftar di-refresh
16. Verifikasi Tidak ada Division `Rapid Unit 2`

## Notes

- Memvalidasi race slot limit (1 sukses, 1 ditolak Dialog 6), race edit pada divisi yang baru saja dihapus admin lain (toast netral "This division is no longer available."), dan delete ganda bersamaan idempotent tanpa error (NC-03, NC-08, PRD §9.4.2, §9.6).
- Sumber pemetaan test case granular: TC-GS-DIV-274, TC-GS-DIV-275, TC-GS-DIV-276.
