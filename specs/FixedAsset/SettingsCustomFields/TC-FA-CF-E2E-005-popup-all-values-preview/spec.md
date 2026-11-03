---
id: TC-FA-CF-E2E-005-popup-all-values-preview
title: "Popup All Values Preview: Buka, Tutup, dan Varian"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-15
  - TC-FA-CF-16
  - TC-FA-CF-17
  - TC-FA-CF-18
coverage:
  web: automated
---

# Popup All Values Preview: Buka, Tutup, dan Varian

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12; dipakai: `Equipment Class` Dropdown opsi `Class A`, `Class B`, `Class C` dengan Scope `Compressor`, `Generator`, `Pump`, dan `Storage Capacity` Numeric 0 Decimal Places), dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral`. Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-15: Chip +N more pada Value Setting membuka Popup All Values Preview

1. Klik chip `+1 more` baris `Equipment Class` kolom Value Setting
2. Verifikasi Popup `All Values` terbuka
3. Verifikasi baris identitas `Equipment Class (3)` tampil di bawah judul popup
4. Verifikasi badge `Class A`, `Class B`, dan `Class C` tampil penuh dalam urutan penambahan
5. Verifikasi tidak ada aksi selain icon close pada popup
6. Tutup popup dengan icon close

### TC-FA-CF-16: Chip +N more pada Scope membuka Popup varian All Asset Names

7. Klik chip `+1 more` baris `Equipment Class` kolom Scope
8. Verifikasi Popup `All Asset Names` terbuka
9. Verifikasi baris identitas `Equipment Class (3)` tampil di bawah judul popup
10. Verifikasi badge `Compressor`, `Generator`, dan `Pump` tampil penuh
11. Tutup popup dengan icon close

### TC-FA-CF-17: Popup ditutup lewat icon close dan Esc tetapi tidak oleh klik di luar popup

12. Klik chip `+1 more` baris `Equipment Class` kolom Value Setting
13. Klik area di luar popup
14. Verifikasi popup tetap terbuka setelah klik di luar popup
15. Klik icon close
16. Verifikasi popup tertutup
17. Klik chip `+1 more` baris `Equipment Class` kolom Value Setting
18. Tekan `Esc`
19. Verifikasi popup tertutup

### TC-FA-CF-18: Value Setting Numeric tidak membuka popup

20. Klik teks `0 Decimal Places` baris `Storage Capacity`
21. Verifikasi tidak ada popup yang terbuka
22. Verifikasi tabel tidak berubah

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec hanya membaca; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 dan 11 (menutup popup yang baru diverifikasi dengan icon close sebelum TC berikutnya, S-09).
- Langkah 17 membuka popup lagi sesuai langkah 5 TC-FA-CF-17 ("Buka popup lagi lalu tekan Esc"); popup pada langkah 12 sudah ditutup di langkah 15.
- Popup ditutup hanya lewat icon close atau Esc; klik di luar popup tidak menutupnya (NC-04 terkonfirmasi di TC).
- Langkah 16 dan 19 (popup tertutup) beranchor langkah 14 yang membuktikan popup terbuka pada surface yang sama sebelum ditutup.
- Temuan untuk QA:
  - TC-FA-CF-18 Expected "tabel tidak berubah" tidak menyebut apa yang dibandingkan; langkah 22 diasersi atas keadaan tabel yang tampil (baris dan sel tidak berubah dibanding sebelum klik) dan kriterianya diputuskan penulis skrip.
