---
id: TC-FA-FAAM-E2E-210-total-assets-himpunan-aset-dan-empty-state-tanpa-aset
title: "Tab Total Assets: Himpunan Aset Draft-Waiting-Active dan Empty State Tanpa Aset"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-503
  - TC-FA-FAAM-505
coverage:
  web: automated
---

# Tab Total Assets: Himpunan Aset Draft-Waiting-Active dan Empty State Tanpa Aset

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Draft Hold Item` (Pre-setup #14i: 1 aset Draft, 1 Waiting for Approval, 1 Active, 1 Deleted, 1 Disposed) dan `Warehouse Pallet` (Pre-setup #13, Total Asset 0).
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-503: Himpunan Tab Total Assets hanya aset Draft, Waiting for Approval, dan Active

1. Klik nama `Draft Hold Item`, klik tab Total Assets
2. Verifikasi label tab `Total Assets (3)`
3. Verifikasi tiga aset Draft, Waiting for Approval, dan Active tampil
4. Verifikasi aset Deleted tidak tampil
5. Verifikasi aset Disposed tidak tampil
6. Tutup popup Detail

### TC-FA-FAAM-505: Tab Total Assets tanpa aset menampilkan empty state genuinely

7. Klik nama `Warehouse Pallet`, klik tab `Total Assets (0)`
8. Verifikasi Title `No assets registered`
9. Verifikasi Description `No assets registered under this asset name yet.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: menutup popup Detail sebelum berpindah ke `Warehouse Pallet`.
- Asersi absence aset Deleted dan Disposed memakai anchor positif: tiga aset Draft, Waiting for Approval, Active tampil pada tabel yang sama.
- Pembagian TC lintas spec: TC-FA-FAAM-501, 502, dan 504 (fixture `Dell Latitude`) ada di spec 166.
- Temuan untuk QA:
  - Nomor Pre-setup `Warehouse Pallet` tidak tertulis di Precondition TC-FA-FAAM-505; spec merujuk Pre-setup #13 (Total Asset 0).
