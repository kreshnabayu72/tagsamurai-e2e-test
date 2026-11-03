---
id: TC-FA-SU-E2E-313-log-disaring-scope-aktor-ber-scope-grup-pada-modal-combined-changelog
title: "Log Disaring Scope Aktor Ber-scope Grup pada Modal Combined Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-940
coverage:
  web: automated
---

# Log Disaring Scope Aktor Ber-scope Grup pada Modal Combined Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Akun aktor kedua dan ketiga: Read Only Citra Lestari (Pre-setup #3), `readOnly_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_RO_PASSWORD` (butir b); Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD` (butir a). Ganti akun dengan langkah eksplisit 4 sampai 10; hook `after` mengembalikan sesi ke akun default suite (S-07).
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), dan Changelog (#27). Sinta Dewi dan Citra Lestari hanya sebagai aktor (tidak diubah). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Budi Santoso {runId}-313`, email `budi.santoso+{runId}-313@qwertysystem.net`: Active; Group Role Manage group pada Finance & Accounting (di dalam scope aktor Finance & Accounting); sedikitnya satu entri Modal Combined Changelog dari seed Changelog.
  - `Hana Kusuma {runId}-313`, email `hana.kusuma+{runId}-313@qwertysystem.net`: Active; tanpa Group Role (di luar scope aktor Finance & Accounting); sedikitnya satu entri Modal Combined Changelog dari seed Changelog.
- Kemampuan membaca isi berkas hasil Download (nilai sel, tipe sel, BOM), disediakan tim FE (kelas f, hook H11).
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-940: Hasil Search dan Filter pada log hanya mencakup pengguna dalam scope aktor ber-scope grup

1. Buka Modal Combined Changelog, muat ulang sampai halaman termuat
2. Verifikasi Modal Combined Changelog memuat entri ber-User Name `Budi Santoso {runId}-313` dan `Hana Kusuma {runId}-313` (Total Control melihat seluruh entri)
3. Tutup Modal Combined Changelog dengan `[✕]`
4. Ganti akun: klik Logout pada akun saat ini
5. Login sebagai Citra Lestari (`readOnly_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_RO_PASSWORD`) lalu buka Fixed Asset > Settings > User
6. Buka Modal Combined Changelog, muat ulang sampai halaman termuat
7. Verifikasi Modal Combined Changelog memuat entri ber-User Name `Budi Santoso {runId}-313` dan `Hana Kusuma {runId}-313` (Read Only melihat seluruh entri)
8. Tutup Modal Combined Changelog dengan `[✕]`
9. Ganti akun: klik Logout pada akun saat ini
10. Login sebagai Sinta Dewi (Manage user & role Group (Update), Finance & Accounting; email disediakan tim FE, `Spectra.env.FA_MURGR_UPD_PASSWORD`) lalu buka Fixed Asset > Settings > User
11. Buka Modal Combined Changelog, muat ulang sampai halaman termuat
12. Verifikasi Modal Combined Changelog memuat entri ber-User Name `Budi Santoso {runId}-313` (pengguna dalam scope, pembanding)
13. Verifikasi Modal Combined Changelog tidak memuat entri ber-User Name `Hana Kusuma {runId}-313` (di luar scope)
14. Buka filter User Name pada Modal Combined Changelog
15. Verifikasi filter User Name memuat opsi `Budi Santoso {runId}-313` (pembanding)
16. Verifikasi filter User Name tidak memuat opsi `Hana Kusuma {runId}-313`
17. Tutup filter lalu klik Download dan pilih `Download as CSV`
18. Verifikasi isi berkas Download memuat baris ber-User Name `Budi Santoso {runId}-313` (pembanding)
19. Verifikasi isi berkas Download tidak memuat baris ber-User Name `Hana Kusuma {runId}-313`
20. Tutup Modal Combined Changelog dengan `[✕]`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan di dalam TC-FA-SU-940 diubah: butir b (Total Control dan Read Only) dikerjakan sebelum butir a (Sinta Dewi) supaya ganti akun hanya satu arah (S-07, S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 3, 6, 8, 11, 14, 17, 20, 4, 5, 9, 10; langkah baseline jumlah entri (S-12): . Langkah 4 sampai 10 adalah ganti akun eksplisit.
- Klausa "tidak memuat" ditulis sebagai asersi scope exclusion dengan anchor positif pada surface yang sama (entri dan opsi pengguna dalam scope), bukan asersi absence kelas g (bagian 3 prinsip 13 butir g).
- Pengguna milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-313` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-940 tidak menyebut pengguna di luar scope yang memiliki entri log, tidak menyebut email Sinta Dewi, dan Expected butir b tidak menyebut Filter dan Download untuk Total Control dan Read Only; spec memakai pengguna di luar scope milik spec (Hana Kusuma) dan mengasersi butir b hanya pada Modal Combined Changelog. Isi berkas Download diasersi lewat kemampuan baca berkas yang disediakan tim FE (kelas f).
  - Langkah Uji TC-FA-SU-940 membuka Modal Combined Changelog sebelum filter User Name dan Download; Search pada log (judul TC) tidak punya langkah dan tidak diasersi. TC-FA-SU-940 tidak punya Post Condition.
