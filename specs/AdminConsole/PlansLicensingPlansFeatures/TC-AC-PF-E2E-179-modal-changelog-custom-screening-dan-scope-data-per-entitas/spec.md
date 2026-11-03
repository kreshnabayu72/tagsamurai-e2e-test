---
id: TC-AC-PF-E2E-179-modal-changelog-custom-screening-dan-scope-data-per-entitas
title: Modal Changelog Custom screening isi modal dan hanya memuat log custom plan milik entitas aktor
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-495
  - TC-AC-PF-496
coverage:
  web: automated
---

# Modal Changelog Custom screening isi modal dan hanya memuat log custom plan milik entitas aktor

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun ganti akun (blok TC-AC-PF-496): #10 `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` (entitas Distributor berstatus Active, Total Control); password `Spectra.env.AC_PF_DIST_TC_PASSWORD`. Ganti akun ditulis sebagai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal); `AC_PF_DIST_TC_PASSWORD` (password Total Control Distributor; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`, belum terdaftar).
- Data Pre-setup: Dataset Log C, Changelog Custom Principal enam entri, terbaru dahulu: `29 Jun 26, 10:00` Push Update `Region Jawa Client` (Plan Version, Old `v3`, New `v20`, Sarah T); `28 Jun 26, 16:00` Edit `Growth Tier` (API call quota, Old `100K/month`, New `1M/month`, John D); `28 Jun 26, 09:10` Edit `Growth Tier` (Custom Report Builder, Old `No`, New `Yes`, John D); `17 Jun 26, 14:30` Create `Growth Tier` (Plan Name, Old `—`, New `Growth Tier`, John D); `12 Jun 26, 16:00` Delete `Pilot Reseller` (Plan Name, Old `Pilot Reseller`, New `—`, Jane S); `10 Jun 26, 09:15` Archive `Enterprise Reseller` (Status, Old `Active`, New `Archived`, Jane S). Dataset Log C2: Changelog Custom milik Distributor satu entri Create `Plan Distributor Satu`. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Custom Principal tepat sama dengan Dataset Log C dan Changelog Custom Distributor tepat sama dengan Dataset Log C2 di hook `before`, dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`. Flag Guided Tooltip akun #10 disetel true oleh hook suite `before`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Isi modal Changelog Custom milik Principal (TC-AC-PF-495)

1. Klik tab Custom
2. Klik ikon Changelog pada toolbar
3. Verifikasi Title modal `Changelog: Plans & Features > Custom`
4. Verifikasi kolom `Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By`
5. Verifikasi entri pertama: `29 Jun 26, 10:00` | `Push Update` | `Region Jawa Client` | `Plan Version` | `v3` | `v20` | `Sarah T`
6. Verifikasi entri kedua: `28 Jun 26, 16:00` | `Edit` | `Growth Tier` | `API call quota` | `100K/month` | `1M/month` | `John D`
7. Verifikasi entri ketiga: `28 Jun 26, 09:10` | `Edit` | `Growth Tier` | `Custom Report Builder` | `No` | `Yes` | `John D`
8. Verifikasi entri keempat: `17 Jun 26, 14:30` | `Create` | `Growth Tier` | `Plan Name` | `—` | `Growth Tier` | `John D`
9. Verifikasi entri kelima: `12 Jun 26, 16:00` | `Delete` | `Pilot Reseller` | `Plan Name` | `Pilot Reseller` | `—` | `Jane S`
10. Verifikasi entri keenam: `10 Jun 26, 09:15` | `Archive` | `Enterprise Reseller` | `Status` | `Active` | `Archived` | `Jane S`
11. Tutup modal dengan icon (X)
12. Klik sub-tab Archive
13. Klik ikon Changelog pada toolbar
14. Verifikasi modal yang sama terbuka: Title `Changelog: Plans & Features > Custom` dengan keenam entri yang sama dengan langkah 5 sampai 10
15. Tutup modal dengan icon (X)

### Scope log milik Distributor (TC-AC-PF-496)

16. Logout dari akun #1
17. Login dengan akun #10 `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.AC_PF_DIST_TC_PASSWORD`
18. Buka halaman Plans & Licensing > Plans & Features
19. Klik tab Custom
20. Klik ikon Changelog pada toolbar
21. Verifikasi modal memuat entri Create `Plan Distributor Satu` milik Distributor
22. Verifikasi entri Principal (`Growth Tier`) tidak tampil di modal

## Notes

- Langkah penghubung (S-03): penutupan modal dengan icon (X) antara blok TC dan klik sub-tab Archive sebagai pemicu Expected butir c TC-AC-PF-495.
- Ganti akun (S-07): langkah 16 sampai 18 berpindah dari #1 ke #10; spec berakhir sebagai #10 dan hook `after` memulihkan sesi ke akun default suite.
- Anchor absence (bagian 8b butir 2): Verifikasi langkah 21 (entri Distributor tampil di modal yang sama) mendahului langkah 22.
- Pembagian TC lintas spec: TC-AC-PF-500 dan TC-AC-PF-501 (screening modal Changelog Global Settings) ada di spec 203.
- Temuan untuk QA:
  - Email dan password akun #10 tersedia di Pre-setup TC (baris 10), tetapi nama env password Distributor tidak terdaftar di `suite.md`; spec memakai `AC_PF_DIST_TC_PASSWORD` sesuai pola nama suite.
  - TC menetapkan enam entri sebagai seluruh isi Changelog Custom Principal dan satu entri sebagai isi Changelog Distributor. Changelog adalah audit trail permanen (S-12), sehingga asersi ini bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - TC-AC-PF-496 tidak menyebut kolom lain entri `Plan Distributor Satu` selain Action dan Plan Name; spec hanya mengasersi keduanya.
