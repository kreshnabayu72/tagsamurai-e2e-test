---
id: TC-GS-GSET-E2E-046-concurrent-edit-conflict-409
title: "Concurrent edit dua admin: dialog conflict 409 dan auto-refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-147
coverage:
  web: automated
---

# Concurrent edit dua admin: dialog conflict dan pemulihan

## Prerequisites

- Dua admin Total Control terpisah: `adminA` dan `adminB`
  (`Fixture.globalSettingsGeneralSettings.actors.concurrentA` / `concurrentB`).
- Keduanya membuka halaman yang sama secara simultan; environment men-simulaikan keadaan data yang
  sudah berubah di sisi server.

## Test Steps

1. Login sebagai admin A dan buka `Global Settings > General Settings`
2. Login sebagai admin B (di session/browser kedua) dan buka halaman yang sama
3. Admin B mengubah `Session Idle Timeout` menjadi `1 hour` dan menyimpan (berhasil)
4. Admin A masih pada halaman (belum tersimpan) mengubah `Time Zone` menjadi `(UTC+08:00) Perth`
5. Admin A klik `[Save]`
6. Verifikasi sistem mendeteksi versi/data sudah berubah di server (409/conflict)
7. Verifikasi dialog peringatan muncul (misal pesan bahwa data telah diubah oleh pengguna lain dan
    perlu dimuat ulang)
8. Verifikasi dialog menampilkan opsi muat ulang/refresh
9. Klik tombol konfirmasi untuk memuat ulang data server (atau auto-refresh)
10. Verifikasi form menampilkan data terbaru dari server (Session = `1 hour`)
11. Verifikasi perubahan lama admin A (`Perth`) hilang dari tampilan (tidak tertimpa)
12. Verifikasi toast error yang sesuai tampil tanpa menimbulkan state rusak pada UI

## Notes

- PMC `CONCURRENT-CONTRACT` dipenuhi: detail modifikasi versi ditindak; admin yang mengedit secara
  stale mendapat dialog dan disortir untuk refresh, bukan silent overwrite.