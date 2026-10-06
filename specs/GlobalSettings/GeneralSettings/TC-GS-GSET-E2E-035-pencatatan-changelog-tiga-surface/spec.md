---
id: TC-GS-GSET-E2E-035-pencatatan-changelog-tiga-surface
title: Pencatatan changelog tiga surface, N field = N baris
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-105
  - TC-GS-GSET-107
  - TC-GS-GSET-108
  - TC-GS-GSET-109
coverage:
  web: automated
---

# Pencatatan changelog: tiga surface dan granularitas per field

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Hook menyiapkan state bersih yang hanya berisi data awal (Currency=IDR, Time Zone Jakarta,
  Session 30min, Date dd/MM/yy, Time HH:mm), sehingga delta yang dihasilkan spec dikenal persis.
- `after` spec mengembalikan nilai field ke kondisi awal agar changelog tidak menumpuk lintas spec.

## Test Steps

### Logging ke tiga surface

1. Ubah `Session Idle Timeout` menjadi `1 hour` dan `Date Format` menjadi `M/d/yy`
2. Klik `[Save]`; verifikasi toast sukses
3. Buka Modal Changelog
4. Verifikasi baris log `Action=Edit` untuk field `Session Idle Timeout` muncul
5. Verifikasi baris log `Action=Edit` untuk field `Date Format` juga muncul
6. Verifikasi nilai `Old Value` dan `New Value` pada tiap baris sesuai perubahan di langkah 1
7. Verifikasi waktu & pembuat (`Modified By`) tiap baris tercatat dengan benar (user Total Control
    yang login)
8. Verifikasi pencatatan terjadi di ketiga surface: Modal Changelog (langkah 3-7), data yang
    dikirim ke server/sinkronisasi lintas modul tidak menghilangkan catatan, dan kolom log pada
    entitas internal (jika surface ketiga merupakan API yang dipakai halaman lain)
9. Bila PRD mendefinisikan log juga tampil di surface lain (misal log pada halaman Audit trail),
    verifikasi baris yang sama tampil di sana

### Granularitas: N field diubah = N baris

10. Dalam satu aksi simpan ubah `Currency` (via dialog) dan `Time Zone`
11. Klik `[Save]`
12. Buka Modal Changelog
13. Verifikasi tepat dua baris log terbaru: satu untuk `Currency`, satu untuk `Time Zone`
    (bukan satu baris gabungan)

### Keterkaitan Action dan fetch field

14. Verifikasi setiap baris menampilkan Action `Edit` dan field yang spesifik (tidak NULL/blank)
15. Verifikasi kolom `Old Value`/`New Value` menampilkan nilai saat ini; tidak menampilkan simbol
    currency pada nilai currency (penegakan PMC `CURRENCY-SYMBOL`)

## Notes

- PMC `CURRENCY-SYMBOL` menyatakan nilai currency pada changelog ditulis tanpa simbol mata uang
  (misal `IDR` bukan `Rp`). PMC `STALE-REFERENCE-CONTRACT` (nama Modified By tetap tampil walau user
  dihapus) diuji di spec 026.