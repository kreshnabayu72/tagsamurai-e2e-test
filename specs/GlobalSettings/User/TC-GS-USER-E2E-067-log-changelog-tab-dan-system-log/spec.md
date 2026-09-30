---
id: TC-GS-USER-E2E-067-log-changelog-tab-dan-system-log
title: 'Tab Changelog dan modal Changelog menampilkan data identik, System Log mencatat aksi yang dilakukan user'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-110
  - TC-GS-USER-111
coverage:
  web: automated
---

# Tab Changelog dan modal Changelog menampilkan data identik, System Log mencatat aksi yang dilakukan user

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, sesi pertama
- Sesi kedua dengan akun "Doni Pratama" yang punya izin mengedit Division
- User "Doni Pratama" punya riwayat perubahan di Changelog (sedikitnya satu baris Edit)
- Satu Division uji "Divisi Uji Log" yang boleh diubah namanya oleh "Doni Pratama"
- Spec ini mengubah nama "Divisi Uji Log", jadi datanya dikembalikan oleh seeding sebelum run berikutnya

## Test Steps

### Dua permukaan Changelog

1. Di sesi pertama, buka User Detail "Doni Pratama" > Tab Changelog dan catat baris riwayatnya
2. Klik ikon Changelog di toolbar User List, lalu filter ke "Doni Pratama"
3. Verifikasi modal Changelog menampilkan baris riwayat yang identik dengan Tab Changelog pada kolom Date, Action, Field, Old Value, New Value, dan Modified By

### System Log

4. Di sesi kedua, login sebagai "Doni Pratama" lalu ubah nama Division "Divisi Uji Log" lewat modul Division
5. Di sesi pertama, buka User Detail "Doni Pratama" > Tab System Log
6. Verifikasi ada baris baru dengan kolom Date, Action `Edit`, Object Division, Name "Divisi Uji Log", Field nama, serta Old Value dan New Value sesuai perubahan
7. Buka Tab Changelog "Doni Pratama" dan verifikasi perubahan Division itu tidak muncul di sana, karena Changelog mencatat apa yang terjadi pada user ini sedangkan System Log mencatat apa yang dilakukan user ini

## Notes

- Sumber `user.md` bagian 4.1, 4.2a, dan 8. Tab Changelog inline tidak punya kolom Object, sedangkan modal Changelog List punya, jadi perbandingan hanya pada kolom yang sama.
- System Log memakai parity penuh terhadap Changelog objek terkait, dan Auto-Deactivate oleh System tidak masuk System Log (`user.md` bagian 8.3 dan 8.6, sudah dicakup spec 035).
- Cara login ganda dan izin "Doni Pratama" di modul Division disediakan tim FE di tahap script.
