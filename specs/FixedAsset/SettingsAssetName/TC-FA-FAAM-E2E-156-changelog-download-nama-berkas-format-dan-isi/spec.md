---
id: TC-FA-FAAM-E2E-156-changelog-download-nama-berkas-format-dan-isi
title: "Modal Changelog Download: Nama Berkas, Format, Cakupan, dan Modified By Nama Lengkap"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-497
  - TC-FA-FAAM-499
coverage:
  web: automated
---

# Modal Changelog Download: Nama Berkas, Format, Cakupan, dan Modified By Nama Lengkap

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28) berisi entri Create, Edit, dan Delete oleh Sarah Johnson, David Kurniawan, dan Michael Wijaya. Jumlah baris berkas tidak diasersi sebagai angka absolut (S-12).
- Kemampuan teknis: pembaca berkas CSV hasil unduhan (nilai sel, header kolom) dan folder unduhan runner (disediakan tim FE). Isi berkas CSV adalah kelas binary buffer (bagian 3 prinsip 13f).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAM-497: Download Changelog: nama berkas, format, dan cakupan mengikuti Search/Filter dan kolom visible

2. Terapkan Filter Action `Edit`: klik icon Filter, pilih Action `Edit`, klik `[Apply]`
3. Klik Download
4. Klik `Download as CSV`
5. Verifikasi tidak ada toast sukses
6. Verifikasi berkas `Changelog-Asset-Name.csv` terunduh
7. Buka isi berkas `Changelog-Asset-Name.csv`
8. Verifikasi berkas memuat sedikitnya satu baris data
9. Verifikasi semua baris data berasal dari entri Edit yang tersaring
10. Verifikasi kolom Date ada dan nilainya mengikuti Date Format dan Time Format General Settings
11. Verifikasi kolom Action ada dan semua nilainya `Edit`
12. Verifikasi kolom Asset Name ada dan berisi nama Asset Name sesudah kejadian
13. Verifikasi kolom Field ada dan berisi nama Field yang diubah
14. Verifikasi kolom Old Value ada dan berisi nilai lama
15. Verifikasi kolom New Value ada dan berisi nilai baru

### TC-FA-FAAM-499: Download Changelog memuat Modified By nama lengkap

16. Bersihkan Filter: klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
17. Klik Download
18. Klik `Download as CSV`
19. Verifikasi berkas `Changelog-Asset-Name.csv` terunduh
20. Buka isi berkas `Changelog-Asset-Name.csv`
21. Verifikasi sel Modified By pada baris entri seed berisi `Sarah Johnson`
22. Verifikasi tidak ada sel Modified By bernilai `Sarah J`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): membersihkan Filter sebelum unduhan kedua (langkah 16, S-09).
- Asersi tidak ada toast sukses (langkah 5) ditulis segera setelah pemicu unduhan dan sebelum asersi artefak; klik `Download as CSV` menjadi anchor positif yang buktinya menyusul pada langkah 6 (bagian 8b butir 11). Asersi tidak ada sel `Sarah J` (langkah 22) beranchor langkah 21.
- Kolom yang diasersi pada langkah 10 sampai 15 adalah enam kolom yang disebut Data Uji TC-FA-FAAM-497; nilai tanggal pada langkah 10 dibandingkan dengan format General Settings client.
- Jika unduhan kedua memakai nama berkas sama, runner memakai berkas terbaru (kemampuan folder unduhan disediakan tim FE).
- Pembagian TC lintas spec: TC-FA-FAAM-498 (kegagalan Download Changelog) ada di spec resilience download pada slice lain.
- Temuan untuk QA:
  - TC-FA-FAAM-497 Data Uji menyebut enam kolom (`Date`, `Action`, `Asset Name`, `Field`, `Old Value`, `New Value`) sebagai kolom visible, sedangkan konfigurasi bawaan Changelog memuat tujuh kolom termasuk `Modified By`; TC-FA-FAAM-499 mengharapkan kolom Modified By ada di berkas. Spec mengasersi enam kolom pada TC-FA-FAAM-497 dan Modified By pada TC-FA-FAAM-499.
  - TC-FA-FAAM-497 Expected d ("nama Asset Name sesudah kejadian") tidak menyebut nilai pembanding; spec membandingkan dengan kolom Asset Name pada tabel Changelog untuk entri yang sama.
