---
id: TC-FA-LIC-E2E-001-screening-halaman-license-plan-paid-breadcrumb-tabs-bar
title: "Screening Halaman License Plan Paid: Breadcrumb, Tabs Bar, dan Route Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-1
  - TC-FA-LIC-2
  - TC-FA-LIC-587
coverage:
  web: automated
---

# Screening Halaman License Plan Paid: Breadcrumb, Tabs Bar, dan Route Tab

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: kuota dan hierarki #12, riwayat #13, sesi aktif #14; hanya dibaca, tidak diubah. Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Kemampuan teknis: membuka route License tanpa segmen tab dan tombol Back browser (kemampuan browser standar).
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-1: Breadcrumb per tab tanpa Page Title

1. Klik menu License pada sidebar
2. Verifikasi Breadcrumb `License > All License`
3. Verifikasi segmen `All License` pada Breadcrumb tidak dapat diklik
4. Verifikasi tidak ada Page Title Header terpisah di bawah Breadcrumb
5. Verifikasi tombol Guided Tooltip `[?]` tampil di sebelah kanan Breadcrumb

### TC-FA-LIC-2: Tabs Bar plan Paid, urutan tab dan tab aktif default

6. Verifikasi Tabs: `All License | Allocation Quota | Concurrent User`
7. Verifikasi Tab `All License` berstatus aktif
8. Klik Tab `Allocation Quota`
9. Verifikasi Breadcrumb `License > Allocation Quota`
10. Klik Tab `Concurrent User`
11. Verifikasi Breadcrumb `License > Concurrent User`
12. Verifikasi ketiga tab berada pada satu halaman License (Tabs Bar tetap tampil dengan ketiga tab)
13. Verifikasi tiap tab memiliki route sendiri (route halaman Tab `Concurrent User` berbeda dari route Tab `Allocation Quota` dan Tab `All License`)

### TC-FA-LIC-587: Pindah tab memperbarui breadcrumb dan route

14. Klik menu License pada sidebar
15. Verifikasi Breadcrumb `License > All License`
16. Klik Tab `Concurrent User`
17. Verifikasi Breadcrumb `License > Concurrent User`
18. Klik Tab `Allocation Quota`
19. Verifikasi Breadcrumb `License > Allocation Quota`
20. Tekan tombol Back browser
21. Verifikasi Breadcrumb `License > Concurrent User`
22. Tekan tombol Back browser
23. Verifikasi Breadcrumb `License > All License`
24. Buka route License tanpa segmen tab
25. Verifikasi halaman di-redirect ke Tab `All License`
26. Verifikasi Breadcrumb `License > All License`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-1, 2, 587). TC-FA-LIC-83, 84, dan 439 (guard struktural tabel) ada di spec 129. Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung: tidak ada langkah penghubung tanpa dasar TC. Langkah 1 dan 14 (klik menu License) adalah langkah TC-1 dan TC-587; pembukaan License oleh hook `beforeEach` suite tidak diulang di langkah lain. Langkah 1 TC-2 ("Buka License melalui sidebar") sudah terpenuhi pembukaan pada langkah 1.
- Klausa "tiap pindah tab menambah entri history browser" (TC-587 butir b) teramati lewat langkah 20 sampai 23: Back pertama kembali ke `License > Concurrent User` dan Back kedua ke `License > All License`; tidak ada langkah observasi terpisah di TC.
- Temuan untuk QA:
  - TC-1 menyebut Precondition "User berada di Fixed Asset > Dashboard" sedangkan hook `beforeEach` suite membuka License; langkah 1 tetap mengklik menu License sebagai objek uji navigasi.
  - TC-2 butir c memuat tiga klausa (satu halaman, Breadcrumb mengikuti tab, route sendiri) tanpa nilai route; langkah 13 membandingkan route antar tab, nilai route tidak tertulis di TC.
