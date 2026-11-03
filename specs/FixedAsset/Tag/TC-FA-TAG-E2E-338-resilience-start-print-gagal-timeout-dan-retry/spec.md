---
id: TC-FA-TAG-E2E-338-resilience-start-print-gagal-timeout-dan-retry
title: "Resilience: Start Print Gagal (5xx dan Timeout) Mempertahankan Dialog Print QR dan Retry Berhasil"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-495
  - TC-FA-TAG-496
  - TC-FA-TAG-497
coverage:
  web: automated
---

# Resilience: Start Print Gagal (5xx dan Timeout) Mempertahankan Dialog Print QR dan Retry Berhasil

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) `Spectra.intercept` parsial atas request Start Print: respons 5xx, tidak ada respons sampai timeout, dan 5xx hanya pada percobaan pertama lalu diteruskan ke backend nyata; hook `after` melepas semua intercept; (2) pengamatan dialog cetak browser (untuk memastikan dialog tidak terbuka, dan untuk menutup dialog yang terbuka pada langkah 30); (3) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog Print QR lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup: tanpa data khusus (Print QR hanya memakai tab Paired). `Quantity` 3 dan `Start position` `Right` hanya dipakai TC-FA-TAG-495.
- State yang diubah dan pemulihannya: langkah 27 membuat satu batch kode QR (TC-FA-TAG-497) yang tidak dapat dibatalkan lewat UI; tidak ada pemulihan yang tersedia (lihat Temuan untuk QA). Semua intercept dilepas di langkah 12, 20, dan 31, dan hook `after` melepas intercept yang tersisa walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-495: Start Print gagal 5xx

1. Klik tombol `Print QR` di toolbar tab Paired
2. Isi `Quantity` dengan 3
3. Pilih `Right` pada `Start position`
4. Pasang intercept 5xx pada request Start Print
5. Klik [Start Print]
6. Verifikasi Toast "Error, failed to print QR labels."
7. Verifikasi dialog cetak browser tidak terbuka
8. Verifikasi dialog Print QR tetap terbuka
9. Verifikasi `Quantity` 3 dan `Right` dipertahankan
10. Verifikasi state loading pada [Start Print] berhenti
11. Verifikasi tombol [Start Print] dapat ditekan lagi
12. Lepas intercept
13. Muat ulang halaman (F5)

### TC-FA-TAG-496: Start Print timeout

14. Pasang intercept: server tidak merespons sampai timeout pada request Start Print
15. Klik tombol `Print QR` di toolbar tab Paired
16. Klik [Start Print]
17. Verifikasi Toast "Error, failed to print QR labels."
18. Verifikasi dialog Print QR tetap terbuka
19. Verifikasi loading pada [Start Print] berhenti
20. Lepas intercept
21. Muat ulang halaman (F5)

### TC-FA-TAG-497: Retry Start Print berhasil

22. Pasang intercept 5xx pada request Start Print hanya untuk percobaan pertama; percobaan berikutnya diteruskan ke backend
23. Klik tombol `Print QR` di toolbar tab Paired
24. Klik [Start Print]
25. Verifikasi Toast "Error, failed to print QR labels."
26. Tunggu toast lama hilang otomatis
27. Klik [Start Print] lagi
28. Verifikasi Toast "Success, QR labels have been sent to print."
29. Verifikasi dialog Print QR menutup
30. Tutup dialog cetak browser yang terbuka oleh percobaan kedua
31. Lepas intercept

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-495 s.d. 497). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-494 (Start Print ditekan beruntun) ada di spec 342. Kegagalan sisi izin dan state tenant pada Start Print ada di spec 325 s.d. 326 dan 349.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 12, 20, dan 31 (melepas intercept), 13 dan 21 (muat ulang halaman untuk menutup dialog Print QR yang berisi isian; dialog `beforeunload` ditangani sesuai Prerequisites), 26 (menunggu toast kegagalan hilang sebelum toast sukses diasersi), 30 (menutup dialog cetak browser).
- Langkah 7 (dialog cetak browser tidak terbuka) didahului `Verifikasi` Toast di langkah 6 sebagai anchor positif (respons server sudah diproses).
- Temuan untuk QA:
  - TC-FA-TAG-497 berlabel "Manual Only" karena dialog cetak browser adalah dialog tingkat OS; spec mengasersi Toast sukses dan dialog Print QR menutup (Expected TC) dan menutup dialog cetak browser lewat kemampuan pengamatan dialog cetak yang disediakan tim FE.
  - Post Condition TC-FA-TAG-495 dan 496 ("Tidak ada kode QR yang dibuat") dan TC-FA-TAG-497 ("Satu batch kode QR dibuat dari percobaan kedua") tanpa langkah observasi di TC tidak diasersi.
  - Batch kode QR yang dibuat langkah 27 (TC-FA-TAG-497) tidak punya cara pemulihan di TC; spec tidak menghapusnya.
  - TC-FA-TAG-496 dan TC-FA-TAG-497 tidak mengisi `Quantity`; spec mengikuti TC (nilai bawaan dialog).
  - Nama dan kode literal Pre-setup tidak dipakai di spec ini; Lampiran A belum memuat butir modul ini.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; spec ini tidak memakai kunci fixture.
