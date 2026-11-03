---
id: TC-FA-LBL-E2E-136-resilience-create-5xx-dan-timeout
title: "Resilience Create: 5xx dan Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-88
  - TC-FA-LBL-89
coverage:
  web: automated
---

# Resilience Create: 5xx dan Timeout

## Prerequisites

- Mode: FE+BE. Backend nyata dengan `Spectra.intercept()` untuk memaksa respons Create 5xx (TC-FA-LBL-88) dan timeout (TC-FA-LBL-89); asersi atas state backend (label tidak dibuat, label berhasil dibuat sesudah intercept dilepas).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (nama bersuffix `{runId}-136`, tanpa seed; label dibuat oleh aksi spec lewat UI):
  - `Fail Create 88 {runId}-136` (TC-FA-LBL-88; Color `Fixture.assetLabeling.hexValid`; tersimpan hanya pada percobaan kedua)
  - `Timeout Create 89 {runId}-136` (TC-FA-LBL-89; tidak tersimpan)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.hexValid` | `#10B981` |

- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx atau timeout (endpoint ditentukan tim FE dan tidak ditulis di TC); intercept dilepas segera sesudah pemicu selesai (S-09) dan hook `after` melepasnya bila spec gagal di tengah. Jeda nyata 10 detik pada TC-FA-LBL-88 (pilihan TC, di bawah batas 30 detik bagian 6) untuk memastikan toast error tidak hilang otomatis. Fixture BE untuk membaca keberadaan label dan membersihkannya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-136`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-88: Create gagal 5xx: modal tetap terbuka dan input dipertahankan

1. Klik `[+ Label]`
2. Isi Label Name `Fail Create 88 {runId}-136`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Kosongkan kolom Hex lalu ketik `Fixture.assetLabeling.hexValid`
5. Paksa respons Create 5xx (`Spectra.intercept()`)
6. Klik `[Submit]`
7. Tunggu 10 detik tanpa menutup toast
8. Verifikasi toast error `Error, failed to create label.` masih tampil (tetap tampil sampai di-dismiss manual)
9. Verifikasi modal Create Label tetap terbuka
10. Verifikasi Label Name `Fail Create 88 {runId}-136` dipertahankan
11. Verifikasi warna `Fixture.assetLabeling.hexValid` dipertahankan
12. Verifikasi `[Submit]` berstatus enabled kembali
13. Verifikasi label `Fail Create 88 {runId}-136` tidak dibuat (fixture BE)
14. Tutup toast error secara manual
15. Lepas intercept
16. Klik `[Submit]`
17. Verifikasi toast `Success, label has been created.`

### TC-FA-LBL-89: Create timeout: toast koneksi dan input dipertahankan

18. Klik `[+ Label]`
19. Isi Label Name `Timeout Create 89 {runId}-136`
20. Paksa request Create timeout (`Spectra.intercept()`)
21. Klik `[Submit]`
22. Verifikasi toast error `Connection problem. Please try again.`
23. Verifikasi modal Create Label tetap terbuka
24. Verifikasi Label Name `Timeout Create 89 {runId}-136` dipertahankan
25. Verifikasi `[Submit]` berstatus enabled kembali
26. Lepas intercept
27. Klik `✕` pada header modal
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3a (Create Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): menutup toast error secara manual dan melepas intercept (S-09); menutup modal dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Pembagian TC lintas spec: resilience Edit (TC-FA-LBL-141 sampai 144) ada di spec 174; resilience Delete dan Bulk Delete di spec 137 dan 138.
- Temuan untuk QA:
  - TC-FA-LBL-88 Post Condition ("hanya satu label tersimpan") tidak punya langkah observasi di TC; keberadaan label sesudah percobaan kedua tidak diasersi selain toast sukses. TC-FA-LBL-89 Post Condition tidak ada.
  - TC-FA-LBL-89 tidak menyebut berapa lama timeout dan cara memaksanya; spec memakai `Spectra.intercept()` untuk simulasi timeout (disediakan tim FE).
