---
id: TC-FA-LBL-E2E-019-screening-popup-create-label-palet-preset-16-swatch
title: "Screening Popup Create Label, Color Picker Overlay, dan Palet Preset (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-510
coverage:
  web: automated
---

# Screening Popup Create Label, Color Picker Overlay, dan Palet Preset (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
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

- Spec ini tidak membuat atau menyimpan label; tidak ada cleanup data.

## Test Steps

### TC-FA-LBL-510: Palet Preset menampilkan 16 swatch sesuai nilai dan urutan di PRD

1. Klik `[+ Label]`
2. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
3. Verifikasi grid 4x4 berisi tepat 16 swatch tanpa duplikat
4. Verifikasi warna tiap swatch dari baris 1 kolom 1 sampai baris 4 kolom 4 sama dengan tabel Palet Preset (Pre-setup #33)
5. Verifikasi swatch baris 3 kolom 3 (`#3B82F6`) adalah warna default Swatch Trigger saat modal Create dibuka
6. Tekan Esc untuk menutup overlay
7. Klik icon `[✕]` untuk menutup modal

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 6 dan 7 (menutup overlay lalu modal; form bersih sehingga tidak ada dialog `Unsaved Changes`).
- Klik tiap swatch preset dan pengisian kolom Hex ada di spec 159 (TC-FA-LBL-49); spec ini hanya membaca nilai dan urutan swatch.
