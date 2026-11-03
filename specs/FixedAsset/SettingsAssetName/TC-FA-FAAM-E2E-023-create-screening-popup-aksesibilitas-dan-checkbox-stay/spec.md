---
id: TC-FA-FAAM-E2E-023-create-screening-popup-aksesibilitas-dan-checkbox-stay
title: "Create: Screening Popup 3 Zona, Aksesibilitas, dan Checkbox Stay Hanya di Mode Create"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-66
  - TC-FA-FAAM-67
  - TC-FA-FAAM-153
coverage:
  web: automated
---

# Create: Screening Popup 3 Zona, Aksesibilitas, dan Checkbox Stay Hanya di Mode Create

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data yang dibaca (tidak diubah): Asset Name Pre-setup #10 `Dell Latitude` hanya dibuka di Popup Edit lalu ditutup tanpa perubahan (Last Updated tidak berubah, S-06). Spec ini tidak membuat data.
- Kemampuan teknis (disediakan tim FE): pembacaan atribut ARIA (`aria-required`, `aria-describedby`) dan posisi fokus keyboard.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan eksplisit di akhir spec.

## Test Steps

### TC-FA-FAAM-66: Screening Popup Create Asset Name (3 zona)

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Verifikasi Zona Header menampilkan Title `Create Asset Name` dan icon close `[✕]`
3. Verifikasi Zona Body urutan pertama: field Asset Name * dengan placeholder `e.g. Laptop, Forklift, Office Desk`
4. Verifikasi Zona Body urutan kedua: field Code dengan placeholder `Enter code, or leave blank to auto-generate`
5. Verifikasi Helper text di bawah Code berbunyi `Letters, numbers, hyphens, underscores, and dots only`
6. Verifikasi Zona Body urutan ketiga: Category * dengan tombol `[Select Category]` dan teks `No category selected`
7. Verifikasi Zona Body urutan keempat: TAG Type * dengan placeholder `Select TAG type` dan Default Addon dengan placeholder `Select default addon` dalam satu baris
8. Verifikasi Zona Body urutan kelima: Default Label dengan placeholder `Select default label` dan tombol `[➕]`
9. Verifikasi Zona Body urutan keenam: Brand * dengan placeholder `Select brand`
10. Verifikasi Tabel Model/Type per Brand belum tampil
11. Verifikasi Zona Body urutan ketujuh: UoM * dengan placeholder `Select UoM`
12. Verifikasi Zona Footer menampilkan checkbox `Stay on this form after submitting` rata kanan di atas `[Clear Field]` dan `[Submit]` rata kanan
13. Verifikasi Semua field kosong

### TC-FA-FAAM-67: Accessibility Popup Create: aria-required, aria-describedby, focus trap, Esc

14. Verifikasi Field Asset Name, Category, TAG Type, Brand, dan UoM memiliki `aria-required`
15. Kosongkan Asset Name lalu klik `[Submit]`
16. Verifikasi Field yang menampilkan pesan error inline memiliki `aria-describedby` ke pesan itu
17. Tekan Tab berulang kali
18. Verifikasi Fokus tetap terperangkap di dalam modal
19. Tekan Esc
20. Verifikasi Esc pada form bersih menutup modal

### TC-FA-FAAM-153: Checkbox Stay hanya tampil pada mode Create

21. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
22. Verifikasi Popup Create memuat checkbox `Stay on this form after submitting`
23. Klik `[✕]` (form bersih tertutup tanpa dialog)
24. Ketik Search `Dell Latitude`, tekan Enter
25. Buka Edit `Dell Latitude` (klik `⋯` pada baris, lalu `Edit`)
26. Verifikasi Popup Edit tidak memuat checkbox `Stay on this form after submitting`
27. Klik `[✕]` pada Popup Edit (tanpa perubahan, tertutup tanpa dialog), lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Urutan TC di dalam spec: screening Popup Create (TC-FA-FAAM-66) dahulu, lalu aksesibilitas (TC-FA-FAAM-67), terakhir perbandingan mode Create dan Edit (TC-FA-FAAM-153) sesuai S-10.
- Langkah penghubung (tanpa `Verifikasi`): `[✕]` pada langkah 23 menutup form bersih tanpa dialog dan `[✕]` pada langkah 27 menutup Popup Edit tanpa perubahan; Search `Dell Latitude` pada langkah 24 hanya untuk menemukan baris target Edit (R-16) dan ditutup lewat `(←)` pada langkah 27.
- TC-FA-FAAM-67 langkah `Periksa atribut field wajib` diterjemahkan menjadi `Verifikasi` Expected a; tidak ada aksi lain di dalamnya. Kosongkan Asset Name lalu `[Submit]` tidak mengisi apa pun sehingga form tetap bersih saat Esc ditekan (Expected d).
