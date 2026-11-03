---
id: TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon
title: "Create: Chip TAG Type, Search Dropdown, dan Default Addon (Opsi, Disabled Non-TAG, Terkunci)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-114
  - TC-FA-FAAM-115
  - TC-FA-FAAM-116
  - TC-FA-FAAM-117
  - TC-FA-FAAM-118
  - TC-FA-FAAM-119
coverage:
  web: automated
---

# Create: Chip TAG Type, Search Dropdown, dan Default Addon (Opsi, Disabled Non-TAG, Terkunci)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): client utama dengan subscription Paid (Pre-setup #10) dan lisensi addon `Maps` tidak teralokasi aktif (Pre-setup #10b).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan di akhir spec.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka

### TC-FA-FAAM-114: Chip TAG Type muncul di dalam field dan dapat dilepas dari dua arah

2. Pilih `RFID` lalu `QR`
3. Verifikasi Chip `RFID` dan `QR` muncul berdampingan di dalam field TAG Type
4. Klik `(✕)` pada chip `RFID`
5. Verifikasi Chip `RFID` terhapus
6. Buka dropdown TAG Type
7. Verifikasi Checkbox `RFID` ter-uncheck
8. Verifikasi Chip `QR` tetap
9. Uncheck `QR` di dropdown
10. Verifikasi Chip `QR` terhapus

### TC-FA-FAAM-115: Search internal dropdown TAG Type

11. Ketik `nf` pada kotak pencarian dropdown TAG Type
12. Verifikasi Daftar menyempit ke `NFC` (substring tanpa membedakan huruf besar-kecil)
13. Ganti isi kotak pencarian dropdown dengan `zzz`
14. Verifikasi Pencarian tanpa kecocokan menampilkan teks `No results found`
15. Tutup dropdown TAG Type lalu pilih `QR`

### TC-FA-FAAM-116, 119: Opsi Default Addon dan opsi terkunci

16. Buka dropdown Default Addon
17. Verifikasi Opsi `Audit`, `Maintenance`, `Tracking`, `Maps` tampil berurutan
18. Verifikasi Field Default Addon boleh dikosongkan (caption tanpa tanda wajib `*`)
19. Hover opsi `Maps`
20. Verifikasi Opsi `Maps` terkunci 🔒 dengan tooltip `Requires an active Maps license`

### TC-FA-FAAM-118, 117: Non-TAG mengosongkan dan menonaktifkan Default Addon

21. Pilih Default Addon `Audit`, lalu pilih TAG Type `Non-TAG`
22. Verifikasi Chip `Audit` di Default Addon hilang
23. Verifikasi Field Default Addon Disabled
24. Hover field Default Addon
25. Verifikasi Field Default Addon Disabled dengan tooltip `Non-TAG asset names cannot have a default addon.`
26. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Urutan TC dalam spec dan alasannya (S-10): TC-FA-FAAM-114 dan 115 lebih dahulu (TAG Type bebas), lalu TC-FA-FAAM-116 dan 119 (membaca dropdown Default Addon yang sama pada TAG Type `QR`, sehingga dua TC itu berbagi satu pembukaan dropdown), dan TC-FA-FAAM-118 sebelum 117 karena chip `Audit` harus ada sebelum Non-TAG dipilih; form dibuka sekali.
- Pilihan `QR` pada langkah penghubung "Tutup dropdown TAG Type lalu pilih `QR`" menyiapkan TAG Type bukan Non-TAG supaya Default Addon aktif (tanpa `Verifikasi`).
- TC-FA-FAAM-116 Expected b "Field boleh dikosongkan" tidak punya langkah uji; spec mengasersi bahwa caption Default Addon tidak bertanda wajib `*`, konsisten dengan screening TC-FA-FAAM-66.
- Dua `Verifikasi` Disabled pada TC-FA-FAAM-118 dan TC-FA-FAAM-117 mengamati keadaan yang sama sebelum dan sesudah hover karena tooltip hanya muncul saat hover (bagian 8b butir 5).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
