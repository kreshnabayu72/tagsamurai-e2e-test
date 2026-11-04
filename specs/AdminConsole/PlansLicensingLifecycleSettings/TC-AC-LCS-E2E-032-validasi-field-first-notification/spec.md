---
id: TC-AC-LCS-E2E-032-validasi-field-first-notification
title: "Validasi Field First Notification"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-110
  - TC-AC-LCS-111
  - TC-AC-LCS-112
  - TC-AC-LCS-113
  - TC-AC-LCS-114
coverage:
  web: automated
---

# Validasi Field First Notification

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

### TC-AC-LCS-110: Field First Notification menolak karakter non-numerik

1. Klik di akhir nilai field First Notification
2. Ketik karakter `a`, `b`, `-`, `.`, `e`, `+` satu per satu
3. Verifikasi Karakter non-numerik tidak tampil pada field First Notification
4. Verifikasi Nilai First Notification tetap `7`
5. Verifikasi Tidak ada pesan error
6. Verifikasi `[Save]` tetap disabled

### TC-AC-LCS-111: Field First Notification dikosongkan: placeholder tampil dan blur mengisi otomatis nilai minimum

7. Pilih seluruh isi field First Notification (Ctrl+A) lalu tekan Delete
8. Verifikasi Placeholder "Enter first notification" tampil pada field kosong
9. Klik area kosong di luar field (blur)
10. Verifikasi Field terisi otomatis `1`
11. Verifikasi Tidak ada pesan error rentang nilai
12. Verifikasi Inline error (severity danger) pada field First Notification: "First notification must be greater than second notification"
13. Verifikasi `[Save]` disabled
14. Kembalikan First Notification ke nilai tersimpan `7`

### TC-AC-LCS-112: Field First Notification diisi 0 (di bawah minimum 1) menampilkan error rentang

15. Pilih seluruh isi field First Notification lalu ketik `0`
16. Klik area kosong di luar field (blur)
17. Verifikasi Inline error text (severity danger) di bawah field First Notification: "Value must be between 1 and 364"
18. Verifikasi `[Save]` disabled
19. Verifikasi Pesan relasi "First notification must be greater than second notification" tidak tampil (pesan rentang ditampilkan lebih dulu daripada pesan relasi)
20. Kembalikan First Notification ke nilai tersimpan `7`

### TC-AC-LCS-113: Field First Notification diisi 365 (di atas maksimum 364) menampilkan error rentang

21. Pilih seluruh isi field First Notification lalu ketik `365`
22. Klik area kosong di luar field (blur)
23. Verifikasi Inline error text (severity danger) di bawah field First Notification: "Value must be between 1 and 364"
24. Verifikasi `[Save]` disabled

### TC-AC-LCS-114: Save First Notification pada nilai maksimum 364

25. Ubah First Notification menjadi `364`, lalu klik area kosong di luar field (blur)
26. Verifikasi Tidak ada pesan error rentang pada First Notification saat nilai `364` diisi
27. Klik `[Save]`
28. Verifikasi Toast sukses: "Success, trial settings have been saved."
29. Verifikasi `[Save]` disabled setelah tab refresh
30. Muat ulang halaman dengan F5
31. Klik tab Trial Settings pada tab bar
32. Verifikasi First Notification bernilai `364` (nilai tersimpan)

## Notes

- Urutan TC dalam spec: kasus tanpa Save dan validasi yang diblokir lebih dulu, kasus Save pada nilai maksimum terakhir (bagian 3 prinsip 7 dan 9). Satu pembukaan tab untuk semua kasus tanpa Save; field ditimpa oleh langkah "pilih seluruh isi field" pada tiap TC, dan kasus Save memakai tab yang dibuka hook `beforeEach` suite. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Langkah penghubung (S-03, S-09): langkah "Kembalikan ... ke nilai tersimpan" (bila ada) membersihkan error inline yang identik sebelum TC berikutnya (R-12); klik tab Trial Settings sesudah F5 adalah langkah "buka kembali tab" TC (tab tetap Trial Settings menurut route, sehingga klik ini tidak mengubah tab).
- Temuan untuk QA: Post Condition "tersimpan" pada TC Save tidak punya langkah observasi sendiri selain Expected butir c (nilai sesudah F5); spec mengasersi nilai tersimpan sesudah F5 sesuai Expected, bukan dari Post Condition. TC "buka kembali tab" tidak menyebut tab mana; spec memakai tab Trial Settings.
- Temuan untuk QA: TC 111 butir c ("tidak ada pesan error rentang nilai") dan butir d (error relasi pada nilai auto-fill `1` terhadap Second Notification `1`) memakai tanda baca berbeda dari TC 96, 101, dan 106 ("tidak ada pesan error"); spec mengikuti masing-masing TC. TC 112 butir a memuat klausa tambahan "pesan rentang ditampilkan lebih dulu daripada pesan relasi"; spec menulisnya sebagai `Verifikasi` pesan relasi tidak tampil sesudah pesan rentang tampil (anchor positif).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
- Langkah 25 menyertakan blur sesuai TC ("lalu blur") sebelum asersi absence pada langkah 26, karena validasi rentang muncul saat blur (bagian 8b butir 2).
