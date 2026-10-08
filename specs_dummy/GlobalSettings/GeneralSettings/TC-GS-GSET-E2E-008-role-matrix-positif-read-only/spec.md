---
id: TC-GS-GSET-E2E-008-role-matrix-positif-read-only
title: "Role Matrix positif Read Only: form read-only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-18
coverage:
  web: automated
---

# Role Matrix positif: Read Only hanya bisa membaca

## Prerequisites

- Sudah login sebagai admin Read Only (`Fixture.globalSettingsGeneralSettings.actors.readOnly`).
- `Fixture.globalSettingsGeneralSettings.data.existing` berisi record lengkap.

## Test Steps

1. Login sebagai Read Only, lalu buka `Global Settings > General Settings`
2. Verifikasi halaman tetap dapat dibuka dan keempat zona halaman tetap tampil
3. Verifikasi seluruh lima field menampilkan data `existing` dan dapat dibaca
4. Verifikasi field `Currency` terlihat tetapi dalam keadaan non-aktif/disabled dan tidak dapat dibuka
5. Verifikasi field `Time Zone`, `Session Idle Timeout`, `Date Format`, dan `Time Format` juga terlihat
   tetapi non-aktif sehingga tidak dapat diubah
6. Verifikasi tombol `[Save]` tidak ditampilkan
7. Verifikasi tidak ada kontrol mutasi lain yang tampil (dialog, dropdown, guided tooltip interaktif)
8. Verifikasi field-field bersifat read-only meskipun respons GET dikirim presisi penuh (cermin dari
   `R-ACC-01`): interaksi apapun tidak mengubah data di layar

## Notes

- Spec ini hanya membuktikan sisi positif: role tidak-Total-Control tetap dapat membuka & membaca halaman.
  Pembuktian penyembunyian menu dan penolakan akses langsung ada di spec 009.
- Perilaku disabled dipisahkan dari hidden: field tetap terlihat namun non-aktif (PRD §4.8).