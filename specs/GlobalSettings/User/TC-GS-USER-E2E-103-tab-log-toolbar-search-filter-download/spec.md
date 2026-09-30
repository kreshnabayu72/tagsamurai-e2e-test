---
id: TC-GS-USER-E2E-103-tab-log-toolbar-search-filter-download
title: 'Search, Filter, dan Download di tiga tab log User Detail'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-137
  - TC-GS-USER-138
  - TC-GS-USER-139
coverage:
  web: automated
---

# Search, Filter, dan Download di tiga tab log User Detail

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Doni Pratama" punya riwayat di Changelog, System Log, dan User Log (User Log memuat IP `192.168.x.x` dan Device / Browser `Chrome`)
- Pembacaan nama berkas unduhan tersedia bagi skrip

## Test Steps

### Tab Changelog

1. Buka User Detail "Doni Pratama" > Tab Changelog dan cari kata dari Action, Field, Old Value, New Value, dan Modified By
2. Verifikasi pencarian cocok untuk kolom-kolom itu, sedangkan teks tanggal tidak menemukan apa pun
3. Buka Filter dan verifikasi field Action, Field, dan Modified By (multi-select, Modified By searchable) tanpa filter Name, lalu terapkan tiap filter
4. Verifikasi OR dalam satu field dan AND antar field
5. Download dan verifikasi nama berkas "Changelog-User-Doni-Pratama"

### Tab System Log

6. Buka Tab System Log dan verifikasi kolom persis Date, Action, Object, Name, Field, Old Value, New Value
7. Cari kata dari keenam kolom teks lalu teks tanggal
8. Verifikasi enam kolom teks cocok dan tanggal tidak
9. Terapkan Filter Action dan Object (multi-select) dan verifikasi keduanya berfungsi
10. Download dan verifikasi nama berkas "System-Log-Doni-Pratama"

### Tab User Log

11. Buka Tab User Log dan cari `192.168` lalu `Chrome`
12. Verifikasi pencarian menemukan baris terkait (IP Address dan Device / Browser bisa dicari)
13. Cari kata dari Activity dan Note, lalu teks tanggal
14. Verifikasi Activity dan Note cocok, tanggal tidak
15. Terapkan Filter Activity dan Status (multi-select) dan verifikasi keduanya berfungsi
16. Download dan verifikasi nama berkas "User-Log-Doni-Pratama"

## Notes

- Sumber `user.md` bagian 4.2, 4.2a, dan 8. Isi kolom tiap tab dicakup `TC-GS-USER-E2E-067-log-changelog-tab-dan-system-log` dan `068-user-log-kolom-dan-sort`.
