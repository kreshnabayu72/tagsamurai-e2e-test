---
id: TC-FA-LIC-E2E-133-edit-allocation-urutan-penolakan-minimum-quota-menang-atas-maximum
title: "Edit Allocation: Urutan Penolakan Saat Submit, Minimum Quota Menang atas Maximum Quota"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-545
coverage:
  web: automated
---

# Edit Allocation: Urutan Penolakan Saat Submit, Minimum Quota Menang atas Maximum Quota

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #12 dengan fixture BE penyetel: Remaining Kantor Pusat 0 (Used by This Group Kantor Pusat dinaikkan 200); Divisi IT beralokasi 100 dengan Used by This Group 100 dan 3 aset Waiting for Approval (Reserved by This Group 3), sehingga Minimum Quota 103 dan Maximum Quota 100.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.

## Test Steps

### TC-FA-LIC-545: Urutan penolakan saat submit, Minimum Quota menang atas Maximum Quota

1. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel: Remaining Kantor Pusat 0 (Used by This Group Kantor Pusat dinaikkan 200) serta Divisi IT beralokasi 100 dengan Used by This Group 100 dan 3 aset Waiting for Approval (Reserved by This Group 3) hingga tersimpan
2. Muat ulang halaman License, lalu klik tab `Allocation Quota`
3. Klik node `Kantor Pusat` di Sidebar
4. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
5. Isi New Allocated Quota `101`
6. Klik `[Save]`
7. Verifikasi `[Save]` ditolak: modal tetap terbuka dengan input `101` dipertahankan
8. Verifikasi hanya pesan inline V-FALIC-01 yang tampil di bawah field: `Cannot set quota below used, reserved, and subgroup-allocated quota (103).`
9. Verifikasi alert V-FALIC-02 tidak tampil
10. Klik icon `[×]`
11. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
12. Klik `[Leave]`
13. Verifikasi Allocated Quota baris `Divisi IT` tetap `100`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, dan klik tab menyiapkan state; menutup modal dirty lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
