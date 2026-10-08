---
id: TC-GS-GSET-E2E-009-role-matrix-negatif-tanpa-akses
title: "Role Matrix negatif: akses tanpa capability ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-19
  - TC-GS-GSET-20
coverage:
  web: automated
---

# Role Matrix negatif: tanpa hak akses menu dan akses langsung

## Prerequisites

- Sudah login sebagai admin dengan capability terbatas yang TIDAK memiliki akses General Settings
  (`Fixture.globalSettingsGeneralSettings.actors.noAccess`).
- Akun Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`) dipakai pada langkah
  kontrol positif.

## Test Steps

### Akses melalui navigasi menu

1. Login sebagai `noAccess`, lalu buka halaman utama aplikasi
2. Verifikasi menu `General Settings` tidak tampil pada navigasi sidebar/Global Settings
3. Verifikasi fungsi navigasi lain tetap dapat diakses

### Akses langsung via URL

4. Coba buka URL halaman `Global Settings > General Settings` secara langsung
5. Verifikasi halaman ditolak/di-redirect ke halaman 403 / halaman tidak ditemukan / kembali ke halaman
   beranda sesuai perilaku yang ditetapkan PRD
6. Verifikasi tidak ada data form yang bocor di layar (form kosong, tidak ada data `existing`)

### Kontrol positif (capability benar)

7. Login sebagai Total Control, lalu buka URL yang sama
8. Verifikasi halaman dapat dibuka dan form menampilkan data
9. Verifikasi tombol `[Save]` tampil dan form dapat diedit

## Notes

- Pembuktian antar-role lain (Read Only tanpa capability) dibahas di spec 008; spec ini fokus pada
  penolakan akses secara navigasi dan URL.