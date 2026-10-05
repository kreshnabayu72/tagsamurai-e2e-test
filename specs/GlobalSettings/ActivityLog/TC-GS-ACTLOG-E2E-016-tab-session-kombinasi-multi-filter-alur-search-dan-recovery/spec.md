---
id: TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery
title: "Tab Session: Kombinasi multi-field filter (AND), alur Search dan Filter, independensi reset, dan pemulihan empty state"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-66
  - TC-GS-ACTLOG-67
  - TC-GS-ACTLOG-68
  - TC-GS-ACTLOG-69
  - TC-GS-ACTLOG-70
  - TC-GS-ACTLOG-71
  - TC-GS-ACTLOG-72
  - TC-GS-ACTLOG-73
coverage:
  web: automated
---

# Tab Session: Kombinasi multi-field filter (AND), alur Search dan Filter, independensi reset, dan pemulihan empty state

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session dengan dataset log bervariasi >10 baris

## Test Steps

1. Terapkan filter Activity "Login" DAN Status "Failed" lalu klik `[Apply]`
2. Verifikasi hasil tabel adalah irisan AND (hanya entri Login yang Failed yang tampil)
3. Masukkan keyword pencarian "Budi" pada search box lalu tekan Enter
4. Verifikasi hasil tabel merupakan irisan Search ∩ Multi-Filter tanpa mereset salah satunya
5. Aktifkan sorting pada kolom User dan ubah page size pagination ke 25
6. Verifikasi keempat kontrol (Search, Filter, Sort, Pagination) aktif harmonis bersamaan
7. Klik `[Clear Field]` pada Filter Panel lalu klik `[Apply]`
8. Verifikasi filter terlepas sementara keyword Search dan arah Sort tetap aktif
9. Kosongkan search box lalu tekan Enter
10. Verifikasi pencarian terlepas sementara arah Sort tetap aktif
11. Ubah target sort ke kolom Date dan verifikasi sort berpindah tanpa mengubah filter atau search
12. Masukkan kombinasi kriteria hingga menghasilkan "No results found", lalu lepas salah satu kriteria
13. Verifikasi tabel pulih menampilkan data yang sesuai dengan kriteria yang tersisa

## Notes

- Multi-field filter menggabungkan kriteria antar-kolom secara AND, dan antar-opsi dalam kolom secara OR.
