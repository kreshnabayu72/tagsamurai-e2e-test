---
id: TC-AC-PF-E2E-170-pagination-tab-assigned-clients-nomor-tidak-valid-page
title: "Pagination Tab Assigned Clients: nomor halaman tidak valid, ganti page size, dan reset halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-441
  - TC-AC-PF-442
  - TC-AC-PF-443
coverage:
  web: automated
---

# Pagination Tab Assigned Clients: nomor halaman tidak valid, ganti page size, dan reset halaman

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang melakukan seeding volume besar serta memulihkan Dataset Plan Q ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan Q, custom plan `Paket Banyak Client` dengan 120 client bernama `PT Massal 001` sampai `PT Massal 120`. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`). Volume 100 baris atau lebih: kelas e (volume data).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Nomor halaman tidak valid (TC-AC-PF-441)

1. Klik tab `Custom`, sub-tab `Active`.
2. Buka Plan Detail `Paket Banyak Client` (klik nama plan `Paket Banyak Client`).
3. Klik Tab Assigned Clients.
4. Klik `Next` untuk pindah ke halaman 2.
5. Verifikasi tabel berada di halaman 2 (teks footer `Showing 11–20 of 120 entries`).
6. Ketik `0` pada input nomor halaman, tekan Enter.
7. Verifikasi input `0` diabaikan dan tabel tetap di halaman 2.
8. Ketik `999` pada input nomor halaman, tekan Enter.
9. Verifikasi input `999` diabaikan dan tabel tetap di halaman 2.
10. Ketik `abc` pada input nomor halaman, tekan Enter.
11. Verifikasi input `abc` diabaikan dan tabel tetap di halaman 2.

### Ganti page size (TC-AC-PF-442)

12. Klik Overlay Page Size, pilih `25`.
13. Verifikasi tabel kembali ke halaman 1.
14. Verifikasi page size 25 (`Rows per page: 25`).
15. Verifikasi teks footer `Showing 1–25 of 120 entries`.

### Reset halaman oleh Search dan Sort (TC-AC-PF-443)

16. Klik Overlay Page Size, pilih `10`.
17. Klik `Next` untuk pindah ke halaman 2.
18. Verifikasi tabel berada di halaman 2 (teks footer `Showing 11–20 of 120 entries`).
19. Klik header kolom pertama satu kali (sort ascending).
20. Verifikasi tabel tetap di halaman 2 (teks footer `Showing 11–20 of 120 entries`).
21. Ketik Search `Massal`, tekan Enter.
22. Verifikasi tabel kembali ke halaman 1.
23. Verifikasi teks footer `Showing 1–10 of 120 entries`.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 4 dan 17 (pindah ke halaman 2 yang disebut TC sebagai "Pindah ke halaman 2") serta langkah 16 (memulihkan page size 10 agar TC-AC-PF-443 berjalan pada page size default).
- Langkah 5 dan 18 menjadi baseline halaman sebelum langkah yang diasersi tidak mengubah halaman (S-14).
- Spec ini memakai kelas e (volume data, 120 baris) sebagai satu-satunya kelas harness; tidak ada pengecualian `P-n`.
- Temuan untuk QA:
  - Judul TC-AC-PF-443 menyebut "Apply Filter ... mereset halaman ke 1", tetapi langkah dan Expected hanya memuat Search; kasus Apply Filter tidak diasersi.
  - TC-AC-PF-443 menyebut teks `Showing 1–10 of 120 entries` setelah Search, sedangkan TC-AC-PF-442 meninggalkan page size 25; TC-AC-PF-443 diasumsikan berjalan pada page size default 10 sehingga spec memulihkannya pada langkah 16.
