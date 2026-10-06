---
id: TC-GS-GSET-E2E-022-screening-filter-panel-dan-isi-opsi
title: Screening Filter Panel 3 field dan isi opsi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-51
  - TC-GS-GSET-55
  - TC-GS-GSET-56
  - TC-GS-GSET-58
coverage:
  web: automated
---

# Screening Filter Panel: 3 field, isi opsi, dan loading state

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Opsi filter yang diharapkan: `Date` (date picker), `Field` (multi-select searchable default
  `All fields`), `Modified By` (multi-select searchable default `All users`).
- Tidak ada filter `Action` (kolom homogen — filter 1 nilai tetap tidak berguna).

## Test Steps

### Screening Filter Panel

1. Buka Modal Changelog (klik Icon Button `Changelog`)
2. Klik tombol `Filter`
3. Verifikasi panel/overlay filter terbuka (misal drawer di sisi kanan) dan menampilkan judul `Filter`
4. Verifikasi panel menampilkan TIGA grup filter: `Date`, `Field`, `Modified By` — dan **tidak ada
   group Action**
5. Verifikasi tombol `[Apply]` dan kontrol clear/preset tampil
6. Verifikasi panel dapat ditutup lewat ikon `[✕]`/`Esc`

### Isi opsi grup Field (hardcode, verbatim & urutan tetap)

7. Buka dropdown `Field`
8. Verifikasi default tampil `All fields`
9. Verifikasi persis 5 opsi tetap dengan urutan: `Currency Code`, `Time Zone`, `Date Format`,
   `Time Format`, `Session Idle Timeout`
10. Verifikasi daftar tidak berubah terlepas isi Changelog (hardcode)

### Isi opsi Modified By (populate dari log, loading state)

11. Buka dropdown `Modified By`
12. Verifikasi default tampil `All users`
13. Verifikasi saat loading (respons async belum tiba) menampilkan skeleton/spinner, bukan dropdown
    kosong tanpa indikator
14. Verifikasi setelah memuat, opsi = distinct admin yang genuinely tercatat di Changelog entitas ini
    (hanya user yang pernah mengubah setting, bukan seluruh master data User)

### Isi kontrol Date

15. Verifikasi kontrol `Date` menampilkan `Start Date` dan `End Date`
16. Verifikasi kedua input berupa date picker yang valid
17. Verifikasi dapat/tidak diisi mandiri termasuk hanya salah satu ujung

## Notes

- Interaksi select & hasil filter tidak diulang di sini; hanya struktur dan isi opsi (TC-GS-GSET-51,
  55, 56, 58). Interaksi kombinasi diuji pada spec 023-025. Ketiadaan filter `Action` merupakan
  keputusan eksplisit TC-GS-GSET-51 karena isi kolom homogen.