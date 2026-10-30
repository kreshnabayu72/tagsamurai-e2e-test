---
id: TC-GS-TAG-E2E-079-download-registri-gagal
title: "Download Registri Gagal: Toast Error dengan Nama File Tanpa Ekstensi"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-243
coverage:
  web: automated
---

# Download Registri Gagal: Toast Error dengan Nama File Tanpa Ekstensi

## Prerequisites

- Mode: FE+BE (kegagalan dipaksa lewat `Spectra.intercept()` di atas backend nyata; bagian 6 konvensi).
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Spec hanya membaca data.
- Kebutuhan intercept: request export registri `POST /v2/hardware-tagging/tags/export` (disebut di `tc-all-tags-backend.md` bagian 5; tab dan format yang dipakai mengikuti langkah) dipaksa mengembalikan respons 5xx. Kode status tepatnya tidak ditetapkan TC (lihat Temuan untuk QA). Intercept dilepas segera setelah asersi toast (S-09) dan di hook `after` sebagai cadangan.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): intercept dilepas.
- Kemampuan teknis: `Spectra.intercept()` pada request export registri.

## Test Steps

### TC-GS-TAG-243: Download gagal menampilkan toast error dengan nama file tanpa ekstensi

1. Aktifkan intercept yang membuat request export registri mengembalikan respons 5xx
2. Klik ikon Download, lalu klik `Download as CSV`
3. Verifikasi toast error `Error, failed to download All-TAGs.`
4. Lepas intercept request export registri

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas harness b (fault injection) berdiri sendiri di spec ini; isi file dan nama file unduhan sukses ada di spec `TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol`.
- Panjang spec: 4 langkah, di bawah ambang sekitar 35 langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (melepas intercept sesudah pemicu selesai).
- Temuan untuk QA:
  - TC-GS-TAG-243 hanya menyebut "5xx" tanpa kode status tepat; spec memakai kode 5xx yang ditentukan di tahap script.
  - TC-GS-TAG-243 hanya menguji `Download as CSV` pada Tab All; kegagalan `Download as XLSX` dan unduhan tab lain tidak diuji TC, sehingga teks toast untuk kombinasi itu (nama file dasar `Paired-TAGs`, `Not-Paired-TAGs`) tidak diverifikasi.
  - TC-GS-TAG-243 tidak memuat Expected tentang berkas yang tidak terunduh atau keadaan tombol Download sesudah gagal; spec tidak menambah asersi untuk itu.
