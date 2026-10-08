---
id: TC-GS-GSET-E2E-010-state-tombol-save
title: State tombol Save behave sesi/editing
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-21
  - TC-GS-GSET-22
  - TC-GS-GSET-23
  - TC-GS-GSET-24
  - TC-GS-GSET-36
coverage:
  web: automated
---

# State tombol Save: disabled/enabled, edit no-op, dan revert

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- `Fixture.globalSettingsGeneralSettings.data.existing` berisi nilai `Currency = IDR`,
  `Time Zone = (UTC+07:00) Bangkok, Hanoi, Jakarta`, `Session Idle Timeout = 30 minutes`,
  `Date Format = dd/MM/yy`, `Time Format = HH:mm`.

## Test Steps

### Tidak ada perubahan → Save disabled

1. Buka halaman `Global Settings > General Settings`
2. Verifikasi tombol `[Save]` dalam keadaan non-aktif (disabled) selama tidak ada perubahan
3. Verifikasi tooltip/keterangan yang menjelaskan alasan tombol non-aktif bila ada per PRD

### Setelah diubah → Save enabled dan nilai tampil

4. Ubah `Session Idle Timeout` menjadi `8 hours`
5. Verifikasi tombol `[Save]` berubah menjadi aktif (enabled)
6. Verifikasi ikon/indikator "perubahan belum disimpan" muncul bila PRD mendefinisikannya

### Edit memicu jalur edit (bukan create)

7. Periksa tombol `[Save]` yang tampil pada keadaan edit
8. Verifikasi tombol itu tidak bermakna Create dan tidak menyisipkan baris baru; label/harga tetap
   `[Save]` sesuai konvensi label edit pada `prd-conventions.md` §24.1
9. Verifikasi tidak ada kontrol `[Submit]`/`[Save Changes]` yang muncul di form ini

### Revert ke nilai awal → kembali disabled

10. Ubah kembali `Session Idle Timeout` ke `30 minutes`
11. Verifikasi tombol `[Save]` kembali non-aktif
12. Verifikasi indikator perubahan belum disimpan (bila ada) hilang

### Revert sebagian dari multi-perubahan

13. Ubah `Time Zone` dan `Currency` sekaligus
14. Verifikasi tombol `[Save]` aktif
15. Kembalikan `Currency` ke nilai awal saja
16. Verifikasi tombol `[Save]` tetap aktif karena `Time Zone` masih berbeda dari tersimpan
17. Kembalikan `Time Zone`, verifikasi tombol `[Save]` non-aktif

## Notes

- TC-GS-GSET-36 dibuktikan pada langkah 8-9: tidak ada jalur Create di form single ini. Detail label
  tombol disepakati dari `prd-conventions.md` §24.1.