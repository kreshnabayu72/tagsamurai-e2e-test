---
id: TC-AC-LA-E2E-010-modal-allocation-log-loading-dan-immutability
title: "Modal Allocation Log: Loading dan Immutability Entri"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-45
  - TC-AC-LA-414
coverage:
  web: automated
---

# Modal Allocation Log: Loading dan Immutability Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini kecuali dinyatakan lain; data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca: #55 alokasi dengan riwayat log lengkap (Allocation ID `Fixture.license-allocation-license.seed55`).
- Kemampuan teknis: `Spectra.intercept()` atas respons log License Allocation di atas backend nyata (tunda 5 detik; endpoint GET log tidak tertulis di TC dan ditulis tim FE, S-13); klien HTTP/fixture BE dengan sesi API akun `totalControlLic` untuk request langsung ubah dan hapus entri log (endpoint tidak tertulis di TC, disediakan tim FE/BE tanpa endpoint karangan); baca entri Allocation Log record lewat fixture BE.
- State yang diubah: intercept respons log dilepas segera sesudah TC-AC-LA-45 (S-09). Request langsung yang diuji ditolak server dan tidak mengubah data.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-45: Loading modal Allocation Log

1. Ketik Search Allocation ID seed riwayat lengkap (`Fixture.license-allocation-license.seed55`), tekan Enter
2. Pasang intercept respons log: tunda 5 detik
3. Klik ikon `⋯` pada baris itu, lalu klik `Allocation Log`
4. Amati isi modal
5. Verifikasi komponen Loading tampil di daftar log
6. Verifikasi header modal tetap tampil
7. Lepas tahanan respons log dan tunggu daftar log selesai dimuat

### TC-AC-LA-414: Entri Allocation Log immutable dan record tidak punya Delete

8. Verifikasi sedikitnya satu entri log tampil pada modal Allocation Log
9. Verifikasi tidak ada kontrol ubah atau hapus entri pada modal
10. Baca jumlah dan isi entri Allocation Log record lewat fixture BE sebagai baseline
11. Kirim request ubah entri log langsung ke server dengan sesi API akun `totalControlLic`
12. Verifikasi server menolak request ubah entri log
13. Kirim request hapus entri log langsung ke server dengan sesi API akun `totalControlLic`
14. Verifikasi server menolak request hapus entri log
15. Baca jumlah dan isi entri Allocation Log record lewat fixture BE
16. Verifikasi jumlah dan isi entri sama dengan baseline (log record tetap utuh)
17. Tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah memasang dan melepas intercept, langkah `Amati`, langkah membaca baseline lewat fixture BE, dan penutupan modal.
- K-1: TC-AC-LA-414 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap masuk spec FE+BE dan asersinya hanya status respons dan state data lewat fixture BE (bagian 8b butir 1).
- P-5: TC-AC-LA-414 adalah objek uji ringan kelas a (tanpa harness eksternal dan tanpa state berat) yang berada di spec fungsional dengan permukaan yang sama (modal Allocation Log); TC-AC-LA-45 bukan kelas b (menahan respons untuk mengamati state Loading).
- Temuan untuk QA:
  - TC-AC-LA-414 langkah 2 (`Kirim request ubah atau hapus entri langsung`) tidak menyebut endpoint, metode, atau akun pengirim; spec memakai sesi API akun `totalControlLic` tanpa endpoint karangan.
  - TC-AC-LA-414 Expected a pertama (`Tidak ada kontrol ubah atau hapus entri`) adalah asersi absence tanpa anchor di TC; spec menambah `Verifikasi` sedikitnya satu entri log tampil sebagai anchor (bagian 8b butir 2).
  - TC-AC-LA-45 Data Uji menyebut `Intercept GET log: tunda 5 detik` tanpa endpoint; endpoint tidak dikarang di spec.
