---
id: TC-FA-TDC-E2E-088-restore-default-classes-gagal-5xx-saving-state-dan-klik-ganda
title: "Restore Default Classes: Gagal 5xx, Saving State Tombol Restore, dan Klik Ganda Tidak Membuat Class Dobel"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-333
  - TC-FA-TDC-334
  - TC-FA-TDC-335
coverage:
  web: automated
---

# Restore Default Classes: Gagal 5xx, Saving State Tombol Restore, dan Klik Ganda Tidak Membuat Class Dobel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Data: tabel Tax Depreciation Class tanpa class sama sekali: di hook `before` seluruh class company uji dihapus lewat seeding API (company yang disediakan tim FE khusus automation) sebelum `beforeEach` membuka halaman, sehingga Empty State tampil. Hook `after` memulihkan tujuh class seed bawaan lewat seeding API (`suite.md`). Antar blok, tabel dikosongkan lagi lewat seeding API (langkah penghubung 15).
- Kemampuan intercept jaringan (`Spectra.intercept()`) di atas backend nyata (Mode FE+BE karena asersi memuat state server) untuk (1) mengembalikan 500 pada endpoint restore (TC-333) dan (2) menunda respons endpoint restore 3 detik (TC-335). Nama endpoint restore tidak tertulis di TC dan disediakan tim FE/BE (S-13). Intercept dilepas segera setelah pemicu selesai (langkah 5 dan 15).
- Kemampuan teknis: mengosongkan seluruh class lewat API; klik ganda cepat.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-333: Restore gagal 5xx

1. Klik `Restore default classes`
2. Atur endpoint restore mengembalikan 500 (intercept jaringan)
3. Klik `[Restore]`
4. Verifikasi toast error "Error, failed to restore default classes."
5. Lepas intercept endpoint restore
6. Verifikasi dialog D-12 tetap terbuka dengan pratinjau yang sama
7. Verifikasi tombol `[Restore]` enabled kembali
8. Klik `[Cancel]`

### TC-FA-TDC-335: Tombol Restore masuk Saving state

9. Atur respons endpoint restore ditunda 3 detik (intercept jaringan)
10. Klik `Restore default classes`
11. Klik `[Restore]` lalu amati dialog selama request
12. Verifikasi tombol `[Restore]` menampilkan spinner
13. Verifikasi tombol `[Restore]` tidak dapat diklik
14. Verifikasi tombol `[Cancel]` tidak interaktif selama request
15. Lepas tahanan respons endpoint restore
16. Tunggu aksi selesai
17. Kosongkan seluruh class lewat seeding API, lalu muat ulang halaman

### TC-FA-TDC-334: Klik ganda cepat pada Restore

18. Klik `Restore default classes`
19. Klik `[Restore]` dua kali dengan cepat
20. Verifikasi satu toast sukses "Success, default classes have been restored."
21. Verifikasi tabel memuat tepat tujuh class, tanpa duplikat kode

## Notes

- P-5 (butir b): TC-333 adalah satu TC objek-uji ringan kelas b (satu kegagalan 5xx pada Restore) pada permukaan yang sama dengan TC-334 dan TC-335 (dialog D-12 Restore); tanpa harness eksternal dan tanpa state berat sendiri.
- Urutan TC-333, 335, 334 (TC-335 sebelum TC-334): setelah TC-333 dialog D-12 masih terbuka pada tabel kosong, sehingga TC-335 yang menunda respons berikutnya langsung memakai tabel kosong itu; sesudah TC-335 berhasil membuat tujuh class, tabel dikosongkan lagi (langkah 17) agar TC-334 memulai dari Empty State.
- Langkah penghubung (S-03): langkah 8 (`[Cancel]` menutup D-12 agar TC-335 mengikuti urutan langkah TC dari tombol `Restore default classes`), langkah 15 (melepas tahanan respons setelah ketiga asersi state Saving selesai, 8b.5), langkah 16 ("Tunggu aksi selesai", 8b.8), langkah 17 (mengosongkan tabel dan muat ulang).
- Intercept 500 dilepas di langkah 5 segera setelah pemicu (S-09).
- Post Condition TC-333 ("tidak ada class dibuat", "tidak ada entri log") dan TC-334 ("tepat tujuh entri L-01 per surface") tidak punya langkah observasi di TC; "tidak ada class dibuat" TC-333 diamati lewat Empty State yang masih tersedia pada langkah 6 (dialog tetap di atas tabel kosong), entri log tidak diasersi (S-01).
- Temuan untuk QA:
  - Post Condition TC-333 dan TC-334 tanpa langkah observasi di TC.
  - Email akun Total Control tidak tertulis di TC.
