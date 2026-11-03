---
id: TC-AC-DN-E2E-006-popup-more-keyboard-dan-tutup
title: "Popup +N more: Keyboard, Klik Luar, Hover, dan Daftar Polos"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-269
  - TC-AC-DN-270
  - TC-AC-DN-271
  - TC-AC-DN-596
coverage:
  web: automated
---

# Popup +N more: Keyboard, Klik Luar, Hover, dan Daftar Polos

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16) `RFID Reader` dengan tiga Brand (`Brand A`, `Brand B`, `Brand C`); daftar default tanpa Search, Filter, atau Sidebar. Baca-saja; tidak ada data Dinamis.
- Kemampuan teknis: navigasi Tab, Enter, dan Esc; klik area di luar popup; hover tanpa gerak selama 2 detik.

## Test Steps

### TC-AC-DN-269: Chip +N more dapat dibuka lewat keyboard

1. Tekan Tab berulang hingga fokus berada pada chip `+1 more` di sel Brand baris `RFID Reader`
2. Verifikasi chip `+1 more` dapat menerima fokus keyboard (menampilkan indikator fokus)
3. Tekan Enter
4. Verifikasi popup daftar Brand tampil
5. Tekan Esc untuk menutup popup

### TC-AC-DN-270: Klik di luar popup +N more menutup popup

6. Klik chip `+1 more` pada sel Brand baris `RFID Reader`
7. Verifikasi popup daftar Brand tampil
8. Klik area di luar popup
9. Verifikasi popup daftar Brand tertutup setelah klik di luar popup
10. Verifikasi List tampil tanpa perubahan
11. Verifikasi klik di luar popup tidak memicu aksi lain pada baris `RFID Reader` (tidak ada dialog atau popup lain yang terbuka)

### TC-AC-DN-271: Hover pada chip +N more tidak membuka popup

12. Verifikasi chip `+1 more` pada sel Brand baris `RFID Reader` tampil
13. Arahkan kursor ke chip `+1 more` pada sel Brand baris `RFID Reader` selama 2 detik
14. Verifikasi popup daftar Brand tidak tampil saat hover
15. Klik chip `+1 more` pada sel Brand baris `RFID Reader`
16. Verifikasi popup daftar Brand tampil setelah chip diklik
17. Tekan Esc untuk menutup popup

### TC-AC-DN-596: Popup +N more kolom Brand berupa daftar polos tanpa pencarian dan tanpa pagination

18. Klik chip `+1 more` pada kolom Brand baris `RFID Reader`
19. Verifikasi popup berjudul "Brand" (nama kolom)
20. Verifikasi popup memuat seluruh nilai Brand baris itu sebagai daftar polos: `Brand A`, `Brand B`, `Brand C`
21. Verifikasi popup tanpa kolom pencarian, tanpa filter, dan tanpa pagination
22. Verifikasi daftar berurutan alfabetis
23. Arahkan kursor ke nilai pada popup
24. Verifikasi tidak ada tooltip pada nilai di popup
25. Tekan Esc
26. Verifikasi popup tertutup lewat Esc
27. Klik chip `+1 more` pada kolom Brand baris `RFID Reader`
28. Klik ikon `[X]` pada popup
29. Verifikasi popup tertutup lewat `[X]`
30. Klik chip `+1 more` pada kolom Brand baris `RFID Reader`
31. Klik area di luar popup
32. Verifikasi popup tertutup lewat klik di luar popup

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Semua TC tanpa aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5 dan 17 menutup popup antar-TC.
- TC-AC-DN-271: Expected butir b ("Popup hanya tampil setelah chip diklik") diasersi lewat langkah 15 (klik chip) dan `Verifikasi` sesudahnya; langkah klik itu tidak ada di langkah TC (lihat Temuan untuk QA).
- TC-AC-DN-596: Expected butir d ("X dan klik di luar popup juga menutupnya") diasersi dengan membuka popup dua kali lagi (langkah 27 sampai 32); TC-AC-DN-267 dan TC-AC-DN-270 mengasersi penutupan lewat `[X]` dan klik luar pada surface yang sama.
- Temuan untuk QA:
  - TC-AC-DN-271 menyebut Expected "Popup hanya tampil setelah chip diklik" tanpa langkah klik di kolom Langkah Uji; spec menambahkan klik sebagai langkah observasi Expected itu.
