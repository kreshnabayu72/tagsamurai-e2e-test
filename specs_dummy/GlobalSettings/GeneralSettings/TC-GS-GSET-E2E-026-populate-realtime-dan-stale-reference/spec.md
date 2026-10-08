---
id: TC-GS-GSET-E2E-026-populate-realtime-dan-stale-reference
title: Populate real-time opsi dan stale reference filter aktif
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-57
  - TC-GS-GSET-60
coverage:
  web: automated
---

# Populate real-time opsi Modified By dan stale reference pada filter

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Environment menyediakan dua tenant identik melalui hook yang dapat menarik/menghapus data Modified By,
  atau bahwa filter level tenant sudah diset sebelum spec dijalankan (diuji hook `seedLogs`).
- Data changelog dengan `Modified By` untuk user bernama `Kevin`.

## Test Steps

### Populate populer saat filter di-seed (real-time)

1. Buka Modal Changelog
2. Gunakan hook untuk menghapus sementara `Kevin` dari data sumber (atau buat record yang hanya milik
   tenant yang berbeda)
3. Buka Filter dan buka dropdown `Modified By`
4. Verifikasi opsi `Kevin` tidak tampil pada dropdown (tidak stale)
5. Gunakan hook untuk mengembalikan `Kevin` (atau tambahkan user baru `Sarah`) ke sumber data
6. Buka kembali dropdown `Modified By`
7. Verifikasi `Kevin`/`Sarah` tampil sebagai opsi (list untuk popup diperbarui real-time saat data
   sumber berubah — tidak perlu refresh halaman)

### Stale reference pada filter yang sedang aktif

8. Pilih `Modified By = Kevin` lalu klik `[Apply]`
9. Verifikasi sebuah baris dengan `Modified By = Kevin` tampil; baris lain tidak
10. Gunakan hook untuk menghapus `Kevin` dari sumber (lalu biarkan riwayat log tersimpan)
11. Muat ulang halaman / buka ulang modal
12. Verifikasi filter `Modified By = Kevin` masih tampil sebagai chip aktif dan hasil masih sesuai
    dengan baris tersimpan (data yang direferensikan tetap tampil walau sumber user-nya sudah tiada)
13. Verifikasi tidak ada error/blank saat baris stale ter-render (nilai `Modified By` tetap tampil
    sebagai teks; nama user tidak hilang)

## Notes

- PMC `STALE-REFERENCE-CONTRACT` diuji penuh di spec 035 untuk tiga surface; spec ini hanya
  membuktikan bahwa opsi dropdown dan chip filter yang aktif tidak bergantung pada keberadaan sumber
  user terkini.