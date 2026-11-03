---
id: TC-FA-LBL-E2E-039-duplikat-nama-label-edit-deteksi-setelah-debounce-dan-kapitalisasi-sendiri
title: "Duplikat Nama Label Edit: Deteksi Setelah Debounce dan Kapitalisasi Sendiri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-119
  - TC-FA-LBL-120
  - TC-FA-LBL-121
  - TC-FA-LBL-122
coverage:
  web: automated
---

# Duplikat Nama Label Edit: Deteksi Setelah Debounce dan Kapitalisasi Sendiri

## Prerequisites

- Mode: FE+BE. Backend nyata (pengecekan keunikan nama ke server); tidak ada intercept.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-039`):
  - `Edit Target 119 {runId}-039` (satu label seed untuk keempat TC)
- Data Pre-setup: label `High Priority` (Pre-setup #12, Color `#EF4444`) ada di katalog Company Alpha; dipakai sebagai nama bentrok dan tidak diubah.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas akun dan data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.labelHighPriority` | `High Priority` (Pre-setup #12) |
  | `Fixture.assetLabeling.labelHighPriorityKecil` | `high priority` |
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |

- Kemampuan teknis: menunggu lebih dari 500 ms sesudah ketikan terakhir (debounce pengecekan keunikan) dan hover tombol.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search `Edit Target 119 {runId}-039`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 119 {runId}-039`, lalu klik `Edit`

### TC-FA-LBL-119: Edit ke nama label lain ditandai duplikat setelah debounce

3. Ganti isi Label Name dengan `Fixture.assetLabeling.labelHighPriorityKecil`, tunggu lebih dari 500 ms
4. Hover `[Save]`
5. Verifikasi inline error `Label name already exists` tampil
6. Verifikasi `[Save]` berstatus disabled dengan tooltip `Label name already exists`

### TC-FA-LBL-120: Edit ke nama label lain dengan spasi tepi tetap duplikat

7. Ganti isi Label Name dengan `Edit Target 119 {runId}-039` (kembalikan ke nilai tersimpan)
8. Ganti isi Label Name dengan dua spasi + `Fixture.assetLabeling.labelHighPriority` + dua spasi, tunggu lebih dari 500 ms
9. Verifikasi inline error `Label name already exists` tampil
10. Verifikasi `[Save]` berstatus disabled

### TC-FA-LBL-122: Mengetik ulang nama sendiri yang sama tidak memicu error duplikat

11. Hapus Label Name lalu ketik ulang `Edit Target 119 {runId}-039`, tunggu lebih dari 500 ms
12. Verifikasi `[Save]` berstatus enabled
13. Verifikasi tidak ada inline error `Label name already exists`

### TC-FA-LBL-121: Mengganti kapitalisasi nama sendiri bukan duplikat dan disimpan sebagai perubahan nyata

14. Ganti isi Label Name dengan `EDIT TARGET 119 {runId}-039`, tunggu lebih dari 500 ms
15. Verifikasi tidak ada inline error `Label name already exists`
16. Klik `[Save]`
17. Verifikasi toast `Success, label has been updated.` (bukan `No changes to save.`)
18. Ganti isi kotak search dengan `EDIT TARGET 119 {runId}-039`, tekan Enter
19. Verifikasi baris menampilkan chip `EDIT TARGET 119 {runId}-039`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 18 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Penyimpangan urutan (S-05, bagian 3): TC-FA-LBL-122 ditaruh sebelum TC-FA-LBL-121 karena TC-FA-LBL-121 menyimpan perubahan dan harus terakhir; keempat TC memakai satu pembukaan modal pada satu label seed.
- Langkah penghubung (S-03, R-12): langkah 7 mengembalikan nama ke nilai tersimpan supaya inline error duplikat kasus sebelumnya hilang sebelum kasus berikutnya.
- Seeding minimal (S-11): TC-FA-LBL-121 mengetik nama label seed dengan huruf kapital semua (`EDIT TARGET 119 {runId}-039`), yaitu nama sendiri dengan kapitalisasi berbeda sesuai maksud TC; satu label seed menggantikan label `Edit Target <nomor TC>` tiap TC.
- Temuan untuk QA:
  - TC-FA-LBL-121 Post Condition b (entri Edit Label Name Old `Edit Target 121` New `EDIT TARGET 121` tercatat, detail di Section 5) tidak punya langkah observasi di TC ini dan tidak diasersi.
