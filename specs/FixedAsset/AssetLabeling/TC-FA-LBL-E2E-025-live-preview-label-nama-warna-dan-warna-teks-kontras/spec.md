---
id: TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras
title: "Live Preview Label: Nama, Warna, dan Warna Teks Kontras"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-63
  - TC-FA-LBL-64
  - TC-FA-LBL-65
  - TC-FA-LBL-66
  - TC-FA-LBL-67
  - TC-FA-LBL-68
coverage:
  web: automated
---

# Live Preview Label: Nama, Warna, dan Warna Teks Kontras

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Nama120 untuk TC-FA-LBL-68 (hanya diketik, tidak disimpan): kata `Alpha` dipisah spasi tunggal dan ditutup akhiran unik per run `{runId}-025` (`{runId}` hanya digit), disusun supaya total tepat 120 karakter termasuk akhiran (nilai dihitung di script).
- Palet Preset (Pre-setup #33): swatch baris 2 kolom 2 bernilai `#22C55E`.
- Spec ini tidak membuat atau menyimpan label; tidak ada cleanup data. Kemampuan teknis: membaca warna teks terkomputasi dan warna latar chip Live Preview.

## Test Steps

1. Klik `[+ Label]`

### TC-FA-LBL-63: Live Preview memperbarui chip secara instan saat nama diketik dan warna diubah

2. Ketik `Support Team` di Label Name
3. Verifikasi chip Live Preview menampilkan teks `Support Team` berlatar `#3B82F6`
4. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
5. Klik swatch baris 2 kolom 2
6. Verifikasi latar chip Live Preview berubah ke warna swatch yang diklik (`#22C55E`)
7. Verifikasi teks chip tetap `Support Team`

### TC-FA-LBL-64: Warna teks Live Preview untuk latar #FFFFFF

8. Ganti isi Label Name dengan `Contrast Check`
9. Kosongkan kolom Hex lalu ketik `#FFFFFF`
10. Verifikasi teks chip Live Preview berwarna hitam `#000000` karena rasio kontras hitam terhadap latar putih lebih tinggi daripada putih

### TC-FA-LBL-65: Warna teks Live Preview untuk latar #000000

11. Kosongkan kolom Hex lalu ketik `#000000`
12. Verifikasi teks chip Live Preview berwarna putih `#FFFFFF` karena rasio kontras putih terhadap latar hitam lebih tinggi daripada hitam

### TC-FA-LBL-66: Warna teks Live Preview untuk latar #1E3A8A

13. Kosongkan kolom Hex lalu ketik `#1E3A8A`
14. Verifikasi teks chip Live Preview berwarna putih `#FFFFFF` karena rasio kontras putih terhadap latar `#1E3A8A` lebih tinggi daripada hitam

### TC-FA-LBL-67: Warna teks Live Preview untuk latar #3B82F6

15. Kosongkan kolom Hex lalu ketik `#3B82F6`
16. Verifikasi teks chip Live Preview berwarna hitam `#000000` karena rasio kontras hitam terhadap latar `#3B82F6` lebih tinggi daripada putih

### TC-FA-LBL-68: Live Preview menampilkan nama 120 karakter penuh

17. Tekan Esc untuk menutup overlay
18. Ganti isi Label Name dengan Nama120
19. Verifikasi chip Live Preview menampilkan Nama120 (120 karakter termasuk akhiran `{runId}-025`) penuh tanpa penggalan `..`
20. Klik icon `[✕]`
21. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
22. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan modal dan satu pembukaan overlay dipakai TC-FA-LBL-63 sampai 67 (prinsip 6); Label Name diganti isinya dan kolom Hex dikosongkan di antara kasus.
- TC-FA-LBL-64 sampai 67 memakai Label Name `Contrast Check`, diganti dari `Support Team` pada langkah pertama TC-FA-LBL-64; nama tidak disimpan.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 17 (menutup overlay sebelum TC-FA-LBL-68 mengisi nama) dan 22 (menutup modal; form dirty karena Label Name terisi, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- Warna teks diasersi dari nilai terkomputasi chip Live Preview; rasio kontras tidak dihitung ulang oleh spec.
