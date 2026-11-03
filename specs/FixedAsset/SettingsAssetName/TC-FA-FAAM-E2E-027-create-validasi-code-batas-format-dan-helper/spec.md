---
id: TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper
title: "Create: Validasi Code (Batas 15, Format, Kapital Otomatis, Duplikat, Helper Text)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-94
  - TC-FA-FAAM-95
  - TC-FA-FAAM-96
  - TC-FA-FAAM-97
  - TC-FA-FAAM-98
  - TC-FA-FAAM-99
coverage:
  web: automated
---

# Create: Validasi Code (Batas 15, Format, Kapital Otomatis, Duplikat, Helper Text)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): Asset Name #10 `Dell Latitude` ber-Code `DLAT` sebagai Code yang sudah ada.
- Kemampuan teknis (disediakan tim FE): pengamatan jeda 500 ms cek keunikan; spec menunggu 600 ms nyata.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan di akhir spec.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka

### TC-FA-FAAM-99: Helper text Code tetap tampil dan digantikan pesan error saat error aktif

2. Verifikasi Helper `Letters, numbers, hyphens, underscores, and dots only` tampil di bawah Code

### TC-FA-FAAM-94, 95: Batas 15 karakter

3. Ketik Code `ABCDE-FGHIJ.K_L` (15 karakter)
4. Verifikasi Tidak ada error `Max. 15 characters`
5. Ganti isi Code dengan `ABCDE-FGHIJ.K_L5` (16 karakter)
6. Verifikasi Error inline `Max. 15 characters` muncul langsung

### TC-FA-FAAM-96, 97: Format dan kapital otomatis

7. Ganti isi Code dengan `AB CD#`
8. Verifikasi Error inline `Code contains invalid characters` muncul real-time
9. Verifikasi Karakter pada field Code tidak diblok (field tetap berisi `AB CD#`)
10. Ganti isi Code dengan `abc-1`
11. Verifikasi Field Code menampilkan `ABC-1`

### TC-FA-FAAM-99 (lanjutan): Pesan error menggantikan helper

12. Ganti isi Code dengan `A#`
13. Verifikasi Pesan `Code contains invalid characters` menggantikan helper text
14. Ganti isi Code dengan `A`
15. Verifikasi Helper `Letters, numbers, hyphens, underscores, and dots only` kembali tampil

### TC-FA-FAAM-98: Code duplikat menampilkan error saat mengetik

16. Ganti isi Code dengan `dlat` lalu tunggu lebih dari 500 ms
17. Verifikasi Error inline `Code already exists` tampil (pembandingan tidak membedakan huruf besar-kecil)
18. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Urutan TC dalam spec: helper awal (TC-FA-FAAM-99 butir a) sebelum mengetik, lalu batas dan format, helper setelah perbaikan (TC-FA-FAAM-99 butir b), dan cek duplikat terakhir; form tidak dibuka ulang (S-10).
- TC-FA-FAAM-99 diperlakukan dua bagian karena Expected a (helper tampil saat form baru dibuka) dan b (helper kembali setelah diperbaiki) tidak dapat diasersi pada satu keadaan; `Verifikasi` b memakai kode `A` sebagai nilai perbaikan yang valid.
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-99 Expected b menulis "helper kembali setelah diperbaiki" tanpa nilai perbaikan; spec memakai Code `A`.
