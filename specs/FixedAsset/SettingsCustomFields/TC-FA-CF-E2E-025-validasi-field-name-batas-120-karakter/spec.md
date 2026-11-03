---
id: TC-FA-CF-E2E-025-validasi-field-name-batas-120-karakter
title: "Validasi Field Name Batas 120 Karakter dan Spasi di Ujung"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-63
  - TC-FA-CF-62
  - TC-FA-CF-64
coverage:
  web: automated
---

# Validasi Field Name Batas 120 Karakter dan Spasi di Ujung

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- N total baris tab General = 8 diturunkan dari seeding Pre-setup #12 (8b butir 10): `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`; asersi 'tepat 8 baris' mengandaikan seluruh baris tampil dalam satu halaman.
- Data dinamis (dibuat lewat UI oleh spec ini; `{runId}` terdiri atas digit; panjang dihitung termasuk suffix):
  - D-025a: Field Name = huruf `A` diulang + ` {runId}-025` sehingga panjang tepat 120 karakter; Data Type Text.
  - D-025b: Field Name = huruf `B` diulang + ` {runId}-025` sehingga panjang tepat 120 karakter, diikuti 5 spasi di akhir saat diketik; Data Type Text.
  - Nilai yang hanya diketik dan tidak pernah tersimpan: 121 huruf `A` pada Field Name.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-025`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-63: Field Name 121 karakter menampilkan pesan batas saat mengetik dan Submit ditolak

1. Klik `[+ Custom Field]`
2. Ketik Field Name 121 karakter (huruf `A` diulang 121 kali)
3. Verifikasi pesan inline `Max. 120 characters` tampil langsung saat karakter ke-121 diketik
4. Pilih Data Type `Text`
5. Klik `[Submit]`
6. Verifikasi modal tetap terbuka
7. Klik `[✕]`
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`
10. Verifikasi tabel tab General memuat 8 baris (Submit tidak menyimpan field)

#### TC-FA-CF-62: Field Name tepat 120 karakter diterima

11. Klik `[+ Custom Field]`
12. Ketik Field Name D-025a (huruf `A` diulang sehingga total 120 karakter termasuk ` {runId}-025`)
13. Verifikasi pesan inline `Max. 120 characters` tidak tampil
14. Pilih Data Type `Text`
15. Klik `[Submit]`
16. Verifikasi toast sukses: "Success, custom field has been created."
17. Ketik Search `{runId}-025`, tekan Enter
18. Verifikasi baris dengan Field Name D-025a tampil di tabel

#### TC-FA-CF-64: Spasi di ujung Field Name tidak dihitung ke batas 120 karakter

19. Klik `[+ Custom Field]`
20. Ketik Field Name D-025b (huruf `B` diulang sehingga total 120 karakter termasuk ` {runId}-025`) lalu 5 spasi di akhir
21. Verifikasi pesan inline `Max. 120 characters` tidak tampil
22. Pilih Data Type `Text` dan klik `[Submit]`
23. Ganti isi kotak search dengan `{runId}-025`, tekan Enter
24. Verifikasi baris dengan Field Name D-025b tampil di tabel
25. Klik row action `⋯` > `Edit` pada baris D-025b
26. Verifikasi Field Name pada form Edit berisi D-025b (120 karakter) tanpa spasi akhir
27. Klik `[✕]`
28. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 63, 62, 64 (urutan sumber 62, 63, 64). Validasi yang diblokir didahulukan sebelum aksi yang membuat data (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan form dirty pada langkah 7 dan dua langkah berikutnya (S-08); Search `{runId}-025` untuk menemukan baris target (R-16, langkah 17 dan 23); `Pilih Data Type` dan `Klik [Submit]` sebagai bagian langkah TC; `Klik [✕]` menutup form Edit yang tidak diubah (tanpa dialog) dan `Klik (←)` mereset Search.
- Field Dinamis bernama bersuffix `{runId}-025` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca. Panjang tepat 120 karakter pada D-025a dan D-025b sudah termasuk suffix sehingga batas yang diuji tidak berubah (R-06).
- Asersi 'Submit tidak menyimpan field' pada TC-FA-CF-63 memakai jumlah baris tab General (8, seed Pre-setup #12) setelah form ditutup.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
  - TC-FA-CF-64 butir b 'Field tersimpan' tidak menyebut toast; spec mengasersi baris tampil di tabel dan nilai pada form Edit saja.
