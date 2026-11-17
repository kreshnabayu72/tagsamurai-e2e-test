---
id: TC-FA-TDC-E2E-228-aksesibilitas-fokus-ter-trap-modal-versions-dan-popup-changelog
title: "Aksesibilitas Fokus Ter-trap Modal Versions dan Popup Changelog"
layer: ui-e2e
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-922
  - TC-FA-TDC-923
sourceRules: ["§4.5#b2", "§4.5#b1", "FATDC-LOGIC-04ae"]
smoke: []
dependsOn: []
trace:
  "§4.5#b2": [3, 9]
  "§4.5#b1": [5, 11]
  "FATDC-LOGIC-04ae": 9
coverage:
  web: automated
---

# Aksesibilitas Fokus Ter-trap Modal Versions dan Popup Changelog

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; BLD-NP memiliki versi Scheduled sehingga modal Versions memuat baris Scheduled dengan tombol `Cancel`. Tidak ada data berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: menekan `Tab` berulang dan `Esc`; mengamati posisi fokus di dalam modal dan popup.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-923: Fokus ter-trap di Popup Changelog dan Esc menutup

1. Klik ikon Changelog di toolbar
2. Tekan Tab berulang sampai fokus berputar
3. Verifikasi fokus berputar di antara elemen interaktif Popup Changelog tanpa keluar ke elemen halaman di belakangnya
4. Tekan Esc
5. Verifikasi Popup Changelog tertutup

### TC-FA-TDC-922: Fokus ter-trap di modal Versions dan Esc menutup

6. Klik link Class Code `BLD-NP`
7. Klik `View versions`
8. Tekan Tab berulang sampai fokus berputar
9. Verifikasi fokus berputar di antara elemen interaktif modal Versions (ikon ✕ dan tombol `Cancel` pada baris Scheduled) tanpa keluar ke Drawer atau halaman di belakangnya
10. Tekan Esc
11. Verifikasi modal Versions tertutup
12. Klik `[×]` pada header Drawer

## Notes

- Urutan TC dalam spec: TC-FA-TDC-923, lalu TC-FA-TDC-922. TC-FA-TDC-922 membuka Drawer dan ditutup di akhir spec (prinsip 6 bagian 3).
- Langkah penghubung (S-03): langkah 12 (menutup Drawer yang tidak diubah; tidak ada dialog `Unsaved Changes`).
- Temuan untuk QA:
  - TC-FA-TDC-922 dan 923 menyebut "Tab berulang sampai fokus berputar" tanpa menyebut daftar elemen interaktif Popup Changelog; spec mengasersi hanya yang tertulis.
  - Email akun Total Control tidak tertulis di TC.
