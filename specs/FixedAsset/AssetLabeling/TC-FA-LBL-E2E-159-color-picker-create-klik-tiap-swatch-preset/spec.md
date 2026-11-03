---
id: TC-FA-LBL-E2E-159-color-picker-create-klik-tiap-swatch-preset
title: "Color Picker Create: Klik Tiap Swatch Preset Menyetel Hex, Swatch Trigger, dan Live Preview"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-49
coverage:
  web: automated
---

# Color Picker Create: Klik Tiap Swatch Preset Menyetel Hex, Swatch Trigger, dan Live Preview

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Tabel Palet Preset (Pre-setup #33, PRD §4.3), urutan baris demi baris; dipakai perulangan langkah 3 sampai 6:

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

### TC-FA-LBL-49: Klik tiap swatch preset menyetel kolom Hex, Swatch Trigger, dan Live Preview ke warna yang sama

1. Klik `[+ Label]`
2. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
3. Untuk setiap baris tabel Palet Preset (langkah 3 sampai 6): klik swatch pada Baris dan Kolom baris tabel itu
4. Verifikasi kolom Hex menampilkan kode `#RRGGBB` kapital sesuai kolom Hex pada baris tabel itu
5. Verifikasi Swatch Trigger dan Live Preview berlatar warna yang sama dengan kolom Hex
6. Verifikasi overlay tetap terbuka
7. Tekan Esc untuk menutup overlay
8. Klik icon `[✕]`
9. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
10. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 3 sampai 6 diulang untuk 16 baris tabel Palet Preset di `## Prerequisites` (satu iterasi = satu swatch, tanpa langkah bersyarat; `Verifikasi` tetap satu per klausa Expected). Dihitung dengan ekspansi, spec ini ±70 langkah; alasan pertahanan: seluruh langkah satu topik (satu palet, satu modal, satu overlay yang tetap terbuka sesudah tiap klik) dan tiap iterasi berdiri sendiri.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 7 dan 10 (menutup overlay dan modal; form dirty karena warna terakhir `#64748B`, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
