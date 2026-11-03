---
id: TC-FA-CF-E2E-023-validasi-placeholder-create
title: "Validasi Placeholder pada Create"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-89
  - TC-FA-CF-90
  - TC-FA-CF-88
coverage:
  web: automated
---

# Validasi Placeholder pada Create

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Kemampuan teknis: injeksi nilai langsung ke DOM input (Pre-setup #26, disediakan tim FE); mengetik karakter emoji pada input.
- N total baris tab General = 8 (Pre-setup #12, diturunkan dari seeding, 8b butir 10); seluruh baris diasumsikan tampil dalam satu halaman.
- Data dinamis (dibuat lewat UI oleh spec ini): D-1 Field Name `Ph Boundary {runId}-023`, Data Type Text, Placeholder 120 karakter `B`. Nilai yang hanya diketik dan tidak pernah tersimpan: `Scan😊`, Field Name `Ph Emoji {runId}-023`, 121 karakter `B`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-023`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-89: Emoji pada Placeholder diblok saat mengetik dan menempel tanpa pesan

1. Klik `[+ Custom Field]`
2. Ketik `Scan😊` pada Placeholder
3. Verifikasi emoji tidak masuk ke input Placeholder
4. Verifikasi tidak ada pesan error yang tampil

#### TC-FA-CF-90: Emoji yang lolos filter klien pada Placeholder ditolak server dengan pesan karakter terlarang

5. Klik `[Clear Field]`
6. Injeksi nilai `Scan😊` langsung ke DOM input Placeholder
7. Isi Field Name `Ph Emoji {runId}-023` dan Data Type `Text`
8. Klik `[Submit]`
9. Verifikasi pesan inline `Placeholder contains invalid characters` tampil
10. Klik `[✕]`
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`
13. Verifikasi tabel tab General memuat 8 baris (field `Ph Emoji {runId}-023` tidak tersimpan)

#### TC-FA-CF-88: Placeholder tepat 120 karakter diterima dan 121 karakter ditolak

14. Klik `[+ Custom Field]`
15. Ketik Placeholder 121 karakter (huruf `B` diulang 121 kali)
16. Verifikasi pesan inline `Max. 120 characters` tampil langsung
17. Hapus satu karakter sehingga Placeholder 120 karakter
18. Verifikasi pesan inline `Max. 120 characters` tidak tampil
19. Isi Field Name `Ph Boundary {runId}-023` dan Data Type `Text`
20. Klik `[Submit]`
21. Verifikasi toast sukses: "Success, custom field has been created."

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 89, 90, 88 (urutan sumber 88, 89, 90). Validasi yang diblokir didahulukan sebelum aksi yang membuat data (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus (halaman yang sama dipakai berulang) dan penutupan form dirty pada langkah 10 dan dua langkah berikutnya (S-08).
- Field Dinamis bernama bersuffix `{runId}-023` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- P-5: TC-FA-CF-90 (emoji yang lolos filter klien, ditolak server) adalah satu TC objek-uji ringan kelas a tanpa harness eksternal dan tanpa state berat, ditaruh di spec fungsional validasi Placeholder yang permukaannya sama (P-5 butir b).
- Asersi 'Field tidak tersimpan' pada TC-FA-CF-90 memakai jumlah baris tab General (8, seed Pre-setup #12) setelah form ditutup, bukan asersi absence log.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
  - TC-FA-CF-89 menyebut 'mengetik dan menempel' pada judul tetapi langkah hanya mengetik; spec mengikuti langkah TC.
