---
id: TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery
title: "Tab User Action: Kombinasi multi-field filter (AND), alur Search dan Filter, independensi reset, dan pemulihan empty state"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-152
  - TC-GS-ACTLOG-153
  - TC-GS-ACTLOG-154
  - TC-GS-ACTLOG-155
  - TC-GS-ACTLOG-156
  - TC-GS-ACTLOG-157
  - TC-GS-ACTLOG-158
  - TC-GS-ACTLOG-159
coverage:
  web: automated
---

# Tab User Action: Kombinasi multi-field filter (AND), alur Search dan Filter, independensi reset, dan pemulihan empty state

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan dataset log bervariasi >10 baris

## Test Steps

1. Terapkan filter Action "Edit" DAN Object "User" lalu klik `[Apply]`
2. Verifikasi hasil tabel adalah irisan AND (hanya entri Edit pada Object User yang tampil)
3. Masukkan keyword pencarian "Finance" pada search box lalu tekan Enter
4. Verifikasi hasil tabel merupakan irisan Search ∩ Multi-Filter tanpa saling menimpa
5. Aktifkan sorting pada kolom Object dan ubah page size pagination ke 25
6. Verifikasi keempat kontrol (Search, Filter, Sort, Pagination) aktif harmonis bersamaan
7. Klik `[Clear Field]` pada Filter Panel lalu klik `[Apply]`
8. Verifikasi filter terlepas sementara keyword Search dan arah Sort tetap aktif
9. Kosongkan search box lalu tekan Enter
10. Verifikasi pencarian terlepas sementara arah Sort tetap aktif
11. Ubah target sort ke kolom Date dan verifikasi sort berpindah tanpa mengubah filter atau search
12. Masukkan kombinasi kriteria hingga menghasilkan "No results found", lalu lepas salah satu kriteria
13. Verifikasi tabel pulih menampilkan data yang sesuai dengan kriteria yang tersisa

## Notes

- State management toolbar mempertahankan status aktif kontrol yang tidak di-clear.
