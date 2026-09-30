---
id: TC-GS-USER-E2E-054-tab-role-edit-inline-sinkron
title: 'Tab Role di User Detail: tampilan, edit CRUD inline, dan sinkron dua arah dengan Role & Permission'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-96
  - TC-GS-USER-578
  - TC-GS-USER-454
  - TC-GS-USER-355
  - TC-GS-USER-98
  - TC-GS-USER-165
coverage:
  web: automated
---

# Tab Role di User Detail: tampilan, edit CRUD inline, dan sinkron dua arah dengan Role & Permission

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, sesi pertama
- Sesi kedua dengan akun Total Control lain di entity yang sama, membuka Role & Permission
- User "Siti Rahmawati" berstatus Total Control di Global Settings
- User "Rina Readonly" berstatus Read Only di Global Settings
- User "Tono Individual" ber-role individual biasa (bukan Total Control/Read Only), dengan `Update` pada baris `Manage TAG` belum tercentang dan role `Manage files` belum aktif
- Spec ini mengubah role "Tono Individual" dan mengembalikannya di langkah akhir

## Test Steps

### Tampilan Tab Role

1. Buka User Detail "Siti Rahmawati" lalu buka Tab Role
2. Verifikasi banner "This user has Total Control access." tampil dan tabel 6 role tampil dengan kolom Active dan CRUD enabled (bisa diedit, bukan view-only)
3. Verifikasi 6 baris role tetap dan alfabetis (Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role), header kolom tidak punya ikon sort, tidak ada Column Visibility, dan toolbar hanya berisi ikon Changelog (tanpa Search, Filter, Download, atau tombol tambah)
4. Buka User Detail "Rina Readonly" lalu buka Tab Role
5. Verifikasi banner "This user has Read Only access." tampil tanpa tombol assign atau remove, dan tabel 6 role tetap tampil

### Sinkron dari Role & Permission ke Tab Role

6. Di sesi pertama, buka User Detail "Tono Individual" > Tab Role dan biarkan terbuka
7. Di sesi kedua, buka Role & Permission lalu assign Total Control ke "Tono Individual" dan konfirmasi
8. Verifikasi di sesi pertama, tanpa refresh manual, banner "This user has Total Control access." muncul dan tabel 6 role menampilkan CRUD penuh
9. Di sesi kedua, hapus assignment Total Control dari "Tono Individual" dan konfirmasi
10. Verifikasi di sesi pertama, tanpa refresh manual, banner hilang
11. Di sesi kedua, aktifkan role `Manage files` untuk "Tono Individual" di Role & Permission
12. Verifikasi di sesi pertama, tanpa refresh manual, baris `Manage files` menjadi Active

### Edit CRUD dari Tab Role dan sinkron ke Role & Permission

13. Di sesi pertama, centang checkbox `Update` pada baris `Manage TAG` di Tab Role "Tono Individual"
14. Verifikasi perubahan tersimpan otomatis tanpa tombol Save dan toast "Success, permissions have been updated." muncul
15. Verifikasi di sesi kedua, tanpa refresh manual, detail role `Manage TAG` untuk "Tono Individual" di Role & Permission menampilkan `Update` tercentang
16. Di sesi pertama, hapus centang `Update` dan nonaktifkan role `Manage files` untuk mengembalikan data awal
17. Verifikasi toast "Success, permissions have been updated." muncul dan Tab Role kembali ke keadaan awal

## Notes

- Sumber `user.md` bagian 4.1 dan 4.2a (Tab: Role) serta `role/PRD/role.md` bagian 4.2. Tab Role modul ini murni role Global Settings dan satu jalur tulis dengan Role & Permission.
- `TC-GS-USER-99` (empty state Tab Role untuk user tanpa assignment) tidak masuk spec ini karena bertentangan dengan tabel 6 baris tetap. Lihat `GAP-281` di `foundation/prd-gap-registry.md`.
- PRD `user.md` bagian 4.1 menyebut tabel Tab Role "sortable", sedangkan bagian 4.2a menyebut header tidak clickable dan urutan tetap. Langkah 3 mengikuti bagian 4.2a (`TC-GS-USER-355`).
- Auto-Revert saat mengedit CRUD milik Total Control/Read Only dicakup `TC-GS-USER-E2E-055-tab-role-auto-revert`, dan guard aktor Read Only atau capability holder dicakup `TC-GS-USER-E2E-057-tab-role-guard-aktor`.
- Kebutuhan sesi kedua dan akun ber-role individual ditulis di Prerequisites untuk tim FE.
