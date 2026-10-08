---
id: TC-GS-USER-E2E-044-sinkron-position-division
title: Perubahan master data Position tercermin di dropdown form User
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-166
  - TC-GS-USER-415
  - TC-GS-USER-416
coverage:
  web: automated
---

# Perubahan master data Position tercermin di dropdown form User

## Prerequisites

- Login sebagai Role: Total Control, entity Client, dengan akses ke Global Settings > Position
- Position "Posisi Sinkron" belum ada di master data, dan nama "Posisi Sinkron Baru" juga belum dipakai
- Spec ini membuat, me-rename, lalu menghapus Position "Posisi Sinkron", jadi tidak meninggalkan data
- Position yang dibuat tidak dipakai user mana pun (bisa dihapus)

## Test Steps

### Position baru langsung muncul

1. Buka User List dan biarkan halaman terbuka
2. Di Global Settings > Position, buat Position baru bernama "Posisi Sinkron"
3. Kembali ke User List dan klik `[+ User]`
4. Buka dropdown Position pada modal Create
5. Verifikasi "Posisi Sinkron" tampil sebagai opsi tanpa perlu memuat ulang aplikasi
6. Klik `✕` untuk menutup modal

### Position di-rename

7. Di Global Settings > Position, ubah nama "Posisi Sinkron" menjadi "Posisi Sinkron Baru"
8. Kembali ke User List, klik `[+ User]`, lalu buka dropdown Position
9. Verifikasi opsi "Posisi Sinkron Baru" tampil dan "Posisi Sinkron" tidak lagi tampil (relasi memakai FK langsung, bukan salinan nama lama)
10. Klik `✕` untuk menutup modal

### Position dihapus

11. Di Global Settings > Position, hapus "Posisi Sinkron Baru" (tidak dipakai user mana pun)
12. Kembali ke User List, klik `[+ User]`, lalu buka dropdown Position
13. Verifikasi "Posisi Sinkron Baru" tidak lagi tampil sebagai opsi
14. Klik `✕` untuk menutup modal

## Notes

- Yang diuji adalah sisi konsumen: dropdown Position di form User mengikuti master data Position secara langsung.
- Aksi hapus ditaruh paling akhir karena Position yang dihapus tidak bisa dipakai langkah lain.
- Stale reference saat form User sedang terbuka dan Position dihapus atau di-rename oleh admin lain dicakup `TC-GS-USER-E2E-041-stale-reference-master-data`.
- Sumber TC menyebut Division dicakup modul Division. Spec ini hanya menguji Position.
