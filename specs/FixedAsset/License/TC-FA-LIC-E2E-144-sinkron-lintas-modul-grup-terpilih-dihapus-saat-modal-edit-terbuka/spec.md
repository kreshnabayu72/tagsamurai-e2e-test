---
id: TC-FA-LIC-E2E-144-sinkron-lintas-modul-grup-terpilih-dihapus-saat-modal-edit-terbuka
title: "Sinkron Lintas Modul: Node Sidebar Terpilih Dihapus Cascade Saat Modal Edit Allocation Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-535
coverage:
  web: automated
---

# Sinkron Lintas Modul: Node Sidebar Terpilih Dihapus Cascade Saat Modal Edit Allocation Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Pelaku kedua (sesi B): Total Control kedua (Pre-setup #22) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC2_PASSWORD`, memakai sesi API aktor untuk menghapus grup (bukan konteks UI kedua). Nama env `FA_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Dinamis: grup anak Kantor Pusat `Divisi IT+{runId}-144` beralokasi 100 tanpa aset aktif (guard Delete grup Settings > Groups terpenuhi), dibuat fixture BE (disediakan tim FE/BE) di hook `before` dan dihapus sesi B pada langkah 3 (target hapus grup memakai grup milik spec, bukan grup Pre-setup #12); hook `after` menghapus grup bila masih ada. Efek yang dicatat: grup terhapus dan entri Remove Allocation bertambah permanen di Changelog Allocation Quota, System Log, dan Activity Log.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-535: Node Sidebar terpilih dihapus (cascade) saat halaman License terbuka

1. Buka tab Allocation Quota, klik node `Divisi IT+{runId}-144` di Sidebar
2. Klik tombol ikon `[Edit]` di samping nilai `Total` pada Group Quota Summary
3. Sesi B (API akun #22): hapus grup `Divisi IT+{runId}-144` di Settings > Groups hingga penghapusan tersimpan
4. Tunggu aksi selesai
5. Isi New Allocated Quota `120`, klik `[Save]`
6. Verifikasi toast netral `This group is no longer available.`
7. Verifikasi modal Edit Allocation tertutup
8. Verifikasi node aktif Sidebar berpindah ke `All Groups`: Context Header `All Groups`
9. Verifikasi Section 1 berjudul `All License`
10. Verifikasi Section 2 berjudul `Level 1 Groups Quota`
11. Verifikasi Sidebar tidak lagi memuat node `Divisi IT+{runId}-144`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 4 menunggu penghapusan oleh sesi B selesai sebelum sesi A menyimpan (bagian 8b butir 8).
- Absence pada langkah 11 didahului node lain di Sidebar yang tampil lewat Context Header `All Groups` pada langkah 8 (bagian 8b butir 2).
- Grup yang dihapus adalah grup milik spec bersuffix `{runId}-144` yang menggantikan `Divisi IT` Pre-setup #12 sebagai target hapus (S-06 `[KEPUTUSAN 2026-11-02]`); TC-FA-LIC-535 menyebut nama literal.
- Temuan untuk QA:
  - TC-FA-LIC-535 berlabel Manual Only (dua sesi paralel); sesi B hanya memicu perubahan state sehingga memakai sesi API aktor, bukan konteks UI kedua.
  - TC-FA-LIC-535 tidak menyebut cara sesi B menghapus grup selain "di Settings > Groups"; spec menuliskannya sebagai aksi sesi API akun #22.
