---
id: TC-AC-DN-E2E-107-filter-apply-clear-dan-penutupan-panel
title: "Filter Panel List: Reset Halaman, Clear Field, Tutup Panel Tanpa Apply, dan Indikator Titik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-310
  - TC-AC-DN-311
  - TC-AC-DN-312
  - TC-AC-DN-313
  - TC-AC-DN-314
coverage:
  web: automated
---

# Filter Panel List: Reset Halaman, Clear Field, Tutup Panel Tanpa Apply, dan Indikator Titik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #15 Brand `Brand A`, `Brand B`; #16 Device Name inti beserta SKU-nya (`Gate Antenna`, `NFC Tag`, `RFID Reader` ber-Brand A; `Barcode Station` ber-Measurement `Unit`; `Tag Reel` ber-Measurement `Meter`); #17 seed 120 baris. Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Filter yang di-Apply dilepas lewat `[Clear Field]` lalu `[Apply]` di akhir spec. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-310: Apply Filter dari halaman lebih dari 1 kembali ke halaman 1

1. Klik tombol halaman berikutnya
2. Klik ikon Filter lalu klik field `Measurement`, centang `Unit`
3. Klik `[Apply]`
4. Verifikasi hasil filter tampil mulai halaman 1 (Barcode Station sebagai baris pertama)
5. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-311: Clear Field lalu Apply melepas filter yang aktif

6. Klik ikon Filter, klik field `Brand`, centang `Brand A`, lalu klik `[Apply]`
7. Klik ikon Filter
8. Klik `[Clear Field]`
9. Verifikasi chip `Brand A` hilang dari field
10. Verifikasi tabel belum berubah (tetap 3 baris)
11. Klik `[Apply]`
12. Verifikasi tabel menampilkan 130 baris
13. Verifikasi halaman 1 menampilkan Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
14. Verifikasi indikator filter aktif pada ikon Filter hilang

### TC-AC-DN-312: Menutup panel lewat ikon Filter tanpa Apply membuang perubahan

15. Klik ikon Filter, klik field `Brand`, centang `Brand A`, lalu klik `[Apply]`
16. Klik ikon Filter, klik field `Brand`, centang tambahan `Brand B` tanpa menekan `[Apply]`
17. Klik ikon Filter (panel menutup)
18. Verifikasi tabel tetap menampilkan 3 baris dari filter `Brand A`
19. Klik ikon Filter (panel terbuka kembali)
20. Verifikasi panel menampilkan hanya chip `Brand A` (centang `Brand B` dibuang)

### TC-AC-DN-313: Menutup panel lewat klik di luar panel tanpa Apply membuang perubahan

21. Klik field `Brand`, centang tambahan `Brand B` tanpa menekan `[Apply]`
22. Klik area kosong di luar panel (panel menutup)
23. Verifikasi tabel tetap menampilkan 3 baris dari filter `Brand A`
24. Klik ikon Filter (panel terbuka kembali)
25. Verifikasi panel menampilkan hanya chip `Brand A` (centang `Brand B` dibuang)

### TC-AC-DN-314: Titik indikator pada ikon Filter selama ada filter ter-Apply

26. Klik `[Clear Field]`, lalu klik `[Apply]`
27. Klik ikon Filter, klik field `Measurement`, centang `Meter`, lalu klik `[Apply]`
28. Verifikasi ikon Filter menampilkan badge titik tanpa angka saat panel tertutup
29. Klik ikon Filter
30. Verifikasi ikon Filter menampilkan badge titik tanpa angka saat panel terbuka
31. Klik `[Clear Field]`, lalu klik `[Apply]`
32. Verifikasi badge titik pada ikon Filter hilang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 5 dan 31 melepas filter yang di-Apply; langkah 26 melepas filter `Brand A` yang masih aktif dari TC-AC-DN-312 dan TC-AC-DN-313 sebelum TC-AC-DN-314 membangun filter `Measurement` sendiri. Filter `Brand A` yang di-Apply pada langkah 15 tetap aktif untuk TC-AC-DN-313, sehingga TC itu tidak mengulang Apply `Brand A`.
- Urutan: mengikuti sourceTc; Apply dan Clear di awal, lalu penutupan panel tanpa Apply, lalu indikator titik di akhir.
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-313 meng-Apply `Brand A` sebagai langkah awalnya sendiri; spec memakai filter `Brand A` yang masih aktif dari TC-AC-DN-312 (state yang sama).
  - TC-AC-DN-314 menulis dua klik ikon Filter (menutup lalu membuka panel) sesudah Apply, yang bertentangan dengan asumsi panel menutup setelah Apply; spec memakai satu klik pembuka (langkah 29) sebelum asersi titik saat panel terbuka.
