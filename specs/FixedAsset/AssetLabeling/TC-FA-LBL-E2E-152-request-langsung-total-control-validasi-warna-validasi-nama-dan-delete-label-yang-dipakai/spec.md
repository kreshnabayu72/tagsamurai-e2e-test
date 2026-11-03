---
id: TC-FA-LBL-E2E-152-request-langsung-total-control-validasi-warna-validasi-nama-dan-delete-label-yang-dipakai
title: "Request Langsung Total Control: Validasi Warna, Validasi Nama, dan Delete Label yang Dipakai"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-453
  - TC-FA-LBL-454
  - TC-FA-LBL-455
  - TC-FA-LBL-456
  - TC-FA-LBL-457
coverage:
  web: automated
---

# Request Langsung Total Control: Validasi Warna, Validasi Nama, dan Delete Label yang Dipakai

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Seluruh langkah berupa request langsung ke server lewat klien HTTP (bagian 8b butir 1): asersi hanya status respons dan state data yang dibaca lewat fixture BE; perilaku FE untuk respons yang sama diasersi di spec jalur form.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), sesi API, `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login API di hook `before` spec ini; tidak ada login UI dan tidak ada ganti akun di tengah spec; hook `after` mengembalikan sesi ke akun default suite.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Warna Tidak Valid (dipakai langkah 2 dan 3, TC-FA-LBL-453):

  | Warna |
  |---|
  | `#GGGGGG` |
  | `#12345` |
  | `#FFF` |
  | `3B82F6` (tanpa `#`) |
  | `#1234567` |

- Nama Tidak Valid (dipakai langkah 12 dan 13, TC-FA-LBL-455):

  | Nama | Pesan |
  |---|---|
  | kosong | `Label name must not be empty` |
  | 121 karakter (`Fixture.assetLabeling.nama121`) | `Max. 120 characters` |
  | `dup name 455 {runId}-152` (sama dengan label seed `Dup Name 455 {runId}-152` tanpa memperhatikan huruf besar-kecil) | `Label name already exists` |
  | `Fixture.assetLabeling.promoEmoji` (`Promo` + emoji) | `Label name contains invalid characters` |

- Data Dinamis (seed milik spec lewat fixture BE di hook `before`, bersuffix `{runId}-152`, Color `Fixture.assetLabeling.warnaSeed`, pola Pre-setup #12 dan #14 dimiliki spec agar data Pre-setup tidak berubah, S-06): label `Dup Name 455 {runId}-152` (bersih); label `Used Label 457 {runId}-152` tertempel pada tiga aset Active `Used Asset 1 {runId}-152`, `Used Asset 2 {runId}-152`, dan `Used Asset 3 {runId}-152`; label `Default Label 457 {runId}-152` menjadi Default Label satu Asset Name `Used Item {runId}-152` (jumlah Asset Name 1).
- Data Dinamis yang dibuat request spec: label `Hex Lower 454 {runId}-152` dan label hasil request TC-FA-LBL-456 (nama tanpa baris baru); dihapus di hook `after`.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.nama121` | nama 121 karakter (sudah ada) |
  | `Fixture.assetLabeling.promoEmoji` | `Promo 😊` (sudah ada) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca state katalog serta jumlah entri Changelog Labels, System Log, dan Activity Log; endpoint tidak ditulis di TC (S-13). Pembaca isi hasil ekspor katalog (CSV/XLSX) untuk TC-FA-LBL-454.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label, aset, dan Asset Name seed serta label hasil request milik spec lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-453: Warna tidak valid lewat permintaan langsung ditolak

1. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE
2. Untuk setiap baris tabel Warna Tidak Valid (langkah 2 dan 3): kirim request langsung ke server sebagai Total Control: membuat label `Hex Direct 453 {runId}-152` dengan warna pada kolom Warna
3. Verifikasi request ditolak dengan pesan `Invalid color format`
4. Verifikasi label `Hex Direct 453 {runId}-152` tidak dibuat
5. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline

### TC-FA-LBL-454: Warna huruf kecil lewat permintaan langsung diterima dan disimpan huruf kapital

6. Kirim request langsung ke server: membuat label `Hex Lower 454 {runId}-152` dengan warna `#ef4444`
7. Ambil data label `Hex Lower 454 {runId}-152` dan entri Changelog-nya lewat fixture BE
8. Verifikasi label tersimpan dengan Color Hex `#EF4444`
9. Verifikasi entri Changelog label memakai `#EF4444`
10. Verifikasi hasil ekspor katalog memakai `#EF4444` untuk label itu

### TC-FA-LBL-455: Validasi nama lewat permintaan langsung (kosong, 121 karakter, duplikat, emoji)

11. Catat jumlah label pada katalog lewat fixture BE
12. Untuk setiap baris tabel Nama Tidak Valid (langkah 12 dan 13): kirim request langsung ke server: membuat label dengan nama pada kolom Nama
13. Verifikasi request ditolak dengan pesan pada kolom Pesan
14. Verifikasi tidak ada label dibuat (jumlah label pada katalog sama dengan yang dicatat)

### TC-FA-LBL-456: Newline dan karakter kontrol di-strip diam-diam oleh server

15. Kirim request langsung ke server: membuat label dengan nama `Line` + baris baru + `Break 456 {runId}-152`
16. Ambil data label hasil request lewat fixture BE
17. Verifikasi label tersimpan dengan nama tanpa karakter baris baru
18. Verifikasi request tidak menghasilkan pesan error

### TC-FA-LBL-457: Delete label yang dipakai lewat permintaan langsung ditolak tanpa mutasi

19. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE
20. Kirim request langsung ke server: menghapus label `Used Label 457 {runId}-152`
21. Verifikasi request ditolak oleh guard in-use dengan jumlah aset `3`
22. Kirim request langsung ke server: menghapus label `Default Label 457 {runId}-152`
23. Verifikasi request ditolak oleh guard in-use dengan jumlah Asset Name `1`
24. Verifikasi kedua label dan seluruh penempelannya tidak berubah
25. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 1, 7, 11, 16, 19 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- K-1: spec ini memuat TC kelas defense-in-depth (bagian 3 prinsip 13a) dengan Expected respons API; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint.
- Asersi "tidak ada entri log baru" ditulis sebagai asersi jumlah entri Changelog Labels, System Log, dan Activity Log terhadap baseline (bagian 3 prinsip 13g: asersi jumlah bukan kelas g; S-12). Suite ini tidak memuat spec absence untuk TC ini, sehingga tidak ada rujukan ke spec lain (S-05).
- Perulangan (bagian 8b butir 7): langkah 2 dan 3 diulang untuk lima warna pada tabel Warna Tidak Valid, dan langkah 12 dan 13 diulang untuk empat nama pada tabel Nama Tidak Valid; parameter tiap iterasi ada di tabel Prerequisites dan `Verifikasi` tetap satu per klausa.
- Ukuran spec (25 langkah nominal, di atas smell 35 langkah dengan ekspansi): kelima TC satu kelas (defense-in-depth lewat request langsung), satu sesi API Total Control, tanpa UI, dan tiap blok memakai seed sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena ekspansi perulangan dan `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-454 Expected "hasil ekspor memakai `#EF4444`" tidak menyebut format berkas; spec membaca ekspor katalog lewat pembaca CSV/XLSX suite.
  - TC-FA-LBL-453 dan 455 Expected "tidak ada entri log" tidak menyebut surface; spec memakai Changelog Labels, System Log, dan Activity Log (453, asersi jumlah dengan baseline); TC-FA-LBL-455 Expected hanya "tidak ada label dibuat".
  - TC-FA-LBL-455 duplikat memakai `high priority` (label Pre-setup #12 `High Priority`); spec memakai label seed milik spec bernama `Dup Name 455` supaya Pre-setup tidak dipakai sebagai target request (S-06).
  - TC-FA-LBL-457 menyebut jumlah aset 3 dan jumlah Asset Name 1 dari Pre-setup (`High Priority`, `Warehouse Priority`); spec men-seed label dengan jumlah yang sama.
  - TC-FA-LBL-456 Expected "tanpa pesan error" tidak menyebut kode status; spec mengasersi tidak ada pesan error pada respons.
  - Lihat catatan keputusan asersi log pada spec 149.
