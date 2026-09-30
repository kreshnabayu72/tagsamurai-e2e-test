---
id: TC-GS-USER-E2E-042-konkurensi-user
title: Dua admin mengubah user yang sama secara bersamaan
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-441
  - TC-GS-USER-401
  - TC-GS-USER-399
  - TC-GS-USER-400
coverage:
  web: automated
---

# Dua admin mengubah user yang sama secara bersamaan

## Prerequisites

- Dua sesi browser dengan akun Total Control (aktor A dan aktor B) di entity yang sama
- Pemicu urutan commit yang terkontrol untuk dua aktor disediakan tim FE: aktor mana yang lebih dulu commit bisa ditentukan, dan kasus bisa diulang dengan urutan dibalik
- User "Budi Santoso" untuk uji edit bersamaan
- User X1 Active Global dengan Access ["Global Settings", "FAMS"] untuk uji Edit lawan Deactivate
- User X2 Active Global dengan foto profil kustom untuk uji Deactivate lawan Delete
- User X3 dengan Access ["Global Settings", "FAMS"] dan access_level Total Control di Global Settings untuk uji Remove Access lawan Delete
- Spec ini menghapus X2 dan X3 dan mengubah X1, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Dua admin mengedit user yang sama

1. Aktor A dan aktor B sama-sama membuka Modal Edit "Budi Santoso" dan melihat data yang sama
2. Aktor A ubah Position lalu klik `[Save]`, dan tunggu sampai berhasil
3. Verifikasi aktor A melihat toast "Success, user has been updated."
4. Aktor B (form masih menampilkan data lama) ubah Division lalu klik `[Save]`
5. Verifikasi aktor B menerima dialog konflik 409 dan perubahan aktor A tidak ditimpa diam-diam
6. Verifikasi aktor B diminta memuat ulang data terbaru sebelum mengirim ulang perubahannya

### Edit Access lawan Deactivate Global

7. Aktor A buka Modal Edit X1 dan hilangkan centang Access "FAMS" (sisa "Global Settings", tetap minimal satu)
8. Aktor B menonaktifkan X1 lewat toggle Active Global dan konfirmasi dialog, sampai commit lebih dulu
9. Aktor A klik `[Save]` pada Modal Edit
10. Verifikasi Save aktor A tetap berhasil dan tidak ada korupsi data
11. Verifikasi X1 berstatus Inactive (dari aktor B) dan Access hanya ["Global Settings"] (dari aktor A), tanpa perubahan yang saling menimpa

### Deactivate Global lawan Delete

12. Aktor A menonaktifkan X2 lewat toggle Active Global dan konfirmasi dialog
13. Aktor B hampir bersamaan menghapus X2 lewat row action `Delete` dan konfirmasi dialog
14. Verifikasi state akhir X2 tidak ambigu: X2 terhapus penuh (baris dan foto profil purge tuntas), atau jika Deactivate commit lebih dulu maka X2 tetap terhapus penuh setelah Delete
15. Verifikasi tidak ada baris X2 berstatus Inactive dengan foto yang hanya sebagian terhapus, dan tabel tidak menampilkan baris dengan status ambigu
16. Ulangi langkah 12 sampai 15 dengan urutan commit dibalik memakai user X2 pengganti

### Remove Access lawan Delete

17. Aktor A hilangkan centang Access "Global Settings" pada Modal Edit X3 dan simpan lewat `[Save]` (cascade menghapus role assignment Role & Permission), konfirmasi dialog Remove Access
18. Aktor B hampir bersamaan menghapus X3 lewat row action `Delete` dan konfirmasi dialog
19. Verifikasi state akhir tidak ambigu: X3 terhapus penuh dan tidak ada baris role assignment di Role & Permission yang menunjuk user yang sudah terhapus
20. Verifikasi tidak ada dua entri cascade Changelog untuk satu perubahan yang sama, dan tidak ada entri Changelog Role & Permission yang menunjuk user yang sudah tidak ada
21. Ulangi langkah 17 sampai 20 dengan urutan commit dibalik memakai user X3 pengganti

## Notes

- Race dua aktor butuh pemicu urutan commit yang terkontrol. Kebutuhan ini ditulis di Prerequisites untuk tim FE, dan hasilnya tidak bergantung pada aktor mana yang menang selama state akhirnya konsisten.
- `TC-GS-USER-399` dan `400` tidak punya padanan lapisan FE, jadi spec ini satu-satunya tempat efeknya di layar (baris, toast, dialog) diperiksa. Sisi API-nya dicakup lapisan BE.
- Aksi yang menghapus data (langkah 12 sampai 21) ditaruh paling akhir.
- Edit bersamaan mengikuti prinsip `P8-8a` (dialog 409 dan refresh, bukan overwrite diam-diam).
