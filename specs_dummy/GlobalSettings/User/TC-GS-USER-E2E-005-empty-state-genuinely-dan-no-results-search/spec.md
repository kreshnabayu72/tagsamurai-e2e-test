---
id: TC-GS-USER-E2E-005-empty-state-genuinely-dan-no-results-search
title: "Empty state entitas baru tanpa user dan no results state hasil pencarian"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-9
  - TC-GS-USER-10
coverage:
  web: automated
---

# Empty state entitas baru tanpa user dan no results state hasil pencarian

## Prerequisites

- Client baru (hanya memuat 1 Default User)
- Client normal dengan dataset pre-setup

## Test Steps

### Genuinely Empty State Entitas Baru

1. Login sebagai Default User pada entitas baru yang belum memiliki user tambahan
2. Buka Global Settings > User > User List
3. Verifikasi tabel hanya menampilkan 1 baris Default User tanpa ilustrasi empty state
4. Verifikasi toggle dan checkbox pada baris Default User tersebut tampil disabled

### No Results Filtered State

5. Login kembali sebagai Total Control pada entitas normal
6. Buka Global Settings > User > User List
7. Klik ikon Search dan masukkan kata kunci acak 'zzzqqq999xyz'
8. Tekan Enter
9. Verifikasi tabel menampilkan ilustrasi no results dengan pesan 'No results found' dan 'Try adjusting your search or filter.'
10. Verifikasi area pagination dinonaktifkan / menampilkan 0 baris

## Notes

- Menggabungkan 2 test case granular (TC-GS-USER-9 s.d. TC-GS-USER-10).
