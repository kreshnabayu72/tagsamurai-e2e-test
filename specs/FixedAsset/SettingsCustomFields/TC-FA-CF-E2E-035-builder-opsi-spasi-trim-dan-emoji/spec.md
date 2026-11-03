---
id: TC-FA-CF-E2E-035-builder-opsi-spasi-trim-dan-emoji
title: "Builder Opsi: Spasi, Trim, dan Emoji"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-112
  - TC-FA-CF-113
  - TC-FA-CF-114
  - TC-FA-CF-115
coverage:
  web: automated
---

# Builder Opsi: Spasi, Trim, dan Emoji

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- N total baris tab General = 8 diturunkan dari seeding Pre-setup #12 (8b butir 10): `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`; asersi 'tepat 8 baris' mengandaikan seluruh baris tampil dalam satu halaman.
- Kemampuan teknis: injeksi nilai langsung ke DOM input (Pre-setup #26, disediakan tim FE).
- Data dinamis: tidak ada field yang disimpan; nilai yang hanya diketik: Field Name `Blank Option {runId}-035`, `Trim Option {runId}-035`, `Emoji Option {runId}-035`; opsi `Valid One`, `Alpha`, `  Alpha  `, tiga spasi, `Gold😊`.
- Jeda nyata 600 ms (TC-FA-CF-113) dibatasi di bawah 30 detik sesuai bagian 6 konvensi.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-112: Nama opsi spasi saja ditolak saat Submit

1. Klik `[+ Custom Field]`
2. Pilih Data Type `Dropdown`
3. Isi Field Name `Blank Option {runId}-035`
4. Ketik `Valid One` pada input Values lalu tekan Enter
5. Injeksi opsi kedua berisi tiga spasi melewati validasi klien
6. Klik `[Submit]`
7. Verifikasi pesan inline `Option name must not be empty` tampil

#### TC-FA-CF-113: Spasi di awal dan akhir nama opsi dipangkas sebelum pengecekan duplikat dan penyimpanan

8. Klik `[Clear Field]`
9. Pilih Data Type `Dropdown`
10. Isi Field Name `Trim Option {runId}-035`
11. Ketik `Alpha` pada input Values lalu tekan Enter
12. Ketik `  Alpha  ` pada input Values tanpa Enter
13. Tunggu 600 ms
14. Verifikasi pesan inline `Option name already exists` tampil karena `  Alpha  ` dipangkas menjadi `Alpha`

#### TC-FA-CF-114: Emoji pada nama opsi diblok saat mengetik dan menempel tanpa pesan

15. Klik `[Clear Field]`
16. Pilih Data Type `Dropdown`
17. Ketik `Gold😊` pada input Values
18. Verifikasi emoji tidak masuk ke input Values
19. Verifikasi tidak ada pesan error yang tampil

#### TC-FA-CF-115: Emoji yang lolos filter klien pada nama opsi ditolak server dengan pesan karakter terlarang

20. Klik `[Clear Field]`
21. Pilih Data Type `Dropdown`
22. Isi Field Name `Emoji Option {runId}-035`
23. Injeksi opsi `Gold😊` langsung ke DOM
24. Klik `[Submit]`
25. Verifikasi pesan inline `Option name contains invalid characters` tampil
26. Klik `[✕]`
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Leave]`
29. Verifikasi tabel tab General memuat 8 baris (TC-FA-CF-112 dan TC-FA-CF-115 butir b: field tidak tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus (halaman yang sama dipakai berulang) dan penutupan form dirty pada langkah 26 dan dua langkah berikutnya (S-08).
- Field Dinamis bernama bersuffix `{runId}-035` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- P-5: TC-FA-CF-112 (opsi spasi saja lolos validasi klien lewat injeksi) dan TC-FA-CF-115 (emoji lolos filter klien lewat injeksi) masing-masing satu TC objek-uji ringan kelas a tanpa harness eksternal dan tanpa state berat, dua TC dalam batas P-5 butir b, ditaruh di spec fungsional builder opsi yang permukaannya sama.
- Asersi 'Field tidak tersimpan' pada TC-FA-CF-112 dan TC-FA-CF-115 memakai jumlah baris tab General (8, seed Pre-setup #12) setelah form ditutup.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
  - TC-FA-CF-112 dan TC-FA-CF-115 butir b ('Field tidak tersimpan') tidak menyebut cara mengamati; spec memakai jumlah baris tab General.
