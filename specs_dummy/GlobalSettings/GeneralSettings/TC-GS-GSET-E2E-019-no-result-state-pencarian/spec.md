---
id: TC-GS-GSET-E2E-019-no-result-state-pencarian
title: No-result saat pencarian dan filter
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-43
coverage:
  web: automated
---

# No-result state pada search dan filter

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Data changelog tersedia (misal riwayat `Session Idle Timeout` dan `Time Zone`).
- Kombinasi query yang tidak cocok disiapkan via fixture.

## Test Steps

1. Buka halaman `Global Settings > General Settings`
2. Buka Modal Changelog
3. Masukkan query pencarian yang tidak cocok dengan baris mana pun (misal `zzzx`)
4. Verifikasi tabel menampilkan 0 baris dan pesan no-result tampil:
   `No results found` dengan bantuan `Try adjusting your search or filter.`
5. Verifikasi indikator jumlah hasil menampilkan 0
6. Verifikasi footer pagination menampilkan "0 baris" (atau 0 halaman) dan tidak ada halaman yang dapat
   diklik
7. Hapus query pencarian
8. Verifikasi seluruh baris data tampil kembali (state pulih)

## Notes

- Gunakan fixture `Fixture.globalSettingsGeneralSettings.search.noMatch` untuk menjaga query tidak
  secara tidak sengaja cocok dengan data lingkungan.