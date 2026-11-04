---
id: TC-AC-LCS-E2E-029-validasi-field-max-trial-duration
title: "Validasi Field Max Trial Duration"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-95
  - TC-AC-LCS-96
  - TC-AC-LCS-97
  - TC-AC-LCS-98
  - TC-AC-LCS-99
coverage:
  web: automated
---

# Validasi Field Max Trial Duration

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-95: Field Max Trial Duration menolak karakter non-numerik

1. Klik di akhir nilai field Max Trial Duration
2. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
3. Verifikasi Karakter non-numerik tidak tampil pada field Max Trial Duration
4. Verifikasi Nilai Max Trial Duration tetap `30`
5. Verifikasi Tidak ada pesan error
6. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-96: Field Max Trial Duration dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

7. Pilih seluruh isi field Max Trial Duration (Ctrl+A) lalu tekan Delete
8. Verifikasi Placeholder "Enter max trial duration" tampil pada field kosong
9. Klik area kosong di luar field (blur)
10. Verifikasi Field terisi otomatis `1`
11. Verifikasi Tidak ada pesan error
12. Verifikasi `[Save]` enabled (nilai berbeda dari nilai tersimpan)

### TC-AC-LCS-97: Field Max Trial Duration diisi 0 (di bawah minimum 1) menampilkan error rentang

13. Pilih seluruh isi field Max Trial Duration lalu ketik `0`
14. Klik area kosong di luar field (blur)
15. Verifikasi Inline error text (severity danger) di bawah field Max Trial Duration: "Value must be between 1 and 365"
16. Verifikasi `[Save]` disabled
17. Kembalikan Max Trial Duration ke nilai tersimpan `30`

### TC-AC-LCS-98: Field Max Trial Duration diisi 366 (di atas maksimum 365) menampilkan error rentang

18. Pilih seluruh isi field Max Trial Duration lalu ketik `366`
19. Klik area kosong di luar field (blur)
20. Verifikasi Inline error text (severity danger) di bawah field Max Trial Duration: "Value must be between 1 and 365"
21. Verifikasi `[Save]` disabled

### TC-AC-LCS-99: Save Max Trial Duration pada nilai maksimum 365

22. Ubah Max Trial Duration menjadi `365`, lalu klik area kosong di luar field (blur)
23. Verifikasi Tidak ada pesan error rentang pada Max Trial Duration saat nilai `365` diisi
24. Klik `[Save]`
25. Verifikasi Toast sukses: "Success, trial settings have been saved."
26. Verifikasi `[Save]` disabled setelah tab refresh
27. Muat ulang halaman dengan F5
28. Klik tab Trial Settings pada tab bar
29. Verifikasi Max Trial Duration bernilai `365` (nilai tersimpan)

## Notes

- Urutan TC dalam spec: kasus tanpa Save dan validasi yang diblokir lebih dulu, kasus Save pada nilai maksimum terakhir (bagian 3 prinsip 7 dan 9). Satu pembukaan tab untuk semua kasus tanpa Save; field ditimpa oleh langkah "pilih seluruh isi field" pada tiap TC, dan kasus Save memakai tab yang dibuka hook `beforeEach` suite. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Langkah penghubung (S-03, S-09): langkah "Kembalikan ... ke nilai tersimpan" (bila ada) membersihkan error inline yang identik sebelum TC berikutnya (R-12); klik tab Trial Settings sesudah F5 adalah langkah "buka kembali tab" TC (tab tetap Trial Settings menurut route, sehingga klik ini tidak mengubah tab).
- Temuan untuk QA: Post Condition "tersimpan" pada TC Save tidak punya langkah observasi sendiri selain Expected butir c (nilai sesudah F5); spec mengasersi nilai tersimpan sesudah F5 sesuai Expected, bukan dari Post Condition. TC "buka kembali tab" tidak menyebut tab mana; spec memakai tab Trial Settings.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
- Langkah 22 menyertakan blur sesuai TC ("lalu blur") sebelum asersi absence pada langkah 23, karena validasi rentang muncul saat blur (bagian 8b butir 2).
