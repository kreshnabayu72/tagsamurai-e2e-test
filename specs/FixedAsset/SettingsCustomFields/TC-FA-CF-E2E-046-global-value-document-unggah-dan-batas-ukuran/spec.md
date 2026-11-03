---
id: TC-FA-CF-E2E-046-global-value-document-unggah-dan-batas-ukuran
title: "Global Value Document: Kontrol Unggah, Format Berkas, dan Batas Ukuran 1 MB"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-140
  - TC-FA-CF-141
  - TC-FA-CF-142
  - TC-FA-CF-143
  - TC-FA-CF-144
coverage:
  web: automated
---

# Global Value Document: Kontrol Unggah, Format Berkas, dan Batas Ukuran 1 MB

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Berkas uji (Pre-setup #36; fixture berkas `Fixture.berkasUji` baru, belum ada): `valid.pdf` (200 KB), `exact-1mb.pdf` (tepat 1 MB), `over-1mb.pdf` (1 MB lebih satu byte), `malware.exe`.
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-046`): `Global Doc 1MB {runId}-046` (Document, Global, berkas akhir `exact-1mb.pdf`, tersimpan) dan `Global Doc Valid {runId}-046` (Document, Global, berkas `valid.pdf`, tersimpan).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-046` beserta berkas yang terunggah.
- Kemampuan teknis: pemilihan berkas lewat file picker; pembacaan format yang diizinkan file picker (mis. atribut `accept` kontrol; disediakan tim FE); injeksi berkas ke kontrol dengan melewati file picker (Pre-setup #26).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]

### TC-FA-CF-140: Global Value Document memakai kontrol FileUpload dengan placeholder Upload document dan tombol Choose file

2. Isi Field Name `Global Doc 1MB {runId}-046`, pilih Data Type `Document`, Scope `General`, Value Type `Global`
3. Verifikasi satu kontrol unggah file tampil dengan placeholder "Upload document"
4. Verifikasi tombol `Choose file` tampil pada kontrol unggah
5. Klik `Choose file`
6. Verifikasi format di luar PDF, DOCX, DOC, XLS, XLSX, PNG, JPG, JPEG, CSV tidak dapat dipilih pada file picker
7. Tutup file picker tanpa memilih berkas

### TC-FA-CF-142: Global Value Document berformat di luar daftar ditolak dengan pesan format

8. Injeksi berkas `malware.exe` ke kontrol (melewati file picker)
9. Verifikasi pesan inline "Unsupported file format. Use PDF, DOCX, DOC, XLS, XLSX, PNG, JPG, JPEG, or CSV." tampil pada kontrol
10. Verifikasi file tidak diterima: kontrol tetap menampilkan placeholder "Upload document"

### TC-FA-CF-144: Global Value Document lebih dari 1 MB ditolak dengan pesan ukuran

11. Pilih berkas `over-1mb.pdf`
12. Verifikasi pesan inline "File size must not exceed 1 MB." tampil pada kontrol
13. Verifikasi file tidak diterima: kontrol tetap menampilkan placeholder "Upload document"

### TC-FA-CF-143: Global Value Document berukuran tepat 1 MB diterima

14. Pilih berkas `exact-1mb.pdf`
15. Verifikasi nama file `exact-1mb.pdf` tampil pada kontrol
16. Verifikasi pesan "File size must not exceed 1 MB." tidak tampil
17. Klik [Submit]
18. Verifikasi toast "Success, custom field has been created." tampil

### TC-FA-CF-141: Global Value Document berformat valid ukuran kecil diterima dan nama file tampil dengan tombol hapus

19. Klik [+ Custom Field]
20. Isi Field Name `Global Doc Valid {runId}-046`, pilih Data Type `Document`, Scope `General`, Value Type `Global`
21. Pilih berkas `valid.pdf`
22. Verifikasi nama file `valid.pdf` tampil pada kontrol
23. Verifikasi tombol hapus `Clear Button` tampil pada kontrol
24. Tunggu toast lama hilang otomatis
25. Klik [Submit]
26. Verifikasi toast "Success, custom field has been created." tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 140, 142, 144, 143, 141 (urutan sumber 140 sampai 144). Berkas yang ditolak (TC-FA-CF-142 dan TC-FA-CF-144) diuji lebih dulu pada modal yang sama (validasi diblokir sebelum aksi sukses, S-10); TC-FA-CF-143 memakai modal yang sama dan berakhir dengan Submit sukses yang menutup modal; TC-FA-CF-141 membuka modal baru (langkah 19).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7 (menutup file picker), 19, serta pemilihan berkas dan pengisian form sebagai bagian langkah TC. Memilih berkas berikutnya pada kontrol yang sama menggantikan berkas sebelumnya dan menghapus pesan inline lama.
- Langkah 15 (nama file `exact-1mb.pdf` tampil) adalah anchor positif bagi asersi absence pesan ukuran pada langkah 16 (bagian 8b butir 2, S-03); langkah 22 dan 23 adalah Expected TC-FA-CF-141.
- Asersi "file tidak diterima" ditulis sebagai kontrol yang tetap menampilkan placeholder "Upload document", karena TC tidak menyebut tampilan kontrol sesudah penolakan.
- Langkah penghubung toast (S-03, R-22): langkah 24 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - TC-FA-CF-140: Expected b ("format di luar daftar tidak dapat dipilih pada file picker") butuh kemampuan membaca format yang diizinkan file picker; mekanismenya tidak didefinisikan di TC, PRD, atau LLD dan ditulis "disediakan tim FE" (S-13).
  - TC-FA-CF-142 dan TC-FA-CF-144: TC tidak menyebut tampilan kontrol sesudah berkas ditolak; asersi "file tidak diterima" memakai placeholder sebagai observasi.
  - Nama field memakai suffix `{runId}-046` (S-12) sehingga tidak sama dengan `Global Doc` pada Data Uji TC.
