---
id: TC-AC-SG-E2E-111-bulk-delete-guard-tiga-campur-lolos-dan-skip-member
title: "Bulk Delete: Guard Entitas Tiga Campur, Dua dari Tiga Group Lolos dan Ketiganya Lolos karena Satu Di-skip"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-163
  - TC-AC-SG-164
coverage:
  web: automated
---

# Bulk Delete: Guard Entitas Tiga Campur, Dua dari Tiga Group Lolos dan Ketiganya Lolos karena Satu Di-skip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Tiga Campur (Pre-setup #25) `totalControlTigaCampur_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_TIGACAMPUR_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #25 (entitas `Distributor Tiga Campur`, komposisi group adalah objek uji): tiga group level 1, `Kantor Pusat` (tanpa entitas), `Kantor Cabang` (tanpa entitas), dan `Kantor Mitra` (satu `Client Sinar` Active).
- Spec ini menghapus `Kantor Pusat` dan `Kantor Cabang` pada kedua TC (komposisi tiga group tidak dapat dimiliki spec, S-06 pengecualian 2026-10-30). Pemulihan lewat Fixture BE di hook `before` dan `after` serta di langkah 8 (antar blok TC). Efek: Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) entitas bertambah oleh penghapusan dan pemulihan dan tidak diasersi.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-163: Bulk Delete dua dari tiga group lolos (T-E=1)

1. Centang kolom Checkbox pada baris `Kantor Pusat` dan `Kantor Cabang`
2. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
3. Verifikasi dialog homogen D-06 tampil dengan title "Delete Groups"
4. Verifikasi dialog blok D-08 "Cannot Delete Groups" tidak tampil (guard would-empty tidak terpicu: T=3, E=2, T-E=1)
5. Klik `[Delete]` pada dialog
6. Verifikasi toast sukses: "Success, group has been deleted."
7. Verifikasi `Kantor Mitra` tersisa
8. Lewat Fixture BE, pulihkan entitas Tiga Campur ke baseline (`Kantor Pusat`, `Kantor Cabang`, `Kantor Mitra` beserta `Client Sinar`) hingga tersimpan
9. Muat ulang halaman (F5)

### TC-AC-SG-164: Bulk Delete ketiga group lolos karena satu di-skip (member)

10. Centang kolom Checkbox pada baris `Kantor Pusat`, `Kantor Cabang`, dan `Kantor Mitra`
11. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
12. Verifikasi dialog campuran D-07 tampil: dua kelompok bullet dengan `Kantor Mitra` di kelompok yang di-skip
13. Verifikasi dialog blok D-08 "Cannot Delete Groups" tidak tampil (T=3, pilih 3, E=2)
14. Klik `[Continue]`
15. Verifikasi toast: "Success, group has been deleted. Some items were skipped (still has members)."

## Notes

- Langkah penghubung (S-03): langkah 8 dan 9 (pemulihan baseline dan muat ulang antar blok, S-09).
- TC-AC-SG-162, TC-AC-SG-165, TC-AC-SG-166, dan TC-AC-SG-173 (guard pada entitas lain) berada di spec 046.
- Temuan untuk QA:
  - TC-AC-SG-163 Expected "dialog homogen D-06" dan TC-AC-SG-164 "dialog campuran D-07" tidak menyebut teks dialog; spec mengasersi title dan struktur kelompok bullet dari TC-AC-SG-157 dan TC-AC-SG-158.
