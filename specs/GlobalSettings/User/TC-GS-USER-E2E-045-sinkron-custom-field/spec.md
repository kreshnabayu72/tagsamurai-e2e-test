---
id: TC-GS-USER-E2E-045-sinkron-custom-field
title: Siklus Custom Field User tercermin di form dan detail User
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-414
  - TC-GS-USER-167
  - TC-GS-USER-411
  - TC-GS-USER-413
  - TC-GS-USER-412
coverage:
  web: automated
---

# Siklus Custom Field User tercermin di form dan detail User

## Prerequisites

- Login sebagai Role: Total Control, entity Client, dengan akses ke Global Settings > Custom Field User
- Custom Field "Blood Type" bertipe Dropdown, tidak wajib, dengan opsi "O+"
- Custom Field "Cost Center" belum ada
- User "Ratna Kustom" ada dan sudah punya value "O+" pada "Blood Type"
- Spec ini mengubah tipe "Blood Type" dan menghapus "Cost Center", jadi "Blood Type" dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Custom Field baru langsung muncul di user yang sudah ada

1. Di Custom Field User, buat field baru "Cost Center" bertipe Text dan tidak wajib
2. Buka Modal Edit "Ratna Kustom"
3. Verifikasi field "Cost Center" tampil dengan value kosong, tanpa perlu backfill atau edit manual
4. Isi "Cost Center" dengan "CC-01", klik `[Save]`, lalu buka User Detail "Ratna Kustom" dan verifikasi "Cost Center" menampilkan "CC-01"

### Deactivate lalu reactivate

5. Di Custom Field User, nonaktifkan field "Blood Type"
6. Buka Modal Edit "Ratna Kustom"
7. Verifikasi field "Blood Type" tidak tampil di form
8. Di Custom Field User, aktifkan kembali "Blood Type"
9. Buka Modal Edit "Ratna Kustom"
10. Verifikasi field "Blood Type" tampil kembali dengan value lama "O+" (bukan kosong)

### Ganti Data Type

11. Di Custom Field User, ganti tipe "Blood Type" dari Dropdown menjadi Text
12. Buka User Detail "Ratna Kustom"
13. Verifikasi value "Blood Type" ter-reset ke kosong ("—") dan value lama Dropdown tidak bisa dipulihkan

### Hapus permanen

14. Di Custom Field User, hapus permanen field "Cost Center"
15. Buka Modal Edit "Ratna Kustom"
16. Verifikasi field "Cost Center" tidak tampil sama sekali
17. Buat ulang field "Cost Center" bertipe Text, lalu buka User Detail "Ratna Kustom"
18. Verifikasi "Cost Center" kosong ("—") dan value "CC-01" yang lama tidak muncul lagi

## Notes

- Deactivate hanya menyembunyikan field dan value tetap tersimpan, sedangkan Delete permanen dan ganti Data Type menghapus atau mereset value. Perbedaan itu yang diuji pada langkah 5 sampai 18.
- Ganti Data Type dan hapus permanen ditaruh paling akhir karena tidak bisa dibalik.
- Hapus permanen dan pembuatan ulang dengan nama yang sama membuktikan value benar-benar terhapus dan bukan hanya disembunyikan.
- Perilaku input Custom Field (keystroke, boundary, placeholder) dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
