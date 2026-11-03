---
id: TC-FA-RP-E2E-313-aksesibilitas-dialog-konfirmasi-fokus-terkunci-dan-esc-setara-cancel
title: "Aksesibilitas dialog konfirmasi: fokus terkunci dan Esc setara Cancel"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1009
coverage:
  web: automated
---

# Aksesibilitas dialog konfirmasi: fokus terkunci dan Esc setara Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #18 (pohon group), #36 (Tab Total Control: Rina Wulandari), #38 (Tab Group Manager: Kevin Susanto di `Data Center`), #39 (Detail Role `Manage Open API`: Budi Santoso). Identitas data dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: Navigasi keyboard (Tab dan Esc) pada dialog konfirmasi.
- State yang diubah dan pemulihannya: Tidak ada state yang diubah: ketiga dialog ditutup dengan Esc tanpa konfirmasi.
- Seeding dan pemulihan: kondisi precondition tiap TC dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1009: Dialog konfirmasi: fokus terkunci di dalam dialog dan Esc setara Cancel

1. Klik `[⋯]` baris Rina Wulandari di Tab `Total Control` lalu `Remove`
2. Tekan Tab berulang melewati seluruh elemen dialog `Remove Total Control`
3. Verifikasi fokus tidak keluar dari dialog `Remove Total Control`
4. Tekan Esc
5. Verifikasi tidak ada toast
6. Verifikasi dialog `Remove Total Control` tertutup (Esc setara `[Cancel]`)
7. Verifikasi baris Rina Wulandari tetap ada di Tab `Total Control`
8. Klik Tab `Group Manager`
9. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`
10. Tekan Tab berulang melewati seluruh elemen dialog `Remove Group Manager`
11. Verifikasi fokus tidak keluar dari dialog `Remove Group Manager`
12. Tekan Esc
13. Verifikasi tidak ada toast
14. Verifikasi dialog `Remove Group Manager` tertutup (Esc setara `[Cancel]`)
15. Verifikasi baris Kevin Susanto di `Data Center` tetap ada
16. Klik Tab `System`
17. Buka Detail Role `Manage Open API`
18. Klik `[⋯]` baris Budi Santoso lalu `Remove`
19. Tekan Tab berulang melewati seluruh elemen dialog `Remove User`
20. Verifikasi fokus tidak keluar dari dialog `Remove User`
21. Tekan Esc
22. Verifikasi tidak ada toast
23. Verifikasi dialog `Remove User` tertutup (Esc setara `[Cancel]`)
24. Verifikasi baris Budi Santoso tetap ada

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 24 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8, 16. Akun aktor pertama sudah login di hook `before` (S-07).
- TC-FA-RP-1009 langkah 4 dan 5 ("ulangi langkah 1 sampai 3") ditulis ulang sebagai langkah eksplisit untuk dialog `Remove Group Manager` dan `Remove User`.
- Asersi absence toast diletakkan segera setelah pemicu Esc (bagian 8b butir 11); penutupan dialog dan baris yang tetap ada menjadi anchor positif.
- Aksesibilitas keyboard dan slot toast pada checkbox Detail Role ada di spec 242.
- Temuan untuk QA:
  - TC-FA-RP-1009 Expected menulis judul dialog hanya sebagai `Remove Total Control` (D-01), `Remove Group Manager` (D-02), dan `Remove User` (D-03) lewat kode dialog; spec memakai judul itu sebagai nama dialog tanpa memverifikasi judulnya.
