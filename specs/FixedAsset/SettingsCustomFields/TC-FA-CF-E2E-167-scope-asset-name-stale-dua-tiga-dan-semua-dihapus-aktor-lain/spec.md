---
id: TC-FA-CF-E2E-167-scope-asset-name-stale-dua-tiga-dan-semua-dihapus-aktor-lain
title: "Scope: Dua, Tiga, dan Seluruh Asset Name Dihapus Aktor Lain Sebelum Submit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-96
  - TC-FA-CF-97
  - TC-FA-CF-98
coverage:
  web: automated
---

# Scope: Dua, Tiga, dan Seluruh Asset Name Dihapus Aktor Lain Sebelum Submit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Pelaku kedua: sesi API Total Control sesi 2 (Pre-setup #10) `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Rina Putri) pada Company Alpha, password lewat `Spectra.env.FA_TC2_PASSWORD`; environment variable: `FA_TC2_PASSWORD` (didaftarkan tim FE). Sesi API memakai token yang tidak dihitung sebagai sesi web (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup yang diubah: Asset Name `Boiler`, `Compressor`, dan `Turbine` Company Alpha (Pre-setup #11, tanpa aset terkait) dihapus oleh sesi API pada langkah 4, 16, dan 27; `Pump` hanya dipilih dan tidak dihapus. Asset Name itu tidak dapat dimiliki spec karena teks pesan Expected memuat nama literal. Pemulihan: seed reset Company Alpha (disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar TC (langkah 12 dan 23); efeknya pada Asset Name tercatat di sini dan suite berjalan serial (S-06).
- Data dinamis (hanya diketik; tidak pernah tersimpan): `Stale Two {runId}-167`, `Stale Three {runId}-167`, `Stale All {runId}-167`, semuanya Data Type Text.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-167`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-96: Dua Asset Name yang dihapus admin lain sebelum Submit ditolak dengan satu pesan gabungan

1. Klik `[+ Custom Field]`
2. Isi Field Name `Stale Two {runId}-167` dan Data Type `Text`
3. Pilih Scope `Specific Asset Name` dengan `Boiler`, `Pump`, dan `Turbine` (urutan abjad)
4. Dari sesi API Total Control sesi 2 (Pre-setup #10), hapus Asset Name `Turbine` dan `Boiler` hingga penghapusan tersimpan
5. Klik `[Submit]`
6. Verifikasi satu pesan inline `Boiler and Turbine no longer exist. Please select another.` tampil pada input Asset Name
7. Verifikasi hanya chip `Turbine` dan `Boiler` dihapus dari input Asset Name
8. Verifikasi chip `Pump` dipertahankan
9. Klik `[✕]`
10. Verifikasi dialog `Unsaved Changes` tampil
11. Klik `[Leave]`
12. Pulihkan Asset Name `Boiler` dan `Turbine` lewat seed reset Company Alpha

#### TC-FA-CF-97: Tiga Asset Name yang dihapus admin lain sebelum Submit ditolak dengan pesan daftar memakai koma dan and

13. Klik `[+ Custom Field]`
14. Isi Field Name `Stale Three {runId}-167` dan Data Type `Text`
15. Pilih Scope `Specific Asset Name` dengan `Boiler`, `Compressor`, `Pump`, dan `Turbine` (urutan abjad)
16. Dari sesi API Total Control sesi 2 (Pre-setup #10), hapus Asset Name `Turbine`, `Boiler`, dan `Compressor` hingga penghapusan tersimpan
17. Klik `[Submit]`
18. Verifikasi satu pesan inline `Boiler, Compressor, and Turbine no longer exist. Please select another.` tampil pada input Asset Name
19. Verifikasi chip `Pump` dipertahankan
20. Klik `[✕]`
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik `[Leave]`
23. Pulihkan Asset Name `Boiler`, `Compressor`, dan `Turbine` lewat seed reset Company Alpha

#### TC-FA-CF-98: Seluruh himpunan Asset Name terhapus sebelum Submit mengosongkan input

24. Klik `[+ Custom Field]`
25. Isi Field Name `Stale All {runId}-167` dan Data Type `Text`
26. Pilih Scope `Specific Asset Name` dengan `Turbine` saja
27. Dari sesi API Total Control sesi 2 (Pre-setup #10), hapus Asset Name `Turbine` hingga penghapusan tersimpan
28. Klik `[Submit]`
29. Verifikasi pesan inline `Turbine no longer exists. Please select another.` tampil pada input Asset Name
30. Verifikasi input Asset Name dikosongkan
31. Klik `[✕]`
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Pemicu pelaku kedua memakai sesi API (bukan konteks UI kedua), ditulis 'hingga ... tersimpan' (R-20); tidak memakai `P-2` (keputusan 2026-10-30).
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan form dirty (`Klik [✕]`, `Verifikasi` dialog `Unsaved Changes`, `[Leave]`) pada akhir tiap TC (S-08) dan pemulihan Asset Name pada langkah 12 dan 23. Urutan penghapusan `Turbine` dan `Boiler` pada langkah 4 mengikuti TC (`Turbine` lalu `Boiler`).
- Field Dinamis bernama bersuffix `{runId}-167` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Temuan untuk QA:
  - TC-FA-CF-96 sampai 98 bertanda Manual Only (dua sesi paralel) tetapi pelaku kedua hanya memicu state; spec memakai sesi API (keputusan 2026-10-21 dan 2026-10-30).
  - TC-FA-CF-96 sampai 98 tidak menyebut pemulihan Asset Name antar TC padahal TC berikutnya memilih Asset Name yang sudah dihapus; spec menambah langkah pemulihan penghubung.
  - Penghapusan Asset Name Pre-setup #11 mengubah data bersama; `suite.md` belum menyatakan pemulihan lewat seed reset untuk kasus ini (S-06 syarat terakhir) dan perlu dilengkapi tim FE/BE.
