---
id: TC-FA-TDC-E2E-009-aksesibilitas-keyboard-toggle-active-dan-fokus-popup-used-by
title: "Aksesibilitas Keyboard Toggle Active dan Fokus Popup Used By"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-34
  - TC-FA-TDC-36
  - TC-FA-TDC-366
  - TC-FA-TDC-378
sourceRules: ["§4.5#b1", "D-03", "§4.1.1#r1", "§4.5#b4", "D-01", "§4.5#b2"]
smoke: []
dependsOn: []
trace:
  "§4.5#b1": [2, 7, 27]
  "D-03": [4, 13]
  "§4.1.1#r1": [5, 8, 14, 21]
  "§4.5#b4": [10, 11, 17, 18]
  "D-01": 20
  "§4.5#b2": 25
anchor: [28]
coverage:
  web: automated
---

# Aksesibilitas Keyboard Toggle Active dan Fokus Popup Used By

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. NB-OLD Inactive dengan Used By 0; NB-4 Active dengan Used By 0; NB-1 Used By 5. Semua dialog hanya dibuka lalu dibatalkan; tidak ada data yang berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: menekan `Tab`, `Enter`, `Space`, dan `Esc` pada elemen terfokus; membaca label aksesibilitas (aria-label) dan state checked toggle; mengamati posisi fokus.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-34: Toggle Active dapat dioperasikan dengan keyboard

1. Tekan Tab sampai fokus berada pada toggle Active baris NB-OLD
2. Verifikasi fokus tampak pada toggle NB-OLD
3. Tekan Enter
4. Verifikasi dialog `Activate Tax Depreciation Class` terbuka
5. Verifikasi toggle NB-OLD tetap Off sampai Confirm
6. Tekan Esc
7. Verifikasi dialog `Activate Tax Depreciation Class` tertutup setara `[Cancel]`
8. Verifikasi toggle NB-OLD tetap Off

### TC-FA-TDC-366: Toggle Active baris Inactive dioperasikan dengan keyboard membuka dialog Activate

9. Tekan `Tab` sampai fokus berada di toggle `Active` baris NB-OLD
10. Verifikasi label aksesibilitas toggle `Active` baris NB-OLD "Active for tax depreciation class NB-OLD"
11. Verifikasi state toggle NB-OLD tidak checked (Off)
12. Tekan `Enter`
13. Verifikasi dialog "Activate Tax Depreciation Class" terbuka
14. Verifikasi toggle NB-OLD tetap Off
15. Tekan Esc

### TC-FA-TDC-378: Toggle Active baris Active dioperasikan dengan Space membuka dialog Deactivate

16. Tekan `Tab` sampai fokus berada di toggle `Active` baris NB-4
17. Verifikasi label aksesibilitas toggle `Active` baris NB-4 "Active for tax depreciation class NB-4"
18. Verifikasi state toggle NB-4 checked (On)
19. Tekan `Space`
20. Verifikasi dialog "Deactivate Tax Depreciation Class" terbuka
21. Verifikasi toggle NB-4 tetap On
22. Tekan Esc

### TC-FA-TDC-36: Fokus ter-trap di Popup Used By dan Esc menutupnya

23. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
24. Tekan Tab berulang sampai fokus berputar
25. Verifikasi fokus tetap berada di dalam Popup Used By dan tidak keluar ke elemen halaman di belakangnya
26. Tekan Esc
27. Verifikasi Popup Used By tertutup
28. Verifikasi fokus kembali ke halaman

## Notes

- Urutan TC dalam spec: TC-FA-TDC-34, 366, 378, 36. TC dialog toggle dijalankan sebelum Popup Used By.
- Langkah penghubung (S-03): langkah 15 dan 22 (`Esc` menutup dialog yang dibuka TC-FA-TDC-366 dan 378 sebelum TC berikutnya; TC tidak menyebut penutupan dialog, `Esc` setara `[Cancel]` seperti pada TC-FA-TDC-34).
- Asersi absence dan state sementara: dialog dan fokus diasersi tepat sesudah pemicunya (8b.5). `Verifikasi` langkah 14 dan 21 (toggle tetap Off dan On) didahului dialog terbuka pada langkah 13 dan 20 sebagai anchor.
- Temuan untuk QA:
  - TC-FA-TDC-36 Expected a-b tidak menyebut elemen yang menerima fokus setelah Esc selain "kembali ke halaman"; spec mengasersi hanya itu.
  - TC-FA-TDC-366 dan TC-FA-TDC-34 menguji aksi yang sama (Enter pada toggle NB-OLD) dengan Expected tumpang tindih; keduanya tetap ditulis karena tiap TC tepat satu spec.
  - Email akun Total Control tidak tertulis di TC.
