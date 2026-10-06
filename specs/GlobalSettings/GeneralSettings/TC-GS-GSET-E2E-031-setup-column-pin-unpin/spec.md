---
id: TC-GS-GSET-E2E-031-setup-column-pin-unpin
title: "Setup Column: pin/unpin keenam kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-95
  - TC-GS-GSET-96
  - TC-GS-GSET-97
  - TC-GS-GSET-98
  - TC-GS-GSET-99
  - TC-GS-GSET-100
coverage:
  web: automated
---

# Setup Column: pin/unpin tiap kolom dan persist

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Modal Changelog memiliki data; tabel default tanpa kolom ter-pin.

## Test Steps

1. Buka Modal Changelog; buka popup Setup Column

### Pin per kolom

2. Pin kolom `Action`
3. Verifikasi kolom `Action` ter-pin di sisi kiri dan ikon pin tampil
4. Pin kolom `Date Modified`
5. Verifikasi saat tabel di-scroll horizontal, kolom `Date Modified` (ter-pin) tetap tampil
6. Verifikasi kolom ter-pin lebih dari satu tetap berurutan sesuai susunan pin

### Unpin

7. Unpin kolom `Action`
8. Verifikasi kolom `Action` kembali ikut dalam scroll horizontal normal
9. Verifikasi pin pada kolom lain (`Date Modified`) tidak terpengaruh

### Perilaku pin/scroll

10. Pin seluruh enam kolom
11. Verifikasi seluruhnya ter-pin (tidak ada konflik), dan guard tidak muncul saat seluruh kolom visible
12. Scroll horizontal; verifikasi tidak ada kolom bebas yang tampil (semua tetap)

### Persist

13. Tutup popup; muat ulang halaman
14. Verifikasi kolom `Date Modified` tetap ter-pin (persist preferensi)

## Notes

- Pin dimaknai sebagai kolom sticky di sisi kiri tabel; implementasi UI boleh monointern — verifikasi
  fokus pada efek scroll dan persistensi.