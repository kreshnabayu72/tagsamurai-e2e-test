---
id: TC-AC-CS-E2E-163-resilience-retry-setelah-timeout-dan-toast-error-bertahan
title: "Resilience: Retry Setelah Timeout dan Toast Error Bertahan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-CS-521
  - TC-AC-CS-563
coverage:
  web: automated
---

# Resilience: Retry Setelah Timeout dan Toast Error Bertahan

## Prerequisites

- Mode: FE+BE. Spec memaksa sebagian respons Submit lewat `Spectra.intercept()` di atas backend nyata (bagian 6); `Mode: mock` tidak dipakai karena modul ini tidak punya `openapi.yaml` maupun LLD sebagai sumber daftar endpoint (R-15, S-13).
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-163`): Client `C521` dan Client `C563` (setara `Client Tanpa Subscription`, Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial). Nilai form Add Subscription (Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`) dirujuk lewat `Fixture.license-allocation-subscription.addForm163`; term yang terbentuk pada langkah 4 dan 22 dibersihkan di hook `after`.
- Kebutuhan intercept (parsial, disediakan tim FE; endpoint Submit Add Subscription dinamai TC, path-nya tidak tertulis di TC, PRD, atau LLD): TC-AC-CS-521 menahan respons Submit melewati timeout klien sementara request tetap diteruskan ke server (percobaan pertama tersimpan); TC-AC-CS-563 memaksa respons Submit 500. Intercept dilepas segera setelah dipakai (S-09).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah term per Client dan Product lewat fixture BE. Jeda pendek 10 detik pada langkah 18 adalah pilihan spec (jeda nyata di bawah ±30 detik, bagian 6); jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-521: Retry setelah timeout tidak menduplikasi term

1. Klik `[+ Subscription]`
2. Pilih Client `C521`, isi form Add Subscription dari `Fixture.license-allocation-subscription.addForm163`
3. Tahan respons Submit melewati timeout klien lewat `Spectra.intercept()`, request tetap diteruskan ke server
4. Klik `[Submit]`
5. Tunggu error timeout tampil (batas tunggu 2 menit)
6. Lepas intercept respons Submit
7. Klik `[Submit]` lagi
8. Verifikasi percobaan kedua ditolak dengan pesan "This client already has an active subscription for this product."
9. Verifikasi hanya satu term yang terbentuk untuk Client `C521` dan Product `SAMS`
10. Klik `✕` pada modal
11. Verifikasi dialog `Unsaved Changes` tampil
12. Klik `[Leave]`

### TC-AC-CS-563: Toast error bertahan sampai di-dismiss dan toast baru menggantikan toast lama

13. Klik `[+ Subscription]`
14. Pilih Client `C563`, isi form Add Subscription dari `Fixture.license-allocation-subscription.addForm163`
15. Paksa respons Submit gagal 500 lewat `Spectra.intercept()`
16. Klik `[Submit]`
17. Verifikasi toast error "Error, failed to add subscription." berada di kanan bawah layar
18. Tunggu 10 detik tanpa interaksi
19. Verifikasi toast error tetap tampil setelah 10 detik
20. Verifikasi toast error hanya dapat hilang lewat dismiss manual (tidak hilang otomatis)
21. Lepas intercept respons Submit
22. Klik `[Submit]`
23. Verifikasi toast sukses "Success, subscription has been added." menggantikan toast error pada slot yang sama (hanya satu toast tampil)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-172, 173, 209, dan 266 (gagal tulis Add, Renew, Activate Trial, Cancel Subscription) ada di spec 140.
- Langkah penghubung (S-03): langkah 6 dan 21 (melepas intercept segera setelah dipakai, S-09), langkah 10 sampai 12 (menutup form dirty, S-08), langkah 18 (jeda 10 detik tanpa `Verifikasi`).
- Langkah 8 (percobaan kedua ditolak) mendahului langkah 9 (hitungan term lewat fixture BE): pesan penolakan menandai respons percobaan kedua selesai diproses sebelum hitungan dibaca; percobaan pertama sudah tersimpan di server.
- Temuan untuk QA:
  - TC-AC-CS-521 tidak menyebut durasi timeout klien maupun teks error timeout; spec menunggu error tampil tanpa mengasersi teksnya (S-02).
  - TC-AC-CS-521 tidak menyebut isi form Add; dirujuk lewat fixture.
  - TC-AC-CS-563 Expected b ("hanya hilang lewat dismiss manual") tidak punya langkah dismiss pada TC dan kondisinya sama dengan Expected a; spec mengasersinya sebagai klausa terpisah pada langkah 20 tanpa menambah langkah dismiss.
  - TC-AC-CS-563 tidak menyebut apakah toast sukses perlu di-dismiss sesudah langkah 23; spec tidak menambahnya.
