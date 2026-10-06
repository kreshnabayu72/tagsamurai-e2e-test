---
id: TC-GS-GSET-E2E-029-setup-column-hide-unhide
title: "Setup Column: hide/unhide tiap kolom dan guard minimum"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-83
  - TC-GS-GSET-84
  - TC-GS-GSET-85
  - TC-GS-GSET-86
  - TC-GS-GSET-87
  - TC-GS-GSET-88
coverage:
  web: automated
---

# Setup Column: hide/unhide tiap kolom dan guard satu kolom

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Modal Changelog memiliki data; table default menampilkan keenam kolom.
- Notasi toggle: ikon mata terbuka (unhide/hidden) dan ikon mata tertutup (hide/tampil).

## Test Steps

1. Buka Modal Changelog; buka popup Setup Column

### Unhide penuh

2. Verifikasi keenam kolom default tampil pada tabel
3. Verifikasi pilihan "hide all" tidak tersedia (kontrol hide tidak dapat mengenai semua baris)

### Hide satu per satu (tiap kolom)

4. Sembunyikan kolom `Action`; verifikasi kolom tidak tampil pada tabel
5. Sembunyikan kolom `Field`; verifikasi `Field` hilang dari tabel
6. Sembunyikan kolom `Old Value`; verifikasi hilang
7. Sembunyikan kolom `New Value`; verifikasi hilang
8. Sembunyikan kolom `Modified By`; verifikasi hilang
9. Verifikasi kolom `Date Modified` masih tampil (minimal satu kolom tersisa)

### Guard minimum satu kolom

10. Coba sembunyikan kolom `Date Modified` (kolom terakhir yang tampil)
11. Verifikasi sistem menolak: menampilkan pesan seperti `At least one column must remain visible.`
12. Verifikasi kolom `Date Modified` tetap tampil / aksi hide diabaikan
13. Kembalikan kolom `Action`; sekarang coba sembunyikan `Date Modified` lagi
14. Verifikasi berhasil (ada kolom lain yang tampil) — guard terpenuhi

### Unhide kembali (persist)

15. Buka popup Setup Column; unhide `Action`, `Field`, `New Value`
16. Tutup popup dan verifikasi kolom kembali tampil pada tabel
17. Muat ulang halaman; verifikasi preferensi persist (state tersimpan di local storage)

## Notes

- Guard minimum berlaku di dalam popup (valider sebelum diterapkan ke tabel), bukan setelah kolom
  hilang dari layar.