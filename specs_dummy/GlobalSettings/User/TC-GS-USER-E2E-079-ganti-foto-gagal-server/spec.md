---
id: TC-GS-USER-E2E-079-ganti-foto-gagal-server
title: 'Ganti foto profil gagal karena error server dan foto lama tidak berubah'
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-450
coverage:
  web: automated
---

# Ganti foto profil gagal karena error server dan foto lama tidak berubah

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Kebutuhan mock: respons `500` atau timeout dipaksa pada permintaan simpan ganti foto
- User "Budi Santoso" punya foto profil A, dan berkas foto B valid tersedia untuk dipilih

## Test Steps

1. Buka User Detail "Budi Santoso", hover Avatar, klik `[Edit]`, lalu pilih berkas foto B
2. Simpan perubahan saat server membalas `500`
3. Verifikasi toast error muncul dan pengguna bisa mencoba lagi secara manual
4. Verifikasi Avatar tetap menampilkan foto A
5. Verifikasi tidak ada permintaan hapus foto A yang terkirim setelah kegagalan itu

## Notes

- Sumber `user.md` bagian 4.1 dan 7. Rollback penuh transaksi User dan File Manager (foto A tidak masuk Recycle Bin, foto B tidak jadi berkas yatim) berada di sisi backend dan diverifikasi di lapisan BE (`TC-GS-USER-450` bagian rollback). Spec ini hanya memverifikasi perilaku FE.
