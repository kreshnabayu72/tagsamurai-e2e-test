---
id: TC-GS-GSET-E2E-002-loading-skeleton-dan-read-failure
title: Loading skeleton dan pemulihan saat GET form gagal
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-02
  - TC-GS-GSET-05
coverage:
  web: automated
mock: true
---

# Loading skeleton dan pemulihan saat GET form gagal

## Prerequisites

- Spec ini dijalankan dengan `Mode: mock`. Respons HTTP disimulasikan; tidak ada perubahan riil yang
  dikirim ke backend.
- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Mock pertama menunda respons GET `settings/general` selama lebih dari batas yang dibentuk skeleton
  loading (misal 1 detik), lalu mengembalikan data `Fixture.globalSettingsGeneralSettings.data.existing`.
- Mock kedua mengembalikan error 500 pada GET `settings/general` satu kali, lalu sukses saat `[Try Again]`
  diklik.

## Test Steps

### Skeleton loading saat GET berjalan

1. Muat ulang halaman `Global Settings > General Settings` dengan mock delay aktif
2. Verifikasi area form menampilkan skeleton/placeholder loading
3. Verifikasi nilai field tidak tampil sebelum respons selesai
4. Setelah respons selesai, verifikasi kelima field terisi sesuai data `existing`

### Pemulihan saat GET gagal

5. Setel mock agar GET `settings/general` mengembalikan 500
6. Muat ulang halaman
7. Verifikasi area form menampilkan pesan error `Unable to load this data.`
8. Verifikasi tombol `[Try Again]` tampil dan dapat diklik
9. Klik `[Try Again]` dengan mock kini mengembalikan sukses
10. Verifikasi pesan error hilang dan kelima field terisi sesuai data `existing`

## Notes

- Tidak ada langkah yang memverifikasi retry otomatis; pemulihan hanya lewat `[Try Again]`.