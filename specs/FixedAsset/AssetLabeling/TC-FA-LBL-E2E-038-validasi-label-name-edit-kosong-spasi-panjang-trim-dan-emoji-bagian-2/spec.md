---
id: TC-FA-LBL-E2E-038-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-2
title: "Validasi Label Name Edit: Kosong, Spasi, Panjang, Trim, dan Emoji (bagian 2/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-116
  - TC-FA-LBL-118
  - TC-FA-LBL-486
coverage:
  web: automated
---

# Validasi Label Name Edit: Kosong, Spasi, Panjang, Trim, dan Emoji (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-038`):
  - `Edit Target 116 {runId}-038` (TC-FA-LBL-486 dan TC-FA-LBL-116, satu pembukaan modal)
  - `Edit Target 118 {runId}-038` (TC-FA-LBL-118)
- Nama120 (hanya hasil Edit pada label seed `Edit Target 116 {runId}-038`, tidak di-seed): kata `Alpha` dipisah spasi tunggal dan ditutup akhiran unik per run `{runId}-038` (`{runId}` hanya digit; Data Uji TC-FA-LBL-116 dan 486 menulis akhiran `{runId}-116` dan `{runId}-486`), disusun supaya total tepat 120 karakter termasuk akhiran (nilai dihitung di script).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas akun dan data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: mengetik teks sampai 120 karakter beserta spasi tepi.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-486: Edit: spasi tepi tidak dihitung terhadap batas 120 karakter

1. Ketik Search `Edit Target 116 {runId}-038`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 116 {runId}-038`, lalu klik `Edit`
3. Ganti isi Label Name dengan Nama120 diikuti 5 spasi di akhir
4. Verifikasi `[Save]` berstatus enabled
5. Verifikasi tidak ada inline error `Max. 120 characters`

### TC-FA-LBL-116: Edit nama menjadi tepat 120 karakter diterima

6. Ganti isi Label Name dengan Nama120 (tanpa spasi tepi)
7. Verifikasi tidak ada inline error pada Label Name
8. Klik `[Save]`
9. Verifikasi toast `Success, label has been updated.`
10. Ganti isi kotak search dengan Nama120, tekan Enter
11. Verifikasi baris menampilkan chip dengan Nama120 (120 karakter termasuk akhiran `{runId}-038`) penuh tersimpan

### TC-FA-LBL-118: Edit: spasi tepi dibuang saat disimpan dan tidak dihitung terhadap 120 karakter

12. Ganti isi kotak search dengan `Edit Target 118 {runId}-038`, tekan Enter
13. Klik `⋯` pada baris `Edit Target 118 {runId}-038`, lalu klik `Edit`
14. Ganti isi Label Name dengan dua spasi + `Edit Trimmed 118 {runId}-038` + dua spasi
15. Klik `[Save]`
16. Verifikasi toast `Success, label has been updated.`
17. Ganti isi kotak search dengan `Edit Trimmed 118 {runId}-038`, tekan Enter
18. Verifikasi baris menampilkan chip `Edit Trimmed 118 {runId}-038` tanpa spasi tepi

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 10, 12, 17 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-486 (tanpa Save) ditaruh sebelum TC-FA-LBL-116 dan TC-FA-LBL-118 (aksi simpan); TC-FA-LBL-486 dan TC-FA-LBL-116 memakai satu pembukaan modal pada label seed pertama.
- Langkah penghubung (S-03): sesudah `[Save]` TC-FA-LBL-116 dan TC-FA-LBL-118, Search diganti ke nama baru agar baris yang tersimpan tampil; TC tidak menyebut cara membaca nama tersimpan.
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-116 Expected "nama 120 karakter tersimpan" tidak menyebut cara membaca; spec mencari lewat Search nama penuh, dan batas panjang kotak Search tidak disebut TC.
  - TC-FA-LBL-118 Post Condition "Nama tersimpan `Edit Trimmed 118`" identik dengan Expected b dan tidak diasersi ganda.
