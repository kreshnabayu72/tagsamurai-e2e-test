---
id: TC-FA-CF-E2E-047-global-value-document-ganti-dan-hapus-file
title: "Global Value Document: Kosong Ditolak, Ganti File, dan Hapus File"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-145
  - TC-FA-CF-146
  - TC-FA-CF-147
coverage:
  web: automated
---

# Global Value Document: Kosong Ditolak, Ganti File, dan Hapus File

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Berkas uji (Pre-setup #36; fixture berkas `Fixture.berkasUji` baru, belum ada): `valid.pdf` dan `second.pdf`.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-047`): `Global Doc {runId}-047` (Document, Global; tidak tersimpan). Tidak ada field yang tersimpan oleh spec ini.
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-047`.
- Kemampuan teknis: pemilihan berkas lewat file picker.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-145: Global Value Document kosong ditolak saat Submit

1. Klik [+ Custom Field]
2. Isi Field Name `Global Doc {runId}-047`, pilih Data Type `Document`, Scope `General`, Value Type `Global`
3. Biarkan kontrol kosong
4. Klik [Submit]
5. Verifikasi pesan inline "Value must not be empty" tampil
6. Verifikasi modal tetap terbuka
7. Klik [Clear Field]

### TC-FA-CF-146: Memilih file lain pada kontrol yang sama menggantikan file sebelumnya

8. Isi Field Name `Global Doc {runId}-047`, pilih Data Type `Document`, Scope `General`, Value Type `Global`
9. Pilih berkas `valid.pdf`
10. Pilih berkas `second.pdf` pada kontrol yang sama
11. Verifikasi kontrol menampilkan hanya nama file `second.pdf`

### TC-FA-CF-147: Tombol hapus pada file terpilih mengosongkan kontrol dan Submit sesudahnya ditolak

12. Pilih berkas `valid.pdf`
13. Klik tombol hapus `Clear Button`
14. Verifikasi kontrol kosong setelah klik hapus
15. Klik [Submit]
16. Verifikasi pesan inline "Value must not be empty" tampil saat Submit
17. Klik `[✕]`
18. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
19. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (145, 146, 147). Ketiga TC memakai modal yang sama tanpa Submit sukses sehingga langkah "Klik [+ Custom Field]" TC-FA-CF-146 dan TC-FA-CF-147 tidak diulang; pengisian ulang form mengikuti langkah TC (langkah 8). Jumlah buka form (1) sama dengan kejadian menutup (langkah 17 sampai 19).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 ([Clear Field] mengosongkan modal dan menghapus pesan inline sebelum TC berikutnya, R-12), serta pemilihan berkas dan pengisian form sebagai bagian langkah TC. Pada langkah 12, memilih `valid.pdf` menggantikan `second.pdf` sebagai awal langkah TC-FA-CF-147.
- Temuan untuk QA:
  - TC-FA-CF-147: Expected tidak menyebut apakah modal tetap terbuka sesudah Submit ditolak (TC-FA-CF-145 menulisnya); hanya pesan inline yang diasersi pada langkah 16.
  - Nama field memakai suffix `{runId}-047` (S-12) sehingga tidak sama dengan `Global Doc` pada Data Uji TC.
