---
id: TC-GS-ACTLOG-E2E-046-snapshot-immutability-data-historis-log-terhadap-mutasi-nama
title: "D3 Snapshot Immutability data historis log terhadap mutasi nama pengguna atau admin di masa kini"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-234
  - TC-GS-ACTLOG-235
coverage:
  web: automated
---

# D3 Snapshot Immutability data historis log terhadap mutasi nama pengguna atau admin di masa kini

## Prerequisites

- Terdapat entri log historis milik user "Budi Santoso" di Tab Session dan admin "Admin A" di Tab User Action sebelum nama diubah

## Test Steps

1. Catat entri log login historis milik "Budi Santoso" pada Tab Session
2. Buka modul User, ubah nama user "Budi Santoso" menjadi "Budi S. Wijaya" lalu simpan
3. Buka kembali Tab Session pada entri log login historis yang dicatat sebelumnya
4. Verifikasi kolom User tetap menampilkan "Budi Santoso" (snapshot beku pada saat kejadian)
5. Catat entri changelog historis dengan Modified By "Admin A" pada Tab User Action
6. Buka modul User, ubah nama admin "Admin A" menjadi "Admin A2" lalu simpan
7. Buka kembali Tab User Action pada entri changelog historis
8. Verifikasi kolom Modified By tetap menampilkan "Admin A" tanpa berubah

## Notes

- Snapshot immutability: log merekam identitas saat kejadian berlangsung dan tidak boleh re-fetch live relation.
