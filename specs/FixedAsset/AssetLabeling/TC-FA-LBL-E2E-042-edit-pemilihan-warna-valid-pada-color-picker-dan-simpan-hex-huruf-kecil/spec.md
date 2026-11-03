---
id: TC-FA-LBL-E2E-042-edit-pemilihan-warna-valid-pada-color-picker-dan-simpan-hex-huruf-kecil
title: "Edit: Pemilihan Warna Valid pada Color Picker dan Simpan Hex Huruf Kecil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-129
  - TC-FA-LBL-130
  - TC-FA-LBL-131
  - TC-FA-LBL-489
coverage:
  web: automated
---

# Edit: Pemilihan Warna Valid pada Color Picker dan Simpan Hex Huruf Kecil

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-042`):
  - `Edit Target 489 {runId}-042` (satu label seed untuk keempat TC; TC-FA-LBL-129 menyimpan warna di akhir)
- Data Pre-setup: Palet Preset Color Picker (Pre-setup #33), 16 swatch grid 4x4 sesuai PRD §4.3; spec memakai swatch baris 4 kolom 4.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.hex5Digit` | `#12345` |
  | `Fixture.assetLabeling.hexValid` | `#10B981` |
  | `Fixture.assetLabeling.hexKecil` | `#1e3a8a` |
  | `Fixture.assetLabeling.hexKapital` | `#1E3A8A` |
  | `Fixture.assetLabeling.swatchBaris4Kolom4` | `#64748B` (Pre-setup #33, baris 4 kolom 4) |

- Kemampuan teknis: mengetik ke kolom Hex, mengklik swatch preset, mengklik satu titik kanvas Color Picker, dan membaca kode Hex sesudahnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 489 {runId}-042`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 489 {runId}-042`, lalu klik `Edit`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay

### TC-FA-LBL-489: Edit: setelah kode hex tidak valid, mengetik kode valid menghapus error dan mengaktifkan Save

4. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hex5Digit`
5. Verifikasi inline error `Invalid color format` tampil
6. Verifikasi `[Save]` berstatus disabled
7. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
8. Verifikasi Live Preview berlatar `Fixture.assetLabeling.hexValid`
9. Verifikasi `[Save]` berstatus enabled
10. Verifikasi inline error `Invalid color format` hilang

### TC-FA-LBL-130: Edit: memilih swatch preset dan titik kanvas memperbarui Hex, Swatch Trigger, dan Live Preview

11. Klik swatch baris 4 kolom 4
12. Verifikasi kolom Hex menampilkan `Fixture.assetLabeling.swatchBaris4Kolom4`
13. Verifikasi Swatch Trigger dan Live Preview berlatar warna yang sama dengan kolom Hex dalam format `#RRGGBB` kapital
14. Verifikasi overlay tetap terbuka
15. Klik satu titik kanvas
16. Verifikasi kolom Hex berisi kode titik kanvas
17. Verifikasi Swatch Trigger dan Live Preview berlatar warna yang sama dengan kolom Hex dalam format `#RRGGBB` kapital
18. Verifikasi overlay tetap terbuka

### TC-FA-LBL-131: Edit: Escape menutup overlay tanpa menutup modal Edit

19. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
20. Tekan Escape
21. Verifikasi overlay tertutup
22. Verifikasi modal Edit Label tetap terbuka
23. Verifikasi Live Preview tetap berlatar `Fixture.assetLabeling.hexValid`

### TC-FA-LBL-129: Edit: kode hex huruf kecil ditampilkan kapital dan disimpan kapital

24. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
25. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexKecil`
26. Verifikasi kolom Hex menampilkan `Fixture.assetLabeling.hexKapital`
27. Klik `[Save]`
28. Verifikasi toast `Success, label has been updated.`
29. Verifikasi kolom Color Hex baris tersebut menampilkan `Fixture.assetLabeling.hexKapital`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-489 dan TC-FA-LBL-131 (tanpa Save) mendahului TC-FA-LBL-129 yang menyimpan warna. TC-FA-LBL-130 ditaruh sesudah TC-FA-LBL-489 supaya warna sebelum TC-FA-LBL-131 berbeda dari `Fixture.assetLabeling.hexValid` dan asersi Live Preview TC-FA-LBL-131 bermakna. Keempat TC memakai satu pembukaan modal; overlay dibuka pada langkah 3, 24 (kedua kali karena Escape pada TC-FA-LBL-131 menutupnya).
- Seeding minimal (S-11): Precondition "Label seed `Edit Target <nomor TC>`" tiap TC terpenuhi oleh satu label seed yang sama (Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0).
- Temuan untuk QA:
  - TC-FA-LBL-489 langkah 3 hanya berbunyi "Ketik `#12345` di kolom Hex" tanpa mengosongkan kolom; TC-FA-LBL-125 sampai 128 menulis "Kosongkan kolom Hex lalu ketik". Spec mengosongkan kolom lebih dulu agar konsisten.
  - TC-FA-LBL-130 menyebut "kode titik kanvas" tanpa nilai; spec membaca kode dari kolom Hex sesudah klik kanvas dan mengasersi formatnya, bukan nilai tertentu.
