---
id: TC-AC-PF-E2E-018-aksesibilitas-aria-required-form-create-custom-plan
title: "Aksesibilitas: Field Wajib Form Create Custom Plan Memiliki aria-required"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-787
coverage:
  web: automated
---

# Aksesibilitas: Field Wajib Form Create Custom Plan Memiliki aria-required

## Prerequisites

- Mode: FE+BE (hanya membuka form dan membaca atribut; TC bertanda UI Only, tanpa intercept dan tanpa perubahan data).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21), termasuk default plan `Growth` sebagai Template. Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal `Growth` dipakai sebagai nilai Template; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Field wajib form Create Custom Plan (21 field, Data Uji TC-AC-PF-787), dipakai langkah 3:

| No | Field |
|---|---|
| 1 | Product |
| 2 | Template |
| 3 | Plan Name |
| 4 | Asset Name cap |
| 5 | Group count |
| 6 | Group hierarchy depth |
| 7 | Category count |
| 8 | Category hierarchy depth |
| 9 | Scheduled reports |
| 10 | API call quota |
| 11 | Asset ID Configuration |
| 12 | License allocation per group |
| 13 | Open API |
| 14 | SAMP & Document Center |
| 15 | Custom Report Builder |
| 16 | Approval Workflow |
| 17 | Borrowing |
| 18 | Assignment |
| 19 | Transfer |
| 20 | Disposal |
| 21 | Accounting & Depreciation |
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: pembacaan atribut ARIA elemen form (accessibility tree atau atribut DOM), fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-787: Accessibility form Create Custom Plan: field wajib memiliki aria-required

1. Klik tab Custom, lalu klik `+ Custom Plan`
2. Pilih Product `FAMS` dan Template `Growth`
3. Untuk setiap baris tabel "Field wajib form Create Custom Plan" pada Prerequisites: Verifikasi atribut aria-required field tersebut bernilai "true"
4. Klik segmen Breadcrumb `Plans & Features`
5. Verifikasi dialog `Unsaved Changes` tampil
6. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): klik tab Custom pada langkah 1 mengarahkan layar ke tab yang disyaratkan precondition TC; langkah 4 sampai 6 menutup form dirty setelah Product dan Template dipilih (S-08, S-09).
- Langkah 3 diulang untuk 21 baris tabel Prerequisites dengan satu `Verifikasi` per field (bagian 8b butir 7); dengan ekspansi spec ini 26 langkah.
- Temuan untuk QA:
  - TC-AC-PF-787: Expected butir a sampai u hanya menyebut aria-required `true`; TC tidak menyebut apakah field Template, Asset Name cap, dan field lain yang bergantung pada pilihan Product dan Template sudah termuat saat dibaca. Spec memilih Product dan Template terlebih dahulu sesuai langkah TC.
