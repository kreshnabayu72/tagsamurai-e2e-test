---
id: TC-FA-LIC-E2E-142-changelog-allocation-quota-contoh-prd-urutan-penanda-tingkat
title: "Modal Changelog Allocation Quota: Contoh PRD Urutan Penanda Tingkat Normal, Low, Full, Normal Konsisten dengan License Summary"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-601
coverage:
  web: automated
---

# Modal Changelog Allocation Quota: Contoh PRD Urutan Penanda Tingkat Normal, Low, Full, Normal Konsisten dengan License Summary

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #37) `totalControlLogPrd_automated_{namaCompany}@qwertysystem.net`, client Paid terpisah dengan data kuota Pre-setup #12 (Total 5000, Remaining 665), password dari `Spectra.env.FA_LOGPRD_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_LOGPRD_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, flag Guided Tooltip): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota contoh PRD #37 (6 entri), dirujuk lewat `Fixture.fixedAssetLicense.changelogAllocationQuotaPrd` (fixture belum ada, disediakan tim FE).

  | Date | Action | Group Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 29/09/26 19:30 | Edit | — | Quota Alert Level | Full | Normal | System |
  | 29/09/26 18:20 | Edit | — | Quota Alert Level | Low | Full | System |
  | 29/09/26 16:00 | Edit | — | Quota Alert Level | Normal | Low | System |
  | 29/09/26 14:30 | Remove Allocation | Divisi Keuangan | Allocated Quota | 50 | — | Dewi L |
  | 28/09/26 10:12 | Edit | Gudang A | Allocated Quota | — | 100 | Dewi L |
  | 28/09/26 10:05 | Edit | Divisi IT | Allocated Quota | — | 100 | Dewi L |

- Spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-FA-LIC-601: Urutan penanda tingkat konsisten dengan License Summary

1. Buka tab Allocation Quota, klik ikon Changelog pada toolbar Section 2
2. Verifikasi entri 1 (Date terbaru): 29/09/26 19:30, Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Full`, New Value `Normal`, Modified By `System`
3. Verifikasi entri 2: 29/09/26 18:20, Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Low`, New Value `Full`, Modified By `System`
4. Verifikasi entri 3: 29/09/26 16:00, Action `Edit`, Group Name `—`, Field `Quota Alert Level`, Old Value `Normal`, New Value `Low`, Modified By `System`
5. Verifikasi entri 4: 29/09/26 14:30, Action `Remove Allocation`, Group Name `Divisi Keuangan`, Field `Allocated Quota`, Old Value `50`, New Value `—`, Modified By `Dewi L`
6. Verifikasi entri 5: 28/09/26 10:12, Action `Edit`, Group Name `Gudang A`, Field `Allocated Quota`, Old Value `—`, New Value `100`, Modified By `Dewi L`
7. Verifikasi entri 6: 28/09/26 10:05, Action `Edit`, Group Name `Divisi IT`, Field `Allocated Quota`, Old Value `—`, New Value `100`, Modified By `Dewi L`
8. Verifikasi urutan tingkat penanda berkesinambungan Normal → Low → Full → Normal (New Value tiap entri sama dengan Old Value entri yang lebih baru berikutnya)
9. Verifikasi tingkat terakhir adalah `Normal`
10. Tutup modal dengan `[×]`
11. Klik Tab `All License`
12. Verifikasi baris `Total` kolom `Asset` bernilai 5000
13. Verifikasi baris `Remaining` kolom `Asset` bernilai 665 (13,3% dari Total, di atas ambang 10%), konsisten dengan tingkat terakhir `Normal`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 10 menutup modal sebelum pindah ke Tab `All License` (S-03).
- Spec ini terpisah dari spec Changelog Allocation Quota lain karena memakai akun dan client lain (Pre-setup #37) dengan dataset riwayat berbeda.
- Temuan untuk QA:
  - TC-FA-LIC-601 butir b dan c menyimpulkan urutan dan konsistensi dari butir a; spec menulis tiap kesimpulan sebagai `Verifikasi` sendiri (S-01). Total entri 6 bergantung pada fixture pemulih riwayat Pre-setup #37 karena Changelog adalah audit trail permanen (S-12).
