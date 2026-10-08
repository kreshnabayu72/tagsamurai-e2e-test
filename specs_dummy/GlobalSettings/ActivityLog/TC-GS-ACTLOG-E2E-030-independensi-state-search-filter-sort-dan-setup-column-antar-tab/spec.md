---
id: TC-GS-ACTLOG-E2E-030-independensi-state-search-filter-sort-dan-setup-column-antar-tab
title: "Independensi State Search, Filter, Sort, Setup Column, dan Paginasi Antar-Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-17
  - TC-GS-ACTLOG-117
  - TC-GS-ACTLOG-126
coverage:
  web: automated
---

# Independensi State Search, Filter, Sort, Setup Column, dan Paginasi Antar-Tab

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log Session dan User Action

## Test Steps

### Konfigurasi State Tab Session
1. Buka Tab Session: masukkan keyword 'Budi' di search box, filter Activity 'Login', sort kolom Activity, ubah page size ke 25.
2. Sembunyikan kolom 'Note' pada Tab Session via Setup Column, klik [Save].
### Pemeriksaan Isolasi Tab User Action
3. Klik tab 'User Action'.
4. Verifikasi kotak Search di Tab User Action kosong (placeholder 'Search user action log...').
5. Verifikasi Filter Panel di Tab User Action kosong tanpa kriteria aktif.
6. Verifikasi pengurutan dan page size berada pada default.
7. Verifikasi kolom 'Field' dan kolom lainnya tetap tampil lengkap (tidak terpengaruh penyembunyian Note di Tab Session).
### Konfigurasi Tab User Action & Kembali ke Session
8. Pada Tab User Action: masukkan Search 'Acme', filter Action 'Edit', sembunyikan kolom 'Field' via Setup Column, klik [Save].
9. Klik kembali tab 'Session'.
10. Verifikasi seluruh state Tab Session (Search 'Budi', filter Activity 'Login', sort Activity, page size 25, dan kolom Note tersembunyi) tetap utuh.
11. Klik kembali tab 'User Action', verifikasi seluruh state Tab User Action (Search 'Acme', filter Action 'Edit', dan kolom Field tersembunyi) tetap utuh.
12. Lakukan refresh browser (F5), verifikasi kedua tab mempertahankan konfigurasinya masing-masing secara independen.

## Notes

- Kedua tab adalah domain audit yang terpisah dengan penyimpanan cache dan state independen.
