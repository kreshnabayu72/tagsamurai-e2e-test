---
id: TC-FA-FAAM-E2E-029-create-tag-type-opsi-dan-mutual-exclusion
title: "Create: Opsi TAG Type dan Pilihan Non-TAG Saling Menggantikan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-107
  - TC-FA-FAAM-108
  - TC-FA-FAAM-109
coverage:
  web: automated
---

# Create: Opsi TAG Type dan Pilihan Non-TAG Saling Menggantikan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data: tidak ada record yang dibuat; client utama memiliki subscription Paid (Pre-setup #10) sehingga seluruh opsi TAG Type dapat dipilih.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan di akhir spec.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka

### TC-FA-FAAM-107: Opsi TAG Type berisi 6 opsi

2. Buka dropdown TAG Type
3. Verifikasi Opsi berurutan `RFID`, `NFC`, `QR`, `BLE`, `GPS`, `Non-TAG`
4. Verifikasi Dropdown TAG Type searchable multi-select

### TC-FA-FAAM-109: Memilih satu tipe TAG mengosongkan Non-TAG tanpa menonaktifkan opsi lain

5. Pilih `Non-TAG`
6. Pilih `QR`
7. Verifikasi Chip `Non-TAG` hilang
8. Verifikasi Chip `QR` tampil
9. Verifikasi Tidak ada opsi yang di-Disabled oleh aturan saling lepas

### TC-FA-FAAM-108: Memilih Non-TAG mengosongkan kelima tipe TAG

10. Pilih `RFID` (`QR` sudah terpilih)
11. Pilih `Non-TAG`
12. Verifikasi Chip `RFID` dan `QR` hilang
13. Verifikasi Chip `Non-TAG` tampil
14. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Urutan TC dalam spec: TC-FA-FAAM-109 sebelum TC-FA-FAAM-108 supaya `QR` sudah terpilih saat TC-FA-FAAM-108 mulai (langkah "Pilih `RFID` dan `QR`" milik TC-FA-FAAM-108 dipenuhi oleh `QR` dari TC-FA-FAAM-109 dan `RFID` yang dipilih pada langkah ini); form tidak dibuka ulang.
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
