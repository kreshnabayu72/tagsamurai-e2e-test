---
id: TC-FA-TDC-E2E-010-aksesibilitas-fokus-ter-trap-dialog-konfirmasi-d-01-d-03-d-06-dan-campuran-d-14-d-15
title: "Aksesibilitas Fokus Ter-trap Dialog Konfirmasi D-01, D-03, D-06 dan Dialog Campuran D-14, D-15"
layer: ui-e2e
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-916
  - TC-FA-TDC-917
sourceRules: ["D-01", "§4.5#b2", "§4.5#b1", "§4.1.1#r1", "D-03", "D-06", "D-14", "D-15"]
smoke: []
dependsOn: []
trace:
  "D-01": 3
  "§4.5#b2": [3, 8, 14, 21, 29]
  "§4.5#b1": [5, 10, 16, 23, 31]
  "§4.1.1#r1": [5, 10, 23]
  "D-03": 8
  "D-06": 14
  "D-14": 21
  "D-15": 29
coverage:
  web: automated
---

# Aksesibilitas Fokus Ter-trap Dialog Konfirmasi D-01, D-03, D-06 dan Dialog Campuran D-14, D-15

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. NB-4 Active Used By 0 (lolos aksi), NB-OLD Inactive Used By 0, NB-1 Used By 5 (diblokir oleh Used By). Semua dialog hanya dibuka lalu ditutup dengan `Esc`; tidak ada data berubah. Data Dinamis: tidak ada.
- Kemampuan teknis: menekan `Tab` berulang dan `Esc`; mengamati posisi fokus di dalam dialog; Bulk Action Bar.
- State global yang diubah: seleksi baris (dibersihkan oleh langkah eksplisit di spec ini).

## Test Steps

### TC-FA-TDC-916: Fokus ter-trap di dialog konfirmasi D-01, D-03, dan D-06 dan Esc menutup

1. Klik toggle `Active` baris NB-4 sehingga dialog D-01 muncul
2. Tekan Tab berulang sampai fokus berputar
3. Verifikasi D-01: fokus berputar di dalam dialog (`[Cancel]`, `[Deactivate]`) tanpa keluar ke halaman
4. Tekan Esc
5. Verifikasi D-01 tertutup dan toggle NB-4 tetap On (data tidak berubah)
6. Klik toggle `Active` baris NB-OLD sehingga dialog D-03 muncul
7. Tekan Tab berulang
8. Verifikasi D-03: fokus berputar di dalam dialog (`[Cancel]`, `[Activate]`) tanpa keluar ke halaman
9. Tekan Esc
10. Verifikasi D-03 tertutup dan toggle NB-OLD tetap Off (data tidak berubah)
11. Klik tombol `⋯` baris NB-4
12. Klik `Delete` sehingga dialog D-06 muncul
13. Tekan Tab berulang
14. Verifikasi D-06: fokus berputar di dalam dialog (`[Cancel]`, `[Delete]`) tanpa keluar ke halaman
15. Tekan Esc
16. Verifikasi D-06 tertutup dan baris NB-4 masih tampil (data tidak berubah)

### TC-FA-TDC-917: Fokus ter-trap di dialog campuran D-14 dan D-15 dan Esc menutup

17. Centang baris NB-4
18. Centang baris NB-1
19. Klik `Deactivate` pada Bulk Action Bar sehingga dialog D-14 muncul
20. Tekan Tab berulang sampai fokus berputar
21. Verifikasi D-14: fokus berputar di dalam dialog (`[Cancel]`, `[Continue]`) tanpa keluar ke halaman
22. Tekan Esc
23. Verifikasi D-14 tertutup dan data tidak berubah (NB-4 tetap Active, NB-1 tetap Active)
24. Klik `Unselect All` pada Bulk Action Bar
25. Centang baris NB-4
26. Centang baris NB-1
27. Klik `Delete` pada Bulk Action Bar sehingga dialog D-15 muncul
28. Tekan Tab berulang
29. Verifikasi D-15: fokus berputar di dalam dialog (`[Cancel]`, `[Continue]`) tanpa keluar ke halaman
30. Tekan Esc
31. Verifikasi D-15 tertutup dan data tidak berubah (baris NB-4 dan NB-1 masih tampil)
32. Klik `Unselect All` pada Bulk Action Bar

## Notes

- Langkah penghubung (S-03): langkah 24 dan 32 (`Unselect All` membersihkan seleksi sebelum D-15 dan di akhir spec; S-09), langkah 25 dan 26 (mencentang ulang baris sebagai precondition D-15 supaya tidak mengandalkan seleksi dari Esc D-14, yang tidak disebut TC).
- Klausa "Esc menutup dialog tanpa mengubah data" pada Expected TC ditulis sebagai satu `Verifikasi` per dialog (menutup tanpa perubahan adalah satu pernyataan hasil Cancel), dengan pemeriksaan data pada baris terkait.
- Tiap dialog dibuka dari datanya sendiri (NB-4 untuk D-01, NB-OLD untuk D-03, NB-4 untuk D-06, NB-4 dan NB-1 untuk D-14 dan D-15). Tidak ada aksi yang menghapus atau mengubah data karena semua dialog dibatalkan.
- Temuan untuk QA:
  - TC-FA-TDC-917 langkah 2 menyebut "Pastikan baris NB-4 dan NB-1 tercentang" tanpa menyebut apakah seleksi bertahan setelah Esc pada D-14; spec membersihkan lalu mencentang ulang secara deterministik.
  - Nama tombol D-14 dan D-15 pada Expected (`[Cancel]`, `[Continue]`) mengikuti TC.
  - Email akun Total Control tidak tertulis di TC.
