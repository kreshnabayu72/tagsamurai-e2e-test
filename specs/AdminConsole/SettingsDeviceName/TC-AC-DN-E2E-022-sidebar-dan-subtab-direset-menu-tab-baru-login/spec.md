---
id: TC-AC-DN-E2E-022-sidebar-dan-subtab-direset-menu-tab-baru-login
title: "Sidebar dan Sub-tab: Reset oleh Klik Ulang Menu, Tab Browser Baru, dan Login Ulang"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-626
coverage:
  web: automated
---

# Sidebar dan Sub-tab: Reset oleh Klik Ulang Menu, Tab Browser Baru, dan Login Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Pohon Uji Kategori (#14), Device Name inti (#16), dan seed 120 Device Name (#17); total baris List 130 (9 inti, 120 seed, 1 nama panjang #23) diturunkan dari seeding Pre-setup (bagian 8b butir 10). Baca-saja; tidak ada data Dinamis.
- Kemampuan teknis: tab browser kedua pada sesi akun yang sama (objek asersi), logout dan login ulang akun yang sama. Tab kedua ditutup sebelum Logout; hook `after` mengembalikan sesi ke akun default suite.
- State global: tidak ada yang diubah; pilihan Sidebar dan sub-tab tidak disimpan oleh perilaku yang diuji.

## Test Steps

### TC-AC-DN-626: Klik ulang menu Settings > Device dan tab baru memulai sub-tab dari Device Name dan Sidebar dari default All

1. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
2. Pilih node `Antenna` pada Category Sidebar
3. Klik sub-tab `Device SKU`
4. Klik menu `Settings > Device` pada sidebar navigasi
5. Verifikasi sub-tab `Device Name` aktif (kembali ke default, bukan `Device SKU`)
6. Verifikasi tidak ada node yang terpilih di Category Sidebar (kembali ke All)
7. Verifikasi pohon Category pada state expand awal
8. Verifikasi List memuat 130 baris dengan halaman 1 mulai dari Barcode Station
9. Expand `Hardware` lalu `Smart Fixed Reader` pada Category Sidebar
10. Pilih kembali node `Antenna` pada Category Sidebar
11. Buka tab browser baru dengan halaman `Settings > Device > Device Name`
12. Verifikasi di tab baru: tidak ada node yang terpilih (All)
13. Verifikasi di tab baru: List memuat 130 baris
14. Beralih ke tab pertama
15. Verifikasi tab pertama tetap memilih node `Antenna`
16. Verifikasi tab pertama memuat dua baris: Door Antenna, Gate Antenna
17. Tutup tab baru
18. Logout
19. Login ulang sebagai akun yang sama (`Fixture.settings-device-name.totalControl`, password `Spectra.env.AC_TC_PASSWORD`)
20. Buka halaman `Settings > Device > Device Name`
21. Verifikasi setelah login ulang tidak ada node yang terpilih (All)
22. Verifikasi setelah login ulang pohon Category pada state expand awal
23. Verifikasi setelah login ulang List memuat 130 baris

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Kelas harness c (multi-konteks): tab browser baru adalah objek asersi (Expected butir b dan c), sehingga TC-AC-DN-626 berada di spec sendiri dan tidak digabung dengan spec fungsional Sidebar.
- Langkah penghubung (S-03, S-09): langkah 17 menutup tab kedua sebelum Logout.
- Langkah 18 sampai 20 (Logout, login ulang, buka halaman) mengikuti langkah TC (login ulang dengan akun yang sama), bukan ganti akun; password hanya lewat `Spectra.env.AC_TC_PASSWORD`.
- Total baris 130 pada Expected TC diturunkan dari seeding (Pre-setup #16, #17, #23).
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
