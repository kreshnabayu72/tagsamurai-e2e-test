---
id: TC-FA-LIC-E2E-154-time-travel-jeda-managed-transition-time-reserved-menjadi-used
title: "Time-travel: Jeda managed_transition_time, Reserved Ditahan Selama Jeda dan Menjadi Used Saat Aset Managed Kembali"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-508
coverage:
  web: automated
---

# Time-travel: Jeda managed_transition_time, Reserved Ditahan Selama Jeda dan Menjadi Used Saat Aset Managed Kembali

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, kuota, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (License Summary Reserved 15, Used 4320, Remaining 665, Unmanaged 27; Divisi IT beralokasi 100 dengan Used by This Group 60) dan #28 (aset Unmanaged di Divisi IT; pemicu aksi Manage sesuai PRD `asset/`). Kondisi blok TC-FA-LIC-508 (diatur fixture BE): `managed_transition_time` 24 jam (nilai bawaan `plans-licensing-config.md`), jam fixture T, Divisi IT Used by This Group 60, Remaining 40, dan 1 aset Unmanaged di Divisi IT.
- Blok TC-FA-LIC-508 (asersi Reserved dari Manage) berlaku setelah `asset/` menetapkan penanda aset dalam transisi Manage (PRD License §12 Open Item #1); selama belum ditetapkan, Reserved dari Manage bernilai 0 dan seluruh aset Unmanaged dihitung pada baris Unmanaged (TC-FA-LIC-612). Pemicu aksi Manage disediakan tim FE.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #28 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Used, Reserved, Unmanaged, dan Remaining, status aset, jam fixture, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: jam fixture digeser maju: sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`) dan jam dipulihkan pada langkah 13 serta di hook `after`. Penantian hasil eventual memakai muat ulang halaman tiap 5 detik dengan batas tunggu 2 menit.

## Test Steps

### TC-FA-LIC-508: Jeda managed_transition_time, Reserved ditahan selama jeda dan menjadi Used saat aset managed kembali

1. Jalankan fixture BE pemulih Pre-setup #12 dengan `managed_transition_time` 24 jam, jam fixture T, Divisi IT Used by This Group 60 (Remaining 40), dan 1 aset Unmanaged di Divisi IT hingga tersimpan
2. Jalankan aksi Manage atas 1 aset Unmanaged di Divisi IT pada jam fixture T sesuai PRD `asset/`
3. Majukan jam fixture ke T + 12 jam
4. Muat ulang License > All License
5. Verifikasi pada T + 12 jam, License Summary: Reserved `16`, Used `4320`, Remaining `664`, dan Unmanaged `26`
6. Buka License > Allocation Quota > node `Divisi IT`
7. Verifikasi Divisi IT: Reserved by This Group `1`
8. Majukan jam fixture melewati T + `managed_transition_time`
9. Muat ulang License > All License tiap 5 detik sampai pemrosesan aset selesai (aset berstatus Active; batas tunggu 2 menit)
10. Verifikasi setelah transisi selesai, License Summary: Reserved `15`, Used `4321`, Remaining `664` (tidak berubah dari langkah 5), dan Unmanaged `26`
11. Buka License > Allocation Quota > node `Divisi IT`
12. Verifikasi Divisi IT: Reserved by This Group `0`, Used by This Group `61`, dan Remaining `39`
13. Pulihkan jam fixture dan jalankan fixture BE pemulih Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Spec berkelas d (time-travel atas `managed_transition_time`); satu TC.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1 dan 13 (fixture BE pemulih dan penyetel state), langkah 2 (pemicu aksi Manage), langkah 3 dan 8 (menggeser jam fixture), muat ulang halaman, dan navigasi License.
- Pemicu aksi Manage ("sesuai PRD `asset/`") belum tertulis di PRD `asset/` (GAP-695); spec mengikuti kalimat TC tanpa mengarang langkah UI.
- Pembagian TC lintas spec: TC-FA-LIC-503, TC-FA-LIC-504, TC-FA-LIC-506, dan TC-FA-LIC-507 ada di spec 123.
