---
id: TC-GS-USER-E2E-039-foto-profil
title: Kelola foto profil user dari User Detail dan Modal Edit
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-75
  - TC-GS-USER-76
  - TC-GS-USER-74
  - TC-GS-USER-371
  - TC-GS-USER-78
  - TC-GS-USER-542
  - TC-GS-USER-373
  - TC-GS-USER-541
  - TC-GS-USER-372
  - TC-GS-USER-77
coverage:
  web: automated
---

# Kelola foto profil user dari User Detail dan Modal Edit

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), bukan Default User, entity Client
- Akses ke File Manager (Recycle Bin) untuk memeriksa foto yang di-soft-delete
- Berkas uji: `photo.jpg` (2 MB, 800x800 px), `photoB.jpg`, `photoSmall.jpg` (di bawah 1 MB), `huge.jpg` (15 MB), dan `document.pdf`
- User "Kartika Foto" tanpa foto profil
- User "Lala Foto" punya foto profil A
- User "Mira Foto" punya foto profil kustom
- Spec ini mengganti dan menghapus foto ketiga user, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Filter dan ukuran file di User Detail

1. Buka User Detail "Kartika Foto", hover Avatar, lalu klik `[Edit]`
2. Verifikasi input file hanya menerima PNG, JPG, dan JPEG dan `document.pdf` tidak bisa dipilih, tanpa pesan error format
3. Pilih `huge.jpg` (15 MB) lalu klik `[Save]`
4. Verifikasi tidak ada pesan error ukuran, foto otomatis di-resize dan tersimpan, dan toast "Success, photo has been updated." muncul
5. Verifikasi avatar "Kartika Foto" berubah dari inisial menjadi foto

### Ganti foto dari User Detail

6. Buka User Detail "Lala Foto", hover Avatar, lalu klik `[Edit]`
7. Verifikasi file picker langsung terbuka (bukan Modal Edit User penuh)
8. Pilih `photoSmall.jpg`
9. Verifikasi toast "Success, photo has been updated." muncul dan avatar menampilkan foto baru
10. Buka Recycle Bin File Manager dan verifikasi foto A milik "Lala Foto" ada di sana (soft-delete otomatis, tidak menumpuk file lama)

### Ganti foto dari Modal Edit

11. Buka Modal Edit "Lala Foto", hover field Photo, lalu klik `[Edit]`
12. Pilih `photoB.jpg`
13. Verifikasi avatar di form langsung menampilkan preview `photoB.jpg` dan foto di server belum berubah
14. Klik `[Save]`
15. Verifikasi toast "Success, user has been updated." muncul dan foto aktif "Lala Foto" sekarang `photoB.jpg`
16. Verifikasi foto sebelumnya ada di Recycle Bin File Manager

### Ganti foto akun sendiri

17. Buka User Detail akun aktor sendiri, hover Avatar di Header, lalu klik `[Edit]`
18. Pilih `photoSmall.jpg`
19. Verifikasi upload berfungsi normal tanpa diblokir self-guard, dan toast "Success, photo has been updated." muncul

### Hapus foto (paling akhir)

20. Buka Modal Edit "Lala Foto", hover field Photo, lalu klik `[Delete]`
21. Verifikasi tidak ada dialog konfirmasi dan tidak ada request ke server, dan avatar di form menandai foto akan dihapus tetapi foto di server belum berubah
22. Klik `[Save]`
23. Verifikasi toast "Success, user has been updated." muncul, foto "Lala Foto" terhapus, dan foto lama ada di Recycle Bin File Manager
24. Buka User Detail "Mira Foto", hover Avatar, lalu klik `[Delete]`
25. Verifikasi dialog memuat "• Mira Foto" dan "This will remove this user's profile photo. Are you sure you want to remove it?", serta tombol `[Cancel]` dan `[Remove]`
26. Klik `[Remove]`
27. Verifikasi toast "Success, photo has been removed." muncul dan avatar kembali ke inisial nama
28. Verifikasi di Recycle Bin File Manager, foto "Mira Foto" tercatat dihapus oleh admin yang login (bukan "System")

## Notes

- Hapus foto ditaruh paling akhir supaya foto yang dipakai kasus lain tetap ada.
- `TC-GS-USER-77` (hapus foto dari Detail) sama dengan `TC-GS-USER-372` pada langkah 24 sampai 28, jadi digabung.
- Pemilihan foto di Modal Edit bersifat staged: tidak ada request sampai `[Save]`, dan baru saat itu foto lama di-soft-delete otomatis.
- `TC-GS-USER-75` dan `76` sudah diselaraskan ke PRD (`prd-conventions.md` bagian File Upload): format difilter di file picker tanpa pesan error, dan ukuran melebihi 1 MB di-resize otomatis tanpa pesan error.
- Tampilan overlay hover (`TC-GS-USER-370`, `537`, `540`), perilaku staged Create (`538`, `539`, `543`), dan kegagalan server (`576`, `450`) dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
