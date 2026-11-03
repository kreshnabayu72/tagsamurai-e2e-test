---
id: TC-FA-LIC-E2E-095-changelog-allocation-quota-empty-state-tanpa-pengaruh
title: "Modal Changelog Allocation Quota: Opsi Filter Group Name, Pemisahan dari Modal Concurrent User, Tanpa Pengaruh Node Sidebar, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-360
  - TC-FA-LIC-383
  - TC-FA-LIC-486
  - TC-FA-LIC-600
coverage:
  web: automated
---

# Modal Changelog Allocation Quota: Opsi Filter Group Name, Pemisahan dari Modal Concurrent User, Tanpa Pengaruh Node Sidebar, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, Setup Column, pembacaan berkas unduhan): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; hook `before` dan `after` memulihkannya lewat fixture BE pemulih): hierarki dan kuota #12 (Produksi, Kantor Pusat dengan Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan, Cabang Surabaya, Cabang Medan), riwayat Changelog Allocation Quota #27 (6 entri) dan riwayat Changelog Concurrent User #31 (4 entri) pada client yang sama, dirujuk lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` dan `Fixture.fixedAssetLicense.changelogConcurrentUser` (fixture belum ada, disediakan tim FE).

  | Date | Action | Group Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Edit | — | Quota Alert Level | Normal | Low | System |
  | 29/09/26 10:05 | Edit | Divisi Logistik | Allocated Quota | 500 | 600 | Rudi H |
  | 28/09/26 15:30 | Edit | Divisi IT | Allocated Quota | — | 100 | Dewi L |
  | 27/09/26 09:00 | Remove Allocation | Gudang A | Allocated Quota | 100 | — | Rudi H |
  | 26/09/26 11:20 | Edit | Divisi Keuangan | Allocated Quota | — | 50 | Dewi L |
  | 25/09/26 08:45 | Remove Allocation | Divisi IT | Allocated Quota | 100 | — | Rudi H |

- Kemampuan teknis: membaca berkas unduhan CSV dan XLSX (nama berkas, kolom, baris, sel) disediakan tim FE. Spec ini tidak mengubah state global dan tidak menyimpan Setup Column.
- Pengecualian S-12 [KEPUTUSAN 2026-11-02]: Jumlah dan urutan entri Changelog (langkah 3, 8, 19, 23) diasersi absolut (tanpa baseline) karena fixture BE pemulih riwayat Pre-setup #27 dan #31 juga menghapus entri baru (dinyatakan di `suite.md`); asersi tidak diubah.

## Test Steps

### TC-FA-LIC-486: Ikon Changelog di Tab Concurrent User dan Tab Allocation Quota membuka modal terpisah

1. Buka tab Concurrent User, klik ikon Changelog pada toolbar
2. Verifikasi modal berjudul `Changelog: Concurrent User` dengan kolom `Date | Action | User Name | Field | Old Value | New Value | Modified By`
3. Verifikasi modal memuat 4 entri Force Logout (Pre-setup #31)
4. Verifikasi toolbar Concurrent User memuat `Search | Filter | Changelog` tanpa Download
5. Tutup modal dengan `[×]`
6. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
7. Verifikasi modal berjudul `Changelog: Allocation Quota` dengan kolom `Date | Action | Group Name | Field | Old Value | New Value | Modified By`
8. Verifikasi 6 entri Edit, Remove Allocation, dan penanda `Quota Alert Level` tampil di modal (Pre-setup #27)
9. Verifikasi tidak ada entri Force Logout pada modal tersebut
10. Verifikasi toolbar Section 2 Allocation Quota memuat `Search | Filter | Download | Changelog`

### TC-FA-LIC-383: Opsi filter Group Name hanya nama yang tercatat di tabel log

11. Klik ikon Filter pada toolbar modal
12. Buka dropdown `Group Name`
13. Verifikasi opsi Group Name: Divisi IT, Divisi Keuangan, Divisi Logistik, Gudang A
14. Verifikasi entri penanda tanpa Group Name (`—`) tidak menjadi opsi
15. Verifikasi nama grup tanpa entri log (Kantor Pusat, Produksi, Cabang Surabaya, Cabang Medan) tidak muncul sebagai opsi
16. Tutup dropdown, lalu tutup modal dengan `[×]`

### TC-FA-LIC-600: Isi modal tidak dipengaruhi node Sidebar, penyaringan per grup lewat filter Group Name

17. Klik node `Cabang Medan` di Sidebar
18. Klik ikon Changelog pada toolbar Section 2
19. Verifikasi modal tetap memuat 6 entri client berurutan Date terbaru: 30/09/26 11:15, 29/09/26 10:05, 28/09/26 15:30, 27/09/26 09:00, 26/09/26 11:20, 25/09/26 08:45
20. Tutup modal dengan `[×]`
21. Klik node `Kantor Pusat` di Sidebar
22. Klik ikon Changelog pada toolbar Section 2
23. Verifikasi modal memuat 6 entri yang sama dengan urutan yang sama (isi tidak berubah mengikuti node Sidebar)
24. Klik ikon Filter, pilih Group Name `Gudang A`, klik `[Apply]`
25. Verifikasi tabel menampilkan satu entri 27/09/26 09:00 dengan Action `Remove Allocation`, Old Value `100`, New Value `—`
26. Klik `[Clear Field]`, klik `[Apply]`, lalu tutup modal dengan `[×]`

### TC-FA-LIC-360: Download CSV dan XLSX dengan nama Changelog-Allocation-Quota

27. Klik ikon Changelog pada toolbar Section 2
28. Klik Download > `Download as CSV`
29. Verifikasi tidak ada toast sukses
30. Verifikasi berkas `Changelog-Allocation-Quota.csv` terunduh
31. Klik Download > `Download as XLSX`
32. Verifikasi tidak ada toast sukses
33. Verifikasi berkas `Changelog-Allocation-Quota.xlsx` terunduh
34. Verifikasi isi berkas mengikuti Search/Filter aktif dan kolom visible (tidak ada Search atau Filter aktif; ketujuh kolom visible)
35. Verifikasi sel Old Value dan New Value yang kosong ditulis `-` (Old Value entri 28/09/26 15:30 dan 26/09/26 11:20; New Value entri 27/09/26 09:00 dan 25/09/26 08:45)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 5, 16, 20, dan 26 menutup modal, dropdown, atau membersihkan filter; langkah 26 ditulis eksplisit supaya TC-FA-LIC-360 mulai tanpa filter (S-09). Klik node di langkah 17 dan 21 adalah aksi uji TC-FA-LIC-600.
- Spec ini hanya membaca data (Pre-setup #12, #27, #31 tidak diubah) sehingga tidak ada pemulihan selain jaring pengaman hook.
- Slug folder `empty-state-tanpa-pengaruh` mempertahankan id spec; isi spec ini mengikuti judul: TC-FA-LIC-486, TC-FA-LIC-383, TC-FA-LIC-600, dan TC-FA-LIC-360.
- Spec ini memuat 35 langkah. TC-FA-LIC-540 (modal tanpa entri) dan TC-FA-LIC-601 (contoh PRD) tidak ada di spec ini.
- TC-FA-LIC-383 langkah 15: contoh nama grup tanpa entri log diambil dari hierarki Pre-setup #12; TC hanya menulis "nama tanpa entri log tidak muncul".
- Temuan untuk QA:
  - TC-FA-LIC-360 butir b ("isi mengikuti Search/Filter aktif dan kolom visible; kolom Old/New kosong ditulis `-`") memeriksa nilai sel berkas, sedangkan prinsip kelas f memisahkan isi berkas dari spec fungsional; spec mengikuti TC. Langkah TC tidak mengaktifkan Search atau Filter, sehingga spec mengasersi keadaan tanpa Search/Filter aktif.
  - Jumlah entri absolut (4 entri Force Logout dan 6 entri) pada TC-FA-LIC-486 butir b dan TC-FA-LIC-600 butir a bergantung pada fixture pemulih riwayat Pre-setup #27 dan #31 karena Changelog adalah audit trail permanen (S-12); spec mengasersinya sesuai TC.
