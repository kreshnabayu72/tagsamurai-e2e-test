---
id: TC-FA-CF-E2E-036-builder-opsi-hapus-opsi-dan-opsi-terakhir
title: "Builder Opsi: Hapus Opsi dan Opsi Terakhir"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-116
  - TC-FA-CF-117
  - TC-FA-CF-118
coverage:
  web: automated
---

# Builder Opsi: Hapus Opsi dan Opsi Terakhir

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- N total baris tab General = 8 diturunkan dari seeding Pre-setup #12 (8b butir 10): `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`; asersi 'tepat 8 baris' mengandaikan seluruh baris tampil dalam satu halaman.
- Data dinamis: tidak ada field yang disimpan; nilai yang hanya diketik: Field Name `Zero Dropdown {runId}-036`; opsi `Class A`, `Class B`, `Only One`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-116: Tombol hapus opsi pada form Create menghapus badge tanpa dialog

1. Klik `[+ Custom Field]`
2. Pilih Data Type `Dropdown`
3. Ketik `Class A` pada input Values lalu tekan Enter
4. Ketik `Class B` pada input Values lalu tekan Enter
5. Klik `✕` pada badge `Class A`
6. Verifikasi badge `Class A` hilang dari form
7. Verifikasi tidak ada dialog apa pun
8. Verifikasi badge `Class B` tetap ada

#### TC-FA-CF-117: Menghapus opsi terakhir tidak menampilkan dialog blok dan tombol hapus tetap Enabled

9. Klik `[Clear Field]`
10. Pilih Data Type `Dropdown`
11. Ketik `Only One` pada input Values lalu tekan Enter
12. Verifikasi tombol hapus `✕` pada badge `Only One` Enabled
13. Klik `✕` pada badge `Only One`
14. Verifikasi badge hilang dan form tanpa opsi sementara
15. Verifikasi tidak ada dialog blok

#### TC-FA-CF-118: Submit Dropdown tanpa opsi ditolak dengan pesan Dropdown options

16. Klik `[Clear Field]`
17. Pilih Data Type `Dropdown`
18. Isi Field Name `Zero Dropdown {runId}-036`
19. Klik `[Submit]`
20. Verifikasi pesan inline `Dropdown options must not be empty` tampil pada Values
21. Verifikasi modal tetap terbuka
22. Klik `[✕]`
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`
25. Verifikasi tabel tab General memuat 8 baris (TC-FA-CF-118 butir b: field tidak tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus (halaman yang sama dipakai berulang) dan penutupan form dirty pada langkah 22 dan dua langkah berikutnya (S-08).
- Field Dinamis bernama bersuffix `{runId}-036` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Asersi 'Tombol hapus opsi tidak pernah disabled' (TC-FA-CF-117 butir c) ditulis sebagai `Verifikasi` Enabled sebelum opsi terakhir dihapus (8b butir 5), karena sesudahnya tidak ada tombol yang dapat diamati.
- Asersi 'Field tidak tersimpan' pada TC-FA-CF-118 memakai jumlah baris tab General (8, seed Pre-setup #12) setelah form ditutup.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
