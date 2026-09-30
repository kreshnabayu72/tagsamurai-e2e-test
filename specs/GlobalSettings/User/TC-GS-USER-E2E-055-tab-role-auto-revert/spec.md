---
id: TC-GS-USER-E2E-055-tab-role-auto-revert
title: 'Auto-Revert Total Control dari Tab Role: batal dulu, lalu lanjut'
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-483
  - TC-GS-USER-455
  - TC-GS-USER-575
coverage:
  web: automated
---

# Auto-Revert Total Control dari Tab Role: batal dulu, lalu lanjut

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Siti Rahmawati" berstatus Total Control di Global Settings dengan semua CRUD tercentang di 6 role dan punya riwayat Role di Changelog
- Spec ini menghapus akses Total Control "Siti Rahmawati", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya. Jalankan sendirian karena mengubah Access Level

## Test Steps

### Batalkan dialog

1. Buka User Detail "Siti Rahmawati" > Tab Role
2. Hapus centang `Update` pada baris `Manage TAG`
3. Verifikasi dialog konfirmasi muncul sebelum ada perubahan tersimpan, berisi nama "Siti Rahmawati" dan teks "Editing this permission will remove Total Control/Read Only access from this user. Are you sure you want to continue?", serta tombol `[Cancel]` dan `[Continue]`
4. Klik `[Cancel]`
5. Verifikasi dialog tertutup, checkbox `Update` kembali tercentang, banner "This user has Total Control access." tetap tampil, tidak ada toast, dan tidak ada permintaan perubahan yang terkirim

### Lanjutkan Auto-Revert

6. Hapus centang `Update` pada baris `Manage TAG` lagi lalu klik `[Continue]` di dialog
7. Verifikasi toast "Success, permissions have been updated. Siti Rahmawati is no longer Total Control/Read Only." muncul (bukan toast biasa)
8. Verifikasi banner "This user has Total Control access." hilang otomatis tanpa refresh, `Update` pada `Manage TAG` tidak tercentang, dan 5 role lain tetap CRUD penuh

### Riwayat Role

9. Klik ikon Changelog di toolbar Tab Role
10. Verifikasi modal "Changelog: Siti Rahmawati > Role" menampilkan baris Edit untuk `Manage TAG` dan tidak ada baris Auto-Revert

## Notes

- Dialog dan toast memakai komponen yang sama dengan Role & Permission (`TC-GS-ROLE-52`, `53`, `54`). Sumber `user.md` bagian 4.1 dan `role/PRD/role.md` bagian 3.
- Jalur batal ditaruh lebih dulu karena tidak mengubah data, dan jalur lanjut paling akhir karena mengubah Access Level.
- Baris Auto-Revert tercatat di Changelog User, System Log, dan Activity Log, tetapi tidak di modal Changelog Role (`user.md` bagian 8.2a dan 8.6).
- Notifikasi target dicakup `TC-GS-USER-E2E-056-tab-role-auto-revert-notifikasi`.
