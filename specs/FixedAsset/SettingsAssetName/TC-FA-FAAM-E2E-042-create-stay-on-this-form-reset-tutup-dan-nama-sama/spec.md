---
id: TC-FA-FAAM-E2E-042-create-stay-on-this-form-reset-tutup-dan-nama-sama
title: "Create: Stay on this Form Tercentang dan Tidak, serta Dua Create Nama Sama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-150
  - TC-FA-FAAM-151
  - TC-FA-FAAM-152
coverage:
  web: automated
---

# Create: Stay on this Form Tercentang dan Tidak, serta Dua Create Nama Sama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item 150 {runId}-042`, `Create Min Item 152 {runId}-042` (dua kali dikirim), dan `Create Min Item 151 {runId}-042`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga Asset Name milik spec ini bila masih ada.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka

### TC-FA-FAAM-150: Stay on this form tercentang mereset form dan membiarkan modal terbuka

2. Isi field wajib: Asset Name `Create Min Item 150 {runId}-042`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
3. Centang `Stay on this form after submitting`
4. Klik `[Submit]`
5. Verifikasi Toast `Success, asset name has been created.` tampil
6. Verifikasi Form di-reset kosong
7. Verifikasi Modal tetap terbuka
8. Verifikasi Checkbox Stay tetap tercentang

### TC-FA-FAAM-152: Dua Create berturut-turut dengan Stay aktif memakai nama sama ditolak pada yang kedua

9. Isi field wajib: Asset Name `Create Min Item 152 {runId}-042`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
10. Klik `[Submit]`
11. Verifikasi Create pertama sukses: toast `Success, asset name has been created.` tampil
12. Tunggu toast lama hilang otomatis
13. Isi field wajib: Asset Name `Create Min Item 152 {runId}-042`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
14. Klik `[Submit]`
15. Verifikasi Create kedua menampilkan error inline `Asset name already exists`

### TC-FA-FAAM-151: Stay tidak tercentang menutup modal dan merefresh tabel

16. Klik `[Clear Field]`
17. Hilangkan centang `Stay on this form after submitting`
18. Isi field wajib: Asset Name `Create Min Item 151 {runId}-042`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
19. Klik `[Submit]`
20. Verifikasi Modal tertutup
21. Ketik Search `{runId}-042`, tekan Enter
22. Verifikasi Tabel menampilkan baris baru `Create Min Item 151 {runId}-042`
23. Verifikasi Baris `Create Min Item 150 {runId}-042` ada di List (dibuat di balik modal saat Stay tercentang)
24. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Urutan TC dalam spec (S-10): TC-FA-FAAM-150 dan 152 berbagi pembukaan form dengan Stay tercentang; TC-FA-FAAM-151 terakhir karena menutup modal. TC-FA-FAAM-150 butir d diperiksa pada langkah Search di akhir (baris dibuat di balik modal).
- Langkah "Tunggu toast lama hilang otomatis" adalah langkah penghubung tanpa `Verifikasi` (R-12); toast sukses TC-FA-FAAM-152 tidak dihitung ulang.
- Search `{runId}-042` adalah langkah penghubung untuk menemukan baris milik spec ini (R-16).
