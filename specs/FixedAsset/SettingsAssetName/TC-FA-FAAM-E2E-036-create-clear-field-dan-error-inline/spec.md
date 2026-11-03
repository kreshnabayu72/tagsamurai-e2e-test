---
id: TC-FA-FAAM-E2E-036-create-clear-field-dan-error-inline
title: "Create: Clear Field Mengosongkan Semua Field dan Menghapus Error Inline"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-69
  - TC-FA-FAAM-70
coverage:
  web: automated
---

# Create: Clear Field Mengosongkan Semua Field dan Menghapus Error Inline

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis: Asset Name `Create Min Item {runId}-036` hanya diketik dan tidak tersimpan (tidak ada Submit pada isian terisi).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat.

## Test Steps

### TC-FA-FAAM-70: Clear Field menghapus pesan error inline dan border merah

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Klik `[Submit]` dengan semua field kosong
3. Verifikasi Pesan error inline tampil pada field wajib
4. Klik `[Clear Field]`
5. Verifikasi Pesan error inline hilang dari semua field
6. Verifikasi Border merah hilang dari semua field
7. Verifikasi Form kembali pristine (semua field kosong dengan placeholder tampil)

### TC-FA-FAAM-69: Clear Field mengosongkan semua field tanpa dialog dan mempertahankan checkbox Stay

8. Isi Asset Name `Create Min Item {runId}-036`
9. Klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`
10. Pilih TAG Type `QR`
11. Pilih Brand `Dell`
12. Pilih UoM `Unit`
13. Centang `Stay on this form after submitting`
14. Klik `[Clear Field]`
15. Verifikasi Semua field kosong dan placeholder tampil
16. Verifikasi Tabel Model/Type per Brand hilang
17. Verifikasi Checkbox Stay tetap tercentang
18. Verifikasi Modal tetap terbuka tanpa dialog `Unsaved Changes`
19. Verifikasi Fokus berada di field Asset Name
20. Klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Urutan TC dalam spec: TC-FA-FAAM-70 sebelum TC-FA-FAAM-69 (kasus tanpa isian lebih dahulu); popup dibuka sekali.
- TC-FA-FAAM-70 Expected "Form kembali pristine" ditulis sebagai `Verifikasi` semua field kosong dengan placeholder; asersi tambahan tidak ada.
- Langkah penghubung (tanpa `Verifikasi`): `[✕]` pada langkah terakhir menutup form bersih (S-09); Stay yang tercentang adalah state popup dan hilang saat popup ditutup.
- Temuan untuk QA:
  - TC-FA-FAAM-70 Expected b ("Form kembali pristine") tidak mendefinisikan arti pristine; spec mengasersi tampilan kosong dengan placeholder.
