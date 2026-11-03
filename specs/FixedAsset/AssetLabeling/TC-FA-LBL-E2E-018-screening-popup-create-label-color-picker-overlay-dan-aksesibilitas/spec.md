---
id: TC-FA-LBL-E2E-018-screening-popup-create-label-color-picker-overlay-dan-aksesibilitas
title: "Screening Popup Create Label, Color Picker Overlay, dan Palet Preset (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-45
  - TC-FA-LBL-46
  - TC-FA-LBL-47
  - TC-FA-LBL-48
  - TC-FA-LBL-504
coverage:
  web: automated
---

# Screening Popup Create Label, Color Picker Overlay, dan Palet Preset (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Data Pre-setup #12: label `High Priority` (`#EF4444`) sudah ada di katalog Company Alpha; dipakai hanya untuk memunculkan pesan duplikat pada TC-FA-LBL-46 dan tidak diubah.
- Data Pre-setup #33 (Palet Preset Color Picker, 16 swatch grid 4x4 menurut PRD §4.3), urutan baris demi baris:

| Baris | Kolom | Hex |
|---|---|---|
| 1 | 1 | `#EF4444` |
| 1 | 2 | `#F97316` |
| 1 | 3 | `#F59E0B` |
| 1 | 4 | `#EAB308` |
| 2 | 1 | `#84CC16` |
| 2 | 2 | `#22C55E` |
| 2 | 3 | `#10B981` |
| 2 | 4 | `#14B8A6` |
| 3 | 1 | `#06B6D4` |
| 3 | 2 | `#0EA5E9` |
| 3 | 3 | `#3B82F6` |
| 3 | 4 | `#6366F1` |
| 4 | 1 | `#8B5CF6` |
| 4 | 2 | `#D946EF` |
| 4 | 3 | `#EC4899` |
| 4 | 4 | `#64748B` |

- Spec ini tidak membuat atau menyimpan label; tidak ada cleanup data. Kemampuan teknis: membaca atribut ARIA elemen (`aria-required`, `aria-describedby`) dan memantau fokus keyboard.

## Test Steps

### TC-FA-LBL-45: Screening Popup Create Label (3 zona)

1. Klik `[+ Label]`
2. Verifikasi Zona Header: Title `Create Label` dan tombol Close `[✕]` tampil
3. Verifikasi Zona Body: Label Name `*` Required dengan placeholder `Enter label name`
4. Verifikasi Zona Body: Color `*` Required dengan Swatch Trigger berupa lingkaran warna `#3B82F6`
5. Verifikasi Zona Body: caption `Live Preview` tampil
6. Verifikasi Zona Body: chip badge Live Preview berlatar `#3B82F6` dengan teks kontras
7. Verifikasi Zona Footer baris 1: checkbox `Stay on this form after submitting` tidak tercentang
8. Verifikasi Zona Footer baris 1: checkbox `Stay on this form after submitting` rata kanan
9. Verifikasi Zona Footer baris 2: `[Clear Field]` (Text, Primary) dan `[Submit]` (Filled, Success) rata kanan
10. Verifikasi `[Submit]` berstatus disabled karena Label Name kosong
11. Verifikasi tidak ada tombol `[Cancel]`
12. Verifikasi modal berukuran `sm`

### TC-FA-LBL-504: Color Swatch Trigger: state Hover dan Active/Open

13. Hover Swatch Trigger Color
14. Verifikasi Swatch Trigger menampilkan glow bayangan halus
15. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
16. Verifikasi Swatch Trigger menampilkan ring border fokus biru selama overlay terbuka

### TC-FA-LBL-47: Warna default form Create adalah #3B82F6 pada Swatch Trigger, kolom Hex, dan Live Preview

17. Verifikasi Swatch Trigger berlatar `#3B82F6`
18. Verifikasi kolom Hex menampilkan `#3B82F6`
19. Verifikasi Live Preview berlatar `#3B82F6`
20. Verifikasi `#3B82F6` adalah salah satu dari 16 swatch preset di grid

### TC-FA-LBL-48: Screening Color Picker Overlay: grid 4x4, kanvas kustom, dan kolom Hex

21. Verifikasi overlay menampilkan grid 4x4 berisi 16 swatch preset berbentuk lingkaran dengan urutan warna sesuai Palet Preset PRD §4.3 (Pre-setup #33)
22. Verifikasi overlay menampilkan area kanvas spektrum warna
23. Verifikasi overlay menampilkan kolom Hex berisi `#3B82F6`
24. Verifikasi modal Create Label tetap tampil di belakang overlay

### TC-FA-LBL-46: Accessibility Popup Create Label: aria-required, aria-describedby, focus trap, dan Esc

25. Klik Swatch Trigger Color untuk menutup overlay
26. Verifikasi field Label Name memiliki `aria-required` bernilai true
27. Verifikasi field Color memiliki `aria-required` bernilai true
28. Ketik `High Priority` di Label Name lalu tunggu pesan duplikat
29. Verifikasi setelah pesan `Label name already exists` tampil, Label Name memiliki `aria-describedby` yang menunjuk pesan error itu
30. Tekan Tab berulang sampai fokus berputar di dalam modal
31. Verifikasi fokus keyboard tetap terjebak di dalam modal (focus trapped)
32. Kosongkan Label Name sehingga form bersih, lalu tekan Esc
33. Verifikasi Esc pada form bersih menutup modal

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan modal dipakai TC-FA-LBL-45, 504, 47, 48, dan 46 (prinsip 6); modal dibuka satu kali dan ditutup satu kali (Esc pada form bersih, langkah akhir). Urutan TC di spec: 45, 504, 47, 48, 46 supaya overlay yang dibuka pada TC-FA-LBL-504 dipakai bersama dan TC-FA-LBL-46 yang menutup modal ada di akhir.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 25 (menutup overlay sebelum TC-FA-LBL-46 memeriksa atribut field).
- Kolom Hex pada TC-FA-LBL-47 butir b dan TC-FA-LBL-48 butir c sama-sama `#3B82F6`; keduanya tetap punya `Verifikasi` sendiri (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-46 Expected c tidak menyebut cara mengamati focus trap; spec memakai Tab berulang seperti langkah TC.
  - TC-FA-LBL-504 berprioritas P3 sedangkan spec ini berprioritas tertinggi dari TC sumber (P0).
