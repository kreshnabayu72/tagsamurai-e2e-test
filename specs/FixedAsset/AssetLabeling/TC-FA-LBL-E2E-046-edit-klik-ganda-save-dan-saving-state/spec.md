---
id: TC-FA-LBL-E2E-046-edit-klik-ganda-save-dan-saving-state
title: "Edit: Klik Ganda Save dan Saving State"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-145
  - TC-FA-LBL-146
coverage:
  web: automated
---

# Edit: Klik Ganda Save dan Saving State

## Prerequisites

- Mode: FE+BE. Backend nyata. `Spectra.intercept()` hanya menahan respons Save untuk mengamati saving state (bukan kegagalan yang dipaksakan).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-046`):
  - `Edit Target 146 {runId}-046` (TC-FA-LBL-146)
  - `Edit Target 145 {runId}-046` (TC-FA-LBL-145)
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: `Spectra.intercept()` untuk menahan lalu melepas respons Save; klik ganda cepat pada `[Save]`; fixture BE untuk membaca entri Changelog Labels (disediakan tim FE/BE; S-12).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-146: Saving state Save: tombol loading dan kontrol lain terkunci selama request

1. Ketik Search `Edit Target 146 {runId}-046`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 146 {runId}-046`, lalu klik `Edit`
3. Ganti isi Label Name dengan `Edit Saving 146 {runId}-046`
4. Tahan respons Save (delay jaringan)
5. Klik `[Save]`
6. Verifikasi `[Save]` menampilkan spinner dan berstatus disabled
7. Verifikasi `[Clear Field]`, icon `[✕]`, dan input berstatus disabled sampai respons diterima
8. Lepas tahanan respons
9. Tunggu aksi selesai (modal tertutup)

### TC-FA-LBL-145: Klik ganda cepat pada Save hanya memproses satu request

10. Ganti isi kotak search dengan `Edit Target 145 {runId}-046`, tekan Enter
11. Klik `⋯` pada baris `Edit Target 145 {runId}-046`, lalu klik `Edit`
12. Ganti isi Label Name dengan `Edit Double 145 {runId}-046`
13. Klik `[Save]` dua kali dengan cepat
14. Verifikasi `[Save]` berstatus disabled dengan loading setelah klik pertama
15. Verifikasi tepat satu entri Edit Label Name tercatat untuk label `Edit Double 145 {runId}-046` di Changelog Labels (baseline nol karena nama bersuffix unik)

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 10 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-146 ditaruh sebelum TC-FA-LBL-145; keduanya memakai label seed terpisah karena masing-masing menyimpan perubahan.
- Langkah penghubung (S-03, 8b butir 8): langkah 8, 9 melepas tahanan respons dan menunggu Save selesai sebelum berpindah ke label berikutnya.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-145 Post Condition ("Nama tersimpan `Edit Double 145`") tidak punya langkah observasi terpisah di TC dan tidak diasersi.
  - TC-FA-LBL-145 Expected "disabled dengan loading setelah klik pertama" bergantung pada waktu respons; TC tidak menahan respons pada kasus ini sehingga asersi state sementara dapat terlewat bila server cepat.
  - TC-FA-LBL-146 tidak menyebut mekanisme "delay jaringan"; spec memakai `Spectra.intercept()` untuk menahan respons.
