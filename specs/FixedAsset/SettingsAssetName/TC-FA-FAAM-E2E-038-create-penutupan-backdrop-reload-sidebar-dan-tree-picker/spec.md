---
id: TC-FA-FAAM-E2E-038-create-penutupan-backdrop-reload-sidebar-dan-tree-picker
title: "Create: Backdrop, Field Dikembalikan, Reload F5, Navigasi Sidebar, dan Esc pada Tree Picker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-76
  - TC-FA-FAAM-77
  - TC-FA-FAAM-78
  - TC-FA-FAAM-79
  - TC-FA-FAAM-80
coverage:
  web: automated
---

# Create: Backdrop, Field Dikembalikan, Reload F5, Navigasi Sidebar, dan Esc pada Tree Picker

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Kemampuan teknis (disediakan tim FE): penanganan dialog bawaan browser `beforeunload` (menerima atau membatalkan reload) agar langkah muat ulang saat form terisi deterministik (S-08).
- Data uji: Asset Name `Backdrop Item`, `Nav Item`, `Reload Item` hanya diketik dan tidak pernah tersimpan.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan eksplisit.

## Test Steps

### TC-FA-FAAM-76: Klik backdrop Popup Create terisi tidak menutup modal

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi Asset Name `Backdrop Item`
3. Klik area gelap di luar modal
4. Verifikasi Modal tetap terbuka dengan input dipertahankan
5. Verifikasi Dialog Unsaved Changes tidak muncul

### TC-FA-FAAM-77: Field diubah lalu dikembalikan identik dianggap bersih

6. Klik `[Clear Field]`
7. Ketik `A` di Asset Name lalu hapus dengan Backspace sampai kosong
8. Klik `[✕]`
9. Verifikasi Modal langsung tertutup
10. Verifikasi Dialog Unsaved Changes tidak muncul

### TC-FA-FAAM-80: Esc pada Tree Picker di atas form hanya menutup Tree Picker

11. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
12. Klik `[Select Category]`
13. Tekan Esc
14. Verifikasi Tree Picker tertutup
15. Verifikasi Dialog tidak muncul saat Tree Picker ditutup
16. Verifikasi Field Category tetap `No category selected`
17. Verifikasi Popup Create tetap terbuka

### TC-FA-FAAM-79: Navigasi sidebar saat form terisi memunculkan Unsaved Changes

18. Isi Asset Name `Nav Item`
19. Klik menu sidebar lain
20. Verifikasi Dialog Unsaved Changes dengan `[Cancel]` dan `[Leave]` tampil sebelum route berubah
21. Klik `[Cancel]`

### TC-FA-FAAM-78: Reload F5 saat form terisi memunculkan konfirmasi bawaan browser

22. Ganti isi Asset Name dengan `Reload Item`
23. Tekan F5
24. Verifikasi Konfirmasi bawaan browser (`beforeunload`) muncul
25. Batalkan reload (pilih tetap di halaman pada konfirmasi browser)
26. Klik `[Clear Field]`
27. Tekan F5
28. Verifikasi Halaman Fixed Asset > Settings > Asset Master > Asset Name termuat ulang
29. Verifikasi Konfirmasi bawaan browser tidak muncul saat form bersih

## Notes

- Urutan TC dalam spec (S-10): backdrop (TC-FA-FAAM-76), field dikembalikan (TC-FA-FAAM-77), Tree Picker (TC-FA-FAAM-80), sidebar (TC-FA-FAAM-79), dan F5 (TC-FA-FAAM-78) terakhir karena memuat ulang halaman; popup dibuka ulang hanya setelah ditutup oleh TC-FA-FAAM-77.
- Form dirty berakhir dengan pemulihan eksplisit (S-09): Cancel pada dialog sidebar mempertahankan form, `[Clear Field]` mengosongkannya, dan F5 pada form bersih memuat ulang halaman sehingga popup tertutup tanpa dialog.
- Muat ulang saat sesi dirty didahului pembatalan reload (TC-FA-FAAM-78 butir a) dan baru dilakukan pada form bersih sesudah `[Clear Field]` (S-08).
- Temuan untuk QA:
  - TC-FA-FAAM-78 Expected b ("Tidak muncul bila form bersih atau setelah Submit sukses") tidak punya langkah uji; spec mengasersi hanya kasus form bersih (F5 sesudah `[Clear Field]`). Kasus "setelah Submit sukses" tidak diasersi karena TC tidak memberi langkahnya.
  - TC-FA-FAAM-79 tidak menyebut menu sidebar mana yang diklik; spec memakai "menu sidebar lain" apa adanya.
