---
id: TC-FA-LBL-E2E-024-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-2
title: "Color Picker Create: Menutup Overlay (Escape, Swatch Trigger, Klik Luar) (bagian 2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-512
coverage:
  web: automated
---

# Color Picker Create: Menutup Overlay (Escape, Swatch Trigger, Klik Luar) (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Tabel "Cara menutup overlay" (dipakai perulangan langkah 4 sampai 14):

| No | Cara menutup overlay |
|---|---|
| 1 | Tekan Escape |
| 2 | Klik Swatch Trigger Color |
| 3 | Klik di luar overlay (area kosong di dalam modal) |

- Spec ini tidak membuat atau menyimpan label (submit tidak dilakukan); tidak ada cleanup data.

## Test Steps

### TC-FA-LBL-512: Menutup overlay saat kolom Hex berisi kode tidak valid membuang kode itu: Submit Enabled, V-04 hilang, warna tidak berubah

1. Klik `[+ Label]`
2. Isi Label Name `Hex Close 512`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Untuk setiap baris tabel "Cara menutup overlay" (langkah 4 sampai 14): kosongkan kolom Hex lalu ketik `#12345`
5. Verifikasi inline error `Invalid color format` tampil di dalam overlay
6. Verifikasi `[Submit]` berstatus disabled walau Label Name terisi
7. Tutup overlay dengan cara pada baris tabel itu
8. Verifikasi overlay tertutup
9. Verifikasi modal Create Label tetap terbuka
10. Klik Swatch Trigger Color untuk membuka overlay lagi
11. Verifikasi kolom Hex kembali ke warna valid terakhir `#3B82F6` (kode `#12345` dibuang)
12. Verifikasi inline error `Invalid color format` hilang
13. Verifikasi `[Submit]` kembali berstatus enabled
14. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `#3B82F6` (tidak berubah)
15. Tekan Escape untuk menutup overlay
16. Klik icon `[✕]`
17. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
18. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 4 sampai 14 diulang untuk 3 baris tabel "Cara menutup overlay" di `## Prerequisites` (Escape, klik Swatch Trigger, klik di luar overlay), sesuai langkah 9 dan 10 TC yang meminta langkah 4 dan 5 diulang untuk tiap cara. Dihitung dengan ekspansi spec ini ±40 langkah; alasan pertahanan: seluruh langkah satu TC dan satu topik (satu modal, satu overlay, satu kode tidak valid) dan tiap iterasi memeriksa hasil yang sama, jadi tidak ada bagian yang bisa dipisah tanpa memutus TC.
- Label Name diisi sekali sebelum overlay dibuka (langkah 2, urutan TC) dan tidak diisi lagi pada pengulangan.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 15 dan 18 (menutup overlay lalu modal; form dirty karena Label Name terisi, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- Pada iterasi kedua dan ketiga overlay sudah terbuka (dibuka ulang pada langkah terakhir iterasi di atasnya) dan kolom Hex berisi `#3B82F6`, sehingga kode `#12345` diketik dari keadaan yang sama.
