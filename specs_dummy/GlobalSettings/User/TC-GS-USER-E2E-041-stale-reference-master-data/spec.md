---
id: TC-GS-USER-E2E-041-stale-reference-master-data
title: Data master dihapus atau di-rename oleh admin lain saat form user terbuka
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-88
  - TC-GS-USER-461
  - TC-GS-USER-462
coverage:
  web: automated
---

# Data master dihapus atau di-rename oleh admin lain saat form user terbuka

## Prerequisites

- Dua sesi browser dengan akun Total Control: sesi A mengisi form user, sesi B mengubah data master di modul Position, Division, dan Custom Field User
- Data master sekali pakai yang dibuat spec ini lewat seeding: Position "Posisi Hapus" dan "Posisi Rename", Division "Divisi Hapus", serta opsi "Finance" dan "Operations" pada Custom Field User bertipe Checkbox atau Multi-Dropdown
- Spec ini menghapus dan me-rename data master tersebut, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya
- Pemicu perubahan data master oleh sesi B di tengah pengisian form sesi A disediakan tim FE

## Test Steps

### Position dihapus sebelum Submit

1. Sesi A: klik `[+ User]`, isi semua field wajib, pilih Position "Posisi Hapus"
2. Sesi B: hapus Position "Posisi Hapus" di modul Position
3. Sesi A: klik `[Submit]`
4. Verifikasi inline error "This position no longer exists. Please select another." muncul di bawah dropdown Position
5. Verifikasi dropdown Position otomatis dikosongkan, opsi terbaru dimuat ulang, dan field lain di form dipertahankan
6. Sesi A: klik `✕` dan `[Leave]` untuk menutup modal

### Division dihapus sebelum Submit

7. Sesi A: klik `[+ User]`, isi semua field wajib, pilih Division "Divisi Hapus"
8. Sesi B: hapus Division "Divisi Hapus" di modul Division
9. Sesi A: klik `[Submit]`
10. Verifikasi inline error "This division no longer exists. Please select another." muncul di bawah dropdown Division
11. Verifikasi dropdown Division otomatis dikosongkan dan field lain di form dipertahankan
12. Sesi A: tutup modal dengan `✕` dan `[Leave]`

### Opsi Custom Field multi-select dihapus sebelum Submit

13. Sesi A: klik `[+ User]`, isi semua field wajib, lalu pilih opsi "Finance" dan "Operations" pada Custom Field
14. Sesi B: hapus opsi "Finance" dari master data Custom Field User
15. Sesi A: klik `[Submit]`
16. Verifikasi inline error "Finance no longer exists. Please select another." muncul di bawah field Custom Field, menyebut value yang stale
17. Verifikasi hanya "Finance" yang otomatis dilepas dan "Operations" tetap terpilih, dan form tetap terbuka dengan input lain utuh
18. Sesi A: tutup modal dengan `✕` dan `[Leave]`

### Data master di-rename (bukan error)

19. Sesi A: klik `[+ User]`, isi semua field wajib, pilih Position "Posisi Rename"
20. Sesi B: ubah nama Position "Posisi Rename" menjadi "Posisi Rename Baru" di modul Position
21. Sesi A: klik `[Submit]`
22. Verifikasi tidak ada error stale reference dan Submit berhasil
23. Verifikasi user tersimpan dengan Position "Posisi Rename Baru"

## Notes

- Kasus stale reference ini butuh dua aktor dan perubahan data master di tengah pengisian form, sehingga dipisah dari alur Create dan Edit biasa. Kebutuhan dua sesi ditulis di Prerequisites untuk tim FE.
- Sumber TC menyebut kasus ini berlaku di modal Create dan modal Edit. Spec ini memakai modal Create. Bila Edit perlu diuji terpisah, langkah yang sama diulang dengan `[Save]`.
- Rename tidak menjadi error karena relasi memakai ID/FK (PRD `user.md` bagian 6, baris "Direname (bukan dihapus)").
- Pesan stale reference mengikuti PRD `user.md` bagian 6.
