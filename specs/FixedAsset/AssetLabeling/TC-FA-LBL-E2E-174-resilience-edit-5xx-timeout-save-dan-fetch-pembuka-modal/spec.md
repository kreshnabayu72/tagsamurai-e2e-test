---
id: TC-FA-LBL-E2E-174-resilience-edit-5xx-timeout-save-dan-fetch-pembuka-modal
title: "Resilience Edit: 5xx dan Timeout pada Save dan Fetch Pembuka Modal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-141
  - TC-FA-LBL-142
  - TC-FA-LBL-143
  - TC-FA-LBL-144
coverage:
  web: automated
---

# Resilience Edit: 5xx dan Timeout pada Save dan Fetch Pembuka Modal

## Prerequisites

- Mode: FE+BE. Backend nyata dengan `Spectra.intercept()` untuk memaksa respons Save 5xx dan timeout serta fetch pembuka modal Edit 5xx dan timeout; asersi atas state backend (nama tersimpan tidak berubah).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-174`):
  - `Edit Target 141 {runId}-174` (TC-FA-LBL-141); nama yang dicoba `Fail Edit 141 {runId}-174` (tidak tersimpan)
  - `Edit Target 142 {runId}-174` (TC-FA-LBL-142); nama yang dicoba `Timeout Edit 142 {runId}-174` (tidak tersimpan)
  - `Edit Target 143 {runId}-174` (TC-FA-LBL-143)
  - `Edit Target 144 {runId}-174` (TC-FA-LBL-144)
- Fixture `fixtures/asset-labeling.json` (disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx atau timeout (endpoint ditentukan tim FE dan tidak ditulis di TC); intercept dilepas segera sesudah pemicu selesai (S-09) dan hook `after` melepasnya bila spec gagal di tengah. Fixture BE untuk seeding, membaca nama tersimpan label, dan membersihkan label.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed dan label yang dibuat spec (nama bersuffix `{runId}-174`, termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh. Entri log bersifat permanen dan tidak dihapus.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-141: Edit gagal 5xx: modal tetap terbuka dan input dipertahankan

1. Ketik Search `Edit Target 141 {runId}-174`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 141 {runId}-174`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Fail Edit 141 {runId}-174`
4. Paksa respons Save 5xx (`Spectra.intercept()`)
5. Klik `[Save]`
6. Verifikasi toast error `Error, failed to update label.`
7. Verifikasi modal Edit Label tetap terbuka
8. Verifikasi Label Name `Fail Edit 141 {runId}-174` dipertahankan
9. Verifikasi `[Save]` berstatus enabled kembali
10. Verifikasi nama tersimpan label tetap `Edit Target 141 {runId}-174` (fixture BE)
11. Lepas intercept
12. Klik `✕` pada header modal
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`

### TC-FA-LBL-142: Edit timeout: toast koneksi dan input dipertahankan

15. Ganti isi kotak search dengan `Edit Target 142 {runId}-174`, tekan Enter
16. Klik `⋯` pada baris `Edit Target 142 {runId}-174`, lalu klik `Edit`
17. Ganti isi Label Name dengan `Timeout Edit 142 {runId}-174`
18. Paksa request Save timeout (`Spectra.intercept()`)
19. Klik `[Save]`
20. Verifikasi toast error `Connection problem. Please try again.`
21. Verifikasi modal Edit Label tetap terbuka
22. Verifikasi Label Name `Timeout Edit 142 {runId}-174` dipertahankan
23. Verifikasi `[Save]` berstatus enabled kembali
24. Lepas intercept
25. Klik `✕` pada header modal
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`

### TC-FA-LBL-143: Fetch pembuka modal Edit gagal 5xx: modal tidak dibuka

28. Ganti isi kotak search dengan `Edit Target 143 {runId}-174`, tekan Enter
29. Tutup toast error sebelumnya
30. Paksa fetch data label gagal 5xx (`Spectra.intercept()`)
31. Klik `⋯` pada baris `Edit Target 143 {runId}-174`, lalu klik `Edit`
32. Verifikasi Popup Edit Label tidak dibuka
33. Verifikasi toast error `Error, failed to update label.`
34. Lepas intercept

### TC-FA-LBL-144: Fetch pembuka modal Edit timeout: modal tidak dibuka

35. Ganti isi kotak search dengan `Edit Target 144 {runId}-174`, tekan Enter
36. Tutup toast error sebelumnya
37. Paksa fetch data label timeout (`Spectra.intercept()`)
38. Klik `⋯` pada baris `Edit Target 144 {runId}-174`, lalu klik `Edit`
39. Verifikasi Popup Edit Label tidak dibuka
40. Verifikasi toast error `Connection problem. Please try again.`
41. Lepas intercept

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): Search untuk menemukan baris label target; menutup toast error sebelumnya supaya toast bersama teks yang berulang dapat diasersi lagi (R-12); melepas intercept (S-09); menutup modal dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Pembagian TC lintas spec: resilience Create (TC-FA-LBL-88 dan 89) ada di spec 136; resilience Delete dan Bulk Delete di spec 137 dan 138.
- Spec ini di atas smell (41 langkah) tetapi semua blok satu kelas harness (b, fault injection), tiap blok memakai label dan intercept sendiri dan berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LBL-141 sampai 144: Post Condition tidak ada. TC-FA-LBL-141 Expected "data tidak berubah" tidak menyebut tempat pengamatan; spec memakai nama tersimpan lewat fixture BE.
  - TC-FA-LBL-142 dan 144 tidak menyebut berapa lama timeout; spec memakai `Spectra.intercept()` untuk simulasi timeout (disediakan tim FE).
