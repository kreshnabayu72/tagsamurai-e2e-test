---
id: TC-FA-CF-E2E-026-field-name-emoji-dan-simbol
title: "Field Name: Emoji dan Simbol Umum"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-65
  - TC-FA-CF-66
  - TC-FA-CF-67
coverage:
  web: automated
---

# Field Name: Emoji dan Simbol Umum

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- N total baris tab General = 8 diturunkan dari seeding Pre-setup #12 (8b butir 10): `Asset Serial Tag`, `Storage Capacity`, `Equipment Class`, `Operating Voltage`, `Total Cost`, `Depreciated Ratio`, `Compliance File`, `Legacy Tag`; asersi 'tepat 8 baris' mengandaikan seluruh baris tampil dalam satu halaman.
- Kemampuan teknis: injeksi nilai langsung ke DOM input (Pre-setup #26, disediakan tim FE).
- Data dinamis (dibuat lewat UI oleh spec ini): D-1 Field Name `Pump Rating (kW) / Max-Load & #1 {runId}-026`, Data Type Text. Nilai yang hanya diketik dan tidak pernah tersimpan: `Asset😊Tag` (diketik, ditempel `🔥`, dan diinjeksi ke DOM).
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-026`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-65: Emoji pada Field Name diblok saat mengetik dan menempel tanpa pesan

1. Klik `[+ Custom Field]`
2. Ketik `Asset😊Tag` pada Field Name
3. Tempel `🔥` pada Field Name
4. Verifikasi karakter emoji tidak pernah masuk ke input Field Name
5. Verifikasi tidak ada pesan error yang tampil

#### TC-FA-CF-66: Emoji yang lolos filter klien pada Field Name ditolak dengan pesan karakter terlarang

6. Klik `[Clear Field]`
7. Injeksi nilai `Asset😊Tag` langsung ke DOM input Field Name (melewati filter keystroke)
8. Pilih Data Type `Text`
9. Klik `[Submit]`
10. Verifikasi pesan inline `Field name contains invalid characters` tampil
11. Verifikasi modal tetap terbuka
12. Klik `[✕]`
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`
15. Verifikasi tabel tab General memuat 8 baris (field tidak tersimpan)

#### TC-FA-CF-67: Field Name dengan tanda baca dan simbol umum diterima

16. Klik `[+ Custom Field]`
17. Isi Field Name `Pump Rating (kW) / Max-Load & #1 {runId}-026`
18. Pilih Data Type `Text`
19. Klik `[Submit]`
20. Verifikasi toast sukses: "Success, custom field has been created."
21. Ketik Search `{runId}-026`, tekan Enter
22. Verifikasi baris dengan Field Name `Pump Rating (kW) / Max-Load & #1 {runId}-026` tampil utuh di tabel
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` setelah TC-FA-CF-65 (mengosongkan Field Name yang berisi `Asset`), penutupan form dirty pada langkah 12 dan dua langkah berikutnya (S-08, memeriksa tabel sebelum TC-FA-CF-67 menambah baris), Search pada langkah 21 untuk menemukan baris target (R-16), dan `Klik (←)` untuk mereset Search.
- Field Dinamis bernama bersuffix `{runId}-026` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- P-5: TC-FA-CF-66 (emoji yang lolos filter klien lewat injeksi DOM) adalah satu TC objek-uji ringan kelas a tanpa harness eksternal dan tanpa state berat, ditaruh di spec fungsional Field Name yang permukaannya sama (P-5 butir b).
- Asersi 'Field tidak tersimpan' pada TC-FA-CF-66 memakai jumlah baris tab General (8, seed Pre-setup #12) setelah form ditutup.
- Temuan untuk QA:
  - TC tidak menyebut ukuran halaman default tabel; asersi jumlah baris tab General (8) mengandaikan seluruh baris tampil dalam satu halaman.
  - Spec dikelompokkan dengan caseType Negative karena dua dari tiga TC menguji penolakan emoji; TC-FA-CF-67 bertipe Positive.
