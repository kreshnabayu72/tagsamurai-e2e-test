---
id: TC-AC-PF-E2E-019-aksesibilitas-aria-required-form-edit-custom-plan-dan-edit-default-plan
title: "Aksesibilitas: Field Wajib Form Edit Custom Plan dan Edit Default Plan Memiliki aria-required"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-789
coverage:
  web: automated
---

# Aksesibilitas: Field Wajib Form Edit Custom Plan dan Edit Default Plan Memiliki aria-required

## Prerequisites

- Mode: FE+BE (hanya membuka form dan membaca atribut; TC bertanda UI Only, tanpa intercept dan tanpa perubahan data).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21): custom plan `Growth Tier` v20 dan default plan `Growth` v5. Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal `Growth Tier` dan `Growth` dipakai sebagai target buka form Edit; spec membuka form tanpa mengubah atau menyimpan apa pun sehingga data dan Last Updated tidak berubah. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Field wajib form Edit Custom Plan dan form Edit Default Plan (20 field, daftar sama, Data Uji TC-AC-PF-789), dipakai langkah 2 dan 5: Plan Name, Product, Asset Name cap, Group count, Group hierarchy depth, Category count, Category hierarchy depth, Scheduled reports, API call quota, Asset ID Configuration, License allocation per group, Open API, SAMP & Document Center, Custom Report Builder, Approval Workflow, Borrowing, Assignment, Transfer, Disposal, Accounting & Depreciation.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: pembacaan atribut ARIA elemen form (accessibility tree atau atribut DOM), fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-789: Accessibility form Edit Custom Plan dan Edit Default Plan: field wajib memiliki aria-required

1. Klik tab Custom, buka Overlay Row Action `Growth Tier`, klik `Edit`
2. Untuk setiap baris tabel "Field wajib form Edit Custom Plan dan form Edit Default Plan" pada Prerequisites: Verifikasi atribut aria-required field tersebut bernilai "true" pada form Edit Custom Plan
3. Tekan Esc tanpa mengubah apa pun
4. Klik tab Default sub-tab Active, buka Overlay Row Action `Growth`, klik `Edit`
5. Untuk setiap baris tabel "Field wajib form Edit Custom Plan dan form Edit Default Plan" pada Prerequisites: Verifikasi atribut aria-required field tersebut bernilai "true" pada form Edit Default Plan
6. Tekan Esc tanpa mengubah apa pun

## Notes

- Langkah penghubung (S-03): klik tab Custom dan tab Default pada langkah 1 dan 4 mengarahkan layar ke tab yang disyaratkan TC; langkah 6 menutup form Edit yang tidak diubah (tanpa dialog `Unsaved Changes` karena tidak ada perubahan).
- Langkah 2 dan 5 diulang untuk 20 baris tabel Prerequisites dengan satu `Verifikasi` per field per form (bagian 8b butir 7); dengan ekspansi spec ini 44 langkah.
- Alasan di atas sekitar 35 langkah (44 langkah): Expected TC-AC-PF-789 memuat 20 butir aria-required yang masing-masing berlaku pada dua form (Edit Custom Plan dan Edit Default Plan), sehingga satu field menghasilkan dua `Verifikasi` (S-01); kedua form memakai daftar field yang sama, satu kelas harness, dan satu TC sumber, sehingga tidak ada pemisah nyata.
- Temuan untuk QA:
  - TC-AC-PF-789: langkah 3 TC berbunyi "Tekan Esc tanpa mengubah apa pun" lalu membuka tab Default; spec mengikuti urutan itu. Expected hanya menyebut aria-required `true` pada kedua form tanpa memerinci perbedaan field antar form.
