---
id: TC-GS-ACTLOG-E2E-039-tab-user-action-struktur-filter-panel-dan-filter-individual
title: "Tab User Action: Struktur 5 Field Filter Panel, Logika OR Intra-Field, Logika AND, dan Alur Search-Filter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-159
  - TC-GS-ACTLOG-160
  - TC-GS-ACTLOG-161
  - TC-GS-ACTLOG-162
  - TC-GS-ACTLOG-163
  - TC-GS-ACTLOG-164
coverage:
  web: automated
---

# Tab User Action: Struktur 5 Field Filter Panel, Logika OR Intra-Field, Logika AND, dan Alur Search-Filter

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log User Action bervariasi

## Test Steps

### Struktur Filter Panel Tab User Action
1. Buka Tab User Action, klik icon Filter di toolbar.
2. Verifikasi Filter Panel menampilkan 5 field berurutan: Date, Action, Object, Field, Modified By.
3. Verifikasi kolom Name, Old Value, dan New Value tidak memiliki kontrol di Filter Panel.
### Logika OR Intra-Field & AND Antar-Field
4. Pada field Action, pilih dua opsi: 'Create' dan 'Delete', klik [Apply].
5. Verifikasi tabel menampilkan baris dengan Action Create ATAU Delete.
6. Buka kembali filter, pilih Action 'Edit' DAN Object 'User', klik [Apply].
7. Verifikasi hanya baris yang memenuhi kedua kriteria (Edit AND User) yang tampil.
8. Terapkan kombinasi: Action (Create + Delete) DAN Object (Brand), verifikasi hasil irisan tepat.
### Alur Kombinasi Search & Filter
9. Masukkan Search 'Acme' lalu tekan Enter, buka Filter Panel, pilih Action 'Edit', klik [Apply].
10. Verifikasi hasil akhir menampilkan baris Edit Brand Acme dan keyword 'Acme' tetap ada di search box.
11. Uji alur sebaliknya: terapkan filter Action 'Edit' terlebih dahulu, lalu masukkan Search 'Acme', verifikasi hasil irisan sama.

## Notes

- Penyaringan Tab User Action mendukung logika multi-dimensi tanpa kontrol filter untuk data nilai spesifik.
