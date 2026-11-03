---
id: TC-FA-CF-E2E-024-validasi-field-name-kosong-spasi-dan-data-type-wajib
title: "Validasi Field Name Kosong atau Spasi Saja dan Data Type Wajib"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-60
  - TC-FA-CF-61
  - TC-FA-CF-71
coverage:
  web: automated
---

# Validasi Field Name Kosong atau Spasi Saja dan Data Type Wajib

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- N total baris tab General = 8 diturunkan dari seeding Pre-setup #12 (8b butir 10): `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`; asersi 'tepat 8 baris' mengandaikan seluruh baris tampil dalam satu halaman.
- Data dinamis: tidak ada field yang disimpan; nilai yang hanya diketik: Field Name kosong, tiga spasi, dan `No Type {runId}-024`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-60: Field Name kosong ditolak saat Submit dengan pesan wajib diisi

1. Klik `[+ Custom Field]`
2. Biarkan Field Name kosong dan pilih Data Type `Text`
3. Klik `[Submit]`
4. Verifikasi pesan inline `Field name must not be empty` tampil di bawah input Field Name
5. Verifikasi modal tetap terbuka
6. Verifikasi tidak ada toast

#### TC-FA-CF-61: Field Name berisi spasi saja ditolak sebagai kosong setelah trim

7. Klik `[Clear Field]`
8. Ketik tiga spasi pada Field Name dan pilih Data Type `Text`
9. Klik `[Submit]`
10. Verifikasi pesan inline `Field name must not be empty` tampil
11. Verifikasi modal tetap terbuka

#### TC-FA-CF-71: Data Type tidak dipilih ditolak saat Submit

12. Klik `[Clear Field]`
13. Isi Field Name `No Type {runId}-024` tanpa memilih Data Type
14. Klik `[Submit]`
15. Verifikasi pesan inline `Data type must not be empty` tampil
16. Verifikasi modal tetap terbuka

#### Penutupan form dan pemeriksaan tabel

17. Klik `[✕]`
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`
20. Verifikasi tabel tab General memuat 8 baris (TC-FA-CF-60 butir b: tidak ada field baru di tabel)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus (halaman yang sama dipakai berulang; kasus hanya mengetik tanpa membuat data) dan penutupan form dirty pada langkah 17 dan dua langkah berikutnya (S-08). Satu-satunya kejadian menutup modal adalah langkah 17.
- Asersi 'tidak ada field baru di tabel' (TC-FA-CF-60 butir b) ditulis sesudah modal ditutup memakai jumlah baris tab General (8, seed Pre-setup #12) karena tabel tidak teramati selama modal terbuka.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
  - TC-FA-CF-60 butir b menyebut 'tidak ada toast' tanpa anchor positif; spec menulisnya segera setelah pesan inline tampil (8b butir 11).
