---
id: TC-FA-RP-E2E-259-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-2
title: "Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (2/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-866
  - TC-FA-RP-869
  - TC-FA-RP-870
  - TC-FA-RP-871
coverage:
  web: automated
---

# Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (2/5)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi, Budi Santoso, dan Dimas Pranata sebagai Standard tanpa tingkat akses; Ahmad Fauzi dan Budi Santoso memegang Global Role `Manage accounting` dengan Create dan Update nonaktif untuk TC-FA-RP-869 sampai 871) dan #39 (Detail Role Global Role `Manage accounting` terisi, termasuk baris Ahmad Fauzi).
- Baseline audit trail (S-12): jumlah entri Changelog, System Log, dan Activity Log dicatat sebelum aksi lewat kemampuan baca yang disediakan tim FE/BE (UI atau fixture BE); asersi memakai selisih terhadap baseline, bukan angka absolut dan bukan posisi teratas.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-866: Assign multi-select menulis satu entri per user pada tiap surface

1. Catat baseline (aksi tanpa `Verifikasi`):
   - Tab Total Control > ikon Changelog di toolbar: jumlah entri Action `Assign`
   - Settings > User > Detail Siti Rahmawati > Tab System Log: jumlah entri Action `Assign` Object `Total Control`
   - Activity Log FAMS (menu Activity Log): jumlah entri Action `Assign` Object `Total Control`
2. Buka Fixed Asset > Settings > Role & Permission > Tab Total Control
3. Klik `[+ Assign]` di Tab Total Control
4. Centang Ahmad Fauzi, Budi Santoso, dan Dimas Pranata lalu klik `[Assign]`
5. Tunggu aksi selesai: popup tertutup
6. Klik ikon Changelog di toolbar Tab Total Control
7. Verifikasi modal Changelog memuat tiga entri `Assign` baru terpisah (satu per user; selisih tiga terhadap baseline)
8. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
9. Verifikasi System Log memuat tiga entri baru Action `Assign` Object `Total Control` (selisih tiga terhadap baseline)
10. Buka Activity Log FAMS (menu Activity Log)
11. Verifikasi Activity Log memuat tiga entri baru Action `Assign` Object `Total Control` (selisih tiga terhadap baseline)

### TC-FA-RP-869 dan TC-FA-RP-871: satu aksi Edit Create pada baris Ahmad Fauzi

12. Pulihkan Ahmad Fauzi, Budi Santoso, dan Dimas Pranata ke state Precondition lewat seeding API hingga tersimpan (Standard tanpa tingkat akses; Ahmad Fauzi dan Budi Santoso memegang `Manage accounting` dengan Create nonaktif)
13. Buka Tab System, lalu Detail Role `Manage accounting`
14. Catat baseline (aksi tanpa `Verifikasi`): klik ikon Changelog di toolbar Detail Role, catat jumlah entri Action `Edit` Field `Create` untuk Ahmad Fauzi dan untuk Budi Santoso, lalu tutup modal
15. Centang Create pada baris Ahmad Fauzi
16. Tunggu aksi selesai: perubahan Create tersimpan
17. Klik ikon Changelog di toolbar Detail Role

### TC-FA-RP-869: Satu perubahan CRUD menghasilkan tepat satu entri per bidang yang berubah

18. Verifikasi modal memuat tepat satu entri baru Action `Edit` Field `Create` untuk Ahmad Fauzi (selisih satu terhadap baseline; tidak ada entri ganda)

### TC-FA-RP-871: Aksi pada satu user tidak menghasilkan entri untuk user lain

19. Verifikasi modal tidak memuat entri baru untuk Budi Santoso (jumlah entri Budi Santoso sama dengan baseline)

### TC-FA-RP-870: Dua bidang berubah pada dua aksi menghasilkan entri untuk kedua bidang

20. Tutup modal, lalu pulihkan baris Ahmad Fauzi ke Create dan Update nonaktif lewat seeding API hingga tersimpan
21. Buka Tab System, lalu Detail Role `Manage accounting`
22. Catat baseline (aksi tanpa `Verifikasi`): klik ikon Changelog di toolbar Detail Role, catat jumlah entri Action `Edit` Field `Create` dan Field `Update` untuk Ahmad Fauzi, lalu tutup modal
23. Centang Create lalu centang Update pada baris Ahmad Fauzi
24. Tunggu aksi selesai: kedua perubahan tersimpan
25. Klik ikon Changelog di toolbar Detail Role
26. Verifikasi modal memuat entri baru Action `Edit` Field `Create` untuk Ahmad Fauzi
27. Verifikasi modal memuat entri baru Action `Edit` Field `Update` untuk Ahmad Fauzi

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 27 langkah.
- TC-FA-RP-869 dan 871 punya precondition dan aksi yang sama (centang Create pada baris Ahmad Fauzi di `Manage accounting`); aksi dijalankan satu kali dan tiap TC mengasersi Expected-nya. TC-FA-RP-870 memakai pemulihan baris sebelum aksinya karena Create sudah aktif sesudah TC-FA-RP-869. Urutan TC dalam spec: 866, 869, 871, 870 (alasan: 870 membutuhkan pemulihan baris sesudah aksi 869).
- Langkah penghubung (S-03): pencatatan baseline, pemulihan lewat seeding API, pembukaan tab dan Detail Role, dan "Tunggu aksi selesai". Akun aktor pertama sudah login di hook `before` (S-07).
- Asersi "tidak memuat entri baru untuk Budi Santoso" (TC-FA-RP-871) ditulis sebagai kesamaan jumlah terhadap baseline pada aksi yang sukses, dengan entri baru Ahmad Fauzi (langkah sebelumnya) sebagai anchor; bukan kelas absence (bagian 3 prinsip 13 butir g).
- Temuan untuk QA:
  - Precondition TC-FA-RP-869, 870, dan 871 merujuk Pre-setup #15, #39, dan #24 (Company Changelog); spec berjalan di Company Alpha dengan baseline selisih, sehingga isi 25 entri #24 tidak dibutuhkan. Baris Ahmad Fauzi pada `Manage accounting` (Pre-setup #39) di-seed lewat seeding API.
  - TC-FA-RP-866 Expected tidak menyebut Object entri System Log dan Activity Log; spec memakai Object `Total Control` mengikuti pola System Log pada TC-FA-RP-851 sampai 856.
  - Post Condition TC-FA-RP-866, 869, 870, dan 871 kosong; tidak ada yang diasersi.
