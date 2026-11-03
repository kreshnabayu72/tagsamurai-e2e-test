---
id: TC-FA-LBL-E2E-165-filter-labels-list-opsi-tanpa-nilai-kosong-dan-indikator-titik
title: "Filter Labels List: Opsi Tanpa Nilai Kosong dan Indikator Titik"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-236
coverage:
  web: automated
---

# Filter Labels List: Opsi Tanpa Nilai Kosong dan Indikator Titik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.akun.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Modified By |
  |---|---|
  | `High Priority` | `Sarah J` |
  | `Finance Department` | `David K` |
  | `Audit Ready` | `Sarah J` |
  | `Executive Asset` | `Michael W` |
  | `Maintenance Due` | `David K` |
  | `Seasonal Event` | `Michael W` |
  | `Night Shift` | `Sarah J` |
  | `Warehouse Priority` | `Sarah J` |
  | `Field Kit` | `David K` |

- Data Dinamis: tidak ada. Spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-236: Opsi filter tidak memuat nilai kosong dan indikator titik muncul saat filter ter-Apply

1. Klik icon Filter di Table Tools
2. Buka dropdown `Modified By`
3. Verifikasi dropdown `Modified By` memuat opsi `Sarah J`, `David K`, dan `Michael W`
4. Verifikasi dropdown tidak memiliki opsi kosong atau `—`
5. Pilih `Sarah J` di dropdown `Modified By`
6. Klik `[Apply]`
7. Verifikasi badge titik muncul di icon Filter saat panel terbuka
8. Tutup panel: klik area di luar panel
9. Verifikasi badge titik muncul di icon Filter saat panel tertutup
10. Klik icon Filter di Table Tools
11. Klik `[Clear Field]`, lalu klik `[Apply]`
12. Verifikasi badge titik hilang dari icon Filter

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah 8 menutup panel agar badge titik diamati pada kedua keadaan (Expected b TC-FA-LBL-236).
- Pembagian TC lintas spec: TC-FA-LBL-232 sampai TC-FA-LBL-235 ada di spec 064.
- Temuan untuk QA:
  - TC tidak menyatakan apakah `[Apply]` menutup Filter Panel; spec mengikuti urutan TC-FA-LBL-235 dan TC-FA-LBL-236 yang menyiratkan panel tetap terbuka sesudah Apply (opsi tambahan dipilih langsung sesudah Apply; panel ditutup lalu dibuka lagi) dan menutup panel lewat klik area di luar panel.
