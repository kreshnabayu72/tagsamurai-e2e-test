---
id: TC-AC-DN-E2E-085-delete-berhasil-hapus-permanen-dan-pilihan-device-sku
title: "Delete Device Name Berhasil: Konfirmasi, List Di-refresh, dan Pilihan Device SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-186
coverage:
  web: automated
---

# Delete Device Name Berhasil: Konfirmasi, List Di-refresh, dan Pilihan Device SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja): #16 `Gate Antenna` sebagai pilihan pembanding pada dropdown Device Name Device SKU.
- Data Dinamis milik spec (di-seed di hook `before`): `Delete Berhasil {runId}-085` (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO); dihapus oleh langkah spec.
- Kemampuan teknis: Fixture BE (disediakan tim FE/BE) untuk men-seed Device Name milik spec (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO; master Pre-setup #13 dan #14) dan menghapus sisanya di hook `after` bila spec berhenti di tengah.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-186: Delete Device Name tanpa SKU dan tanpa unit BYO berhasil setelah konfirmasi

1. Ketik Search `Delete Berhasil {runId}-085`, tekan Enter
2. Klik ikon aksi pada kolom Actions baris `Delete Berhasil {runId}-085` lalu klik `Delete`
3. Klik `[Delete]` pada dialog konfirmasi
4. Verifikasi muncul toast sukses: "Success, device name has been deleted."
5. Verifikasi dialog tertutup
6. Verifikasi List di-refresh
7. Verifikasi baris `Delete Berhasil {runId}-085` tidak lagi ada pada List
8. Buka form Device SKU pada sub-tab `Device SKU` lalu buka dropdown Device Name
9. Verifikasi dropdown Device Name menampilkan pilihan lain `Gate Antenna`
10. Verifikasi `Delete Berhasil {runId}-085` tidak lagi menjadi pilihan Device Name
11. Tutup dropdown dan form Device SKU tanpa mengubah isi, lalu kembali ke sub-tab `Device Name`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (Search target, R-16); langkah 8 dan 11 (membuka dan menutup dropdown Device Name pada sub-tab Device SKU, dibutuhkan Expected butir d). Pilihan `Gate Antenna` pada dropdown adalah anchor positif untuk absence (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-AC-DN-199, 200, 187 ada di spec 070.
- Temuan untuk QA:
  - TC-AC-DN-186 butir d tidak merinci cara membuka dropdown Device Name pada Device SKU; spec membuka form Device SKU yang memuat dropdown itu.
  - Post Condition TC-AC-DN-186 (record terhapus permanen; entri Delete di Changelog, Activity Log, dan System Log aktor) tidak punya langkah observasi di TC, sehingga tidak diasersi.
