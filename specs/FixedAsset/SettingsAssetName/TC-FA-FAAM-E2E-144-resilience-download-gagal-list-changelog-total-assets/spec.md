---
id: TC-FA-FAAM-E2E-144-resilience-download-gagal-list-changelog-total-assets
title: "Resilience Download Gagal: Toast Error dengan Nama Berkas pada List, Changelog, dan Tab Total Assets"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-458
  - TC-FA-FAAM-498
  - TC-FA-FAAM-524
coverage:
  web: automated
---

# Resilience Download Gagal: Toast Error dengan Nama Berkas pada List, Changelog, dan Tab Total Assets

## Prerequisites

- Mode: FE+BE (backend nyata, `Spectra.intercept()` parsial untuk respons Download 5xx).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (tidak diubah spec ini; nama literal tanpa suffix karena asersi bergantung pada nama baris; `Fixture.faSettingsAssetName.baselineList`, fixture baru belum ada): client utama dengan enam Asset Name contoh (Pre-setup #10 sampai #14) dan 30 `Seed Item` (Pre-setup #15, Total Asset 0, UoM `Unit`). Baris yang dirujuk: `Dell Latitude` (Pre-setup #10, Total Asset 42; aset contoh Pre-setup #26 dengan Status beragam). Changelog berisi entri contoh PRD (Pre-setup #28).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx pada request Download List, Download Changelog, dan Download tab Total Assets (endpoint dipilih tim FE; TC tidak menyebut endpoint dan status kode untuk TC-FA-FAAM-498 dan 524, spec memakai 5xx seperti TC-FA-FAAM-458). Tiap intercept dilepas segera sesudah pemicu (S-09).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-458: Download gagal menampilkan toast error dengan nama berkas
1. Paksa respons Download List gagal 5xx lewat intercept
2. Klik icon Download lalu `Download as CSV`
3. Verifikasi toast `Error, failed to download Asset-Names.` (tanpa extension)
4. Lepas intercept
5. Tunggu toast lama hilang otomatis
### TC-FA-FAAM-498: Download Changelog gagal menampilkan toast error dengan nama berkas
6. Paksa Download Changelog gagal lewat intercept
7. Klik icon Changelog
8. Klik icon Download lalu `Download as XLSX`
9. Verifikasi toast `Error, failed to download Changelog-Asset-Name.`
10. Lepas intercept
11. Tunggu toast lama hilang otomatis
12. Klik `[✕]` pada Modal Changelog
### TC-FA-FAAM-524: Download Tab Total Assets gagal menampilkan toast dengan nama berkas tab
13. Klik nama `Dell Latitude`
14. Klik tab `Total Assets (42)`
15. Paksa Download Tab Total Assets gagal lewat intercept
16. Klik icon Download lalu `Download as CSV`
17. Verifikasi toast `Error, failed to download Asset-Name-Assets.`
18. Lepas intercept
19. Klik icon `[✕]` Popup Detail

## Notes

- Mode FE+BE dengan intercept parsial di atas backend nyata (bagian 6 dan prinsip 13b); bukan `Mode: mock`.
- Langkah penghubung (aksi tanpa `Verifikasi`): melepas intercept segera setelah toast diasersi, menunggu toast lama hilang otomatis sebelum toast error berikutnya (R-12), serta menutup Modal Changelog dan Popup Detail.
- Pemicu kegagalan pada ketiga blok adalah kelas b yang sama (kegagalan unduh); nama berkas toast diambil dari TC.
- Temuan untuk QA: TC-FA-FAAM-498 dan 524 menulis "lewat intercept" tanpa status respons; spec memakai 5xx seperti TC-FA-FAAM-458.
